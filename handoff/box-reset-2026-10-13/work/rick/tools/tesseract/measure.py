import json, random, statistics as st, time, tesseract as T
res = {}
qs = ["earthquake alaska", "wildfire california", "qlab fidelity", "tessera gate", "bhnmc reservoir", "satellite orbit", "flood warning", "forecast quake count", "rick bus", "einstein bell"]
T.query("warm"); lat = [T.query(q)["_ms"] for q in qs for _ in range(3)]
res["latency_ms"] = {k: {"median": round(st.median(x[k] for x in lat), 2), "max": round(max(x[k] for x in lat), 2)} for k in lat[0]}
raw = open(T.EV).read() + "".join(open(b).read() for b in T.BUS) + open(T.QD).read() + open(T.GRAPH).read()
b = T.brief(); open("brief.md", "w").write(b)
res["brief"] = {"brief_tokens": T.toks(b), "raw_tokens": T.toks(raw), "ratio": round(T.toks(raw) / T.toks(b), 1)}
xs = [v for _, v in json.load(open(T.QD))]
base = set(T.anomalies(xs)); P = R = []; tp = fp = fn = 0; random.seed(7)
for trial in range(20):  # fixtures: real 1y series + 10 injected spikes/dips (labeled), seed 7
    y = xs[:]; inj = set(random.sample(range(40, len(y)), 10))
    for i in inj: y[i] = round(y[i] * random.choice([2.2, 2.8, 0.15]))
    al = set(T.anomalies(y)) - base  # judge only vs. injected labels; pre-existing real anomalies excluded
    tp += len(al & inj); fp += len(al - inj); fn += len(inj - al)
res["anomaly_fixture"] = {"trials": 20, "injected": 200, "precision": round(tp / (tp + fp), 3), "recall": round(tp / (tp + fn), 3), "real_series_anomalous_days": len(base), "series_days": len(xs)}
cov, n = T.cone_coverage(); res["cone_p10_p90_coverage"] = {"coverage": round(cov, 3), "target": 0.8, "days": n}
json.dump(res, open("results.json", "w"), indent=1); print(json.dumps(res, indent=1))
