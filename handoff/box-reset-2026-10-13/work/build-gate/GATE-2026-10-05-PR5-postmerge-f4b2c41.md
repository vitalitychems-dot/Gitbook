# Build gate — PR #5 post-merge (vitalitychems-dot/Gitbook) @ main f4b2c41e

**RESULT: PASS**
**TESTED** — Build lane ran every check below itself (2026-10-05 ~15:48 CT). Read-only: no merge, push, review, comment, or label.

## Merge identity
| Field | Expected | Actual | OK |
|---|---|---|---|
| PR | #5 merged | merged=true, merged_at 20:46:03Z (3:46 PM CT), merged_by vitalitychems-dot | Y |
| Head at merge | 910681660b9076dae0ee49b3c412502d58f1f2a0 (pre-merge PASS) | 910681660b9076dae0ee49b3c412502d58f1f2a0 | Y |
| Branch | tessera/gb-015-019-021-020 (NOT tessera/gb-015-021-approved) | tessera/gb-015-019-021-020 | Y |
| Base | feaeb558 (stated main) | feaeb558b88df9679a45b4a03a375f58e50bcb4d | Y |
| Merge commit | — | f4b2c41ee458e54fc4f12cecd4cab941aa8e627c (merge commit, parents feaeb558 + 91068166, GitHub-verified signature) | Y |
| Main tip now | f4b2c41e | f4b2c41e (first in main log) | Y |
| Merge tree vs head tree | equal | 0bca12fd… == 0bca12fd… | Y |
| Stat | +121/-42, 8 files, 4 commits | +121/-42, 8 files, 4 commits | Y |

Merge tree equals verified head tree, so main content is byte-identical to the head that passed GATE-2026-10-05-PR5-91068166 (frozen hashes eb81d94f, 4ecfef83, 68bcb522, 2e3b5400 all matched there).

## Blob check on main tree 0bca12fd
| File | Expected blob | Main blob | OK |
|---|---|---|---|
| brain-consciousness/AGENT-WORKPLAN.md | 3f93f1c2 | 3f93f1c2 | Y |
| brain-consciousness/SNN-SOURCE-MANIFEST.md | 3c13149e | 3c13149e | Y |
| brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md | 25055cde | 25055cde | Y |
| intake/CORTICAL-LABS-READINESS.md | 0703e754 | 0703e754 | Y |
| intake/HYBRID-CONSOLIDATION-BACKLOG.md | 11353ce3 | 11353ce3 | Y |
| mesh/AGENT-SKILL-MATRIX.md | 0a993e1c | 0a993e1c | Y |
| mesh/COLLABORATION-PLAYBOOK.md | 8ee89bbf | 8ee89bbf | Y |
| mesh/roles/grok-bot.md | c0d88f3b | c0d88f3b | Y |

## Relative links in the 8 touched files
| From | Link | Target on main | OK |
|---|---|---|---|
| brain-consciousness/AGENT-WORKPLAN.md | SNN-SOURCE-MANIFEST.md | brain-consciousness/SNN-SOURCE-MANIFEST.md | Y |
| intake/HYBRID-CONSOLIDATION-BACKLOG.md | ../merge/hyb-007-z-app.md | merge/hyb-007-z-app.md | Y |
| intake/HYBRID-CONSOLIDATION-BACKLOG.md | CORTICAL-LABS-READINESS.md | intake/CORTICAL-LABS-READINESS.md | Y |
No other relative links in those files (external http links not fetched).

## Overlap check
- Open PRs on Gitbook after merge: none.
- GB-017, GB-018, GB-016 not on main (being rebased separately, as the PR body says).
