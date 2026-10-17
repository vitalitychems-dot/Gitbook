

## Latest synchronization refresh — 2026-10-15 10:34 UTC

This update supersedes the earlier table for current-status decisions; the original table remains a dated 07:07 UTC snapshot.

| Repository / source | Current exact state | Synchronization status | Next safe action |
|---|---|---|---|
| TESSERA | `main` `564811dc5f74073802e38c701ec98b4c32402bc3`. PR #372 merged by `vitalitychems-dot` at 10:25:58Z; merge-commit CI, secret scan, and provenance runs succeeded. PR #367 closed unmerged at 10:26:01Z. PR #361 open at `e8beb40086cb91dbe2c2ee59fc57ee8cd5b68f45`, base `00d6dc7ad7b5ebf390ed33345b28c698b89d2056`, conflicting, no review decision. | PR #372 is merged; app remains undeployed. PR #361 is a conflicting broad-deletion proposal with active UI/preview paths and is not safe to merge as-is. | Reconcile the UI retirement request against the full-stack objective; review PR #361 on current base and require exact consumer/dependency, restoration, and test evidence before any deletion. |
| Gitbook | `main` `17cdbdbae3e98001cca1b2365b834ab10431ac54`. PR #123 was last checked at `4a9e68ef860a1ab2bf4e713eccffea1b7e5790a4`, with exact-head run 38698025357 failing JSON validation. This docs-only follow-up advances that PR branch. | Handoff update remains a PR proposal; no merge or CI-green evidence for the new commit yet. | Check the exact pushed head, retain the failed protected JSON gate, obtain its owner’s decision, then use normal review/merge only after checks pass. Issue #124 is the live checklist. |
| GitMesh | `main` `602d6559c7d3d912e8cc5b43914d1193700c02b0`. | Standalone public proposal/manual intake surface. The two-commit README/hidden-input update was reviewed as a path-limited diff only; the external Replit regression harness was not accessed or run. Direct-to-main source sync was not executed. | Keep isolated; use PR/check/review for future changes and do not integrate the source-sync helper into TESSERA. |
| Box backup | `files` `46baaf7d87e41ee89555c61617a8e31c1d35bdc9`. | Unchanged, metadata-only review. No file deletion, content replay, or transfer occurred. | Retain until candidate-specific provenance, consumer, rollback, retention, and explicit owner decisions are complete. |
| Replit / other external agents | No authenticated Replit session or connector. The first supplied invite URL redirected to login; user reports login failure; other supplied invites were not tested. | Source intake remains blocked; PR #367 closure is not proof of project access. Grok/Cursor/bot workspaces remain unverified. | Obtain read-only exports/repository snapshots and provenance; do not ask for credentials or post invite tokens. |
| Hosting | No selected production host, project, URL, or rollback target verified. | No permanent deployment is evidenced. | Require exact authorized full-stack host/project/database/domain/secret-store target and release validation. |

Gitbook is the cross-agent record; this matrix does not authorize direct writes to default branches, repository/file deletion, source replay, credential transfer, or deployment. Vitality-related content remains excluded without an exact authorized destination and scope.
