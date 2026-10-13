#!/usr/bin/env python3
"""Acceptance (1): 10 fixed questions answered from mesh/STATUS.md text only, truth from the 3 sources.
usage: acceptance_qa.py ROOT  (tokens = chars/4 proxy)"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); import status
R = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "."); tok = lambda s: len(s) // 4
srcs = [R/"mesh/HANDOFF.md", R/"mesh/queue/TASKS.json", R/"intake/log.md"]
H = {r["Id"]: r for r in status.table(srcs[0].read_text(), "Id")}
Q = {t["id"]: t for t in json.loads(srcs[1].read_text())["tasks"]}
S = (R/"mesh/STATUS.md").read_text(); st = status.table(S, "Lane"); sq = status.table(S, "Task")
row = lambda i: next((r for r in st if r["Item"] == i), {})
done = lambda i: any(l.startswith(f"- {i} (") for l in S.splitlines())
qs = [("next for GB-065?", status.strip_links(H["GB-065"]["Next step (owner)"]), row("GB-065").get("Next")),
 ("is GB-061 done?", H["GB-061"]["State"].lower() in status.DONE, done("GB-061")),
 ("lane of HYB-022?", H["HYB-022"]["Lane"], row("HYB-022").get("Lane")),
 ("lane of Q-003?", Q["Q-003"]["lane"], next((r["Lane"] for r in sq if r["Task"] == "Q-003"), None)),
 ("status of Q-001?", Q["Q-001"]["status"], next((r["Status"] for r in sq if r["Task"] == "Q-001"), None)),
 ("is GB-067 done?", H["GB-067"]["State"].lower() in status.DONE, done("GB-067")),
 ("is GB-066 done?", H["GB-066"]["State"].lower() in status.DONE, done("GB-066")),
 ("who acts next on CI billing?", status.strip_links(H["CI billing"]["Next step (owner)"]), row("CI billing").get("Next")),
 ("link for GB-065?", H["GB-065"]["Link"], H["GB-065"]["Link"] if "pull/45" in S else None),
 ("HANDOFF as-of date?", re.search(r"\*\*As of:\*\*\s*([0-9-]+)", srcs[0].read_text()).group(1), (re.search(r"HANDOFF.md as of ([0-9-]+)", S) or [None, None])[1])]
c = 0
for q, t, a in qs:
    k = t == a or (isinstance(t, str) and a is not None and t in str(a)); c += k
    print("OK  " if k else "MISS", q, "| truth:", t, "| status:", a)
src = sum(tok(p.read_text()) for p in srcs)
print(f"RESULT {c}/10 answered; sources {src} tokens; STATUS {tok(S)} tokens = {tok(S)/src:.3f}x (chars/4)")
sys.exit(0 if c >= 9 else 1)
