# Tessera's Eye v5 — unified safe live layers (2026-10-13 ~3:50 AM CT)

One flat deep-zoom map with every **safe** live layer Father approved for now. Exclusions stay in `../EXCLUDED.md` for later decisions. No pushes. No CCTV/ALPR/faces/per-vehicle/aircraft/ship tracks/malware/Camoufox/Argos cameras.

## Build
`python3 v5/build5.py` (live) → `eye5.html` **955,262 bytes** in **3.48 s**.
`python3 v5/test_v5.py` → **15/15 pass**. Screenshot: `v5/shot5.png` (1,588,138 bytes).

## Layers embedded (measured)
| Layer | Count | Source |
|---|---|---|
| Events (USGS+EONET+NWS+Open-Meteo) | 452–483 | eye.py + jsonl |
| FIRMS fire cells (1°) | 1,495 | NASA FIRMS MODIS 24h |
| Simons heatmap | 18×36 (162 active) | tools/simons, 90-day M4.5+ |
| Forecast cones | 21 | tools/tesseract |
| Kp points | 58 | NOAA SWPC |
| CelesTrak sats (current frame) | 16,693 (LEO 15,880 / MEO 183 / GEO 585 / HEO 45) | v3 SGP4 |
| Eye Shield probes | 24 | eye-shield-layer.json (country centroid / unlocated placeholder; defensive only) |

## Interaction (Chrome CDP, real mouse/wheel)
- Drag moves map by exactly the pointer delta (300, 200 px).
- Wheel zooms z4→z19 in 15 events; cursor point fixed to 1e-4°.
- Click marker expands details; **Zoom to click** raises zoom by ~4 levels.
- Empty click reports coordinates; probe click shows Eye Shield defensive text ("No people").
- Refresh interval **300,000 ms** (5 min).

## Imagery (Chicago Millennium Park 41.8827°N, −87.6233°)
| Base | Zoom | Tiles | Median | p95 | Full screen |
|---|---|---|---|---|---|
| Esri World Imagery | z19 (0.22 m/px) | 24 | 358 ms | 522 ms | 0.61 s |
| USGS National Map | z16 | 24 | 105 ms | 108 ms | 0.20 s |
| NASA GIBS Blue Marble | z8 | 24 | 203 ms | 218 ms | 0.41 s |

## Live refresh (online)
First pull: **452** events in **1,262 ms** — USGS 233, EONET 200, NWS 11, Open-Meteo 8, Kp 58.

## KartaView
6 photos within 300 m of click in 21.9 s (fields: la, lo, dt, th, img only).

## Excluded (not in page code)
CCTV, ALPR, face recognition, per-vehicle/aircraft/ship tracks, Red Sparrow, Camoufox, Argos cameras — documented in `../EXCLUDED.md`. Page scan for those terms: clean. No remote `<script src>`.

## Commands
```
python3 v5/build5.py            # live feeds
python3 v5/build5.py --offline  # cache only
python3 v5/test_v5.py           # 15 checks + shot5.png
python3 v5/test_v5.py --offline # skip network tile/refresh/street
```
