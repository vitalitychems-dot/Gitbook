# Tesseract results (2026-10-13 ~02:30 CT) — reproduce: `python3 tesseract.py build && python3 measure.py`
Store: 474 observed rows (463 world events + 11 bus msgs) + 21 forecast-cone rows. 5/5 tests pass (no pytest; run via python import).
- **Query latency** (10 queries ×3, all stores): median total 2.26 ms, max 27.6 ms (palace dominates: median 1.81 ms; store 0.30; graph 0.05).
- **Brief**: 560 tokens vs 98,014 tokens of raw sources (≈175× smaller). Tokens = chars/4 estimate.
- **Anomaly precision on fixtures**: real 364-day quake series + 10 labeled injected spikes/dips ×20 trials (seed 7): precision 0.969, recall 0.475 (misses mild spikes; threshold z>3.5 favors precision). Real series has 10 anomalous days (unlabeled).
- **Cone coverage** (p10–p90 next-day backtest, 304 days): 0.734 vs 0.80 target → under-wide; invention 13 fixes.
- **View**: tesseract.html (offline, rotating 4D hypercube, 8 layer cells); shot.png captured headless.
Limits: OR-match FTS ranks bus messages high for common words; forecasts are counts only, no claim of influence.

## Round 2 — inventions 7-20 (2026-10-13 ~02:30 CT) — `python3 -c "import test_tess2"` style runner; 15/15 + 5/5 tests pass; results2.json
- 13 Cone calibration: width k=1.30 fit on first half (train cov 0.803); held-out 152 days cov 0.855 (vs 0.783 at k=1). Overshoots 80% by 5.5 pts — honest holdout, not tuned on it.
- Rank fix (coordination + IDF + agent-name downweight in bus headers): top-1 layer accuracy 0.6→0.8 on 10 labeled queries, 0.52 ms/query. 2 misses are bus summaries that genuinely contain the words.
- 20 Honest-claims lint: brief 25 bullets, 0 uncited; negative fixture 2/2 caught.
- 17 Feed health: 4 sources; usgs 10 min, meteo 13 min (fresh); eonet 448 min, nws 235 min flagged stale (note: age is from newest event time, not fetch time).
- 11 Delta brief: first run 474 new (167 tok for 15 shown lines), second run 0 new.
- 9 Salience: 463 scored; top = NWS Mobile AL flood warning (0.241).
- 10 Cross-links: 5/5 world kinds linked to palace docs, 1/5 to graph nodes.
- 7 Scheduler: run_feeds.sh (flock + per-feed interval stamps, FIXDIR offline mode); NOT installed in cron. Test: store due → ran; immediate rerun → gated (no new log line).
- 14 Geo grid 10°: 41 cells; busiest 30N,-120 (73 events); sums equal geo rows.
- 16 Compactor: 159,670 → 1,207 bytes (132×), 73 day×kind groups, totals preserved (463).
- 18 Budget brief: budgets 150/300/600 → 142/296/560 tokens.
- 8 Time slider: tesseract.html slider over 197 hourly frames / 463 events; in shot.png.
- 12 What-if: cf:drop-usgs 218/463 rows; cf:scale-earthquake×2 raises quake severity (run on a temp copy of t5d.db).
- 15 Mesh-flow: rick claim 1/note 7, moderator gate 1 (PASS 1), security block 1, tessera ask 1 (sample bus).
- 19 Mesh City overlay: city5d.json (meshcity/ untouched), 29 buildings, 3 lit, world_glow 0.714.
