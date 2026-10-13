# Build Gate: TESSERA post-merge of PR #2 @ main `50876d40` + PR #1 stack check

**Part A, OVERALL: PASS (TESTED)**, main tip `50876d40cc1ed03538fa0dd4761231805292d5da`. CI is red only on the known braces GHSA audit step. That step already failed on main before this merge, and this sub-check expects it.
**Part B: PR #1 still merges cleanly onto 50876d40: YES (TESTED).** PR #1 content PASS reconfirmed on 50876d40 (TESTED). A CI re-run on the combined tree is recommended before merge (see B4).

Verified by Build lane from its own read-only GitHub MCP calls and local scratch checks, Mon Oct 5 2026, about 5:20 PM CT.
Nothing was pushed, merged, commented on, or edited. The repo was not cloned. Build set no DATABASE_URL, started no servers against a real DB, and touched no TESSERA_ENABLE_* flag.
Scratch evidence: `/workspace/build-gate/work-TESSERA-PR2-postmerge-50876d40/` (both recursive trees as JSON, workflow-runs JSON, the reconstructed tip `pnpm-workspace.yaml`, `pr1.patch`, and the `applytest/` git sandbox).

---

## Part A: post-merge of PR #2 at tip 50876d40

### A1. Main tip: PASS (TESTED)
- `list_commits sha=main`: newest commit is `50876d40cc1ed03538fa0dd4761231805292d5da`, followed by `fec56eb` → `9a0323f` → `216e4e8` → `f662284`.

### A2. Commit shape: PASS (TESTED)
- `get_commit 50876d40`: **one parent**, `fec56eb09d19907832663d5f16fcbc24f3d00317`, so this is a squash and not a merge commit.
- Tree: `42fb940d92ea7ee097b3b9e2a3165b77fae3763d` (fec56eb tree was `e0c58c61c9e0aebb9f7badb134f15d9fec1b97c0`)
- Author Tessera; committer GitHub (web-flow); signature verified=true.
- Committed 2026-10-05 22:18:12 UTC = **5:18 PM CT**.
- Message: "HYB-012: route inventory test (test-first, no runtime change)" and body "Father yes (word merge) 5:17 PM CT. Security PASS. CI validate red on braces GHSA (HYB-005) already on main." The message names HYB-012. It reuses PR #2's title but does not contain a literal "#2" (cosmetic only).

### A3. Diff scope fec56eb → 50876d40: PASS (TESTED)
- `get_commit` stats: total 530, **+530 / −0**, exactly 2 files, both `status=added`:
  1. `artifacts/api-server/src/__tests__/route-inventory.test.ts`: +295/−0, blob `ef96c712dabcd9353c459b5c3aeefa97e34abb0a`
  2. `artifacts/api-server/src/__tests__/route-inventory.ts`: +235/−0, blob `aa0aa604267d91059228a5de4154fc356448f0f9`
- No other paths.
- Squash fidelity: these two blob SHAs **match exactly** the blobs at PR #2 head `cb19f210` (`list_pull_request_files #2`). What landed is exactly the reviewed content.

### A4. Tree equality: PASS (TESTED)
- I ran `get_git_tree recursive` on both trees. Neither listing was truncated: fec56eb has 1567 entries, 50876d40 has 1569. I diffed them locally with Python.
- **Added:** exactly the 2 paths above, mode 100644, with the blob SHAs above.
- **Removed:** none.
- **Changed blobs:** none. All **1383 of 1383** pre-existing blobs have identical SHAs.
- The only other changed entries are the 4 parent tree objects on the path (`artifacts`, `artifacts/api-server`, `artifacts/api-server/src`, `artifacts/api-server/src/__tests__`). Adding files always changes those.
- `pnpm-workspace.yaml` has blob `fb46443d119afa183de4d2847f1b9c03801ef01b` in both trees, so it is unchanged.

### A5. No TESSERA_ENABLE_* changes: PASS (TESTED)
- I read the full squash patch (both files, all 530 added lines). There is no `TESSERA_ENABLE` string, no env flag flips, no runtime or route module edits, and no package/lock/workspace files.
- The tree diff in A4 shows no other file changed, so no enable flag could have changed anywhere else.
- Same note as the pre-merge report: the test sets a placeholder `DATABASE_URL` (`postgresql://[REDACTED]@127.0.0.1:5432/route_inventory`) only when the variable is unset, and restores it afterwards. It is not a secret.

### A6. CI on 50876d40: PASS for this sub-check (red only on audit, as expected) (TESTED)
- `list_check_runs_for_ref 50876d40`: 1 check, `validate`, head_sha exact, completed, **conclusion=failure**.
- Workflow run `37381588511` (CI, push, main, run #8), job `112004653014`, started 5:18 PM CT and finished 5:19 PM CT.
- Steps:
  | # | Step | Result |
  |---|---|---|
  | 1–5 | Set up job / Initialize containers (postgres:16 service) / checkout / pnpm setup / setup-node | success |
  | 6 | Install frozen workspace (`pnpm install --frozen-lockfile --ignore-scripts`) | success |
  | 7 | **Audit all dependencies** (`pnpm audit`) | **failure** |
  | 8 | Typecheck all applications and libraries | skipped |
  | 9 | Apply schema to disposable CI database | skipped |
  | 10 | Run isolated workspace tests | skipped |
  | 11 | Build all workspace applications | skipped |
  | post | cleanup / stop containers / complete | success (setup-node post skipped) |
- Audit log: 1 high, `braces` <=3.0.3, no patched version, path `artifacts__mockup-sandbox>fast-glob>micromatch>braces`, **GHSA-vfj7-8cjw-p6xm**, exit code 1. This is the same advisory and path as main @ fec56eb (run #3, failure) and PR #2 head (run #7, failure).
- No failures other than the audit step. The audit step **masks** steps 8–11, so typecheck, schema, tests, and build have **not run** in GitHub CI on main @ 50876d40. The new route-inventory vitest has not yet run in CI anywhere. The cloud agent's local 5/5 pass is still REPORTED only.

### A7. Board comment: PASS (TESTED)
- `list_issue_comments` on Gitbook #2: comment `6004286102` exists. Created 22:18:38 UTC (5:18 PM CT) by vitalitychems-dot through the Cursor app, as "Tessera Admin coordinator".
- It reads "HYB-012: DONE (merged 17:18 CT)", squash `50876d40…`, head `cb19f210`, parent `fec56eb`, and says CI is red only on braces / HYB-005. That matches what I found.

### Part A verdict
| Check | Result |
|---|---|
| A1 tip = 50876d40 | PASS |
| A2 single parent fec56eb, HYB-012 message | PASS |
| A3 exactly 2 added test files, +530/−0, blobs = PR head | PASS |
| A4 tree = fec56eb + 2 blobs (1383/1383 other blobs identical) | PASS |
| A5 no TESSERA_ENABLE_* / runtime change | PASS |
| A6 CI red only on braces audit (expected); no other failures | PASS (expected red) |
| A7 board comment 6004286102 present | PASS |

**OVERALL A: PASS (TESTED)**. Caveat: main CI is still not green, and tests/typecheck/build are masked until HYB-005 lands.

---

## Part B: PR #1 on the new main

### B1. PR state (TESTED)
- `get_pull_request #1`: open, not draft, not merged.
- Head `cursor/hyb-005-audit-ignore-943c` @ **`76716c22d79085e1eb72c1e33ea9471b1c43103d`**. That is the same head as the prior PASS; there were no new pushes.
- `base.sha` still shows `fec56eb` because GitHub only refreshes the PR base SHA on a push or retarget. Base ref is `main`, which is now 50876d40.
- Mergeability: the first read returned `mergeable=null, mergeable_state=unknown` while GitHub recomputed after main moved. The re-read returned **`mergeable=true, rebaseable=true, mergeable_state=clean`**.
- The `merge_commit_sha` field still points at the old test merge `a4acbddf`, which has parents fec56eb + 76716c22 and was created 4:57 PM CT. GitHub had not yet regenerated the test merge against 50876d40 when I checked. The independent apply check in B2 covers that gap.

### B2. Clean stack onto 50876d40: YES (TESTED)
- `list_pull_request_files #1`: still **one file**, `pnpm-workspace.yaml`, modified, **+8/−0**, result blob `cf1e10ee3fc366408f5c19b7c50f661e6aeb6752`.
- `pnpm-workspace.yaml` at 50876d40 has blob `fb46443d…`, identical to fec56eb (from the A4 tree diff). PR #2 never touched it, so the two PRs change disjoint files.
- Local check without a clone:
  1. Fetched `pnpm-workspace.yaml` @ 50876d40 with `get_file_contents` and rebuilt it locally. `git hash-object` = `fb46443d119afa183de4d2847f1b9c03801ef01b`, which matches the tree blob, so the copy is byte-exact.
  2. Put that one file in a scratch git repo and saved PR #1's hunk (`@@ -11,6 +11,14 @@`) as `pr1.patch`.
  3. `git apply --check -v pr1.patch` → `Checking patch pnpm-workspace.yaml...` with no errors.
  4. Applied it: the result's `git hash-object` = **`cf1e10ee3fc366408f5c19b7c50f661e6aeb6752`**, the same blob as PR #1 head. `git diff --numstat` = `8 0 pnpm-workspace.yaml`.
- Conclusion: PR #1 applies cleanly onto 50876d40 with no conflict, and the result is byte-identical to the PR head file. GitHub's own recompute also says `mergeable=true, clean`.

### B3. Prior PASS criteria on the stacked result: PASS reconfirmed (TESTED)
- Still +8/−0, one file (`pnpm-workspace.yaml`).
- Adds `auditConfig.ignoreGhsas: [GHSA-vfj7-8cjw-p6xm]` with the HYB-005 comment block: advisory URL, transitive path `artifacts/mockup-sandbox > fast-glob > micromatch > braces`, review date 2026-11-05, and "remove once braces >=3.0.4 ships".
- It ignores only that one GHSA. The audit command and level are unchanged.
- `grep -c TESSERA_ENABLE` on the stacked file = 0. No TESSERA_ENABLE_*, no deps, no lockfile changes.
- The advisory PR #1 ignores is exactly the one that fails main @ 50876d40 (A6), and it is the only one. PR #1 should therefore turn the audit step green on the combined tree.

### B4. CI on PR #1 and whether to re-run (TESTED / judgment)
- `list_check_runs_for_ref 76716c22`: `validate` **success** (run `37379320719`, #6, 4:57–5:00 PM CT). That run's PR association shows base `fec56eb`, so it tested the merge with fec56eb **without** PR #2's files.
- No new pull_request run started after main moved (latest runs: #8 push main 50876d40, #7 PR #2, #6 PR #1).
- `mergeable_state=clean`: the existing green check on the head SHA satisfies GitHub, so a merge is technically not blocked.
- **Re-run recommended before merge (not strictly required by mergeable_state):** CI has never run the new route-inventory test, because audit masked it on PR #2 and on main. PR #1 + 50876d40 will be the first combined tree where typecheck, schema, tests, and build actually run. Updating PR #1's branch from main, or re-running CI on the combined tree, would show green for the HYB-012 test before HYB-005 lands. If it merges without that, the first real test signal will be the post-merge push run on main.
- Build did not trigger any re-run or branch update (out of scope: no edits or pushes).

### Part B verdict
| Check | Result |
|---|---|
| Head still 76716c22, 1 file +8/−0 | PASS |
| Merges cleanly onto 50876d40 (git apply --check + GitHub mergeable) | **YES** |
| Content PASS (HYB-005 ignoreGhsas GHSA-vfj7-8cjw-p6xm, no ENABLE) on 50876d40 | PASS reconfirmed |
| mergeable_state | `clean` |
| CI re-run on combined tree | Recommended (old green run was vs fec56eb; route-inventory tests have never run in CI) |
