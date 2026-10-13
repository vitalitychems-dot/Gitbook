# scoreboard-proposal (read-only, not pushed)

Sources: GitHub connector, read-only, on 2026-10-13: `pull_request_read get` (merged, merged_at) and `get_check_runs` (head commit) for every PR referenced in mesh/scoreboard/metrics.jsonl and agents.jsonl: TESSERA #251 #256 #260-#265 and Gitbook #57-#59. No other PRs are referenced.

- `agents.jsonl.additions`: 7 rows in the existing agents.jsonl format, one for each merged PR that has no row yet. `merged` is GitHub `merged_at`. `agent`, `launched` and `tokens_est` are null because GitHub doesn't record them. Per the README, they come from cloud-agent transcripts. These rows should not count toward tokens-per-improvement until those fields are filled.
- The 4 existing rows (TESSERA #262 and #264, Gitbook #58 and #59) match GitHub merged_at exactly, so they need no update.
- `ci.jsonl.sidecar`: CI results, kept in a separate file because agents.jsonl has no CI field. All 8 TESSERA PRs have one `validate` check that ended in `failure`. Durations (GitHub check-run started_at → completed_at, head commit of each PR):
  - #251: 2s (job 115161001845)
  - #256: 2m11s (job 115172826561)
  - #260: 1m56s (job 115190328611)
  - #261: 2m30s (job 115193441079)
  - #262: 2m15s (run 38366719917, job 115193490111)
  - #263: 2m04s (job 115206794524)
  - #264: 2m05s (job 115213401592)
  - #265: 1m46s (job 115213443186)
  Cause: Actions billing outage is REPORTED, not verified. Only #251 (2s) looks like a job that never ran; the other 7 ran 1m46s–2m30s and are likely real validate failures. All 3 Gitbook PRs have 0 check runs, so their result is null.
- No metrics.jsonl additions: GitHub has no before/after measurements.
- No Vitality or Stripe content. The scoreboard scripts were not touched.
