# GB-073: where I left off (2026-10-13, ~8:57 AM CT)

- GB-073.diff: new file direction/NEXT.md only, against main aa9506f5. direction/ does not exist on main (API 404). 20 lines.
- sha256 in SHA256.txt. The forward and reverse apply-check results are in APPLY-CHECK.txt.
- Sources: issue #72 body plus 22 comments, read with 2 gh api calls (the issue, and its comments).
- 10 goals: 8 cite issue #72 comments. Goals 9 and 10 (Cordnation's script and GB-072) have no posted source and are marked "pending (not posted)".
- There is no intake/log.md row for GB-073 yet. Add one via intake_pkg.py once GB-071 (#91) and GB-072 settle, to avoid a third stacked log edit.
- Next: Moderator gate 1. Nothing pushed.

## Rev 2 (~9:05 AM CT): Moderator CHANGES NEEDED. Rev 1 moved to rev1/ (not deleted).
- Header now says ADVISORY until Father reviews it.
- Every sourced row links to a real issue or PR comment URL.
- Rank 2: TESSERA #315 merged 08:29 CT as 54a69041 (API). 349x is Moderator's figure, REPORTED; I found no posted #72 comment for it. 8.5x is labelled ESTIMATE. "About 20x" is kept because Build posted it in comment 6146678100.
- Rank 6: #79 FAILed and was superseded by #88 (Moderator PASS, comment 6145880467; −89% full checks per the #88 title).
- Rank 10: GB-072 rev 2 APPROVED (REPORTED).
- Ranks 9 and 10 still have no posted URL.
- PR #76 compare aa9506f5...17ccff7e: ahead 1, behind 0, merge base aa9506f5, so the head contains main. Reported only; no GB-072 rev 3.
- Also fixed: rev 1's links were empty, because a shell variable swallowed the comment ids. All 8 sourced rows now carry full URLs.
