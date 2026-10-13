"""Einstein verification toolkit: seeded runs, bootstrap CIs, crossing finder,
baseline-vs-candidate harness. numpy + stdlib only."""
import json, math, time, numpy as np

def rng(seed):
    return np.random.default_rng(seed)

def seeds(n, base=12345):
    return [base + 1000 * i for i in range(n)]

def bootstrap_ci(x, stat=np.mean, n=2000, alpha=0.05, seed=0):
    x = np.asarray(x, float)
    r = rng(seed)
    idx = r.integers(0, len(x), (n, len(x)))
    bs = np.array([stat(x[i]) for i in idx])
    return float(stat(x)), float(np.quantile(bs, alpha / 2)), float(np.quantile(bs, 1 - alpha / 2))

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 0.0, 1.0)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, max(0.0, c - h), min(1.0, c + h))

def find_crossing(x, y1, y2, log=True):
    """Return x where y1-y2 changes sign (linear interp, in log y if log). None if no crossing."""
    x = np.asarray(x, float); a = np.asarray(y1, float); b = np.asarray(y2, float)
    if log:
        a = np.log(np.maximum(a, 1e-12)); b = np.log(np.maximum(b, 1e-12))
    d = a - b
    for i in range(len(x) - 1):
        if d[i] == 0: return float(x[i])
        if d[i] * d[i + 1] < 0:
            t = d[i] / (d[i] - d[i + 1])
            return float(x[i] + t * (x[i + 1] - x[i]))
    return None

def bench(name, baseline, candidate, n_seeds=20, higher_is_better=True, metric="metric", base_seed=12345):
    """baseline/candidate: f(seed)->float. Paired over seeds. KEEP only if the 95% bootstrap CI of
    the paired difference excludes 0 in the better direction."""
    s = seeds(n_seeds, base_seed)
    b = np.array([baseline(x) for x in s], float)
    c = np.array([candidate(x) for x in s], float)
    d = c - b if higher_is_better else b - c
    m, lo, hi = bootstrap_ci(d)
    res = {
        "name": name, "metric": metric, "n_seeds": n_seeds, "higher_is_better": higher_is_better,
        "baseline": dict(zip(["mean", "lo", "hi"], bootstrap_ci(b))),
        "candidate": dict(zip(["mean", "lo", "hi"], bootstrap_ci(c))),
        "improvement": {"mean": m, "lo": lo, "hi": hi},
        "verdict": "KEEP" if lo > 0 else "DROP",
    }
    return res

def fmt(r):
    b, c, i = r["baseline"], r["candidate"], r["improvement"]
    return (f"{r['name']}: {r['metric']} baseline {b['mean']:.4g} [{b['lo']:.4g},{b['hi']:.4g}] -> "
            f"candidate {c['mean']:.4g} [{c['lo']:.4g},{c['hi']:.4g}]; gain {i['mean']:.4g} "
            f"[{i['lo']:.4g},{i['hi']:.4g}] (n={r['n_seeds']}) => {r['verdict']}")

def save(results, path):
    with open(path, "w") as f: json.dump(results, f, indent=2)

def timeit(f, reps=5):
    ts = []
    for _ in range(reps):
        t = time.perf_counter(); f(); ts.append(time.perf_counter() - t)
    return float(np.median(ts))

def svg_plot(series, path, xlabel="x", ylabel="y", logy=True, title=""):
    """series: {label: (xs, ys)}. Minimal dependency-free SVG line plot."""
    W, H, m = 640, 420, 60
    xs = [x for s in series.values() for x in s[0]]; ys = [y for s in series.values() for y in s[1] if (y > 0 or not logy)]
    tf = (lambda y: math.log10(y)) if logy else (lambda y: y)
    x0, x1 = min(xs), max(xs); y0, y1 = tf(min(ys)), tf(max(ys))
    X = lambda x: m + (x - x0) / (x1 - x0 or 1) * (W - 2 * m)
    Y = lambda y: H - m - (tf(max(y, 1e-12)) - y0) / (y1 - y0 or 1) * (H - 2 * m)
    cols = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<line x1="{m}" y1="{H-m}" x2="{W-m}" y2="{H-m}" stroke="black"/><line x1="{m}" y1="{m}" x2="{m}" y2="{H-m}" stroke="black"/>',
         f'<text x="{W/2}" y="{H-15}" text-anchor="middle">{xlabel}</text><text x="15" y="{H/2}" transform="rotate(-90 15 {H/2})" text-anchor="middle">{ylabel}{" (log)" if logy else ""}</text>',
         f'<text x="{W/2}" y="25" text-anchor="middle" font-size="14">{title}</text>']
    for k in range(6):
        xv = x0 + k * (x1 - x0) / 5; o.append(f'<text x="{X(xv)}" y="{H-m+16}" text-anchor="middle">{xv:.3g}</text>')
        yv = y0 + k * (y1 - y0) / 5; lab = f"{10**yv:.2g}" if logy else f"{yv:.3g}"
        o.append(f'<text x="{m-5}" y="{H-m-k*(H-2*m)/5+4}" text-anchor="end">{lab}</text>')
    for i, (lab, (sx, sy)) in enumerate(series.items()):
        c = cols[i % len(cols)]; pts = " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in zip(sx, sy) if b > 0 or not logy)
        o.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2"/>')
        o += [f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3" fill="{c}"/>' for a, b in zip(sx, sy) if b > 0 or not logy]
        o.append(f'<text x="{W-m-60}" y="{m+18*i+10}" fill="{c}">{lab}</text>')
    o.append("</svg>"); open(path, "w").write("\n".join(o))
