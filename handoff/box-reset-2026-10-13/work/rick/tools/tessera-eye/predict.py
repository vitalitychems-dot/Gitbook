#!/usr/bin/env python3
"""Honest forecasting harness: predict next-day global M4.5+ quake count band (low/med/high).
Data: USGS FDSN catalog history (public domain), stored as daily counts in data/quake_daily.json.
Bands = terciles of TRAINING days only. Walk-forward on held-out tail; compare vs baselines.
This forecasts counts; it does not and cannot influence events."""
import json, os, sys, csv, io, collections, datetime, urllib.request, random
HERE = os.path.dirname(os.path.abspath(__file__)); DAILY = os.path.join(HERE, "data", "quake_daily.json")
URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={s}&endtime={e}&minmagnitude=4.5&orderby=time-asc"
def build_daily(csvtext):
    c = collections.Counter(r["time"][:10] for r in csv.DictReader(io.StringIO(csvtext)))
    d0 = datetime.date.fromisoformat(min(c)); d1 = datetime.date.fromisoformat(max(c))
    return [[(d0+datetime.timedelta(i)).isoformat(), c.get((d0+datetime.timedelta(i)).isoformat(), 0)] for i in range((d1-d0).days+1)]
def fetch_history(days=365):
    e = datetime.date.today(); s = e - datetime.timedelta(days)
    t = urllib.request.urlopen(urllib.request.Request(URL.format(s=s, e=e), headers={"User-Agent": "tessera-eye/2"}), timeout=120).read().decode()
    d = build_daily(t)[:-1]  # drop partial last day
    json.dump(d, open(DAILY, "w")); return d
def band(x, q): return 0 if x <= q[0] else (1 if x <= q[1] else 2)
def terciles(v): s = sorted(v); return s[len(s)//3], s[2*len(s)//3]
def evaluate(counts, test_frac=0.25, k=7):
    n = len(counts); cut = int(n*(1-test_frac)); train = counts[:cut]; q = terciles(train)
    tb = [band(x, q) for x in train]; majority = collections.Counter(tb).most_common(1)[0][0]
    preds = {"persistence": [], f"mean{k}": [], "climatology": [], "random": []}; truth = []; rng = random.Random(0)
    for i in range(cut, n):
        truth.append(band(counts[i], q))
        preds["persistence"].append(band(counts[i-1], q))
        preds[f"mean{k}"].append(band(sum(counts[i-k:i])/k, q))
        preds["climatology"].append(majority)
        preds["random"].append(rng.randrange(3))
    res = {m: round(sum(a == b for a, b in zip(p, truth))/len(truth), 3) for m, p in preds.items()}
    # exact-count MAE for the mean model vs climatology mean
    mean_train = sum(train)/len(train)
    mae = {f"mean{k}": round(sum(abs(sum(counts[i-k:i])/k - counts[i]) for i in range(cut, n))/(n-cut), 2),
           "climatology": round(sum(abs(mean_train - counts[i]) for i in range(cut, n))/(n-cut), 2)}
    return {"days": n, "train": cut, "test": n-cut, "tercile_cuts": q, "hit_rate": res, "mae_count": mae,
            "test_band_dist": dict(collections.Counter(truth))}
def synthetic(n=200, seed=1):  # Poisson-ish counts with aftershock bursts, for tests only
    r = random.Random(seed); out = []; boost = 0
    for _ in range(n):
        if r.random() < 0.05: boost = r.randint(10, 25)
        lam = 6 + boost; boost = int(boost*0.6)
        out.append(sum(r.random() < lam/50 for _ in range(50)))
    return out
if __name__ == "__main__":
    if "--fetch" in sys.argv or not os.path.exists(DAILY): d = fetch_history()
    else: d = json.load(open(DAILY))
    r = evaluate([c for _, c in d]); r["range"] = [d[0][0], d[-1][0]]; print(json.dumps(r, indent=1))
