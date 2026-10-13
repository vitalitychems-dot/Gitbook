"""Bootstrap CIs, paired tests, Benjamini–Hochberg FDR. Pure numpy (no scipy)."""
from __future__ import annotations
import math
import numpy as np

RNG_SEED = 7


def bootstrap_ci(values, n_boot=1000, alpha=0.05, statistic=np.mean, seed=RNG_SEED):
    """Percentile 95% CI (default) for a statistic of 1-d values. Returns (point, lo, hi)."""
    v = np.asarray(values, dtype=float)
    n = len(v)
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    point = float(statistic(v))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    samples = statistic(v[idx], axis=1)
    lo, hi = np.quantile(samples, [alpha / 2, 1 - alpha / 2])
    return point, float(lo), float(hi)


def bootstrap_paired_diff(a, b, n_boot=1000, alpha=0.05, higher_better=True, seed=RNG_SEED):
    """Paired bootstrap of mean(b-a) or mean(a-b) depending on direction.
    Returns dict: delta, lo, hi, p_two_sided (proportion of bootstrap samples on wrong side of 0, *2 capped).
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    assert len(a) == len(b) and len(a) > 0
    d = (b - a) if higher_better else (a - b)  # positive d => candidate better
    n = len(d)
    point = float(d.mean())
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    samples = d[idx].mean(axis=1)
    lo, hi = np.quantile(samples, [alpha / 2, 1 - alpha / 2])
    # two-sided p: fraction of bootstrap means on the opposite side of 0 (or zero), *2
    p_lo = (samples <= 0).mean()
    p_hi = (samples >= 0).mean()
    p = float(min(1.0, 2 * min(p_lo, p_hi)))
    return dict(delta=point, lo=float(lo), hi=float(hi), p=p, n_boot=n_boot)


def mcnemar(base_correct, cand_correct):
    """Exact McNemar (binomial mid-p approximation via normal when b+c large).
    base_correct / cand_correct: bool arrays, True = correct/hit.
    Tests whether candidate differs from baseline on discordant pairs.
    Returns p_two_sided, b (base-only), c (cand-only).
    """
    base = np.asarray(base_correct, dtype=bool)
    cand = np.asarray(cand_correct, dtype=bool)
    b = int((base & ~cand).sum())   # baseline right, cand wrong
    c = int((~base & cand).sum())   # baseline wrong, cand right
    n = b + c
    if n == 0:
        return dict(p=1.0, b=b, c=c, n_discordant=0)
    # Exact binomial two-sided: P(X>=max(b,c) or X<=min) under p=0.5
    # Use continuity-corrected chi2 for n>=25 else exact enumeration
    if n >= 25:
        chi2 = (abs(b - c) - 1) ** 2 / n
        # chi2_1 survival via erfc
        p = math.erfc(math.sqrt(chi2 / 2))
    else:
        k = max(b, c)
        # P(X >= k) * 2, with X~Bin(n,0.5); cap at 1
        # sum_{i=k}^{n} C(n,i) / 2^n
        from math import comb
        tail = sum(comb(n, i) for i in range(k, n + 1)) / (2 ** n)
        p = min(1.0, 2 * tail)
    return dict(p=float(p), b=b, c=c, n_discordant=n)


def wilcoxon_signed_rank(a, b, higher_better=False, seed=RNG_SEED):
    """Two-sided Wilcoxon signed-rank on paired differences.
    For lower-is-better metrics, positive improvement = a-b > 0 (baseline - candidate).
    Uses normal approximation with continuity correction; exact for n_nz <= 20.
    Returns p, W, n_nonzero.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    d = (a - b) if not higher_better else (b - a)  # positive => candidate better
    # drop zeros
    d = d[d != 0]
    n = len(d)
    if n == 0:
        return dict(p=1.0, W=0.0, n_nonzero=0)
    ranks = _rankdata(np.abs(d))
    W_pos = float(ranks[d > 0].sum())
    W_neg = float(ranks[d < 0].sum())
    W = min(W_pos, W_neg)
    if n <= 20:
        p = _wilcoxon_exact(W, n)
    else:
        mean = n * (n + 1) / 4
        # tie correction not needed (continuous-ish floats); var without ties:
        var = n * (n + 1) * (2 * n + 1) / 24
        z = (W - mean + 0.5) / math.sqrt(var)  # continuity toward mean
        p = float(min(1.0, 2 * (0.5 * math.erfc(abs(z) / math.sqrt(2)))))
    return dict(p=p, W=W, W_pos=W_pos, W_neg=W_neg, n_nonzero=n)


def _rankdata(x):
    """Average ranks for ties, 1-based."""
    x = np.asarray(x, dtype=float)
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(len(x), dtype=float)
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and x[order[j + 1]] == x[order[i]]:
            j += 1
        avg = 0.5 * (i + j) + 1  # 1-based average
        ranks[order[i:j + 1]] = avg
        i = j + 1
    return ranks


def _wilcoxon_exact(W, n):
    """Exact two-sided p for Wilcoxon signed-rank statistic W = min(W+, W-)."""
    # Generate all 2^n sign assignments via DP: number of subsets with each sum of ranks
    # ranks 1..n
    max_s = n * (n + 1) // 2
    dp = np.zeros(max_s + 1, dtype=np.float64)
    dp[0] = 1.0
    for r in range(1, n + 1):
        ndp = dp.copy()
        ndp[r:] += dp[:-r]
        dp = ndp
    total = 2 ** n
    # two-sided: P(min(S, max_s-S) <= W) = 2 * P(S <= W) but careful not to double-count mid
    cdf = dp[: int(W) + 1].sum()
    p = 2 * cdf / total
    return float(min(1.0, p))


def benjamini_hochberg(pvalues, alpha=0.05):
    """BH FDR correction. Returns list of (reject, q_value) aligned with input.
    q_value = BH-adjusted p.
    """
    m = len(pvalues)
    if m == 0:
        return []
    order = np.argsort(pvalues)
    ranked = np.asarray(pvalues, dtype=float)[order]
    q = np.empty(m, dtype=float)
    prev = 1.0
    for i in range(m - 1, -1, -1):
        adj = ranked[i] * m / (i + 1)
        prev = min(prev, adj)
        q[i] = prev
    out_q = np.empty(m, dtype=float)
    out_q[order] = np.clip(q, 0, 1)
    reject = out_q <= alpha
    return list(zip(reject.tolist(), out_q.tolist()))


def percentile(values, p):
    return float(np.percentile(np.asarray(values, dtype=float), p))
