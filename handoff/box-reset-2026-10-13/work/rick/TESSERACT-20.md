# TESSERACT-20 — seeing in 5D (x,y,z space · time · possibility)
Public data only, no person tracking. Built = ✅ (tools/tesseract/, tests in test_tesseract.py).
1. ✅ **5D event store** (lat,lon,alt,t,scenario) — `python3 tools/tesseract/tesseract.py build` — test: observed>400 rows, 7 p50 cone rows.
2. ✅ **One query, all stores** (world+bus+forecast FTS, palace, graph) — `tesseract.py query earthquake` — test: hits from store+palace, <2s.
3. ✅ **Forecast cones (5th axis)** p10/p50/p90 next 7 days, width ∝ √horizon — `cones()` — test: p10≤p50≤p90; backtest coverage.
4. ✅ **Anomaly alerts** robust z (median/MAD, 30-day window) — `anomalies(xs)` — test: injected spike detected; precision on fixtures.
5. ✅ **Whole-picture brief <2k tokens** — `tesseract.py brief` — test: toks<2000.
6. ✅(view) **Hypercube view**: 8 cells = 8 layers, rotating 4D projection — open `tesseract.html` — test: headless shot.png renders.
7. ✅ **Continuous Shepherd scheduler** — `feeds on intervals (quake 5m, eonet 30m, kp 15m)` — test: 3 ticks → 3 appends, no dup ids.
8. ✅ **Time slider & replay** — `replay(t0,t1,step)` over store — test: frame counts sum to window row count.
9. ✅ **Salience score** = severity × novelty × proximity-to-active-work — test: M6.7 ranks above M2.0.
10. ✅ **World↔memory cross-links** (event terms → palace/graph ids) — test: ≥1 link for "satellite".
11. ✅ **Delta brief** (only what changed since last brief) — test: unchanged store → empty delta.
12. ✅ **Scenario branching** (counterfactual "what if feed X down") — test: branch rows tagged scenario=cf:*.
13. ✅ **Cone calibration loop** (auto-widen until 80% coverage) — test: coverage → 0.8±0.03.
14. ✅ **Geo tiles / H3-like 10° grid index** — test: cell counts sum to geo rows.
15. ✅ **Mesh-flow layer** (bus claims/gates as time-series) — test: gate verdicts counted per lane.
16. ✅ **Retention compactor** (old raw → daily aggregates, keep cites) — test: size shrinks, totals preserved.
17. ✅ **Source health monitor** (feed latency/staleness alerts) — test: stale fixture → alert.
18. ✅ **Attention budget** (brief sized to token budget N) — test: brief(N=500) ≤ 500 toks.
19. ✅ **Mesh City 5D overlay** (meshcity buildings glow with live salience) — test: city.json gains salience field.
20. ✅ **Honest-claims gate** (every brief line carries a cite or measured number) — test: lint finds 0 uncited lines.
