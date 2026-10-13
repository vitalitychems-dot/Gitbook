#!/usr/bin/env python3
"""Silence as signal. Agents post only when their state changes, plus one tiny keepalive per KEEPALIVE window.
The watchdog flags any agent whose last bus message is older than DEADLINE (= keepalive + grace).
usage: silence.py watch BUS.jsonl [--deadline-min 90] [--now ISO] | silence.py sim [--seed 7]"""
import json, sys, random, datetime as dt
KEEPALIVE = 60; GRACE = 30  # minutes
def should_post(state, last_state, last_post_min, now_min, keepalive=KEEPALIVE):
    return state != last_state or now_min - last_post_min >= keepalive
def watch(msgs, now, deadline_min=KEEPALIVE + GRACE):
    last = {}
    for m in msgs:
        a = m.get("agent") or m.get("from"); t = dt.datetime.fromisoformat(m["ts"])
        if a and (a not in last or t > last[a]): last[a] = t
    return sorted(a for a, t in last.items() if (now - t).total_seconds() / 60 > deadline_min)
def sim(seed=7, agents=9, cycle=15, hours=24, p_change=0.08, stall_agent=3, stall_at_h=10):
    """SYNTHETIC replay: each agent has a status every `cycle` minutes; one agent stalls."""
    rng = random.Random(seed); steps = hours * 60 // cycle; before = after = 0
    detect_before = detect_after = None; stall = stall_at_h * 60
    for a in range(agents):
        state, last_state, last_post = 0, None, -10**9; last_seen_b = last_seen_a = 0
        for s in range(steps):
            now = s * cycle
            if a == stall_agent and now >= stall: break
            if rng.random() < p_change: state += 1
            before += 1; last_seen_b = now          # old: post every cycle
            if should_post(state, last_state, last_post, now):
                after += 1; last_post = now; last_state = state; last_seen_a = now
        if a == stall_agent:
            # first watchdog tick (every cycle) at which silence exceeds each policy's deadline
            detect_before = next(t for t in range(stall, 10**6, cycle) if t - last_seen_b > 2 * cycle) - stall
            detect_after = next(t for t in range(stall, 10**6, cycle) if t - last_seen_a > KEEPALIVE + GRACE) - stall
    return {"agents": agents, "hours": hours, "msgs_before": before, "msgs_after": after,
            "saved_pct": round(100 * (1 - after / before), 1),
            "stall_caught_before": detect_before is not None, "stall_caught_after": detect_after is not None,
            "detect_latency_min_before": detect_before, "detect_latency_min_after": detect_after}
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "watch":
        now = dt.datetime.fromisoformat(a[a.index("--now")+1]) if "--now" in a else dt.datetime.now().astimezone()
        d = int(a[a.index("--deadline-min")+1]) if "--deadline-min" in a else KEEPALIVE + GRACE
        stale = watch([json.loads(l) for l in open(a[1]) if l.strip()], now, d)
        print(json.dumps({"stale": stale})); sys.exit(1 if stale else 0)
    elif a and a[0] == "sim":
        print(json.dumps(sim(int(a[a.index("--seed")+1]) if "--seed" in a else 7)))
    else: print(__doc__)
