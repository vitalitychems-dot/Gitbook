# Tessera's Eye: data plan v2 (2026-10-13, Rick)
Rule: public open data only; aggregates, not individuals; each source cited; disk budget is under 80MB new for this phase. Sizes are estimates unless marked "measured".

| Area | Source | URL | License | Size | Fetch under our disk? |
|---|---|---|---|---|---|
| Satellites | CelesTrak GP "active" (CSV) | https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv | Public; credit CelesTrak | 2.5MB measured; we store only counts | YES (live in feeds2.py) |
| Space weather | NOAA SWPC planetary Kp | https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json | Public domain | 4.5KB measured | YES (live in feeds2.py) |
| Quake history | USGS FDSN event query, M4.5+, 1 yr | https://earthquake.usgs.gov/fdsnws/event/1/query | Public domain | 1.4MB CSV measured; stored ~10KB daily counts | YES (predict.py) |
| Earth imagery | NASA GIBS WMTS tiles | https://gibs.earthdata.nasa.gov | NASA open, no auth | ~50KB/tile | YES, a few tiles on demand |
| Imagery catalog | Earth Search STAC (Sentinel-2/Landsat) | https://earth-search.aws.element84.com/v1 | CC0 metadata; scenes are Copernicus/USGS open | KB per query | YES, metadata only |
| Imagery catalog | MS Planetary Computer STAC | https://planetarycomputer.microsoft.com/api/stac/v1 | Per-collection open; SAS token for assets | KB per query | YES, metadata only |
| Emotion/EQ | GoEmotions (58k Reddit comments, 27 emotions) | https://github.com/google-research/google-research/tree/master/goemotions | CC BY 4.0 | ~4MB TSV | YES |
| Emotion/EQ | EmpatheticDialogues | https://github.com/facebookresearch/EmpatheticDialogues | CC BY-NC 4.0 (non-commercial) | ~28MB tar | YES, research only |
| Physiology | WESAD (wearable stress/affect) | https://archive.ics.uci.edu/dataset/465 | CC BY 4.0 | ~2.1GB | NO (too big) |
| Physiology | PhysioNet open sets (e.g. MIT-BIH arrhythmia) | https://physionet.org/content/mitdb/ | ODC-By | ~73MB | MARGINAL; skip this phase |
| Neuroscience | OpenNeuro BIDS sets | https://openneuro.org | CC0 | GBs per set | NO; metadata only |
| Neuroscience | Allen Brain Atlas API | https://api.brain-map.org | Allen terms (non-commercial research) | KB per query | YES, small queries |
| Topic knowledge | Simple English Wikipedia abstracts | https://dumps.wikimedia.org/simplewiki/ | CC BY-SA 4.0 | ~300MB+ | NO this phase |
| Topic knowledge | Project Gutenberg single classics | https://www.gutenberg.org | Public domain (US) | ~0.5-2MB/book | YES, a few books |
| World events | GDELT 2.0 15-min events | http://data.gdeltproject.org/gdeltv2/lastupdate.txt | Free, citation required | ~0.3-1MB zip/15 min | YES, possible next feed; counts by country only (it names actors, so drop actor fields) |

No dataset was downloaded this phase. GoEmotions (4MB, CC BY 4.0) is the best next one if the empathy model needs it.
Excluded: ADS-B or AIS per-aircraft or per-ship tracks, cameras, social profiles, and anything that identifies a person.
