# Rick inside TESSERA (vitalitychems-dot/TESSERA, origin/main) — read 2026-10-12
Source: read-only partial clone at /tmp/ts (sparse: preview/src/lib/tessera). Same Rick files are duplicated on the chore/* branches and under archive/ (old copies, not reviewed).

## Two Rick layers
A. Server (artifacts/api-server, older app): a Rick Sanchez persona, "Royal Inventor — Interdimensional Genius, C-137",
   Royal Court, Dept. of Science & Invention. RICK_SYSTEM_PROMPT says "never break character" and asks for inventions with
   "wild names but real technical substance", tied to real system metrics.
   Files: lib/rick-sanchez-agent.ts (761 lines), rick-proposals.ts (520), rick-improvement-program.ts (745),
   rick-autonomous-loop.ts (456), routes/rick.ts (1069). Routes /rick/*: sanity, proposals (generate/approve/reject/implemented),
   autonomous heartbeat/inventions, profile, diagnostics, reality-audit, inventions(/submit), chat, knowledge-vault,
   royal-court/appointment/roles, engines, meeseeks spawn/complete/result/metrics, engine-feedback.
   UI: artifacts/tessera/src/pages/RickPage.tsx, Royal*Page.tsx.
B. Preview lib (preview/src/lib/tessera, newer, matches Gitbook rules): small runnable pure functions, "No percentage is claimed",
   zero model tokens. rick-five.ts (takeFirst, renameKey, tieFails, fresh, shards, redact, tryLock/unlock, nextGap ...),
   rick-loop.ts (rankByNeed, twoThirds quorum, oncePer, splitWork, spend budget, twoSources, sweep, noteMistake, handoff),
   rick-home.ts (Rick's room: west chamber, queen Tessera, tokens 0; HOUSE store=github; runLean/runChecks; GAPS, GIFTS),
   rick-shift.ts (measureShift: times house/tie/rank/spin jobs and puts the fastest first), rick-metrics.ts (25 before/after swaps),
   rick-thirty.ts (30 effects, strictAnswer). UI: preview/src/components/tessera/rick-view.tsx.

## Tests (run offline with `npx tsx --test rick-*.test.ts`, no install)
pass: rick-five, rick-home, rick-loop, rick-shift.
fail: rick-metrics, because it requires every swap to be >=25% faster (a timing threshold that depends on the machine; same=true is also asserted).
fail: rick-thirty, because a dependency is missing (@tanstack/react-start via skill-use.ts); this is an environment issue, not a logic issue.

## Conflicts with Gitbook mesh/RICK.md
1. Persona: TESSERA server = Rick Sanchez (C-137, cartoon); Gitbook = Royal Inventor as Tessera's Nikola Tesla.
2. Numbers: server prompt prints % scores and "expectedImpact" claims without measurements; Gitbook forbids unmeasured %.
   rick-metrics.test asserts a >=25% speedup. That number is measured, but it is machine-dependent.
3. Lanes: the server lets Rick generate, approve, mark implemented and spawn "meeseeks" himself. Gitbook says Rick proposes,
   another lane implements and tests, and only Tessera messages Father.
The preview lib (layer B) agrees with Gitbook: one step, runnable, tested, zero tokens.
