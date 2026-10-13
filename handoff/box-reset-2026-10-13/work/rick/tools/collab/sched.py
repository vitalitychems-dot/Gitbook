#!/usr/bin/env python3
"""Mesh scheduler: dependency + gate-order aware list scheduler. Each task expands into its gate chain
(work -> moderator -> tessera -> security -> build? -> father); each lane runs one step at a time.
Priority = critical-path length (longest remaining chain), tie-break Father priority then age."""
import json, sys, heapq, collections
GATES = ["moderator", "tessera", "security", "build", "father"]
def expand(tasks, gate_cost):
    steps = {}
    for t in tasks:
        chain = [(t["id"] + ":work", t["lane"], t["cost"])]
        for g in GATES:
            if g == "build" and not t.get("code"): continue
            chain.append((f'{t["id"]}:{g}', g, gate_cost.get(g, 1)))
        prev = [d + ":father" for d in t.get("needs", [])]
        for sid, lane, c in chain:
            steps[sid] = {"lane": lane, "cost": c, "deps": prev, "prio": t.get("prio", 0)}; prev = [sid]
    return steps
def cpl(steps):
    succ = collections.defaultdict(list)
    for s, v in steps.items():
        for d in v["deps"]: succ[d].append(s)
    memo = {}
    def f(s):
        if s not in memo: memo[s] = steps[s]["cost"] + max((f(x) for x in succ[s]), default=0)
        return memo[s]
    return {s: f(s) for s in steps}
def simulate(steps, policy):
    """event sim; returns makespan, finish times, order. policy: 'cp' or 'fifo'"""
    if any(d not in steps for v in steps.values() for d in v["deps"]): raise ValueError("unknown dependency")
    try: pri = cpl(steps)
    except RecursionError: raise ValueError("cycle")
    idx = {s: i for i, s in enumerate(steps)}
    done, fin, t, busy, order = set(), {}, 0, {}, []
    running = []  # (end, step)
    while len(done) < len(steps):
        ready = [s for s in steps if s not in done and s not in busy.values() and all(d in done for d in steps[s]["deps"])]
        key = (lambda s: (-pri[s], -steps[s]["prio"], idx[s])) if policy == "cp" else (lambda s: idx[s])
        for s in sorted(ready, key=key):
            ln = steps[s]["lane"]
            if ln not in busy: busy[ln] = s; heapq.heappush(running, (t + steps[s]["cost"], s)); order.append((t, s))
        if not running: raise ValueError("cycle or deadlock")
        t, s = heapq.heappop(running); done.add(s); fin[s] = t; del busy[steps[s]["lane"]]
    return t, fin, order
if __name__ == "__main__":
    d = json.load(open(sys.argv[1])); st = expand(d["tasks"], d.get("gate_cost", {}))
    for p in ("fifo", "cp"):
        m, fin, order = simulate(st, p); print(p, "makespan", m)
    print("next per lane (cp):"); seen = set()
    for t0, s in simulate(st, "cp")[2]:
        if st[s]["lane"] not in seen: seen.add(st[s]["lane"]); print(f'  {st[s]["lane"]}: {s} @t={t0}')
