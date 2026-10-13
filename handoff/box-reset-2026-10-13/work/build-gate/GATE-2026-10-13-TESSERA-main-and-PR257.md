# Build gate — TESSERA main 234e3dcf + PR #257 8de873c6 (2026-10-13 ~02:05–02:20 CT)
Verify-only. DATABASE_URL unset, no servers, no TESSERA_ENABLE_* set, no push/merge/comment. Node v22.20.0, pnpm 11.25.0.
Clone: /workspace/build-gate/full-f76d (blob:none, sparse excl. 1T/vault/archives) fetched after forced update 32af55c...234e3dc.

## main tip: 234e3dcf43d1e184d0d9e2bf544801639d5896ad (#258); #256 e6a0aa2 present — verdict PASS (with env caveat)
1. Emails (TESTED, `git log origin/main --format=%ae%n%ce`): 1161 332565808+vitalitychems-dot@users.noreply.github.com, 21 206951365+cursor[bot]@users.noreply.github.com, 3 manus@users.noreply.github.com, 5 noreply@github.com.
   Exception to literal "users.noreply.github.com" rule: committer `noreply@github.com` (GitHub web-flow, squash merges) on 234e3dc, e6a0aa2, e0e5f64, 6abb561, d144dfd. No personal emails.
2. gitleaks 8.21.2, config /workspace/pubscan/gl.toml, `--log-opts=main` on bare clone /workspace/build-gate/tess-gl.git (filter blob:limit=1m — blobs >1 MB not scanned): 319 commits scanned, "no leaks found", 0 findings, exit 0.
3. Tests at 234e3dc (TESTED): scripts 15/15; v2 116/116 (three 0.169.0 installed); GitAI 27/27; api-server vitest: 420/420 tests pass, 47/51 files pass, 4 files fail to load: evolution-sandbox-loop, invention-glb-upload, safe-fetch-policy, tessera-codex — all "DATABASE_URL must be set" thrown at import in lib/db (env-limited; not run, DATABASE_URL forbidden). Full api-server vitest is therefore NOT fully green here.

## PR #257 head 8de873c6f667dfb67131e7682446f93cade30445 (sec/gate-shadow-routes) — verdict PASS (with same env caveat)
- Base e0e5f64; 1 ahead / 2 behind main; `git merge-tree` clean (tree 2990a86); lockfile unchanged. Author/committer noreply.
- Tests at head (TESTED): scripts 15/15, v2 112/112, GitAI 22/22, api-server 442/442 tests, 48/52 files (same 4 DB-import files).
- Merged tree (main+PR, local uncommitted merge, aborted after): api-server 442/442 tests, 48/52 files (same 4).
- Targeted: route-inventory.test.ts + shadow-route-admin-gate.test.ts 36/36.
- Refusal assertions: shadow-route-admin-gate.test.ts is STATIC (greps route files for requireAdminSession on 20 owner-only paths, hallucination-check stays public, sovereign-admin still has 401/fail-closed) — it does not issue requests. Runtime refusal IS asserted in route-inventory.test.ts: 10 `anonymous.status).toBe(401)` checks (main has 3), plus 200 with owner session.
- Diff: 9 files, +137/−48 (route files add requireAdminSession; 3 tessera UI pages; 2 tests).

#255 not gated (on hold for Father).
- Note: main has 595 commits (342 non-merge); gitleaks reported 319 scanned — remaining likely merge-only/large-blob-only commits; not proven.
