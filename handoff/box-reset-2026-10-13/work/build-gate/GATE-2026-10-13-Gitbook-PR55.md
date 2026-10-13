# Build gate — vitalitychems-dot/Gitbook PR #55 (qlab) — 2026-10-13 ~02:10 CT
**Verdict: PASS @ head 3e17e9ab506a9dcee9f51aa32438475b4656ca38** (verify-only; not merged/commented)

- Head: rick/qlab-v1 @ 3e17e9ab506a9dcee9f51aa32438475b4656ca38 (1 commit)
- Base: main @ 8138ea2f83dec0f851f2340b7e9584b4e5bc40b0
- Mergeable: true, mergeable_state=clean, rebaseable=true (GitHub API, REPORTED)
- Files: 34, all `added`, all under tools/qlab/, +1266/−0. No .github/workflows, no TESSERA paths, no SUMMARY.md.
- Method: no clone (disk 97%). Rebuilt all 34 files from PR patches into /tmp/pr55; every file's git blob SHA matched the PR's blob SHA (0 mismatches) => exact head content. /tmp/pr55 deleted after.

## TESTED
- `cd tools/qlab && OMP_NUM_THREADS=1 python3 -m qlab test` (numpy 2.5.3): 8/8 OK, ALL PASS —
  test_sim 3.1s, test_opt 15.0s, test_noise 1.9s, test_geom 0.1s, test_opt2 21.2s, test_opt3 49.9s, selftest_twin 14.1s, selftest_cli 0.3s.
- Scope grep (socket|requests|urllib|http|subprocess|wallet|payment|vault|TESSERA_ENABLE|secret|token|eval/exec): 0 hits for network libs, wallet/payment/vault, TESSERA_ENABLE_*, secrets. `subprocess` only in qlab/__main__.py (runs local test files with sys.executable) and selftest_cli.py (runs `python -m qlab optimize` locally). URLs only in NOTICE/RESULTS.md as Apache-2.0 attribution text (not fetched at runtime).

## REPORTED / not checked
- Docs: only tools/qlab/README.md and RESULTS.md; no SUMMARY.md touched, so no Gitbook nav links to check. External raw.githubusercontent attribution URL not fetched.
- Overlap: open PRs #39, #40, #45. PR #55 only adds new files under tools/qlab/ and GitHub reports clean merge; file-level overlap with others not enumerated (inferred none).
- Moderator/Security verdicts: NOT visible on the PR (0 issue comments, 0 review comments, no reviews requested). Merge precondition in Tessera's ask ("if Moderator and Security both PASS") is not evidenced on the PR; PR body also says do not merge without Father's yes.
- CI: billing-blocked; no checks.

## Addendum, 2026-10-13 ~2:35 AM CT: long AQFT tests, no time cap (Moderator request)
Head 3e17e9ab506a9dcee9f51aa32438475b4656ca38. No clone: 34 tools/qlab blobs rebuilt in /tmp from the GitHub git tree/blob API, and all 34 `git hash-object` values match the tree SHAs. Each test ran with OMP_NUM_THREADS=1, sequentially, under a 1500 s safety timeout that was never hit. The /tmp copy was deleted afterward.
| test | exit | wall time | script "elapsed" | FAIL / pass=False | RESULTS.md says |
|---|---|---|---|---|---|
| test_aqft.py | 0 | ~784 s | 784.2 | 0 / 0 | 484 s |
| test_aqft_fix.py | 0 | ~492 s | 492 | 0 / 0 | 327 s |
Verdict: PASS for both, meaning each ran to completion with exit 0 and no FAIL markers. Caveat: neither script has an assert, FAIL output or sys.exit, so "PASS" only means it ran cleanly. These are simulation sweeps (they print fidelity tables and write aqft_results.json / aqft_fix_results.json, which are not committed), not checks against expected values. Runtimes came in about 1.5x RESULTS.md, probably because the box is shared and loaded.
Excluded by design: yes. qlab/__main__.py `test` lists 8 tests, and `--full` adds only test_aqft_avg.py. Neither test_aqft.py nor test_aqft_fix.py appears in either list, which matches RESULTS.md §7/7b documenting them as separate long manual runs.
Not merged, pushed or commented.
