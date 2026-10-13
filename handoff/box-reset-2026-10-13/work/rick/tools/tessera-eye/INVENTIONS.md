# Tessera's Eye inventions (v3, measured only)
1. One-file offline globe: imagery and all layers in 7.04 MB, CSP blocks every network call except opt-in GIBS imagery. Tested.
2. Batch SGP4 "time cube": 16,693 satellites x 13 frames in 0.91 s, replayable on the slider. Reference error within 10 km tested.
3. Occlusion-aware click picking across satellites, events and fires, plus ground clicks that read the Simons heat cell.
4. Heat-as-texture: the Simons 10° grid is blended into the globe shader (one draw, no extra geometry).
5. Privacy gate test: a recursive key scan rejects person, camera, ALPR, aircraft and ship identifiers in shipped data.
6. Keyless-feed policy: every v3 source is keyless. Keyed sources are listed and left out (REA-11.md).

# v4 (measured only)
7. Streaming tile pyramid with three keyless sources (Esri z19 / USGS z16 / GIBS z8) and per-source max zoom plus overzoom to z21. Tile load times are measured in-page (T4.loads).
8. Off-screen tile cancellation: 344 -> 24 requests per deep zoom, median Esri tile 3.7 s -> 0.3 s.
9. Cursor-anchored wheel zoom: the cursor point stays fixed to within 1e-4° from z4 to z19 (tested with real input events).
10. 5-minute live feed refresh (USGS + EONET). 439 events in 242 ms.
11. Click-to-street: a ground click fetches keyless KartaView photos (privacy-blurred by the provider), with a field whitelist so no uploader identity is kept.
12. CDP input-event test harness (no Playwright; only websocket-client vendored).
