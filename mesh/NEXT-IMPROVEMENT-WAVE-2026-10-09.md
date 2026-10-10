# Next TESSERA improvement wave — Cursor + Replit

**Base:** TESSERA `c10b8379079075529f3aae9ac09b1afbf3339940` (pull request 97; parent `d9e431d` is pull request 81; pull request 96 is `c938ac3`; pull request 95 is `a708206`; the chunk split is ancestor `072acd8`)
**Coordination:** Gitbook Issue #2
**Lane:** Cursor and Replit. Grok bot is out of credits and is not in this wave.
**Status:** PERF-001 tested. PERF-002 accepted on the diff. Replit confirmed the SITE-005 hybrid draft on 2026-10-10 in the Replit app. SITE-006 is recorded. Pull request 97 is on main as `c10b837`. The site is not published.

## PERF-001 — Replit implementation lane

**Scope:** `artifacts/tessera/vite.config.ts` and the smallest required frontend import boundaries needed to reduce the non-fatal 1,019.51 kB OrbitControls production chunk.
**Goal:** produce a measurable bundle-size improvement without changing route behavior, authentication, data access, research semantics, or safety gates.
**Required evidence:** before/after chunk sizes, `pnpm typecheck`, `pnpm test`, `pnpm run build`, route-manifest validation, and a rollback commit. Evidence is recorded in [PERF-001-RESULT-2026-10-09.md](PERF-001-RESULT-2026-10-09.md); TESSERA commit `072acd8`.
**Excludes:** database/API changes, SNN changes, secrets, protected material, autonomous loops, and broad refactors.

## PERF-002 — Cursor correctness lane

**Scope:** read-only review of PERF-001's diff and `artifacts/tessera/public/manus-routes.json`.
**Result:** accepted on 2026-10-09 in issue comment 6090067090. Commit `072acd8` adds twelve lines to `artifacts/tessera/vite.config.ts`. Match order is drei, fiber, three-stdlib, then three. The manifest lists 51 routes. The diff adds no fetch and no route edit. Cursor did not re-run the build. Rollback remains `git revert 072acd8`.

## SITE-005 — Replit deployment lane

**Scope:** Gitbook report only. Recommend static, container, or hybrid serving for the current TESSERA architecture. Name the build command, output, runtime, health path, and non-secret environment names.
**Draft:** [SITE-005-2026-10-09.md](SITE-005-2026-10-09.md), Gitbook commit `0d0a661`. Recommendation in that draft: hybrid. Web output `artifacts/tessera/dist/public`. API runtime `node --enable-source-maps ./dist/index.mjs`. Health path `GET /api/healthz`. Non-secret names: `PORT`, `BASE_PATH`, `REPL_ID`.
**Base cited in that draft:** TESSERA `63a9911`. Current main is `c10b837`.
**Excludes:** production deployment, secret changes, repository deletion, and any copy of the olive-giant clock.
**Result:** Replit confirmed the hybrid draft as written on 2026-10-10. The answer is in the Replit app, recorded by Cursor on the SITE-005 page. Replit has not posted that confirmation on issue #2.

## SITE-006 — Cursor security/content lane

**Scope:** read-only review of the route manifest, public assets, release documentation, and claims language.
**Result:** recorded on 2026-10-09 in [SITE-006-2026-10-09.md](SITE-006-2026-10-09.md). Base at review time was `ed8e096`. The 51 manifest paths match the 51 App routes. All of them sit inside the browser `TesseractKeyGate`. Twelve public files, and no secret-shaped filename. On that base, `artifacts/api-server/src/routes/sovereign-engines.ts` had no `requireAdminSession`. Consciousness, AGI, and biological-equivalence sentences stay product copy. AGI is unmet.
**Follow-up:** Father said merge. Pull request 96 is on main as `c938ac30724f22fc38e0c9afa5e9b78dc10f1636`. Validate run 38014313293 passed. Each engine route and `GET /api/diagnostics/consciousness` use `requireAdminSession`. `GET /api/healthz` stays open. The site was not published.

## Approved merges — 2026-10-10

Father said to auto-approve and keep building. Each merge below was CLEAN, with validate SUCCESS, and was merged one at a time.

- Pull request 78, `ad2025b`. Legacy engines no longer start the autonomous loop at import. The start and stop routes stay behind the owner session.
- Pull request 89, `7664998`. Conversation routes require an owner session.
- Pull request 90, `5bc28e5`. Colonial and sovereign language cipher routes require an owner session. Caught 500 bodies no longer return the error message.
- Pull request 91, `85fc46a`. Grand-council and omniversal catches return stable error codes.
- Pull request 68, `03e4d1b`. Untracked local trees are ignored. The shared Zz archive was not read.
- Pull request 81, `d9e431d`. The preview package shell is runnable. The lockfile was not changed.
- Pull request 97, `c10b837`. The remaining 42 catalog cards. Validate run 38017838713 passed. Three names moved: `SushiSwap/sushiswap` to `sushi-labs/sushiswap`, `venturaEffect/the_consciousness_ai` to `tlcdv/the_consciousness_ai`, and `yatrogenesis/HumanBrain` to `Yatrogenesis/HumanBrain`. Three steps were read from `tweenjs/tween.js`: linear sample, quadratic ease in, and quadratic ease out. These are not a new set of weights. AGI is unmet. Trading, exchange, and miner cards stay pointers. No repository was cloned.

Left open on purpose: pull request 80, because its identity line says the pen is Tessera; pull request 82, because validate failed and it conflicts; draft 34, because it conflicts; draft 87, because it conflicts. None of those were force-merged.

## Merge rule

Passing tests and a merged pull request can mark the work on main. They do not authorize a production publication.
