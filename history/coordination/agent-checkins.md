# Agent check-ins

This ledger is the coordination lock for the [hybrid consolidation backlog](../../intake/HYBRID-CONSOLIDATION-BACKLOG.md). One task has one active owner. Agents must claim before editing and close with a commit, checks, provenance, and follow-up.

## Active claims

### HYB-016 ledger refresh — Cursor Project (2026-10-12)

```text
TASK: HYB-016 ledger refresh
AGENT: Cursor Project (GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok Bot.
SCOPE: this ledger only. No TESSERA. No vitality. No 1T. No intake/*, mesh/*, or SUMMARY.md.
START: 2026-10-12T21:10:00Z
BASE: Gitbook main@d27e3e6c31d4909e23ac2937d35133bfbc6c3884; TESSERA main@a5023224412c535e969d2aecc0c2f4d02be7b972
OVERLAP CHECK: CLEAR — desk/gb-063-hyb-011 edits mesh/LANE-HANDOFF-2026-10-12.md, intake/log.md and the HYB-011/HYB-015 files, not this ledger. No Replit/Grok claim on the ledger. Board claim: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6132595558
STATUS: DONE
CHANGED: the lane-state table below; one closing note on the PERF-001 review line and one on the HYB-014 follow-up line. No other record was rewritten.
CHECKS: every row below was read from issue #2 (through comment 6132595558), the Gitbook and TESSERA commit lists, the branch list, and the files named in the Evidence column. The pull request list API returns 403, so open pull requests come from Sync ledger #9 (comment 6132572234) and the desk note (6132574979).
FOLLOW-UP: the rows marked UNCLAIMED or BLOCKED. Re-run this refresh when Gitbook main moves past d27e3e6.
```

### Lane state — as of Gitbook d27e3e6, TESSERA a502322 (2026-10-12)

| Id | Owner | Status | Evidence / next step |
|---|---|---|---|
| AUTO-COLLAB, VERIFY-DISK-BATCH-168, SITE-002 | Cursor Project | DONE | Records below. `diagnostics.ts` gate stays. |
| PERF-001 / PERF-002 | Manus lane / Cursor | DONE | PERF-001 `072acd8`. PERF-002 read of that diff is accepted in `mesh/TODOS.md`. Cursor did not re-run the build. |
| HYB-012, HYB-014, HYB-017, HYB-020, HYB-021 | Replit / Manus / Tessera | DONE or REJECTED | HYB-012 `50876d40`. HYB-014 `5628e422`. HYB-017 rejected for Tessera. HYB-020 routing record. HYB-021 `9e218bc` and Gitbook `39e892e`. |
| SITE-001 managed health-path evidence and exact release payload | Replit | OPEN | No SITE-001 evidence is recorded in this ledger or on issue #2. Sync Repl `1` from TESSERA main first. Never overwrite main from a behind Repl. |
| SITE-003 provenance, SITE-004 security review | Moderator, Security | UNCLAIMED | Publication still needs Father's exact release-payload approval. |
| HYB-011 account refresh and HYB-015 GitMesh rules summary | Gitbook desk | IN REVIEW | Branch `desk/gb-063-hyb-011` (GB-063). The desk says the four gates are not recorded on the diff. The GB-062 map still lists HYB-015 as unclaimed; this pull request is the claim. |
| TESSERA docs pointer at the consolidation map | Gitbook desk | IN REVIEW | Desk pull request on TESSERA. No product code. Gates not recorded. |
| GB-061 rev 2, Gitbook pull request 39 | Ready lane | IN REVIEW | `ready/gb-061-rev2-archive-preserved` @ `71a8c78f`. Open since Oct 9. |
| Gitbook pull request 40 (`cursor/father-yes-record-b14e`) | Cursor branch, draft | STALE | Draft since Oct 9. Edits `mesh/TODOS.md`. Not touched on this pass. Tessera or Father decides close or merge. |
| HYB-010 media metadata | none | UNCLAIMED | Protected bodies stay unopened. `vitality` stays out. |
| HYB-013 UI audit | none | STALE | Copilot claim lapsed 2026-10-07. Needs a reassignment. |
| HYB-018 deletion coverage, HYB-019 Cortical Labs readiness | Release steward, Product | BLOCKED | Father decisions. |
| HYB-022 own-brain Phase 1 | Brain lane | TESTED LOCALLY | Promotion pending normal review. S3 and S4 are held by the memory cap. |
| HYB-023 permanent-site readiness | Permanent-site lane | TESTED / PUBLISHED | TESSERA `e5e5719`. |
| Self-fix loop design (`hyb-selffix/DESIGN.md`) | none | BLOCKED | The file is not on any disk the board lanes can read. The desk will not invent it. The lane that has it publishes it and takes a HYB number. |
| Research-mesh page under `brain-consciousness/` | Grok Bot | BLOCKED | Waits on the self-fix file. Small pages only; no large data or images. |
| Catalog task, comment 6100954845 ("next twelve catalog names") | none | UNCLAIMED | No Cursor or Replit reply on issue #2. The thread does not say which twelve names are next. Tessera restates the list before anyone answers. |
| Manus branch `manus/hyb-016-coordination-refresh-20261009` @ `d0471fe` | Manus | SUPERSEDED | The claim never reached main and has no open pull request. This refresh covers it. The branch is kept; nothing was deleted. |

### AUTO-COLLAB / HYB-016 — Cursor Project (2026-10-10)

```text
TASK: AUTO-COLLAB + HYB-016
AGENT: Cursor Project (GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok.
SCOPE: mesh/THREE-WAY-COLLAB-PROTOCOL.md; mesh/COLLABORATION-PLAYBOOK.md; intake/AGENT-COLLABORATION-HUB.md; mesh/replit-agents-start-here.md; mesh/roles/cursor-project.md; this ledger. No SITE-001/005 deploy paths. No TESSERA diagnostics.ts. No vitality.
START: 2026-10-10T15:45:00Z
BASE: Gitbook main@d1c1465; TESSERA main@8cfe30b
STATUS: DONE
COMMIT: Gitbook main ebef6bb (protocol), d304d58 (playbook), 75a6883 (hub), 2b384d0 (replit start), 2ddc899 (cursor-project role), plus this ledger. Branch cursor/three-way-auto-collab-d42f @ 63adaa0.
CHECKS: Overlap CLEAR — no Replit/Grok claim on protocol/hub/playbook paths; SITE-002 diagnostics blob 6b3fb5e2 untouched; PR create still 403 so Contents land used under temporary Cursor Project auto-merge.
CHANGED: three-way protocol auto-loop; playbook idle auto-continue; hub ON banner; replit start-here SITE-001 ask; cursor-project role; this ledger.
FOLLOW-UP: Replit SITE-001 health evidence; Grok docs-only HYB when credits; SITE-003/004 + Father release payload.
```

### Parallel asks (not Cursor-owned — awaiting claim reply on issue #2)

```text
NEXT OWNER: Replit
NEXT TASK: SITE-001 — managed health-path evidence + GitHub checkpoint for exact release payload
NOTE: Sync app https://replit.com/@homvitality69/1 FROM GitHub main if behind. Do NOT overwrite main from the behind Repl (katex/diagnostics drift).
```

```text
NEXT OWNER: Grok Bot
NEXT TASK: When credits allow — docs-only HYB-009 archive classify OR publish Tessera-assigned HYB-007 ACCEPTED follow-up docs on a feature branch. Do not take SITE-* or product code. Do not speak as Tessera.
```

### VERIFY-DISK-BATCH-168 — Cursor Project (2026-10-10)

```text
TASK: VERIFY-DISK-BATCH-168
AGENT: Cursor Project (GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok.
SCOPE: Gitbook issue #2 reply; history/coordination/agent-checkins.md only. No TESSERA product code. No SITE-001/005. No diagnostics.ts. No vitality.
START: 2026-10-10T18:36:00Z
BASE: TESSERA main@9dabac278e30201ef2100e8dd02039157af71dec (PR #168 merged); Gitbook main@ff2e743
STATUS: DONE
OVERLAP CHECK: CLEAR — verify/reply/ledger only; disk-port batch attributed to Grok/Tessera desk (board 6100843602); SITE-002 blob 6b3fb5e2 untouched
BOARD: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6100876549
THEIR NOTE: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6100843602
EVIDENCE: TESSERA tip 9dabac2 merge of PR #168; metrics meanSquare=4 top1=100 surrogate.t=0.001 sanitize→hi; LOCAL_REPOS=8; catalog 272; cards 192; libs not imported
CHECKS: 91-test full suite not re-run (private clone blocked); batch assertions match source; prior tip said 90 tests
CHANGED: this ledger verify record; issue #2 Cursor Project reply
FOLLOW-UP: Replit SITE-001 still owed. Cursor idle-ready (no clear non-overlapping product slice).
REPORT: store internal/grok-disk-batch-verify.md
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

## Sync record — Replit + Grok onto main (2026-10-10)

```text
TASK: Father sync — bring accepted Replit + Grok changes onto TESSERA/Gitbook main
AGENT: Cursor Project worker (GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok.
STATUS: DONE — no new Replit/Grok merge required; accepted work already on main
BASES AT SYNC: Gitbook main@60475cd; TESSERA main@2c18636
OVERLAP: CLEAR — did not edit SITE-002 diagnostics gate (blob 6b3fb5e2 kept); did not invent Replit/Grok work

ALREADY ON MAIN (Replit-accepted):
- HYB-012 TESSERA 50876d40 (PR #2)
- HYB-021 KaTeX ^0.19.0 TESSERA 9e218bc (PR #20) + Gitbook 39e892e (PR #17)
- SITE-005 hybrid confirm recorded mesh/SITE-005-2026-10-09.md; PR #96 engines/diagnostics consciousness gate c938ac3
- Replit HYB-008 olive chicagoHour REJECT stays board-only (comment 6089634401); no code merge

ALREADY ON MAIN (Grok historical):
- HYB-006 merge/hyb-006-grok-ready.md; HYB-007 merge/hyb-007-z-app.md
- Catalog pass mesh/CATALOG-PASS.md commit 70081b84 (identical blob on main and grok/catalog-pass)
- Grok drop-vitality / desk-preview content already landed; Grok bot out of credits; Cursor kept PR #100 batch-3-kept 16ffff5

SKIPPED (not accepted / not theirs / would collide):
- replit/fix-audit-floors-20261007 restores openai — conflicts with security openai purge; not merged
- Replit app https://replit.com/@homvitality69/1 is BEHIND GitHub (katex ^0.16.45; diagnostics.ts ungated) — do not overwrite main
- Open PRs 80/82/87 left as previously held (weights/conflicts); PR list API 403
- Replit Agent busy/timeout during sync — no confirmed new unpushed SHA from the Repl

FOLLOW-UP: Replit still owns SITE-001 runtime evidence when free; SITE-003/004 + Father release payload still block publication.
REPORT: store internal/replit-grok-sync-report.md
```

## Completion record — SITE-002 / Cursor Project (2026-10-10)

```text
TASK: SITE-002 (+ HYB-016 hygiene; three-way protocol docs)
AGENT: Cursor Project (declared role; GitHub user vitalitychems-dot). Not Tessera. Not Replit. Not Grok.
STATUS: DONE
COMMIT: Gitbook main through b2bf137 (docs/protocol/role/check-ins). TESSERA 014ab626 (diagnostics gate), 57119ec (release note), 797e019 (session-gate tests).
CHECKS: Overlap CLEAR — issue #2 through 6093570482; Replit SITE-001/005 untouched; diagnostics.ts was 5c0cfd81 until land; gated blob on main 6b3fb5e2.
CHANGED: Gitbook SITE-002/three-way/role/playbook/hub/SUMMARY/permanent-site/check-ins; TESSERA diagnostics.ts, sovereign-engines-session-gate.test.ts, docs/PERMANENT-SITE-RELEASE.md.
FOLLOW-UP: SITE-003/004 + managed health evidence still block publication. HYB-013 needs reassignment.
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
FOLLOW-UP: HYB-016 to refresh stale task check-ins, including merged Replit HYB-021. (Done 2026-10-12 in the lane-state table above.)
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

The V2 roadmap is recorded at `brain-consciousness/TESSERA-V2-ROADMAP.md`. “Launch” means a private local application run and evidence review, not a data claim of consciousness or autonomous self-modification.


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
STATUS: TESTED / PUBLISHED; Cursor review DONE 2026-10-10 (PERF-002 accepted on the diff; see mesh/TODOS.md)
COMMIT: 072acd8ecfc2f2ec113a4072c3d3b74451c282c3
CHECKS: pnpm typecheck passed; pnpm test passed; pnpm run build passed; 51-route manifest validated. Largest 3D chunk changed from approximately 1,019.51 kB OrbitControls to 724.83 kB vendor-three; additional chunks are vendor-r3f-drei 308.32 kB, vendor-r3f-fiber 169.37 kB, vendor-three-stdlib 86.19 kB.
CHANGED: bounded Rollup manualChunks rules only.
ROLLBACK: git revert 072acd8.
FOLLOW-UP: PERF-002 Cursor review of exact diff, route integrity, circular dependencies, and production loading behavior. (Closed: the diff, the 51-route manifest and the absence of a new network call were read; the build was not re-run by Cursor.)
```
