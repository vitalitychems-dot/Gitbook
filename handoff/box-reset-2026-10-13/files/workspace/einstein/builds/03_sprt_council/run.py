"""Sequential syndrome reading: Wald SPRT over council votes. Stop calling agents once the
log-likelihood ratio crosses +/-A (A = log((1-alpha)/alpha)). Target: consensus-engine.ts polls all 24
personas (one LLM call each) for every proposal. Metrics: LLM calls per decision (lower better) and accuracy."""
import sys; sys.path.insert(0, "..")
sys.path.insert(0, "../01_llr_consensus")
from common import *
import importlib; b1 = importlib.import_module("run")
ALPHA = 0.01; A = np.log((1 - ALPHA) / ALPHA)
def sprt(seed):
    truth, approve, spec, a = b1.world(seed); w = np.log(a / (1 - a)); r = vtk.rng(seed + 7)
    calls = []; dec = []
    for t in range(len(truth)):
        order = r.permutation(len(w)); s = 0.; k = 0
        for k, i in enumerate(order, 1):
            s += w[i] if approve[t, i] else -w[i]
            if abs(s) >= A: break
        calls.append(k); dec.append(s >= np.log(2))
    return np.mean(calls), float((np.array(dec) == truth).mean())
calls_all = lambda seed: 24.0
calls_sprt = lambda seed: sprt(seed)[0]
acc_sprt = lambda seed: sprt(seed)[1]
if __name__ == "__main__":
    report([vtk.bench("03 SPRT early stop: calls per decision", calls_all, calls_sprt, 20, False, "LLM calls/decision"),
            vtk.bench("03 SPRT accuracy vs current full poll phi/2-3", b1.baseline, acc_sprt, 20, True, "decision accuracy"),
            vtk.bench("03 SPRT accuracy vs full-poll LLR (build 01)", b1.candidate, acc_sprt, 20, True, "decision accuracy")], "results.json")
