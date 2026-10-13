#!/usr/bin/env python3
"""Disagreement-driven study queue: rank questions by how much agents' answers spread out.
usage: study.py ROUND.jsonl QUESTIONS.json [--min 0.001] -> JSON list of {id, q, spread} (questions only, never answers)."""
import json, sys
from common import load_round, spread
def study_queue(qs, ans, minspread=0.001):
    s = [(spread(q, [a[i] for a in ans.values()]), q) for i, q in enumerate(qs)]
    return [{"id": q["id"], "q": q["q"], "spread": round(v, 4)} for v, q in sorted(s, key=lambda t: -t[0]) if v > minspread]
if __name__ == "__main__":
    a = sys.argv[1:]; m = float(a[a.index("--min")+1]) if "--min" in a else 0.001
    qs = json.load(open(a[1])); print(json.dumps(study_queue(qs, load_round(a[0], len(qs)), m), indent=1))
