#!/usr/bin/env python3
"""Silence as signal, tuned for fast stall detection.
An agent sends a tiny heartbeat only when it has sent nothing (real post or heartbeat) for HB minutes;
any real post counts as a heartbeat. The watchdog runs every TICK minutes and flags an agent
whose last message is older than DEADLINE minutes. Worst-case detection <= DEADLINE + TICK.
Defaults HB=20, DEADLINE=25, TICK=5 (Actions-cron compatible, 5 min slack against late heartbeats).
usage: silence.py watch BUS.jsonl [--deadline-min 25] [--now ISO]
       silence.py replay [real-trace.json] [--grid]"""
import json, sys, os, bisect, datetime as dt
HB, DEADLINE, TICK, BASE = 20, 25, 5, 15  # BASE = old policy: status every 15 min
def should_heartbeat(last_msg_min, now_min, hb=HB):
    return now_min - last_msg_min >= hb
def watch(msgs, now, deadline_min=DEADLINE):
    last = {}
    for m in msgs:
        a = m.get("agent") or m.get("from"); t = dt.datetime.fromisoformat(m["ts"].replace("Z", "+00:00"))
        if a and (a not in last or t > last[a]): last[a] = t
    return sorted(a for a, t in last.items() if (now - t).total_seconds() / 60 > deadline_min)
def replay(trace, hb=HB, deadline=DEADLINE, tick=TICK, base=BASE, stall_step=7):
    span = trace["span_min"]; before = after = worst = false_alarms = 0
    for real in trace["minutes"].values():
        rs = set(real); before += len(rs) + span // base
        last, sent = -10**9, []
        for m in range(span + 1):
            if m in rs or should_heartbeat(last, m, hb): last = m; sent.append(m)
        after += len(sent)
        false_alarms += max(b - a for a, b in zip(sent, sent[1:])) > deadline
        for s in range(0, span - 60, stall_step):  # agent dies at minute s
            lm = sent[bisect.bisect_right(sent, s) - 1]; t = (s // tick + 1) * tick
            while t - lm <= deadline: t += tick
            worst = max(worst, t - s)
    base_worst = 2 * base  # old policy deadline: two missed statuses
    return {"msgs_before": before, "msgs_after": after, "saved_pct": round(100 * (1 - after / before), 1),
            "worst_detect_min_before": base_worst, "worst_detect_min_after": worst, "false_alarms": false_alarms,
            "hb": hb, "deadline": deadline, "tick": tick}
def grid(trace, max_detect=30, slack=2):
    ok = [replay(trace, h, d, t) for t in (1, 5) for h in range(5, 30) for d in range(h + slack, 31)]
    ok = [r for r in ok if r["worst_detect_min_after"] <= max_detect and r["false_alarms"] == 0]
    return sorted(ok, key=lambda r: r["msgs_after"])
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "watch":
        now = dt.datetime.fromisoformat(a[a.index("--now")+1]) if "--now" in a else dt.datetime.now().astimezone()
        d = int(a[a.index("--deadline-min")+1]) if "--deadline-min" in a else DEADLINE
        stale = watch([json.loads(l) for l in open(a[1]) if l.strip()], now, d)
        print(json.dumps({"stale": stale})); sys.exit(1 if stale else 0)
    elif a and a[0] == "replay":
        f = next((x for x in a[1:] if not x.startswith("--")), os.path.join(os.path.dirname(os.path.abspath(__file__)), "real-trace.json"))
        tr = json.load(open(f))
        if "--grid" in a:
            g = grid(tr); print(json.dumps({"best_tick1": next(r for r in g if r["tick"] == 1), "best_tick5": next(r for r in g if r["tick"] == 5)}))
        else: print(json.dumps(replay(tr)))
    else: print(__doc__)
