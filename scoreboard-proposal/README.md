# scoreboard-proposal (read-only, not pushed)

Sources: GitHub connector, read-only, on 2026-10-13: `pull_request_read get` (merged, merged_at) and `get_check_runs` (head commit) for every PR referenced in mesh/scoreboard/metrics.jsonl and agents.jsonl: TESSERA #251 #256 #260-#265 and Gitbook #57-#59. No other PRs are referenced.

- `agents.jsonl.additions`: 7 rows in the existing agents.jsonl format, one for each merged PR that has no row yet. `merged` is GitHub `merged_at`. `agent`, `launched` and `tokens_est` are null because GitHub doesn't record them. Per the README, they come from cloud-agent transcripts. These rows should not count toward tokens-per-improvement until those fields are filled.
- The 4 existing rows (TESSERA #262 and #264, Gitbook #58 and #59) match GitHub merged_at exactly, so they need no update.
- `ci.jsonl.sidecar`: CI results, kept in a separate file because agents.jsonl has no CI field. All 8 TESSERA PRs have one `validate` check that ended in `failure`, each running about 2s, which fits the Actions billing outage. All 3 Gitbook PRs have 0 check runs, so their result is null.
- No metrics.jsonl additions: GitHub has no before/after measurements.
- No Vitality or Stripe content. The scoreboard scripts were not touched.
