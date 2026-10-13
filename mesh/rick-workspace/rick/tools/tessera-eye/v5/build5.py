#!/usr/bin/env python3
"""Tessera's Eye v5 builder: unify all SAFE live layers into one flat deep-zoom map (eye5.html).
Includes: USGS, EONET, FIRMS, NWS, Open-Meteo, CelesTrak current positions, Kp, Simons heat,
forecast cones, Eye Shield probe points (no people/vehicles), sources for KartaView + Esri/USGS/GIBS.
Excludes: see ../EXCLUDED.md. No pushes. Offline-capable embed + online live refresh."""
from __future__ import annotations
import csv, json, math, os, re, sys, time, hashlib, urllib.request, datetime as dt
from pathlib import Path

H = Path(__file__).resolve().parent
EYE = H.parent
TOOLS = EYE.parent
V3 = EYE / "v3"
SHIELD = TOOLS / "eye-shield"
SIMONS = TOOLS / "simons"

# Rough ISO 3166-1 alpha-2 country centroids (public knowledge; country-level only).
CC = {
    "US": (39.8, -98.5), "CA": (56.1, -106.3), "MX": (23.6, -102.5), "GB": (54.0, -2.5),
    "DE": (51.2, 10.4), "FR": (46.2, 2.2), "NL": (52.1, 5.3), "RU": (61.5, 105.3),
    "CN": (35.9, 104.2), "JP": (36.2, 138.3), "KR": (35.9, 127.8), "IN": (20.6, 78.9),
    "BR": (-14.2, -51.9), "AU": (-25.3, 133.8), "NZ": (-40.9, 174.9), "ZA": (-30.6, 22.9),
    "SG": (1.4, 103.8), "HK": (22.3, 114.2), "TW": (23.7, 121.0), "IE": (53.1, -8.2),
    "SE": (60.1, 18.6), "NO": (60.5, 8.5), "FI": (61.9, 25.7), "PL": (51.9, 19.1),
    "ES": (40.5, -3.7), "IT": (41.9, 12.6), "TR": (38.96, 35.2), "UA": (48.4, 31.2),
    "IL": (31.0, 34.8), "AE": (23.4, 53.8), "SA": (23.9, 45.1), "EG": (26.8, 30.8),
    "NG": (9.1, 8.7), "KE": (-0.0, 37.9), "AR": (-38.4, -63.6), "CL": (-35.7, -71.5),
    "CO": (4.6, -74.3), "PE": (-9.2, -75.0), "VE": (6.4, -66.6), "TH": (15.9, 100.9),
    "VN": (14.1, 108.3), "ID": (-0.8, 113.9), "MY": (4.2, 101.9), "PH": (12.9, 121.8),
    "PK": (30.4, 69.3), "BD": (23.7, 90.4), "IR": (32.4, 53.7), "IQ": (33.2, 43.7),
    "RO": (45.9, 24.97), "CZ": (49.8, 15.5), "AT": (47.5, 14.6), "CH": (46.8, 8.2),
    "BE": (50.5, 4.5), "PT": (39.4, -8.2), "GR": (39.1, 21.8), "HU": (47.2, 19.5),
    "ZZ": (0.0, -30.0), "None": (0.0, -30.0), "": (0.0, -30.0),
}
CLASS = {"LEO": 0, "MEO": 1, "GEO": 2, "HEO": 3}

def get(url, path, timeout=40):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tessera-eye/5 (open data, read-only)"})
        b = urllib.request.urlopen(req, timeout=timeout).read()
        if len(b) > 100:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b)
            return True, len(b)
    except Exception as e:
        print("fetch fail (cache ok)", url.split("?")[0], e)
    return False, 0

def load_v3():
    html = (V3 / "eye3.html").read_text()
    m = re.search(r"const D=(\{.*?\});\n", html, re.S)
    if not m:
        # globe template uses /*DATA*/null style
        m = re.search(r"(?:const D=|/\*DATA\*/)(\{.*?\})", html, re.S)
    if not m:
        raise SystemExit("cannot parse v3 eye3.html data")
    return json.loads(m.group(1) if m.group(1).startswith("{") else re.search(r"(\{.*\})", m.group(0), re.S).group(1))

def sat_current(sats, mid_idx=6):
    """Compact current-frame positions: [la, lo, class_code] + parallel names for click."""
    pts, names = [], []
    for s in sats:
        p = s.get("p") or []
        # each frame is la,lo,alt triple; mid frame ~ index 6 in 13-frame list
        i = mid_idx * 3
        if len(p) < i + 2:
            continue
        pts.append([p[i], p[i + 1], CLASS.get(s.get("c"), 0)])
        names.append([s.get("n", "")[:40], s.get("id"), s.get("c")])
    return pts, names

def enrich_probes(layer):
    """Map Eye Shield points to lat/lon via country centroid (or Atlantic placeholder)."""
    sys.path.insert(0, str(SHIELD))
    lookup = None
    try:
        from feeds_loader import ThreatFeeds
        feeds = ThreatFeeds()
        lookup = feeds.lookup_asn
    except Exception as e:
        print("asn lookup unavailable", e)

    out, seen = [], {}
    for p in layer.get("points") or []:
        ip = p.get("ip") or ""
        cc = p.get("country")
        asn = p.get("asn")
        if lookup and (not cc or cc in ("None", "null", None, "0")):
            try:
                info = lookup(ip) or {}
                cc = info.get("country") or cc
                asn = info.get("asn") or asn
            except Exception:
                pass
        cc_key = str(cc or "ZZ")
        if cc_key in ("None", "null", "0"):
            cc_key = "ZZ"
        la, lo = CC.get(cc_key, CC["ZZ"])
        # jitter so multiple probes in one country don't stack
        h = int(hashlib.sha1(ip.encode()).hexdigest()[:8], 16)
        jla = ((h % 1000) / 1000 - 0.5) * 4.0
        jlo = (((h // 1000) % 1000) / 1000 - 0.5) * 6.0
        geo = "country_centroid" if cc_key != "ZZ" else "unlocated_placeholder"
        out.append({
            "k": "probe", "s": "eye-shield",
            "t": f"probe {p.get('kind')} {ip}",
            "la": round(la + jla, 3), "lo": round(lo + jlo, 3),
            "ip": ip, "kind": p.get("kind"), "sev": p.get("severity"),
            "cc": cc_key, "asn": str(asn or ""), "feeds": p.get("feeds") or [],
            "detail": (p.get("detail") or "")[:160], "geo": geo,
        })
        seen[ip] = 1
    return out, {
        "updated": layer.get("updated"),
        "findings_count": layer.get("findings_count"),
        "anomaly": layer.get("anomaly"),
        "defensive_only": True,
        "points": len(out),
        "note": "Country-centroid or unlocated placeholder only. No people/vehicles.",
    }

def build(live=True):
    T = time.time()
    fetch_stats = {}
    if live:
        d3 = V3 / "data"
        for name, url in (
            ("firms.csv", "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv"),
            ("kp.json", "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"),
        ):
            ok, n = get(url, d3 / name)
            fetch_stats[name] = {"ok": ok, "bytes": n}
        # refresh eye.py events (USGS/EONET/NWS/Open-Meteo)
        try:
            sys.path.insert(0, str(EYE))
            import eye as eye_mod
            fetch_stats["eye_pull"] = eye_mod.pull()
        except Exception as e:
            fetch_stats["eye_pull"] = {"error": str(e)[:160]}

    v3 = load_v3()
    # rebuild events from jsonl so NWS/meteo are present even if v3 embed stale
    events = []
    ev_path = EYE / "data" / "events.jsonl"
    if ev_path.exists():
        for line in ev_path.open():
            e = json.loads(line)
            if e.get("lat") is None:
                continue
            events.append({
                "k": e["kind"], "s": e["source"], "t": (e.get("title") or "")[:90],
                "la": e["lat"], "lo": e["lon"], "tm": e.get("time"),
                "sv": e.get("severity") or 0.3, "cite": e.get("cite") or "",
            })
    else:
        events = v3.get("events") or []

    fires = v3.get("fires") or []
    # refresh FIRMS cells from csv if present
    firms = V3 / "data" / "firms.csv"
    if firms.exists():
        cells = {}
        for r in csv.DictReader(firms.open()):
            try:
                k = (math.floor(float(r["latitude"])) + 0.5, math.floor(float(r["longitude"])) + 0.5)
                cells[k] = cells.get(k, 0) + 1
            except (KeyError, ValueError):
                pass
        if cells:
            fires = [[a, b, c] for (a, b), c in cells.items()]

    kp = v3.get("kp") or []
    kp_path = V3 / "data" / "kp.json"
    if kp_path.exists():
        try:
            j = json.load(kp_path.open())
            if j and isinstance(j[0], list):
                kp = [[r[0], float(r[1])] for r in j[1:]]
            else:
                kp = [[r["time_tag"], float(r["Kp"])] for r in j]
        except Exception:
            pass

    cones = v3.get("cones") or []
    heat = v3.get("heat") or []
    heat_window = v3.get("heat_window") or []
    # rebuild Simons heat if quakes.csv present
    qpath = SIMONS / "data" / "quakes.csv"
    if qpath.exists():
        q = list(csv.DictReader(qpath.open()))
        last = max(r["date"] for r in q)
        cut = (dt.date.fromisoformat(last) - dt.timedelta(days=90)).isoformat()
        grid = [[0] * 36 for _ in range(18)]
        for r in q:
            if r["date"] > cut:
                la = min(int((float(r["lat"]) + 90) // 10), 17)
                lo = min(int((float(r["lon"]) + 180) // 10), 35)
                grid[la][lo] += 1
        heat = [[round(math.log1p(v), 3) for v in row] for row in grid]
        heat_window = [cut, last]

    sats_pts, sats_names = sat_current(v3.get("sats") or [])
    census = {"total": len(sats_pts), "LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
    for p in sats_pts:
        census[["LEO", "MEO", "GEO", "HEO"][p[2]]] += 1

    layer_path = SHIELD / "out" / "eye-shield-layer.json"
    layer = json.load(layer_path.open()) if layer_path.exists() else {"points": []}
    probes, shield_meta = enrich_probes(layer)

    D = {
        "t0": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "events": events,
        "fires": fires,
        "kp": kp,
        "cones": cones,
        "heat": heat,
        "heat_window": heat_window,
        "sats": sats_pts,
        "sat_names": sats_names,
        "sat_census": census,
        "probes": probes,
        "shield": shield_meta,
        "sources": {
            "usgs": "USGS earthquake GeoJSON (public domain)",
            "eonet": "NASA EONET open events (public domain)",
            "nws": "NOAA/NWS severe alerts (public domain)",
            "meteo": "Open-Meteo current weather (CC BY 4.0)",
            "firms": "NASA FIRMS MODIS 24h, 1-degree cell counts",
            "celestrak": "CelesTrak GP active, SGP4 current frame (no aircraft/ship tracks)",
            "kp": "NOAA SWPC planetary K index",
            "heat": "Simons-style 10° grid from USGS M4.5+ (tools/simons)",
            "cones": "tesseract forecast cones (tools/tesseract)",
            "probes": "Eye Shield defensive probes (IP→country centroid; no people/vehicles)",
            "street": "KartaView / OpenStreetCam keyless photos (position, date, image only)",
            "tiles": "Esri World Imagery / USGS National Map / NASA GIBS Blue Marble",
        },
    }
    html = (H / "template5.html").read_text().replace("__DATA__", json.dumps(D, separators=(",", ":")))
    out = H / "eye5.html"
    out.write_text(html)
    st = {
        "build_s": round(time.time() - T, 2),
        "html_bytes": out.stat().st_size,
        "events": len(events),
        "by_source": {s: sum(1 for e in events if e["s"] == s) for s in ("usgs", "eonet", "nws", "meteo")},
        "fire_cells": len(fires),
        "kp_pts": len(kp),
        "cones": len(cones),
        "heat_cells": sum(1 for row in heat for v in row if v),
        "sats": census,
        "probes": len(probes),
        "shield": shield_meta,
        "fetch": fetch_stats,
        "excluded_doc": str(EYE / "EXCLUDED.md"),
    }
    (H / "build_stats.json").write_text(json.dumps(st, indent=1))
    print(json.dumps(st, indent=1))
    return st

if __name__ == "__main__":
    build(live="--offline" not in sys.argv)
