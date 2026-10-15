# Consolidated TODO list

The authoritative, deduplicated work board is now [HYBRID-CONSOLIDATION-BACKLOG.md](HYBRID-CONSOLIDATION-BACKLOG.md). Do not create a second task list.

## Completed foundation

- `TESSERA` is the active code repository.
- `Gitbook` is the active instruction, coordination, provenance, and future-work repository.
- Exact duplicate groups were audited and eight fully covered/empty repositories were deleted.
- Safe coordination, handoff, migration, and historical records were moved into Gitbook.
- TESSERA typecheck, tests, and production build pass after the Vite compatibility repair.

## Current open work — reconciled 2026-10-15

- **TESSERA #369 / HYB-025:** candidate fix is in [PR #372](https://github.com/vitalitychems-dot/TESSERA/pull/372), head `56c54a7150c1f4dcd5a041947302c40e6225b91e`. All six GitHub checks now pass; no review decision or merge exists, so state remains **IN REVIEW**. The full applicable workspace suite, typechecks, build, and responsive production gate smoke also pass locally. API integration tests need a dedicated test database and were skipped. Complete report, audits, plan/TODO, and screenshots: [Tessera Next handoff pack](../handoff/tessera-next-2026-10-14/INDEX.md).
- **HYB-013:** production Next theme candidate is in the same PR #372 on a clean current-main implementation branch. PRs [#361](https://github.com/vitalitychems-dot/TESSERA/pull/361) and [#367](https://github.com/vitalitychems-dot/TESSERA/pull/367) remain conflicting; neither was merged or altered. The old console, preview, mockup, archives, routes, redirects, and key gate were retained. No production publication is claimed.
- **HYB-026:** Gitbook queue gate is **BLOCKED for owner review**: `python3 -m unittest test_spawn -v` produced 5 failing assertions across enabled/changed flags, unlisted-host detection, gate-tamper detection, and rogue-flag reporting. The affected `mesh/queue/` is CODEOWNERS-protected; no code was changed.
- **HYB-027:** Gitbook PR #123 current head is `f80f3a5eeb63fe3d7de8359bfa720c4e43dfe8e6`; [CI run 38653862921](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38653862921) fails JSON validity on `handoff/box-reset-2026-10-13/work/build-plan-2026-10-12/FULLPICTURE-LOADED.json` (`Expecting property name enclosed in double quotes`, line 36, column 2). The historical artifact contains Vitality metadata. `.github/` is CODEOWNERS-protected; obtain the JSON-scan owner's decision. Do not open, alter, copy, delete, or transfer that artifact; do not suppress validation. The earlier `runs.json` repair remains byte-preserving and is not the current failure. The sparse local checkout lacks `.codebase-memory/artifact.json`, so local CI is not a substitute for the remote run.
- **HYB-028:** Vitality-related metadata is present in the historical Gitbook handoff manifest, but no authorized destination repository is identified among the selected repos. Await the owner’s exact destination and scope; do not copy, move, delete, or otherwise alter the source until then.
- **HYB-005:** the narrow ignore for GHSA-vfj7-8cjw-p6xm is on TESSERA main `5c1137fa` (`pnpm-workspace.yaml` `auditConfig.ignoreGhsas`). Review date 2026-11-05 remains. braces ≥ 3.0.4 is still the removal condition.
- **HYB-008:** rejected. The olive-giant archive has its own auth and database. Nothing was copied. See [hyb-008-olive.md](../merge/hyb-008-olive.md).
- **HYB-009:** the two archive families are preserved; historical archive chunks were not re-read in this pass. See [hyb-009-archives.md](../merge/hyb-009-archives.md).
- **HYB-010–HYB-011:** media/provenance and privacy/exclusion review remain open because the named source repositories are unavailable locally. Protected bodies remain unopened.
- **HYB-012:** the eight non-quantum duplicates are triaged and intentionally retained. See [hyb-012-eight.md](../merge/hyb-012-eight.md).
- **HYB-015–HYB-016:** compact topic pages and coordination-state reconciliation remain open. Preserve historic rows; keep one current owner/scope per active task.
- **HYB-017:** rejected for Tessera. The storefront stays out. See [hyb-017-storefront.md](../merge/hyb-017-storefront.md).
- **HYB-018:** blocked until fresh exact file-coverage evidence and explicit approval exist for each named repository; no repositories were deleted.
- **HYB-023:** blocked pending an explicitly authorized full-stack host/project. Current GitHub evidence shows no TESSERA/Gitbook release, deployment, or Pages site; a `.replit` declaration is not a deployment receipt. The host-native server secret, database, health, security, monitoring and rollback gates remain unverified. Do not repeat the previously refused connector-activation proposal.
- **Box backup:** historical, partial recovery evidence only; preserve it. Metadata tree at `46baaf7d87e41ee89555c61617a8e31c1d35bdc9` is indexed in the handoff. The prior audit reports 355 safe-screened text/evidence files and 59 duplicate groups, but does not map every review to a current TSV row. All item-level content decisions remain unproven; no bundle/patch/WIP replay. See [Box intake ledger](../handoff/tessera-next-2026-10-14/BOX-INTAKE-LEDGER.md).
- **GitMesh:** remain a standalone public room/manual proposal surface. Current `main` is `951acb79a7825fff181617fa48d5d37270418ea3`, and all fetched work refs are ancestors. The new local-vault sync helper writes allowlisted paths directly to `main`; it was not run and must not be integrated under PR-based governance without an owner-approved change.
- **Grok, Replit, Cursor, bots:** live workspaces/logs are unavailable in this session; historical repository references are untrusted evidence only. Exact access/export requirements are in the [external-source inventory](../handoff/tessera-next-2026-10-14/EXTERNAL-SOURCE-INVENTORY.md).

### GLM-5 Pen integration follow-ups

Track these in [GLM5-AUDIT-FOLLOWUPS.md](../brain-consciousness/GLM5-AUDIT-FOLLOWUPS.md):

- **GLM5-001 / GLM5-007:** pin the exact model/revision and complete Apache-2.0 compatibility review.
- **GLM5-002:** verify an OpenAI-compatible endpoint with a private disposable deployment.
- **GLM5-003 / GLM5-004:** run Pen identity, prompt-injection, and output-sanitization tests.
- **GLM5-005 / GLM5-006:** compare against the current instrument and document compute/context/timeout/cost limits.
- **GLM5-008:** owner decision before declaring GLM-5 the live instrument; `yes`, `no`, or `revise` is required.

### Pen / product-identity status

- **PEN-SCOPE:** deferred. No separate Pen brief, data contract, production route, or evidence-backed own-identity capability was authorized or implemented. Do not simulate repository authorship, approvals, external actions, or personhood.

## Coordination rule

Every agent must claim one HYB task in [agent-checkins.md](../history/coordination/agent-checkins.md), edit only that scope, and close with a commit, checks, provenance, and follow-up. Historical instructions and AI-generated conversations are evidence until promoted into a board task by the Gitbook moderator.

For current branch evidence and the exact 2026-10-14 scope, see the Gitbook #2 check-in comment and [TESSERA PR #372](https://github.com/vitalitychems-dot/TESSERA/pull/372). Do not mark it DONE before actual merge and current-head checks.
