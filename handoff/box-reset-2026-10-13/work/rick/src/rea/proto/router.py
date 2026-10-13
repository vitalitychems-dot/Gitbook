"""REA from tashfeenahmed/freellmapi -> collab/mesh: route each request to the best backend that is under its quota,
fail over on rate-limit, put limited backends on cooldown, track per-key usage. Offline simulation only (no keys, no network)."""
import random
class Backend:
    def __init__(s, name, rpm, quality, fail=0.02): s.name, s.rpm, s.q, s.fail, s.used, s.cool = name, rpm, quality, fail, {}, -1
    def call(s, minute, rng):
        n = s.used.get(minute, 0)
        if n >= s.rpm: return "429"
        s.used[minute] = n + 1
        return "err" if rng.random() < s.fail else "ok"
def fresh(): return [Backend("A", 20, .9), Backend("B", 10, .8), Backend("C", 30, .6, .05), Backend("D", 5, .95)]
def run(policy, reqs_per_min=50, minutes=60, seed=0):
    rng = random.Random(seed); bs = fresh(); ok = att = qual = 0; i = 0
    for m in range(minutes):
        for _ in range(rng.randint(reqs_per_min - 15, reqs_per_min + 15)):
            if policy == "single": order = [bs[0]]
            elif policy == "roundrobin": i += 1; order = [bs[i % 4]]
            else:  # router: best quality first among backends with known headroom and not cooling, fail over down the list
                order = sorted([b for b in bs if b.cool < m and b.used.get(m, 0) < b.rpm], key=lambda b: -b.q)
            for b in order:
                att += 1; r = b.call(m, rng)
                if r == "ok": ok += 1; qual += b.q; break
                if r == "429": b.cool = m      # cooldown for rest of this minute
    tot = sum(1 for _ in range(1)) and None
    return ok, att, qual
if __name__ == "__main__":
    for p in ("single", "roundrobin", "router"):
        rs = [run(p, seed=s) for s in range(20)]; n = 60 * 50
        ok = sum(r[0] for r in rs) / 20; att = sum(r[1] for r in rs) / 20; q = sum(r[2] for r in rs) / max(sum(r[0] for r in rs), 1) * 20 / 20
        print(f"{p:10s} served {ok/n:.1%} of ~{n} req/h  calls/served {att/max(ok,1):.2f}  mean quality {q:.3f}")
