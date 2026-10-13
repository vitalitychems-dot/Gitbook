# Self-improvement gate drafts (Gitbook #71, sections 3 and 6) — Build lane

Drafted 2026-10-13 against TESSERA main 47983dda and Gitbook main 75b5ffcc. Not pushed; Tessera opens the draft PR(s).
Out of scope here (owned by Tessera's executor): moderator-lock, CODEOWNERS, issue-opening cron.

## Files and target paths
| File here | Target repo | Target path |
|---|---|---|
| tessera/required-gate.yml | TESSERA | .github/workflows/required-gate.yml (A + B: install/audit, typecheck-build, tests matrix, security tests, hygiene, score-drop, gate) |
| tessera/rollback-watchdog.yml | TESSERA | .github/workflows/rollback-watchdog.yml (C) |
| gitbook/required-gate.yml | Gitbook | .github/workflows/required-gate.yml (D) |
| scripts/make_scores.py | TESSERA | .github/gate/make_scores.py (TAP / vitest JSON -> scores/<suite>.json) |
| scripts/compare_scores.py | TESSERA | .github/gate/compare_scores.py (score-drop rule, removed-tests:) |
| scripts/bench_compare.py | TESSERA | .github/gate/bench_compare.py (median p50, >5% fails) |
| scripts/check_enable_defaults.py | TESSERA | .github/gate/check_enable_defaults.py |
| scripts/check_noreply.sh | both | .github/gate/check_noreply.sh |
| scripts/check_links.py | Gitbook | .github/gate/check_links.py |
| scripts/check_tables.py | Gitbook | .github/gate/check_tables.py |

Branch protection: require the single check `gate` from required-gate in both repos.

## PR body convention
To drop a passing test on purpose, list it in the PR body:

    removed-tests:
    - exact test name as it appears in scores/<suite>.json

## Open questions / gaps
1. `gh variable set AUTOMERGE` cannot use GITHUB_TOKEN; needs a fine-grained PAT secret `AUTOMERGE_ADMIN_TOKEN` (Variables: read/write, this repo only). Father must create it.
2. Label `auto-rollback` must exist in TESSERA before the first rollback.
3. Dead-man rule runs inside the watchdog, so it catches failing cycles but not GitHub silently not scheduling it. Whatever does auto-merge should also refuse when the last scheduled watchdog success is >30 min old. Scheduled cron on GitHub is best-effort (often 5–20 min late) so 2 cycles may false-trip; consider 45 min. First-ever run sets AUTOMERGE=0 (fail-safe).
4. The existing ci.yml uses Postgres + DATABASE_URL; this gate runs DB-less as requested. The 4 api-server vitest files that need a DB will fail here (seen on 234e3dcf). Either they skip without DB (needs #255 DB-optional work, on hold for Father) or they get listed as expected-skip. Until then the api-server suite will be red.
5. ci.yml runs plain `pnpm audit`; this uses `--audit-level high` as requested. Keep or retire ci.yml?
6. Three v2 tests write screenshots to a fixed folder (seen on 47983dda); they may fail on runners. Fix in TESSERA (configurable dir) before making v2 required.
7. Baseline = latest successful push-to-main required-gate run. The first run after landing has no baseline and passes the score step (bootstrap).
8. Bench only runs on PRs, only if scripts/bench-latency.mjs exists, compares p50 per path. bench-latency is 200 runs x paths x 5 x 2 refs x up to 3 attempts; may be slow — measure and maybe cut to `--runs`.
9. gitleaks binary is downloaded by version without checksum verification (TODO in YAML). The TESSERA config /workspace/pubscan/gl.toml should be committed as .github/gate/gitleaks.toml if wanted; the workflow uses it when present.
10. Actions are pinned to SHAs for checkout/setup-node/pnpm-action-setup/upload/download-artifact v4 and setup-python v5 as resolved on 2026-10-13.
11. Watchdog `verify` reuses required-gate via workflow_call (every 15 min = full install+tests; Actions minutes cost). Rollback reverts the tip commit only; if several commits landed between cycles it reverts the newest, not necessarily the culprit.
12. qlab job assumes numpy only (or tools/qlab/requirements.txt). The two long aqft tests (8–13 min) are excluded by `qlab test` itself and are not run.
13. Noreply check accepts `noreply@github.com` as committer (GitHub web/squash merges use it).
