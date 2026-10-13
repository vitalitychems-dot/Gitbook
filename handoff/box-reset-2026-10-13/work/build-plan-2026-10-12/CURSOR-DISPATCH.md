# Cursor dispatch — 2026-10-13 ~2:50 AM CT

## Merged (all squash, author 332565808+vitalitychems-dot@users.noreply.github.com)
- TESSERA #255 DB-optional boot → 7edb62e. Rebased onto main (fa0d2b6); merged tree byte-identical to the tested tree. Node 22.20.0, DATABASE_URL unset: api-server 463 passed / 9 skipped, 52/53 files (main before: 48/52 files load; 4 DB-only files failed at import → now only invention-glb-upload fails, "database not configured"). With DATABASE_URL: NOT run (no Postgres on box). gitleaks: no leaks.
- TESSERA #259 GitAI key required → 80d2c74. Removed X-GitAI-Handle in gitai server + v2 studio; agent/moderator accounts need Bearer key or X-GitAI-Key (forged header or cookie → 401). GitAI 28/28 (+1 regression test), v2 116/116. README + openapi updated. Follow-up: spectator cookie is still the unsigned handle (queued as Q-007).
- Gitbook #56 mesh/queue pipeline → 4feab77. Gated by its own autogate.sh.

## Pipeline (Gitbook mesh/queue/)
TASKS.json (7 tasks: Q-001 PR #45 rebase, Q-002 GB-067/068, Q-003 GitbookAI→GitMesh 5 files, Q-004 generative_agents REA retry, Q-005 embedding recall [blocked: model download], Q-006 affect recognition, Q-007 sign spectator cookie), PROMPT-TEMPLATE.md, dispatch.py, autogate.sh, README.md.
Dispatcher run now selected Q-003, Q-004, Q-006, Q-007; skipped Q-001/Q-002 (scope overlaps open PR #45). Rendered prompts: /workspace/dispatch/prompts.json.

## Cloud agents
NOT launched: the executor has no CloudAgent tool. No bc- ids exist from this run. Parent should launch one CloudAgent per entry in prompts.json, then run `dispatch.py --claim` and commit the claims.

## Metrics (real)
- Baseline, last 24 h: 75 PRs merged across TESSERA+Gitbook = 3.1/h; PR open→merge mean 1.3 min, median 0.1 min (PRs are opened after work is done, so this is not true task time).
- This run: 3 PRs merged in ~10 min (2:41→2:51 AM CT).
- Autogate: Gitbook PR ~1–11 s (sparse blob-less); TESSERA ~1 min tests.
- Credits per task, mine vs cloud agent: NOT measurable — no credit counter is exposed to me. After/before for cloud agents can only be measured once they are launched.

## Blocked / notes
- Disk hit 98% (3.6G free) mid-run: a depth-1 Gitbook clone is 11 GB. Deleted my own clones; disk back to 87% (16G free). autogate now uses sparse blob-less clones.
- Gitbook autogate does not run qlab's Python tests (no Gitbook test runner).
- The 4 DB-only api-server files: autogate tolerates import failures mentioning DATABASE_URL / database not configured only.
