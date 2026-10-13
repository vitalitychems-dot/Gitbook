#!/usr/bin/env python3
"""Quiet consensus: ask a panel of K agents first; escalate a question to everyone only if the panel disagrees.
usage: quiet.py ROUND.jsonl QUESTIONS.json [--k 3] [--tol 0.01]
Cost unit = agent-answers requested (proxy for tokens: each answer costs ~ the same prompt+reply)."""
import json, sys
from common import load_round, merge_one, spread
def quiet(qs, ans, k=3, tol=0.01, panel=None):
    agents = sorted(ans); panel = panel or agents[:k]; rest = [a for a in agents if a not in panel]
    out, cost, esc = [], 0, []
    for i, q in enumerate(qs):
        pv = [ans[a][i] for a in panel]; cost += len(pv)
        if spread(q, pv) <= tol: out.append(merge_one(q, pv))
        else:
            esc.append(q["id"]); cost += len(rest)
            out.append(merge_one(q, pv + [ans[a][i] for a in rest]))
    return out, cost, esc
def full(qs, ans):
    return [merge_one(q, [a[i] for a in ans.values()]) for i, q in enumerate(qs)], len(ans) * len(qs)
if __name__ == "__main__":
    a = sys.argv[1:]; k = int(a[a.index("--k")+1]) if "--k" in a else 3
    tol = float(a[a.index("--tol")+1]) if "--tol" in a else 0.01
    qs = json.load(open(a[1])); ans = load_round(a[0], len(qs))
    f, fc = full(qs, ans); o, oc, esc = quiet(qs, ans, k, tol)
    same = sum((abs(x-y) <= 1e-9*max(1,abs(y))) if isinstance(y,float) else x == y for x, y in zip(o, f))
    print(json.dumps({"agents": len(ans), "full_cost": fc, "quiet_cost": oc, "saved_pct": round(100*(1-oc/fc),1),
                      "escalated_ids": esc, "same_as_full_merge": f"{same}/{len(qs)}"}))
