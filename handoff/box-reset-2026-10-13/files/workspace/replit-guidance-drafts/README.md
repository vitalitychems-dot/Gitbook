# Replit agent guidance draft pack (2026-10-05)

Prepared by Command Center executor. PRs were NOT opened: this box has no git/gh push auth,
cursor-github MCP has no file-write/commit tool, and CloudAgent (cursor namespace) is unavailable.

## Confirmed targets
1. vitalitychems-dot/Zz — base: main (6e64ca612e450cf30eb924162ca76f771deee44d)
   - update replit.md (exists), update AGENTS.md (exists)
2. vitalitychems-dot/5t — base: main (ea874b7a391ce6d207038215700ce97101114884)
   - update replit.md (exists), create AGENTS.md (missing)
3. vitalitychems-dot/1 — base: subrepl-nftoz8d7 (7de2b4a778ec62f084e92dd4ed5a3e9be35e45ab) EXISTS
   - update replit.md (exists), create AGENTS.md (missing)

## Start-here path confirmed
https://github.com/vitalitychems-dot/Gitbook/blob/main/mesh/replit-agents-start-here.md

## Side effect to clean up
Accidental empty branch created while probing MCP create_branch:
  vitalitychems-dot/Zz refs/heads/cc/replit-agent-guidance-probe @ 6e64ca6
(no commits beyond main; delete when convenient)

## Desired branch / PR
- branch: cc/replit-agent-guidance (cut from base above)
- title: Replit agent guidance: Gitbook start-here, PR-only, status on issue #2
- draft: true; do not merge; do not mark ready
- body: see PR_BODY.md
- touch ONLY replit.md and AGENTS.md
