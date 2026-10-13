"""Repeated syndrome rounds for alerts. Surface codes measure stabilizers for d rounds because single
measurements are noisy; a flip is trusted only when it persists in time. Same here.
Target: anomaly-detection.ts runAnomalyCheck: one 30 s snapshot vs fixed threshold (cpuWarning 0.70)
opens an anomaly; the next snapshot below closes it -> flapping on noise.
Candidate: open when >=2 of the last 3 rounds exceed the threshold; close only when 0 of the last 3 do.
Simulation: one day of 30 s ticks (2880), AR(1) load around 0.58 (sd 0.07), 6 real incidents of 20-60
ticks at +0.22. Metrics: false opens/day (lower better), missed incidents, mean detection delay (ticks)."""
import sys; sys.path.insert(0, "..")
from common import *
THR, T = 0.70, 2880
def day(seed):
    r = vtk.rng(seed); x = np.zeros(T); e = 0
    for t in range(T): e = 0.7 * e + r.normal(0, 0.07 * np.sqrt(1 - .49)); x[t] = 0.58 + e
    inc = np.zeros(T, bool); starts = np.sort(r.choice(np.arange(50, T - 80, 100), 6, replace=False)); spans = []
    for s in starts:
        L = r.integers(20, 61); inc[s:s + L] = True; x[s:s + L] += 0.22; spans.append((s, s + L))
    return x, inc, spans
def run(x, rule):
    open_ = False; opens = []; hi = x >= THR
    for t in range(T):
        if rule == "single":
            if hi[t] and not open_: open_ = True; opens.append(t)
            elif not hi[t]: open_ = False
        else:
            w = hi[max(0, t - 2):t + 1].sum()
            if not open_ and w >= 2: open_ = True; opens.append(t)
            elif open_ and w == 0: open_ = False
    return opens
def score(seed, rule):
    x, inc, spans = day(seed); o = run(x, rule)
    false = sum(1 for t in o if not inc[max(0, t - 2):t + 1].any())
    delays = []; missed = 0
    for s, e in spans:
        d = [t - s for t in o if s <= t < e + 3]
        if d: delays.append(min(d))
        else: missed += 1
    return false, missed, (np.mean(delays) if delays else np.nan)
if __name__ == "__main__":
    R = [vtk.bench("07 2-of-3 rounds + hysteresis vs single snapshot", lambda s: score(s, "single")[0], lambda s: score(s, "rep")[0], 30, False, "false opens/day"),
         vtk.bench("07 missed incidents (of 6)", lambda s: score(s, "single")[1], lambda s: score(s, "rep")[1], 30, False, "missed incidents/day"),
         vtk.bench("07 detection delay", lambda s: score(s, "single")[2], lambda s: score(s, "rep")[2], 30, False, "ticks (30 s) to open")]
    report(R, "results.json")
