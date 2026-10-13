# Quiet-backoff gate timer (Gitbook #72 idea 5)
Cron ticks every 5 min. `quiet_backoff.py due STATE` exits 1 (no API call, ~0 s) until the backoff interval passes. After fetching the head, `seen STATE SHA` prints RUN on a new SHA (interval resets to 5) or IDLE (interval doubles, capped at 30). Worst-case push-detect latency ≤ 30 min. 5 unit tests. Not wired into any workflow (that would touch locked paths).

Measured: replay of real TESSERA commit times, 2026-10-06 → 10-13 (601 commits), deterministic, identical over 5 runs:

| Metric | Fixed 5-min | Quiet-backoff 5→30 |
|---|---|---|
| Head checks/day | 288.1 | 78.2 (−73%) |
| Detect latency, mean (bootstrap 95% CI) | 2.51 [2.40, 2.63] min | 5.86 [5.39, 6.34] min |
| Detect latency, max | — | 28.4 min (< 30 target) |

Trade: +3.4 min mean latency for −73% checks. Complements #295 (that one skips per-PR rechecks; this one spaces the polls).
