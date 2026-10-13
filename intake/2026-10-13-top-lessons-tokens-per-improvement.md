# PROPOSED intake/ entry — Top measured lessons by tokens per merged improvement
Route: Gitbook Cordnation (approved by Tessera; feature branch only). Assigned by Mesh Admin Coordinator / Tessera (provisional).
Source: vitalitychems-dot/Gitbook @ aa9506f — mesh/scoreboard/metrics.jsonl (16 rows), agents.jsonl (4 rows). Scoreboard scripts untouched.

Method: join metrics.jsonl `pr` to agents.jsonl `pr`; tokens/improvement = agents.tokens_est ÷ count of metrics rows with that PR. Lower = better. No self-grading; values are copied as recorded.

| Rank | Lesson | metrics.jsonl row | agents.jsonl row | Tokens/improvement |
|---|---|---|---|---|
| 1 | Expose the shared queue to agents: small, targeted mesh wiring is cheapest | L14 `TM-tasks` queued tasks visible 0→7 (hi), TESSERA#264 | L2 bc-c39255ef, 32,914 | 32,914 |
| 2 | Verify data-source terms up front (sovereign) | L16 `SH-terms` verified sources 0→8 (hi), Gitbook#59 | L3 bc-9edda2cd, 66,098 | 66,098 |
| 3 | Security fix with a binary measurable (forged cookie rejected) | L12 `Q007-forge` accepted 1→0 (lo), TESSERA#262 | L1 bc-ae89f0a9, 76,087 | 76,087 |
| 4 | DATA GAP: unranked, no tokens_est in agents.jsonl for the remaining metrics rows | n/a | n/a | n/a |
| 5 | DATA GAP: unranked, Gitbook#58 has tokens (55,932) but no metrics row | n/a | L4 bc-093f8a2a | n/a |

## Data gaps
- agents.jsonl covers only 4 PRs; 12 of 16 metrics rows (PRs TESSERA#251, 256, 260, 261, 263, 265; Gitbook#57) have no tokens_est, so their tokens/improvement can't be computed.
- Gitbook#58 has tokens (L4 bc-093f8a2a, 55,932) but no metrics row, so there is no measured improvement to cite.
- tokens_est is an estimate field. There is no "merged improvement" count field, so the count is inferred as 1 metrics row per PR.

## Ask
Have agents append to agents.jsonl for every merged PR so ranks 4–5 can be filled.
