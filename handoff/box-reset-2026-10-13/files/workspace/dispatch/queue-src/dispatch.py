#!/usr/bin/env python3
"""Pick independent queued tasks and render cloud-agent prompts.
Usage: dispatch.py [--max 6] [--agent NAME] [--claim]
Prints JSON [{id, repo, branch, prompt}] for the launcher (CloudAgent tool).
--claim writes claims into TASKS.json (commit that via PR before launching)."""
import json, subprocess, sys, datetime, pathlib, argparse
HERE = pathlib.Path(__file__).parent
ap = argparse.ArgumentParser(); ap.add_argument("--max", type=int, default=6)
ap.add_argument("--agent", default="Tessera"); ap.add_argument("--claim", action="store_true")
a = ap.parse_args()
q = json.loads((HERE / "TASKS.json").read_text())
sha = subprocess.run(["git", "ls-remote", "https://github.com/vitalitychems-dot/Gitbook", "main"], capture_output=True, text=True).stdout.split()[0]
def open_pr_files(repo):
    out = subprocess.run(["gh", "pr", "list", "-R", f"vitalitychems-dot/{repo}", "--state", "open", "--json", "number,files"], capture_output=True, text=True).stdout or "[]"
    return {(f["path"]): p["number"] for p in json.loads(out) for f in p.get("files", [])}
busy = {r: open_pr_files(r) for r in {t["repo"] for t in q["tasks"]}}
def overlaps(t, taken):
    for s in t["scope"]:
        if any(path.startswith(s) or s.startswith(path) for path in busy[t["repo"]]): return True
        if any(r == t["repo"] and (s.startswith(o) or o.startswith(s)) for r, o in taken): return True
    return False
tmpl = (HERE / "PROMPT-TEMPLATE.md").read_text()
picked, taken = [], []
for t in q["tasks"]:
    if len(picked) >= a.max: break
    if t["status"] != "queued" or overlaps(t, taken): continue
    taken += [(t["repo"], s) for s in t["scope"]]
    if a.claim:
        t.update(status="claimed", claimed_by=a.agent, claimed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), claim_lock=f"{a.agent}:{sha}")
    prompt = tmpl.format(id=t["id"], id_lower=t["id"].lower(), title=t["title"], repo=t["repo"], scope=", ".join(t["scope"]), acceptance="; ".join(t["acceptance"]), gitbook_sha=sha, agent=a.agent)
    picked.append({"id": t["id"], "repo": t["repo"], "branch": f"cursor/{t['id'].lower()}", "prompt": prompt})
if a.claim: (HERE / "TASKS.json").write_text(json.dumps(q, indent=2) + "\n")
json.dump(picked, sys.stdout, indent=1)
