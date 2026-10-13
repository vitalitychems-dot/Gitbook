# GATE 2026-10-05 — TESSERA PR #6 / #7 pre-merge (Build, verify-only)

Lane: Build (verify-only). No push, merge, comment, clone, branch edit, DATABASE_URL, server, flag flips, LEDGER.md, or messages.
Source: cursor-github MCP (read-only). No local checkout/run.
Checked: 2026-10-05 ~6:38 PM CT. Fresh gate (prior attempt interrupted with no report).

## Tips / overlap first (TESTED)
- main tip = `b16796591c3f92d76290d827ac41c8ffcc975182` (unchanged; post-merge #3→#4→#5).
- Open PRs on TESSERA: exactly #6 and #7 (both draft, base main @ b1679659).

| PR | head (API) | matches receipt | base | draft | mergeable | mergeable_state |
|----|-----------|-----------------|------|-------|-----------|-----------------|
| #6 Gitbook MCP `cursor/gitbook-mcp-connector-301f` | d9c4f1e04c87595998f54bcc2a44afd6c8a1b587 | YES | main b1679659 | true | true | clean |
| #7 learning memory `cursor/tessera-learning-memory-301f` | f57c40aa3863a8f688fb0e61e75bee289c296baa | YES | main b1679659 | true | true | clean |

## PR #6 — PASS (TESTED)
- Head pin: `d9c4f1e04c87595998f54bcc2a44afd6c8a1b587` matches receipt exactly.
- Files (21, +2209/−0): new package `artifacts/gitbook-mcp/` (17 added: README, agents.json, package.json, src/*, vitest/tsconfig), plus `.env.example` (+8 blank `GITBOOK_*` names), `README.md` (+1 bullet), `pnpm-lock.yaml` (+70), `scripts/test-unified.mjs` (+1 Gitbook MCP suite entry).
- Base contains b1679659: YES (API base.sha = tip).
- Forbidden: **none**
  - No `.github/workflows` edits.
  - `.env.example` adds blank names only (`GITBOOK_GITHUB_TOKEN=` etc.); no values.
  - Test fixture `[REDACTED]` in `service.test.ts` is a mock used to assert redaction to `[REDACTED]` — not a live credential.
  - No wallets/payments secrets.
  - Zero `TESSERA_ENABLE_*` hits in diff.
- pnpm-lock: **OK limited** — new importer `artifacts/gitbook-mcp` (devDeps `@types/node` catalog + `vitest@4.1.11`) plus snapshot variants for the same vitest/vite versions under a `jiti@2.7.0` peer path. No unrelated package version bumps. Frozen install passed in CI.
- API response changes (existing Tessera HTTP): **none** — new standalone MCP/HTTP connector package; does not edit `artifacts/api-server` routes.
- CI: run **37388265798** / job **112026929554** `validate` completed **success** (6:24–6:27 PM CT) on head d9c4f1e (PR event). Log TESTED:
  - install frozen + audit `1 high (1 ignored)`
  - typecheck pass (includes gitbook-mcp)
  - scripts node:test **14/14**
  - `[test] Gitbook MCP` vitest **28 passed** (1 file) — **TESTED** (matches agent claim)
  - API vitest 18 files **116 passed | 1 skipped**
  - build pass (gitbook-mcp + apps)

## PR #7 — PASS (TESTED)
- Head pin: `f57c40aa3863a8f688fb0e61e75bee289c296baa` matches receipt exactly.
- Files (13, +594/−3): new `artifacts/api-server/src/lib/memory/` (README, bm25, distill, improve, index, redact, store, text, types), `__tests__/learning-memory.test.ts` (+131), `artifacts/api-server/package.json` (+`test:memory`), `README.md` (+1 bullet), `scripts/test-unified.mjs` (optional `script` arg on `runWorkspaceTest` + learning-memory suite entry). No lockfile.
- Base contains b1679659: YES.
- Forbidden: **none** — no workflows, no secrets/.env, no wallets/payments, no `TESSERA_ENABLE_*` (PR body + diff). Module is side-effect free on import; not mounted on live request path.
- pnpm-lock: **OK limited** (unchanged; no new packages / no churn).
- API response changes (existing Tessera HTTP): **none** — library + tests only; `contextForQuery` not wired to routes.
- CI: run **37388267246** / job **112026935177** `validate` completed **success** (6:24–6:27 PM CT) on head f57c40a. Log TESTED:
  - install frozen + audit `1 high (1 ignored)`
  - typecheck pass
  - scripts node:test **14/14**
  - API vitest 19 files **120 passed | 1 skipped** (includes `learning-memory.test.ts` **4 tests**)
  - `[test] Tessera learning memory` dedicated `test:memory` **4 passed** — **TESTED** (matches agent claim)
  - build pass

## Stack #6 → #7 on b1679659 — CLEAN
- File overlap: `README.md`, `scripts/test-unified.mjs` only. All other paths disjoint (gitbook-mcp package vs memory lib).
- Hunk analysis (independent of agent claim):
  - **README.md:** #6 inserts gitbook-mcp bullet after the `artifacts/` line; #7 inserts memory bullet after the `docs/` line. Non-overlapping context → both bullets survive a sequential merge.
  - **scripts/test-unified.mjs:** #6 only adds `["Gitbook MCP", "@workspace/gitbook-mcp"]` to the early for-loop. #7 changes `runWorkspaceTest(..., script = "test")` near the top and appends the learning-memory `runWorkspaceTest(..., "test:memory")` after the API block. Non-overlapping hunks → combined tree keeps Gitbook MCP entry + memory entry + optional script arg (3-arg Gitbook call still valid via default).
- No textual conflict expected. After #6 merges, #7 will be behind main tip and may need update-branch before merge; content applies clean.
- Combined tree (#6+#7) has NOT been CI-run as one merge ref.

## Merge advice
Merge draft #6 then #7 on tip b1679659 (stack CLEAN); confirm main CI green after #6 before merging #7, and expect API vitest 120 passed | 1 skipped plus Gitbook MCP 28 after both land.
