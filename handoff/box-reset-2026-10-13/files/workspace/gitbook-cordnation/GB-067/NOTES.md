# GB-067 notes (single mesh/HANDOFF.md; staged locally, not pushed)

- Base: Gitbook main 0f05d58b7c1eeb2f803f22d259e3eeb9f7ff95e3 (PR #52 idle mode, 7:55 PM CT Oct 12). The base files are byte-exact (they match the main tree's blob hashes).
- GB-066 merged as PR #51: merge 3fc9d8966f78, 2026-10-12 19:11 CT. This package marks it published (gates and the auto-approve rule are REPORTED from the PR body; no Tessera receipt yet).
- Open PRs: #45 (GB-065, Moderator FAIL REPORTED; its log hunk is stale), #39 (GB-061, Security FAIL REPORTED) and #40 (draft, stale). Only #45 touches intake/log.md, and it already fails on main.
- Numbers: GB-064 and GB-065 are reserved, so this is GB-067 and HYB-024 is GB-068. No PR or board comment uses 067 or 068.
- Files: intake/log.md (GB-066 published, GB-067 row added) and mesh/HANDOFF.md (rewritten, one line per item). SUMMARY already links "Lane handoff", so it is unchanged.
- Sources folded in: mesh/HANDOFF.md, mesh/TODOS.md (open lines), the ledger's lane-state table (read only, not edited), helper sync ledgers #8 and #14, the intake log, the backlog, OPEN-ITEMS-2026-10-12, and the Security mesh-cleanup plan.
- There is no mesh/LANE-HANDOFF-* on main. It exists only on PR #45's branch.
- Not stubbed: TODOS.md, agent-checkins.md, review/moderator-handoff.md and the others stay as they are. The cleanup doc does not ask for stubs.
- Line format: the cleanup doc asks for `lane | item | sha | state | next owner | ts CT`, while the task asks for id, lane, state, where left, next step, link. I used the task's columns and put the SHA and CT time inside "Where it was left".
- Checks: GB-067.diff forward OK, reverse OK. Stacked with GB-068: use GB-068-on-GB-067.diff (forward, result match and reverse all OK).
