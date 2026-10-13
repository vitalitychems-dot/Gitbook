#!/usr/bin/env python3
"""Memory palace: read-only local index of mesh knowledge. stdlib only."""
import os, re, sys, sqlite3, time, math, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("PALACE_DB", os.path.join(HERE, "palace.db"))
ROOTS = os.environ.get("PALACE_ROOTS", "/workspace/rick:/workspace/TESSERA-ro:/workspace/gitbook-gate-1e3bb50").split(":")
SHALLOW = set(filter(None, os.environ.get("PALACE_SHALLOW", "").split(":")))  # roots: top-level + summary-named files only
SKIP = {".git", "node_modules", "__pycache__", "dist", "build", ".next", "vendor", "palace"}
EXT = tuple(os.environ.get("PALACE_EXT", ".md:.txt").split(":")); MAXF = int(os.environ.get("PALACE_MAXF", 512 * 1024)); CH = 30  # lines per chunk
STOP = set("the a an and or of to in is for on with that this it as be are by at from not we you i if all".split())
ROOMS = {"quantum": "qlab qsim aqft qft qubit quantum noise fidelity circuit gate",
 "bhnmc": "bhnmc baseline spec manifest engine reservoir narma esn",
 "tesla": "tesla patent coil resonance turbine",
 "rules": "rule gitbook moderator security approval gate policy",
 "agents": "agent tessera rick mesh lane executor handoff",
 "inventions": "invention idea garage idle round",
 "code": "api function install npm python typescript route test"}
ROOMS = {k: set(v.split()) for k, v in ROOMS.items()}
tok = lambda s: [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP]

def files(roots):
    for r in roots:
        if not os.path.isdir(r): continue
        for d, ds, fs in os.walk(r):
            ds[:] = sorted(x for x in ds if x not in SKIP and not x.startswith(".") and os.path.join(d, x) not in roots)  # nested roots indexed once
            for f in sorted(fs):
                p = os.path.join(d, f)
                if r in SHALLOW and not (os.path.relpath(d, r).count(os.sep) < 1 or re.search(r"(?i)readme|summary|result|report|findings", f)): continue
                if f.endswith(EXT) and "lock" not in f and os.path.isfile(p) and os.path.getsize(p) <= MAXF: yield r, p

def room(root, path, text):
    c = collections.Counter(tok(text + " " + path))
    best = max(ROOMS, key=lambda k: sum(c[w] for w in ROOMS[k]))
    if sum(c[w] for w in ROOMS[best]) == 0:
        rel = os.path.relpath(path, root).split(os.sep)
        best = rel[0] if len(rel) > 1 else "misc"
    return f"{os.path.basename(root)}/{best}"

def fts_ok(c):
    try: c.execute("create virtual table temp.x using fts5(a)"); return True
    except sqlite3.OperationalError: return False

def build(roots=ROOTS, db=DB):
    tmp = db + ".tmp"
    if os.path.exists(tmp): os.remove(tmp)
    c = sqlite3.connect(tmp); fts = fts_ok(c)
    c.execute("create table chunks(id integer primary key, path, l0 int, l1 int, room, body)")
    if fts: c.execute("create virtual table f using fts5(body, content='chunks', content_rowid='id')")
    nd = 0
    for r, p in files(roots):
        try: lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError: continue
        nd += 1
        for i in range(0, max(len(lines), 1), CH):
            body = "\n".join(lines[i:i + CH])
            if body.strip():
                c.execute("insert into chunks(path,l0,l1,room,body) values(?,?,?,?,?)", (p, i + 1, min(i + CH, len(lines)), room(r, p, body), body))
    if fts: c.execute("insert into f(f) values('rebuild')")
    c.execute("create table meta(k primary key, v)"); c.execute("insert into meta values('docs',?),('fts',?)", (nd, int(fts)))
    c.commit(); c.execute("vacuum"); c.close(); os.replace(tmp, db)  # atomic, idempotent
    return nd

def search(q, k=5, db=DB):
    c = sqlite3.connect(db); terms = tok(q)
    if not terms: return []
    if c.execute("select v from meta where k='fts'").fetchone()[0]:
        m = " OR ".join(f'"{t}"' for t in terms)
        return c.execute("select path,l0,l1,room,snippet(f,0,'[',']','…',12) from f join chunks on chunks.id=f.rowid where f match ? order by bm25(f) limit ?", (m, k)).fetchall()
    rows = c.execute("select path,l0,l1,room,body from chunks").fetchall()  # pure-python BM25 fallback
    docs = [tok(r[4]) for r in rows]; N = len(docs); avg = sum(map(len, docs)) / max(N, 1)
    df = collections.Counter(t for d in docs for t in set(d)); sc = []
    for r, d in zip(rows, docs):
        tf = collections.Counter(d); s = 0
        for t in terms:
            if tf[t]: s += math.log(1 + (N - df[t] + .5) / (df[t] + .5)) * tf[t] * 2.2 / (tf[t] + 1.2 * (.25 + .75 * len(d) / avg))
        if s: sc.append((s, r))
    return [r[:4] + (r[4][:160],) for s, r in sorted(sc, key=lambda x: -x[0])[:k]]

def main(a):
    cmd = a[0] if a else "stats"
    if cmd == "build": t = time.time(); n = build(); print(f"built {n} docs in {time.time()-t:.1f}s -> {DB}")
    elif cmd == "search":
        for p, l0, l1, rm, sn in search(" ".join(a[1:])): print(f"{p}:{l0}-{l1}  [{rm}]\n   {' '.join(sn.split())[:200]}")
    elif cmd == "rooms":
        for rm, n in sqlite3.connect(DB).execute("select room,count(*) from chunks group by room order by 2 desc"): print(f"{n:6d}  {rm}")
    elif cmd == "stats":
        c = sqlite3.connect(DB); d = dict(c.execute("select * from meta"))
        print(json.dumps({"docs": d["docs"], "fts5": bool(d["fts"]), "chunks": c.execute("select count(*) from chunks").fetchone()[0], "bytes": os.path.getsize(DB)}))
    else: print(__doc__ + "\nusage: palace.py build|search 'query'|rooms|stats")
if __name__ == "__main__": main(sys.argv[1:])
