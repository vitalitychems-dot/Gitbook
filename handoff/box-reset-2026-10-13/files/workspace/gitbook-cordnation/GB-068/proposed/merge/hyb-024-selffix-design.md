# HYB-024 — Self-fix loop for TESSERA CI

**Design author:** Tessera (admin). **Published by:** Gitbook / Cordnation.
**Status:** Phase 0 (suggest-only dry run) approved, as Tessera reports: Father's 5:32 PM CT approval of the Oct 5 bulk update ([comment 6004515093](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6004515093)). Phase 1 is not approved.
**Source:** the design file from 2026-10-05 and its dry-run ledger, both kept on the work machine.

This is a narrow loop. When the TESSERA CI job `validate` fails, it reads the logs, proposes a small fix, and sends that fix through the normal gates. It makes no claims about self-improvement and trains no weights.

## What it must never do

- Edit `.github/workflows/*` or any other CI config.
- Flip a feature flag, read secrets, or touch wallet, payment, blockchain or 1T paths.
- Upgrade dependencies broadly or run a mass `pnpm update`.
- Delete, skip or weaken tests or audit rules. The one exception is a narrow, dated ignore for a single advisory, as in HYB-005.
- Push to `main`.

## Trigger and dedupe

- One failing run id is one attempt.
- If a branch or draft PR already exists for that run id, no second agent starts.
- A run that never got a runner (empty steps, runner id 0) is infrastructure, not code. It is escalated and gets no fix PR.
- Two trigger options are open: a polling routine, or a `workflow_run` watcher. The watcher is itself a CI-config change, so it needs Father's yes.

## Fix classes allowed in phase 1

| Class | Real example | Fix |
|---|---|---|
| Audit advisory with no patched version | `braces` advisory GHSA-vfj7-8cjw-p6xm, fixed by HYB-005 | One dated ignore entry with the advisory URL, path and review date |
| One-file TypeScript error | Not yet seen in CI | Smallest type or import fix under `artifacts/**` or `lib/**` |
| Broken deterministic test | Route-inventory test from HYB-012 | Fix the test or the code under test; never delete the test |
| Lockfile or install mismatch | Not yet seen | Regenerate the lockfile only for the package that broke; Build re-verifies |

## Runner and limits

- Branch `selffix/<run-id>`, one commit, draft PR only.
- 50 lines and 3 files at most. Anything larger is BLOCKED.
- 2 attempts per run id. After that it is BLOCKED and Father is told.
- The PR body carries the failing log excerpt and the passing `validate` run on the new head.

## Gates and merge

1. Gitbook Moderator: docs impact, or N/A for code-only fixes.
2. Tessera: class, size, one commit, evidence present.
3. Security: changed paths, no secrets, inside the allow-list.
4. Build: re-runs `validate` on the exact head.

If Security and Build both pass on the same head, Tessera may merge pinned to that head. If the head moves, the fix is re-gated.

**Kill switch:** Father says "stop selffix". Open drafts stay open; nothing new starts and nothing merges.

## Rollout

- **Phase 0 (approved):** diagnose and write a proposal note only. No branch, no PR, no merge.
- **Phase 1 (needs Father's yes):** draft PRs and gated merges for the classes above.
- **Phase 2:** widen the classes only with phase 1 evidence and Father's yes for each new class.

## Phase 0 results so far

- 13 runs are recorded in the dry-run ledger. All were classified, and none led to a code change.
- The two replay runs from Oct 5 were classified correctly: the audit class, and an infrastructure cancel. That meets the "two clean dry runs" mark.
- Oct 12: 11 `main` runs never started because of the GitHub Actions billing or spending limit. They were recorded as infrastructure and escalated once. No fix PR was opened.

## Measures

Time to green, fix acceptance rate, reverts within 7 days, false fixes caught by the gates, and infrastructure cancels skipped.

## Open questions for Father (yes or no)

1. After two clean dry runs, turn on phase 1 draft PRs, with Tessera merging when Security and Build pass?
2. Polling instead of a watcher workflow?
3. Keep the limit of 2 attempts per failure?
4. Keep the limit of 50 lines and 3 files?
5. Let the single-advisory ignore class run in phase 1 without a new yes each time?
