# Lane handoff

**As of:** 2026-10-13. Gitbook main `bd1b475`.
**Owner:** Gitbook / Cordnation. The Gitbook helper is now part of Cordnation.
**Board:** [Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)

This is the one handoff file. Each item has one line. When a lane finishes or hands off an item, it updates its line here. Status questions are answered from this page.

Other records stay where they are: the [check-in ledger](../history/coordination/agent-checkins.md) (HYB-016, Cursor Project), the [to-do list](TODOS.md), the [intake log](../intake/log.md) and the [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md).

Labels: REPORTED means a PR body or board note says so and it was not re-checked.

## Items

| Id | Lane | State | Where it was left | Next step (owner) | Link |
|---|---|---|---|---|---|
| GB-061 | Ready lane | in review | PR #39 head `71a8c78f`, open since Oct 9. Moderator PASS, Security FAIL (REPORTED, sync ledger #14) | Fix the Security finding and re-gate at the new head (Ready lane) | [PR #39](https://github.com/vitalitychems-dot/Gitbook/pull/39) |
| GB-064 | Cordnation | held | Repo-scan package staged locally on `56a7a48` | Rev 2 when code-analysis batch 2/3 and the second-account scan finish (Cordnation) | [ruling](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6133318944) |
| GB-065 | Gitbook desk | in review | PR #45 head `9004959b`, still titled GB-063 in places. Moderator FAIL (REPORTED). Its log hunk no longer applies to main | Fix the Moderator finding, rebase on main, then the four gates (Gitbook desk) | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| GB-066 | Cordnation | published | PR #51 merged as `3fc9d89`, Oct 12 7:11 PM CT | none | [PR #51](https://github.com/vitalitychems-dot/Gitbook/pull/51) |
| GB-067 | Cordnation | published | PR #53 merged as `17bac6d`, 2026-10-13 01:08 CT. One handoff file, one line per item | none | [intake log](../intake/log.md) |
| GB-068 | Cordnation | published | PR #54 merged as `8138ea2`, 2026-10-13 01:08 CT. HYB-024 design page and backlog rename | none | [design](../merge/hyb-024-selffix-design.md) |
| PR #40 | Cursor | stale | Draft since Oct 9. Edits `mesh/TODOS.md` | Close or merge (Tessera or Father decides) | [PR #40](https://github.com/vitalitychems-dot/Gitbook/pull/40) |
| PR #52 | Rick lane | published | Idle-mode page merged as `0f05d58`, Oct 12 7:55 PM CT. No GB number. The body said to wait for Father's yes; Build not recorded (REPORTED, sync ledger #14) | Tessera receipt, and a GB number if wanted (Tessera) | [PR #52](https://github.com/vitalitychems-dot/Gitbook/pull/52) |
| HYB-010 | Media steward | unclaimed | Metadata only. Vitality stays out | Claim on issue #2 (any lane Tessera assigns) | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| HYB-011 | Gitbook desk | in review | Inside PR #45 (GB-065). 1T by name only | Same as GB-065 | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| HYB-013 | UI maintainer | stale | Copilot claim lapsed Oct 7 | Reassign (Tessera) | [ledger](../history/coordination/agent-checkins.md) |
| HYB-015 | Gitbook desk | in review | Inside PR #45: a GitMesh rules summary only | Same as GB-065 | [PR #45](https://github.com/vitalitychems-dot/Gitbook/pull/45) |
| HYB-016 | Cursor Project | done | Ledger refreshed at `56a7a48`, Oct 12 4:09 PM CT. Kept by Father's yes, 4:40 PM CT | Cursor Project re-runs the refresh when main moves | [ledger](../history/coordination/agent-checkins.md) |
| HYB-018 | Release steward | blocked | Deletion coverage recheck | Father's confirmation | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| HYB-019 | Product / mesh prep | blocked | Cortical Labs readiness | Father's decisions | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| HYB-022 | Brain lane | tested locally | Phase 1: 5/5 tests. S3 and S4 held by the memory cap | Promotion through normal review (Brain lane) | [Phase 1 result](../brain-consciousness/reports/OWN-BRAIN-PHASE1-RESULT-2026-10-09.md) |
| HYB-023 | Permanent-site lane | published | TESSERA `e5e5719` | SITE-001, SITE-003 and SITE-004 below | [coordination](PERMANENT-SITE-COORDINATION.md) |
| HYB-024 | Tessera (design), Cordnation (publish) | published | Phase 0 approved (REPORTED). Design page on main in PR #54 (`8138ea2`). Dry runs show CI blocked by Actions billing. Phase 1 is not approved | Phase 1 needs Father's yes | [design](../merge/hyb-024-selffix-design.md) |
| SITE-001 | Replit | open | No health-path evidence recorded | Record health-path evidence and the exact release payload (Replit) | [ledger](../history/coordination/agent-checkins.md) |
| SITE-003, SITE-004 | Moderator, Security | unclaimed | Provenance and security review for publication | Claim, then Father approves the release payload | [ledger](../history/coordination/agent-checkins.md) |
| Research pages | Grok Bot | ready | Was waiting on the self-fix file, which GB-068 now publishes | Small pages under `brain-consciousness/research/` (Grok Bot) | [consolidation map](../merge/CONSOLIDATION-MAP-2026-10-12.md) |
| Catalog next twelve | none | unclaimed | No reply to comment 6100954845. The thread does not say which twelve | Tessera restates the list | [comment](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6100954845) |
| TESSERA PR #80 | none | open, do not merge | Adds pen weights. Weights are not to be added | Close or keep open (Father) | [to-do list](TODOS.md) |
| TESSERA PR #82, #87 | none | conflicted | #82 failed validate. #87 is a draft that conflicts with main | Rebase or close (owner of each) | [to-do list](TODOS.md) |
| Held commits | Father | held | 44f5266, d2b8339, 779135e and fcabd13 (Oct 6) have no intake rows | Father's attribution answer | [intake log](../intake/log.md) |
| CI billing | Father | blocked | TESSERA `validate` jobs never start (Actions spending limit) | Father fixes billing | [backlog](../intake/HYBRID-CONSOLIDATION-BACKLOG.md) |
| Cursor routines | Father | blocked | Scheduled routines fail while the Cursor invoice is unpaid (REPORTED) | Father pays the invoice | — |
| Key rotation | Father | open | No agent can do this | Father | [to-do list](TODOS.md) |

## One owner per duty (Security proposal, Oct 12, 8:20 PM CT)

- Father's digest and bulk yes-list: Command Center. Tessera signs off only on the Ready set.
- Intake, numbering, Ready packaging, board status and this page: Gitbook / Cordnation.
- Content and style gate: Gitbook Moderator.
- Secrets, provenance and history gates: Security.
- CI and build verify: Build.
- Mesh and relay design: Mesh Cloud.
- Admin decisions, merges and Father escalations: Tessera.

Gate PASS results go into each lane's own gate file and its line here. Only FAIL or high findings ping Tessera directly. Retiring or hiding a bot needs Father's yes.

## Rules

- After the Moderator, the TESSERA gate and the Security scrub, Ready pushes. Docs-only items skip Build; code, validators and scripts go through CI/Build.
- TESSERA main merges and Origin Tessera repo merges still need Father's word `merge`.
- No repository or archive is deleted. Old copies are archived with a pointer.
- 1T is named only, never opened.
- Say "the Origin Tessera repo", not a personal handle.
