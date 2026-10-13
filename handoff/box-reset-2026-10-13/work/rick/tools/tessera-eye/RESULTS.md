# Tessera's Eye v1 results (2026-10-13 ~2:23 AM CT)
Live pull: 463 events (USGS 245, EONET 200, NWS 10 with geometry, Open-Meteo 8).
Latency: USGS 97 ms, EONET 133 ms, NWS 266 ms, Open-Meteo 589 ms; whole pull 1.2 s wall.
Index: 159,670 bytes (events.jsonl); chunks 96,842 B; bus 4 msgs, all valid under collab/bus.py.
Tool dir total: 468K (limit 100MB). Tests: 6/6 pass, offline, 0.01 s.
Map: eye.html with 463 events, no external scripts.

# v2 (2026-10-13 ~2:30 AM CT)
New Shepherd feeds (feeds2.py, aggregate-only). Live pull:
- CelesTrak active satellites: 16,693 total = LEO 15,881 / GEO 584 / MEO 183 / HEO 45. 2.53MB fetched in 1.59 s; only counts stored (no names or IDs).
- NOAA SWPC Kp (last ~7 days): latest Kp 3.33, max 7.0, 3 three-hour periods at Kp>=5 (storm level). 4.5KB, 75 ms.
- Both posted to the bus (2 msgs, valid under collab/bus.py).
Forecast harness (predict.py): next-day global M4.5+ quake count band. Data: USGS, 364 days (2025-10-13 to 2026-10-11). Train on the first 273 days (tercile cuts 17/21) and walk forward over the held-out 91 days.
Hit rate: persistence 0.505, 7-day mean 0.473, random 0.451, climatology majority 0.308. Chance is about 0.33.
Count MAE: 7-day mean 7.14 vs climatology 7.59.
Honest read: persistence beats chance by about 17 points, because quake clusters and aftershocks carry over day to day. The random baseline scored 0.45 by luck on n=91, so the margin over it is small and not significant. The held-out period was busier than training (49% of days high-band), so climatology failed. This forecasts counts only. It cannot influence any event.
Tests: test_v2 5/5 plus test_eye 6/6 = 11/11 pass offline in 0.014 s.

# v3 interactive globe (2026-10-13 ~2:40 AM CT), in v3/
Build (`python3 v3/build.py`, live; `--offline` reuses cache): 3.3 s total, of which SGP4 took 0.91 s for 16,693/16,693 CelesTrak satellites x 13 frames (-12h..+12h, 2h steps). Classes: LEO 15,880 / MEO 183 / GEO 585 / HEO 45.
Layers in eye3.html: 16,693 satellites (name, NORAD, class, orbit ring on click), 463 events (USGS/EONET/NWS/Open-Meteo), 1,452 FIRMS 1° fire cells, 58 Kp points, 21 cone values (7 days x p10/p50/p90), Simons 18x36 heat grid (90 days to the last quake date), 50 Harvard Dataverse entries (search list only).
Imagery: NASA GIBS MODIS Terra true color 2048x1024 base (587 KB) embedded for offline use. Online checkbox loads GIBS for the slider date.
Interaction: drag to rotate, wheel or pinch to zoom, right-drag (or shift-drag, or the slider) to tilt 0-70°, click to pick with occlusion test, click the ground for lat/lon plus the heat-cell count, time slider and play button replaying all layers.
Single self-contained file eye3.html is 7.04 MB. Its CSP is connect-src 'none' and it loads no remote scripts. Total v3 dir about 13 MB (vendor sgp4 0.7 MB, data 4 MB).
Render: median draw 80.5 ms for 18,608 points under headless SwiftShader (software GL, first frames). This is not a GPU number.
Tests: v3/test_v3.py 5/5 pass (Vallado 00005 SGP4 within 10 km, fixture OMM positions sane, layer parsing, no remote loads, no person-tracking keys). v1 6/6 and v2 still pass.
Screenshot: v3/shot3.png (exists, 1400x850).
Kept vs v2 (measured): satellites went from counts only to 16,693 clickable positions. The globe went from a canvas spin to WebGL with zoom, tilt and pick. Added fire, heat and cone layers on the time axis. Nothing was dropped.
Not done: CesiumJS was not vendored (a hand-written WebGL globe was used instead, and Cesium's size was not measured). Orbit rings are a two-body approximation, while the dots are SGP4. Satellite dots snap to 2 h frames during replay.

# v4 deep-zoom map (2026-10-13 ~2:53 AM CT), in v4/
`python3 v4/build4.py` builds eye4.html (134 KB; v3 events + fires embedded). `python3 v4/test_v4.py` drives headless Chrome over CDP with real mouse/wheel input events (`--offline` skips network checks). **12/12 pass.**
- Imagery (tile pyramid, streams per zoom level; off-screen downloads cancelled):
  - Esri World Imagery: real detail to **z19 = 0.22 m/px at Chicago (41.9°N), 0.30 m/px at the equator**. Esri returns a "no data" placeholder at z20+ over Chicago, so z20-21 are overzoomed (scaled, no new detail). Viewport at z19: 24 tiles, median 316 ms, p95 538 ms, full screen in 0.61 s.
  - USGS National Map orthoimagery (USGSImageryOnly): cached to z16 (~1.8 m/px here); z17+ returns 404. z16: 24 tiles, median 104 ms, p95 107 ms, 0.21 s.
  - NASA GIBS Blue Marble (3857): z8. 24 tiles, median 211 ms, 0.41 s.
- Measured improvement kept: cancelling off-screen tile downloads during zoom cut a z4->z19 wheel zoom from 344 to 24 requests. Esri median tile time dropped from 3,756 ms to 316-384 ms.
- Input tests: drag moves the map exactly by the pointer delta (300,200 px). 15 wheel events zoom z4->z19 and keep the cursor point fixed to within 1e-4°. Wheel-out works. Clicking a marker opens its details (USGS quake title). Clicking empty ground returns coordinates.
- Live refresh: every 5 min (300,000 ms) in online mode. First pull got 439 USGS+EONET events in 242 ms.
- Street level: KartaView works keyless (api.openstreetcam.org 2.0, CORS *). It returned 6 photos within 300 m of the click in 1.6 s (a curl run once took 18 s). Only position, date and image URLs are kept; no uploader fields. Mapillary needs an access token (the keyless call returns HTTP 500/auth), so it is listed as needing a key and skipped.
- Screenshot: v4/shot4.png (Millennium Park, Chicago, z19 Esri). v4 dir total 2.5 MB (websocket-client vendored 1 MB).
- Limits: no plate reading, no face recognition, no CCTV, no tracking of people, vehicles, aircraft or ships. A test scans the page code for those terms.

# v5 unified safe layers (2026-10-13 ~3:50 AM CT), in v5/
`python3 v5/build5.py` → eye5.html 955 KB in 3.48 s. `python3 v5/test_v5.py` → **15/15 pass**.
Layers: 452–483 events (USGS/EONET/NWS/Open-Meteo), 1,495 FIRMS cells, Simons 18×36 heat, 21 cones, 58 Kp, 16,693 CelesTrak current positions, 24 Eye Shield probes (country/placeholder; no people/vehicles), KartaView, Esri/USGS/GIBS tiles, 5-min live refresh.
Click-to-zoom expand works; Esri z19 full screen 0.61 s (median tile 358 ms); live refresh 452 events in 1.26 s; KartaView 6 photos.
Excluded items (CCTV/ALPR/faces/vehicle-aircraft-ship tracks/Red Sparrow/Camoufox/Argos cameras) documented in EXCLUDED.md — not wired. Screenshot: v5/shot5.png.
