# REA-11: gods-eye-view + 10 similar open projects (2026-10-13 ~2:40 AM CT)
Stars and licenses come from the GitHub API, today. "Borrow" means what Tessera's Eye v3 takes: ideas or keyless public feeds only. No code was copied from AGPL or GPL projects.

| # | Project | License | What it does | Data sources | Safe layers borrowed | Excluded |
|---|---|---|---|---|---|---|
| 0 | bilawalsidhu/gods-eye-view | MIT code (data keeps its own terms) | Cesium globe of live world feeds plus an MCP server | CelesTrak, USGS, NASA FIRMS, weather, ADS-B, AIS, CCTV, traffic | satellites, quakes, fires, weather (all in v3) | CCTV, ALPR, traffic cams, military layer, per-aircraft (ADS-B) and per-ship (AIS) tracks |
| 1 | koala73/worldmonitor | AGPL-3.0 | Global news and events dashboard | news and RSS feeds, event APIs | idea: layered feed panel with citations | code (AGPL), person or news-subject profiles |
| 2 | CesiumGS/cesium | Apache-2.0 | 3D globe engine | n/a | interaction model (drag, zoom, tilt, pick) | not vendored: v3 uses a hand-written WebGL globe (dir 13MB). Cesium's built size was not measured. |
| 3 | open-meteo/open-meteo | AGPL-3.0 | Weather API | NOAA/DWD/ECMWF models | public API, keyless (in v3 via eye.py) | self-hosting code |
| 4 | wiedehopf/tar1090 | GPL-derived | ADS-B map | ADS-B receivers | none in v3 (aggregate counts only if added later) | all per-aircraft tracks |
| 5 | nasa-gibs/worldview | NASA OSA | Satellite-imagery browser | NASA GIBS, EONET | GIBS MODIS true-color WMS (offline cache + online by date), EONET | none |
| 6 | sentinel-hub/sentinelhub-py | MIT | Sentinel imagery client | Copernicus | none (needs an account or OAuth key) | left out: key required |
| 7 | stac-utils/pystac | Apache-2.0 | STAC catalog library | any STAC | idea: normalized records with source and license | none |
| 8 | microsoft/PlanetaryComputer | MIT | EO STAC catalog | Landsat, Sentinel, etc. | idea only (some collections need a token) | keyed collections |
| 9 | Flowm/satvis (new) | MIT | Cesium satellite tracker and pass predictor | CelesTrak GP | click a satellite to get name, NORAD id, orbit class and orbit ring; SGP4 propagation | observer-location pass alerts (not needed) |
| 10 | cambecc/earth (new) | MIT | Animated global wind and weather globe | NOAA GFS, OSCAR | idea: time-scrubbed global field overlay (used for the Simons heat texture and time slider) | none |
Also reviewed: thkruz/keeptrack.space (AGPL-3.0, satellite astrodynamics UI), used for ideas only. openskynetwork/opensky-api (GPL-3.0) was not used because it exposes individual aircraft states.

## Red Sparrow
Excluded. github.com/Iankulani/red-sparrow is a command-and-control (C2) malware framework. The legal substitute for its "see more" role is the keyless public-feed set below, plus satvis-style satellite inspection. Nothing offensive and no recon.

## Feeds: keyless and no signup (used in v3)
USGS GeoJSON, NASA EONET, NWS api.weather.gov, Open-Meteo, CelesTrak GP CSV, NASA GIBS WMS, NOAA SWPC Kp, NASA FIRMS MODIS Global 24h CSV (the open public file, aggregated to 1° counts), Harvard Dataverse search API (dataset titles and links only; authors and contacts removed).
## Needs a key or account (left out)
FIRMS area API (MAP_KEY), Copernicus Data Space / Sentinel Hub (OAuth), OpenSky authenticated API, NASA Earthdata login (Earthdata downloads), Cesium ion (token), Windy API (key), Planetary Computer signed collections (token).
