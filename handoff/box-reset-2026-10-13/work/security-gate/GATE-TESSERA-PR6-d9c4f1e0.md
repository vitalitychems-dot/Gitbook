# Security gate — TESSERA PR #6 — FAIL

- Repo: vitalitychems-dot/TESSERA · PR #6 "Add Gitbook MCP connector for mesh agents"
- Expected head: d9c4f1e04c87595998f54bcc2a44afd6c8a1b587
- Live head (get_pull_request): **d9c4f1e04c87595998f54bcc2a44afd6c8a1b587 — MATCH**
- Base: main @ b16796591c3f92d76290d827ac41c8ffcc975182 · state open · draft true · merged false · 21 files, +2209/−0
- Gate run: 2026-10-05 18:39 CT · read-only (no merge/push/comment; LEDGER.md untouched). Fresh rerun replacing interrupted run.
- RECEIPT: TESSERA PR #6 d9c4f1e0, #7 f57c40aa
- Evidence dir: /workspace/security-gate/work-tessera-pr6-7/ (pr6.diff, service.ts, service.test.ts, lane-bypass-sim.mjs/.out)

## Verdict: **FAIL** — checklist #4 broken (lane guard bypassable); #3 not enforced

## Hard forbids
| Check | Result | Evidence |
|---|---|---|
| TESSERA_ENABLE_* flips | none | grep pr6.diff: 0 hits |
| Committed secret values | none real | .env.example adds blank GITBOOK_* keys only; test token `[REDACTED]` is a dummy (FLAG-3) |
| Wallet/payment creds | none | grep wallet/stripe/payment: 0 |
| [REDACTED-PATH] | not touched; code *refuses* 1T paths | src/paths.ts assertRepoPath |
| Deleting data/tests | none — 0 deleted lines | pr6.diff |
| Manus authorship | none | 3fd198c7 + d9c4f1e0: author/committer Cursor Agent, Co-authored-by Tessera, signatures verified |
| Workflows edited | none | no .github/ paths |

## PR #6 checklist
1. **Token env-only — PASS.** `src/config.ts` loadConfig: `token: [REDACTED]`; `src/github.ts` throws if empty; only used in Authorization header; error text passed through `redactSecret(…, token)`. Only log line is `gitbook http listening on http://host:port` (src/http.ts). No hardcoded token. FLAG-2: `GITBOOK_GITHUB_API` env can redirect the bearer token to any host.
2. **Branch + draft PR only, never main — PASS.** `src/service.ts`: createBranch refuses `main`/default; commitFile refuses default branch; branchName always `gitbook-mcp/<kind>-<stamp>-<slug>` (src/paths.ts); openDraftPull posts `draft:true`, closes and throws if GitHub returns non-draft; no merge endpoint anywhere. Test: service.test.ts ~L305-322.
3. **HTTP binds 127.0.0.1 only — FAIL (not enforced).** Default host is 127.0.0.1 (`config.ts` httpHost), but `GITBOOK_HTTP_HOST` is accepted verbatim and passed to `server.listen(port, host)` (`src/http.ts`) with no loopback check. Setting it to 0.0.0.0 exposes an **unauthenticated** HTTP API that can post board comments and open draft PRs with the token. README only says "Keep this on loopback." Fix: reject non-loopback hosts (127.0.0.1/::1/localhost) in loadConfig, or add auth.
4. **Security & Build lanes cannot open PRs — FAIL (bypass).** `src/service.ts` assertFileWrite: `const laneId = explicitLane?.trim() || options.agentLane` — the caller-supplied `lane` tool argument (exposed in write_handoff / propose_page_change schemas over MCP and HTTP) **overrides** the process env lane. `findLane` (src/routing.ts) is exact-match and returns undefined → allow. Simulation of the exact logic (work-tessera-pr6-7/lane-bypass-sim.out):
   - env=security, lane arg none → BLOCKED (only case the test covers, service.test.ts ~L397)
   - env=security, lane arg "tessera" → **ALLOWED**
   - env=security, lane arg "Security" → **ALLOWED**
   - env=build, lane arg "nonexistent" → **ALLOWED**
   - env="Security" (case) → **ALLOWED**
   - no env, no arg → ALLOWED (fail-open default)
   Fix: env lane must be authoritative (ignore/deny explicit lane that differs), case-normalize, and fail closed on unknown lane; add tests for override cases.
5. **AGENT: prefix on board comments — PASS (with FLAG-1).** postBoardUpdate builds `AGENT: ${name}\n\n${note}`; assertAgentName rejects newlines/empty/>80 chars; handoff block also writes `AGENT: name`. Test asserts body "AGENT: Build\n\nTypecheck passed." FLAG-1: name is caller-asserted (not bound to the process lane), so any caller can label itself any agent; body text may contain further "AGENT:" lines.
6. **No secrets in tests — PASS.** service.test.ts uses mocked fetch and dummy `[REDACTED]` (not a real-format 36-char token) on `https://github.test`; no network.

## FLAGs
- FLAG-1: AGENT name self-asserted (impersonation guard is prefix-only).
- FLAG-2: GITBOOK_GITHUB_API overridable → token could be sent to non-GitHub host.
- FLAG-3: dummy ghp_-shaped token literal in tests may trip secret scanners.
- FLAG-4: post_board_update has no lane check (Security/Build can comment — likely intended; comments ≠ PRs).
- FLAG-5: lockfile adds second vite/vitest variant resolved with jiti 2.7.0 (dev-only).

## Required to flip to PASS
Fix #3 (enforce loopback) and #4 (env lane authoritative, case-insensitive, fail-closed; tests for override), push new head, re-gate on new SHA.

Nothing merged, pushed, or commented by this gate. PR remains open draft, merged=false.
