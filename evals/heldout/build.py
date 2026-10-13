#!/usr/bin/env python3
"""Rebuild pr-outcomes.jsonl from TESSERA PRs only (never Gitbook: its titles are private).
Usage: gh pr list -R vitalitychems-dot/TESSERA --state all --limit 1000 --json number,title,state > pr-TESSERA.json
       python3 evals/heldout/build.py pr-TESSERA.json && (cd evals/heldout && sha256sum data/*.jsonl > MANIFEST.sha256)
Any title matching PRIVATE is dropped outright (not scrubbed). Benchmark files are fixed picks; see LICENSES.md."""
import json, re, sys, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "pr-outcomes.jsonl")
PRIVATE = re.compile(r"collink|vitality|drive|\bzz\b|archive|gmail|@|https?://|www\.|\.com\b", re.I)
SCRUB = [(re.compile(r"\b[0-9a-f]{7,40}\b"), "<sha>"), (re.compile(r"#\d+"), "#<n>")]
EXCLUDE = {302}  # the leaked/withdrawn first version of this set
rows, dropped = [], 0
for p in sorted(json.load(open(sys.argv[1])), key=lambda p: p["number"]):
    if p["state"] == "OPEN" or p["number"] in EXCLUDE: continue
    t = p["title"]
    if PRIVATE.search(t): dropped += 1; continue
    for rx, rep in SCRUB: t = rx.sub(rep, t)
    rows.append({"id": f"pr-tessera-{p['number']}", "repo": "TESSERA", "title": t,
                 "outcome": "pass" if p["state"] == "MERGED" else "fail"})
with open(OUT, "w") as f:
    for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")
print(f"{len(rows)} rows, {dropped} dropped for private terms")
