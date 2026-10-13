"""Inventions 6-9 (speed/hardware) and 13-15 (accuracy) on allsee.db, c1 test (dev for choices)."""
import json, time, statistics, collections, os, functools, random
from harness import *
c = con(); R = {}
def run(xs, fn):
    r = a = 0; lat = []
    for x in xs:
        t = time.perf_counter(); hs = fn(x["q"]); lat.append((time.perf_counter()-t)*1e3)
        r += recall(hs, x); a += answer(x["q"], hs) == x["a"]
    return dict(recall5=round(r/len(xs),4), acc=round(a/len(xs),4), p50_ms=round(statistics.median(lat),2), total_ms=round(sum(lat)))
S = lambda cfg: (lambda q: allsee.search(q, 5, c, cfg))
for x in TEST[:20]: S({})(x["q"])  # warm
# 6 resonance batching: order queries so ones sharing rare terms run back-to-back (hot pages) vs given order
def rare(q): t = tok(q); return min(t, key=lambda w: allsee.idf(c, w) * -1) if t else ""
order = sorted(TEST, key=lambda x: (rare(x["q"]), x["q"]))
a_ = []; b_ = []
for _ in range(3): a_.append(run(TEST, S({}))["total_ms"]); b_.append(run(order, S({}))["total_ms"])
R["6_resonance_batch"] = dict(seq_total_ms=min(a_), resonant_total_ms=min(b_), speedup=round(min(a_)/min(b_),3))
# 7 bifilar dual-path cache: path A exact string, path B normalized token-set; replay zipf stream of real queries
rnd = random.Random(1); pool = TEST + DEV; wts = [1/(i+1) for i in range(len(pool))]
stream = [rnd.choices(pool, wts)[0]["q"] for _ in range(600)]
stream = [q if rnd.random() < .7 else q.upper() + " " for q in stream]  # agents re-ask with case/space variants
def replay(mode):
    A = {}; B = {}; hit = 0; t = time.perf_counter()
    for q in stream:
        if mode and q in A: hit += 1; continue
        k = " ".join(sorted(set(tok(q))))
        if mode == 2 and k in B: A[q] = B[k]; hit += 1; continue
        r = allsee.search(q, 5, c, {}); A[q] = r; B[k] = r
    return dict(hit_rate=round(hit/len(stream),3), total_s=round(time.perf_counter()-t,2))
R["7_bifilar_cache"] = dict(nocache=replay(0), exact_only=replay(1), bifilar=replay(2))
# 8 canon() memo (hash->paths cached per process)
base8 = run(TEST, S({}))
orig = allsee.canon; allsee.canon = functools.lru_cache(maxsize=None)(orig); run(TEST, S({}))
memo8 = run(TEST, S({})); allsee.canon = orig
R["8_canon_memo"] = dict(base=base8, memo=memo8)
# 9 thermal-aware ncand from /proc/loadavg: measure the tradeoff it would apply under load
R["9_thermal_ncand"] = {f"ncand{n}": run(DEV, S({"ncand": n})) for n in (10, 15, 30)}
R["9_thermal_ncand"]["test_ncand15"] = run(TEST, S({"ncand": 15})); R["9_thermal_ncand"]["test_ncand30"] = run(TEST, S({}))
R["9_thermal_ncand"]["loadavg_now"] = open("/proc/loadavg").read().split()[0]
# 13 spread / 14 prior / tfidf ; 15 RRF fusion
nl = c.execute("select count(*) from links").fetchone()[0]; R["links"] = nl
for name, cfgs in (("13_spread", [{"spread": s} for s in (0.1, 0.3)]), ("14_prior_tfidf", [{"prior": 0.5}, {"tfidf": 0.5}])):
    R[name] = {json.dumps(cf): {"dev": run(DEV, S(cf)), "test": run(TEST, S(cf))} for cf in cfgs}
def rrf(q):
    L = [allsee.search(q, 10, c, {}), allsee.search(q, 10, c, {"tfidf": 0.5}), allsee.search(q, 10, c, {"agg": "sum"})]
    sc = collections.Counter(); byp = {}
    for l in L:
        for i, h in enumerate(l): sc[h["path"]] += 1/(60+i); byp.setdefault(h["path"], h)
    return [byp[p] for p, _ in sc.most_common(5)]
R["15_rrf_fusion"] = {"dev": run(DEV, rrf), "test": run(TEST, rrf), "base_dev": run(DEV, S({})), "base_test": base8}
json.dump(R, open("results/speed_acc.json", "w"), indent=1); print(json.dumps(R, indent=1))
