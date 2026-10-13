#!/usr/bin/env python3
"""Learning-rate experiments vs BM25 top-3 baseline. Seed=42. Local only."""
from __future__ import annotations
import argparse, json, os, sys, time, traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from quiz_bank import ORIGINAL, HELDOUT, all_items, by_split
from grade import grade
from retrieval import (
    BM25, load_docs, chunk_baseline, chunk_heading_overlap,
    rrf_fuse, ollama_embed, DenseIndex, build_context,
)
from memory_store import MemoryStore
from ollama_client import generate, DEFAULT_MODEL

CORPUS = "/workspace/evals/data/gitbook-corpus"
OUT_DIR = Path("/workspace/learning-rate/results")
SEED = 42
MODEL = DEFAULT_MODEL

def ask(question: str, context: str | None, extra: str | None = None, num_predict: int = 128) -> dict:
    system = (
        "You answer questions about the Tessera mesh / Gitbook docs. "
        "Be concise and factual. Prefer short answers."
    )
    parts = []
    if context:
        parts.append(f"Use the following retrieved Gitbook doc excerpts if relevant.\n\nCONTEXT:\n{context}")
    if extra:
        parts.append(extra)
    parts.append(f"QUESTION: {question}\n\nShort answer:")
    prompt = "\n\n".join(parts)
    return generate(prompt, model=MODEL, system=system, num_predict=num_predict, num_ctx=3072, temperature=0.0)

def rewrite_queries(question: str, n: int = 2) -> list[str]:
    """LLM multi-query rewrite; always includes original."""
    prompt = (
        f"Rewrite the search query into {n} short alternative keyword queries for BM25 over Tessera/Gitbook docs. "
        f"One alternative per line. No numbering. No explanations.\n\nQuery: {question}"
    )
    out = generate(prompt, model=MODEL, system="You expand search queries. Output only queries.",
                   num_predict=80, num_ctx=1024, temperature=0.2)
    alts = []
    for line in (out.get("response") or "").splitlines():
        line = line.strip().lstrip("0123456789.-) ").strip()
        if line and len(line) > 3:
            alts.append(line)
    return [question] + alts[:n]

def llm_rerank(question: str, candidates: list[dict], top_k: int = 3) -> list[dict]:
    """Ask local model to pick best chunk ids from top candidates."""
    if len(candidates) <= top_k:
        return candidates
    listing = []
    for i, c in enumerate(candidates):
        listing.append(f"ID={c['id']}\n{(c['text'][:400])}")
    prompt = (
        f"Question: {question}\n\nWhich {top_k} passages are most relevant? "
        f"Reply with their IDs only, one per line.\n\n" + "\n\n".join(listing)
    )
    out = generate(prompt, model=MODEL, system="You are a relevance ranker. Output IDs only.",
                   num_predict=64, num_ctx=3072, temperature=0.0)
    text = out.get("response") or ""
    picked = []
    by_id = {c["id"]: c for c in candidates}
    for line in text.splitlines():
        for cid in by_id:
            if cid in line and cid not in [p["id"] for p in picked]:
                picked.append(by_id[cid])
                break
        if len(picked) >= top_k:
            break
    if len(picked) < top_k:
        # fill from original order
        for c in candidates:
            if c["id"] not in [p["id"] for p in picked]:
                picked.append(c)
            if len(picked) >= top_k:
                break
    return picked[:top_k]

def eval_items(items, retrieve_fn, label: str, memory: MemoryStore | None = None,
               few_shot: bool = False, use_lessons: bool = False) -> dict:
    results = []
    correct = 0
    t0 = time.time()
    for item in items:
        ctx = None
        retrieved = []
        extra_parts = []
        try:
            hits = retrieve_fn(item["q"]) if retrieve_fn else []
            retrieved = [{"id": d["id"], "path": d.get("path"), "text": d["text"][:500]} for d in hits]
            if hits:
                ctx = "\n\n---\n\n".join(f"[{d['id']}]\n{d['text']}" for d in hits)
        except Exception as e:
            retrieved = [{"error": str(e)}]
        if memory and use_lessons:
            lc = memory.context_for_query(item["q"], limit=3)
            if lc:
                extra_parts.append(lc)
        if memory and few_shot:
            pairs = memory.few_shot_pairs(item["q"], limit=2)
            if pairs:
                shots = []
                for p in pairs:
                    shots.append(f"Q: {p['input']}\nA: {p['output']}")
                extra_parts.append("Similar past Q&A:\n" + "\n\n".join(shots))
        extra = "\n\n".join(extra_parts) if extra_parts else None
        out = ask(item["q"], ctx, extra=extra)
        ans = out.get("response") or ""
        ok = grade(item, ans)
        correct += int(ok)
        results.append({
            "id": item["id"], "split": item["split"], "question": item["q"],
            "expected": item["expected"], "answer": ans, "correct": ok,
            "retrieved": retrieved, "tok_s": out.get("_tok_s"), "wall_s": out.get("_wall_s"),
        })
        print(f"[{label}] {item['id']} ok={ok} ans={ans[:70]!r}", flush=True)
    wall = time.time() - t0
    summary = {
        "method": label, "n": len(items), "correct": correct,
        "accuracy": correct / len(items) if items else 0.0,
        "wall_s": wall, "seed": SEED, "model": MODEL,
        "by_split": {},
    }
    for sp in ("seen", "heldout"):
        sub = [r for r in results if r["split"] == sp]
        if sub:
            c = sum(1 for r in sub if r["correct"])
            summary["by_split"][sp] = {"n": len(sub), "correct": c, "accuracy": c / len(sub)}
    return {"summary": summary, "results": results}

def make_bm25_retriever(docs, top_k=3):
    bm = BM25(docs)
    by_id = {d["id"]: d for d in docs}
    def retrieve(q):
        return [d for _, d in bm.score(q, top_k=top_k)]
    retrieve.bm = bm
    retrieve.by_id = by_id
    retrieve.docs = docs
    return retrieve

def make_multiquery_retriever(docs, top_k=3):
    bm = BM25(docs)
    by_id = {d["id"]: d for d in docs}
    def retrieve(q):
        queries = rewrite_queries(q, n=2)
        lists = [bm.rank_ids(qq, top_k=10) for qq in queries]
        fused = rrf_fuse(lists, top_k=top_k)
        return [by_id[i] for i in fused if i in by_id]
    return retrieve

def make_hybrid_retriever(docs, dense: DenseIndex, top_k=3):
    bm = BM25(docs)
    by_id = {d["id"]: d for d in docs}
    def retrieve(q):
        fused = rrf_fuse([bm.rank_ids(q, top_k=15), dense.rank_ids(q, top_k=15)], top_k=top_k)
        return [by_id[i] for i in fused if i in by_id]
    return retrieve

def make_rerank_retriever(docs, top_k=3, pool=8):
    bm = BM25(docs)
    def retrieve(q):
        cands = [d for _, d in bm.score(q, top_k=pool)]
        return llm_rerank(q, cands, top_k=top_k)
    return retrieve

def write_lesson_from_failure(store: MemoryStore, item: dict, wrong_answer: str) -> dict:
    key_facts = "; ".join(item["expected"])
    lesson_text = (
        f"LESSON: For question '{item['q']}', the correct key fact(s) are: {key_facts}. "
        f"Do not answer with: {(wrong_answer or '')[:120]}"
    )
    return store.record(
        source="reflexion",
        input=item["q"],
        output=lesson_text,
        tags=["lesson", "failure", "reflexion", item["id"]],
        meta={"lesson_text": lesson_text, "qid": item["id"], "expected": item["expected"]},
    )

def write_correct_qa(store: MemoryStore, item: dict, answer: str) -> dict:
    return store.record(
        source="quiz",
        input=item["q"],
        output=answer,
        tags=["qa", "correct", item["id"]],
        meta={"qid": item["id"]},
    )

def self_study(store: MemoryStore, docs: list[dict], n_pages: int = 6) -> list[dict]:
    """Model writes Q&A from Gitbook chunks; verify keys appear in source chunk."""
    # Pick diverse chunks with headings
    picked = []
    seen_paths = set()
    for d in docs:
        p = d.get("path", "")
        if p in seen_paths:
            continue
        if len(d["text"]) < 200:
            continue
        seen_paths.add(p)
        picked.append(d)
        if len(picked) >= n_pages:
            break
    verified = []
    for d in picked:
        prompt = (
            "From the Gitbook excerpt below, write ONE factual question and its short answer. "
            "Answer must be a phrase copied or tightly paraphrased from the excerpt. "
            "Format exactly:\nQ: ...\nA: ...\n\nEXCERPT:\n" + d["text"][:1200]
        )
        out = generate(prompt, model=MODEL, system="Extract one grounded Q&A. No invention.",
                       num_predict=120, num_ctx=2048, temperature=0.2)
        text = out.get("response") or ""
        q = a = None
        for line in text.splitlines():
            if line.lower().startswith("q:"):
                q = line.split(":", 1)[1].strip()
            elif line.lower().startswith("a:"):
                a = line.split(":", 1)[1].strip()
        if not q or not a:
            continue
        # verify: at least one content token of answer appears in chunk
        toks = [t for t in a.lower().split() if len(t) >= 4]
        if not toks:
            continue
        hits = sum(1 for t in toks if t in d["text"].lower())
        if hits / len(toks) < 0.4:
            print(f"[self_study] reject unverified A={a[:60]!r}", flush=True)
            continue
        lesson = f"LESSON: Q '{q}' → A '{a}' (from {Path(d['path']).name})"
        rec = store.record(
            source="self_study",
            input=q,
            output=lesson,
            tags=["lesson", "self_study", "verified"],
            meta={"lesson_text": lesson, "source_chunk": d["id"], "raw_a": a},
        )
        verified.append(rec)
        print(f"[self_study] verified {rec['id']} Q={q[:50]!r}", flush=True)
    return verified

def learning_curve(retriever, train_items, hold_items, store: MemoryStore, steps=(0, 0.25, 0.5, 1.0)):
    """After wrong answers on train, write lessons; measure held-out accuracy at fractions of feedback."""
    # First pass: get baseline wrongs on train with retrieval only (no lessons)
    print("=== learning curve: initial train pass ===", flush=True)
    init = eval_items(train_items, retriever, "curve_train0", memory=None)
    wrongs = [r for r in init["results"] if not r["correct"]]
    # Map back to items
    by_id = {i["id"]: i for i in train_items}
    wrong_items = [(by_id[r["id"]], r["answer"]) for r in wrongs if r["id"] in by_id]

    curve = []
    n_fb = len(wrong_items)
    for frac in steps:
        # reset store for clean curve points? cumulative from empty
        pass
    # Build cumulative: clear store file
    if store.path.exists():
        store.path.unlink()
    points = []
    for frac in steps:
        k = int(round(frac * n_fb)) if frac < 1 else n_fb
        # ensure store has exactly first k lessons (rebuild)
        if store.path.exists():
            store.path.unlink()
        for item, ans in wrong_items[:k]:
            write_lesson_from_failure(store, item, ans)
        label = f"curve_fb{k}"
        print(f"=== learning curve heldout with {k}/{n_fb} feedback lessons ===", flush=True)
        # held-out with lessons + retrieval
        res = eval_items(hold_items, retriever, label, memory=store, use_lessons=True)
        points.append({
            "feedback_events": k,
            "feedback_frac": frac,
            "n_train_wrong": n_fb,
            "heldout": res["summary"]["by_split"].get("heldout", res["summary"]),
            "wall_s": res["summary"]["wall_s"],
            "summary": res["summary"],
        })
        # also save raw
        (OUT_DIR / f"{label}.json").write_text(json.dumps(res, indent=2))
    return {"train_init": init["summary"], "n_feedback_available": n_fb, "points": points}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="all",
                    choices=["all", "retrieval", "learning", "selfstudy", "chart", "embed_index"])
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = {"seed": SEED, "model": MODEL, "corpus": CORPUS, "started": time.strftime("%Y-%m-%dT%H:%M:%S")}
    table = []

    print("Loading corpora...", flush=True)
    docs_base = load_docs(CORPUS, chunk_baseline)
    docs_hov = load_docs(CORPUS, chunk_heading_overlap)
    print(f"chunks baseline={len(docs_base)} heading_overlap={len(docs_hov)}", flush=True)
    (OUT_DIR / "chunk_stats.json").write_text(json.dumps({
        "baseline_chunks": len(docs_base), "heading_overlap_chunks": len(docs_hov)
    }, indent=2))

    seen = by_split("seen")
    held = by_split("heldout")
    allq = all_items()

    # ---- Phase: retrieval ablations ----
    if args.phase in ("all", "retrieval"):
        methods = []
        # 1) BM25 baseline (original chunking) — remeasure on extended quiz
        methods.append(("bm25_baseline", make_bm25_retriever(docs_base, 3), docs_base))
        # 2) Better chunking
        methods.append(("bm25_heading_overlap", make_bm25_retriever(docs_hov, 3), docs_hov))
        # 3) Multi-query (on better chunks)
        methods.append(("multiquery_rrf", make_multiquery_retriever(docs_hov, 3), docs_hov))
        # 4) Rerank
        methods.append(("bm25_llm_rerank", make_rerank_retriever(docs_hov, 3, 8), docs_hov))

        # Hybrid if dense index exists
        dense_path = OUT_DIR / "dense_index.json"
        if dense_path.exists():
            try:
                raw = json.loads(dense_path.read_text())
                # rebuild docs_hov alignment
                if raw.get("n") == len(docs_hov):
                    dense = DenseIndex(docs_hov, raw["embeddings"])
                    methods.append(("hybrid_rrf", make_hybrid_retriever(docs_hov, dense, 3), docs_hov))
                    print("Hybrid RRF enabled", flush=True)
            except Exception as e:
                print(f"Dense index load failed: {e}", flush=True)

        for name, retr, _ in methods:
            print(f"\n======== METHOD {name} ========", flush=True)
            res = eval_items(allq, retr, name)
            (OUT_DIR / f"{name}.json").write_text(json.dumps(res, indent=2))
            table.append(res["summary"])

        # alone baseline on extended (no retrieval) — smaller time: seen only? Do all for fairness
        print("\n======== METHOD alone ========", flush=True)
        res = eval_items(allq, None, "alone")
        (OUT_DIR / "alone.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

    # ---- Phase: learning (reflexion + few-shot) ----
    if args.phase in ("all", "learning"):
        retr = make_bm25_retriever(docs_hov, 3)
        store = MemoryStore("/workspace/learning-rate/data/memory-reflexion")
        if store.path.exists():
            store.path.unlink()
        print("\n======== LEARNING CURVE ========", flush=True)
        curve = learning_curve(retr, seen, held, store, steps=(0, 0.5, 1.0))
        (OUT_DIR / "learning_curve.json").write_text(json.dumps(curve, indent=2))

        # Full reflexion: lessons from all train wrongs + evaluate all quiz
        if store.path.exists():
            store.path.unlink()
        # recreate full lessons
        init = eval_items(seen, retr, "reflexion_train_probe")
        by_id = {i["id"]: i for i in seen}
        for r in init["results"]:
            if not r["correct"]:
                write_lesson_from_failure(store, by_id[r["id"]], r["answer"])
            else:
                write_correct_qa(store, by_id[r["id"]], r["answer"])

        print("\n======== METHOD reflexion_lessons ========", flush=True)
        res = eval_items(allq, retr, "reflexion_lessons", memory=store, use_lessons=True)
        (OUT_DIR / "reflexion_lessons.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

        print("\n======== METHOD fewshot_memory ========", flush=True)
        res = eval_items(allq, retr, "fewshot_memory", memory=store, few_shot=True)
        (OUT_DIR / "fewshot_memory.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

        print("\n======== METHOD reflexion+fewshot ========", flush=True)
        res = eval_items(allq, retr, "reflexion_fewshot", memory=store, use_lessons=True, few_shot=True)
        (OUT_DIR / "reflexion_fewshot.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

        # consolidation
        cons = store.consolidate(decay_below=0.5)
        print(f"consolidation: {cons['before']} -> {cons['after']} dropped={cons['dropped']} merged={cons['merged']}", flush=True)
        (OUT_DIR / "consolidation.json").write_text(json.dumps({k: cons[k] for k in ("before", "after", "dropped", "merged")}, indent=2))
        # After consolidation, rebuild memory from kept lessons as explicit records
        store2 = MemoryStore("/workspace/learning-rate/data/memory-consolidated")
        if store2.path.exists():
            store2.path.unlink()
        for l in cons["kept"]:
            store2.record(source="consolidated", input=" ".join(l["terms"][:8]), output=l["fact"],
                          tags=["lesson", "consolidated"], meta={"lesson_text": l["fact"], "confidence": l["confidence"]})
        print("\n======== METHOD consolidated_lessons ========", flush=True)
        res = eval_items(allq, retr, "consolidated_lessons", memory=store2, use_lessons=True)
        (OUT_DIR / "consolidated_lessons.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

    # ---- Phase: self-study ----
    if args.phase in ("all", "selfstudy"):
        retr = make_bm25_retriever(docs_hov, 3)
        store = MemoryStore("/workspace/learning-rate/data/memory-selfstudy")
        if store.path.exists():
            store.path.unlink()
        verified = self_study(store, docs_hov, n_pages=8)
        (OUT_DIR / "selfstudy_lessons.json").write_text(json.dumps({"n_verified": len(verified), "ids": [v["id"] for v in verified]}, indent=2))
        print("\n======== METHOD self_study ========", flush=True)
        res = eval_items(allq, retr, "self_study", memory=store, use_lessons=True)
        (OUT_DIR / "self_study.json").write_text(json.dumps(res, indent=2))
        table.append(res["summary"])

    # Save table so far
    if table:
        # compute deltas vs bm25_baseline if present
        base_acc = None
        for s in table:
            if s["method"] == "bm25_baseline":
                base_acc = s["accuracy"]
        for s in table:
            s["delta_vs_bm25_baseline"] = (s["accuracy"] - base_acc) if base_acc is not None else None
        (OUT_DIR / "table.json").write_text(json.dumps(table, indent=2))
        print(json.dumps(table, indent=2), flush=True)

    meta["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2))
    print("DONE", flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
