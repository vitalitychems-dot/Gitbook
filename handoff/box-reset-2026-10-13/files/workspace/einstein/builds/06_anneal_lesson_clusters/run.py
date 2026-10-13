"""Lesson clustering as an Ising/Potts correlation-clustering problem solved by annealing.
Target: memory/distill.ts distillLessons: first-fit greedy; a record joins the first cluster whose UNION of
tokens shares >=3 tokens (or Jaccard>=0.34). Unions grow, so clusters snowball and swallow unrelated lessons.
Candidate: Potts energy E = -sum_{i<j} (J_ij - tau) [c_i == c_j], J = record-record Jaccard, minimised by
single-label Metropolis annealing. tau fixed on calibration seed 0 (not a bench seed).
Data: records cut from real TESSERA docs paragraphs (30 source paragraphs per run, 2-6 records each:
input = 8-word span, output = 20-word span with 20% dropout). Metric: pairwise F1 vs true source."""
import sys, re; sys.path.insert(0, "..")
from common import *
STOP = set("the and for with that this from into over how are was were been being before after anyone them they you your our not but can could should would about what when where which who why has have had does did get got its via per than then also only just all any each use used using within without across example pattern".split())
def mtok(t): return [w for w in re.findall(r"[a-z0-9]+", t.lower()) if len(w) >= 3 and w not in STOP]
def records(seed):
    r = vtk.rng(seed); P = paragraphs(); src = r.choice(len(P), 30, replace=False); R, y = [], []
    for s in src:
        t = tok(P[s])
        for _ in range(r.integers(2, 7)):
            a = r.integers(0, max(1, len(t) - 8)); b = r.integers(0, max(1, len(t) - 20))
            out = [w for w in t[b:b + 20] if r.random() > .2]
            R.append(" ".join(t[a:a + 8]) + "\n" + " ".join(out)); y.append(s)
    o = r.permutation(len(R)); return [R[i] for i in o], np.array(y)[o]
def distill_baseline(R):
    cl = []; lab = []
    for i, rec in enumerate(R):
        T = set(mtok(rec)); placed = False
        for k, c in enumerate(cl):
            U = set(mtok("\n".join(R[j] for j in c)))
            inter = len(T & U)
            if inter >= 3 or (inter / len(T | U) if T | U else 0) >= .34:
                c.append(i); lab.append(k); placed = True; break
        if not placed: cl.append([i]); lab.append(len(cl) - 1)
    return np.array(lab)
def potts(R, tau, seed, sweeps=60):
    r = vtk.rng(seed); S = [set(mtok(x)) for x in R]; n = len(R)
    J = np.array([[len(a & b) / max(1, len(a | b)) for b in S] for a in S]) - tau; np.fill_diagonal(J, 0)
    c = np.arange(n)
    for sw in range(sweeps):
        T = 0.5 * (0.005 / 0.5) ** (sw / (sweeps - 1))
        for i in r.permutation(n):
            labs = np.unique(np.append(c[J[i] > 0], [c[i], n + i]))   # neighbours' labels, own, a fresh one
            g = np.array([J[i][c == l].sum() for l in labs])           # energy gain of joining l
            p = np.exp((g - g.max()) / T); c[i] = labs[r.choice(len(labs), p=p / p.sum())]
    return c
def single_link(R, tau):
    S = [set(mtok(x)) for x in R]; n = len(R); par = list(range(n))
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if len(S[i] & S[j]) / max(1, len(S[i] | S[j])) > tau: par[f(i)] = f(j)
    return np.array([f(i) for i in range(n)])
def ctrl(seed): R, y = records(seed); return f1(single_link(R, TAU), y)
def f1(lab, y):
    same_p = lab[:, None] == lab[None]; same_t = y[:, None] == y[None]; m = ~np.eye(len(y), dtype=bool)
    tp = (same_p & same_t & m).sum(); fp = (same_p & ~same_t & m).sum(); fn = (~same_p & same_t & m).sum()
    return 2 * tp / max(1, 2 * tp + fp + fn)
def calibrate():
    R, y = records(0); return max(np.arange(0.02, 0.3, 0.02), key=lambda t: f1(potts(R, t, 0), y))
TAU = None
def base(seed): R, y = records(seed); return f1(distill_baseline(R), y)
def cand(seed): R, y = records(seed); return f1(potts(R, TAU, seed), y)
if __name__ == "__main__":
    TAU = float(calibrate()); print("tau (calibrated on seed 0) =", TAU)
    R, y = records(1); print("seed1 clusters: true", len(set(y)), "baseline", len(set(distill_baseline(R))), "potts", len(set(potts(R, TAU, 1))))
    report([vtk.bench("06 Potts-anneal lesson clustering vs distillLessons", base, cand, 15, True, "pairwise F1"),
            vtk.bench("06 Potts-anneal vs single-link at same tau (non-quantum control)", ctrl, cand, 15, True, "pairwise F1")], "results.json")
