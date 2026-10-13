# Security gate — TESSERA PR #6 — PASS (re-gate)

- Repo: vitalitychems-dot/TESSERA · PR #6 "Add Gitbook MCP connector for mesh agents"
- Expected head: e898111ae9fe730ad214ec63f9173d338a9df53e
- Live head (get_pull_request): **e898111ae9fe730ad214ec63f9173d338a9df53e — MATCH**
- Base: main @ 004b692e4f84a49a4a0fa863f2868a64b7566a3c · state open · draft true · merged false · 21 files, +2284/−0
- Gate run: 2026-10-05 18:46 CT · read-only (no merge/push/comment; LEDGER.md untouched)
- RECEIPT: TESSERA PR #6 e898111a, #8 25183afb
- Prior FAIL: GATE-TESSERA-PR6-d9c4f1e0.md @ d9c4f1e04c87595998f54bcc2a44afd6c8a1b587
- Evidence dir: /workspace/security-gate/work-tessera-pr6-e898/ (lane-authority-sim.mjs/.out)

## Verdict: **PASS** — prior blockers (A) loopback and (B) lane override are fixed

## Hard forbids
| Check | Result | Evidence |
|---|---|---|
| TESSERA_ENABLE_* flips | none | patch keyword scan: 0 ENABLE hits across 21 files |
| Committed secret values | none real | .env.example blank GITBOOK_* keys; test token `[REDACTED]` dummy on github.test (FLAG-3) |
| Wallet/payment creds | none | 0 wallet/stripe/payment hits |
| [REDACTED-PATH] | not touched; code refuses 1T paths | paths.ts assertRepoPath; test rejects vault/1T/secret.md |
| Deleting data/tests | none — 0 deleted lines | list_pull_request_files |
| Manus authorship | none | e898111a + 6b65e0e3 (+ earlier branch commits): Cursor Agent, Co-authored-by Tessera, signatures verified |
| Workflows edited | none | no .github/ paths |

## PR #6 checklist
1. **Token only from GITBOOK_GITHUB_TOKEN — PASS.** `config.ts` loadConfig: `token: [REDACTED]`; `requireToken` / `github.ts` createGitHubClient throw if empty; Authorization Bearer only; errors via `redactSecret(…, token)`. FLAG-2 retained: `GITBOOK_GITHUB_API` can redirect the bearer.
2. **Writes via branch+draft PR only, never main — PASS.** createBranch/commitFile/openDraftPull refuse default/`main`; branchName always `gitbook-mcp/<kind>-…`; openDraftPull posts `draft:true` and closes+throws if non-draft; no merge endpoint.
3. **NEW: host loopback-only; 0.0.0.0 / non-loopback refuse to start — PASS (prior FAIL fixed).** `assertLoopbackHttpHost` in `config.ts`: only `127.0.0.1` / `::1` / `localhost` (case-insensitive trim). Called from `loadConfig` before return — not merely a default. `startHttpServer` → `loadConfig()` so `GITBOOK_HTTP_HOST=0.0.0.0` throws "Refusing to start". Test: service.test.ts "refuses to start when GITBOOK_HTTP_HOST is not loopback". Sim: 0.0.0.0 / 1.2.3.4 / * → REFUSE; loopback → OK.
4. **NEW: GITBOOK_AGENT_LANE authoritative — PASS (prior FAIL fixed).** `assertFileWrite` in `service.ts`:
   - empty env → throw read-only (no PR)
   - unknown env lane → denied
   - `findLane` case-insensitive (`routing.ts` toLowerCase)
   - explicit/call lane must match env lane id or throw "cannot override"; cannot escalate
   - then `fileWrites===false` still blocks security/build
   Tests cover prior bypasses: env security + arg tessera → cannot override; env security + arg Security → read-only; env build + nonexistent → cannot override; unset env + arg tessera → read-only.
   Re-sim (`lane-authority-sim.out`): all three prior ALLOWED cases now **BLOCKED**.
5. **AGENT: prefix on board comments — PASS (FLAG-1).** postBoardUpdate builds `AGENT: ${name}\n\n${note}`; assertAgentName rejects newlines/empty/>80.
6. **No secrets in tests — PASS.** mocked fetch; dummy ghp_ on github.test; no live network.

## Prior FAIL blockers status
| Blocker | @ d9c4f1e0 | @ e898111a |
|---|---|---|
| (A) GITBOOK_HTTP_HOST not loopback-enforced | FAIL | **FIXED** — refuse non-loopback at loadConfig |
| (B) lane arg override bypassed security/build PR block | FAIL | **FIXED** — env lane authoritative; case-insensitive; unknown/empty denied |

## FLAGs
- FLAG-1: AGENT name self-asserted (impersonation guard is prefix-only).
- FLAG-2: GITBOOK_GITHUB_API overridable → token could be sent to non-GitHub host.
- FLAG-3: dummy ghp_-shaped token literal in tests may trip secret scanners.
- FLAG-4: post_board_update has no lane check (Security/Build can comment — intended; comments ≠ PRs).
- FLAG-5: lockfile adds second vite/vitest variant resolved with jiti 2.7.0 (dev-only).
- FLAG-6: HTTP API remains unauthenticated on loopback (acceptable given bind refuse for non-loopback).

## Verdict: **PASS** @ e898111ae9fe730ad214ec63f9173d338a9df53e

Nothing merged, pushed, or commented by this gate. PR remains open draft, merged=false.
