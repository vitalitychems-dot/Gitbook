# GATE 2026-10-05 — TESSERA PR #3 / #4 / #5 pre-merge (Build, verify-only)

Lane: Build (verify-only). No push, merge, comment, branch edit, DATABASE_URL, server, flag flips, LEDGER.md, or messages.
Source: cursor-github MCP (read-only). No clone; no local run (no disposable TESSERA git checkout under /workspace).
Checked: 2026-10-05 ~6:17 PM CT.

## Tips / overlap first (TESTED)
- main tip = `5c1137faeb7714482add93c2d6876396f34f1a03` (unchanged; HYB-005 merge #1).
- Open PRs on TESSERA: exactly #3, #4, #5 (all draft, base main @ 5c1137fa, created 6:09 PM CT, 1 commit each).

| PR | head (API) | matches receipt | base | draft | mergeable | mergeable_state |
|----|-----------|-----------------|------|-------|-----------|-----------------|
| #3 hygiene `cursor/code-hygiene-5146` | a01b50e9ce997b9a5f4dcd600f14bf0338ee9805 | YES | main 5c1137fa | true | true | clean |
| #4 eval `cursor/eval-harness-tests-5146` | 39db6a6ec1c74411b1d2cae5e48791aace6abb0a | YES | main 5c1137fa | true | true | clean |
| #5 docs `cursor/docs-readme-config-5146` | 820d0be57d88fb463bcef74e1ca06e04c4ae6dd7 | YES | main 5c1137fa | true | true | clean |

## PR #3 — PASS (TESTED)
- Files (3, +8/−10): `.gitignore` (−10), `routes/legacy-engines.ts` (+4 comment), `routes/system-runtime.ts` (+4 comment).
- `.gitignore`: removed block is byte-identical to the block that remains directly above it (verified via get_file_contents at head: `.env`, `.env.*`, `!.env.example`, `*.pem`, `*.key`, `credentials*.json`, `secrets*.json`, `service-account*.json` still present). Ignore behavior unchanged.
- Route files: comment lines only above `GET /quantum/state`; handlers untouched; `// @ts-nocheck` kept.
- Forbidden: none (no .github/workflows, secrets, wallets, payments, TESSERA_ENABLE_*).
- API response changes: none.
- CI: run 37386859599 / job 112022133361 `validate` completed **success** (6:09–6:12 PM CT) on merge ref 6be2e3f (a01b50e9 into 5c1137fa). Log: install frozen, audit `1 high (1 ignored)`, typecheck pass, scripts node:test 6/6, API vitest 14 files **99 passed | 1 skipped**, build pass. Matches PR body claim.

## PR #4 — PASS (TESTED)
- Files (16, +1064/−120):
  - modified: `scripts/eval-chatbot.ts` (+11/−25; CASES moved out, main() only when entry), `__tests__/route-inventory.test.ts` (+161), `lib/eval-runner.ts` (+1/−93; OS-metric fns moved), `package.json` (+2/−1 `merge-gate` script), `scripts/package.json` (+1/−1 test list)
  - added: `__tests__/eval-chatbot-cases.test.ts`, `__tests__/eval-runner-os-metrics.test.ts`, `__tests__/healthz.test.ts`, `__tests__/routes-index-import.test.ts`, `src/eval/chatbot-cases.ts`, `src/lib/eval-os-metrics.ts`, `docs/eval/README.md`, `scripts/eval/write-result.mjs` + test, `scripts/historical-merge-gate.mjs` + test
- Scope: tests + offline eval harness + refactor-by-move. `eval-os-metrics.ts` functions are byte-equivalent in score bands, pass lines (uptime still always passes), ids, names, evidence strings → `/evaluation/*` output unchanged. CASES array identical.
- Test hygiene: `@workspace/db` mocked offline in route-inventory; route-index import test mocks all starters (wallet observer, income executor, bounty, scraper, autonomy) + fake timers; sets a fake loopback `DATABASE_URL` in-process only if unset and restores it (test-only, no real DB). Synthetic natal chart only.
- Forbidden: none. No workflow edit (merge-gate is a script, `--run-suite` opt-in). No TESSERA_ENABLE_* (0 hits in diff). Wallet references are mocks only.
- API response changes: none (new probes *assert* existing shapes: consciousness/consensus/dual-brain/emotional/universe metrics, propose 400, improvement 500 offline envelope, simulate 400/200).
- CI: run 37386858947 / job 112022131049 `validate` **success** (6:09–6:13 PM CT) on merge ref 5c7817b. Log: typecheck pass, scripts node:test **14/14**, API vitest **18 files, 116 passed | 1 skipped (117)**, `[route-inventory] registration total=925`, build pass.
- "116 passed, 1 skipped": **TESTED** (seen in CI log), not just REPORTED.

## PR #5 — PASS (TESTED)
- Files (10, +55/−11): `.env.example` (+4/−1 comments only, names blank, no values), `README.md` (+17: eval commands, CI section, mesh pointer), `archives/README.md`, `docs/CONSOLIDATION.md`, `docs/PROJECT_MAP.md`, `docs/SECRETS.md`, `docs/TESSERA_SYSTEM.md` (honesty labels), `docs/VALIDATION-STATUS.md`, `docs/migration-review/VALIDATION.md`, `pnpm-workspace.yaml` (+2/−1).
- `pnpm-workspace.yaml`: `allowBuilds.core-js` placeholder string → `false` (explicit deny of core-js postinstall). Not API/flag/secret. NOTE: CI installs with `--ignore-scripts`, so CI does not exercise this; local `pnpm install` may now stop warning about the unset placeholder. Low risk.
- README CI description (install → audit → typecheck → db push → test → build) matches actual CI step order (TESTED from log). Workflow only linked, not edited.
- Forbidden: none. API response changes: none (docs/config text).
- CI: run 37386858861 / job 112022131141 `validate` **success** (6:09–6:12 PM CT) on merge ref f3ce36c. API vitest 14 files **99 passed | 1 skipped**, scripts 6/6, build pass.

## Stack 3 → 4 → 5 on 5c1137fa — CLEAN
- File overlap: #3∩#4 = ∅, #3∩#5 = ∅, #4∩#5 = ∅ (computed from list_pull_request_files). No textual conflict possible.
  - After #3: #4 applies clean (no shared paths). After #3+#4: #5 applies clean (no shared paths).
- Semantic cross-checks (static):
  - #3 comments in route files do not change route registrations → #4's `registration total=925` assertion holds.
  - #4 `historical-merge-gate` reads `pnpm-workspace.yaml` (#5 edits it): `packages:` parser stops at the next top-level key (`allowBuilds:`), and #5 adds no stale-app strings to scanned manifests → gate test stays green.
  - #5 README references `artifacts/api-server/scripts/eval-chatbot.ts` (exists on main and after #4); does not link `docs/eval/README.md`.
- Caveat: combined tree (3+4+5) has NOT been CI-run (each PR CI ran alone vs 5c1137fa). If branch protection requires up-to-date branches, #4/#5 may show `behind` after each merge and need an update-branch before merge.

## Merge advice
Merge #3 → #4 → #5 in that order on 5c1137fa (no shared files); after each merge, confirm main CI `validate` green before the next, and expect API vitest 116 passed | 1 skipped on main after #4.

## Addendum (parent steering, 6:17 PM CT): Security PASS on all three heads noted

### 1. PR #5 `core-js: false` → pnpm install
- **TESTED (CI, limited to --ignore-scripts):** run 37386858861 on merge ref f3ce36c (820d0be5 into 5c1137fa), step `pnpm install --frozen-lockfile --ignore-scripts` (pnpm v11.25.0): "Lockfile is up to date", "✓ Lockfile passes supply-chain policies (766 entries)", 750 packages added, "Done in 8.6s". No core-js, allowBuilds, or ignored-build warnings in the log. Audit next: `1 high (1 ignored)`, exit ok.
- **REPORTED / static, not tested:** a plain `pnpm install` that runs lifecycle scripts. CI always passes `--ignore-scripts`, so `allowBuilds` is never checked there. No local run (no checkout; clone not allowed). Risk is low: `false` only denies core-js's postinstall (a funding banner). esbuild stays `true`. Before this change the value was a placeholder string that was not a boolean. The lockfile is unchanged (frozen install passed).

### 2. PR #4: suite with outbound network blocked
- **TESTED:** 116 passed | 1 skipped (117), 18 files, in CI log job 112022131049. The skip is the existing `evolution-sandbox-loop.test.ts` (also skipped on main and #3/#5). node:test 14/14.
- **Not tested with network blocked:** the GitHub-hosted `ubuntu-latest` runner has normal network, and ci.yml adds no egress block.
- **Static evidence (REPORTED):**
  - Every test `fetch` targets a `127.0.0.1:<ephemeral>` server made in the test (healthz, route-inventory `request()`).
  - `@workspace/db` is replaced with an offline mock that rejects (`probe-db-offline`) in route-inventory.
  - routes-index-import mocks every background starter (wallet observer, scraper, bounty refresher, income executor, autonomy, shepherd) and uses fake timers plus clearAllTimers.
  - eval-chatbot-cases imports `src/eval/chatbot-cases.ts` only, and `main()` is entry-gated. os-metrics and write-result/merge-gate tests are local only (os/process/fs/git ls-files).
  - The CI test step log has 0 hits for ENOTFOUND, ECONNREFUSED, getaddrinfo, ETIMEDOUT, "fetch failed" or external URLs.
  - Leftover risk: side effects at module scope in the many route modules that routes/index imports. Not proven offline without a sandboxed local run.

### 3. Dummy DB password literals marked "unused"
- **New in PR #4:** `artifacts/api-server/src/__tests__/routes-index-import.test.ts`, `postgresql://[REDACTED]@127.0.0.1:5432/routes_index_smoke`. It is set in-process only when DATABASE_URL is unset, then restored.
- **Already on main (not added by these PRs):**
  - route-inventory.test.ts `postgresql://[REDACTED]@127.0.0.1:5432/route_inventory` (HYB-012)
  - ci.yml `POSTGRES_PASSWORD: [REDACTED]` / `tessera_test:test-only@127.0.0.1`
- None in #3 or #5. The `.env.example` names in #5 stay blank.
- **Scan outcome:**
  - ci.yml has no gitleaks/trufflehog/secret-scan step.
  - Check runs on all three heads are only `validate` (success). No code-scanning or secret-scanning check run exists.
  - `pnpm audit` scans dependencies, not source. It passed with `1 high (1 ignored)`, the existing braces GHSA.
  - GitHub secret-scanning alerts: NOT CHECKED (no read tool for that API here; private repo).
  - Non-blocking: CI did not fail. The literal is a loopback placeholder with password `unused`, not a credential.

### Overall (unchanged)
- #3 PASS (TESTED); #4 PASS (TESTED; "offline" is REPORTED/static); #5 PASS (TESTED; install TESTED with --ignore-scripts only).
- Stack 3→4→5: CLEAN.
