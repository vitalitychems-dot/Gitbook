# Mesh status

Built 2026-10-13 15:45 CT by status.py from files only (0 model tokens). Source: HANDOFF.md as of 2026-10-13, TASKS.json, intake/log.md.

## Needs attention

- Q-002 is 'queued' but GB-067 is 'published' in HANDOFF.md -> close or re-scope
- Q-002 is 'queued' but GB-068 is 'published' in HANDOFF.md -> close or re-scope
- Cursor routines: missing Link

## By lane: doing and next

| Lane | Item | State | Next |
|---|---|---|---|
| Brain lane | HYB-022 | tested locally | Promotion through normal review (Brain lane) |
| Cordnation | GB-064 | held | Rev 2 when code-analysis batch 2/3 and the second-account scan finish (Cordnation) |
| Cursor | PR #40 | stale | Close or merge (Tessera or Father decides) |
| Father | Held commits | held | Father's attribution answer |
| Father | CI billing | blocked | Father fixes billing |
| Father | Cursor routines | blocked | Father pays the invoice |
| Father | Key rotation | open | Father |
| Gitbook desk | GB-065 | in review | Fix the Moderator finding, rebase on main, then the four gates (Gitbook desk) |
| Gitbook desk | HYB-011 | in review | Same as GB-065 |
| Gitbook desk | HYB-015 | in review | Same as GB-065 |
| Grok Bot | Research pages | ready | Small pages under `brain-consciousness/research/` (Grok Bot) |
| Media steward | HYB-010 | unclaimed | Claim on issue #2 (any lane Tessera assigns) |
| Moderator, Security | SITE-003, SITE-004 | unclaimed | Claim, then Father approves the release payload |
| Product / mesh prep | HYB-019 | blocked | Father's decisions |
| Release steward | HYB-018 | blocked | Father's confirmation |
| Replit | SITE-001 | open | Record health-path evidence and the exact release payload (Replit) |
| UI maintainer | HYB-013 | stale | Reassign (Tessera) |
| none | Catalog next twelve | unclaimed | Tessera restates the list |
| none | TESSERA PR #80 | open, do not merge | Close or keep open (Father) |
| none | TESSERA PR #82, #87 | conflicted | Rebase or close (owner of each) |

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

- GB-061 (Ready lane): PR #39 merged to main in merge commit `c62d45b3` (c62d45b36f4a2fe82dc8fad50a88f476aafb032c, 2026-10-
- GB-066 (Cordnation): PR #51 merged as `3fc9d89`, Oct 12 7:11 PM CT
- GB-067 (Cordnation): PR #53 merged as `17bac6d`, 2026-10-13 01:08 CT. One handoff file, one line per item
- GB-068 (Cordnation): PR #54 merged as `8138ea2`, 2026-10-13 01:08 CT. HYB-024 design page and backlog rename
- PR #52 (Rick lane): Idle-mode page merged as `0f05d58`, Oct 12 7:55 PM CT. No GB number. The body said to wait for Fathe
- HYB-016 (Cursor Project): Ledger refreshed at `56a7a48`, Oct 12 4:09 PM CT. Kept by Father's yes, 4:40 PM CT
- HYB-023 (Permanent-site lane): TESSERA `e5e5719`
- HYB-024 (Tessera (design), Cordnation (publish)): Phase 0 approved (REPORTED). Design page on main in PR #54 (`8138ea2`). Dry runs show CI blocked by 

## Can be cleaned up

- GB-061: done with next step 'none' -> move line to archive
- GB-066: done with next step 'none' -> move line to archive
- GB-067: done with next step 'none' -> move line to archive
- GB-068: done with next step 'none' -> move line to archive
- PR #40: stale -> Close or merge (Tessera or Father decides)
- HYB-013: stale -> Reassign (Tessera)
