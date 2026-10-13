"""Before/after: gate catch-rate on the crafted bad set, and parallel-schedulable tasks."""
import json, os, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent; sys.path[:0] = [str(HERE.parent), str(HERE)]
import dispatch as D, gatecheck as G
from fixtures import BAD, GOOD, SCOPE, make_repo
GL = os.environ.get("GITLEAKS", "/workspace/pubscan/gitleaks")
old = new = 0
for name, (f, e) in list(BAD.items()) + [("GOOD", GOOD)]:
    r = make_repo(f, e)
    o = subprocess.run([str(HERE / "old_gate_local.sh"), r, "main"], capture_output=True, text=True, cwd=r).stdout.strip().startswith("GATE FAIL")
    n = not G.check(r, "main", "pr", {"scope": SCOPE}, gitleaks=GL)["pass"]
    if name != "GOOD": old += o; new += n
    print(f"{name:22} old={'REJECT' if o else 'pass  '} new={'REJECT' if n else 'pass  '}")
print(f"SYNTHETIC-ONLY (not counted as a win) catch-rate old {old}/{len(BAD)} new {new}/{len(BAD)}")
# Parallel: old dispatch.py rules (max 6, overlap only) vs new select (cap 12, caps/quarantine), offline (no open-PR files).
def old_select(q, mx=6):
    picked, taken = [], []
    for t in q["tasks"]:
        if len(picked) >= mx: break
        if t["status"] != "queued" or any(r == t["repo"] and (s.startswith(o) or o.startswith(s)) for s in t["scope"] for r, o in taken): continue
        taken += [(t["repo"], s) for s in t["scope"]]; picked.append(t["id"])
    return picked
q = json.loads((HERE.parent / "TASKS.json").read_text())
print("current queue: old", old_select(q), "new", [t["id"] for t in D.select(q)])
# Spawn scenario: 4 root tasks each proposing 4 children (disjoint sub-scopes); old dispatch has no spawn path.
q2 = {"tasks": [{"id": f"R{i}", "repo": "Gitbook", "scope": [f"area{i}/"], "title": "r", "acceptance": [], "status": "done"} for i in range(4)]}
for i in range(4): D.spawn(q2, f"R{i}", [{"title": "c", "repo": "Gitbook", "scope": [f"area{i}/c{j}/"]} for j in range(4)], f"R{i}")
print("SYNTHETIC-ONLY (not counted as a win) spawn scenario (16 children): old", len(old_select(q2)), "new", len(D.select(q2)))
