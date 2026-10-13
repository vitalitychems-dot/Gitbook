#!/usr/bin/env python3
"""Turn CREATOR-PROFILE rules into learning-memory interactions + one lesson per rule.
Uses BM25 recall over explicit lessons (avoids over-merging shared date tokens).
Mirrors learning-rate MemoryStore interaction format.
"""
from __future__ import annotations
import json, math, re, time, hashlib
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
MEM_DIR = ROOT / "memory"
PROFILE = ROOT / "CREATOR-PROFILE.md"
TOKEN = [REDACTED](r"[a-z0-9]+", re.I)
STOP = set("the and for with that this from into over how are was were been being before after them they you your our not but can could should would about what when where which who why has have had does did get got its via per than then also only just all any each use used using within without across example pattern lesson father".split())

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

PAIRS = [
    {
        "id": "cr-paid-replit",
        "input": "Should I buy the paid Replit connector / paid plan?",
        "lesson": "Prefer free routes: no paid Replit connector; sync via GitHub + Gitbook (Father 2026-10-05 6:44 PM CT).",
        "tags": ["cost", "replit", "free", "paid", "plan", "connector", "buy"],
    },
    {
        "id": "cr-test-as-you-build",
        "input": "Can we skip writing tests and add them later?",
        "lesson": "Test as you build. Father's rule 2026-10-05: every script ships with a small test; run before recording TESTED.",
        "tags": ["tests", "build", "skip", "test"],
    },
    {
        "id": "cr-digest-cadence",
        "input": "How often should Command Center ask Father for approval?",
        "lesson": "Bulk yes/no/revise digests every 30-45 minutes while work is active.",
        "tags": ["digest", "cadence", "approval", "bulk", "minutes"],
    },
    {
        "id": "cr-father-push",
        "input": "Should agents push Gitbook changes to GitHub themselves?",
        "lesson": "After digest yes, Father alone pushes GitBook to GitHub. Agents and Command Center do not push.",
        "tags": ["pipeline", "push", "github", "agents"],
    },
    {
        "id": "cr-own-keys-free",
        "input": "Do we need paid OpenAI for the next eval?",
        "lesson": "Prefer free routes and Father's own API keys rather than paying platforms; local Ollama when keys absent (no spend).",
        "tags": ["cost", "api", "keys", "openai", "ollama", "spend"],
    },
    {
        "id": "cr-openmanus",
        "input": "Should Tessera full-copy OpenManus into the product repo?",
        "lesson": "OpenManus full copy is not the board rule — recover portable pieces only.",
        "tags": ["openmanus", "copy", "portable", "consolidate"],
    },
    {
        "id": "cr-cl1-sim",
        "input": "Can we sign up for Cortical Cloud or buy CL1 hardware now?",
        "lesson": "CL1 path: simulator-only for now (Father 2026-10-05 5:38 PM CT); no Cloud signup or hardware purchase without new approval.",
        "tags": ["cl1", "hardware", "cloud", "simulator", "cortical", "buy"],
    },
    {
        "id": "cr-token-channel",
        "input": "Who should message Father to save tokens?",
        "lesson": "Token-saving preference: Tessera / Command Center as the channel that messages Father (2026-10-05 7:02-7:03 PM CT).",
        "tags": ["messaging", "tokens", "channel", "tessera"],
    },
    {
        "id": "cr-no-invent-psych",
        "input": "Should Tessera invent Father's personality traits?",
        "lesson": "Creator model uses only dated stated rules. Do not invent psychology. PRIVATE profile wired to admin + memory.",
        "tags": ["creator", "privacy", "psychology", "personality"],
    },
    {
        "id": "cr-consolidate",
        "input": "Old repos still getting commits — what should happen?",
        "lesson": "Consolidate old repos into TESSERA and Gitbook; once work lands there, stop committing to old repos.",
        "tags": ["consolidate", "repos", "old", "commits"],
    },
]

class CreatorMemory:
    def __init__(self, dir: Path):
        self.dir = dir
        self.dir.mkdir(parents=True, exist_ok=True)
        self.interactions = self.dir / "interactions.jsonl"
        self.lessons_path = self.dir / "lessons.jsonl"

    def rebuild(self):
        for p in (self.interactions, self.lessons_path):
            if p.exists():
                p.unlink()
        lessons = []
        with open(self.interactions, "w") as fi, open(self.lessons_path, "w") as fl:
            for pair in PAIRS:
                rec = {
                    "id": f"rec-{pair['id']}",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "sourceAgent": "creator_profile",
                    "input": pair["input"],
                    "output": f"LESSON: {pair['lesson']}",
                    "tags": ["lesson"] + pair["tags"],
                    "meta": {"lesson_text": pair["lesson"], "rule_id": pair["id"]},
                }
                fi.write(json.dumps(rec) + "\n")
                lesson = {
                    "id": f"lesson-{pair['id']}",
                    "fact": pair["lesson"],
                    "evidenceIds": [rec["id"]],
                    "confidence": 0.95,
                    "terms": tokenize(pair["lesson"] + " " + " ".join(pair["tags"]) + " " + pair["input"]),
                    "n": 1,
                }
                fl.write(json.dumps(lesson) + "\n")
                lessons.append(lesson)
        (self.dir / "lessons_snapshot.json").write_text(json.dumps(lessons, indent=2))
        return lessons

    def lessons(self) -> list[dict]:
        if not self.lessons_path.exists():
            return self.rebuild()
        return [json.loads(l) for l in self.lessons_path.read_text().splitlines() if l.strip()]

    def recall(self, query: str, limit: int = 3) -> list[dict]:
        lessons = self.lessons()
        docs = [(l["id"], f"{l['fact']} {' '.join(l.get('terms', []))}") for l in lessons]
        scores = bm25_score(docs, query)
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

def build() -> CreatorMemory:
    assert PROFILE.exists()
    text = PROFILE.read_text()
    assert "PRIVATE" in text
    mem = CreatorMemory(MEM_DIR)
    lessons = mem.rebuild()
    print(f"interactions={len(PAIRS)} lessons={len(lessons)}")
    return mem

if __name__ == "__main__":
    build()
