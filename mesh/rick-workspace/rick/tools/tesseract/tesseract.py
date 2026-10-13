#!/usr/bin/env python3
"""Tesseract: 5D store (lat,lon,alt,time,scenario) + unified query + forecast cones + anomalies + brief. stdlib only, read-only on sources."""
import os, sys, json, sqlite3, time, math, re, statistics as st, datetime as dt
T = "/workspace/rick/tools"; HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{T}/palace"); import palace
DB = os.path.join(HERE, "t5d.db")
EV = f"{T}/tessera-eye/data/events.jsonl"; QD = f"{T}/tessera-eye/data/quake_daily.json"
GRAPH = f"{T}/fullpicture/graph.json"; BUS = [f"{T}/collab/sample-bus.jsonl", f"{T}/tessera-eye/data/bus.jsonl"]
def ts(s):
    try: return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except Exception: return None
def jl(p): return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
# 1. unified 5D event store
def build(db=DB):
    if os.path.exists(db): os.remove(db)
    c = sqlite3.connect(db)
    c.execute("create table e(id text primary key,layer text,kind text,title text,lat real,lon real,alt real,t real,scenario text,p real,sev real,cite text)")
    c.execute("create index ix on e(scenario,t)"); c.execute("create index il on e(lat,lon)")
    c.execute("create virtual table ef using fts5(title,kind,layer,content='e',content_rowid='rowid')")
    rows = []
    for e in jl(EV):
        rows.append((e["id"], "world", e.get("kind"), e.get("title", ""), e.get("lat"), e.get("lon"), 0.0, ts(e.get("time", "")) or 0, "observed", 1.0, e.get("severity") or 0, e.get("cite")))
    for i, m in enumerate(sum((jl(b) for b in BUS), [])):
        rows.append((f"bus:{i}:{m.get('id','')}", "bus", m.get("kind"), f"{m.get('from')}→{m.get('to')}: {m.get('body') or m.get('title') or m.get('ref','')}", None, None, None, ts(m.get("ts", "")) or 0, "observed", 1.0, 0, m.get("ref")))
    c.executemany("insert or ignore into e values(?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    c.executemany("insert or ignore into e values(?,?,?,?,?,?,?,?,?,?,?,?)", cones())
    c.execute("insert into ef(ef) values('rebuild')"); c.commit(); return c.execute("select scenario,count(*) from e group by 1").fetchall()
# 3. forecast cones: 5th axis = scenario (p10/p50/p90 next 7 days of global M2.5+ counts from 1y history)
def cones(days=7):
    q = json.load(open(QD)); xs = [v for _, v in q]; last = dt.date.fromisoformat(q[-1][0]); r = xs[-30:]; s = sorted(r)
    out = []
    for h in range(1, days + 1):
        d = last + dt.timedelta(days=h); w = math.sqrt(h)  # cone widens with horizon
        mid = st.mean(xs[-7:]) * .5 + st.mean(r) * .5
        for name, pc in (("p10", .1), ("p50", .5), ("p90", .9)):
            base = s[int(pc * (len(s) - 1))]; v = mid + (base - st.median(r)) * w
            out.append((f"cone:{d}:{name}", "forecast", "quake_count", f"global quake count {name} {d}: {v:.1f}", None, None, None,
                        dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc).timestamp(), f"forecast:{name}", pc, v, "predict.py history"))
    return out
def cone_coverage(q=None, warm=60):  # backtest: share of real next-day counts inside p10..p90 (h=1)
    q = q or json.load(open(QD)); xs = [v for _, v in q]; hit = n = 0
    for i in range(warm, len(xs)):
        r = sorted(xs[i - 30:i]); mid = st.mean(xs[i - 7:i]) * .5 + st.mean(r) * .5; md = st.median(r)
        lo = mid + r[int(.1 * 29)] - md; hi = mid + r[int(.9 * 29)] - md; n += 1; hit += lo <= xs[i] <= hi
    return hit / n, n
# 2. one query across world store, palace, graph, bus
_G = None
def query(q, k=5, db=DB):
    global _G; t0 = time.perf_counter(); out = {}
    c = sqlite3.connect(db); terms = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if len(w) > 1]
    m = " OR ".join(f'"{w}"' for w in terms) or '""'
    a = time.perf_counter(); out["world+bus+forecast"] = c.execute("select e.layer,e.scenario,e.title,e.cite from ef join e on e.rowid=ef.rowid where ef match ? order by bm25(ef) limit ?", (m, k)).fetchall(); la = time.perf_counter() - a
    a = time.perf_counter(); out["palace"] = [r[:3] for r in palace.search(q, k)]; lp = time.perf_counter() - a
    a = time.perf_counter(); _G = _G or json.load(open(GRAPH))
    out["graph"] = sorted([n["id"] for n in _G["nodes"] if any(w in n["id"].lower() for w in terms)], key=len)[:k]; lg = time.perf_counter() - a
    out["_ms"] = {"store": la * 1e3, "palace": lp * 1e3, "graph": lg * 1e3, "total": (time.perf_counter() - t0) * 1e3}
    return out
# 4. anomaly alerts: robust z (median/MAD) over trailing 30 days
def anomalies(xs, z=3.5, win=30):
    al = []
    for i in range(win, len(xs)):
        r = xs[i - win:i]; md = st.median(r); mad = st.median([abs(x - md) for x in r]) or 1
        if abs(0.6745 * (xs[i] - md) / mad) > z: al.append(i)
    return al
# 5. whole-picture brief under 2k tokens
def brief(db=DB):
    c = sqlite3.connect(db); L = ["# Tessera whole-picture brief (5D)"]
    for k, n, mx in c.execute("select kind,count(*),max(sev) from e where layer='world' group by 1 order by 2 desc"): L.append(f"- {k}: {n} events, max severity {mx:.2f}")
    L.append("## Top salient (severity)")
    for t, ci in c.execute("select title,cite from e where layer='world' order by sev desc limit 8"): L.append(f"- {t} [{ci}]")
    L.append("## Regions (10° cells, busiest)")
    for la, lo, n in c.execute("select cast(lat/10 as int)*10,cast(lon/10 as int)*10,count(*) from e where lat is not null group by 1,2 order by 3 desc limit 5"): L.append(f"- cell {la},{lo}: {n}")
    L.append("## Possibility axis (quake count cone)")
    for t in c.execute("select title from e where scenario like 'forecast:%' and title like '%p50%' order by t limit 3"): L.append(f"- {t[0]}")
    xs = [v for _, v in json.load(open(QD))]; a = anomalies(xs); L.append(f"## Anomalies: {len(a)} anomalous days in {len(xs)}-day history (robust z>3.5)")
    L.append("## Mesh bus (latest)")
    for t in c.execute("select title from e where layer='bus' order by t desc limit 4"): L.append(f"- {t[0][:120]}")
    g = json.load(open(GRAPH)); L.append(f"## Memory graph: {len(g['nodes'])} nodes, {len(g['edges'])} edges; top: " + ", ".join(n["id"] for n in sorted(g["nodes"], key=lambda n: -n.get("degree", 0))[:5]))
    return "\n".join(L)
toks = lambda s: math.ceil(len(s) / 4)  # ~4 chars/token estimate
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build": print(build())
    elif cmd == "query": print(json.dumps(query(" ".join(sys.argv[2:])), indent=1, default=str))
    elif cmd == "brief": print(brief())
