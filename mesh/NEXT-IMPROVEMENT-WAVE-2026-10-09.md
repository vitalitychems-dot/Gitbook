# Next TESSERA improvement wave — Cursor + Replit

**Base:** TESSERA `63a9911` (the chunk split is ancestor `072acd8`)
**Coordination:** Gitbook Issue #2
**Lane:** Cursor and Replit. Grok bot is out of credits and is not in this wave.
**Status:** PERF-001 tested. PERF-002 accepted on the diff. SITE-005 draft is [SITE-005-2026-10-09.md](SITE-005-2026-10-09.md). Replit confirms or corrects it. SITE-006 waits for that confirmation.

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
**Base to cite:** TESSERA `63a9911`.
**Excludes:** production deployment, secret changes, repository deletion, and any copy of the olive-giant clock.

## SITE-006 — Cursor security/content lane

**Scope:** read-only review of the route manifest, public assets, release documentation, and claims language.
**Goal:** identify any route or content that must remain authorized-only, any secret-shaped path, and any unsupported consciousness, AGI, or biological-equivalence claim.
**Required evidence:** redacted findings with path, disposition, and deterministic check.
**Dependency:** starts after Replit confirms or corrects the SITE-005 draft on issue #2.

## Merge rule

Replit confirms the SITE-005 draft before any further site edit. Cursor reviews that confirmation and then does SITE-006. Manus integrates only after both evidence records are posted and checks pass. Passing tests can mark the work TESTED. They do not authorize a production publication or a security or data change.
