"""Correlated-error decoding for echoing voters. In QEC, correlated errors defeat a decoder that assumes
independent flips; the fix is to model the correlation. vote-record.ts shows 50 personas moving together
(before: mostly A; after: all B) - near-copies, not independent evidence.
Target: consensus-engine.ts weighted approval (and build 01's independent-LLR rule).
Candidate: cluster agents by excess agreement on graded history, decode at cluster level
(cluster majority, LLR weight from the cluster's own history). Metric: decision accuracy."""
import sys; sys.path.insert(0, "..")
from common import *
PHI = 1.618033988749895; N, HIST, PROPS = 24, 60, 2000
def world(seed):
    r = vtk.rng(seed); T = HIST + PROPS
    sizes = [8, 6, 4, 2, 1, 1, 1, 1]; cl = np.repeat(np.arange(len(sizes)), sizes)
    cacc = r.uniform(0.55, 0.85, len(sizes)); rho = 0.85      # within-cluster echo probability
    acc = np.clip(cacc[cl] + r.normal(0, 0.03, N), 0.5, 0.95)
    spec = np.zeros(N, bool); spec[r.choice(N, 6, replace=False)] = True
    truth = r.random(T) < .5
    shared = r.random((T, len(sizes))) < cacc                 # cluster's common judgement
    own = r.random((T, N)) < acc
    echo = r.random((T, N)) < rho
    correct = np.where(echo, shared[:, cl], own)
    approve = np.where(correct, truth[:, None], ~truth[:, None])
    return truth, approve, spec
def split(seed):
    t, a, s = world(seed); return (t[:HIST], a[:HIST]), (t[HIST:], a[HIST:]), s
def acc_of(dec, truth): return float((dec == truth).mean())
def current(seed):
    _, (t, a), s = split(seed); w = np.where(s, PHI, 1.) ; return acc_of((a * w).sum(1) / w.sum() >= 2 / 3, t)
def indep_llr(seed):
    (th, ah), (t, a), _ = split(seed); p = ((ah == th[:, None]).sum(0) + 1) / (HIST + 2); w = np.log(p / (1 - p))
    return acc_of((np.where(a, 1, -1) * w).sum(1) >= np.log(2), t)
def clusters(th, ah, thr=0.25):
    """Excess agreement over independence: agree_ij - (p_i p_j + (1-p_i)(1-p_j)). Union-find above thr."""
    c = (ah == th[:, None]); p = c.mean(0); agree = (ah[:, :, None] == ah[:, None, :]).mean(0)
    exc = agree - (np.outer(p, p) + np.outer(1 - p, 1 - p)); par = list(range(len(p)))
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if exc[i, j] > thr: par[f(i)] = f(j)
    return np.array([f(i) for i in range(len(p))])
def candidate(seed):
    (th, ah), (t, a), _ = split(seed); lab = clusters(th, ah); llr = np.zeros(len(t))
    for g in np.unique(lab):
        m = lab == g
        vh = ah[:, m].mean(1) >= .5; pg = ((vh == th).sum() + 1) / (HIST + 2)
        v = a[:, m].mean(1) >= .5; llr += np.where(v, 1, -1) * np.log(pg / (1 - pg))
    return acc_of(llr >= np.log(2), t)
if __name__ == "__main__":
    report([vtk.bench("02 echo-cluster decoder vs current phi/2-3", current, candidate, 30, True, "decision accuracy"),
            vtk.bench("02 echo-cluster decoder vs independent LLR (build 01)", indep_llr, candidate, 30, True, "decision accuracy")], "results.json")
