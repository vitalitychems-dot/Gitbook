"""Synapses for ALL-SEE: blob<->blob links (weight w) in allsee.db `links`. Builders return edge counts.
tfidf: embedding-free TF-IDF cosine (top terms per file); dirs: same-folder co-location; graph: fullpicture edges mapped to files;
hebbian: strengthen links that delivered a correct file on DEV questions, weaken misfires, prune weak/unused."""
import os, math, json, sqlite3, collections, allsee
tok = allsee.tok
def tfidf(c, topt=30, nb=5, thr=0.2, maxdf=200):
    vec = {}
    for (h,) in c.execute("select hash from blobs").fetchall():
        ct = collections.Counter()
        for (b,) in c.execute("select body from chunks join cmap on cid=id where hash=? limit 20", (h,)): ct.update(tok(b))
        vec[h] = ct
    df = collections.Counter(t for v in vec.values() for t in v); N = len(vec); inv = collections.defaultdict(list); W = {}
    for h, ct in vec.items():
        w = {t: (1 + math.log(n)) * math.log(N / df[t]) for t, n in ct.items() if 1 < df[t] <= maxdf}
        top = dict(sorted(w.items(), key=lambda x: -x[1])[:topt]); nrm = math.sqrt(sum(v * v for v in top.values())) or 1
        W[h] = {t: v / nrm for t, v in top.items()}
        for t in W[h]: inv[t].append(h)
    n = 0
    for h, w in W.items():
        acc = collections.Counter()
        for t, v in w.items():
            for o in inv[t]:
                if o != h: acc[o] += v * W[o][t]
        for o, s in acc.most_common(nb):
            if s >= thr: c.execute("insert or replace into links values(?,?,?)", (h, o, round(s, 3))); n += 1
    return n
def dirs(c, w=0.3, cap=8):
    by = collections.defaultdict(list)
    for p, h in c.execute("select path,hash from files where status='ok'"): by[os.path.dirname(p)].append(h)
    n = 0
    for d, hs in by.items():
        hs = list(dict.fromkeys(hs))
        if len(hs) > cap: continue
        for a in hs:
            for b in hs:
                if a != b: c.execute("insert or ignore into links values(?,?,?)", (a, b, w)); n += 1
    return n
def graph(c, w=0.5):
    g = allsee.graph(); P = {}
    for nd in g["nodes"]:
        if nd.get("path"):
            r = c.execute("select hash from files where path=? or path like ?", (nd["path"], "%" + nd["path"])).fetchone()
            if r: P[nd["id"]] = r[0]
    n = 0
    for e in g["edges"]:
        a, b = P.get(e["source"]), P.get(e["target"])
        if a and b and a != b:
            for x, y in ((a, b), (b, a)): c.execute("insert or ignore into links values(?,?,?)", (x, y, w)); n += 1
    return n
def hebbian(c, dev, cfg, up=1.25, down=0.85, prune=0.15):
    use = collections.Counter(); good = collections.Counter()
    for x in dev:
        terms = tok(x["q"]); m = " OR ".join(f'"{t}"' for t in dict.fromkeys(terms))
        if not m: continue
        seeds = list(dict.fromkeys(h for (i,) in c.execute("select rowid from f where f match ? order by bm25(f) limit 10", (m,)) for (h,) in c.execute("select hash from cmap where cid=?", (i,))))[:10]
        tgt = c.execute("select hash from files where path=?", (x["file"],)).fetchone()
        for a in seeds:
            for (b,) in c.execute("select b from links where a=?", (a,)):
                use[(a, b)] += 1
                if tgt and b == tgt[0]: good[(a, b)] += 1
    for (a, b), n in use.items():
        f = up ** good[(a, b)] * down ** (n - good[(a, b)])
        c.execute("update links set w=min(2.0,w*?) where a=? and b=?", (f, a, b))
    before = c.execute("select count(*) from links").fetchone()[0]
    c.execute("delete from links where w<?", (prune,)); c.commit()
    return dict(used=len(use), strengthened=sum(1 for k in good), pruned=before - c.execute("select count(*) from links").fetchone()[0])
