#!/usr/bin/env python3
"""Tessera's Eye v2 Shepherd feeds: aggregate-only summaries (no per-object tracking, no people).
 - celestrak: active-satellite catalog -> counts by orbit class (LEO/MEO/GEO/HEO). Object names/IDs are discarded.
 - kp: NOAA SWPC planetary K index (geomagnetic activity), last 7 days.
usage: feeds2.py pull [--fixtures DIR]"""
import csv, io, json, os, sys, time, datetime, urllib.request, hashlib, collections
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, "data")
FEEDS = {
 "celestrak": ("https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv", "CelesTrak GP data (public; attribution CelesTrak / 18 SDS)"),
 "kp": ("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json", "NOAA SWPC, public domain"),
}
MU = 398600.4418; RE = 6378.137
def orbit_class(mm, ecc):
    n = mm * 2 * 3.141592653589793 / 86400; a = (MU / n**2) ** (1/3); per = a*(1-ecc) - RE
    if ecc > 0.25: return "HEO"
    if per < 2000: return "LEO"
    if abs(a - 42164) < 700: return "GEO"
    return "MEO"
def parse_celestrak(text):
    c = collections.Counter(); epochs = []
    for r in csv.DictReader(io.StringIO(text)):
        try: c[orbit_class(float(r["MEAN_MOTION"]), float(r["ECCENTRICITY"]))] += 1; epochs.append(r["EPOCH"])
        except (ValueError, KeyError, ZeroDivisionError): c["bad"] += 1
    return {"kind": "satellite-census", "total": sum(v for k, v in c.items() if k != "bad"), "by_orbit": dict(c),
            "newest_epoch": max(epochs) if epochs else None}
def parse_kp(rows):
    if rows and isinstance(rows[0], list): rows = [dict(zip(rows[0], r)) for r in rows[1:]]
    kp = [float(r["Kp"]) for r in rows]
    return {"kind": "geomagnetic", "n": len(kp), "latest_kp": kp[-1] if kp else None, "max_kp": max(kp) if kp else None,
            "storm_periods_kp5plus": sum(k >= 5 for k in kp), "from": rows[0]["time_tag"] if rows else None, "to": rows[-1]["time_tag"] if rows else None}
def fetch(src):
    r = urllib.request.Request(FEEDS[src][0], headers={"User-Agent": "tessera-eye/2 (read-only research)"})
    t = time.time(); b = urllib.request.urlopen(r, timeout=60).read(); return b.decode(), time.time()-t, len(b)
def pull(fixdir=None, out=os.path.join(DATA, "summaries.jsonl"), bus=os.path.join(DATA, "bus.jsonl")):
    rep = {}; now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    for src, fn in (("celestrak", "celestrak.csv"), ("kp", "kp.json")):
        try:
            if fixdir: txt, dt, n = open(os.path.join(fixdir, fn)).read(), 0.0, 0
            else: txt, dt, n = fetch(src)
            s = parse_celestrak(txt) if src == "celestrak" else parse_kp(json.loads(txt))
        except Exception as x: rep[src] = {"error": str(x)[:120]}; continue
        s.update(source=src, license=FEEDS[src][1], cite=FEEDS[src][0], pulled=now)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "a").write(json.dumps(s) + "\n")
        body = f"{src}: " + json.dumps({k: v for k, v in s.items() if k in ("total","by_orbit","latest_kp","max_kp","storm_periods_kp5plus")})
        open(bus, "a").write(json.dumps({"id": "eye-" + hashlib.sha1((src+now).encode()).hexdigest()[:10], "ts": now, "from": "rick", "to": "tessera",
            "kind": "note", "ref": "tessera-eye", "body": body, "shepherd": src, "cite": FEEDS[src][0]}) + "\n")
        rep[src] = {**{k: s.get(k) for k in ("total","by_orbit","latest_kp","max_kp","storm_periods_kp5plus")}, "latency_ms": round(dt*1000), "bytes": n}
    return rep
if __name__ == "__main__":
    a = sys.argv[1:]; print(json.dumps(pull(a[2] if len(a) > 2 else None), indent=1))
