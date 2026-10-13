# Engineering rules (as decided)

Status: DRAFT (HYB-015, staged locally). This page summarizes decisions. The binding wording stays on the backlog.

- Compare behavior and tests, not manifests or file counts. Prefer the newest reviewed TESSERA code. (HYB-006/007 "Rule applied".)
- UI stack stays Vite + wouter. The gate stays the HttpOnly admin session (`artifacts/api-server/src/routes/admin-session.ts`). TanStack Start, better-auth, PGlite, and Kysely stay out. (HYB-007 Z1, Z4, Z5.)
- Outbound fetch only through the allowlisted guard `artifacts/api-server/src/lib/safe-fetch.ts` and its test `safe-fetch-policy.test.ts`. No second fetcher. (HYB-006 C2/C3; HYB-007 Z12, Z13.)
- Port ideas, not apps. Any RETAINED idea needs one named TESSERA target, one test, and a rollback before it moves. (HYB-007 Z9/Z10/Z14.)
- No re-import of old lockfiles, generated output, Nitro/Vercel builds, or migration-running builds. (HYB-006; HYB-007 Z8; HYB-008.)
- Suite DB policy: loopback Postgres only. CI plus a blank `.env.example` stays. (HYB-006 C11, C16.)
- Historical merge gate: HYB-014 (DONE, TESSERA PR #63).

## Provenance

- `merge/hyb-006-grok-ready.md` @ Gitbook `cd8faa0` (sources Grok-ready `9e3fbca`, TESSERA `fec56eb`)
- `merge/hyb-007-z-app.md` @ Gitbook `cd8faa0` (sources Zz `150d4ec`, TESSERA `fec56eb`)
- `merge/hyb-008-olive.md`, `merge/hyb-017-storefront.md` @ Gitbook `cd8faa0`
- `intake/HYBRID-CONSOLIDATION-BACKLOG.md` @ Gitbook `cd8faa0`
