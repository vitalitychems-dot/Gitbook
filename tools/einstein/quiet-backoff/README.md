# Quiet gate timer (Gitbook #72 idea 5), rev 2

**Change after Moderator FAIL @6e9b0e49:** the default no longer backs off. Each 5-min tick does a conditional GET with `If-None-Match`. A 304 is free (it doesn't count against the GitHub rate limit) and means IDLE; a 200 with a new ETag means RUN the full gate check. Backoff is now opt-in (`QB_CAP>5`) and is not recommended, because every backoff setting regressed latency (table).

**Reproduce from this PR:** `python3 replay.py` (real data in `data/`):
- `pushes.txt.zst`: 601 TESSERA commit times, 2026-10-06 → 10-13 (7 d 8 h);
- `ci_runs.tsv.zst`: snapshot of 700 TESSERA CI runs (time, conclusion, event).

Latency is mean push-detect latency, bootstrap 95% CI over pushes, 5 seeded runs (all 5 within ±0.01 of this one).

| Policy | Cron wakes/day | Full (rate-limited) checks/day | Mean latency [95% CI] | Max |
|---|---|---|---|---|
| fixed 5 min (baseline) | 288.1 | 288.1 | 2.51 [2.40, 2.63] min | 5.0 |
| **ETag 5 min (new default)** | 288.1 | **31.8 (−89%)** | **2.51 [2.40, 2.63]** (identical) | 5.0 |
| backoff cap 30 (rev 1) | 78.2 | 78.2 | 5.86 [5.40, 6.34] | 28.4 |
| backoff cap 10 | 158.0 | 158.0 | 3.35 [3.17, 3.54] | 9.8 |
| backoff after 1 h quiet | 118.8 | 118.8 | 4.77 [4.30, 5.26] | 29.1 |
| backoff after 4 h quiet | 177.7 | 177.7 | 4.14 [3.74, 4.57] | 28.0 |

**Limits:**
- Cron wakes (Actions minutes) are not reduced; only full checks and API quota are.
- Every wake-reducing setting gives a latency CI that doesn't overlap the baseline's.
- This is a simulation on real timestamps, and assumes 304s are free per GitHub's conditional-request docs.
- It is not wired into any workflow; that would touch locked paths.
- It is related to #295 (that PR caches PR-list ETags; this one gates the cron's full check on the head ref).

Tests: `python3 -m unittest test_quiet_backoff` (8 tests, including a replay-reproduction test).
