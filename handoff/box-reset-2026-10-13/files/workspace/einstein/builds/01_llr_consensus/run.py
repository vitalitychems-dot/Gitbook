"""Repetition-code MAP decoding for council votes (Nitzan-Paroush / BSC log-likelihood weights).
Target: consensus-engine.ts computeWeightedApprovalRate (phi weight 1.618 for specialists, approve >= 2/3).
Candidate: weight_i = log(a_i/(1-a_i)) from each agent's graded history (Beta(1,1) posterior), approve iff
posterior P(good) >= 2/3 (same conservatism as the BFT 2/3 rule). Metric: decision accuracy (higher better)."""
import sys; sys.path.insert(0, "..")
from common import *
PHI = 1.618033988749895; N_AG, N_SPEC, HIST, PROPS = 24, 6, 30, 2000
def world(seed):
    r = vtk.rng(seed)
    acc = r.uniform(0.5, 0.85, N_AG); spec = np.zeros(N_AG, bool); spec[:N_SPEC] = True
    acc[spec] = r.uniform(0.65, 0.9, N_SPEC)          # specialists really are better on average
    acc[N_SPEC:N_SPEC + 4] = r.uniform(0.35, 0.5, 4)   # a few miscalibrated agents (worse than chance)
    hist_ok = r.binomial(HIST, acc); a_hat = (hist_ok + 1) / (HIST + 2)
    truth = r.random(PROPS) < 0.5
    correct = r.random((PROPS, N_AG)) < acc
    approve = np.where(correct, truth[:, None], ~truth[:, None])
    return truth, approve, spec, a_hat
def baseline(seed):
    truth, approve, spec, _ = world(seed); w = np.where(spec, PHI, 1.0) * (0.85 + 0.5 * 0.15)
    rate = (approve * w).sum(1) / w.sum(); return float(((rate >= 2 / 3) == truth).mean())
def candidate(seed):
    truth, approve, spec, a = world(seed); w = np.log(a / (1 - a))
    llr = (np.where(approve, 1, -1) * w).sum(1); return float(((llr >= np.log(2)) == truth).mean())
def baseline_majority(seed):  # same 2/3 rule replaced by simple majority, to separate threshold from weights
    truth, approve, spec, _ = world(seed); w = np.where(spec, PHI, 1.0)
    return float((((approve * w).sum(1) / w.sum() >= .5) == truth).mean())
if __name__ == "__main__":
    R = [vtk.bench("01 LLR consensus vs phi/2-3 (current)", baseline, candidate, 30, True, "decision accuracy"),
         vtk.bench("01 LLR consensus vs phi weights at 1/2 (stronger baseline)", baseline_majority, candidate, 30, True, "decision accuracy")]
    report(R, "results.json")
