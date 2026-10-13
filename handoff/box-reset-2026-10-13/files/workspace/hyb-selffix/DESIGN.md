# HYB-SELFFIX — Narrow self-fix loop for TESSERA CI

IDENTITY: Tessera Admin coordinator  
Audience: Father (Collin Keane)  
Date (CT): 2026-10-05, ~5:30 PM  
Repo: vitalitychems-dot/TESSERA (private TypeScript pnpm monorepo)  
Base (TESTED): main@5c1137faeb7714482add93c2d6876396f34f1a03 (HYB-005 braces audit-ignore and HYB-012 route-inventory test both on main today)

This design invents no AGI, consciousness, or owned model weights. It is a narrow bot loop: when the CI job `validate` fails, diagnose from logs, propose a minimal fix, gate it, and maybe merge.

## 1. Purpose and non-goals

Purpose (GOAL): When `validate` fails on `main` or on a PR into `main`, Tessera launches one Cursor cloud agent that diagnoses the failure from job logs, writes a minimal fix on branch `selffix/<run-id>`, opens a draft PR with evidence, and runs the four gates. Under Father's standing rule (2026-10-05, 5:21 PM CT: "do all fixes automatically, as long as they aren't illegal"), a fix that passes Security and Build may be merged by Tessera, pinned to the head SHA.

Non-goals (GOAL — hard stop):

- No weight training and no "recursive self-improvement" claims.
- No `TESSERA_ENABLE_*` flag flips.
- No dependency upgrades without Build re-verify of the exact head.
- No edits to `.github/workflows/*` or other CI config.
- No secret access (no reading Actions secrets, env files with credentials, wallets, payments, blockchain, or the [REDACTED-PATH]
- No deleting files, tests, or data.
- No disabling or weakening tests or audit rules, except a narrow, dated, advisory-specific ignore like HYB-005 (one GHSA id, path evidence, review date).
- No touching wallets, payments, blockchain, or 1T material.

## 2. Trigger and dedupe

CI today (TESTED): single workflow `.github/workflows/ci.yml`, job `validate` on `push`/`pull_request` to `main`. Steps: frozen install → `pnpm audit` → `pnpm run typecheck` → schema push to throwaway Postgres → `pnpm test` → `pnpm run build`. Root scripts (TESTED): `typecheck`, `test`, `build` via unified scripts; workspace packages under `artifacts/*`, `projects/*`, `lib/*`, `scripts`.

Trigger options (GOAL — choose one in open questions):

1. A small Tessera polling routine that lists recent `validate` runs and acts when `conclusion=failure`.
2. A GitHub `workflow_run` trigger (separate watcher workflow) that fires when CI completes with failure. Adding that watcher is itself a CI-config change and is out of phase 0; phase 1 may add it only with Father's yes.

Dedupe (GOAL): one failing run id equals one attempt key. Store `selffix/<run-id>` branch name and a ledger entry keyed by `run_id`. If a branch or open draft PR already exists for that `run_id`, do not start another agent. Re-runs of the same failed SHA after a successful merge are ignored. Hosted-runner cancels (no steps started) are not code failures; escalate as infrastructure, do not open a fix PR.

## 3. Allowed vs forbidden fix classes

Allowed (phase 1 allow-list), grounded in real failures (TESTED):

| Class | Example from today | Typical fix |
| --- | --- | --- |
| Unpatched audit advisory blocking CI | `pnpm audit` fails on GHSA-vfj7-8cjw-p6xm (`braces` ≤3.0.3, path `artifacts/mockup-sandbox>fast-glob>micromatch>braces`). Runs: 37341568741, 37348793133, 37348832495, 37381241741, 37381588511. Fixed by HYB-005. | Narrow dated `auditConfig.ignoreGhsas` entry in `pnpm-workspace.yaml` with advisory URL, path, and review date — only when patched versions are `None`. |
| Obvious one-file TypeScript error | Not yet seen in CI logs because audit failed first (REPORTED from commit titles such as "Fix mockup Vite plugin type compatibility"). | Minimal type annotation / import fix in app or test code under `artifacts/**` or `lib/**`. |
| Broken or missing deterministic test assertion | HYB-012 added a route-inventory test; future failures of that class are expected once audit is green. | Fix the test or the registration under test; do not delete the test. |
| Frozen lockfile / install mismatch | Install step can fail on `--frozen-lockfile` (not observed red today after early audit fail). | Regenerate lockfile only for the exact package that broke install; Build must re-verify. |

Forbidden (always):

- Workflow or CI-config edits.
- Broad audit disables, removing `pnpm audit`, or ignoring multiple GHSAs without per-advisory evidence.
- Dependency major upgrades or mass `pnpm update`.
- Flag flips, secret touches, wallet/payment/blockchain/1T paths.
- Deleting tests, skipping tests, or weakening assertions to go green.
- Infrastructure cancels: runs 37362882386 and 37364732967 had `validate` cancelled with empty steps / `runner_id=0` (hosted runner never acquired). Escalate to Father as BLOCKED infrastructure; do not "fix" in code.

Green contrast (TESTED): after HYB-005, PR head run 37379320719 and main run 37382015797 both succeeded full `validate`.

## 4. Runner

Tessera launches one Cursor cloud agent on branch `selffix/<run-id>` from the failing ref's base (`main` for main failures; the PR head's merge base for PR failures).

Rules (GOAL):

- Exactly one commit on the branch.
- Draft PR only.
- PR body starts with `IDENTITY: Tessera Admin coordinator` and includes STATUS, COMMIT, CHECKS, CHANGED, PROVENANCE.
- Evidence block: excerpt of the failing log (step name + error lines), then the passing `validate` run id on the PR head after the fix.
- Size limits: ≤50 lines changed, ≤3 files. Larger diffs escalate as BLOCKED.
- Max attempts: 2 per `run_id`. After that, STATUS=BLOCKED and Father is notified.
- Agent must not push to `main`. Tessera merges only after gates.


## 4a. Draft PR body template

```text
IDENTITY: Tessera Admin coordinator

STATUS: IN REVIEW | BLOCKED
COMMIT: <branch SHA>
CHECKS: validate fail run <failing-run-id> step <name>; validate pass run <passing-run-id> on head <sha>
CHANGED: <≤3 paths>
PROVENANCE: selffix/<run-id>; allow-list class <name>; attempt <1|2> of 2

EVIDENCE FAIL:
<short log excerpt>

EVIDENCE PASS:
CI run <id> conclusion=success on head <sha>
```

Security and Build both pin their PASS/FAIL to the same head SHA named in COMMIT. If the head moves after those checks, merge is refused and the attempt counts toward the max of 2.

## 5. Gates, merge rules, kill switch

Gate order (RETAINED from mesh practice):

1. Gitbook Moderator — docs impact only; for code-only selffix PRs this is a no-docs PASS or N/A with explicit note.
2. Tessera review — allow-list class, size limits, IDENTITY body, one commit, evidence present.
3. Security (read-only) — provenance of changed paths, no secrets, scope inside allow-list, no forbidden paths.
4. Build (independent verify-only) — re-run `validate` on the exact PR head SHA and require success. Build does not edit code.

Merge (GOAL, under standing fix rule 5:21 PM CT): if Security PASS and Build PASS on head SHA H, Tessera may merge pinned to H (`sha` argument on merge). If head moved, refuse and re-gate.

Kill switch (GOAL): Father says "stop selffix" (or Tessera sets STATUS=BLOCKED globally). Existing draft PRs stay open but no new agents launch and no merges proceed until Father re-enables.

## 6. Metrics

Track per week (GOAL):

- Time to green: failing `run_id` timestamp → merge timestamp (or BLOCKED).
- Fix acceptance rate: merged selffix PRs / attempts.
- Reverts: merges reverted within 7 days.
- False fixes caught: Security FAIL or Build FAIL after a proposed fix (these are successes of the gate system).
- Skipped infrastructure cancels (should be high when GitHub runners flake).

## 7. Rollout

- Phase 0 (GOAL, start here): dry-run. Diagnose and write a proposal note only. No branch, no PR, no merge.
- Phase 1: draft PRs on `selffix/<run-id>`, human-free gate merge when Security+Build PASS, allow-list as in §3.
- Phase 2: widen allow-list only with measured evidence from phase 1 metrics (Father yes required per new class).

## 8. Acceptance test and open questions

Acceptance test for the track (GOAL):

1. Inject or wait for a real `validate` failure of an allow-listed class on a non-main branch or dry-run ledger.
2. Phase 0 produces a diagnosis with run id, failing step, and proposed patch class labeled correctly.
3. Phase 1 (when enabled) opens one draft PR `selffix/<run-id>` with IDENTITY body and evidence, ≤50 lines / ≤3 files.
4. Security and Build run on that head; a false fix is refused; a true fix merges pinned to head SHA.
5. A second agent for the same `run_id` does not start (dedupe).
6. A cancelled runner job does not open a code PR.

Open questions for Father (yes/no only):

1. Approve phase 0 dry-run now?
2. After two clean dry-runs, enable phase 1 draft PRs with Tessera merge on Security+Build PASS?
3. Prefer polling over adding a `workflow_run` watcher workflow?
4. Keep max attempts at 2 per failure?
5. Keep size limits at 50 lines / 3 files?
6. Allow the HYB-005-style dated single-GHSA ignore class in phase 1 without a fresh per-incident yes (standing rule covers it)?

## 9. HYB task card

```text
IDENTITY: Tessera Admin coordinator
AGENT: Tessera (admin) — design author; Cordnation assigns the number
TASK: HYB-SELFFIX (placeholder id)
SOURCE: Father standing fix rule 2026-10-05 5:21 PM CT; live TESSERA CI failures today; mesh four-gate practice
TARGET: vitalitychems-dot/TESSERA self-fix loop design only (this doc); no GitHub writes in this drafting pass
SCOPE: Design the first narrow self-fix loop as a HYB track: trigger, allow-list, runner, gates, metrics, rollout, acceptance test. Read-only grounding against .github/workflows/ci.yml, package.json scripts, pnpm-workspace.yaml, and list_workflow_runs.
DELIVERABLE: /workspace/hyb-selffix/DESIGN.md (this file)
ACCEPTANCE TEST: Doc covers purpose/non-goals, trigger+dedupe, allow vs forbidden classes with real run ids, runner shape, gates/merge/limits/kill switch, metrics, phased rollout, yes/no open questions, and this HYB card with live OVERLAP CHECK.
OVERLAP CHECK: TESSERA main@5c1137faeb7714482add93c2d6876396f34f1a03 (TESTED); TESSERA open PRs: none (TESTED); Gitbook main@45651521a137c4448673d6abfaa77e1567230f83 (TESTED); Gitbook open PRs: #11 draft "GB-029 rev 3: intake log backfill (PR #8, #9, #10)" head baa0daeb (TESTED). No competing selffix branch or PR found.
BLOCKERS: Cordnation number assignment; Father answers to §8 yes/no questions before phase 1.
NEXT CHECK-IN: After Father answers §8 (target same evening CT 2026-10-05 or next session).
STATUS: DESIGN READY — awaiting Father yes/no on phase 0 and phase 1.
```

## Provenance of CI facts (TESTED)

- Workflow path: `.github/workflows/ci.yml` (only workflow; job name `validate`).
- Failed audit runs (braces GHSA-vfj7-8cjw-p6xm): 37341568741, 37348793133, 37348832495, 37381241741, 37381588511.
- Cancelled / never-acquired runner (not code): 37362882386, 37364732967.
- Green after HYB-005: 37379320719 (PR), 37382015797 (main@5c1137fa).
