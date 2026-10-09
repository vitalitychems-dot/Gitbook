# Permanent-site readiness sync — 2026-10-09

**TESSERA source commit:** `e5e571966b5c37a9c59d5485345b1f46cca20dac`  
**Gitbook base:** `fd7a3586e891aeffe942e720bce7b258b26c4705`  
**Status:** TESTED / publication preparation continues

## Improvements published to TESSERA

1. Vite development-only Replit plugins are now restricted to `vite serve`; production builds no longer load the runtime-error overlay, cartographer, or dev banner.
2. Removed the unnecessary Next.js-only `"use client"` directive from the Vite tooltip component.
3. Added the managed Webdev route manifest at `artifacts/tessera/public/manus-routes.json` with 51 application routes.
4. Added the source-side release record at `docs/PERMANENT-SITE-RELEASE.md`.

## Verification

- `pnpm typecheck`: passed.
- `pnpm test`: passed; database integration tests remain intentionally skipped without a dedicated local test database.
- `pnpm run build`: passed with no sourcemap, TypeScript, lifecycle, or build-failure diagnostics.
- Built route manifest: present and valid with 51 routes.
- One non-fatal performance advisory remains: the OrbitControls bundle is approximately 1,019.51 kB after minification. This is a follow-up optimization, not a failed build.

## Collaboration status

No new SITE-001–SITE-004 agent check-in has been posted on issue #2 yet. Existing open TESSERA pull requests remain separate review items and were not merged or rewritten by this sync. Agents must post their exact scope, base SHA, evidence, risk, and rollback before promotion.

## Still required before permanent publication

- Managed Webdev model choice and implementation of the authorized-access site.
- Production health-path and deployment evidence.
- SITE-004 security/privacy review, including secret-shaped paths and protected-material exclusion.
- GitHub checkpoint and exact release payload.
- Owner bulk approval for the final permanent-site publication.
