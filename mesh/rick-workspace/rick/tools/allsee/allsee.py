#!/usr/bin/env python3
"""ALL-SEE: one shared read-only index for every Tessera agent. Extends tools/palace (tokenizer/rooms)
and federates tesseract t5d.db + fullpicture graph at query time (no data duplication).
  allsee query 'x' [-k 5] [--json]   allsee update   allsee manifest   allsee stats
Incremental by (mtime,size) then sha1; identical files stored once (blob dedup); big files chunked, no 64KB cap."""
import os, re, sys, json, time, sqlite3, hashlib, math, collections
sys.path.insert(0, "/workspace/rick/tools/palace"); import palace
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("ALLSEE_DB", os.path.join(HERE, "allsee.db"))
T5D = "/workspace/rick/tools/tesseract/t5d.db"; GRAPH = "/workspace/rick/tools/fullpicture/graph.json"
ROOTS = ["/workspace/rick", "/workspace/TESSERA-ro", "/workspace/rick/src/Gitbook"] + sorted(
    "/workspace/" + d for d in os.listdir("/workspace") if d.startswith("gitbook-gate-")) + [
    "/workspace/gitbook-cordnation", "/workspace/tessera-brain", "/workspace/full-picture", "/workspace/tess-opt",
    "/workspace/tw", "/workspace/improve-from-logs-2026-10-12", "/workspace/rea-batch"]
SHALLOW = {"/workspace/rea-batch"}  # 2.5GB of raw clone text: summaries/readmes/results only (disk budget)
EXT = (".md", ".txt", ".json", ".jsonl", ".log", ".py", ".ts", ".tsx", ".js", ".yml", ".yaml", ".toml", ".sh", ".csv", ".html")
SKIP = palace.SKIP - {"palace"} | {"allsee", ".cache", "coverage"}
FTSOPT = os.environ.get('ALLSEE_FTSOPT', ''); CH = int(os.environ.get('ALLSEE_CH', 30))
MAXF = 8 << 20; CHUNKDEDUP = os.environ.get('ALLSEE_CHUNKDEDUP', '1') == '1'; CHB = 4096
tok = palace.tok
CFG = dict(ncand=30, agg="max", tfidf=0.0, spread=0.0, prior=0.0, compress=False, pathw=0.0, dedupfile=True)

def walk():
    for r in ROOTS:
        if not os.path.isdir(r): continue
        for d, ds, fs in os.walk(r):
            ds[:] = sorted(x for x in ds if x not in SKIP and not x.startswith(".") and os.path.join(d, x) not in ROOTS)
            for f in sorted(fs):
                p = os.path.join(d, f)
                if not f.endswith(EXT) or "lock" in f or not os.path.isfile(p): continue
                if r in SHALLOW and not (os.path.relpath(d, r).count(os.sep) < 1 or re.search(r"(?i)readme|summary|result|report|findings", f)):
                    yield r, p, "shallow-skip"; continue
                yield r, p, ("too-big" if os.path.getsize(p) > MAXF else "ok")

def chunks(text):
    lines = text.splitlines(); i = 0
    while i < max(len(lines), 1):
        body = "\n".join(lines[i:i + CH])
        for j in range(0, max(len(body), 1), CHB):
            b = body[j:j + CHB]
            if b.strip(): yield i + 1, min(i + CH, len(lines)), b
        i += CH

def con(db=DB):
    c = sqlite3.connect(db); c.executescript(("""
    create table if not exists files(path primary key, root, mtime real, size int, hash, status);
    create table if not exists blobs(hash primary key, rank int);
    create table if not exists chunks(id integer primary key, chash, body);
    create table if not exists cmap(cid int, hash, l0 int, l1 int);
    create index if not exists cm on cmap(cid); create index if not exists cmh on cmap(hash); create index if not exists cc on chunks(chash); create index if not exists fh on files(hash);
    create virtual table if not exists f using fts5(body, content='chunks', content_rowid='id'FTSOPT);
    create table if not exists links(a, b, w real, primary key(a,b)) without rowid;
    create table if not exists meta(k primary key, v);""").replace("FTSOPT", FTSOPT)); return c

def update(db=DB):
    t0 = time.time(); c = con(db); seen = set(); stats = collections.Counter()
    old = {p: (m, s, h) for p, m, s, h in c.execute("select path,mtime,size,hash from files")}
    for ri, (r, p, st) in enumerate(walk()):
        seen.add(p); stats["total"] += 1
        if st != "ok":
            c.execute("insert or replace into files values(?,?,?,?,?,?)", (p, r, 0, 0, None, st)); stats[st] += 1; continue
        s_ = os.stat(p); o = old.get(p)
        if o and o[0] == s_.st_mtime and o[1] == s_.st_size and o[2]: stats["unchanged"] += 1; continue
        try: data = open(p, "rb").read()
        except OSError: stats["unreadable"] += 1; continue
        h = hashlib.sha1(data).hexdigest(); stats["changed"] += 1
        if not c.execute("select 1 from blobs where hash=?", (h,)).fetchone():
            c.execute("insert into blobs values(?,?)", (h, ROOTS.index(r)))
            for l0, l1, b in chunks(data.decode("utf-8", "replace")):
                ch = hashlib.sha1(b.encode()).hexdigest()[:16]
                r_ = c.execute("select id from chunks where chash=?", (ch,)).fetchone() if CHUNKDEDUP else None
                if r_: cid = r_[0]
                else:
                    cid = c.execute("insert into chunks(chash,body) values(?,?)", (ch, b)).lastrowid
                    c.execute("insert into f(rowid,body) values(?,?)", (cid, b))
                c.execute("insert into cmap values(?,?,?,?)", (cid, h, l0, l1))
        c.execute("insert or replace into files values(?,?,?,?,?,?)", (p, r, s_.st_mtime, s_.st_size, h, "ok"))
    for p in set(old) - seen: c.execute("delete from files where path=?", (p,)); stats["removed"] += 1
    orphan = [h for (h,) in c.execute("select hash from blobs where hash not in (select hash from files where hash is not null)")]
    for h in orphan:
        cids = [r[0] for r in c.execute("select cid from cmap where hash=?", (h,))]; c.execute("delete from cmap where hash=?", (h,))
        for i in cids:
            if not c.execute("select 1 from cmap where cid=?", (i,)).fetchone():
                b = c.execute("select body from chunks where id=?", (i,)).fetchone()[0]
                c.execute("insert into f(f,rowid,body) values('delete',?,?)", (i, b)); c.execute("delete from chunks where id=?", (i,))
        c.execute("delete from blobs where hash=?", (h,))
    c.execute("insert or replace into meta values('updated',?)", (time.time(),)); c.commit()
    stats["seconds"] = round(time.time() - t0, 2); return dict(stats)

_g = None
def graph():
    global _g
    if _g is None:
        try: _g = json.load(open(GRAPH))
        except Exception: _g = {"nodes": [], "edges": []}
    return _g

def canon(c, h):  # canonical path for a blob: earliest root, shortest path
    ps = [r[0] for r in c.execute("select path from files where hash=?", (h,))]
    return sorted(ps, key=lambda p: (next((i for i, r in enumerate(ROOTS) if p.startswith(r + "/")), 99), len(p)))

_idf = {}
def idf(c, t):
    if t not in _idf:
        try: n = c.execute("select count(*) from f where f match ?", (f'"{t}"',)).fetchone()[0]
        except sqlite3.OperationalError: n = 0
        _idf[t] = math.log(1 + 3e5 / (1 + n))
    return _idf[t]

def search(q, k=5, c=None, cfg=None):
    cfg = {**CFG, **(cfg or {})}; c = c or sqlite3.connect(f"file:{DB}?mode=ro", uri=True); terms = tok(q)
    if not terms: return []
    m = " OR ".join(f'"{t}"' for t in dict.fromkeys(terms))
    rows = []
    for i, body, b in c.execute("select chunks.id,chunks.body,bm25(f) from f join chunks on chunks.id=f.rowid where f match ? order by bm25(f) limit ?", (m, cfg["ncand"])).fetchall():
        rows += [(i, h, l0, l1, body, b) for h, l0, l1 in c.execute("select hash,l0,l1 from cmap where cid=?", (i,))]
    sc = {}
    qt = collections.Counter(terms)
    for i, h, l0, l1, body, b in rows:
        s = -b
        if cfg["tfidf"]:
            ct = collections.Counter(tok(body)); w = {t: idf(c, t) for t in qt}
            dot = sum(qt[t] * w[t] * ct[t] * w[t] for t in qt); nq = math.sqrt(sum((qt[t] * w[t]) ** 2 for t in qt))
            nd = math.sqrt(sum(v * v for v in ct.values())) or 1
            s *= 1 + cfg["tfidf"] * dot / (nq * nd + 1e-9)
        sc.setdefault(h, []).append((s, i, l0, l1, body))
    agg = {h: (max(v)[0] if cfg["agg"] == "max" else max(v)[0] + 0.3 * sum(x[0] for x in sorted(v)[:-1])) for h, v in sc.items()}
    if cfg["spread"]:  # multi-hop spreading activation over synapse links
        act = dict(agg)
        for h, s in sorted(agg.items(), key=lambda x: -x[1])[:10]:
            for b, w in c.execute("select b,w from links where a=?", (h,)):
                act[b] = act.get(b, 0) + cfg["spread"] * w * s
        agg = act
    if cfg["prior"]:
        for h in agg:
            r = c.execute("select w from links where a='__prior__' and b=?", (h,)).fetchone()
            if r: agg[h] *= 1 + cfg["prior"] * r[0]
    out = []
    for h, s in sorted(agg.items(), key=lambda x: -x[1])[:k]:
        ps = canon(c, h)
        if not ps: continue
        best = max(sc[h]) if h in sc else (0, 0, 1, 1, (c.execute("select body from chunks join cmap on cid=id where hash=? limit 1", (h,)).fetchone() or [""])[0])
        body = best[4]
        if cfg["compress"]:
            qs = set(terms); body = "\n".join(l for l in body.splitlines() if qs & set(tok(l))) or body[:300]
        out.append(dict(path=ps[0], aliases=ps[1:4], l0=best[2], l1=best[3], score=round(s, 3), body=body))
    return out

def federated(q, k=5):
    out = []
    try:
        t = sqlite3.connect(f"file:{T5D}?mode=ro", uri=True); m = " OR ".join(f'"{x}"' for x in tok(q))
        out += [dict(src="eye/t5d", layer=a, kind=b, title=d, cite=e) for a, b, d, e in
                t.execute("select e.layer,e.kind,e.title,e.cite from ef join e on e.rowid=ef.rowid where ef match ? limit ?", (m, k))]
    except Exception: pass
    qs = set(tok(q))
    out += [dict(src="graph", node=n["id"], kind=n["kind"], degree=n.get("degree")) for n in graph()["nodes"] if qs & set(tok(n["id"]))][:k]
    return out

def manifest(db=DB):
    c = sqlite3.connect(db); st = dict(c.execute("select status,count(*) from files group by status"))
    tot = sum(st.values()); by = {}
    for r, s, n in c.execute("select root,status,count(*) from files group by 1,2"): by.setdefault(r, {})[s] = n
    m = dict(files_total=tot, files_indexed=st.get("ok", 0), coverage=round(st.get("ok", 0) / max(tot, 1), 4),
             coverage_excl_shallow=round(st.get("ok", 0) / max(tot - st.get("shallow-skip", 0), 1), 4), by_status=st, by_root=by,
             blobs=c.execute("select count(*) from blobs").fetchone()[0], chunks=c.execute("select count(*) from chunks").fetchone()[0], chunk_refs=c.execute("select count(*) from cmap").fetchone()[0],
             links=c.execute("select count(*) from links").fetchone()[0], bytes=os.path.getsize(db),
             federated=["tesseract t5d.db (Eye events, live)", "fullpicture graph.json (live)"])
    json.dump(m, open(os.path.join(HERE, "MANIFEST.json"), "w"), indent=1); return m

def main(a):
    cmd = a[0] if a else "help"
    if cmd == "update": print(json.dumps(update())); print(json.dumps({k: v for k, v in manifest().items() if k != "by_root"}))
    elif cmd == "manifest": print(json.dumps(manifest(), indent=1))
    elif cmd == "query":
        k = int(a[a.index("-k") + 1]) if "-k" in a else 5; q = " ".join(x for i, x in enumerate(a[1:], 1) if not x.startswith("--") and x != "-k" and a[i - 1] != "-k")
        cfgp = os.path.join(HERE, "config.json"); cfg = json.load(open(cfgp)).get('cfg', {}) if os.path.exists(cfgp) else {}
        t = time.time(); r = search(q, k, cfg=cfg); fe = federated(q); ms = (time.time() - t) * 1e3
        if "--json" in a: print(json.dumps(dict(ms=round(ms, 1), hits=r, federated=fe))); return
        for h in r: print(f"{h['path']}:{h['l0']}-{h['l1']}  ({h['score']})\n   {' '.join(h['body'].split())[:200]}")
        for x in fe: print("  +", json.dumps(x))
        print(f"[{ms:.1f} ms]")
    else: print(__doc__)
if __name__ == "__main__": main(sys.argv[1:])
