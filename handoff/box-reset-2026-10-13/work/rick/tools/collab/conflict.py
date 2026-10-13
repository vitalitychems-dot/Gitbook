#!/usr/bin/env python3
"""Claim-conflict detector: scan lane notes for task IDs (HYB-012, GB-029, SITE-001...) and the lanes that claim/own them.
Flags IDs claimed by 2+ lanes, and file paths touched by 2+ open claims (bus claims with 'paths')."""
import re, sys, os, glob, collections, json
ID = re.compile(r"\b(HYB|GB|SITE|PERF|OPT|AGI|BH)-\d{2,4}\b")
LANE = {"tessera": r"\btessera\b", "cursor-project": r"cursor", "replit": r"replit", "grok-bot": r"grok bot", "cordnation": r"cordnation",
        "moderator": r"moderator", "security": r"security", "build": r"\bbuild\b", "mesh-cloud": r"mesh cloud", "command-center": r"command center", "rick": r"\brick\b"}
CLAIM = re.compile(r"\b(claim(s|ed)?|owns?|assigned to|taking|in progress)\b", re.I)
def scan_lines(lines):
    owners = collections.defaultdict(set); ev = collections.defaultdict(list)
    for src, n, ln in lines:
        if not CLAIM.search(ln): continue
        ids = {m.group(0) for m in ID.finditer(ln)}
        lanes = {k for k, p in LANE.items() if re.search(p, ln, re.I) and re.search(p + r".{0,40}" + CLAIM.pattern, ln, re.I)}
        if len(lanes) != 1: continue  # multi-lane rows are ownership tables, not claims
        for i in ids:
            for l in lanes: owners[i].add(l); ev[i].append(f"{src}:{n}")
    return {i: {"lanes": sorted(o), "evidence": ev[i][:4]} for i, o in owners.items() if len(o) > 1}
def path_conflicts(claims):
    by = collections.defaultdict(set)
    for c in claims:
        for p in c.get("paths", []): by[p.rstrip("/")].add(c["from"])
    keys = sorted(by); out = []
    for i, a in enumerate(keys):
        for b in keys[i:]:
            if (a == b or b.startswith(a + "/")) and len(by[a] | by[b]) > 1: out.append((a, b, sorted(by[a] | by[b])))
    return out
if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.environ.get("RICK_GITBOOK", "/workspace/rick/src/Gitbook"), "mesh")
    L = [(os.path.relpath(p, root), n, l) for p in glob.glob(root + "/**/*.md", recursive=True) for n, l in enumerate(open(p, errors="replace"), 1)]
    r = scan_lines(L); print(json.dumps({"lines": len(L), "multi_claimed_ids": len(r), "items": r}, indent=1))
