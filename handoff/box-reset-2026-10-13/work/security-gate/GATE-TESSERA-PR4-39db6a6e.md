# Security gate — TESSERA PR #4 @ 39db6a6e (extra scrutiny: eval harness + tests)

- Gate run: 2026-10-05 18:16 CDT (CT), read-only. Nothing merged, pushed, or commented. LEDGER.md not touched.
- Repo: vitalitychems-dot/TESSERA, PR #4 "Add offline eval harness and route/health contract tests" (draft, open, not merged)
- Branch: cursor/eval-harness-tests-5146 → main (base 5c1137faeb7714482add93c2d6876396f34f1a03)
- Expected head: 39db6a6ec1c74411b1d2cae5e48791aace6abb0a
- Live head:     39db6a6ec1c74411b1d2cae5e48791aace6abb0a — **MATCH**
- RECEIPT cross-check: Tessera Admin "PR #4 39db6a6e" — matches.
- Patch copy for audit: work-tessera-pr4/pr4.patch

## VERDICT: PASS (with non-blocking FLAGs)

## Authorship
- 1 commit, 39db6a6e. Author/committer: Cursor Agent <cursoragent@cursor.com> (GitHub user cursoragent). Commit time 2026-10-05 18:06 CT.
- Trailer: Co-authored-by: Tessera <vitalitychems-dot@users.noreply.github.com>. GitHub signature: verified (SSH, valid).
- Manus: none. Replit: none.

## Files (16; +1064 / −120)
| File | Status | Security note |
| --- | --- | --- |
| artifacts/api-server/scripts/eval-chatbot.ts | mod +11/−25 | CASES moved out. main() now runs **only when invoked directly** (import.meta.url === argv[1]). Before this change, importing the file ran the live quiz, so the change **removes** an import-time side effect. |
| src/eval/chatbot-cases.ts | add | Static prompt table only. No I/O. |
| src/__tests__/eval-chatbot-cases.test.ts | add | Pure assertions on CASES. |
| src/lib/eval-os-metrics.ts | add | Moves the 4 OS scorers out unchanged (the score bands are identical to the removed code). Uses only node `os`/`process`. No db, network, or timers. |
| src/lib/eval-runner.ts | mod +1/−93 | Imports the moved functions instead of defining them. No other logic change. The provider-registry and sovereign-engine imports already existed and are unchanged. |
| src/__tests__/eval-runner-os-metrics.test.ts | add | Pure unit tests. Reads local OS stats only. |
| src/__tests__/healthz.test.ts | add | Mounts the health router on an ephemeral **127.0.0.1:0** server and fetches it over loopback. Closes it in afterAll. |
| src/__tests__/route-inventory.test.ts | mod +161 | Mocks the whole file's @workspace/db with a client that always rejects ("probe-db-offline"). Adds a registration-total assertion (925). Adds 8 HTTP shape probes against a loopback 127.0.0.1:0 server. The improvement/cycle probe hits the mocked offline db. I checked routes/improvement.ts at the head: that path makes only db/stat calls, with no LLM or provider call. |
| src/__tests__/routes-index-import.test.ts | add | Imports routes/index with **all six module-load starters mocked** (startWalletObserver, startAutonomousBuildCycleTimer, startFreeStuffScraper, startBountyRefresher, startIncomeExecutor, initShepherdPersistence) plus autonomous-wiring.startAutonomousOperation. Uses fake timers, clearAllTimers, and restores env afterward. Sets a synthetic FATHER_NATAL_CHART_JSON (year 2000, "Synthetic Test Location"). |
| docs/eval/README.md | add | Docs. Explicitly makes no MMLU/GSM8K/HumanEval claims. |
| package.json | mod | Adds a `merge-gate` script. No dependency changes. |
| scripts/eval/write-result.mjs | add | Builds a JSON record from CLI args and refuses /mmlu/i. Writes to a file only if --out is given, and only when invoked directly. No network. |
| scripts/eval/write-result.test.mjs | add | node:test. Spawns the script with a temp-dir output only. |
| scripts/historical-merge-gate.mjs | add | Static: reads local files plus `git ls-files`. `--run-suite` (opt-in) runs pnpm typecheck/test/build/audit. Runs nothing at import. |
| scripts/historical-merge-gate.test.mjs | add | Runs the static report only (no --run-suite). |
| scripts/package.json | mod | The test script adds the two new node:test files. |

## PR #4 extra-scrutiny checks
### Network at import / collect time
- None to external hosts. The only fetch targets in tests are ephemeral `http://127.0.0.1:<port>` servers the tests start and stop themselves.
- eval-chatbot.ts (EVAL_BASE_URL, default http://localhost:5000) no longer runs on import. It is not in `pnpm test`.
- No axios, got, undici, or external URLs in the added code. No new dependencies.
### Secrets in code / fixtures
- None real. One dummy loopback connection string: `postgresql://[REDACTED]@127.0.0.1:5432/routes_index_smoke`. It is used only if DATABASE_URL is unset, restored in afterAll, and its password is literally "unused" → FLAG-1 (scanner noise only).
- Natal chart fixture is synthetic and contains no personal data.
### Module-load side effects
- The new modules (chatbot-cases, eval-os-metrics, write-result, historical-merge-gate) have none. Script entry points are guarded by invokedDirectly.
- routes/index.ts (unchanged here) **does** start wallet observer, scraper, bounty refresher, income executor, build-cycle timer, and shepherd persistence at module load. That behavior is already on main. The new test mocks every one of these and asserts they are called → FLAG-2 (existing risk; test is correctly sandboxed).
### Paid / external LLM
- Not called by any test. eval-chatbot.ts talks to the operator's own API by default (localhost) and only runs manually, as before.

## Hard forbids
- TESSERA_ENABLE_*: none. Committed secrets: none. Wallet/payments/blockchain creds: none. Wallet code appears only as vi.fn mocks. 1T: not touched. Data/test deletions: none. route-inventory.test.ts gains code and loses none; the eval-runner.ts removal is a move into eval-os-metrics.ts. .github/workflows/*: not touched. The merge gate is a local script, as the PR body states.

## FLAGs (non-blocking)
1. **FLAG-1** Dummy loopback DATABASE_URL with password "unused" in routes-index-import.test.ts. It is not a secret, but secret scanners may trip on it. Optional: build it from parts or use a no-password URL.
2. **FLAG-2** Pre-existing: importing routes/index starts six background jobs at module load, including wallet observer, scraper, and income executor. The test contains this with mocks plus fake timers. Any future test that imports routes/index without these mocks would trigger live side effects. Remediation is out of scope for this PR.
3. **FLAG-3** routes-index-import imports about 90 route modules for real. Only the six starters plus autonomous-wiring are mocked, and other modules' module-scope behavior is covered only by fake timers and the dummy loopback DB. The PR body reports the suite passed locally (116 passed / 1 skipped); Build should confirm in CI with no egress.
4. **FLAG-4** (info) `pnpm run merge-gate --run-suite` runs `pnpm audit`, which contacts the npm registry. It is opt-in only and not used in tests.
