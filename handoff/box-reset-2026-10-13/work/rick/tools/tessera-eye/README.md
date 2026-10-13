# Tessera's Eye v1
Read-only Shepherd fetchers for public open data -> normalized cited events -> JSONL index -> mesh bus notes -> offline globe.
- `python3 eye.py pull`: fetch USGS quakes, NASA EONET, NOAA/NWS severe alerts, Open-Meteo (8 cities); appends to data/events.jsonl (dedup by id, 20MB cap), data/bus.jsonl (collab/bus.py format, kind=note, rick->tessera), data/chunks.jsonl (palace-ready text + citation).
- `python3 eye.py map`: writes eye.html (single file, no CDN; drag to spin, click a dot for details + citation link).
- `python3 eye.py stats`; tests: `python3 -m unittest test_eye` (fixtures, network disabled).
Limits: public open data only; no aircraft/ship IDs, no people, cameras, faces or phones. NWS zone-only alerts (no geometry) are skipped in v1.
Licenses: USGS/NASA/NOAA public domain; Open-Meteo CC BY 4.0 (attribution kept per event).
