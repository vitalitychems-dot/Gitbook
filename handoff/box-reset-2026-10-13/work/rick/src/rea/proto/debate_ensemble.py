"""REA from HKUDS/Vibe-Trading 'multi-agent debate' -> Simons forecast (science only, no trading).
Each forecaster 'argues'; votes are weighted by trailing out-of-sample skill (inverse MAE over last W days, known at t)."""
import sys, numpy as np, collections
sys.path.insert(0, "/workspace/rick/tools/simons"); import simons as S
def preds(test_start="2025-10-12", test_end="2026-10-11"):
    days, cnt, eng, mx, kp = S.load(); names, X, y, g = S.features(days, cnt, eng, mx, kp)
    s = days.index(test_start) - 120; e = days.index(test_end) + 1; start = 100   # 120 extra warmup days for skill weights
    tr = np.arange(start, days.index(test_start) - 1); r, p = S.edge_pvalues(np.nan_to_num(X[tr]), (y - np.append(np.full(29, np.nan), np.convolve(g, np.ones(30)/30, "valid")))[tr])
    surv = np.where(S.bh(p, .05))[0]; P = collections.defaultdict(list); truth = []
    for i, t in enumerate(range(s - 1, e - 1)):
        if i % 7 == 0:
            Xa = np.nan_to_num(X[np.arange(start, t)]); ma = S.ridge_counts(Xa, y[start:t], 1.0); ms = S.ridge_counts(Xa[:, surv], y[start:t], .1)
        xt = np.nan_to_num(X[t:t+1]); truth.append(g[t+1])
        P["mean7"].append(g[t-6:t+1].mean()); P["mean30"].append(g[t-29:t+1].mean())
        P["ridge_all"].append(float(ma(xt)[0])); P["ridge_survivors"].append(float(ms(xt[:, surv])[0]))
    return {k: np.array(v) for k, v in P.items()}, np.array(truth), 121
def debate(P, truth, W=30, power=2):
    ks = list(P); M = np.stack([P[k] for k in ks]); E = np.abs(M - truth); out = np.empty(len(truth))
    for t in range(len(truth)):
        if t < W: out[t] = M[:, t].mean(); continue
        w = 1 / (E[:, t-W:t].mean(1) ** power); out[t] = (w * M[:, t]).sum() / w.sum()   # only errors of days already observed
    return out
if __name__ == "__main__":
    P, truth, off = preds(); eq = np.mean([P[k] for k in P], 0)
    T = slice(off - 1, None)
    for W in (14, 30, 60):
        for pw in (1, 2):
            d = debate(P, truth, W, pw); print(f"W={W} p={pw} debate MAE={np.abs(d-truth)[T].mean():.3f}")
    print(f"equal ensemble MAE={np.abs(eq-truth)[T].mean():.3f} n={len(truth[T])}")
