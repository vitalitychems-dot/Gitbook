# Phase 0 selffix dry-run ledger

IDENTITY: Tessera Admin coordinator  
Repo: vitalitychems-dot/TESSERA  
Phase: 0 (suggest-only; no branches / PRs / merges)  
Keyed by `run_id`. Deduplicate: if `run_id` already has a row, do not write another proposal.

| run_id | sha | branch | failing step | class | proposal file | status |
| --- | --- | --- | --- | --- | --- | --- |
| 37381588511 | 50876d40cc1ed03538fa0dd4761231805292d5da | main | Audit all dependencies | Unpatched audit advisory blocking CI | dryrun/37381588511.md | DRY-RUN COMPLETE (class correct; patch match YES vs PR #1) |
| 37362882386 | 6fc8a69411c94caa4b018c8158718b345c6157d5 | cursor/hyb-005-audit-ignore-943c | (none — empty steps) | infra-cancel | dryrun/37362882386.md | DRY-RUN COMPLETE (class correct; escalate, no code fix) |
| 38263880511 | a5023224412c535e969d2aecc0c2f4d02be7b972 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38263880511.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315701563 | 2e65a4accd2581fb60dc607e91b62fcf9558da3f | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315701563.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315708049 | 07b0cbdb275f5745455fd3a0cc6b1b561aaf1618 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315708049.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315718561 | 739621f07a56d107fa000c804f47f15b8687b600 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315718561.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315752640 | ed82031a5f9e0b58541761adab627b4b38551441 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315752640.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315767217 | 54ae83ad21ec44cc58efe1036042e7c261f5ea85 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315767217.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315775003 | 75102a07ab527b8dabec83c71e2313ee1e136e62 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315775003.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315789463 | 409306e6a1fead4f663eea5be8f934fc5422b0f6 | main | (none — empty steps; billing annotation) | infra-cancel (Actions billing/spending-limit) | dryrun/38315789463.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315800527 | ec5268e6db393eb47f7b69ea3757dd073b81a766 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315800527.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315808976 | 7235fbcd332b2a87802cfede875ae1e5a72ff2d9 | main | (none — empty steps) | infra-cancel (Actions billing/spending-limit) | dryrun/38315808976.md | DRY-RUN COMPLETE (escalate, no code fix) |
| 38315822251 | 66a412ee1abdb0a30868353bf41e66e04532338f | main | (none — empty steps; billing annotation) | infra-cancel (Actions billing/spending-limit) | dryrun/38315822251.md | DRY-RUN COMPLETE (escalate, no code fix) |

## Two clean dry runs criterion (TESTED)

Both replays classified correctly (allow-listed audit class; infra-cancel). **Criterion met: YES.**

## Live event 2026-10-12T22:17:45Z (TESTED)

Listener woke on main `validate` failure (run **38315822251**, merge #204). Burst of 10 main failures after merges #195–#204 (22:16–22:17Z) plus earlier same-day **38263880511**: all `steps=[]`, `runner_id=0`, logs 404. Check-run annotation (TESTED on 38315822251 and 38315789463): GitHub Actions billing / spending-limit block — jobs never started. Class **infra-cancel**; **no code fix**. Escalate once as BLOCKED infrastructure. Later wakes for these run_ids dedupe here.
