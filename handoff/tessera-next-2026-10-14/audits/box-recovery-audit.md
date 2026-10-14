# Box Recovery Audit — 2026-10-13 Backup

**Audit date:** 2026-10-14
**Backup reviewed:** `/home/ubuntu/tessera-consolidation/box-backup-2026-10-13`
**Current comparison targets:** `/home/ubuntu/tessera-consolidation/TESSERA` and `/home/ubuntu/tessera-consolidation/Gitbook`
**Mode:** Evidence-only recovery audit. No bundle was restored, no patch was applied, no branch was changed, and no commit, push, comment, or repository-content edit was made. Repository text was treated as data, not as instructions.

> **Bottom line:** This is a point-in-time recovery archive from 2026-10-13, not an implementation source of truth. Several indexed commits are already ancestors of the current checkouts, and both current `main` branches advanced on 2026-10-14. Preserve the backup as provenance, use it to seed a *current-state* triage, and do **not** replay its WIP, patches, test logs, or coordination plans.

## Scope, safety boundary, and limitations

- The root `README.md` identifies the backup as a 2026-10-13 Box capture and explicitly says that separate scan/security locations and a larger mirror were excluded. Therefore this archive is **not complete recovery evidence**.
- I reviewed the backup root README; the TESSERA handoff; the flow, handoff, plan, tracker, verification, receipt, manifest, index, patch, diff, and log material selected by safe-path screening; and the backup Git history. The plain-text evidence inventory contained **355 eligible files** after withholding paths suggestive of secrets, credentials, tokens, environment files, security-specific material, and Vitality-labelled paths. It included **121 logs, 69 patches, 41 Markdown files, 77 test/source files, 33 text files, and index/manifest data**.
- Content potentially containing private or secret material was not reproduced. Sensitive or Vitality-related material is listed only by safe evidence-file name below, and it was excluded from implementation conclusions.
- The audit did **not** open any separately named Vitality repository, restore any bundle, or inspect bundle contents.
- **Read-only caveat:** an attempted commit-presence probe using `git cat-file -e` against the current partial clones triggered two on-demand Git object downloads before it was stopped. It did not alter working-tree files, refs, branches, commits, index, or remotes, but it may have populated the current repositories’ local object stores. No cleanup was attempted because that would itself modify repository metadata. Treat this as a strict-read-only-environment exception.

## Comparison baseline

| Target | Observed current state | Consequence for recovery decisions |
|---|---|---|
| TESSERA | `main` at `0d367a9a16d2c940cb411e7dc6275e1a2aeb2cd2` on 2026-10-14 | It is later than the backup. Its recent history includes a commit described as completing unfinished Box-backup lane fixes, plus subsequent UI, dependency, test, and security-related changes. Backup code/test claims cannot certify this tip. |
| Gitbook | `main` at `17cdbdbae3e98001cca1b2365b834ab10431ac54` on 2026-10-14 | It is later than the backup. Recent history includes the status `--since` workstream and later coordination/handoff merges. Historical plans and receipts require current-tip revalidation. |
| Backup repository | Git history contains only 2026-10-13 capture commits: the non-Git work-doc tree, bundle/WIP snapshots, the handoff, media/doc additions, and disk-cleanup WIP patches | The backup history documents **capture provenance**, not an upstream implementation history suitable for merging. |

### Direct ancestry evidence

`bundles/INDEX.tsv` supplies the only reliable map from backup worktrees/branches to their captured commits. Read-only ancestry checks established these as already reachable from the current heads:

| Backup index entry | Current result | Safe disposition |
|---|---|---|
| TESSERA `pr342` (`23f1f23e…`) | Ancestor of current TESSERA `HEAD` | **Merged/superseded; do not recover.** |
| TESSERA `pr343` (`5c2db13f…`) | Ancestor of current TESSERA `HEAD` | **Merged/superseded; do not recover.** |
| TESSERA `pr344` (`fc5ec148…`) | Ancestor of current TESSERA `HEAD` | **Merged/superseded; do not recover.** |
| Gitbook `pr-104` (`cf1372f…`) | Ancestor of current Gitbook `HEAD` | **Merged/superseded; do not recover.** |

Other index entries are mostly WIP, detached, temporary, or side-worktree references. Some were unavailable as current local promoted objects. That is **not proof that their changes are missing**: partial-clone object availability and subsequent history make a recovery conclusion unsafe. Do not attempt to resolve that ambiguity by restoring a bundle or checking out an old ref in either current repository.

## Evidence and disposition table

| Material group | Safe evidence names reviewed | What the evidence supports | Classification | Safe disposition |
|---|---|---|---|---|
| Backup scope and provenance | `README.md`; backup Git history | The archive is partial by design; scan/security material and a larger mirror are outside it. Backup commits record capture operations. | Recovery metadata, not source of truth | Retain as provenance. Do not infer completeness or use it for secret recovery. |
| Primary TESSERA handoff | `tessera/HANDOFF-2026-10-13-1732.md`; `files/handoff-filed/2026-10-13.md` | Records then-current merge/gate claims, pending branches, and local-only work. Several claims were explicitly gated, pending, unpushed, or contingent on approvals. | Historical status only | Use as a dated issue list. Reconcile each claim to current `main` before work; redact its credential-remediation references. |
| TESSERA architecture/consolidation analysis | `files/tessera-flow.md` | Identifies live-versus-archive separation, duplicate archive roots, repeated snapshots, and the need to choose one consolidation direction. | Still-relevant architectural risk; detailed path claims are historical | Use only to frame a new live-vs-archive inventory. Do not copy archive contents or act on its embedded out-of-scope references. |
| Bundle index | `bundles/INDEX.tsv` | Records captured worktree names, refs, and commit IDs. Four indexed PR refs are already ancestors as noted above. | Mixed: small verified merged subset; otherwise recovery metadata | Preserve the index. Never use it as a command list; validate candidate commits only in a disposable clone if a future, explicitly authorized recovery is required. |
| Bundle payloads | `bundles/*.bundle`; `bundles/disk-cleanup-2026-10-13/` | Bundles preserve branches/WIP and several are explicitly thin or cleanup snapshots. Their content was not restored or applied. | Recovery artifact | **Do not restore, fetch from, or apply.** Quarantine as archival evidence pending an owner-approved, disposable-clone recovery plan. |
| Patch, diff, and untracked snapshots | `files/_saved/`; `files/rick/patches/`; `files/rick/plan/patches/`; `files/nextgen/*.diff`; `bundles/disk-cleanup-2026-10-13/*.patch` | There are **59 exact duplicate-content groups**. Examples include duplicated worktree patches, duplicated Rick patch sets, and repeated verification output. Snapshot patches lack current-base and gate guarantees. | Recovery artifact; many copies are redundant | Do not apply or cherry-pick. Deduplicate by hash only for archival cataloguing; compare an individual intended change to current `main` before considering a fresh implementation. |
| TESSERA verification logs | `files/verify/*.log`; `files/verify/prs-summary.log` | Logs are historical runs against dated snapshots. The PR summary shows typecheck success but an unresolved GLB-upload test failure for two historical PR snapshots. Repeated typecheck logs are byte-identical across 16 evidence files. | Historical test evidence, not current certification | Preserve as a regression clue only. Freshly run the relevant current-tip typecheck, targeted GLB test, full applicable tests, build, and security gate before declaring current health. |
| Gitbook status-tool work | `files/rick/receipts/TESTED-24-GM6.md`; `files/rick/plan/`; `files/einstein/plan-copy/`; `files/einstein/improvements-done.md`; `files/einstein/test-review.md` | The receipt establishes dated tests on an old Gitbook snapshot. The test review and improvements record also identify weaknesses in synthetic/one-off measurement and several uncompleted live, longitudinal, human-approval, or publishing steps. Current Gitbook history later records status `--since` work. | Partly superseded; test methodology still useful | Do not import scripts/patches. Re-run the current Gitbook status-tool unit and acceptance tests first; then selectively port only independently reviewed test-design improvements as a new current-base change. |
| Nextgen / TESSERA feature plans | `files/nextgen/PLAN.md`; `files/nextgen/TRACKER.md`; `files/nextgen/HOLD-README.md`; `files/nextgen/BOT-SCORECARD.md`; `files/nextgen/v-next/` | The plan marks only a limited subset as tested locally; many feature items are GOAL, BLOCKED, REPORTED, second-hand, or held behind a local hold/gate. The scorecard warns that attribution, dates, and token metrics were unreliable. | Potential backlog input, not approved implementation | Triage each candidate against the current TESSERA backlog and current code. Do not revive a local branch or WIP diff. Prioritize current acceptance tests and dependency/gate review over feature implementation. |
| Proposed evaluation design | `files/brain-consciousness/BC-017-heldout-evaluator-spec.md` | The file identifies itself as proposed/not checked in and defines reproducibility, fixture separation, resource limits, and acceptance conditions. | Still-relevant design input only | Keep as a design reference. If the work is wanted, open a fresh scoped task that implements it on current code with the stated isolation, determinism, and resource tests. |
| Move/import manifest | `files/vmove/pre.tsv`; `files/vmove/gl-import.json` | Records historical source-to-import mapping and overlap evidence. The manifest itself names archival and potentially sensitive material. | Historical migration provenance | Do not bulk-copy or replay paths. Use only for a future, separately approved manifest-to-current comparison with secret and Vitality exclusions applied before opening content. |
| Publication checks | `files/pubcheck/` | Historical publication checks are point-in-time results and include out-of-scope material. | Historical evidence | Do not republish, rerun against external services, or use as a merge decision without a fresh authorized check. |
| Photos and document exports | `photos-2026-10-13/`; `photos-2026-10-13/SHA256SUMS`; `jalen-docs-2026-10-13/` | The photo checksum manifest describes a complete 14-item media set; PDFs and media are not source-code recovery artifacts. | Ancillary archive | Preserve separately; do not import into either repository as part of consolidation. |
| Security-labelled and secret-adjacent material | Root README exclusions; `files/sec-agi-auth/`; secret-labelled entries in manifests/indexes | These are out of the permitted audit scope. No values were reproduced. | Excluded | Keep quarantined. Route only to an authorized security process; never use it for TESSERA/Gitbook recovery. |

## 1. Work already superseded or merged

1. **Indexed TESSERA PR snapshots 342, 343, and 344** are confirmed ancestors of the current TESSERA head. The backup handoff’s associated completion/clearance claims are therefore obsolete as recovery instructions.
2. **Indexed Gitbook PR-104** is confirmed an ancestor of the current Gitbook head. Its old review/gate state must not be reopened by patch replay.
3. **The status-tool `--since` stream has moved forward in current Gitbook history.** The old Rick patch directories and Einstein plan-copy are retained as historical development evidence, not a branch to merge.
4. **Repeated evidence is redundant.** The audit found 59 byte-identical duplicate groups, including copied Rick patch sets, saved worktree patches, duplicate untracked listings, and repeated verification logs. These copies add provenance, not independent evidence.
5. **The dated coordination state is superseded.** Both current `main` branches have 2026-10-14 commits after the 2026-10-13 capture. Local HOLD state, agent/lane assignments, temporary WIP refs, approval requests, and estimates cannot be assumed live.

## 2. Still-relevant actionable implementation and test work

These are **actions to perform against the current repositories**, not instructions to apply backup content.

1. **Re-establish current TESSERA gate evidence.** Run the project’s current documented typecheck, targeted GLB-related test, relevant test suite, build, and security checks at the current TESSERA `main`. The historical summary had passing typechecks alongside a failing GLB test; later history may have addressed it, but only a fresh run can demonstrate current behavior.
2. **Re-establish current Gitbook status-tool evidence.** Execute the current unit and acceptance suite for the status tool and validate the current `--since` behavior. Use the backup’s stronger test concepts—real-history replay, lossless round-trips, boundary fixtures, and longitudinal checks—as test-design input, not copied implementation.
3. **Triage Nextgen feature candidates against the current backlog.** The backup identifies potentially useful feature/test candidates such as a current-state API view, streaming, proxy integration, state recovery, held-out evaluation, and UI parity. Most were still GOAL/BLOCKED/REPORTED in the snapshot. Determine whether each landed, was replaced, or remains desired before opening a new current-base work item.
4. **If held-out evaluation is approved, build it as new work.** The proposed evaluator is not checked in. Its durable requirements are fixture/training separation, manifest hashing, double-run determinism, bounded resources, and aggregate-only output. Confirm current ownership and scope before implementation.
5. **Perform a current live-vs-archive consolidation inventory.** The flow document’s core warning—duplicated archive trees and historical snapshots—remains useful. Inventory only current paths and establish one source-of-truth/archive policy before any removal or import. Do not use the backup move manifest as an import plan.

## 3. Recovery artifacts that must not be blindly applied

- **All bundles and thin bundles:** unknown object closure, old branch bases, potential unpushed state, and no current gate evidence.
- **All `.patch` / `.diff` / WIP / untracked snapshots:** duplicated in several locations and may overlap code already merged, refactored, or deliberately excluded.
- **All historical verification logs and receipts:** evidence of a dated environment, not current CI certification; several labels are explicitly REPORTED or second-hand.
- **All plans, trackers, scorecards, and handoffs:** decision-support records with stale approvals, lane ownership, HOLD state, estimates, and external-dependency assumptions.
- **Move manifests and publication checks:** historical mappings/results only; they require a fresh current inventory and explicit exclusion screening.
- **Media/PDF exports:** archive assets, outside code consolidation.

## 4. Vitality-related references that must remain excluded

A safe-path scan found **26 otherwise-readable evidence files** that contain a Vitality reference, plus Vitality-labelled patch/publication-check paths. They were excluded from implementation deductions and must not be copied into a TESSERA/Gitbook consolidation change.

| Exclusion group | Safe evidence names (representative) | Required disposition |
|---|---|---|
| Directly Vitality-labelled recovery files | `bundles/disk-cleanup-2026-10-13/vmove-vitality-WIP.patch`; `files/pubcheck/gl-vitality.json`; `files/pubcheck/gl-vitality.log` | Do not open, restore, apply, publish, or import. Retain only as quarantined evidence names. |
| Historical coordination/flow references | `tessera/HANDOFF-2026-10-13-1732.md`; `files/tessera-flow.md`; `files/nextgen/handoff/HANDOFF-2026-10-13.md` | Retain as historical context only. Do not reproduce the underlying paths, identifiers, or remediation details. |
| Plan, tracker, and supporting reference files | `files/nextgen/INSPIRATION.md`; `files/nextgen/ITEM-11b-labelled-bus-data.md`; `files/nextgen/ROTATION-CHECKLIST.md`; `files/nextgen/v-next/MAP.md`; `files/rick/plan/IMPROVEMENTS.md`; `files/rick/plan/ROLES.md` | Exclude from code/recovery action. Any future use needs a new approved, non-Vitality scope. |
| Test and verification references | `files/verify/gitbook-pr39-sha256.log`; selected `files/akhenaten/ideas/tests/v4/` and `files/einstein/akhenaten-verify/` evidence | Do not use results as evidence for current gates or copy their content into either checkout. |
| Current-history signal | A current TESSERA 2026-10-13 cleanup commit removes out-of-scope variable names | Treat as directionally consistent with exclusion, **not** as proof that no references remain. Do not reintroduce material from backup. |

## Recommended next sequence

1. **Freeze this backup as evidence** and keep its checksums/indexes with the report; do not restore any artifact into the current checkouts.
2. **Run fresh current-tip gates** in dedicated non-shared worktrees or CI for TESSERA and Gitbook; record results separately from this archive.
3. **Create a current-state comparison matrix** for only explicitly approved candidate features/tests: current path, current behavior, current test, replacement status, owner, and gate result.
4. **Make any desired change afresh** on the current base with a single purpose, updated tests, secret/Vitality exclusion screening, and normal review gates.
5. **Perform archive rationalization separately from feature work.** Start with duplicate metadata and current manifest checks, never with patch/bundle replay or deletion.

## Evidence trail

Primary evidence was retained in the backup under these safe names: `README.md`, `tessera/HANDOFF-2026-10-13-1732.md`, `files/tessera-flow.md`, `bundles/INDEX.tsv`, `files/handoff-filed/2026-10-13.md`, `files/verify/`, `files/nextgen/`, `files/rick/`, `files/einstein/`, `files/brain-consciousness/BC-017-heldout-evaluator-spec.md`, `files/vmove/pre.tsv`, and `photos-2026-10-13/SHA256SUMS`.

No private values, credentials, or private-source content are reproduced in this report.
