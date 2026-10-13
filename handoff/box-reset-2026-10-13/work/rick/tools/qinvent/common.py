"""Shared read-only retrieval (copy of c2 brain2 BM25 retrieve) for qinvent experiments."""
import sys, re, json, sqlite3, functools, collections
sys.path.insert(0, "/workspace/rick/tools/palace"); import palace
tok = palace.tok
QA = json.load(open("/workspace/rick/cycles/c1/qa_set.json"))
DEV = [x for x in QA if x["split"] == "dev"]; TEST = [x for x in QA if x["split"] == "test"]
C = sqlite3.connect("file:/workspace/rick/cycles/c2/palace.db?mode=ro", uri=True, check_same_thread=False)
@functools.lru_cache(maxsize=None)
def dfc(w): return C.execute("select count(*) from f where f match ?", (f'"{w}"',)).fetchone()[0]
@functools.lru_cache(maxsize=None)
def retrieve(q, k=30):
    """identical to c2 brain2.retrieve; rows=(chunk_id,path,body,bm25)"""
    t = tok(q)
    if not t: return ()
    rows = []; rare = sorted(set(t), key=dfc)[:4]
    sql = "select chunks.id,path,chunks.body,bm25(f) from f join chunks on chunks.id=f.rowid where f match ? order by bm25(f) limit ?"
    try: rows = C.execute(sql, (" AND ".join(f'"{w}"' for w in rare), k)).fetchall()
    except sqlite3.OperationalError: pass
    if len(rows) < k: rows += [r for r in C.execute(sql, (" OR ".join(f'"{w}"' for w in t), k)).fetchall() if r not in rows]
    return tuple(rows[:k])
def files(rows, k):
    out = []
    for r in rows:
        if r[1] not in out: out.append(r[1])
    return out[:k]
def score(rank_fn, xs=None):
    xs = xs or TEST; h1 = h5 = 0
    for x in xs:
        f = rank_fn(x["q"]); h1 += f[:1] == [x["file"]]; h5 += x["file"] in f[:5]
    return dict(top1=round(h1 / len(xs), 3), recall5=round(h5 / len(xs), 3), n=len(xs))
ROOT = lambda p: "/".join(p.split("/")[:3]) if not p.startswith("/workspace/rick/src/") else "/".join(p.split("/")[:5])
