# GATE 2026-10-05 — TESSERA post-merge tip `9c0fa1cd` (Build, verify-only)

**OVERALL: PASS (TESTED)**

Lane: Build (verify-only). No push, merge, comment, clone, LEDGER edit, flag flips, or messages.
Source: cursor-github MCP (read-only). Checked: 2026-10-05 ~6:52 PM CT.

## 1. Main tip: PASS (TESTED)
- `list_commits sha=main` / `get_commit ref=9c0fa1cd…`: tip = `9c0fa1cdc0812753cce0301d216eac57dcb9eb5b` (exact match to expected).
- Message: "Merge PR #8: memory redaction patterns (Security+Build PASS)"
- Author Tessera; committer GitHub (web-flow).
- Committed 2026-10-05 23:48:46 UTC = **6:48 PM CT**.

## 2. Ancestry / claimed merges: PASS (TESTED)
| | SHA (full) | Role |
|--|------------|------|
| tip | `9c0fa1cdc0812753cce0301d216eac57dcb9eb5b` | Merge PR #8 onto main |
| parent1 | `7566781070ab8a68898968adae26a9c8cddabbb0` | #6 merge commit |
| parent2 | `25183afb894194cb28c17ef3898b70b81d2115cb` | #8 PASS head |

#6 merge `7566781070ab8a68898968adae26a9c8cddabbb0`:
| | SHA (full) | Role |
|--|------------|------|
| merge | `7566781070ab8a68898968adae26a9c8cddabbb0` | Merge PR #6 onto prior tip |
| parent1 | `004b692e4f84a49a4a0fa863f2868a64b7566a3c` | Prior main tip |
| parent2 | `e898111ae9fe730ad214ec63f9173d338a9df53e` | #6 Security-repass / Build PASS head |

- Order confirmed: prior tip `004b692e` → #6 merge `75667810` (head `e898111a`) → #8 merge tip `9c0fa1cd` (head `25183afb`).
- Security re-pass of #6 at `e898111a` noted as REPORTED context (not re-audited here).

## 3. CI on tip: PASS (TESTED)
- Workflow run **37390612481** (CI / `ci.yml`, push, main, run #24)
- Job `validate` id **112034523610**
- Status: completed; **conclusion: success**
- Window: started 23:48:50 UTC (6:48 PM CT) → finished 23:51:15 UTC (6:51 PM CT)
- URL: https://github.com/vitalitychems-dot/TESSERA/actions/runs/37390612481

### Steps (all success)
| # | Step | Result |
|---|------|--------|
| 1–5 | setup / containers / checkout / pnpm / node | success |
| 6 | Install frozen workspace | success |
| 7 | Audit all dependencies | success |
| 8 | Typecheck all applications and libraries | success |
| 9 | Apply schema to disposable CI database | success |
| 10 | Run isolated workspace tests | success |
| 11 | Build all workspace applications | success |

## 4. Test counts from job logs: PASS (TESTED)
From `get_job_logs` job 112034523610:

- scripts node:test: `# tests 14` / `# pass 14` / `# fail 0` / `# skipped 0`
- gitbook-mcp vitest: `Test Files  1 passed (1)` / `Tests  30 passed (30)`
- API vitest (`pnpm test` → `test-unified.mjs`): `Test Files  19 passed (19)` / `Tests  121 passed | 1 skipped (122)`
- learning-memory in suite: `learning-memory.test.ts (5 tests)` ✓
- `[test] Tessera learning memory` / `vitest run src/__tests__/learning-memory.test.ts`: `Test Files  1 passed (1)` / `Tests  5 passed (5)` (test:memory path)
- `[route-inventory] registration total=925`

**Expected post-#6+#8: API 121 passed | 1 skipped; gitbook-mcp 30; learning-memory 5: CONFIRMED (TESTED from logs).**

## 5. Other jobs / steps
- **audit:** success — log `1 vulnerabilities found` / `Severity: 1 high (1 ignored)` (braces GHSA ignore)
- **typecheck:** success (incl. `artifacts/gitbook-mcp typecheck: Done`)
- **db schema push:** success (`[✓] Changes applied`)
- **build:** success (incl. `artifacts/gitbook-mcp build: Done`; mockup-sandbox + tessera vite; api-server)

## One-line for Tessera
PASS postmerge tip 9c0fa1cdc0812753cce0301d216eac57dcb9eb5b CI run 37390612481 success; #6 then #8 (parents 75667810+25183afb; #6 parents 004b692e+e898111a); vitest 121 passed | 1 skipped (19 files); gitbook-mcp 30/30; learning-memory/test:memory 5/5; node:test 14/14; audit/typecheck/db/build all success.

## Report path
`/workspace/build-gate/GATE-2026-10-05-TESSERA-postmerge-9c0fa1cd.md`
