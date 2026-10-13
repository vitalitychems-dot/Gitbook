# Build Gate — vitalitychems-dot/TESSERA PR #2 @ cb19f210

**RESULT: FAIL (TESTED)** — verified by Build lane from its own read-only GitHub MCP calls, Mon Oct 5 2026, about 5:18 PM CT.
Nothing was pushed, merged, commented on, or edited. The repo was not cloned. No DATABASE_URL was set by Build, no servers were started against a real DB, and no TESSERA_ENABLE_* flag was touched.

## PR
- URL: https://github.com/vitalitychems-dot/TESSERA/pull/2
- Title: "HYB-012: route inventory test (test-first, no runtime change)"
- State: open, not draft, not merged; 1 commit; changed_files=2, additions=530, deletions=0
- Head: `tessera/hyb-012-route-inventory` @ `cb19f210dd4fa62c4d9b77b25a2f24b9df133d87` (exact match)
- Base: `main` @ `fec56eb09d19907832663d5f16fcbc24f3d00317`
- mergeable=true, rebaseable=true, mergeable_state=`unstable` (after CI settled — required check red)
- Cloud agent bc-78705fed will not merge it (accepted)

## Base / main
- `get_commit ref=main`: tip is still `fec56eb09d19907832663d5f16fcbc24f3d00317` ("Remove stale workspace lockfile entries"). No drift. PR base equals current main.

## 1. File scope — PASS (TESTED)
- `list_pull_request_files`: exactly **2** files, both status=`added` (additions only):
  1. `artifacts/api-server/src/__tests__/route-inventory.ts` (+235/−0)
  2. `artifacts/api-server/src/__tests__/route-inventory.test.ts` (+295/−0)
- Total +530/−0 matches claim. No other paths.

## 2. No runtime change — PASS (TESTED)
- Diff only under `artifacts/api-server/src/__tests__/`.
- No route modules, no `routes/index.ts`, no `app.ts`, no response-contract changes in the PR file list.

## 3. No TESSERA_ENABLE_*, secrets, or dependency adds — PASS (TESTED)
- Grep of both new file bodies (`get_file_contents` at head): no `TESSERA_ENABLE_*`.
- No `package.json` / `pnpm-lock.yaml` / `pnpm-workspace.yaml` in the PR file list (no new deps).
- Test file sets a **placeholder** `DATABASE_URL=postgresql://[REDACTED]@127.0.0.1:5432/route_inventory` only when unset, for module import; restores it in `afterAll`. Not a secret; Build lane did not set DATABASE_URL itself.
- No password/token/secret credentials introduced.

## 4. CI green on exact head — FAIL (TESTED)
- `list_check_runs_for_ref` on `cb19f210dd4fa62c4d9b77b25a2f24b9df133d87`: 1 check, `validate`, head_sha exact match, status=completed, **conclusion=failure**.
- Workflow run `37381241741` (CI, pull_request, run #7): head_sha exact, conclusion=**failure**.
- Failed step: **Audit all dependencies** (`pnpm audit`) — high advisory on `braces` <=3.0.3 (GHSA-vfj7-8cjw-p6xm) via `artifacts/mockup-sandbox > fast-glob > micromatch > braces`. Exit code 1.
- Typecheck / schema / tests / build were **skipped** after audit failure. GitHub Actions never executed the route-inventory vitest on this head.
- Context (not a waiver): same audit failure exists on `main` @ fec56eb (workflow runs 1–3 all conclusion=failure). Open PR #1 (HYB-005 audit ignore) is the intended CI unblock; it is **not** in this PR’s base. Required-check rule remains: every required check success — **not met**.
- mergeable_state after settle: `unstable`.

Cloud-agent local claims (`pnpm typecheck` / `pnpm test` / vitest route-inventory 5 tests) stay **REPORTED** — not confirmed by GitHub CI on this head, and Build lane did not re-run them (no clone / no local workspace).

## 5. Inventory claims — PARTIAL (TESTED / REPORTED)
- Mounted modules from `routes/index.ts` at head: **85** `router.use(...)` mounts (TESTED). Matches PR claim of 85 modules.
- Allow-list in `route-inventory.test.ts` at head: **exactly 10** `DuplicateRoute` entries (TESTED), including:
  - Scope: `GET /quantum/state`, `POST /quantum/gate` (modules `system-runtime.ts` then `legacy-engines.ts`)
  - Other 8 named in PR body: `GET /consciousness/state`, `GET /consensus/proposals`, `GET /dual-brain/state`, `GET /emotional/profile`, `GET /universe/metrics`, `POST /consensus/propose`, `POST /improvement/cycle`, `POST /universe/simulate`
- Presence of those 10 METHOD+path pairs as duplicates was spot-checked in owning route sources at head (system-runtime, legacy-engines, sovereign-engines, governance-consensus, universe, improvement) — TESTED for key presence/ownership order.
- Absolute count **~925 registrations**: **REPORTED** only (PR body + cloud-agent bc-78705fed transcript Python scan: `registrations 925 unique keys 915 duplicate keys 10`). Inventory helper does not hardcode 925; Build lane did not clone and CI never reached tests, so Build did not independently recompute 925. Unique keys would be 915 if 925−10 surplus holds (each of 10 dups contributes +1 surplus).

## 6. Fail-case behavior A and B — PASS (TESTED, static)
Read `route-inventory.test.ts` thoroughly. Critical assertion:

```ts
const live = duplicateRoutes(registrations).slice().sort(byMethodPath);
const allowed = DUPLICATE_ROUTE_ALLOW_LIST.slice().sort(byMethodPath);
expect(live).toEqual(allowed);
```

Plus surplus check:
```ts
expect(hidden).toBe(allowListSurplus); // hidden = registrations.length - collapsed
```

- **(A) New exact duplicate METHOD+path not on allow-list → FAIL:** `duplicateRoutes` would include the new key; `live` ≠ `allowed` (set equality of sorted duplicate lists). Also `hidden` would exceed `allowListSurplus`.
- **(B) Allow-listed duplicate disappears (no longer duplicated / allow-list mismatch) → FAIL:** if a listed key is no longer duplicated, it drops out of `duplicateRoutes` so `live` ≠ `allowed`. If removed from the allow-list while still duplicated, same inequality. Surplus check also fails when registration count of a listed dup drops.

Static analysis is unambiguous (exact array equality of sorted live vs allow-list). No CloudAgent mutation/vitest run was required. CloudAgent launch tool was not available in this session’s dynamic catalog.

## 7. Mergeability vs base — PASS with unstable CI
- Main tip still fec56eb (TESTED).
- PR still mergeable=true against base; mergeable_state=`unstable` because validate failed.

## Verdict drivers
| Check | Result |
|---|---|
| 2 new test files only | PASS |
| No runtime / ENABLE / deps | PASS |
| CI green on exact head | **FAIL** (audit braces; tests skipped) |
| 925 / 10 allow-list | 10 allow-list PASS; 925 REPORTED |
| Fail-cases A & B | PASS (static) |
| Main tip / mergeable | main OK; mergeable=true, state=unstable |

**Overall: FAIL** until required CI `validate` is green on `cb19f210…` (or a successor head). Likely depends on landing HYB-005 audit ignore (PR #1) or equivalent before/with this PR — out of scope for Build to fix.

## Evidence IDs
- PR: 4751395714 / number 2
- CI run: 37381241741 / job 112003488132
- Head: cb19f210dd4fa62c4d9b77b25a2f24b9df133d87
- Base/main: fec56eb09d19907832663d5f16fcbc24f3d00317
