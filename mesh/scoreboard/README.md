# mesh/scoreboard

- `metrics.jsonl`: one row per merged, measured change (before/after, PR). Seeded from the 2026-10-13 results: brain r1-r4, TESSERA #251-#265, Gitbook #57 and #59. #55 and #58 are left out because they have no measured delta.
- `agents.jsonl`: real cloud-agent launch-to-merge times. Launch is the agent's first tool call and merge is gh `mergedAt`. Tokens are estimated as transcript chars/4, which is a lower bound.
- `velocity.py`: kept improvements per day, mean % gain, gate pass rate, launch-to-merge time, and the headline **tokens per merged improvement**.
- `rank.py`: Father's bulk list. impact = goal weight × relative gain (capped at 100%) / token cost. Weights are tokens 0.40, speed 0.30, accuracy 0.20, and other goals 0.10. Only merged, measured gains are listed.
- `collab_check.py`: validates the HANDOFF and PROPOSALS lines described in `mesh/COLLAB.md`.

## Messages per merged item
Before (Tessera chat log, 2026-10-13, 07:55-09:05 UTC): about 19 messages for 10 merged PRs, which is about **1.9 per item**. That was 16 Tessera→Father messages and 3 agent→Tessera messages from Moderator, Akhenaten and Einstein.
After (by design): 0 agent chat messages (1 HANDOFF line each) plus 1 bulk list per batch, so a 10-item batch is about **0.1 per item**. This is a design target that still needs to be measured.
