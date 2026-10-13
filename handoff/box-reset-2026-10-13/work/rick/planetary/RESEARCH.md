# Planetary View research (2026-10-13, read-only)

## Candidates
| Project | Stars / License | What it does | Class |
|---|---|---|---|
| github.com/bilawalsidhu/gods-eye-view | ~54.2k (API). Code is MIT; data keeps its own terms. TeleGeography cables are CC BY-NC-SA. | 3D Cesium globe showing live ADS-B aircraft, AIS ships, satellites (CelesTrak), USGS quakes, NASA FIRMS fires, weather, traffic and public CCTV. Has an MCP server with about 40 tools. Very likely what Father means. | Mostly global awareness from public data. The CCTV/ALPR camera layers and the "military awareness" layer reach toward watching places and vehicles, so leave them out. |
| github.com/uhrichsam4/gods-eye-view | 471, fork | Same app plus about 5,200 public cameras | Camera-heavy, so leave out |
| github.com/VrushankPatel/godseye | 97, Apache-2.0 | Frontend-only geospatial OSINT globe with aircraft, satellites, CCTV and traffic | Like GEV |
| github.com/paveldat/Gods-eye | 50, no license | Python recon/OSINT toolkit ("The God's EYE in Python") | Network and target recon, so don't use it |
| github.com/guoyaohua/GodsEYE | 28, no license | Location monitoring plus messaging (Chinese) | Tracks individuals, so don't use it |
| "Eye of God" (Glaz Boga) Telegram bot | not on GitHub | Russian service for looking up personal data on people | Person-level surveillance, so don't use it |
| github.com/Iankulani/red-sparrow | 5, no license | "Cross-platform command-and-control (C2) framework", i.e. offensive malware infrastructure | Don't use it (security risk; breaks the harm line) |
| Others named Red Sparrow (Teleinformatyka/RedSparrow plagiarism checker, Kirk-Wang front-end notes, RedSparrowEU AI forks, hongque-pro Kotlin libs) | 0-2 | Unrelated | n/a |
"Red Sparrow" is otherwise a 2018 spy film and novel (Jason Matthews). No public planetary or OSINT tool by that name was found.

Father's repos (vitalitychems-dot, collink1007): no repo names or descriptions mention eye, sparrow, planet or globe. Code search needs auth, so a full mention check wasn't possible without a token.

## Safe Planetary View design (public, aggregate data only)
Layers: USGS quakes (GeoJSON, public domain), NOAA/NWS alerts (api.weather.gov), NASA FIRMS fires and NASA GIBS/EONET imagery and events, ESA Copernicus Sentinel (CDSE), GDELT 2.0 event and tone data (aggregated by country/region), OpenStreetMap (ODbL), ADS-B aircraft as aggregate counts and density per region (adsb.lol / OpenSky), CelesTrak satellites.
Excluded: CCTV/ALPR, face recognition, people search, phone or social tracking, following individual aircraft or vessels, and any C2 or recon tooling.
Architecture: one Python fetcher per layer -> normalized JSON {layer, source, license, fetched_at, items} -> a local cache under /workspace/rick/planetary/cache (size-capped) -> a daily "world brief" for Tessera plus an optional Mesh City / Cesium view. Option: run a fork of gods-eye-view with the camera, ALPR and military layers disabled, once the gates pass.

## Step 1 (built and run)
- quakes.py: input is the USGS all_day feed; output is JSON {count, max_mag, top5}.
- test_quakes.py: offline fixture test. PASS.
- Live run 2026-10-13 ~2:2x AM CT: 245 quakes, max M6.7 central Mid-Atlantic Ridge; M6.1 near Río Grande, Panama.

## Top 8 similar open projects (GitHub API stars, checked 2026-10-13 ~2:25 AM CT)
| # | URL | Stars | License | What it does | Person-tracking risk |
|---|---|---|---|---|---|
| 1 | github.com/koala73/worldmonitor | 88,340 | AGPL-3.0 | Real-time global dashboard: news aggregation, geopolitical events, map layers | no (aggregate news/events); copy ideas only, AGPL |
| 2 | github.com/CesiumGS/cesium | 15,826 | Apache-2.0 | 3D globe JS library (GEV is built on it) | no |
| 3 | github.com/open-meteo/open-meteo | 6,332 | AGPL-3.0 | Free weather forecast API (we call the public API) | no |
| 4 | github.com/wiedehopf/tar1090 | 1,929 | NOASSERTION (GPL-derived) | ADS-B map web UI | yes-ish (single aircraft); use only aggregate counts |
| 5 | github.com/nasa-gibs/worldview | 1,917 | NOASSERTION (NASA OSA) | Browse global satellite imagery + EONET events | no |
| 6 | github.com/sentinel-hub/sentinelhub-py | 909 | MIT | Download/process Sentinel imagery | no (10 m resolution) |
| 7 | github.com/stac-utils/pystac | 467 | Apache-2.0 (NOASSERTION in API) | SpatioTemporal Asset Catalog library | no |
| 8 | github.com/microsoft/PlanetaryComputer | 208 | MIT | Planetary-scale EO catalog (STAC API) | no |
Ideas taken into Tessera's Eye: layered feeds (1,5), globe view (2, done offline in canvas), STAC-like normalized records with source+license citations (7,8), aggregate-only rule for traffic (4).
