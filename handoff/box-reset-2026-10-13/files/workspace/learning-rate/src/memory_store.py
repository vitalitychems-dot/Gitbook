#!/usr/bin/env python3
"""Python mirror of PR #7 retrieval memory + reflexion lessons + consolidation."""
from __future__ import annotations
import hashlib, json, math, re, time
from collections import Counter
from pathlib import Path

TOKEN = [REDACTED](r"[a-z0-9]+", re.I)
STOP = set("the and for with that this from into over how are was were been being before after them they you your our not but can could should would about what when where which who why has have had does did get got its via per than then also only just all any each use used using within without across example pattern".split())

def tokenize(text: str) -> list[str]:
    return [t for t in (TOKEN.findall(text.lower()) or []) if len(t) >= 3 and t not in STOP]

def bm25_score(docs: list[tuple[str, str]], query: str) -> dict[str, float]:
    tokenized = [(i, tokenize(t)) for i, t in docs]
    N = len(tokenized) or 1
    avgdl = sum(len(t) for _, t in tokenized) / N
    df: Counter = Counter()
    for _, t in tokenized:
        df.update(set(t))
    q = tokenize(query)
    scores = {}
    k1, b = 1.2, 0.75
    for i, toks in tokenized:
        tf = Counter(toks)
        s = 0.0
        dl = len(toks) or 1
        for term in q:
            if term not in tf:
                continue
            idf = math.log(1 + (N - df[term] + 0.5) / (df[term] + 0.5))
            f = tf[term]
            s += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
        scores[i] = s
    return scores

class MemoryStore:
    def __init__(self, dir: str | Path):
        self.dir = Path(dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.path = self.dir / "interactions.jsonl"
        self.lessons_path = self.dir / "lessons.jsonl"

    def record(self, *, source: str, input: str, output: str, tags: list[str] | None = None,
               meta: dict | None = None) -> dict:
        rec = {
            "id": f"rec-{int(time.time()*1000)}-{hashlib.sha1((input+output).encode()).hexdigest()[:8]}",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "sourceAgent": source,
            "input": input,
            "output": output,
            "tags": tags or [],
            "meta": meta or {},
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(rec) + "\n")
        return rec

    def list(self) -> list[dict]:
        if not self.path.exists():
            return []
        return [json.loads(l) for l in self.path.read_text().splitlines() if l.strip()]

    def distill_lessons(self) -> list[dict]:
        """Group interactions into lessons (PR#7-style Jaccard/overlap)."""
        records = self.list()
        clusters: list[list[dict]] = []
        for rec in records:
            tokens = set(tokenize(f"{rec['input']}\n{rec['output']}\n{' '.join(rec.get('tags',[]))}"))
            placed = False
            for cluster in clusters:
                ct = set(tokenize("\n".join(f"{r['input']}\n{r['output']}" for r in cluster)))
                shared = len(tokens & ct)
                union = len(tokens | ct) or 1
                if shared >= 3 or shared / union >= 0.34:
                    cluster.append(rec)
                    placed = True
                    break
            if not placed:
                clusters.append([rec])
        lessons = []
        for cluster in clusters:
            eids = [r["id"] for r in cluster]
            counts: Counter = Counter()
            for r in cluster:
                counts.update(tokenize(f"{r['input']}\n{r['output']}"))
            terms = [t for t, _ in counts.most_common(12)]
            sample = (cluster[0]["output"] or "").replace("\n", " ")[:180]
            # Prefer explicit lesson text if tagged
            fact = None
            for r in cluster:
                if "lesson" in r.get("tags", []) or r.get("meta", {}).get("lesson_text"):
                    fact = r.get("meta", {}).get("lesson_text") or r["output"]
                    break
            if not fact:
                fact = f"Pattern across {len(cluster)} interaction(s): {', '.join(terms[:6])}. Example: {sample}"
            conf = min(0.95, round(0.45 + 0.15 * (len(cluster) - 1), 2))
            digest = hashlib.sha256("|".join(sorted(eids)).encode()).hexdigest()[:12]
            lessons.append({
                "id": f"lesson-{digest}",
                "fact": fact,
                "evidenceIds": eids,
                "confidence": conf,
                "terms": terms,
                "n": len(cluster),
            })
        return lessons

    def recall(self, query: str, limit: int = 3, min_conf: float = 0.0) -> list[dict]:
        lessons = [l for l in self.distill_lessons() if l["confidence"] >= min_conf]
        if not lessons:
            return []
        scores = bm25_score([(l["id"], f"{l['fact']} {' '.join(l['terms'])}") for l in lessons], query)
        ranked = sorted(lessons, key=lambda l: -(scores.get(l["id"], 0)))
        out = []
        for l in ranked:
            s = scores.get(l["id"], 0)
            if s <= 0:
                continue
            out.append({**l, "score": s})
            if len(out) >= limit:
                break
        return out

    def context_for_query(self, query: str, limit: int = 3) -> str:
        hits = self.recall(query, limit=limit)
        if not hits:
            return ""
        lines = [f"- ({h['confidence']:.2f}) {h['fact']} [evidence: {', '.join(h['evidenceIds'])}]" for h in hits]
        return "Retrieved lessons (retrieval memory, not trained weights):\n" + "\n".join(lines)

    def consolidate(self, decay_below: float = 0.5) -> dict:
        """Dedupe near-identical lessons; decay/drop low-confidence singles."""
        lessons = self.distill_lessons()
        kept = []
        seen_facts = []
        dropped = 0
        merged = 0
        for l in lessons:
            # decay: single low-conf with no lesson tag
            if l["confidence"] < decay_below and l["n"] == 1 and "lesson" not in str(l["fact"]).lower()[:20]:
                # keep explicit reflexion facts always
                if not l["fact"].startswith("LESSON:"):
                    dropped += 1
                    continue
            toks = set(tokenize(l["fact"]))
            dup = False
            for i, prev in enumerate(seen_facts):
                pt = set(tokenize(prev["fact"]))
                j = len(toks & pt) / (len(toks | pt) or 1)
                if j >= 0.7:
                    # merge into higher conf
                    if l["confidence"] > prev["confidence"]:
                        seen_facts[i] = l
                    merged += 1
                    dup = True
                    break
            if not dup:
                seen_facts.append(l)
                kept.append(l)
        # rewrite lessons file as snapshot
        with open(self.lessons_path, "w") as f:
            for l in kept:
                f.write(json.dumps(l) + "\n")
        return {"before": len(lessons), "after": len(kept), "dropped": dropped, "merged": merged, "kept": kept}

    def few_shot_pairs(self, query: str, limit: int = 3) -> list[dict]:
        """Retrieve similar past Q&A (correct ones preferred)."""
        recs = [r for r in self.list() if "qa" in r.get("tags", []) or "correct" in r.get("tags", [])]
        if not recs:
            recs = self.list()
        if not recs:
            return []
        scores = bm25_score([(r["id"], f"{r['input']}\n{r['output']}") for r in recs], query)
        ranked = sorted(recs, key=lambda r: -(scores.get(r["id"], 0)))
        out = []
        for r in ranked:
            if scores.get(r["id"], 0) <= 0:
                continue
            out.append(r)
            if len(out) >= limit:
                break
        return out
