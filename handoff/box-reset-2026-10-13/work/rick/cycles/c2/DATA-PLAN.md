# DATA-PLAN (cycle 2): open public sources for prediction and learning
Sizes are approximate; verify the license on each source page before use. Rule: fetch only slices under 50MB, keep citations, no personal data. Forecasts report skill only: **no causal claims and no claims of "swaying" events.**

| Domain | Source | What | License | Typical size | <50MB fetch? |
|---|---|---|---|---|---|
| Satellites | CelesTrak GP/TLE (celestrak.org) | Orbital elements for active satellites | Free public use (attribution to CelesTrak) | ~2–5MB for the active set | Yes |
| Satellites | NASA GIBS (WMTS tiles) | Daily global imagery tiles | NASA open data (no copyright, credit NASA) | KB per tile | Yes (single tiles) |
| Satellites | NASA CMR-STAC / Earth Search STAC (Sentinel-2 / Landsat COGs) | Searchable scene metadata + COGs | Metadata open; Sentinel CC BY-SA 3.0 IGO / Copernicus terms; Landsat public domain | STAC JSON KB; scenes 100MB+ | Metadata yes; scenes no (windowed COG reads only) |
| Human studies | GoEmotions | Emotion-labelled text | Apache-2.0 | 4.4MB | Yes (in use) |
| Human studies | EmpatheticDialogues | Empathetic dialogue | CC BY-NC 4.0 | ~28MB | Yes (non-commercial only) |
| Human studies | OpenPsychometrics raw data | Personality/psych questionnaires | Per-dataset terms; mostly free for research | 1–50MB | Mostly |
| Human studies | PhysioNet open (Fantasia, MIT-BIH) | ECG/HRV | ODC-By / Open Data Commons, per set | records ~1–20MB | Single records |
| Human studies | OpenNeuro (BIDS) | EEG/fMRI | Mostly CC0 | GBs | Metadata/participants.tsv only |
| Human studies | Allen Brain Map API | Cell types, ephys | Allen terms of use (research) | API slices KB–MB | Yes (slices) |
| Topic knowledge | Wikipedia (dumps.wikimedia.org, REST page summaries) | Article abstracts | CC BY-SA 4.0 | Full abstract dump ~1GB+; summary API per page KB | Per-page summaries yes; full dump no |
| Topic knowledge | arXiv OAI-PMH / API metadata | Titles + abstracts | Metadata CC0; abstracts per-paper licence | ~KB per paper | Yes (a few thousand records) |
| World events | USGS earthquake GeoJSON/CSV feeds | Quakes (hour → month) | Public domain | 0.3–5MB | Yes (in use) |
| World events | NASA EONET v3 | Natural events (fires, storms, volcanoes) | NASA open | <1MB | Yes |
| World events | GDELT 2.0 events/GKG (15-minute files) | News-coded events | Free/open with citation (GDELT terms) | ~1–10MB zipped per 15 min; full archive TB | Yes (single 15-min files) |
| Weather | Open-Meteo (forecast + archive API) | Temperature, precipitation, wind | CC BY 4.0 | KB per city-year | Yes |
| Weather | NOAA GHCN-Daily per-station CSV | Daily station extremes | Public domain | ~0.1–5MB per station | Yes |

## Prediction harness (design + prototype: forecast.py)
- Targets: (a) next-day global M2.5+ quake **count** (USGS); (b) next-day weather extreme per city (Tmax above the 90th percentile, from Eye's Open-Meteo history, once the Eye has enough days).
- Protocol: rolling-origin backtest (each day predicted only from earlier days); baselines are persistence, 7-day mean and median, EWMA, and climatology. Metrics: MAE, hit-rate (|err| ≤20%), busy-day accuracy, skill vs persistence. A model is only promoted if it beats persistence on ≥60 held-out days.
- Wording rule: report "forecast skill" and "correlation". Never "caused", "influenced" or "swayed". The Eye observes; it does not act on the world.
- Data source: the Eye's `tools/tessera-eye/data/quake_daily.json` once it holds ≥90 days. Until then, the USGS 30-day feed.
