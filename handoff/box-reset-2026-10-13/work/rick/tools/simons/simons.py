#!/usr/bin/env python3
"""Simons-style forecasting lab for Tessera's Eye (science only: NO trading/finance, NO person tracking).
Target: next-day global USGS M4.5+ count (band low/med/high + exact-count MAE).
Pipeline: space-time heat maps -> mass features -> train-only screening w/ Bonferroni & BH-FDR -> walk-forward ensemble.
'Quantum-inspired' features are classical linear algebra on normalized grids (amplitude overlaps). NOT quantum."""
import csv, json, os, math, zlib, struct, datetime, collections, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, "data")
NLAT, NLON = 18, 36  # 10-degree cells

# ---------- data ----------
def load(end="2026-10-12"):
    rows = list(csv.DictReader(open(os.path.join(D, "quakes.csv"))))
    d0 = datetime.date.fromisoformat(min(r["date"] for r in rows)) + datetime.timedelta(1)  # first day may be partial
    d1 = datetime.date.fromisoformat(end) - datetime.timedelta(1)                           # last day partial
    days = [(d0 + datetime.timedelta(i)).isoformat() for i in range((d1 - d0).days + 1)]
    ix = {d: i for i, d in enumerate(days)}
    cnt = np.zeros((len(days), NLAT, NLON)); eng = np.zeros_like(cnt); mx = np.full(len(days), 4.5)
    for r in rows:
        i = ix.get(r["date"])
        if i is None: continue
        la = min(int((float(r["lat"]) + 90) // 10), NLAT - 1); lo = min(int((float(r["lon"]) + 180) // 10), NLON - 1)
        m = float(r["mag"]); cnt[i, la, lo] += 1; eng[i, la, lo] += 10 ** (1.5 * (m - 4.5)); mx[i] = max(mx[i], m)
    kpj = json.load(open(os.path.join(D, "kp_daily.json")))
    kp = np.array([kpj.get(d, [np.nan])[0] for d in days], float)
    kp = np.where(np.isnan(kp), np.nanmean(kp), kp)  # Kp file lags a few days; fill (only affects last ~days)
    return days, cnt, eng, mx, kp

# ---------- heat map PNG (pure python) ----------
def _png(path, rgb):  # rgb: HxWx3 uint8
    h, w, _ = rgb.shape; raw = b"".join(b"\x00" + rgb[y].tobytes() for y in range(h))
    ck = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n" + ck(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + ck(b"IDAT", zlib.compress(raw, 9)) + ck(b"IEND", b""))
def _cmap(v):  # v in [0,1] -> 'inferno-ish'
    v = np.clip(v, 0, 1)[..., None]; a = np.array([0, 0, 4.]); b = np.array([187, 55, 84.]); c = np.array([252, 255, 164.])
    return np.where(v < .5, a + (b - a) * v * 2, b + (c - b) * (v - .5) * 2).astype(np.uint8)
def render(cnt, path, last=365, s=12):
    world = np.log1p(cnt[-last:].sum(0))[::-1]                     # top panel: lat x lon, north up
    hov = np.log1p(cnt[-last:].sum(2)).T[::-1]                      # bottom panel: lat x day (space-time)
    top = np.kron(_cmap(world / world.max()), np.ones((s, s, 1), np.uint8))
    bot = np.kron(_cmap(hov / hov.max()), np.ones((s, 1, 1), np.uint8))
    W = max(top.shape[1], bot.shape[1]); pad = lambda a: np.pad(a, ((0, 0), (0, W - a.shape[1]), (0, 0)))
    img = np.concatenate([pad(top), np.full((6, W, 3), 255, np.uint8), pad(bot)]); _png(path, img); return img.shape

# ---------- quantum-inspired (classical!) amplitude interference ----------
def amplitudes(g):  # g: (T, cells) nonneg -> unit vectors psi = sqrt(p)
    p = g / np.maximum(g.sum(1, keepdims=True), 1e-12); return np.sqrt(p)
def interference(psi, lag):  # fidelity |<psi_t|psi_{t-lag}>|^2 ; the cross term of |psi_t+psi_{t-lag}|^2
    out = np.full(len(psi), np.nan); out[lag:] = (psi[lag:] * psi[:-lag]).sum(1) ** 2; return out

# ---------- features ----------
def roll(x, w, f):
    out = np.full(len(x), np.nan)
    for t in range(w - 1, len(x)): out[t] = f(x[t - w + 1:t + 1])
    return out
def lag(x, k): out = np.full(len(x), np.nan); out[k:] = x[:len(x) - k]; return out
def ewma(x, a):
    out = np.empty(len(x)); m = x[0]
    for t, v in enumerate(x): m = a * v + (1 - a) * m; out[t] = m
    return out
def features(days, cnt, eng, mx, kp):
    T = len(days); g = cnt.sum((1, 2)); F = {}
    flat = cnt.reshape(T, -1); eflat = eng.reshape(T, -1)
    for k in range(0, 15): F[f"g_lag{k}"] = lag(g, k)
    for w in (3, 7, 14, 30, 60, 90):
        F[f"g_mean{w}"] = roll(g, w, np.mean); F[f"g_std{w}"] = roll(g, w, np.std)
        F[f"g_max{w}"] = roll(g, w, np.max); F[f"g_dev{w}"] = g - F[f"g_mean{w}"]
    for a in (.05, .1, .2, .3, .5, .7): F[f"g_ewma{a}"] = ewma(g, a)
    le = np.log1p(eflat.sum(1))
    for k in range(4): F[f"logE_lag{k}"] = lag(le, k); F[f"maxmag_lag{k}"] = lag(mx, k)
    for thr in (5.5, 6.0, 6.5):
        b = (mx >= thr).astype(float)
        for w in (1, 3, 7, 14, 30): F[f"m{thr}_in{w}"] = roll(b, w, np.sum)
    # regions: top-20 active cells (chosen on first 60% of days only -> no leakage) + 6 lat bands
    top = np.argsort(-flat[:int(T * .6)].sum(0))[:20]
    for j, c in enumerate(top):
        x = flat[:, c]; F[f"c{c}_lag0"] = x; F[f"c{c}_lag1"] = lag(x, 1); F[f"c{c}_m7"] = roll(x, 7, np.mean); F[f"c{c}_dev30"] = x - roll(x, 30, np.mean)
    lb = cnt.sum(2).reshape(T, 6, 3).sum(2)
    for j in range(6): F[f"latband{j}_m3"] = roll(lb[:, j], 3, np.mean); F[f"latband{j}_m14"] = roll(lb[:, j], 14, np.mean)
    # regional cross-correlations (30d rolling) among top-5 cells
    for a in range(5):
        for b in range(a + 1, 5):
            xa, xb = flat[:, top[a]], flat[:, top[b]]
            F[f"xcorr{top[a]}_{top[b]}"] = np.array([np.nan if t < 29 or xa[t-29:t+1].std() == 0 or xb[t-29:t+1].std() == 0 else np.corrcoef(xa[t-29:t+1], xb[t-29:t+1])[0, 1] for t in range(T)])
    # Kp (geomagnetic) lags/rolls
    for k in range(8): F[f"kp_lag{k}"] = lag(kp, k)
    for w in (3, 7, 27): F[f"kp_mean{w}"] = roll(kp, w, np.mean)
    # heat-map shape features
    p = flat / np.maximum(flat.sum(1, keepdims=True), 1)
    ent = -(np.where(p > 0, p * np.log(p + 1e-12), 0)).sum(1)
    act = (flat > 0).sum(1).astype(float)
    F["hm_entropy"] = ent; F["hm_active"] = act; F["hm_maxcell"] = flat.max(1); F["hm_entropy_m7"] = roll(ent, 7, np.mean)
    F["hm_active_m7"] = roll(act, 7, np.mean); F["hm_conc"] = (p ** 2).sum(1)
    dec = np.zeros_like(flat, float); acc = np.zeros(flat.shape[1])
    for t in range(T): acc = .7 * acc + flat[t]; dec[t] = acc
    F["hm_decay_max"] = dec.max(1); F["hm_decay_sum"] = dec.sum(1)
    # quantum-inspired interference features (classical)
    psi = amplitudes(flat.astype(float)); psid = amplitudes(dec); psie = amplitudes(eflat)
    for k in (1, 2, 3, 5, 7, 14): F[f"qi_fid_lag{k}"] = interference(psi, k); F[f"qi_decfid_lag{k}"] = interference(psid, k)
    for k in (1, 3, 7): F[f"qi_Efid_lag{k}"] = interference(psie, k)
    clim = amplitudes(np.cumsum(flat, 0).astype(float))  # overlap with expanding climatology (past only)
    F["qi_fid_clim"] = (psi * lag2d(clim, 1)).sum(1) ** 2
    F["qi_fid_clim_m7"] = roll(np.nan_to_num(F["qi_fid_clim"], nan=np.nanmean(F["qi_fid_clim"])), 7, np.mean)
    # calendar (catalog artifacts)
    dow = np.array([datetime.date.fromisoformat(d).weekday() for d in days])
    for k in range(7): F[f"dow_next{k}"] = ((dow + 1) % 7 == k).astype(float)
    F["doy_sin"] = np.sin(2 * np.pi * np.arange(T) / 365.25); F["doy_cos"] = np.cos(2 * np.pi * np.arange(T) / 365.25)
    names = sorted(F); X = np.column_stack([F[n] for n in names]); y = np.append(g[1:], np.nan)  # y[t] = count at t+1
    return names, X, y, g
def lag2d(a, k): out = np.full(a.shape, np.nan); out[k:] = a[:-k]; return out

# ---------- stats ----------
def _ncdf(z): return 0.5 * math.erfc(-z / math.sqrt(2))
def edge_pvalues(X, y):
    """Spearman-ish (rank) correlation of each feature with next-day surprise (y - 30d mean); p from Fisher z
    with Bartlett effective-n for autocorrelation (honest for persistent series)."""
    rk = lambda v: np.argsort(np.argsort(v)).astype(float)
    ps, rs = [], []
    yr = rk(y)
    def ac1(v): v = v - v.mean(); return float((v[1:] * v[:-1]).sum() / max((v * v).sum(), 1e-12))
    for j in range(X.shape[1]):
        x = X[:, j]
        if np.std(x) == 0: ps.append(1.0); rs.append(0.0); continue
        xr = rk(x); r = float(np.corrcoef(xr, yr)[0, 1]); a, b = ac1(xr), ac1(yr)
        neff = max(10, len(x) * (1 - a * b) / (1 + a * b))
        z = math.atanh(max(min(r, .999999), -.999999)) * math.sqrt(neff - 3); ps.append(2 * (1 - _ncdf(abs(z)))); rs.append(r)
    return np.array(rs), np.array(ps)
def bh(p, q=.05):
    m = len(p); o = np.argsort(p); thr = q * np.arange(1, m + 1) / m; ok = p[o] <= thr
    keep = np.zeros(m, bool)
    if ok.any(): keep[o[:np.max(np.where(ok)[0]) + 1]] = True
    return keep
def ridge(Xtr, ytr, lam):
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-9; Z = (Xtr - mu) / sd; ym = ytr.mean()
    w = np.linalg.solve(Z.T @ Z + lam * len(Z) * np.eye(Z.shape[1]), Z.T @ (ytr - ym))
    f = lambda Xn: ym + ((Xn - mu) / sd) @ w
    return f
def ridge_counts(Xtr, ytr_counts, lam):  # fit on log1p, Duan smearing for unbiased count back-transform (train-only)
    f = ridge(Xtr, np.log1p(ytr_counts), lam); smear = float(np.mean(np.exp(np.log1p(ytr_counts) - f(Xtr))))
    return lambda Xn: (1 + 0 * f(Xn)) * (np.exp(f(Xn)) * smear - 1)
def band(x, q): return np.where(x <= q[0], 0, np.where(x <= q[1], 1, 2))
def wilson(k, n, z=1.96):
    p = k / n; c = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n); return round(c - h, 3), round(c + h, 3)
def sign_test(a_right, b_right):  # exact two-sided McNemar on discordant pairs
    b = int(np.sum(a_right & ~b_right)); c = int(np.sum(~a_right & b_right)); n = b + c
    if n == 0: return 1.0, b, c
    k = min(b, c); p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n; return min(1.0, 2 * p), b, c

# ---------- experiment ----------
def experiment(names, X, y, g, days, test_start, test_end, q=None, refit_every=7):
    T = len(days); s = days.index(test_start); e = days.index(test_end) + 1
    start = 100  # first rows have NaN warmups
    surprise = y - np.append(np.full(29, np.nan), np.convolve(g, np.ones(30) / 30, "valid"))  # y_{t+1} - mean30_t
    # screening on train only (rows whose TARGET day < test_start, i.e. t+1 < s)
    tr = np.arange(start, s - 1); Xs = np.nan_to_num(X[tr]); ys = surprise[tr]
    r, p = edge_pvalues(Xs, ys); m = len(p)
    bonf = p < .05 / m; fdr = bh(p, .05)
    surv = np.where(fdr)[0]
    if q is None: q = tuple(np.sort(g[start:s])[[ (s - start) // 3, 2 * (s - start) // 3 ]])
    preds = collections.defaultdict(list); truth = []
    model_s = model_a = None; ly = np.log1p(y)
    for i, t in enumerate(range(s - 1, e - 1)):  # predict day t+1 from info at t
        if i % refit_every == 0:
            trn = np.arange(start, t)  # targets up to day t (known at t)
            Xa = np.nan_to_num(X[trn])
            model_a = ridge_counts(Xa, y[trn], 1.0)
            model_s = ridge_counts(Xa[:, surv], y[trn], 0.1) if len(surv) else None
        xt = np.nan_to_num(X[t:t + 1]); truth.append(g[t + 1])
        preds["persistence"].append(g[t]); preds["mean7"].append(g[t - 6:t + 1].mean())
        preds["mean30"].append(g[t - 29:t + 1].mean())
        preds["ridge_all"].append(float(model_a(xt)[0]))
        preds["ridge_survivors"].append(float(model_s(xt[:, surv])[0]) if model_s else g[t - 29:t + 1].mean())
    P = {k: np.array(v) for k, v in preds.items()}; truth = np.array(truth)
    P["ensemble"] = np.mean([P["ridge_survivors"], P["ridge_all"], P["mean30"], P["mean7"]], 0)
    tb = band(truth, q); out = {}
    for k, v in P.items():
        right = band(v, q) == tb; out[k] = {"band_acc": round(float(right.mean()), 3), "ci95": wilson(int(right.sum()), len(right)),
                                            "mae": round(float(np.abs(v - truth).mean()), 2), "_right": right}
    for k in out:
        if k != "persistence":
            pv, b, c = sign_test(out[k]["_right"], out["persistence"]["_right"]); out[k]["vs_persistence_p"] = round(pv, 3)
    em7 = np.abs(P["mean7"] - truth)
    for k in out:
        if k != "mean7":
            ek = np.abs(P[k] - truth); pv, b, c = sign_test(ek < em7, ek > em7); out[k]["mae_vs_mean7_signtest_p"] = round(pv, 4)
    for k in out: out[k].pop("_right")
    top = np.argsort(p)[:15]
    return {"window": [test_start, test_end], "n_test": len(truth), "bands": [float(q[0]), float(q[1])], "n_features": m,
            "n_train_rows_screen": len(tr), "bonferroni_survivors": [names[j] for j in np.where(bonf)[0]],
            "fdr_survivors": [names[j] for j in surv],
            "top15": [[names[j], round(float(r[j]), 3), float("%.2g" % p[j])] for j in top], "models": out}
def eye_terciles(g, days, test_start, ntrain):  # identical to tessera-eye/predict.py terciles
    s = days.index(test_start); v = sorted(g[s - ntrain:s]); return (v[len(v) // 3], v[2 * len(v) // 3])
def run():
    days, cnt, eng, mx, kp = load(); names, X, y, g = features(days, cnt, eng, mx, kp)
    shp = render(cnt, os.path.join(H, "heatmap.png"))
    A = experiment(names, X, y, g, days, "2026-07-13", "2026-10-11", q=eye_terciles(g, days, "2026-07-13", 273))
    B = experiment(names, X, y, g, days, "2025-10-12", "2026-10-11")
    res = {"days": [days[0], days[-1], len(days)], "events": int(cnt.sum()), "heatmap_px": list(shp),
           "A_same_window_as_eye": A, "B_one_year_holdout": B}
    json.dump(res, open(os.path.join(H, "results.json"), "w"), indent=1); return res
if __name__ == "__main__": print(json.dumps(run(), indent=1))
