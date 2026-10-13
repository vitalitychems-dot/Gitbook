#!/usr/bin/env python3
"""Tessera's Eye v1: read-only Shepherd fetchers -> normalized events -> JSONL index + mesh bus + offline map.
usage: eye.py pull [--fixtures DIR] | map | stats
Public open data only. No person-level data: events are natural/weather phenomena."""
import json, sys, os, time, urllib.request, hashlib, datetime, html
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data"); IDX = os.path.join(DATA, "events.jsonl"); BUS = os.path.join(DATA, "bus.jsonl")
CAP = 20 * 1024 * 1024  # index cap 20MB
FEEDS = {
 "usgs": ("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson", "USGS, public domain"),
 "eonet": ("https://eonet.gsfc.nasa.gov/api/v3/events?status=open&limit=200", "NASA EONET, public domain"),
 "nws": ("https://api.weather.gov/alerts/active?severity=Severe,Extreme", "NOAA/NWS, public domain"),
 "meteo": ("https://api.open-meteo.com/v1/forecast?latitude=41.88,29.76,34.05,40.71,51.51,35.68,-33.87,-23.55&longitude=-87.63,-95.37,-118.24,-74.01,-0.13,139.69,151.21,-46.63&current=temperature_2m,wind_speed_10m,precipitation", "Open-Meteo, CC BY 4.0"),
}
def ev(src, lic, url, eid, kind, title, lat, lon, t, sev, extra):
    return {"id": f"{src}:{eid}", "source": src, "license": lic, "cite": url, "kind": kind, "title": title,
            "lat": lat, "lon": lon, "time": t, "severity": sev, "extra": extra}
def centroid(g):
    pts = []
    def walk(c):
        if isinstance(c[0], (int, float)): pts.append(c)
        else: [walk(x) for x in c]
    if g and g.get("coordinates"): walk(g["coordinates"])
    return (sum(p[1] for p in pts)/len(pts), sum(p[0] for p in pts)/len(pts)) if pts else (None, None)
def parse(src, d):
    url, lic = FEEDS[src]; out = []
    if src == "usgs":
        for f in d["features"]:
            p = f["properties"]; lon, lat = f["geometry"]["coordinates"][:2]
            m = p.get("mag") or 0
            out.append(ev(src, lic, p.get("url") or url, f["id"], "earthquake", p.get("title"), lat, lon,
                datetime.datetime.fromtimestamp(p["time"]/1000, datetime.timezone.utc).isoformat(), round(min(m/7, 1), 2), {"mag": m}))
    elif src == "eonet":
        for e in d["events"]:
            g = e["geometry"][-1]; c = g["coordinates"]
            lat, lon = (c[1], c[0]) if isinstance(c[0], (int, float)) else centroid(g)
            out.append(ev(src, lic, e.get("link") or url, e["id"], e["categories"][0]["id"], e["title"], lat, lon, g["date"], 0.5, {}))
    elif src == "nws":
        for f in d["features"]:
            p = f["properties"]; lat, lon = centroid(f.get("geometry"))
            if lat is None: continue  # zone-only alerts skipped in v1
            out.append(ev(src, lic, p.get("@id") or url, p["id"].split(":")[-1][-40:], "weather-alert", p.get("headline") or p.get("event"),
                lat, lon, p.get("sent"), 1.0 if p.get("severity") == "Extreme" else 0.7, {"event": p.get("event")}))
    elif src == "meteo":
        for c in (d if isinstance(d, list) else [d]):
            cur = c["current"]
            out.append(ev(src, lic, url, f'{c["latitude"]},{c["longitude"]}@{cur["time"]}', "weather-now",
                f'{cur["temperature_2m"]}°C wind {cur["wind_speed_10m"]} km/h', c["latitude"], c["longitude"], cur["time"]+"Z", 0.1, cur))
    return [e for e in out if e["lat"] is not None]
def fetch(src):
    r = urllib.request.Request(FEEDS[src][0], headers={"User-Agent": "tessera-eye/1 (read-only research)", "Accept": "application/geo+json, application/json"})
    t = time.time(); b = urllib.request.urlopen(r, timeout=30).read()
    return json.loads(b), time.time() - t, len(b)
def bus_msg(src, events, ms):
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    body = f"{src}: {len(events)} events in {ms:.0f} ms; top: " + "; ".join(e["title"] or "" for e in sorted(events, key=lambda e: -e["severity"])[:3])
    return {"id": "eye-" + hashlib.sha1((src+now).encode()).hexdigest()[:10], "ts": now, "from": "rick", "to": "tessera",
            "kind": "note", "ref": "tessera-eye", "body": body.replace("%", " pct"), "shepherd": src, "cite": FEEDS[src][0]}
def index(events, path=IDX):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    seen = set()
    if os.path.exists(path): seen = {json.loads(l)["id"] for l in open(path)}
    new = [e for e in events if e["id"] not in seen]
    with open(path, "a") as f:
        for e in new: f.write(json.dumps(e) + "\n")
    if os.path.getsize(path) > CAP:  # keep newest half
        L = open(path).readlines(); open(path, "w").writelines(L[len(L)//2:])
    return len(new)
def chunks(events):  # palace-ready text chunks with citations
    return [{"doc": e["cite"], "text": f'{e["kind"]} | {e["title"]} | {e["time"]} | {e["lat"]:.2f},{e["lon"]:.2f} | src {e["license"]}'} for e in events]
def pull(fixdir=None, idx=IDX, bus=BUS):
    report = {}; allev = []
    for src in FEEDS:
        try:
            if fixdir: d, dt, n = json.load(open(os.path.join(fixdir, src + ".json"))), 0.0, 0
            else: d, dt, n = fetch(src)
            es = parse(src, d)
        except Exception as x: report[src] = {"error": str(x)[:120]}; continue
        allev += es; m = bus_msg(src, es, dt*1000)
        os.makedirs(os.path.dirname(bus), exist_ok=True)
        open(bus, "a").write(json.dumps(m) + "\n")
        report[src] = {"events": len(es), "latency_ms": round(dt*1000), "bytes": n}
    report["new_indexed"] = index(allev, idx); report["total"] = len(allev)
    with open(os.path.join(os.path.dirname(idx), "chunks.jsonl"), "w") as f:
        for c in chunks(allev): f.write(json.dumps(c, ensure_ascii=False) + "\n")
    return report
def make_map(idx=IDX, out=os.path.join(HERE, "eye.html")):
    evs = [json.loads(l) for l in open(idx)][-5000:]
    tpl = open(os.path.join(HERE, "map_template.html")).read()
    open(out, "w").write(tpl.replace("/*EVENTS*/[]", json.dumps(evs).replace("</", "<\\/")))
    return out, len(evs)
if __name__ == "__main__":
    a = sys.argv[1:] or ["stats"]
    if a[0] == "pull": print(json.dumps(pull(a[2] if len(a) > 2 else None), indent=1))
    elif a[0] == "map": print(make_map())
    else:
        L = [json.loads(l) for l in open(IDX)] if os.path.exists(IDX) else []
        import collections; print(len(L), "events", dict(collections.Counter(e["source"] for e in L)), os.path.getsize(IDX) if L else 0, "bytes")
