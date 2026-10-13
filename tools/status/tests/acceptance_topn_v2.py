#!/usr/bin/env python3
"""Acceptance (2) v2: same bar as acceptance_topn.py (10/10 planted contradictions caught at
<= 0.5x tokens of the FULL needs-attention list; gate is chars/4, tiktoken cl100k_base also shown if installed), measured for several broadcast variants
on current data and on a larger fixture (>=10 attention items). Baseline is never changed.
usage: acceptance_topn_v2.py ROOT   exit 0 iff the delta variant passes on both datasets."""
import datetime as dt, json, pathlib, shutil, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); import status
R = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "."); NOW = dt.datetime.fromisoformat("2026-10-13T15:00-05:00")
tok = lambda xs: len("\n".join(f"- {x}" for x in xs)) // 4  # chars/4 (the gate)
try:
    import tiktoken; _enc = tiktoken.get_encoding("cl100k_base")
    ttok = lambda xs: len(_enc.encode("\n".join(f"- {x}" for x in xs)))
except Exception: ttok = None  # optional: report tiktoken cl100k_base too when installed
def copy(extra=()):
    t = pathlib.Path(tempfile.mkdtemp())
    for d in ("mesh/HANDOFF.md", "mesh/queue/TASKS.json", "intake/log.md"):
        (t/d).parent.mkdir(parents=True, exist_ok=True); shutil.copy(R/d, t/d)
    p = t/"mesh/queue/TASKS.json"; q = json.loads(p.read_text()); q["tasks"] += list(extra); p.write_text(json.dumps(q)); return t
def run(t):
    _, w = status.build(t, NOW); shutil.rmtree(t); return w
done = sorted(r["Id"] for r in status.table((R/"mesh/HANDOFF.md").read_text(), "Id") if r["Id"].startswith("GB-") and r["State"].lower() in status.DONE)
# larger fixture: 12 extra pre-existing attention items of mixed kinds (contradictions, stale claims, bad timestamps)
big = [{"id": f"Q-8{i:02d}", "lane": "Build", "status": "queued", "title": f"Old follow-up on {done[i % len(done)]}"} for i in range(6)]
big += [{"id": f"Q-82{i}", "lane": "Moderator", "status": "claimed", "claimed_by": "X", "claimed_at": "2026-10-12T01:00:00-05:00", "pr": None, "title": "t"} for i in range(4)]
big += [{"id": f"Q-83{i}", "lane": "Build", "status": "claimed", "claimed_by": "X", "claimed_at": "garbage", "title": "t"} for i in range(2)]
V = {"all items, compact codes": lambda w, prev: [status.compact(x) for x in w],
     "delta since last wake, prose": lambda w, prev: status.delta(w, prev),
     "delta since last wake, compact": lambda w, prev: [status.compact(x) for x in status.delta(w, prev)]}
ok = True
for name, extra in (("current", []), ("large fixture", big)):
    base = {status.key(x) for x in run(copy(extra))}  # keys the agent saw at its last wake
    res = {k: [0, 0, 0] for k in V}; fulls = 0; tfulls = 0
    for i in range(10):
        tag = f"Q-9{i:02d}"
        w = run(copy(extra + [{"id": tag, "lane": "Build", "status": "queued", "title": f"Follow-up on {done[i % len(done)]}"}]))
        F = tok(w); fulls += F; tfulls += ttok(w) if ttok else 0
        for k, f in V.items():
            b = f(w, base); res[k][0] += any(x.startswith(tag) for x in b); res[k][1] += tok(b); res[k][2] += ttok(b) if ttok else 0
    print(f"\n[{name}] attention items/wake: {len(w)}; full list {fulls/10:.1f} tokens/wake (chars/4)" + (f", {tfulls/10:.1f} (tiktoken cl100k_base)" if ttok else ""))
    print(f"| variant | tokens/wake (chars/4) | caught | ratio (chars/4) | ratio (tiktoken cl100k_base) | pass |\n|---|---|---|---|---|---|")
    for k, (c, t, tt) in res.items():
        r = t / fulls; p = c == 10 and r <= 0.5
        print(f"| {k} | {t/10:.1f} | {c}/10 | {r:.3f}x | {f'{tt/tfulls:.3f}x' if ttok else 'n/a'} | {'PASS' if p else 'fail'} |")
        if k == "delta since last wake, prose": ok &= p
sys.exit(0 if ok else 1)
