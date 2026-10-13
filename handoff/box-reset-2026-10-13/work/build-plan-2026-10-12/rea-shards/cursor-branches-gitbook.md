# REA shard: cursor/* branches on vitalitychems-dot/Gitbook (read-only)

- main: 2344334e689ad8fdfc9b5c7848aa8f1fdeac6afb (committed 2026-10-12 17:18 CT)
- Triage time: 2026-10-12 ~19:00 CT. Fetched with `git fetch --all --prune`; PR list from GitHub connector (state=all).
- No pushes, merges, deletes, comments or PRs made.

## Summary counts
- cursor/* branches on remote: **17** (not 19).
- With an open PR (excluded from triage): 1 — `cursor/father-yes-record-b14e` (PR #40 open).
- Triaged (no open PR): **16** — **9 merged** (ancestors of main, all via closed+merged PRs), **7 unmerged**.
- Duplicate: `origin/chamber-desk-sync-bf31` (non-cursor name) and `origin/cursor/chamber-desk-sync-bf31` both point at 9bd972c7. Counting that twin gives 17 heads, still not 19.
- None of the 7 unmerged branches has a PR record (open or closed).

## Table
| Branch | Head | Date (CT) | Merged? | Notes |
|---|---|---|---|---|
| cursor/gb-040-batch-014-4d1a | 46654c24 | 10-06 18:57 | YES (PR #15) | ancestor |
| cursor/gitbook-batch-013-6568 | 9511a776 | 10-06 18:54 | YES (PR #14) | ancestor |
| cursor/gitbook-list1-approved-f67c | 64778b33 | 10-05 18:01 | YES (PR #12) | ancestor |
| cursor/hyb-006-grok-ready-b214 | 4da54d5a | 10-05 13:34 | YES (PR #3) | ancestor |
| cursor/hyb-007-z-app-5404 | 580a3dc3 | 10-05 13:50 | YES (PR #4) | ancestor |
| cursor/hyb-008-017 | 5a1ad10e | 10-10 14:22 | YES (PR #41) | ancestor |
| cursor/hyb-next | 940b8a21 | 10-10 14:24 | YES (PR #42) | ancestor |
| cursor/ready-batches-003-009-9e09 | 80106264 | 10-05 08:25 | YES (PR #1) | ancestor |
| cursor/todos | b4a5899b | 10-10 14:28 | YES (PR #43) | ancestor |
| cursor/chamber-desk-sync-bf31 (+ twin chamber-desk-sync-bf31) | 9bd972c7 | 10-05 22:33 | NO | +2 / -218 behind; 5 files +72/-10; conflicts |
| cursor/grok-disk-batch-verify-1387 | 681c946c | 10-10 13:39 | NO (content in main) | patch-equivalent already on main |
| cursor/hyb-016-ledger-refresh-44f1 | a4c2803f | 10-12 16:08 | NO | +2 / -11; 1 file +41/-3; merges clean |
| cursor/hyb-021-checkin-aa90 | 5e8396b5 | 10-09 03:07 | NO (content in main) | patch-equivalent; conflicts |
| cursor/project-lane-site-002-7ea3 | 7b46ef2e | 10-09 22:54 | NO | +6 / -57; 9 files +189/-23; heavy conflicts |
| cursor/three-way-auto-collab-d42f | 63adaa02 | 10-10 10:45 | NO | +2 / -38; 6 files +109/-23; conflict |
| cursor/todos-current-aa90 | 51571178 | 10-08 16:36 | NO (content in main) | patch-equivalent; conflicts |
| cursor/father-yes-record-b14e | 4d577008 | 10-09 17:29 | — | OPEN PR #40, out of scope; would conflict in mesh/TODOS.md |

## REA per unmerged branch

### cursor/chamber-desk-sync-bf31 @ 9bd972c7 (and twin `chamber-desk-sync-bf31`)
- Commits (author "Tessera" — git author name is not proof): 5679503 "Record the chamber desk branches and the audit block"; 9bd972c "File GB-030 on the intake log and point the desk note at it".
- Adds review/CHAMBER-DESK-SYNC-2026-10-06.md (new, 53 lines, not on main), edits SUMMARY.md, intake/log.md, mesh/HANDOFF.md, mesh/roles/board-world-chamber.md.
- Conflicts: intake/log.md, mesh/HANDOFF.md (218 commits behind main).
- Risk: none seen (no secrets/1T/wallet terms; no deletions beyond line edits).
- Recommendation: **needs rebase** if the chamber-desk review page is still wanted (check GB-030 status on main first); otherwise **stale**. Twin branch is a **duplicate** — keep only one.

### cursor/grok-disk-batch-verify-1387 @ 681c946c
- Adds 19-line check-in entry verifying Grok disk-port batch (TESSERA PR #168) to history/coordination/agent-checkins.md.
- git cherry shows the patch is already on main (main line 80–85 records PR #168 verification).
- Risk: none. Recommendation: **superseded** (safe to delete later with approval).

### cursor/hyb-016-ledger-refresh-44f1 @ a4c2803f
- 2 commits: refresh check-in ledger to Gitbook d27e3e6 / TESSERA a502322; restore HYB-023 follow-up wording and list HYB-014 note under CHANGED. 1 file, +41/-3; merges cleanly.
- Main already carries a d27e3e6/a502322 ledger snapshot (agent-checkins.md lines 14–22), so this is likely the pre-push or follow-up version of the work that landed by direct push 56a7a48d (flagged in Ledger #10). Patches are not identical to main.
- Risk: none (its own SCOPE line excludes TESSERA/vitality/1T). Process note: HYB-016 agent reported PR creation returns 403.
- Recommendation: **mostly superseded**; diff the two follow-up edits against main and either open a small PR for the remaining wording or drop.

### cursor/hyb-021-checkin-aa90 @ 5e8396b5
- Marks HYB-021 done in agent-checkins.md and intake/HYBRID-CONSOLIDATION-BACKLOG.md.
- git cherry: both patches already on main. Conflicts are only from later edits.
- Risk: none. Recommendation: **superseded**.

### cursor/project-lane-site-002-7ea3 @ 7b46ef2e
- 6 commits: claim SITE-002 lane, three-way collab protocol, roles/overview, SUMMARY links, hub lanes table, mark HYB-013 STALE. 9 files +189/-23.
- main already has mesh/SITE-002-2026-10-10.md and mesh/THREE-WAY-COLLAB-PROTOCOL.md (add/add conflicts on 7 files); 1 of 6 patches already identical on main.
- Contains a BLOCKER line "create_pull_request returns 403" and safety lines ("Did not open 1T", "No vitality / 1T / weights") — mentions only, no secrets.
- Recommendation: **superseded / needs rebase** — most of the lane landed via another route; only the HYB-013 STALE marking and hub table may be unique. Re-check before any PR.

### cursor/three-way-auto-collab-d42f @ 63adaa02
- 2 commits: turn on three-way automatic collaboration loop; claim auto-collab + Replit/Grok next actions. 6 files +109/-23 (protocol +60 lines, hub, playbook, replit-agents-start-here, cursor-project role, check-ins).
- Conflict only in agent-checkins.md; patches not on main.
- Risk: process — it switches on an "automatic" collaboration loop between agents; that is a policy change that needs Tessera + Father approval, not a doc tweak.
- Recommendation: **keep for PR (needs rebase)** only if Tessera wants the auto-collab loop; otherwise drop.

### cursor/todos-current-aa90 @ 51571178
- Syncs mesh/TODOS.md to main state (5/-5). Patch already on main.
- Risk: none. Recommendation: **superseded**.
