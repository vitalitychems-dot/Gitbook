"""Prediction harness prototype: next-day M2.5+ global quake COUNT from history (USGS public feed, 30 days; Eye quake_daily.json if longer).
Rolling-origin backtest: each day t is predicted only from days < t. Hit = |pred-actual| <= 20% of actual. Also 'busy-day' (> median) classification.
Correlation/forecast skill only, NO causal claims, and nothing here influences events."""
import csv, json, collections, datetime as dt, numpy as np, os
days = collections.Counter(r["time"][:10] for r in csv.DictReader(open("data/usgs_month.csv")))
ds = sorted(days)[1:-1]  # drop partial first/last day
y = np.array([days[d] for d in ds], float)
models = {"persistence": lambda h: h[-1], "mean7": lambda h: h[-7:].mean(), "median7": lambda h: np.median(h[-7:]),
          "ewma0.3": lambda h: (lambda w: (w * h[-14:]).sum() / w.sum())(0.7 ** np.arange(len(h[-14:]))[::-1]),
          "climatology": lambda h: h.mean()}
R = dict(source="USGS 2.5_month.csv (public domain)", days=len(ds), first=ds[0], last=ds[-1], mean=round(y.mean(), 1), std=round(y.std(), 1), start_index=7, models={})
for name, f in models.items():
    P = np.array([f(y[:t]) for t in range(7, len(y))]); A = y[7:]
    med = np.array([np.median(y[:t]) for t in range(7, len(y))])
    R["models"][name] = dict(MAE=round(float(np.abs(P - A).mean()), 2), hit20=round(float(np.mean(np.abs(P - A) <= .2 * A)), 3),
        busy_day_acc=round(float(np.mean((P > med) == (A > med))), 3))
best = min(R["models"], key=lambda k: R["models"][k]["MAE"]); R["best"] = best
R["skill_vs_persistence"] = round(1 - R["models"][best]["MAE"] / R["models"]["persistence"]["MAE"], 3)
R["caveat"] = "n≈22 test days, so the uncertainty is large; aftershock sequences dominate the variance; forecast skill ≠ causation."
json.dump(R, open("forecast_results.json", "w"), indent=1); print(json.dumps(R))
