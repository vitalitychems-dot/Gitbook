#!/usr/bin/env python3
"""Mesh queue dispatcher with lineage, spawn caps and quarantine.

  dispatch.py --next [--max 12] [--agent Tessera] [--claim] [--offline]
      JSON [{id, repo_url, title, prompt, parent_id, depth, branch}] of launchable tasks.
  dispatch.py --spawn PR_BODY.md --parent ID [--spawned-by AGENT]
      Adds the child tasks listed in the PR body's "## SPAWN" section (one JSON object per line:
      {"title":..,"repo":..,"scope":[..],"acceptance":[..],"budget":{..}}), enforcing caps.
  dispatch.py --record ID --agent-id X [--pr N] --status S [--launcher Tessera]
      Appends a row to LINEAGE.jsonl and sets the task status.
  dispatch.py --quarantine ID --reason TEXT
      Marks ID and all descendants quarantined (no further launches).
Only the launcher (Tessera) runs this; cloud agents propose children via SPAWN only."""
import argparse, datetime, json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); from gatecheck import is_protected
MAX_DEPTH, MAX_CHILDREN, MAX_CONCURRENT = 3, 4, 12
DEFAULT_BUDGET = {"max_files": 20, "max_lines": 800}
RUNNING = {"claimed", "launched", "running", "in_review"}
DONE = {"done", "merged"}
OWNER = "vitalitychems-dot"
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def load(p): return json.loads(pathlib.Path(p).read_text())
def save(p, q): pathlib.Path(p).write_text(json.dumps(q, indent=2) + "\n")
def by_id(q): return {t["id"]: t for t in q["tasks"]}

def ancestors(t, idx):
    seen = []
    while t.get("parent_id") and t["parent_id"] in idx and t["parent_id"] not in seen:
        seen.append(t["parent_id"]); t = idx[t["parent_id"]]
    return seen

def descendants(tid, q):
    out, frontier = [], [tid]
    while frontier:
        kids = [t["id"] for t in q["tasks"] if t.get("parent_id") in frontier and t["id"] not in out]
        out += kids; frontier = kids
    return out

def scopes_overlap(a, b):
    return any(x.startswith(y) or y.startswith(x) for x in a for y in b)

def select(q, max_n=MAX_CONCURRENT, busy=None):
    """Ready tasks honouring depth, quarantine, deps, global concurrency and file overlap."""
    idx, busy = by_id(q), busy or {}
    running = [t for t in q["tasks"] if t.get("status") in RUNNING]
    slots = min(max_n, MAX_CONCURRENT - len(running))
    taken = [(t["repo"], t["scope"]) for t in running]
    picked = []
    for t in q["tasks"]:
        if len(picked) >= slots: break
        if t.get("status") != "queued" or t.get("depth", 0) > MAX_DEPTH: continue
        if any(idx[a].get("status") == "quarantined" for a in ancestors(t, idx)): continue
        if any(idx.get(d, {}).get("status") not in DONE for d in t.get("depends_on", [])): continue
        if any(is_protected(s.rstrip("/")) or is_protected(s) for s in t["scope"]): continue
        if scopes_overlap(t["scope"], busy.get(t["repo"], [])): continue
        if any(r == t["repo"] and scopes_overlap(t["scope"], s) for r, s in taken): continue
        taken.append((t["repo"], t["scope"])); picked.append(t)
    return picked

def lineage_text(t, idx):
    chain = list(reversed(ancestors(t, idx))) + [t["id"]]
    return " -> ".join(chain)

def render(t, q, tmpl, sha, agent):
    idx = by_id(q); b = {**DEFAULT_BUDGET, **(t.get("budget") or {})}
    return tmpl.format(id=t["id"], id_lower=t["id"].lower(), title=t["title"], repo=t["repo"],
        scope=", ".join(t["scope"]), acceptance="; ".join(t["acceptance"]), gitbook_sha=sha, agent=agent,
        parent=t.get("parent_id") or "none (root task; supervisor is Tessera)", depth=t.get("depth", 0),
        lineage=lineage_text(t, idx), supervisor=t.get("spawned_by") or agent,
        max_depth=MAX_DEPTH, max_children=MAX_CHILDREN, max_files=b["max_files"], max_lines=b["max_lines"],
        can_spawn="yes" if t.get("depth", 0) < MAX_DEPTH else "no (max depth reached)")

def parse_spawn(body):
    m = re.search(r"^##\s*SPAWN\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    out = []
    for l in (m.group(1) if m else "").splitlines():
        l = l.strip().strip("`").lstrip("-* ").strip()
        if l.startswith("{"): out.append(json.loads(l))
    return out

def spawn(q, parent_id, reqs, spawned_by):
    idx = by_id(q); p = idx.get(parent_id)
    if not p: raise SystemExit(f"unknown parent {parent_id}")
    if p.get("status") == "quarantined" or any(idx[a].get("status") == "quarantined" for a in ancestors(p, idx)):
        raise SystemExit(f"{parent_id} is quarantined; no children")
    depth = p.get("depth", 0) + 1
    if depth > MAX_DEPTH: raise SystemExit(f"max depth {MAX_DEPTH} reached")
    have = sum(1 for t in q["tasks"] if t.get("parent_id") == parent_id)
    added, refused = [], []
    for i, r in enumerate(reqs):
        why = None
        if have + len(added) >= MAX_CHILDREN: why = f"max {MAX_CHILDREN} children"
        elif r.get("repo") not in ("Gitbook", "TESSERA"): why = "repo not allowed"
        elif not r.get("scope") or any(is_protected(s.rstrip("/")) or is_protected(s) for s in r["scope"]): why = "missing or protected scope"
        if why: refused.append({"title": r.get("title"), "why": why}); continue
        b = {**DEFAULT_BUDGET, **(p.get("budget") or {})}
        rb = {k: min(int((r.get("budget") or {}).get(k, b[k])), b[k]) for k in b}  # child budget <= parent's
        t = {"id": f"{parent_id}.{have + len(added) + 1}", "repo": r["repo"], "scope": r["scope"],
             "title": r["title"], "acceptance": r.get("acceptance") or ["autogate passes"], "lane": p.get("lane"),
             "status": "queued", "parent_id": parent_id, "depth": depth, "spawned_by": spawned_by,
             "budget": rb, "claimed_by": None, "claimed_at": None, "claim_lock": None, "pr": None}
        q["tasks"].append(t); added.append(t["id"])
    return added, refused

def quarantine(q, tid, reason):
    ids = [tid] + descendants(tid, q); idx = by_id(q)
    for i in ids:
        if idx[i].get("status") not in DONE:
            idx[i].update(status="quarantined", quarantine_reason=reason, quarantined_at=now())
    return ids

def ledger(path, row):
    with open(path, "a") as f: f.write(json.dumps(row, sort_keys=True) + "\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default=str(HERE / "TASKS.json")); ap.add_argument("--ledger", default=str(HERE / "LINEAGE.jsonl"))
    ap.add_argument("--next", action="store_true"); ap.add_argument("--max", type=int, default=MAX_CONCURRENT)
    ap.add_argument("--agent", default="Tessera"); ap.add_argument("--claim", action="store_true"); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--spawn"); ap.add_argument("--parent"); ap.add_argument("--spawned-by")
    ap.add_argument("--record"); ap.add_argument("--agent-id"); ap.add_argument("--pr"); ap.add_argument("--status"); ap.add_argument("--launcher", default="Tessera")
    ap.add_argument("--quarantine"); ap.add_argument("--reason", default="")
    a = ap.parse_args(); q = load(a.tasks)
    if a.spawn:
        added, refused = spawn(q, a.parent, parse_spawn(pathlib.Path(a.spawn).read_text()), a.spawned_by or a.parent)
        save(a.tasks, q); print(json.dumps({"added": added, "refused": refused})); return
    if a.record:
        t = by_id(q)[a.record]; t["status"] = a.status
        if a.pr: t["pr"] = int(a.pr)
        ledger(a.ledger, {"ts": now(), "task": a.record, "agent_id": a.agent_id, "parent": t.get("parent_id"),
                          "launcher": a.launcher, "pr": t.get("pr"), "status": a.status})
        save(a.tasks, q); return
    if a.quarantine:
        ids = quarantine(q, a.quarantine, a.reason); save(a.tasks, q)
        for i in ids: ledger(a.ledger, {"ts": now(), "task": i, "agent_id": by_id(q)[i].get("agent_id"), "parent": by_id(q)[i].get("parent_id"),
                                        "launcher": "autogate", "pr": by_id(q)[i].get("pr"), "status": "quarantined", "reason": a.reason})
        print(json.dumps({"quarantined": ids})); return
    busy, sha = {}, "offline"
    if not a.offline:
        sha = subprocess.run(["git", "ls-remote", f"https://github.com/{OWNER}/Gitbook", "main"], capture_output=True, text=True).stdout.split()[0]
        for r in {t["repo"] for t in q["tasks"]}:
            out = subprocess.run(["gh", "pr", "list", "-R", f"{OWNER}/{r}", "--state", "open", "--json", "files"], capture_output=True, text=True).stdout or "[]"
            busy[r] = [f["path"] for p in json.loads(out) for f in p.get("files", [])]
    tmpl = (HERE / "PROMPT-TEMPLATE.md").read_text()
    picked = select(q, a.max, busy)
    res = []
    for t in picked:
        if a.claim: t.update(status="claimed", claimed_by=a.agent, claimed_at=now(), claim_lock=f"{a.agent}:{sha}")
        res.append({"id": t["id"], "repo_url": f"https://github.com/{OWNER}/{t['repo']}", "title": f"{t['id']} {t['title']}"[:80],
                    "prompt": render(t, q, tmpl, sha, a.agent), "parent_id": t.get("parent_id"), "depth": t.get("depth", 0),
                    "branch": f"cursor/{t['id'].lower()}"})
    if a.claim: save(a.tasks, q)
    json.dump(res, sys.stdout, indent=1); print()

if __name__ == "__main__": main()
