# GATE 2026-10-13 — TESSERA #65 / #298 / #269, Gitbook #70 (Build)
Main baseline TESTED at 47983dda (Node 22.20, pnpm 11.25, no DATABASE_URL): scripts 23/23, v2 137/140 (3 env EACCES), GitAI 28/28, api 483 pass/10 skip/0 fail (invention-glb-upload file fails to load: DB not configured, same on every head).
Note: the first run had all 4 heads in parallel, which made the timing/route tests flaky. I re-ran api serially, and the serial numbers are the ones below.

## 1. TESSERA PR #65 — FAIL (head moved)
Expected 5e437c30; actual head 38055af5. No merge-base with main (unrelated history): 191 commits, 5672 files, −768k lines, CONFLICT vs main. Commit emails are not noreply: 113 vitalitychems@gmail.com, 66 cursoragent@cursor.com. Its tests set TESSERA_ENABLE_COLONIAL_FALLBACK=1 (scoped, and restored afterwards). api 244 pass, 4 files failed. TESTED.

## 2. TESSERA PR #298 @ fdb2cb61 — PASS
Base 47983dda (=main), 1 commit, 6 files, merge clean, noreply email, gitleaks 0, no TESSERA_ENABLE changes.
Math.random: 19 removed from forum-engine/knowledge/mysticism; the only `+` line is a comment. Repo api-server/src non-test sites: 88→70 (the remaining ones are ID suffixes/jitter, out of scope). 7 determinism tests in deterministic-selectors.test.ts.
api 483→490 pass (10 skip, 0 fail). scripts 23/23, v2 137/140, GitAI 28/28, all unchanged. TESTED.

## 3. TESSERA PR #269 @ 5552a42f — PASS
Base f91ff82c (stale), 1 commit, 2 files (v2 brain/grounded.mjs + test), merge clean, noreply, gitleaks 0.
Head alone: v2 124/127 (3 EACCES), GitAI 28/28, api 464/9 skip, scripts 18/18, so the 127/28/464 claim matches the old base (TESTED). The 127 counts all v2 tests, of which 124 pass.
Merged onto main (63171af8, local only): v2 142/145 (+5 vs 137), GitAI 28/28, api 483/10. No drop. TESTED. A rebase is recommended.

## 4. Gitbook PR #70 — FAIL (no CI)
Merged 2026-10-13 06:00 CT (merge 75b5ffcc) during the freeze. Head b861691b: 0 check runs, 0 statuses (combined "pending"). REPORTED via API.
