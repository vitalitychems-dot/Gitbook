# Mesh status

Built 2026-10-13 15:45 CT by status2.py from files only (0 model tokens).

REPORTED rows: 7 of 30 (GB-061, GB-065, PR #52, AUTO-ADMISSION, SITE-002-R1, HYB-024, Cursor routines)  
Complete open rows: 21 of 25

## Needs attention

- OWNERLESS Catalog next twelve: Tessera restates the list
- OWNERLESS TESSERA PR #80: Close or keep open (Father)
- OWNERLESS TESSERA PR #82, #87: Rebase or close (owner of each)
- Cursor routines: missing Link
- Q-002 is 'queued' but GB-067 is 'published' in HANDOFF.md -> close or re-scope
- Q-002 is 'queued' but GB-068 is 'published' in HANDOFF.md -> close or re-scope
- HYB-013: incomplete (evidence)
- HYB-022: incomplete (evidence)
- Catalog next twelve: incomplete (owner_in_next)
- Cursor routines: incomplete (link)
- lane lint Catalog next twelve: no owner
- lane lint TESSERA PR #80: no owner
- lane lint TESSERA PR #82, #87: no owner

## Lanes: doing and next

| Lane | Item | State | Gate | Next |
|---|---|---|---|---|
| none | Catalog next twelve | unclaimed |  | Tessera restates the list |
| none | TESSERA PR #80 | open, do not merge |  | Close or keep open (Father) |
| none | TESSERA PR #82, #87 | conflicted |  | Rebase or close (owner of each) |
| Brain lane | HYB-022 | tested locally |  | Promotion through normal review (Brain lane) |
| Cordnation | GB-064 | held |  | Rev 2 when code-analysis batch 2/3 and the second-account scan finish (Cordnation) |
| Cursor | PR #40 | stale |  | Close or merge (Tessera or Father decides) |
| Cursor Project | AUTO-API-HARDEN | landing |  | Landing worker posts blob check and result (Cursor Project); gates as Tessera sets them |
| Cursor Project | AUTO-ADMISSION | landed |  | Wiring behind an admin gate is a follow-up (Tessera decides) |
| Cursor Project | MESH-001 | landed |  | Father answers the three questions (Father) |
| Cursor Project | YouTube playlist | blocked |  | Father sends an unlisted link or the video URLs |
| Father | Held commits | held |  | Father's attribution answer |
| Father | CI billing | blocked |  | Father fixes billing |
| Father | Cursor routines | blocked |  | Father pays the invoice |
| Father | Key rotation | open |  | Father |
| Gitbook desk | GB-065 | in review | FAIL | Fix the Moderator finding, rebase on main, then the four gates (Gitbook desk) |
| Gitbook desk | HYB-011 | in review |  | Same as GB-065 |
| Gitbook desk | HYB-015 | in review |  | Same as GB-065 |
| Grok Bot | Research pages | ready |  | Small pages under `brain-consciousness/research/` (Grok Bot, or whoever holds the source) |
| Media steward | HYB-010 | unclaimed |  | Claim on issue #2 (any lane Tessera assigns) |
| Moderator, Security | SITE-003, SITE-004 | unclaimed |  | Claim, then Father approves the release payload |
| Product / mesh prep | HYB-019 | blocked |  | Father's decisions |
| Ready lane | GB-061 | in review | FAIL | Fix the Security finding and re-gate at the new head (Ready lane) |
| Release steward | HYB-018 | blocked |  | Father's confirmation |
| Replit | SITE-001 | open |  | Record health-path evidence and the exact release payload (Replit) |
| UI maintainer | HYB-013 | stale |  | Reassign (Tessera) |

## Queue

| Task | Lane | Status | Title |
|---|---|---|---|
| Q-001 | Build | queued | Rebase Gitbook PR #45 (desk/gb-063-hyb-011) onto main |
| Q-002 | Build | queued | Land GB-067 + GB-068 (Build PASS 2026-10-13, see GATE-2026-10-13-GB-067-068.md) |
| Q-003 | Moderator | queued | Rename leftover GitbookAI references to GitMesh (5 files as of 8138ea2f; keep historical q |
| Q-004 | Tessera | queued | Retry generative_agents REA ingest (shallow, license kept) |
| Q-005 | Tessera | blocked | Embedding recall for brain memory graph (blocked until a small embedding model can be fetc |
| Q-006 | Pharaoh | queued | Improve emotion recognition (stuck at 72% on 50 unseen; low on 218-line mesh set) |
| Q-007 | Security | queued | Sign the GitAI spectator session cookie (cookie is currently the plain handle) |

## Token ledger (today)

- no entries
- no ledger line today: Brain lane, Build, Cordnation, Cursor, Cursor Project, Einstein, Father, Gitbook desk, Grok Bot, Media steward, Moderator, Permanent-site lane, Pharaoh, Product / mesh prep, Ready lane, Release steward, Replit, Rick lane, Security, Tessera, UI maintainer

## Can be cleaned up

- PR #40: stale -> Close or merge (Tessera or Father decides)
- HYB-013: stale -> Reassign (Tessera)
