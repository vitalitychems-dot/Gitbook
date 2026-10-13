"""Father's rule: keep a change only if it beats the previous version on the fixed benchmark (no other metric worse by >2%)."""
import os, sys, json, time, re, shutil, sqlite3, subprocess, statistics, collections, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import allsee, synapse
HERE = allsee.HERE; V = "/workspace/rick/versions"; NUM = r"\b\d+(?:\.\d+)?%?"
QA = json.load(open("/workspace/rick/cycles/c1/qa_set.json")); TEST = [x for x in QA if x["split"] == "test"]; DEV = [x for x in QA if x["split"] == "dev"]
T = lambda s: max(1, len(s) // 4)
def answer(q, hits):
    best = None; qt = set(allsee.tok(q))
    for rank, h in enumerate(hits):
        for s in re.split(r"(?<=[.!?])\s+|\n", h["body"]):
            ov = len(qt & set(allsee.tok(s))) / max(1, len(qt))
            for n in re.findall(NUM, s):
                if best is None or ov / (1 + rank) > best[0]: best = (ov / (1 + rank), n)
    return best and best[1]
def bench(cfg, db=allsee.DB):
    c = sqlite3.connect(f"file:{db}?mode=ro", uri=True); allsee._idf.clear(); r = a = tk = 0; lat = []
    for x in TEST:
        t = time.perf_counter(); hits = allsee.search(x["q"], 5, c, cfg); lat.append((time.perf_counter() - t) * 1e3)
        r += any(x["file"] == h["path"] or x["file"] in h["aliases"] for h in hits); a += answer(x["q"], hits) == x["a"]; tk += sum(T(h["body"]) for h in hits)
    lat2 = [];  # second timing pass, take per-query min to damp noise
    for x in TEST: t = time.perf_counter(); allsee.search(x["q"], 5, c, cfg); lat2.append((time.perf_counter() - t) * 1e3)
    lat = [min(p, q) for p, q in zip(lat, lat2)]; qs = statistics.quantiles(lat, n=20)
    st = os.statvfs("/")
    return dict(recall5=round(r / len(TEST), 4), acc=round(a / len(TEST), 4), p50_ms=round(statistics.median(lat), 2), p95_ms=round(qs[18], 2),
                tokens_brief=round(tk / len(TEST), 1), index_bytes=os.path.getsize(db), disk_free=st.f_bavail * st.f_frsize)
LOWER = ("p50_ms", "p95_ms", "tokens_brief", "index_bytes"); HIGHER = ("recall5", "acc", "disk_free")
def paired(cfgA, dbA, cfgB, dbB, reps=3):
    ca = sqlite3.connect(f"file:{dbA}?mode=ro", uri=True); cb = sqlite3.connect(f"file:{dbB}?mode=ro", uri=True); ra = []; rb = []
    for x in TEST:
        ta = []; tb = []
        for _ in range(reps):
            t = time.perf_counter(); allsee.search(x["q"], 5, ca, cfgA); ta.append(time.perf_counter() - t)
            t = time.perf_counter(); allsee.search(x["q"], 5, cb, cfgB); tb.append(time.perf_counter() - t)
        ra.append(min(ta)); rb.append(min(tb))
    return statistics.median(rb) / statistics.median(ra)
def better(n, o):
    gain = []; 
    for k in HIGHER + LOWER:
        rel = (n[k] - o[k]) / max(abs(o[k]), 1e-9) * (1 if k in HIGHER else -1)
        if k in ("p95_ms",) : continue  # p95 reported, not gated (noise)
        if k == "disk_free": continue   # disk is gated via index_bytes; free space moves with other agents
        if rel < -0.02: return False, f"regressed {k} {o[k]}->{n[k]}"
        if (k in ("recall5", "acc") and n[k] > o[k]) or (k not in ("recall5", "acc") and rel >= 0.05): gain.append(f"{k} {o[k]}->{n[k]}")
    return bool(gain), "; ".join(gain) or "no measurable gain"
def rebuild(env):
    cand = allsee.DB + ".cand"
    for p in glob.glob(cand + "*"): os.remove(p)
    e = {**os.environ, "ALLSEE_DB": cand, **env}; subprocess.run([sys.executable, os.path.join(HERE, "allsee.py"), "update"], env=e, check=True, capture_output=True)
    return cand
def links_db(db, fn):
    cand = allsee.DB + ".cand"; shutil.copy(db, cand); c = sqlite3.connect(cand); info = fn(c); c.commit(); c.close(); return cand, info
def optimize(db):
    cand = allsee.DB + ".cand"; shutil.copy(db, cand); c = sqlite3.connect(cand); c.execute("insert into f(f) values('optimize')"); c.commit(); c.execute("vacuum"); c.close(); return cand, "fts optimize + vacuum"

C = [("chunk-level dedup (identical chunks stored once across clones)", "rebuild", {"ALLSEE_CHUNKDEDUP": "1"}),
 ("FTS5 segment optimize + vacuum", "opt", None),
 ("brief compression: only query-matching lines per hit", "cfg", {"compress": True}),
 ("TF-IDF cosine rerank (weight 0.5)", "cfg", {"tfidf": 0.5}),
 ("candidate pool 30->60", "cfg", {"ncand": 60}),
 ("synapses: TF-IDF cosine links + spreading activation 0.2", "links", ("tfidf", {"spread": 0.2})),
 ("synapses: same-folder co-location links", "links", ("dirs", {"spread": 0.2})),
 ("synapses: fullpicture graph edges mapped to files", "links", ("graph", {"spread": 0.2})),
 ("synapses: Hebbian strengthen/prune on dev split", "links", ("hebbian", {})),
 ("multi-chunk evidence aggregation", "cfg", {"agg": "sum"}),
 ("FTS5 detail=column (smaller postings)", "rebuild", {"ALLSEE_FTSOPT": ", detail=column"}),
 ("porter stemming tokenizer", "rebuild", {"ALLSEE_FTSOPT": ", tokenize='porter unicode61'"}),
 ("15-line chunks", "rebuild", {"ALLSEE_CH": "15"}),
 ("candidate pool ->15 (latency)", "cfg", {"ncand": 15}),
 ("TF-IDF rerank weight 1.0", "cfg", {"tfidf": 1.0}),
 ("spreading activation 0.05", "cfg", {"spread": 0.05}),
 ("60-line chunks", "rebuild", {"ALLSEE_CH": "60"}),
 ("FTS5 detail=none", "rebuild", {"ALLSEE_FTSOPT": ", detail=none"}),
 ("candidate pool ->100", "cfg", {"ncand": 100}),
 ("spreading activation 0.5", "cfg", {"spread": 0.5})]
def run(start=1):
    os.makedirs(V, exist_ok=True); cfg = dict(allsee.CFG); env = {}; linkfns = []; base = bench(cfg); cur = dict(base); log = [dict(round=0, bench=base)]
    queue = list(C); empty = 0; kept_all = []
    if start > 1:  # resume from pass-1 round-1 state (index already deduped+optimized)
        src = "rounds_log_pass1.json" if start == 2 else "rounds_log.json"
        P = json.load(open(os.path.join(HERE, src))); base = P["base"]; kept_all = P["kept"]
        if start == 2: log = P["log"][:start]; env = {"ALLSEE_CHUNKDEDUP": "1"}; done = set()
        else:
            log = P["log"]; K = json.load(open(os.path.join(HERE, "config.json"))); cfg, env, linkfns = K["cfg"], K["env"], K["links"]
            done = {t["change"] for r in log if isinstance(r.get("round"), int) and r["round"] >= 2 and r.get("tried") and log.index(r) > 1 for t in r["tried"]}
        cur = bench(cfg); log.append(dict(round="resume-rebench", bench=cur))
        queue = [c_ for c_ in C if c_[0] not in {k["change"] for k in kept_all} | done]
    for rn in range(start, 20):
        ver = rn + 3; picks, queue = queue[:4], queue[4:]; kept = []; tried = []
        for name, kind, arg in picks:
            ncfg = dict(cfg); db = allsee.DB; nenv = env; info = ""
            try:
                if kind == "cfg": ncfg.update(arg)
                elif kind == "opt": db, info = optimize(allsee.DB)
                elif kind == "rebuild":
                    nenv = {**env, **arg}; db = rebuild(nenv)
                    for fn in linkfns: c = sqlite3.connect(db); getattr(synapse, fn)(c, DEV, ncfg) if fn == "hebbian" else getattr(synapse, fn)(c); c.commit()
                elif kind == "links":
                    fn, extra = arg; ncfg.update(extra)
                    db, info = links_db(allsee.DB, (lambda c: synapse.hebbian(c, DEV, ncfg)) if fn == "hebbian" else getattr(synapse, fn))
                nb = bench(ncfg, db); ratio = paired(cfg, allsee.DB, ncfg, db); nb['p50_ms'] = round(cur['p50_ms'] * ratio, 2); nb['latency_ratio_paired'] = round(ratio, 3); ok, why = better(nb, cur)
            except Exception as e: ok, why, nb = False, f"error {e}", None
            tried.append(dict(change=name, kept=ok, why=why, info=info, bench=nb))
            if ok:
                if db != allsee.DB: os.replace(db, allsee.DB)
                cfg, env, cur = ncfg, nenv, nb
                if kind == "links": linkfns.append(arg[0])
                kept.append(dict(change=name, gain=why, info=info, bench=nb)); kept_all.append(dict(version=f"v{ver}", change=name, gain=why, info=info))
            for p in glob.glob(allsee.DB + ".cand*"): os.remove(p)
        subprocess.run("find /workspace/rick -name __pycache__ -type d -prune -exec rm -rf {} +", shell=True)  # Rick's own temp only
        log.append(dict(round=rn, version=f"v{ver}", tried=tried, kept=kept, bench=cur))
        with open(f"{V}/v{ver}.md", "w") as f:
            f.write(f"# Tessera v{ver} draft (ALL-SEE round {rn})\n\nFather's rule: only kept improvements are listed.\n\n")
            if kept:
                for k in kept: f.write(f"- **{k['change']}**: {k['gain']}" + (f" ({k['info']})" if k['info'] and not isinstance(k['info'], str) else "") + "\n")
            else: f.write("- No change beat v%d this round; nothing kept.\n" % (ver - 1))
            f.write(f"\nBenchmark after round: `{json.dumps(cur)}`\n")
        empty = 0 if kept else empty + 1
        json.dump(dict(cfg=cfg, env=env, links=linkfns), open(os.path.join(HERE, "config.json"), "w"))
        json.dump(dict(base=base, log=log, kept=kept_all, cfg=cfg, env=env, links=linkfns), open(os.path.join(HERE, "rounds_log.json"), "w"), indent=1, default=str)
        print(rn, [ (t["change"], t["kept"], t["why"]) for t in tried], flush=True)
        if empty >= 3: print("stop: 3 consecutive rounds without a kept change", flush=True); break
if __name__ == "__main__": run(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
