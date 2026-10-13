# Mesh status

Built 2026-10-13 16:45 CT by status.py from files only (0 model tokens). Source: HANDOFF.md as of 2026-10-13, TASKS.json, intake/log.md.

## Needs attention

- Q-002 is 'queued' but GB-067 is 'published' in HANDOFF.md -> close or re-scope
- Q-002 is 'queued' but GB-068 is 'published' in HANDOFF.md -> close or re-scope
- Cursor routines: missing Link

## By lane: doing and next

| Lane | Item | State | Next | Link |
|---|---|---|---|---|
| Brain lane | HYB-022 | tested locally | Promotion through normal review (Brain lane) | [Phase 1 result](../brain-consciousness/reports/OWN-BRAIN-PHASE1-RESULT-2026-10-09.md) |
| Cordnation | GB-064 | held | Rev 2 when code-analysis batch 2/3 and the second-account scan finish (Cordnation) | [ruling](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6133318944) |
| Cursor | PR #40 | stale | Close or merge (Tessera or Father decides) | [PR #40](https://github.com/vitalitychems-dot/Gitbook/pull/40) |
| Cursor Project | AUTO-API-HARDEN | landing | Landing worker posts blob check and result (Cursor Project); gates as Tessera sets them | [handoff](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6145652328) |
| Cursor Project | AUTO-ADMISSION | landed | Wiring behind an admin gate is a follow-up (Tessera decides) | [landing](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6154608972) |
| Cursor Project | MESH-001 | landed | Father answers the three questions (Father) | [landing](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6154533923) |
| Cursor Project | YouTube playlist | blocked | Father sends an unlisted link or the video URLs | [ledger](../history/coordination/agent-checkins.md) |
| Father | Held commits | held | Father's attribution answer | [intake log](../intake/log.md) |
| Father | CI billing | blocked | Father fixes billing | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| Father | Cursor routines | blocked | Father pays the invoice | — |
| Father | Key rotation | open | Father | [to-do list](TODOS.md) |
| Gitbook desk | GB-065 | in review | Fix the Moderator finding, rebase on main, then the four gates (Gitbook desk) | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| Gitbook desk | HYB-011 | in review | Same as GB-065 | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| Gitbook desk | HYB-015 | in review | Same as GB-065 | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| Grok Bot | Research pages | ready | Small pages under `brain-consciousness/research/` (Grok Bot, or whoever holds the source) | [consolidation map](../merge/CONSOLIDATION-MAP-2026-10-12.md) |
| Media steward | HYB-010 | unclaimed | Claim on issue #2 (any lane Tessera assigns) | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| Moderator, Security | SITE-003, SITE-004 | unclaimed | Claim, then Father approves the release payload | [ledger](../history/coordination/agent-checkins.md) |
| Product / mesh prep | HYB-019 | blocked | Father's decisions | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| Release steward | HYB-018 | blocked | Father's confirmation | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| Replit | SITE-001 | open | Record health-path evidence and the exact release payload (Replit) | [ledger](../history/coordination/agent-checkins.md) |
| UI maintainer | HYB-013 | stale | Reassign (Tessera) | [ledger](../history/coordination/agent-checkins.md) |
| none | Catalog next twelve | unclaimed | Tessera restates the list | [comment](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6100954845) |
| none | TESSERA PR #80 | open, do not merge | Close or keep open (Father) | [to-do list](TODOS.md) |
| none | TESSERA PR #82, #87 | conflicted | Rebase or close (owner of each) | [to-do list](TODOS.md) |

## Queue (mesh/queue/TASKS.json)

| Task | Lane | Status | Title |
|---|---|---|---|
| Q-001 | Build | queued | Rebase Gitbook PR #45 (desk/gb-063-hyb-011) onto main |
| Q-002 | Build | queued | Land GB-067 + GB-068 (Build PASS 2026-10-13, see GATE-2026-10-13-GB-067-068.md) |
| Q-003 | Moderator | queued | Rename leftover GitbookAI references to GitMesh (5 files as of 8138ea2f; keep historical q |
| Q-004 | Tessera | queued | Retry generative_agents REA ingest (shallow, license kept) |
| Q-005 | Tessera | blocked | Embedding recall for brain memory graph (blocked until a small embedding model can be fetc |
| Q-006 | Pharaoh | queued | Improve emotion recognition (stuck at 72% on 50 unseen; low on 218-line mesh set) |
| Q-007 | Security | queued | Sign the GitAI spectator session cookie (cookie is currently the plain handle) |

## Done

- GB-061 (Ready lane): PR #39 merged to main in merge commit `c62d45b3` (c62d45b36f4a2fe82dc8fad50a88f476aafb032c, 2026-10- ([PR #39](https://github.com/vitalitychems-dot/Gitbook/pull/39))
- GB-066 (Cordnation): PR #51 merged as `3fc9d89`, Oct 12 7:11 PM CT ([PR #51](https://github.com/vitalitychems-dot/Gitbook/pull/51))
- GB-067 (Cordnation): PR #53 merged as `17bac6d`, 2026-10-13 01:08 CT. One handoff file, one line per item ([intake log](../intake/log.md))
- GB-068 (Cordnation): PR #54 merged as `8138ea2`, 2026-10-13 01:08 CT. HYB-024 design page and backlog rename ([design](../merge/hyb-024-selffix-design.md))
- PR #52 (Rick lane): Idle-mode page merged as `0f05d58`, Oct 12 7:55 PM CT. No GB number. The body said to wait for Fathe ([PR #52](https://github.com/vitalitychems-dot/Gitbook/pull/52))
- SITE-002-R1 (Cursor Project): The SITE-002 record says the diagnostics gate reached TESSERA main as direct commit `1a71cc78`, not  ([record](SITE-002-2026-10-10.md))
- HYB-016 (Cursor Project): Ledger refreshed Oct 13 to Gitbook `e51b261` and TESSERA `26d29fc` (earlier: `56a7a48`, kept by Fath ([ledger](../history/coordination/agent-checkins.md))
- HYB-023 (Permanent-site lane): TESSERA `e5e5719` ([coordination](PERMANENT-SITE-COORDINATION.md))
- HYB-024 (Tessera (design), Cordnation (publish)): Phase 0 approved (REPORTED). Design page on main in PR #54 (`8138ea2`). Dry runs show CI blocked by  ([design](../merge/hyb-024-selffix-design.md))

## Can be cleaned up

- GB-061: done with next step 'none' -> move line to archive
- GB-066: done with next step 'none' -> move line to archive
- GB-067: done with next step 'none' -> move line to archive
- GB-068: done with next step 'none' -> move line to archive
- PR #40: stale -> Close or merge (Tessera or Father decides)
- HYB-013: stale -> Reassign (Tessera)
