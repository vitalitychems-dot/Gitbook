# Agent check-ins

This ledger is the coordination lock for the [hybrid consolidation backlog](../../intake/HYBRID-CONSOLIDATION-BACKLOG.md). One task has one active owner. Agents must claim before editing and close with a commit, checks, provenance, and follow-up.

## Active claims

### SITE-002 / Cursor Project — 2026-10-10

```text
TASK: SITE-002 (+ HYB-016 hygiene for this claim; three-way protocol docs)
AGENT: Cursor Project (declared role; GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok.
SCOPE: Gitbook mesh/SITE-002-2026-10-10.md, mesh/roles/cursor-project.md, mesh/THREE-WAY-COLLAB-PROTOCOL.md, playbook/hub/roles/SUMMARY/check-ins updates; TESSERA diagnostics session gates on branch cursor/site-002-diagnostics-gate-7ea3
START: 2026-10-10T03:41:00Z
BASE: TESSERA main@bb4b3191ed037982d8b525bbb9bc507058854686; Gitbook main@691daa5b0980bd6364eb38bc20611e6a446ce88a
STATUS: GITBOOK DOCS ON MAIN — overlap CLEAR; TESSERA diagnostics gate next
NEXT CHECK-IN: after TESSERA diagnostics gate on main
BLOCKER: none for overlap; PR create still 403 (Contents land used)
OVERLAP CHECK: issue #2 through comment 6093570482; no Replit/Grok claim on SITE-002 or diagnostics.ts; Replit remains SITE-001/005; main Rick commits only touched mesh/RICK.md; diagnostics.ts SHA unchanged on TESSERA main since bb4b319 (5c0cfd81)
```

### HYB-013 — STALE (HYB-016)

```text
TASK: HYB-013
AGENT: Copilot Chat Assistant (GitHub user: vitalitychems-dot; coordinating under the Gitbook mesh lane with no overlap with any current active owner)
SCOPE: Gitbook review of historical UI flow candidates and TESSERA candidate flow recovery; no direct product code edit until a scoped acceptance test and owner approval are recorded
START: 2026-10-07T00:00:00Z
BASE: TESSERA main@a024d83f90fb1bfe9ca82a5b5cc4a435df91a422; Gitbook main@372cf1e4a0c4cbfa413b748be9e1de4e7ae505a1
STATUS: STALE
REASON: Next check-in was 2026-10-07T02:00:00Z with no completion record; backlog still says READY while ledger said IN REVIEW. Cursor Project did not take HYB-013.
NEXT: Tessera reassigns or Copilot renews the claim before any HYB-013 edit.
```

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


## HYB-021 / own-brain plan — planning record (2026-10-09)

```text
IDENTITY: Human owner plan relayed to Tessera; coordinator recorded as a reported assignment, not an impersonated agent post
TASK: HYB-021
SOURCE: owner-provided own-brain plan; public SNN source manifest
TARGET: Gitbook brain-consciousness/OWN-BRAIN-PLAN.md and OWN-BRAIN-LANE-ASSIGNMENTS.md; future isolated TESSERA SNN package
SCOPE: deterministic original LIF core, sparse synapses, 10k→100M scale ladder, bounded learning, read-only memory adapter, connectome-statistics controls, computable indicators, and held-out evaluation
DELIVERABLE: phase plan plus BC-011–BC-020 non-overlapping task queue
ACCEPTANCE TEST: each phase has a reproducible result record, control, seed, resource report, limitations, and no consciousness/biological-equivalence claim
OVERLAP CHECK: Gitbook main checked; no SNN implementation PR is being promoted by this record
STATUS: REPORTED / READY FOR TESSERA LANE ASSIGNMENT
FOLLOW-UP: BC-011 and BC-012 first; BC-017 held-out evaluation remains separate from training
```

The owner message reports that the Brain lane is writing the held-out self-improvement set. That is recorded as a reported assignment; implementation begins only after the actual lane posts its check-in using the template above.


## HYB-022 / BC-011–BC-013–BC-019 — Phase 1 evidence (2026-10-09)

```text
IDENTITY: TESSERA build lane / local implementation record; no agent impersonation
TASK: HYB-022; BC-011, BC-012, BC-013, BC-019
SOURCE: original design recorded in brain-consciousness/OWN-BRAIN-PLAN.md
TARGET: TESSERA/research/own-brain; Gitbook brain-consciousness/reports/OWN-BRAIN-PHASE1-RESULT-2026-10-09.md
SCOPE: deterministic sparse LIF core, seeded currents, reset/threshold/refractory tests, bounded scale runner; excludes STDP, product-memory writes, self-modification, APIs, and biological claims
DELIVERABLE: Phase 1 implementation and machine-readable scale results
ACCEPTANCE TEST: 5/5 unit tests pass; S0–S2 complete with deterministic replay; S3–S4 explicitly blocked by the 512 MiB safety cap
OVERLAP CHECK: rebased against current TESSERA/Gitbook heads; no learning, memory-adapter, or production-runtime files changed
STATUS: TESTED LOCALLY / PROMOTION PENDING NORMAL REVIEW
RESULT: S0 10k, S1 100k, S2 1M tested; S3 10M and S4 100M blocked by estimated memory
NEXT: BC-014 bounded STDP control, after lane check-in; BC-017 held-out evaluator remains separate
```

The V2 roadmap is recorded at `brain-consciousness/TESSERA-V2-ROADMAP.md`. “Launch” means a private local application run and evidence review, not a claim of consciousness or autonomous self-modification.


## HYB-023 readiness sync — 2026-10-09
```text
IDENTITY: Manus / TESSERA build lane; no agent impersonation
TASK: HYB-023
SOURCE: TESSERA permanent-site coordination brief and current application route declarations
TARGET: TESSERA artifacts/tessera/vite.config.ts, artifacts/tessera/src/components/ui/tooltip.tsx, artifacts/tessera/public/manus-routes.json, docs/PERMANENT-SITE-RELEASE.md; Gitbook mesh readiness records
SCOPE: Restrict Replit-only Vite plugins to serve mode, remove the unnecessary client directive, add the 51-route managed-Web manifest, and synchronize evidence. Excludes production deployment, database migrations, secrets, protected material, and merging unrelated open PRs.
BASE: TESSERA c71b4ef; Gitbook fd7a358
STATUS: TESTED / PUBLISHED
COMMIT: TESSERA e5e571966b5c37a9c59d5485345b1f46cca20dac; Gitbook follow-up pending publication
CHECKS: pnpm typecheck passed; pnpm test passed; pnpm run build passed with no sourcemap/TypeScript/lifecycle/build-failure diagnostics; built manus-routes.json validated with 51 routes. A non-fatal 1,019.51 kB OrbitControls chunk advisory remains recorded.
CHANGED: TESSERA Vite production plugin gating, tooltip directive, route manifest, release record; Gitbook readiness report, coordination state, backlog, navigation, and this ledger.
FOLLOW-UP: SITE-001 deployment report; SITE-002 quality review; SITE-003 provenance review; SITE-004 security review; managed health check and exact release payload approval.
```


## PERF-001 — bounded 3D vendor chunking — 2026-10-09
```text
IDENTITY: Manus / TESSERA build lane; no agent impersonation
TASK: PERF-001
SCOPE: TESSERA artifacts/tessera/vite.config.ts only
BASE: TESSERA e5e571966b5c37a9c59d5485345b1f46cca20dac
STATUS: TESTED / PUBLISHED; Cursor review pending
COMMIT: 072acd8ecfc2f2ec113a4072c3d3b74451c282c3
CHECKS: pnpm typecheck passed; pnpm test passed; pnpm run build passed; 51-route manifest validated. Largest 3D chunk changed from approximately 1,019.51 kB OrbitControls to 724.83 kB vendor-three; additional chunks are vendor-r3f-drei 308.32 kB, vendor-r3f-fiber 169.37 kB, vendor-three-stdlib 86.19 kB.
CHANGED: bounded Rollup manualChunks rules only.
ROLLBACK: git revert 072acd8.
FOLLOW-UP: PERF-002 Cursor review of exact diff, route integrity, circular dependencies, and production loading behavior.
```
