# Build gate: Gitbook PR #11 post-merge (GB-029 rev 3) — verify-only

**RESULT: PASS** · **TESTED** (all checks run by Build via cursor-github reads, ~17:29–17:31 CT). No push, merge, comment, or edit.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | PR #11 merged | PASS | state=closed, merged=true, merged_at 22:28:49Z (17:28 CT), merged_by vitalitychems-dot, merge_commit_sha `bc6b32871faed56b13df3dfadc849ec725d60f14` |
| 2 | Main tip = merge commit | PASS | get_commit main → `bc6b3287…`; signature verified (GitHub web-flow) |
| 3 | Parents = base + pinned head | PASS | parent1 `45651521a137c4448673d6abfaa77e1567230f83` (expected base), parent2 `baa0daeb64cf78dbbba3853a617f86421764edcb` (Build-verified head) |
| 4 | Tree = verified head tree | PASS | merge tree `cd9cf21bddba62b0451bb972652c4df0471c81d3` == PR head tree from pre-merge gate (GATE-2026-10-05-PR11-baa0daeb.md, which verified base→head = only intake/log.md `dec5f592`→`eee24da2`, 160 entries, frozen sha256 34285eff…ca83 binary-identical) |
| 5 | Diff vs base (first parent) | PASS | 1 file `intake/log.md` modified +8/−4, blob `eee24da289936d626e4e0cba29fffe842db0cc71` (== frozen post-apply blob) |
| 6 | No TESSERA_ENABLE_* flips | PASS | 0 occurrences in merge patch |
| 7 | Open PRs after merge | PASS | list_pull_requests open = 0 |

Since tree identity holds, main = 45651521 + frozen GB-029 rev3 change exactly.

**OVERALL: PASS (TESTED)**
