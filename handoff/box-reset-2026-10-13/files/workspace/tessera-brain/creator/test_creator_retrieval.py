#!/usr/bin/env python3
"""TESTED: new request → retrieval returns matching Father rule."""
from __future__ import annotations
import json
from pathlib import Path
from profile_to_lessons import build

CASES = [
    ("should I buy the paid plan?", ["no paid replit", "prefer free"]),
    ("skip tests for now?", ["test as you build"]),
    ("how often should we digest to father?", ["30-45", "30–45", "bulk"]),
    ("may an agent push gitbook to github?", ["father alone pushes", "do not push"]),
    ("full copy openmanus into tessera?", ["portable pieces", "not the board"]),
    ("buy cl1 hardware today?", ["simulator-only", "simulator"]),
]

def main():
    store = build()
    passed = failed = 0
    details = []
    for query, needles in CASES:
        hits = store.recall(query, limit=3)
        blob = " ".join(h["fact"].lower() for h in hits)
        ok = any(n.lower() in blob for n in needles)
        top = hits[0]["fact"] if hits else None
        if ok:
            passed += 1
            details.append({"query": query, "pass": True, "top": top, "score": hits[0].get("score") if hits else None})
            print("PASS", query, "->", top[:80] if top else None)
        else:
            failed += 1
            details.append({"query": query, "pass": False, "blob": blob, "top": top})
            print("FAIL", query, "->", blob[:200])
    print(f"passed={passed} failed={failed} total={len(CASES)}")
    Path("retrieval_test_results.json").write_text(
        json.dumps({"passed": passed, "failed": failed, "total": len(CASES), "details": details}, indent=2)
    )
    assert failed == 0
    return passed, failed

if __name__ == "__main__":
    main()
