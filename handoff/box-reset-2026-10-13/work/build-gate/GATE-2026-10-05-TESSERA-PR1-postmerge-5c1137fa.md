# Build Gate: TESSERA post-merge of PR #1 (HYB-005) @ main `5c1137fa`

**OVERALL: PASS (TESTED)**

- Main tip: `5c1137faeb7714482add93c2d6876396f34f1a03`
- CI: run **37382015797** (CI #9, push to main), job `validate` id **112006094090**. Conclusion: **success**.
- The audit step is now green: `Severity: 1 high (1 ignored)`. Typecheck, db push, tests, and build all ran and passed. Nothing was skipped.
- route-inventory: `src/__tests__/route-inventory.test.ts (5 tests)` passed in CI (TESTED). **The ~925 registration count is NOT TESTED.** CI logs never print it, and the test file has no numeric 925 assertion (details in C3).

Verified by Build lane from its own read-only cursor-github MCP calls and local Python/grep, Mon Oct 5 2026, 5:22 to 5:27 PM CT.
Nothing was pushed, merged, commented on, or edited. The repo was not cloned. Build set no DATABASE_URL, started no servers, and flipped no TESSERA_ENABLE_* flag.
Scratch: `/workspace/build-gate/work-TESSERA-PR1-postmerge-5c1137fa/` contains `tree-50876d40.json`, `tree-5c1137fa.json`, `tip-commit-patch.diff`, and `validate-job-112006094090.log`.

**Overlap header (read-only, not gated):** vitalitychems-dot/Gitbook main tip is `45651521a137c4448673d6abfaa77e1567230f83` ("Merge PR #10: GB-028 rev 3", 5:00:51 PM CT). Open PRs: **0** (both list_pull_requests state=open and search returned none).

---

## A. Tip and commit shape: PASS (TESTED)

1. `list_commits sha=main` returns newest `5c1137faeb7714482add93c2d6876396f34f1a03`, followed by `50876d40` → `76716c22` → `53856e22` → `6fc8a694`. A second check at about 5:26 PM CT returned the same tip.
2. `get_commit 5c1137fa`:
   - **Merge commit with 2 parents:** `50876d40cc1ed03538fa0dd4761231805292d5da` (first parent, previous main) and `76716c22d79085e1eb72c1e33ea9471b1c43103d` (PR #1 head, as pinned).
   - Tree: `3e48bd5f95e589708831a2f5721d2fa893925d5d`
   - Author Tessera; committer GitHub (web-flow); PGP signature verified=true.
   - Committed 2026-10-05 22:22:07 UTC = **5:22:07 PM CT**.
   - Message: "HYB-005: ignore unpatched braces advisory so CI can continue (#1)". Body: "IDENTITY: Tessera Admin coordinator / Father's standing approval of fixes (5:21 PM CT). Security PASS and Build PASS on head 76716c22 (CI run 37379320719 green). Narrow ignore of GHSA-vfj7-8cjw-p6xm, to be removed once braces is 3.0.4 or later."
   - Stats vs first parent: total 8, **+8 / −0**, 1 file: `pnpm-workspace.yaml` (modified), blob `cf1e10ee3fc366408f5c19b7c50f661e6aeb6752`.
3. `get_pull_request #1`:
   - state=closed, **merged=true**, merged_at 22:22:07 UTC (5:22 PM CT), merged_by vitalitychems-dot.
   - merge_commit_sha = `5c1137fa…`; head.sha = `76716c22…`.
   - 3 commits, +8/−0, changed_files=1.

## B. Tree equality, 5c1137fa == 50876d40 + pnpm-workspace.yaml only: PASS (TESTED)

1. I ran `get_git_tree recursive` on tree `42fb940d…` (50876d40) and tree `3e48bd5f…` (5c1137fa). Both returned **truncated=false** with 1569 entries each, and I diffed them locally with Python.
   - My fresh 50876d40 listing is byte-identical to the one saved by the PR #2 post-merge gate.
2. Results:
   - Added paths: **none**.
   - Removed paths: **none**.
   - Changed subtree entries: **none**. pnpm-workspace.yaml sits at the repo root, so no subtree SHAs move.
   - Changed blobs: **exactly 1**, `pnpm-workspace.yaml`: `fb46443d119afa183de4d2847f1b9c03801ef01b` → `cf1e10ee3fc366408f5c19b7c50f661e6aeb6752`, mode 100644 unchanged.
   - Unchanged blobs: 1384 of 1385.
3. PR head blob: the root tree of PR #1 head `76716c22` (tree `38e69808…`) lists `pnpm-workspace.yaml` = `cf1e10ee3fc366408f5c19b7c50f661e6aeb6752` (5641 bytes). This **exactly matches** the tip, so what landed is what was reviewed.
4. HYB-012 files are still present at the tip with the expected blobs:
   - `artifacts/api-server/src/__tests__/route-inventory.test.ts` = `ef96c712dabcd9353c459b5c3aeefa97e34abb0a` ✔
   - `artifacts/api-server/src/__tests__/route-inventory.ts` = `aa0aa604267d91059228a5de4154fc356448f0f9` ✔
5. Diff content (+8/−0): an 8-line comment plus `auditConfig: ignoreGhsas: [GHSA-vfj7-8cjw-p6xm]` block, inserted after `autoInstallPeers: false`. It has a review date of 2026-11-05 and a note to remove it once braces >=3.0.4 ships.

## C. CI validate on 5c1137fa: PASS (TESTED)

- `list_workflow_runs head_sha=5c1137fa…` returns 1 run: **37382015797** ("CI", `.github/workflows/ci.yml`, event=push, branch main, run #9, attempt 1). It was created at 5:22:10 PM CT, 3 seconds after the merge.
- `list_check_runs_for_ref 5c1137fa` returns 1 check run, `validate` (112006094090): completed / **success**, 5:22:16 to 5:25:18 PM CT. It has 2 annotations; the log shows one of them is the GitHub Node.js 20 deprecation warning for the actions. That is not a step failure.
- Polling: the first check at about 5:23 PM CT showed the audit already done and typecheck running. At about 5:24 PM, tests were done and build was running. At about 5:25 PM, the job was complete. I waited between polls with AwaitShell (75 s, then 60 s).

### C1. Step table (from `list_workflow_run_jobs` plus the job log; times CT)

| # | Step | Command (from log) | Result | Time |
|---|------|--------------------|--------|------|
| 6 | Install frozen workspace | `pnpm install --frozen-lockfile --ignore-scripts` | success | 5:22:47–5:23:02 |
| 7 | **Audit all dependencies** | `pnpm audit` → "1 vulnerabilities found / Severity: 1 high (1 ignored)" | **success** | 5:23:02–5:23:03 |
| 8 | **Typecheck** | `pnpm run typecheck` (tsc --build libs; api-server, mockup-sandbox, tessera, scripts all "Done") | **success** | 5:23:03–5:23:50 |
| 9 | **Apply schema to disposable CI DB** | `pnpm --filter @workspace/db run push` → drizzle-kit "[✓] Changes applied" (CI-only loopback `127.0.0.1:5432/tessera_test`) | **success** | 5:23:50–5:23:52 |
| 10 | **Run isolated workspace tests** | `pnpm test` → suite-policy 6/6 pass; vitest **14 files passed, 99 passed / 1 skipped (100)** | **success** | 5:23:52–5:24:01 |
| 11 | **Build all workspace applications** | `pnpm run build` (mockup-sandbox, api-server, and tessera builds all "Done") | **success** | 5:24:01–5:24:58 |

Steps 1–5 (setup, containers, checkout, pnpm setup, node setup) and the post/cleanup steps 19–23 all succeeded.

### C2. HYB-005 effect: CONFIRMED (TESTED)
- On 50876d40, CI stopped at the audit step because of GHSA-vfj7-8cjw-p6xm. On 5c1137fa the audit exits 0 with the advisory shown as "1 ignored".
- Every later step then ran and passed. The audit command itself is unchanged (`pnpm audit`).

### C3. HYB-012 route-inventory in CI: RAN AND PASSED (TESTED); 925 count NOT TESTED
- The log shows `✓ src/__tests__/route-inventory.test.ts (5 tests) 859ms`, including `✓ matches Express registrations for the two quantum modules 779ms`. This is the first time these tests have run green on main.
- **925 registrations: NOT TESTED.** The CI log never prints a registration total. The only "925" in the log is a Vite asset hash (`FrequencyMeter-925BjVjx.js`), which is unrelated.
- I read the test file at the tip (`get_file_contents`). It does not assert a fixed total. What it does assert:
  - the mounted modules equal `routeModuleFileNames()`;
  - `registrations.length > collapsedRouteKeyCount`;
  - hidden duplicates equal the allow-list surplus. There are 10 allow-listed METHOD+path collisions, each with 2 modules, so the surplus is 10;
  - live duplicates equal the allow-list exactly, including the 2 ruling-named quantum entries;
  - the Express registrations for system-runtime.ts and legacy-engines.ts match the source scan;
  - `GET /api/quantum/state` and `POST /api/quantum/gate` resolve to the system-runtime handlers.

  So CI proves the inventory is internally consistent and that exactly 10 duplicates are hidden. It does not prove a total of ~925.
- To make 925 TESTED, a future change would need to log the total or assert on it (e.g. `expect(registrations.length).toBe(925)`). That is a suggestion only. Build made no change.

## D. No ENABLE flips: PASS (TESTED)
- The pnpm-workspace.yaml diff has 0 matches for `ENABLE` (grep on the saved patch).
- The tree diff shows no other file changed (B2), so no flag file or env file was touched.
- The CI job log has 0 matches for `TESSERA_ENABLE`.
- Note: the route-inventory test sets a placeholder `DATABASE_URL` inside its own process so the route modules can be imported, and restores it afterwards. That is existing test code running in CI, not anything Build set.

---

## Verdict
**OVERALL PASS (TESTED).**
- Tip `5c1137fa` is a merge commit of `50876d40` and `76716c22`.
- The tree is exactly 50876d40 plus the PR #1 `pnpm-workspace.yaml` blob `cf1e10ee…`, with HYB-012 blobs intact.
- CI run 37382015797 `validate` passed end to end: audit (1 ignored), typecheck, db push, tests (99 passed, including route-inventory 5/5), and build.
- Only open item, which does not block: the ~925 registration count is not shown in CI output, so it stays NOT TESTED.
