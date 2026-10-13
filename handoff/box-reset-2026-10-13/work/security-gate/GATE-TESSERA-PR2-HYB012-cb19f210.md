# SECURITY GATE: TESSERA PR #2 (HYB-012), head cb19f210

- Gate run: Mon Oct 5, 2026, 5:16 PM CT. Read-only: nothing in the repo was changed. No secrets printed.
- PR: https://github.com/vitalitychems-dot/TESSERA/pull/2, "HYB-012: route inventory test (test-first, no runtime change)"
- State: open, not draft, not merged, mergeable=true, mergeable_state=unstable (CI is red; see CI below)
- Head: `tessera/hyb-012-route-inventory` @ cb19f210dd4fa62c4d9b77b25a2f24b9df133d87 (matches the receipt)
- Base: `main` @ fec56eb09d19907832663d5f16fcbc24f3d00317 (matches the receipt; this is still the main HEAD)
- Agent: Cursor cloud agent bc-78705fed-bceb-5859-add0-494439ea6dae (linked in the PR footer)

## VERDICT: PASS (security), with advisories
The PR adds 2 files and 530 lines, deletes 0, and has 1 commit. Both files are test files under `artifacts/api-server/src/__tests__/`. The commit is signed by Cursor Agent with a verified SSH signature, and Tessera is the co-author. I found no secrets, no external network calls, no ENABLE flips, no dependency changes and no runtime edits. The PR is not Manus-authored. Merging still needs Father's explicit "merge".

## 1) Provenance and signing: PASS
| Field | Value |
|---|---|
| Path | PR from a feature branch. Not a direct push to main. |
| Commits | 1 (cb19f210), parent = fec56eb (base) |
| Author/committer | `Cursor Agent <cursoragent@cursor.com>` (GitHub user `cursoragent`) |
| Co-author trailer | `Co-authored-by: Tessera <vitalitychems-dot@users.noreply.github.com>` |
| Signature | **verified=true, reason=valid, SSH (ssh-ed25519)**, verified 2026-10-05 5:14 PM CT |
| Commit time | 2026-10-05 5:14 PM CT. PR opened 5:15 PM CT. |
| PR opener | vitalitychems-dot (OWNER), through the Cursor agent PR body markers |
| Manus markers | **None.** No `Manus Consolidation` author, no float-noreply (`3.32565808e+08+...`) committer, no manus-connector, and the commit is not unsigned. |

## 2) Secrets / network / ENABLE / deps / runtime: PASS
- **Secrets:** none. The only credential-shaped string is a **non-secret placeholder** `DATABASE_URL` that points to loopback (127.0.0.1:5432, user "route-inventory", password literally "unused"). It is set only when `DATABASE_URL` is unset and is restored in `afterAll`. Advisory: secret scanners may flag this pattern, but it is not a real credential.
- **Network:** the test starts an in-process Express server on `127.0.0.1:0` (an ephemeral loopback port), and `fetch` only reaches `http://127.0.0.1:<port>`. There are no external hosts and no exfiltration path. The only URL that isn't loopback is the Gitbook ruling link, and it appears in a code comment only.
- **Filesystem:** `route-inventory.ts` uses only `readFileSync`/`readdirSync` on `../routes` (read-only). It does not write anything.
- **ENABLE flips:** none. The diff contains no `TESSERA_ENABLE_*` and no env writes other than the placeholder above.
- **Dependencies:** no `package.json`, lockfile or `pnpm-workspace.yaml` changes. The test imports only existing modules: `vitest`, `express`, `node:http`, `node:fs`, `node:path` and `node:url`.
- **Runtime/production edits:** none. No changes to route modules, `app.ts`, `routes/index.ts` or `lib/`. `vi.mock("../lib/autonomous-wiring")` stubs the scheduler in the test only, so importing `legacy-engines.ts` does not start background work.
- Advisory: the test dynamically imports `routes/system-runtime` and `routes/legacy-engines`. Any other module-scope side effects in those files (beyond the mocked scheduler) would run during the test. I didn't audit them because they are unchanged production code.

## 3) Scope matches the claim: PASS
| File | Status | +/- |
|---|---|---|
| artifacts/api-server/src/__tests__/route-inventory.test.ts | added | +295 / -0 |
| artifacts/api-server/src/__tests__/route-inventory.ts | added | +235 / -0 |
| **Total** | 2 files | **+530 / -0** (matches the reported scope) |

## 4) S-2 (Replit app "29" / 1T homepage promotion): no flag
Nothing in the diff, commit message or PR body mentions Replit, app "29", "1T" or a homepage promotion.

## CI (informational, does not block the security gate)
- The `validate` check on cb19f210 **failed** at the `pnpm audit` step: 1 high-severity advisory, `braces <=3.0.3` (GHSA-vfj7-8cjw-p6xm, no patched version), path `artifacts__mockup-sandbox>fast-glob>micromatch>braces`.
- **This failure already exists on main:** the same `validate` check also fails on base fec56eb. The PR changes no dependencies.
- Because audit fails first, CI did **not** run this PR's typecheck or tests. The pass results for typecheck, test and vitest (5 tests) come from the agent's own report, not from CI.

## Context outside this PR (advisory only)
- The last 3 commits on `main` (fec56eb, 9a0323f, 216e4e8) were authored by `Manus Consolidation <manus@users.noreply.github.com>`, have the float-noreply committer `3.32565808e+08+vitalitychems-dot@...` and are **unsigned**. They look like direct-to-main pushes. This predates PR #2 and is not introduced by it, but the branch builds on that base. Recommend a separate Security review of main's Manus history.

## Merge condition
PR #2 can merge only after Father's explicit word "merge". Neither the Tessera agent nor Security merges it.
