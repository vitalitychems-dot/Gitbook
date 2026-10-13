# Mesh queue — Cursor cloud-agent dispatch
1. `TASKS.json` — one entry per task (id, repo, scope, acceptance, lane, status, claim lock).
2. `python3 dispatch.py --max 6 --agent Tessera [--claim]` — picks queued tasks whose scope does not overlap each other or any open PR, and renders a prompt per task from `PROMPT-TEMPLATE.md`. Launch one cloud agent per prompt (CloudAgent tool), branch `cursor/<id>`.
3. `autogate.sh <repo> <pr> [--merge]` — Node 22 tests (TESSERA), gitleaks, noreply-author check, no `.github/workflows`, no `TESSERA_ENABLE_*` flips. Squash-merges with the noreply author only on PASS and `--merge`.
Gitbook is ~11 GB at depth 1, so autogate uses a blob-less, sparse checkout of only the changed files.
