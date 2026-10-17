# Consolidated TODO list

The authoritative work board is [HYBRID-CONSOLIDATION-BACKLOG.md](HYBRID-CONSOLIDATION-BACKLOG.md). This page summarizes it; it is not a second task queue.

## Current continuation — 2026-10-17

Exact implementation/validation/PR receipts are recorded in [the continuation receipt](../handoff/tessera-next-2026-10-14/CONTINUATION-2026-10-17.md). Earlier dated check-ins and status pages remain historical evidence and do not establish live external-agent sessions or current-head checks.

- **TESSERA #369 / HYB-025:** the owner merged PR #372 at `564811dc5f74073802e38c701ec98b4c32402bc3` on 2026-10-15. Its recorded merge-SHA CI, secret scan and provenance succeeded. No later merge or permanent deployment is claimed by this continuation.
- **HYB-013 / current runtime-shell successor:** the unfinished source patch was recovered into `manus/runtime-shell-recovery-20261017`, based on that merged main. It removes unused decorative theme/control assets, preserves feature routes and the session gate, defers chat's 3D renderer, fixes port validation, provides configured-model chat with honest disabled/error states, uses newest conversation context, and requires fresh isolated Cortex → Pen passes. Independent review found and the patch corrected cross-request batching and concurrent persistence risks. Exact final validation and PR status belong in the continuation receipt.
- **Database acceptance:** a new disposable loopback-only PostgreSQL cluster and dedicated database were created for this continuation. Application/production databases were not used. The final current-source DB-suite result is recorded separately; historic “DB suite skipped” statements must not be reused as current evidence.
- **Old PRs:** PR #361 remains OPEN/DIRTY and must not be merged as-is; it is a broad historical deletion proposal, not the current narrow successor. PR #367 is closed unmerged; no live Replit workspace was imported.
- **HYB-015:** six compact canonical-source topic entry points plus a shared provenance index now exist under [topics](../topics/README.md), with SUMMARY navigation. No archived instruction block was replayed. Documentation review/merge remains pending.
- **HYB-016:** current nonoverlapping Manus claims and evidence-based status reconciliation are recorded in [agent check-ins](../history/coordination/agent-checkins.md). External Replit/Cursor/Grok/bot sessions were not contacted or represented as newly coordinated.
- **HYB-010 / HYB-011:** BLOCKED for missing authorized source/ref metadata and media-rights/privacy-owner decisions. Protected bodies remain unopened; historical root-name observations do not complete item-level source/privacy review.
- **HYB-026:** BLOCKED for queue CODEOWNER `@collink1007` or designated-owner diagnosis/authorization. The prior five failing protected gate assertions are reported evidence, not a new reproduction or a proven fixture-vs-implementation diagnosis. No `mesh/queue/` code changed.
- **HYB-027:** BLOCKED for protected JSON-scan owner `@collink1007` or designated owner's provenance-safe policy. Before this docs update, PR #123 head `e6879eb83e1f11771d4da6720c1032e95d36ec4b` failed [CI run 38722033226](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38722033226). This update needs a fresh exact-head check. No excluded artifact was opened, altered, copied, deleted, transferred, or ignored; validation is not suppressed.
- **HYB-028:** BLOCKED until the owner names the exact authorized destination repository and approves the Vitality-related scope. No such destination/transfer is supplied by this continuation.
- **HYB-018:** repository deletion remains BLOCKED for fresh exact coverage and explicit final approval for each named repository. Nothing was deleted.
- **HYB-023 / permanent site:** BLOCKED for an exact approved existing full-stack host/project and release/secret/database/security/monitoring/rollback target. No active managed project or connected approved host was found; no replica or new host was created, no deployment or payment performed, and no previously refused connector proposal repeated.
- **HYB-022 / own-brain:** recorded Phase 1 local evidence remains separate from product release and later learning/memory/scale phases. The two-pass configured-model patch does not complete those later phases or prove consciousness.
- **GLM-5:** [audit follow-ups](../brain-consciousness/GLM5-AUDIT-FOLLOWUPS.md) still require the exact model/revision/license, authorized endpoint verification, bounded comparative evaluation, and explicit live-instrument owner decision. Offline adapter tests are not deployed-provider verification.
- **PEN-SCOPE / identity:** the configured-model adapter and honest identity fallback do not establish a separate authorized product brief, evidence-backed original identity, personal memory, or autonomous repository authority. Those product/provenance decisions remain open.

## Repository and source boundaries

TESSERA remains the application; Gitbook remains coordination/provenance; GitMesh remains a separate public/manual proposal room. GitMesh main is `602d6559c7d3d912e8cc5b43914d1193700c02b0`; its direct-main source-sync helper was not run or imported. The Box backup main snapshot remains `46baaf7d87e41ee89555c61617a8e31c1d35bdc9`; two deployment records do not prove an approved Tessera release or safe content migration.

The Box index has 455 historical metadata rows with 21 names withheld. Prior safe-screened items, duplicate groups, and a handful of exact-byte matches are partial evidence, not full per-row certification or authorization to move/delete material. No bundle, WIP replay, backup transfer, or Box deletion occurred.

The auxiliary repositories `Gitai`, `1`, `2`, `3`, `4`, and `5` currently return GitHub HTTP 409 “Git Repository is empty” for commits. They supply no source commits to integrate; they were not populated, renamed, or deleted. A configured repository selection is not a deployment target.

Private Drive, Grok, Replit, Cursor and bot source/log coverage remains bounded by actual authorized access/export. The [external-source inventory](../handoff/tessera-next-2026-10-14/EXTERNAL-SOURCE-INVENTORY.md) records the requirements. Historical claims or unavailable exports were not authenticated as current capability or original identity.

## Historical decisions retained

- HYB-005's narrow accepted audit advisory and 2026-11-05 review/removal condition remain at [the original decision](../merge/hyb-005-braces-decision.md); a clean audit under repository policy is not proof that the accepted advisory no longer exists.
- HYB-008 and HYB-017 remain rejected for Tessera; no separate archive authentication/database or storefront checkout was imported.
- HYB-009 remains archive-family classification, not a fresh file-by-file re-review.
- HYB-012's eight non-quantum duplicates remain intentionally retained. Existing reviewed foundation merges and their immutable receipts remain history.

See [Gitbook issue #124](https://github.com/vitalitychems-dot/Gitbook/issues/124), the [handoff index](../handoff/tessera-next-2026-10-14/INDEX.md), and the authoritative board for the next owner decision. An implementation can be locally tested and proposed without being merged, released, permanently hosted, or fully source-certified.
