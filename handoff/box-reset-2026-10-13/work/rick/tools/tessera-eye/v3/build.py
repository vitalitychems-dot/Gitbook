"""Tessera's Eye v3 builder: public open data only -> one self-contained offline HTML globe (eye3.html).
No people, no cameras, no ALPR, no per-aircraft/ship tracks. Satellites are objects (names allowed)."""
import os, sys, csv, json, math, time, base64, gzip, urllib.request, datetime as dt, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "vendor"))
from sgp4.api import Satrec, WGS72, jday
from sgp4 import omm
D = os.path.join(H, "data"); EYE = os.path.dirname(H); TOOLS = os.path.dirname(EYE)
FORBIDDEN = ["icao", "callsign", "mmsi", "imo", "plate", "alpr", "face", "cctv", "camera", "user_id", "username",
             "phone", "email", "device_id", "author", "contact", "person", "registration", "tail_number"]
STEPS = list(range(-12, 13, 2))  # hours relative to build time (13 frames)

def get(url, path, timeout=40):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tessera-eye/3 (open data)"})
        b = urllib.request.urlopen(req, timeout=timeout).read()
        if len(b) > 200: open(path, "wb").write(b)
    except Exception as e: print("fetch fail (using cache)", url, e)
    return path

def gmst(jd_ut1):
    t = (jd_ut1 - 2451545.0) / 36525.0
    g = 67310.54841 + (876600 * 3600 + 8640184.812866) * t + 0.093104 * t * t - 6.2e-6 * t ** 3
    return math.radians((g % 86400) / 240.0)

def teme_to_geo(r, jd):
    th = gmst(jd); x, y, z = r
    xe = x * math.cos(th) + y * math.sin(th); ye = -x * math.sin(th) + y * math.cos(th)
    lon = math.degrees(math.atan2(ye, xe)); rho = math.hypot(xe, ye)
    lat = math.degrees(math.atan2(z, rho)); alt = math.sqrt(x * x + y * y + z * z) - 6371.0
    return lat, lon, alt

def orbit_class(n, e):
    a = (398600.4418 / (n * 2 * math.pi / 86400) ** 2) ** (1 / 3) - 6378.137
    if e > 0.25: return "HEO"
    if a < 2000: return "LEO"
    if abs(a - 35786) < 1000: return "GEO"
    return "MEO"

def satellites(rows, t0):
    out, names, t = [], [], time.time()
    for f in rows:
        s = Satrec()
        try: omm.initialize(s, f)
        except Exception: continue
        fr = []
        for h in STEPS:
            tt = t0 + dt.timedelta(hours=h); jd, frc = jday(tt.year, tt.month, tt.day, tt.hour, tt.minute, tt.second)
            e, r, v = s.sgp4(jd, frc)
            if e: fr = None; break
            la, lo, al = teme_to_geo(r, jd + frc); fr += [round(la, 2), round(lo, 2), int(al)]
        if not fr: continue
        n = float(f["MEAN_MOTION"]); ec = float(f["ECCENTRICITY"])
        out.append({"n": f["OBJECT_NAME"], "id": int(f["NORAD_CAT_ID"]), "c": orbit_class(n, ec),
                    "el": [n, ec, float(f["INCLINATION"]), float(f["RA_OF_ASC_NODE"]), float(f["ARG_OF_PERICENTER"]),
                           float(f["MEAN_ANOMALY"]), f["EPOCH"]], "p": fr})
    return out, time.time() - t

def load_jsonl(p): return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

def build(live=True):
    T = time.time(); t0 = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    if live:
        get("https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv", os.path.join(D, "gp.csv"))
        get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json", os.path.join(D, "kp.json"))
        get("https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv", os.path.join(D, "firms.csv"))
    rows = list(csv.DictReader(open(os.path.join(D, "gp.csv"))))
    sats, sgp_s = satellites(rows, t0)
    ev = [e for e in load_jsonl(os.path.join(EYE, "data", "events.jsonl"))]
    events = [{"k": e["kind"], "s": e["source"], "t": e["title"][:90], "la": e["lat"], "lo": e["lon"], "tm": e.get("time"),
               "sv": e.get("severity"), "cite": e.get("cite")} for e in ev if e.get("lat") is not None]
    # fires: aggregated to 1-degree cells (counts only; objects = thermal anomalies, not people)
    fires = {}
    if os.path.exists(os.path.join(D, "firms.csv")):
        for r in csv.DictReader(open(os.path.join(D, "firms.csv"))):
            k = (math.floor(float(r["latitude"])) + .5, math.floor(float(r["longitude"])) + .5); fires[k] = fires.get(k, 0) + 1
    fires = [[a, b, c] for (a, b), c in fires.items()]
    kp = []
    try:
        j = json.load(open(os.path.join(D, "kp.json")))
        if isinstance(j[0], list): kp = [[r[0], float(r[1])] for r in j[1:]]
        else: kp = [[r["time_tag"], float(r["Kp"])] for r in j]
    except Exception: pass
    # tesseract forecast cones
    spec = importlib.util.spec_from_file_location("tz", os.path.join(TOOLS, "tesseract", "tesseract.py")); tz = importlib.util.module_from_spec(spec)
    cones = []
    try:
        spec.loader.exec_module(tz); cones = [[c[0].split(":")[1], c[0].split(":")[2], round(c[10], 1)] for c in tz.cones()]
    except Exception as e: print("cones unavailable", e)
    # Simons heat map: same 10-degree grid as tools/simons, last 90 days, log1p counts
    q = list(csv.DictReader(open(os.path.join(TOOLS, "simons", "data", "quakes.csv"))))
    last = max(r["date"] for r in q); cut = (dt.date.fromisoformat(last) - dt.timedelta(days=90)).isoformat()
    grid = [[0] * 36 for _ in range(18)]
    for r in q:
        if r["date"] > cut:
            la = min(int((float(r["lat"]) + 90) // 10), 17); lo = min(int((float(r["lon"]) + 180) // 10), 35); grid[la][lo] += 1
    heat = [[round(math.log1p(v), 3) for v in row] for row in grid]
    dv = []
    try:
        for it in json.load(open(os.path.join(D, "dv.json")))["data"]["items"]:
            dv.append({"title": it["name"][:160], "url": it["url"], "pub": it.get("published_at", "")[:10],
                       "subj": it.get("subjects", [])[:4], "desc": (it.get("description") or "")[:240]})
    except Exception: pass
    data = {"t0": t0.isoformat(), "steps": STEPS, "sats": sats, "events": events, "fires": fires, "kp": kp, "cones": cones,
            "heat": heat, "heat_window": [cut, last], "dataverse": dv,
            "sources": {"sats": "CelesTrak GP active (SGP4, sgp4 2.27 MIT)", "img": "NASA GIBS MODIS Terra CorrectedReflectance TrueColor",
                        "events": "USGS, NASA EONET, NWS, Open-Meteo (eye.py)", "fires": "NASA FIRMS MODIS 24h, 1-degree counts",
                        "kp": "NOAA SWPC", "cones": "tools/tesseract cones()", "heat": "tools/simons grid (USGS M4.5+)", "dataverse": "Harvard Dataverse search API"}}
    js = json.dumps(data, separators=(",", ":"))
    img = base64.b64encode(open(os.path.join(D, "gibs_base.jpg"), "rb").read()).decode()
    html = open(os.path.join(H, "globe_template.html")).read().replace("/*DATA*/null", js).replace("%%IMG%%", img)
    open(os.path.join(H, "eye3.html"), "w").write(html)
    st = {"build_s": round(time.time() - T, 2), "sgp4_s": round(sgp_s, 2), "sats": len(sats), "sat_rows": len(rows),
          "events": len(events), "fire_cells": len(fires), "kp_pts": len(kp), "cones": len(cones), "dataverse": len(dv),
          "html_bytes": os.path.getsize(os.path.join(H, "eye3.html")), "classes": {c: sum(s["c"] == c for s in sats) for c in ("LEO", "MEO", "GEO", "HEO")}}
    json.dump(st, open(os.path.join(H, "build_stats.json"), "w"), indent=1); print(st); return data

if __name__ == "__main__": build(live="--offline" not in sys.argv)
