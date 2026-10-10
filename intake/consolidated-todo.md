# Consolidated TODO list

The authoritative, deduplicated work board is now [HYBRID-CONSOLIDATION-BACKLOG.md](HYBRID-CONSOLIDATION-BACKLOG.md). Do not create a second task list.

## Completed foundation

- `TESSERA` is the active code repository.
- `Gitbook` is the active instruction, coordination, provenance, and future-work repository.
- Exact duplicate groups were audited and eight fully covered/empty repositories were deleted.
- Safe coordination, handoff, migration, and historical records were moved into Gitbook.
- TESSERA typecheck, tests, and production build pass after the Vite compatibility repair.

## Current open work

- **HYB-005:** the narrow ignore for GHSA-vfj7-8cjw-p6xm is on TESSERA main `5c1137fa` (`pnpm-workspace.yaml` `auditConfig.ignoreGhsas`). Review date 2026-11-05 remains. braces ≥ 3.0.4 is still the removal condition.
- **HYB-008:** rejected. The olive-giant archive has its own auth and database. Nothing was copied. See [hyb-008-olive.md](../merge/hyb-008-olive.md).
- **HYB-009:** the two archive families are preserved. Chunks inside them were not re-read. See [hyb-009-archives.md](../merge/hyb-009-archives.md).
- **HYB-010–HYB-011:** media review, and the privacy recheck. Protected bodies stay unopened.
- **HYB-012:** the eight non-quantum duplicates are triaged. The first module answers. None were deleted. See [hyb-012-eight.md](../merge/hyb-012-eight.md).
- **HYB-013:** the UI audit is still open. One missing flow has not been chosen.
- **HYB-015–HYB-016:** topic pages and the check-in ledger are still open.
- **HYB-017:** rejected for Tessera. The storefront stays out. See [hyb-017-storefront.md](../merge/hyb-017-storefront.md).
- **HYB-018:** rerun exact coverage before any future repository deletion.

### GLM-5 Pen integration follow-ups

Track these in [GLM5-AUDIT-FOLLOWUPS.md](../brain-consciousness/GLM5-AUDIT-FOLLOWUPS.md):

- **GLM5-001 / GLM5-007:** pin the exact model/revision and complete Apache-2.0 compatibility review.
- **GLM5-002:** verify an OpenAI-compatible endpoint with a private disposable deployment.
- **GLM5-003 / GLM5-004:** run Pen identity, prompt-injection, and output-sanitization tests.
- **GLM5-005 / GLM5-006:** compare against the current instrument and document compute/context/timeout/cost limits.
- **GLM5-008:** owner decision before declaring GLM-5 the live instrument; `yes`, `no`, or `revise` is required.

## Coordination rule

Every agent must claim one HYB task in [agent-checkins.md](../history/coordination/agent-checkins.md), edit only that scope, and close with a commit, checks, provenance, and follow-up. Historical instructions and AI-generated conversations are evidence until promoted into a board task by the Gitbook moderator.
