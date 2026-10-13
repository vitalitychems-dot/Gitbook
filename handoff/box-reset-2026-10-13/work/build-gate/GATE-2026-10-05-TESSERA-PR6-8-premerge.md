# GATE 2026-10-05 — TESSERA PR #6 / #8 pre-merge (Build, verify-only)

Lane: Build (verify-only). No push, merge, comment, clone, branch edit, DATABASE_URL, server, flag flips, LEDGER.md, or messages.
Source: cursor-github MCP (read-only). No local checkout/run.
Checked: 2026-10-05 ~6:48 PM CT.

## Tips / overlap first (TESTED)
- main tip = `004b692e4f84a49a4a0fa863f2868a64b7566a3c` (unchanged; #7-only post-merge; matches claimed tip).
- Open PRs on TESSERA: exactly #6 and #8 (both draft, base main @ 004b692e).

| PR | head (API) | matches receipt | base | draft | mergeable | mergeable_state |
|----|-----------|-----------------|------|-------|-----------|-----------------|
| #6 Gitbook MCP `cursor/gitbook-mcp-connector-301f` | e898111ae9fe730ad214ec63f9173d338a9df53e | YES | main 004b692e | true | true | unstable→CI now green |
| #8 memory redaction `cursor/memory-redaction-patterns-301f` | 25183afb894194cb28c17ef3898b70b81d2115cb | YES | main 004b692e | true | true | unstable→CI now green |

#6 contains main 004b692e: **YES** — merge commit `6b65e0e30feae958435732b6d90573f44f068f1d` parents are `d9c4f1e0` (prior #6 head) + `004b692e` (main tip); security fix commit `e898111` sits on that merge.

## PR #6 — PASS (TESTED)
- Head pin: `e898111ae9fe730ad214ec63f9173d338a9df53e` matches receipt exactly.
- Files (21, +2284/−0): new package `artifacts/gitbook-mcp/` (17 added: README, agents.json, package.json, src/*, vitest/tsconfig), plus `.env.example` (+10 blank `GITBOOK_*` names/comments), `README.md` (+1 bullet), `pnpm-lock.yaml` (+70), `scripts/test-unified.mjs` (+1 Gitbook MCP suite entry).
- Forbidden: **none**
  - No `.github/workflows` edits.
  - `.env.example` blank names only (`GITBOOK_GITHUB_TOKEN=` etc.); no values.
  - No wallets/payments secrets.
  - Zero `TESSERA_ENABLE_*` hits in diff.
- pnpm-lock: **OK limited** — new importer `artifacts/gitbook-mcp` (devDeps catalog + `vitest@4.1.11`) plus snapshot variants under `jiti@2.7.0` peer path. No unrelated package version bumps. Frozen install passed in CI.
- API response changes (existing Tessera HTTP): **none** — new standalone MCP/HTTP connector package; does not edit `artifacts/api-server` routes.
- Security-fix notes (Build, not Security; verify CI + hard-limit only): prior FAIL themes at `d9c4f1e0` addressed in code/tests visible in this head:
  - **HTTP bind enforcement:** `assertLoopbackHttpHost` in `config.ts`; only `127.0.0.1` / `::1` / `localhost`; `GITBOOK_HTTP_HOST=0.0.0.0` refuses to start; test `"refuses to start when GITBOOK_HTTP_HOST is not loopback"`.
  - **Lane bypass fix:** `assertFileWrite` uses env `GITBOOK_AGENT_LANE` only; empty/unknown → read-only; per-call `lane` cannot override/escalate; case-insensitive `findLane`; tests for security→tessera / build→nonexistent / unset→read-only.
- CI: run **37390126478** / job **112032964467** `validate` completed **success** (6:43–6:46 PM CT) on head e898111 (PR event). Log TESTED:
  - install frozen + audit `1 vulnerabilities found` (1 high ignored)
  - typecheck pass
  - scripts node:test **14/14**
  - `[test] Gitbook MCP` vitest **30 passed** (1 file) — **TESTED** (matches agent claim 30)
  - API vitest 19 files **120 passed | 1 skipped** (includes learning-memory 4 from main)
  - dedicated `test:memory` **4 passed**
  - build pass

## PR #8 — PASS (TESTED)
- Head pin: `25183afb894194cb28c17ef3898b70b81d2115cb` matches receipt exactly.
- Files (3, +27/−2): `artifacts/api-server/src/lib/memory/redact.ts` (+4/−1 patterns), `__tests__/learning-memory.test.ts` (+22 new redaction test), `lib/memory/README.md` (+1/−1 docs). No lockfile.
- Forbidden: **none** — no workflows, no secrets/.env, no wallets/payments, no `TESSERA_ENABLE_*`. Fake secrets in tests are built from joined pieces (no contiguous fake token in source).
- pnpm-lock: **OK limited** (unchanged; no new packages / no churn).
- API response changes (existing Tessera HTTP): **none** — redaction library + tests only; still not mounted on live request path.
- CI: run **37390140635** / job **112033005887** `validate` completed **success** (6:43–6:46 PM CT) on head 25183af. Log TESTED:
  - install frozen + audit `1 vulnerabilities found` (1 high ignored)
  - typecheck pass
  - scripts node:test **14/14**
  - API vitest 19 files **121 passed | 1 skipped** (learning-memory.test.ts **5 tests**)
  - `[test] Tessera learning memory` dedicated `test:memory` **5 passed** — **TESTED** (matches agent claim 5)
  - build pass

## Stack #6 → #8 on 004b692e — CLEAN
- File overlap: **none**. #6 touches gitbook-mcp package + `.env.example` + root README + lockfile + `scripts/test-unified.mjs`. #8 touches only `memory/redact.ts`, `learning-memory.test.ts`, `memory/README.md`.
- No textual conflict expected. After #6 merges, #8 will be behind main tip and may need update-branch before merge; content applies clean (disjoint paths).
- Combined tree (#6+#8) has NOT been CI-run as one merge ref.

## Merge advice
Merge draft #6 then #8 on tip 004b692e (stack CLEAN). Confirm main CI green after #6 before merging #8. Expect after both: Gitbook MCP 30 + learning-memory 5 + API vitest ~121p/1s. Security already failed prior #6 head; this head carries bind + lane fixes — Security should re-review #6 before merge (Build: CI green, no hard-limit violations).
