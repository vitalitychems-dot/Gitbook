import json, common as c, inv3_mwpm_dedup as m
EVAL = lambda p: p.startswith("/workspace/rick/cycles/")  # benchmark files leaked into the palace
def clean(rows): return tuple(r for r in rows if not EVAL(r[1]))
MIRROR = ("/archive", "/history/", "/recovered/", "/moved/", "/imports/", "/tess-opt/", "/tw/")
def rank(q, k=5, use_prior=True):
    rows = clean(c.retrieve(q, 40))[:30]
    if not rows: return []
    lab, _ = m.clusters(rows); groups = {}
    for i, r in enumerate(rows): groups.setdefault(lab[i], []).append(r)
    pr = m.prior if use_prior else (lambda p: -sum(s in p for s in MIRROR))
    out = []
    for g in groups.values():
        rep = max(g, key=lambda r: (pr(r[1]), -g.index(r)))[1]
        if rep not in out: out.append(rep)
    return out[:k]
R = dict(
 clean_baseline=c.score(lambda q: c.files(clean(c.retrieve(q, 40)), 5)),
 clean_mwpm_mirror_rule=c.score(lambda q: rank(q, use_prior=False)),
 clean_mwpm_dev_prior=c.score(rank),
 clean_prior_only=c.score(lambda q: sorted(c.files(clean(c.retrieve(q, 40)), 30), key=lambda p: -m.prior(p))[:5]),
 clean_mirror_rule_only=c.score(lambda q: sorted(c.files(clean(c.retrieve(q, 40)), 30), key=lambda p: sum(s in p for s in MIRROR))[:5]),
)
print(json.dumps(R, indent=1)); d = json.load(open("results/inv3.json")); d["leak_fixed"] = R; json.dump(d, open("results/inv3.json", "w"), indent=1)
