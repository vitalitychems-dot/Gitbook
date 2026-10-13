# Einstein loop guard (mandatory, 2026-10-13)
1. First step of every run: if /workspace/einstein/loop/STOP exists -> exit immediately, do nothing.
2. NEVER merge (no `gh pr merge`, no PUT /pulls/N/merge, no merge_pull_request). Open PRs only,
   comment "Ready for Security/Moderator/Build gate", and let the 30-min gated timer merge.
3. Ship only via /workspace/einstein/round4/ship.sh (open-only, STOP-guarded).
