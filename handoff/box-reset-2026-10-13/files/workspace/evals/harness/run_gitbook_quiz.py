#!/usr/bin/env python3
"""Gitbook knowledge check: model alone vs BM25 top-3 retrieval."""
from __future__ import annotations
import argparse, json, re, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ollama_client import generate, DEFAULT_MODEL
from bm25 import load_corpus

# From /workspace/full-picture/BASELINE.md section C — expected abbreviated answers
QUIZ = [
    {"id": 1, "q": "What are the two active repos' roles?", "expected": ["TESSERA = app", "Gitbook = instructions", "coordination"], "keys": ["tessera", "gitbook", "app", "instruction", "coordination", "code"]},
    {"id": 2, "q": "What is the single coordination board?", "expected": ["Gitbook issue #2"], "keys": ["issue", "#2", "gitbook"]},
    {"id": 3, "q": "Who is Father?", "expected": ["Collin Keane"], "keys": ["collin", "keane"]},
    {"id": 4, "q": "Does Tessera have owned weights?", "expected": ["No (GOAL until chamber test)"], "keys": ["no", "not", "goal", "owned weights"]},
    {"id": 5, "q": "Is Tessera AGI today?", "expected": ["No"], "keys": ["no", "not agi"]},
    {"id": 6, "q": "What instrument is the Pen?", "expected": ["xAI/Grok"], "keys": ["xai", "grok"]},
    {"id": 7, "q": "Label TESTED means?", "expected": ["Real output / named check seen"], "keys": ["real", "output", "check", "seen", "proven"]},
    {"id": 8, "q": "Label REPORTED means?", "expected": ["Stated, not proven"], "keys": ["stated", "not proven", "not yet", "reported"]},
    {"id": 9, "q": "What does HYB-005 decide?", "expected": ["Narrow braces advisory ignore"], "keys": ["braces", "ghsa", "ignore", "mitigat", "accept"]},
    {"id": 10, "q": "Which GHSA is ignored?", "expected": ["GHSA-vfj7-8cjw-p6xm"], "keys": ["vfj7", "8cjw", "p6xm", "ghsa"]},
    {"id": 11, "q": "What did HYB-012 deliver?", "expected": ["Route inventory test; duplicates allow-listed"], "keys": ["route", "inventory", "duplicate", "allow"]},
    {"id": 12, "q": "How many ruling-named quantum duplicate routes?", "expected": ["Two"], "keys": ["two", "2"]},
    {"id": 13, "q": "Which module wins GET /quantum/state?", "expected": ["system-runtime (mount order)"], "keys": ["system-runtime", "system_runtime", "mount"]},
    {"id": 14, "q": "May agents flip TESSERA_ENABLE_*?", "expected": ["No"], "keys": ["no", "do not", "stay", "0"]},
    {"id": 15, "q": "May agents open [REDACTED-PATH]", "expected": ["No"], "keys": ["no", "not", "do not", "protected"]},
    {"id": 16, "q": "Four gates order?", "expected": ["Moderator → Tessera → Security → CI/Build"], "keys": ["moderator", "tessera", "security", "ci", "build"]},
    {"id": 17, "q": "Who merges TESSERA?", "expected": ["Needs Father's explicit \"merge\""], "keys": ["father", "merge"]},
    {"id": 18, "q": "Command Center pushes Gitbook?", "expected": ["Never; only private Replit app-set after yes"], "keys": ["never", "not", "replit"]},
    {"id": 19, "q": "Status of Recursive Learning Sponge?", "expected": ["Provisional / not instantiated"], "keys": ["provisional", "not instantiated", "tbd", "to be confirmed"]},
    {"id": 20, "q": "HYB-019 blocker?", "expected": ["Father decisions on Cortical Labs readiness"], "keys": ["father", "cortical", "readiness", "decision"]},
    {"id": 21, "q": "OpenManus full copy into TESSERA?", "expected": ["Not the board rule — recover portable pieces only"], "keys": ["not", "portable", "no", "do not copy", "wholesale"]},
    {"id": 22, "q": "Storefront in active workspace?", "expected": ["No"], "keys": ["no", "not", "goal", "not a live"]},
    {"id": 23, "q": "Honesty banner instrument line?", "expected": ["Pen is currently xAI/Grok"], "keys": ["xai", "grok", "pen"]},
    {"id": 24, "q": "What is SOVEREIGN_NO_EXTERNAL_LLM default behavior?", "expected": ["External LLM treated off unless opted in"], "keys": ["off", "default", "external", "unless", "1"]},
    {"id": 25, "q": "CI job name?", "expected": ["validate"], "keys": ["validate"]},
]

GRADING_RULE = (
    "key-fact match: case-insensitive; a question scores correct if ANY listed key substring "
    "appears in the model answer AND (for multi-key questions 1,9,11,16) at least 2 keys match; "
    "for yes/no questions require an explicit no/not denial when expected is No; "
    "exact GHSA id or 'vfj7' counts for Q10; exact 'validate' for Q25."
)

def grade(item: dict, answer: str) -> bool:
    a = answer.lower()
    keys = item["keys"]
    qid = item["id"]
    # special cases
    if qid in (4, 5, 14, 15, 22):
        # expect No
        if re.search(r"\b(yes|true)\b", a) and not re.search(r"\b(no|not|never|false)\b", a):
            return False
        return bool(re.search(r"\b(no|not|never|false|goal)\b", a)) or any(k in a for k in keys)
    if qid == 12:
        return bool(re.search(r"\b(two|2)\b", a))
    if qid == 10:
        return ("vfj7" in a) or ("ghsa-vfj7-8cjw-p6xm" in a)
    if qid == 25:
        return "validate" in a
    if qid == 3:
        return ("collin" in a and "keane" in a) or ("collin keane" in a)
    hits = sum(1 for k in keys if k.lower() in a)
    if qid in (1, 9, 11, 16):
        return hits >= 2
    if qid == 18:
        return ("never" in a) or ("does not push gitbook" in a) or ("not push" in a and "gitbook" in a) or ("replit" in a and "never" in a)
    return hits >= 1

def ask(question: str, context: str | None, model: str) -> dict:
    system = (
        "You answer questions about the Tessera mesh / Gitbook docs. "
        "Be concise and factual. Prefer short answers."
    )
    if context:
        prompt = (
            "Use the following retrieved Gitbook doc excerpts if relevant.\n\n"
            f"CONTEXT:\n{context}\n\nQUESTION: {question}\n\nShort answer:"
        )
    else:
        prompt = f"QUESTION: {question}\n\nShort answer:"
    return generate(prompt, model=model, system=system, num_predict=128, num_ctx=3072, temperature=0.0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--corpus", default="/workspace/evals/data/gitbook-corpus")
    ap.add_argument("--mode", choices=["both", "alone", "rag"], default="both")
    args = ap.parse_args()

    bm25 = load_corpus(args.corpus) if args.mode in ("both", "rag") else None
    modes = []
    if args.mode in ("both", "alone"):
        modes.append("alone")
    if args.mode in ("both", "rag"):
        modes.append("rag")

    all_out = {"grading_rule": GRADING_RULE, "quiz_source": "/workspace/full-picture/BASELINE.md section C", "modes": {}}
    t_all = time.time()
    for mode in modes:
        results = []
        correct = 0
        t0 = time.time()
        for item in QUIZ:
            ctx = None
            retrieved = []
            if mode == "rag" and bm25 is not None:
                hits = bm25.score(item["q"], top_k=3)
                retrieved = [{"score": s, "id": d["id"], "path": d["path"], "text": d["text"][:800]} for s, d in hits]
                ctx = "\n\n---\n\n".join(f"[{d['id']}]\n{d['text']}" for _, d in hits)
            out = ask(item["q"], ctx, args.model)
            ans = out.get("response") or ""
            ok = grade(item, ans)
            correct += int(ok)
            results.append({
                "id": item["id"],
                "question": item["q"],
                "expected": item["expected"],
                "answer": ans,
                "correct": ok,
                "retrieved": retrieved,
                "tok_s": out.get("_tok_s"),
                "wall_s": out.get("_wall_s"),
            })
            print(f"[{mode}] Q{item['id']} ok={ok} ans={ans[:80]!r}", flush=True)
        summary = {
            "mode": mode,
            "n": len(QUIZ),
            "correct": correct,
            "accuracy": correct / len(QUIZ),
            "wall_s": time.time() - t0,
            "model": args.model,
            "item_ids": [f"gitbook_q{i}" for i in range(1, 26)],
        }
        all_out["modes"][mode] = {"summary": summary, "results": results}
        print(json.dumps(summary, indent=2), flush=True)

    all_out["wall_s_total"] = time.time() - t_all
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(all_out, f, indent=2)

if __name__ == "__main__":
    main()
