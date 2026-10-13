# Build gate — TESSERA main 47983ddabd96c7804845705bc3d2b9eac0da2c4d (#290) — 2026-10-13 ~5:58 AM CT
Verdict: PASS (with env-only failures noted)
- df: 15G free at start (89%); 23G free after install.
- Ancestry: 234e3dcf IS ancestor of tip (32 commits since). No rewrite since 234e3dcf. f76d6484 object still fetchable but NOT an ancestor of 234e3dcf or tip — consistent with the approved secret-scrub rewrite that preceded 234e3dcf.
- Emails 234e3dcf..tip (author+committer): only 332565808+vitalitychems-dot@users.noreply.github.com, noreply@github.com.
- Tests (Node 22.20.0, pnpm 11.25.0, no DATABASE_URL), log: 4798-tests.log
  - scripts 23/23 (baseline 15/15)
  - v2 137/140, 3 fail: EACCES mkdir /opt/cursor/artifacts (hard-coded screenshot path in v2-063/064/065 tests; box env, not code). Baseline 116/116. Pass count up, no logic failures.
  - GitAI 28/28 (baseline 27/27)
  - api-server 483 pass / 10 skipped / 0 failed tests; 1 file fails at load: invention-glb-upload.test.ts (DbUnavailableError, needs DB). Baseline 420 with 4 files skipped for DB.
- gitleaks (/workspace/pubscan/gl.toml, 234e3dcf..HEAD, max 50MB): 32 commits, no leaks. Report gl-4798.json.
- Recommendation: make v2 screenshot dir configurable (e.g. os.tmpdir()) so 3 tests pass off-Cursor.
