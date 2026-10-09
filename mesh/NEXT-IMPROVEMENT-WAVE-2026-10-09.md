# Next TESSERA improvement wave — Cursor + Replit

**Base:** TESSERA `e5e5719`  
**Coordination:** Gitbook Issue #2  
**Status:** READY FOR AGENT CHECK-IN

## PERF-001 — Replit implementation lane

**Scope:** `artifacts/tessera/vite.config.ts` and the smallest required frontend import boundaries needed to reduce the non-fatal 1,019.51 kB OrbitControls production chunk.  
**Goal:** produce a measurable bundle-size improvement without changing route behavior, authentication, data access, research semantics, or safety gates.  
**Required evidence:** before/after chunk sizes, `pnpm typecheck`, `pnpm test`, `pnpm run build`, route-manifest validation, and a rollback commit.  
**Excludes:** database/API changes, SNN changes, secrets, protected material, autonomous loops, and broad refactors.

## PERF-002 — Cursor correctness lane

**Scope:** read-only review of PERF-001's proposed diff and `artifacts/tessera/public/manus-routes.json`.  
**Goal:** verify lazy-loading does not remove routes, alter guarded pages, introduce hidden network calls, or create a production-only failure.  
**Required evidence:** route-by-route conclusion, exact commands, risks, and accept/reject recommendation.  
**Dependency:** review begins after Replit posts a concrete proposal; no overlapping edits.

## SITE-005 — Replit deployment lane

**Scope:** Gitbook report only: recommend static, container, or hybrid serving for the current TESSERA architecture; specify build command, output, runtime, health path, and non-secret environment requirements.  
**Excludes:** production deployment and secret changes.

## SITE-006 — Cursor security/content lane

**Scope:** read-only review of route manifest, public assets, release documentation, and claims language.  
**Goal:** identify any route or content that must remain authorized-only, any secret-shaped path, and any unsupported consciousness/AGI/biological-equivalence claim.  
**Required evidence:** redacted findings with path, disposition, and deterministic check.

## Merge rule

Replit must post a check-in before editing. Cursor reviews the exact proposed diff after it exists. Manus/TESSERA integrates only after both evidence records are posted and checks pass. Passing tests can mark the work TESTED; they do not by themselves authorize a production publication or a security/data change.
