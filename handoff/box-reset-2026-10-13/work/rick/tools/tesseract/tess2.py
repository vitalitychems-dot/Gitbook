#!/usr/bin/env python3
"""Tesseract inventions 7-20. stdlib only. Never writes outside tools/tesseract/."""
import os, sys, json, sqlite3, time, math, re, hashlib, statistics as st, datetime as dt, subprocess, gzip
import tesseract as T
HERE = T.HERE; STATE = os.path.join(HERE, "state"); os.makedirs(STATE, exist_ok=True)
STOP = set("the a an and or of to in is for on with that this it as be are by at from not who has".split())
# 13 cone calibration: width multiplier k fit on first half, scored on held-out second half
def band(xs, i, k):
    r = sorted(xs[i - 30:i]); mid = st.mean(xs[i - 7:i]) * .5 + st.mean(r) * .5; md = st.median(r)
    return mid + k * (r[3] - md), mid + k * (r[26] - md)
def cover(xs, lo_i, hi_i, k): return sum(band(xs, i, k)[0] <= xs[i] <= band(xs, i, k)[1] for i in range(lo_i, hi_i)) / (hi_i - lo_i)
def calibrate(xs=None, target=.8):
    xs = xs or [v for _, v in json.load(open(T.QD))]; h = (60 + len(xs)) // 2
    k = 1.0
    while cover(xs, 60, h, k) < target and k < 5: k = round(k + .05, 2)
    return {"k": k, "train_cov": round(cover(xs, 60, h, k), 3), "holdout_cov": round(cover(xs, h, len(xs), k), 3), "holdout_cov_k1": round(cover(xs, h, len(xs), 1), 3), "holdout_days": len(xs) - h}
# bus-ranking fix: coordination (rows matching more distinct query terms first), IDF-weighted, then bm25.
# Diagnosis: OR-bm25 let short bus rows win on one rare word ("tessera" is in every bus header).
AGENTS = {'rick','tessera','all','moderator','security','einstein','pharaoh','father'}
def query2(q, k=5, db=T.DB):
    c = sqlite3.connect(db); N = c.execute("select count(*) from e").fetchone()[0]
    terms = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if len(w) > 1 and w not in STOP]
    hit = {}
    for w in terms:
        ids = [r[0] for r in c.execute("select rowid from ef where ef match ?", (f'"{w}"',))]
        idf = math.log(1 + N / (1 + len(ids)))
        bus = {r[0] for r in c.execute("select rowid from e where layer='bus'")} if w in AGENTS else set()
        for i in ids:
            if i in bus: continue  # agent names in bus headers are addressing, not content
            hit.setdefault(i, [0, 0.0]); hit[i][0] += 1; hit[i][1] += idf
    if not hit: return []
    m = " OR ".join(f'"{w}"' for w in terms); bm = {r: s for r, s in c.execute("select rowid,bm25(ef) from ef where ef match ?", (m,))}
    top = sorted(hit, key=lambda i: (-hit[i][0], -hit[i][1], bm.get(i, 0)))[:k]
    return [c.execute("select layer,kind,title,cite from e where rowid=?", (i,)).fetchone() for i in top]
def query1(q, k=5, db=T.DB):  # old ranking, for comparison
    c = sqlite3.connect(db); terms = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if len(w) > 1]
    return c.execute("select e.layer,e.kind,e.title,e.cite from ef join e on e.rowid=ef.rowid where ef match ? order by bm25(ef) limit ?", (" OR ".join(f'"{w}"' for w in terms), k)).fetchall()
RANK_SET = [("earthquake alaska tessera", "world"), ("wildfire idaho for tessera", "world"), ("tessera storm alert", "world"),
 ("rick earthquake california", "world"), ("who has graph", "bus"), ("bus prototype claim", "bus"), ("celestrak satellites", "bus"),
 ("quake count p50 forecast", "forecast"), ("wildfire wyoming", "world"), ("tessera weather now", "world")]
def rank_eval(f):
    return sum((f(q, 1) or [("",)])[0][0] == want for q, want in RANK_SET) / len(RANK_SET)
# 20 honest-claims lint: every bullet line needs a cite ([..]/http) or a number
def lint(text):
    bad = [l for l in text.splitlines() if l.startswith("- ") and not re.search(r"\d|\[|http", l)]
    return bad
# 17 feed health: staleness per source from newest event time + bus summaries
MAXAGE = {"usgs": 3600, "eonet": 6 * 3600, "nws": 3 * 3600, "open-meteo": 3 * 3600}
def health(now=None, events=None):
    now = now or time.time(); events = events if events is not None else T.jl(T.EV); last = {}
    for e in events:
        t = T.ts(e.get("time", "")) or 0; s = e.get("source"); last[s] = max(last.get(s, 0), t)
    return {s: {"age_s": int(now - t), "stale": now - t > MAXAGE.get(s, 6 * 3600)} for s, t in last.items()}
# 11 delta brief
def delta(db=T.DB, snap=os.path.join(STATE, "last_ids.json")):
    c = sqlite3.connect(db); cur = {i: t for i, t in c.execute("select id,title from e where scenario='observed'")}
    old = set(json.load(open(snap))) if os.path.exists(snap) else set()
    new = [cur[i] for i in cur if i not in old]; gone = len(old - set(cur))
    json.dump(sorted(cur), open(snap, "w")); return {"new": len(new), "gone": gone, "lines": [f"- NEW {t}" for t in new[:15]]}
# 9 salience = severity × novelty × relevance
def salience(db=T.DB, now=None, focus=("tessera", "quantum", "satellite")):
    c = sqlite3.connect(db); rows = c.execute("select id,title,kind,sev,t from e where layer='world'").fetchall()
    now = now or max(r[4] for r in rows); kc = {}
    for r in rows: kc[r[2]] = kc.get(r[2], 0) + 1
    out = []
    for i, ti, k, s, t in rows:
        nov = math.exp(-max(0, now - t) / 86400) * (1 / math.log(2 + kc[k]))  # recent + rare kind
        rel = 1 + .5 * any(f in ti.lower() for f in focus)
        out.append((round((s or 0) * nov * rel, 4), i, ti))
    return sorted(out, reverse=True)
# 10 cross-links world → palace/graph
def links(db=T.DB, k=2, maxev=40):
    c = sqlite3.connect(db); g = json.load(open(T.GRAPH)); out = []
    for kind, in c.execute("select distinct kind from e where layer='world'"):
        word = re.sub(r"(?<!^)([A-Z])", r" \1", kind).replace("-", " ").lower().split()[-1].rstrip("s")
        pal = [r[0] for r in T.palace.search(word, k)]; gr = [n["id"] for n in g["nodes"] if word in n["id"].lower()][:k]
        out.append({"kind": kind, "term": word, "palace": pal, "graph": gr})
    return out
# 14 geo grid (10°)
def grid(db=T.DB, deg=10):
    c = sqlite3.connect(db); cells = {}
    for la, lo in c.execute("select lat,lon from e where lat is not null"):
        key = (math.floor(la / deg) * deg, math.floor(lo / deg) * deg); cells[key] = cells.get(key, 0) + 1
    return cells
# 16 compactor: raw events → daily×kind aggregates (gz), keep cites sample
def compact(src=T.EV, out=os.path.join(STATE, "daily.json.gz")):
    agg = {}
    for e in T.jl(src):
        key = f"{(e.get('time') or '')[:10]}|{e.get('kind')}"; a = agg.setdefault(key, {"n": 0, "max_sev": 0, "cites": []})
        a["n"] += 1; a["max_sev"] = max(a["max_sev"], e.get("severity") or 0)
        if len(a["cites"]) < 2: a["cites"].append(e.get("cite"))
    with gzip.open(out, "wt") as f: json.dump(agg, f)
    return {"raw_bytes": os.path.getsize(src), "compact_bytes": os.path.getsize(out), "groups": len(agg), "total": sum(a["n"] for a in agg.values())}
# 18 budget brief: trim lowest-priority lines until ≤ N tokens (keep headers)
def budget_brief(n, text=None):
    L = (text or T.brief()).splitlines()
    while T.toks("\n".join(L)) > n:
        idx = [i for i, l in enumerate(L) if l.startswith("- ")]
        if not idx: break
        L.pop(idx[-1])
    return "\n".join(L)
# 8 replay frames (data for HTML slider)
def replay(db=T.DB, step=3600):
    c = sqlite3.connect(db); rows = c.execute("select t,kind,lat,lon,sev from e where layer='world' and lat is not null and t>0 order by t").fetchall()
    t0 = rows[0][0]; fr = {}
    for t, k, la, lo, s in rows: fr.setdefault(int((t - t0) // step), []).append([round(la, 1), round(lo, 1), k[:5], round(s or 0, 2)])
    return {"t0": t0, "step": step, "frames": fr, "n": len(rows)}
# 12 what-if branches: drop a feed / scale a kind, recompute brief stats under scenario cf:*
def whatif(db=T.DB, drop=None, scale=None):
    c = sqlite3.connect(db); name = "cf:" + (f"drop-{drop}" if drop else f"scale-{scale[0]}x{scale[1]}")
    c.execute("delete from e where scenario=?", (name,))
    rows = c.execute("select * from e where scenario='observed' and layer='world'").fetchall(); out = []
    for r in rows:
        r = list(r)
        if drop and r[11] and drop in (r[0].split(":")[0]): continue
        if scale and r[2] == scale[0]: r[10] = min(1, (r[10] or 0) * scale[1])
        r[0] = f"{name}|{r[0]}"; r[8] = name; out.append(r)
    c.executemany("insert into e values(?,?,?,?,?,?,?,?,?,?,?,?)", out); c.commit()
    return {"scenario": name, "rows": len(out), "observed": len(rows)}
# 15 mesh-flow: bus messages per lane per kind + gate verdicts
def flow(paths=T.BUS):
    lanes = {}
    for p in paths:
        for m in T.jl(p):
            l = lanes.setdefault(m.get("from", "?"), {}); k = m.get("kind") or "msg"; l[k] = l.get(k, 0) + 1
            if m.get("verdict"): l["verdict:" + m["verdict"]] = l.get("verdict:" + m["verdict"], 0) + 1
    return lanes
# 19 Mesh City overlay (writes city5d.json; never touches meshcity/)
def overlay(out=os.path.join(HERE, "city5d.json")):
    city = json.load(open(f"{T.T}/meshcity/city.json")); fl = flow(); top = salience()[:20]; mx = top[0][0] or 1
    for b in city["buildings"]:
        nm = b["name"].lower(); b["activity"] = sum(fl.get(nm, {}).values())
        b["salience"] = round(min(1, b["activity"] / 5 + sum(s for s, _, ti in top if nm in ti.lower()) / mx), 3)
    city["world_glow"] = round(sum(s for s, _, _ in top) / (20 * mx), 3)
    json.dump(city, open(out, "w")); return city
