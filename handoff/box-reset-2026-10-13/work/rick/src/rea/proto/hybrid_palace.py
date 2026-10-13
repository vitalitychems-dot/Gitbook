"""REA from open-webui/open-webui hybrid retrieval (BM25 + second ranker fused, top-k distinct docs) -> palace.
Ranker 1: chunk BM25 (palace FTS5), collapsed to best chunk per file. Ranker 2: query-term overlap with the file PATH.
Fused with Reciprocal Rank Fusion (k=60), returns k distinct files. Read-only on palace.db."""
import sqlite3, re, sys
sys.path.insert(0, "/workspace/rick/tools/palace"); import palace
def search(q, k=5, db=palace.DB, pool=200, K=60):
    c = sqlite3.connect(db); terms = palace.tok(q)
    if not terms: return []
    m = " OR ".join(f'"{t}"' for t in terms)
    rows = c.execute("select path from f join chunks on chunks.id=f.rowid where f match ? order by bm25(f) limit ?", (m, pool)).fetchall()
    r1 = list(dict.fromkeys(p for (p,) in rows))
    paths = [p for (p,) in c.execute("select distinct path from chunks")]
    ts = set(terms); sc = []
    for p in paths:
        pt = set(re.findall(r"[a-z0-9]+", p.lower().rsplit("/rick/", 1)[-1])); o = len(ts & pt)
        if o: sc.append((-o, len(p), p))
    r2 = [p for *_, p in sorted(sc)]
    f = {}
    for r in (r1, r2):
        for i, p in enumerate(r): f[p] = f.get(p, 0) + 1 / (K + i + 1)
    return [(p,) for p in sorted(f, key=lambda p: -f[p])[:k]]
