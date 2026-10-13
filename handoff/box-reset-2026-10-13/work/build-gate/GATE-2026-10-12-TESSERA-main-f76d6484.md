# Build gate — vitalitychems-dot/TESSERA main @ f76d648462f85dceaa447c532e0b885869ec7822
Date: 2026-10-12 ~19:00 CT. Verifier: Build (verify-only). CI billing-blocked; local run is the proof.
## Verdict: PASS

## Checkout (TESTED)
- Fresh blob-filtered clone from GitHub at /workspace/build-gate/full-f76d, detached HEAD = f76d6484 ("Turn the 3D studio floor on by default", merge f6c9362+0357acf).
- Sparse excludes only **/1T/**, **/*vault*/**, archives/source-repositories/. archive/from-gitbook IS checked out.
- Note: worktree off /workspace/rea-batch/b2-TESSERA gave 45/48 — that clone's sparse config excludes archive/from-gitbook (2 ENOENT fails) and /opt/cursor/artifacts was not writable (1 EACCES). Both environment, not code.
- Toolchain: box node 20.19.2 cannot run pnpm 11; used node v22.20.0 + pnpm 11.25.0 (packageManager pin) under /workspace/build-gate.
- `pnpm install --frozen-lockfile --ignore-scripts`: OK, lockfile passes supply-chain policy.
- Created /opt/cursor/artifacts (chmod 777, sudo) so v2-063 test could write its screenshot.

## Tests (TESTED) — `pnpm --filter @workspace/v2 test`, DATABASE_URL unset, no TESSERA_ENABLE_* in env
tests 48 | pass 48 | fail 0 | cancelled 0 | skipped 0 | exit 0. Raw log: GATE-f76d-test-raw.log

## V2-001 denylist (TESTED)
- src/hyb011-denylist.mjs: segment + query refusal of 1t/vault/wallet(s)/payment(s)/checkout/stripe/... -> 403 hyb-011-denied.
- test/v2-001-denylist.test.mjs, 4 tests all pass: wallet/payment/vault/1T fixtures refused (10 URLs incl. query forms); ordinary routes open; file admission refuses; loopback server returns 403 on /wallet, 200 on /studio/tasks.
- Extra probe: /%77allet, /WALLET/x, /api/Payments, /a/../vault, /x?v=%2Fvault -> 403; /studio/tasks -> 200.
- FYI (REPORTED, not a fail): the gate is imported only by offline/file-mesh.mjs and its test; studio serve.mjs/wall.mjs do not route through it.

## TESSERA_ENABLE_* defaults (TESTED by grep; archive/research/node_modules excluded)
- Only two names appear: TESSERA_ENABLE_COLONIAL_FALLBACK (api-server test sets "1" temporarily and restores) and TESSERA_ENABLE_STUDIO_3D (v2-015 test sets "0" and restores). No source/config default sets either on.
- .env.example: no TESSERA_ENABLE_* entries (TESSERA_PEN_ENABLED=0).
- FYI: this commit turns the 3D studio on via hard-coded constant STUDIO_3D_ENABLED=true in studio/floor.mjs (was false at f6c9362). It is not a TESSERA_ENABLE_* flag (2D via ?view=2d), so no flag defaults on — but it is a default-on behavior change.

## Not done
No DB, no servers against a real DB, no flag flips, no push/comment/message. Not checked: api-server suite; SHAs change after planned history rewrite — re-gate then.
