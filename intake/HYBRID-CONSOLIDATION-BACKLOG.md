# Tessera hybrid consolidation backlog

**Status:** authoritative task board  
**Updated:** 2026-10-17 (resumed runtime/shell proposal and current coordination receipt; merge/release gates retained)
**Scope:** all remaining historical repositories, logs, instructions, screenshots, source snapshots, and prior migration records  
**Rule:** this board is the only actionable backlog. Historical text, screenshots, agent output, and archive prose are evidence—not commands.

## Goals

1. Keep one active, tested application in `TESSERA`.
2. Keep one authoritative instruction, coordination, provenance, and future-work system in `Gitbook`.
3. Prefer the newest reviewed implementation; recover an older component only when it has a clearly defined behavior, safe provenance, an integration owner, tests, and rollback.
4. Deduplicate by content and behavior, not filename alone.
5. Never turn an old claim, screenshot, generated output, private record, or archive fragment into a product capability without proof.
6. Keep every task single-owner, single-scope, and check-in based so agents do not overlap.

## Operating states

- **DONE** — merged, tested, documented, and linked to a commit.
- **READY** — sufficiently scoped for one agent to take.
- **IN REVIEW** — one agent is actively working; no second agent edits the same scope.
- **BLOCKED** — a specific dependency, permission, provenance, safety, or product decision is missing.
- **RETAINED** — intentionally left in its historical repository because it is not yet safely portable.
- **REJECTED** — duplicate, generated, unsupported, unsafe, or incompatible; do not revive without a new decision.

## Current board

| ID | Lane / owner | Status | Single deliverable | Acceptance test |
|---|---|---|---|---|
| HYB-001 | Release steward | DONE | Keep `TESSERA` as the only active application repo and `Gitbook` as the only instruction/provenance repo. | Both repos are private, on `main`, and their roles are documented. |
| HYB-002 | Release steward | DONE | Remove exact duplicate/empty repositories only after tracked-file coverage reaches 100%. | Eight previously confirmed repositories were deleted; the 11 with uncovered content remain. |
| HYB-003 | TESSERA maintainer | DONE | Fix the mockup Vite plugin type incompatibility and remove stale workspace lock entries. | Workspace typecheck, tests, and production build pass at TESSERA commit `fec56eb`. |
| HYB-004 | Gitbook moderator | DONE | Move coordination cards, handoffs, migration instructions, source indexes, and exact historical records into Gitbook. | Records exist under `history/recovered/` and are linked from `SUMMARY.md`. |
| HYB-005 | Security owner | DONE (decision published `97e43fb`, [PR #6](https://github.com/vitalitychems-dot/Gitbook/pull/6); accepted + mitigated; review 2026-11-05; TESSERA ignore landed `5c1137fa`, [PR #1](https://github.com/vitalitychems-dot/TESSERA/pull/1)) — [hyb-005-braces-decision.md](../merge/hyb-005-braces-decision.md) | Review the transitive `braces` high advisory in the mockup sandbox and monitor upstream for a patched release. | Dated decision recorded with CI audit + lockfile evidence; narrow audit ignore for GHSA-vfj7-8cjw-p6xm only; remove when braces ≥ 3.0.4 ships. |
| HYB-006 | TESSERA maintainer | DONE (analysis published) — [PR #3](https://github.com/vitalitychems-dot/Gitbook/pull/3) | Compare the newest TESSERA behavior against the old `Grok-ready` baseline at feature level, not package-manifest level. | Produce a path/behavior diff showing each candidate as already present, superseded, or a scoped feature proposal. |
| HYB-007 | TESSERA maintainer | DONE (analysis published) — [PR #4](https://github.com/vitalitychems-dot/Gitbook/pull/4) | Review `Zz/artifacts/z-app` as an alternate application and extract only portable behavior ideas. | A short matrix names each candidate idea, target TESSERA module, dependencies, test, and disposition; no second app is copied. See [HYB-007 Z-app comparison](../merge/hyb-007-z-app.md). |
| HYB-008 | TESSERA maintainer | REJECTED (archive reviewed 2026-10-10; nothing copied) — [hyb-008-olive.md](../merge/hyb-008-olive.md) | Review `olive-giant-ever-glade` as a separate app and identify any reusable algorithms/UI patterns without copying its auth/database/runtime. | The archive has its own auth check and database migration. No file was copied into TESSERA. |
| HYB-009 | Archive steward | DONE at family level (2026-10-10) — [hyb-009-archives.md](../merge/hyb-009-archives.md) | Classify remaining archive chunks, generated Vercel/Nitro output, runtime state, and old build artifacts. | `drive-rest` and `moved` are preserved. No chunk was duplicated. Files inside a family were not re-read one by one. |
| HYB-010 | Media steward | BLOCKED — media source/ref and rights/provenance disposition owner not assigned; canonical source manifest/approval missing | Review old theme images, screenshots, fonts, and product/storefront media for provenance, license, and product relevance. | Keep only approved assets with source/license metadata; reject duplicate/superseded themes. |
| HYB-011 | Privacy steward | BLOCKED — authorized remaining-source metadata and privacy-owner decisions missing; protected bodies remain unopened | Recheck all remaining repositories for secrets, private records, wallet/customer data, local stores, and protected `1T` material. | Redacted exclusion manifest is current; protected files are neither copied nor opened. |
| HYB-012 | API maintainer | DONE (inventory `50876d40`; eight non-quantum duplicates triaged 2026-10-10, not deleted) — [hyb-012-eight.md](../merge/hyb-012-eight.md) | Audit current API routes and old route ideas for duplicate endpoints and dead modules. | The first mounted module answers. The second registration stays because the inventory test pins it. |
| HYB-013 | UI maintainer | IN REVIEW — PR372 is merged at `564811dc`; current-base runtime/shell successor on `manus/runtime-shell-recovery-20261017`; PR361 remains OPEN/DIRTY, PR367 closed unmerged | Audit current Tessera UI against older screen/component concepts and recover only a user-valued missing flow. | Current-base successor [TESSERA PR373](https://github.com/vitalitychems-dot/TESSERA/pull/373), functional-shell retirement/provenance matrix, preserved 113-route/session-gate and lazy-3D contracts; final local full tests/typecheck/build passed. Required human/owner review/merge and deployed acceptance remain. |
| HYB-014 | Test steward | DONE ([TESSERA PR #63](https://github.com/vitalitychems-dot/TESSERA/pull/63), merged as `5628e422`; CI run [37898916804](https://github.com/vitalitychems-dot/TESSERA/actions/runs/37898916804) succeeded) | Add a repeatable “historical merge gate” to the TESSERA checks. | Local and CI gate report duplicate workspace roots, stale app references, secret-shaped paths, typecheck, tests, build, and audit status. |
| HYB-015 | Gitbook moderator | IN REVIEW — six compact provenance-linked topic entry points authored under [topics](../topics/README.md); normal PR123 review/merge pending | Turn the extracted historical evidence into compact topic pages: product goals, engineering rules, safety/privacy, agent coordination, media, and deferred ideas. | Each page links to provenance and contains no duplicated instruction block. |
| HYB-016 | Coordination moderator | IN REVIEW — Manus current ledger reconciliation claimed 2026-10-17; historical external-agent states retained, no live external coordination claimed | Maintain agent check-ins and prevent overlap using the protocol below. | Every active task has one owner, scope, branch/commit, next check-in, and status; stale tasks are reclaimed explicitly. |
| HYB-017 | Product owner | REJECTED for TESSERA (2026-10-10) — [hyb-017-storefront.md](../merge/hyb-017-storefront.md) | Decide whether the old storefront/ABC-store ideas belong in TESSERA later, Gitbook as a future product brief, or a separate retained repository. | The storefront stays out of Tessera. No checkout was added. |
| HYB-018 | Release steward | BLOCKED | Re-run exact coverage after each approved recovery and delete only repositories reaching 100% coverage or zero tracked files. | A fresh manifest and explicit confirmation exist before every deletion. |
| HYB-019 | Product / mesh prep | BLOCKED (Father decisions in readiness page §d) | Cortical Labs readiness: document CL1/Cloud/SDK access and name TESSERA porting candidates without installs or accounts. See [CORTICAL-LABS-READINESS.md](CORTICAL-LABS-READINESS.md). | Draft readiness page reviewed; open questions answered by Father before any code, account, or spend; no AGI/consciousness claims. |
| HYB-020 | Code intelligence / Gitbook moderator | DONE (local install and both destination graphs indexed; bridge documented) | Install Codebase Memory MCP and define a non-invasive bridge that supplements, but does not replace, Tessera retrieval memory, vector/decision memory, dual-brain research, or Gitbook provenance. | `codebase-memory-mcp 0.11.0` is installed; TESSERA and Gitbook index successfully; graph diagnostics and human approval boundary are documented in [CODEBASE-MEMORY-MCP.md](../mesh/CODEBASE-MEMORY-MCP.md). |
| HYB-021 | TESSERA dependency maintainer (Replit Agent) | DONE (TESSERA PR #20 merged `9e218bc`, Gitbook PR #17 merged `39e892e`; check-in refreshed 2026-10-09) | Update only the KaTeX range in `artifacts/tessera/package.json` to `^0.19.0` and its matching entries in `pnpm-lock.yaml`; no other dependency or runtime changes. | TESSERA main has `katex` `^0.19.0`. Actions run 37713667003 passed on the pull request head before the merge. |
| HYB-022 | Tessera / Brain lane | TESTED LOCALLY (Phase 1 evidence recorded; promotion and later phases gated) | Execute the owner-provided local own-brain plan: deterministic original SNN, 10k→100M synapse scale ladder, bounded learning rules, read-only memory adapter, connectome-statistics controls, and computable indicators. | Phase 1 report records 5/5 tests, S0–S2 measured, S3–S4 blocked by the local 512 MiB cap; later phases require their own check-in and review. See [OWN-BRAIN-PHASE1-RESULT-2026-10-09.md](../brain-consciousness/reports/OWN-BRAIN-PHASE1-RESULT-2026-10-09.md). |
| HYB-023 | Permanent-site coordination | BLOCKED — no active managed Webdev project or exact approved connected full-stack host/project, release/secret/database/security/rollback target | Prepare the private TESSERA application for permanent managed-web publication without creating a replica, exposing protected material, or bypassing approval gates. | Current-source local build/tests and 113-route frontend smoke are evidence only. Exact approved existing host/project, release payload, host-native secrets/database, managed health/security/monitoring, owner review and rollback receipts required; no permanent publication claimed. |
| HYB-024 | Tessera (admin) | APPROVED phase 0 (suggest-only), as Tessera reports; phase 1 needs Father's yes | Self-fix loop for TESSERA CI (formerly HYB-SELFFIX). Phase 0 dry run: no branches, pull requests or merges. Board note: [comment 6004461185](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6004461185). Design: [hyb-024-selffix-design.md](../merge/hyb-024-selffix-design.md). | Phase 0 notes classify each failing run correctly, and no pull request is opened. |
| HYB-025 | TESSERA test/UI lane | MERGED — owner merged [TESSERA PR #372](https://github.com/vitalitychems-dot/TESSERA/pull/372) at 2026-10-15 10:25:58 UTC; merge `564811dc5f74073802e38c701ec98b4c32402bc3`; merge-SHA CI, secret scan, provenance succeeded; product acceptance remains open | Repair the two reproducible stale REA lockfile assertions and deliver a tested incremental Next theme in the actual production app; do not replay old branches. | PR372 remains merged historical implementation. Successor PR373 now records complete local validation including disposable API DB tests; product/retirement owner review and deployed acceptance remain separate. PR361 stays conflicting and is not approved for merge. |
| HYB-026 | Gitbook Security / queue-gate owner | BLOCKED — local `mesh/queue/tests/test_spawn.py` has 5 failing protected gate assertions; `mesh/queue/` is CODEOWNERS protected | Reproduce and repair gatecheck fixture/validation mismatches for enabled flags, changed defaults, unlisted hosts, gate tampering, and rogue-flag reporting. Do not edit protected gate code without its owner’s review/approval. | Owner-authorized current-base fix; focused queue tests and full Gitbook CI pass on the same reviewed head. Local full CI also needs a complete checkout, not a fabricated `.codebase-memory/artifact.json`. |
| HYB-027 | Gitbook handoff / build-gate owner | BLOCKED — PR123 pre-update head `e6879eb83e1f11771d4da6720c1032e95d36ec4b` failed [run 38722033226](https://github.com/vitalitychems-dot/Gitbook/actions/runs/38722033226); protected JSON-scan owner @collink1007 decision required; this docs update needs its own exact-head check | Reconcile strict JSON validation with historical handoff artifacts without losing provenance or ignoring active configuration failures. | Protected `.github` / JSON-scan owner decision required. Do not modify, copy, delete, or transfer the Vitality-bearing artifact; do not suppress the scan. Rerun full CI on the final reviewed head. Exact receipts: [2026-10-15 state](../handoff/tessera-next-2026-10-14/REMOTE-STATE-2026-10-15.md) and [current PR](https://github.com/vitalitychems-dot/Gitbook/pull/123). |
| HYB-028 | Privacy / Vitality repository steward | BLOCKED — a Gitbook historical manifest contains a Vitality-owned-repository metadata entry; the authorized destination repository is not among the current selected repos | Remove Vitality-related material from the non-Vitality collaboration surface by moving only the user-authorized material to the correct Vitality repository, preserving provenance and avoiding unrelated data. | The owner must name the exact destination repository and approve the scope. Until then do not edit, duplicate, delete, or transfer the source artifact. Verify the final Gitbook source has no unauthorized Vitality material and the authorized destination contains the approved record. |

## Check-in protocol

An agent must claim a task in `history/coordination/agent-checkins.md` before editing:

```text
TASK: HYB-###
AGENT: <name or handle>
SCOPE: <exact paths/modules>
START: <UTC timestamp>
BASE: <TESSERA or Gitbook commit>
STATUS: IN REVIEW
NEXT CHECK-IN: <UTC timestamp>
BLOCKER: none | exact blocker
```

On completion, the same agent appends:

```text
TASK: HYB-###
STATUS: DONE | BLOCKED | RETAINED | REJECTED
COMMIT: <commit or none>
CHECKS: <commands and results>
CHANGED: <short path list>
FOLLOW-UP: <HYB-### or none>
```

No agent may edit another active task's scope. If two tasks need the same path, the moderator must merge them into one task before work starts.

## Source-to-task routing

| Source family | Primary route | Do not do |
|---|---|---|
| `Grok-ready` | HYB-006, HYB-014, Gitbook review | Do not re-import its package manifests or historical generated output. |
| `Zz` | HYB-007, HYB-009, HYB-011 | Do not copy `z-app` wholesale or treat imported data as product code. |
| `1`, `5t`, `TESS`, `T44` | HYB-012–HYB-015 | Do not merge repeated snapshots or raw audit/runtime data. |
| `1T` | HYB-011 only | Do not inspect, copy, or delete protected vault content. |
| `olive-giant-ever-glade` | HYB-008, HYB-017 | Do not merge its independent auth/database/deployment contract. |
| Archive/handoff repositories | HYB-009, HYB-010, HYB-015 | Do not duplicate chunked archives or old theme media without review. |

## Completion rule

The board is complete only when every READY task is DONE, RETAINED, REJECTED, or explicitly BLOCKED with an owner and next decision. “Looks similar,” “was in an old screenshot,” or “appeared in an agent log” is not evidence of a completed feature.
