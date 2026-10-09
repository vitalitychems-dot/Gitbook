# Agent check-ins

This ledger is the coordination lock for the [hybrid consolidation backlog](../../intake/HYBRID-CONSOLIDATION-BACKLOG.md). One task has one active owner. Agents must claim before editing and close with a commit, checks, provenance, and follow-up.

## Active claims

### HYB-013 — coordinated claim proposal

```text
TASK: HYB-013
AGENT: Copilot Chat Assistant (GitHub user: vitalitychems-dot; coordinating under the Gitbook mesh lane with no overlap with any current active owner)
SCOPE: Gitbook review of historical UI flow candidates and TESSERA candidate flow recovery; no direct product code edit until a scoped acceptance test and owner approval are recorded
START: 2026-10-07T00:00:00Z
BASE: TESSERA main@a024d83f90fb1bfe9ca82a5b5cc4a435df91a422; Gitbook main@372cf1e4a0c4cbfa413b748be9e1de4e7ae505a1
STATUS: IN REVIEW
NEXT CHECK-IN: 2026-10-07T02:00:00Z
BLOCKER: none
```

This claim is intentionally scoped to a Gitbook review and design pass only. It does not overlap with any currently recorded active HYB task in the ledger and it preserves the one-task/one-owner rule while enabling collaboration through the issue thread and the Gitbook moderator review.

## Completion record — HYB-021 (2026-10-09)

The earlier active block said TESSERA pull request 20 and Gitbook pull request 17 were still open. Both are merged. Cursor refreshed this record. No TESSERA source was edited.

```text
TASK: HYB-021
AGENT: Replit Agent via the owner-authorized GitHub connection
STATUS: DONE
COMMIT: TESSERA merge 9e218bc27a4503f5d2e71162da636bd890ee6315 (pull request 20, merged 2026-10-08T03:43:59Z). Gitbook merge 39e892e6557d79c7536c2aa3f27aaf844423eb62 (pull request 17, merged 2026-10-08T03:44:05Z).
CHECKS: TESSERA main artifacts/tessera/package.json has katex ^0.19.0. Actions run 37713667003 was recorded on the pull request head before the merge. This refresh did not re-run that workflow.
CHANGED: history/coordination/agent-checkins.md and the HYB-021 row in intake/HYBRID-CONSOLIDATION-BACKLOG.md.
FOLLOW-UP: none for the KaTeX range.
```

## Completion record — HYB-014 (2026-10-09)

```text
TASK: HYB-014
AGENT: Manus release steward
STATUS: DONE
COMMIT: TESSERA merge commit 5628e4222cfa4e1fb3b5f9ac6f11af5654aaeeee (PR #63)
CHECKS: pnpm --filter @workspace/scripts test (15 passed); pnpm run merge-gate (clean); pnpm run merge-gate:full (exit 0); GitHub Actions run 37898916804 succeeded on the PR head.
CHANGED: TESSERA scripts/historical-merge-gate.mjs, scripts/historical-merge-gate.test.mjs, package.json, README.md, .github/workflows/ci.yml; Gitbook review/validation.md, intake/HYBRID-CONSOLIDATION-BACKLOG.md, history/coordination/agent-checkins.md.
FOLLOW-UP: HYB-016 to refresh stale task check-ins, including merged Replit HYB-021.
```

## HYB-012 — preserved claim text

Decision-time STATUS inside the blocks below remains IN REVIEW. Current status is DONE (`50876d40`).

## HYB-020 / repository routing — completion record (2026-10-07)

```text
TASK: HYB-020
AGENT: Manus consolidation coordinator
SCOPE: Gitbook merge/ALL-REPOSITORIES-ROUTING-2026-10-07.md; mesh/CODEBASE-MEMORY-MCP.md; intake/HYBRID-CONSOLIDATION-BACKLOG.md; SUMMARY.md; local CBM graph artifacts in TESSERA and Gitbook
START: 2026-10-07T22:49:00Z
BASE: Gitbook cfaba85; TESSERA 8ca8fb2
STATUS: DONE
BLOCKER: none
CHECKS: codebase-memory-mcp 0.11.0 installed; TESSERA indexed with 20,742 nodes and 54,278 edges (58 partial parses, 16 intentional exclusions, 0 unusable); Gitbook indexed with 1,236 nodes and 1,361 edges (0 partial, 0 unusable); account repository list routed without opening protected 1T contents; no source repository deleted.
CHANGED: Gitbook routing record, Codebase Memory bridge contract, backlog HYB-020 row, SUMMARY navigation, local .codebase-memory artifacts for both destinations
FOLLOW-UP: HYB-014 for a reviewed historical-merge refresh/check command; HYB-008/HYB-013 for selective feature recovery; owner digest approval applies only to this scoped publication
```

The routing pass accounts for current account repositories without claiming that every historical byte belongs in TESSERA. Unrelated `Run-Z-app` repositories are recorded as outside Tessera scope; `1T` remains protected and uninspected; archives and generated/runtime data remain at their sources. Agents must use the routing record before opening a new recovery task.
