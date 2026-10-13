# GB-018: mechanical rebase onto feaeb558 (Tessera task 15:42 CT)

> **Base update (Tessera 15:46 CT):** the final base is **f4b2c41** (`f4b2c41ee458e54fc4f12cecd4cab941aa8e627c`), which is PR #5 merged on top of feaeb558. PR #5 landed GB-015, 019, 021 and 020.
> - A snapshot of feaeb558 with those 4 diffs applied matches every one of the 8 PR #5 blobs (`git hash-object`).
> - PR #5 did not touch flow.md, roles.md, command-center.md, agent-checkins.md, SUMMARY.md or the operating-mode page.
> - This package's diff regenerated on f4b2c41 is **byte-identical** to the feaeb558 version. It is saved as `*.f4b2c41.diff`, and `*.feaeb558.diff` is kept as an identical copy.
> - Copies are in `base-f4b2c41/` and `proposed-f4b2c41/`.
> - Apply checks on f4b2c41: solo OK, 0 offsets; stack 017 → 018 → 016 rev 3.2 OK, 0 offsets.


- **Main:** `feaeb558b88df9679a45b4a03a375f58e50bcb4d`. Parent fb984ad, then 1e3bb50.
- **Overlap check:** 0 open PRs at ~15:44 CT. Tessera's 015/019/021/020 PR was not visible yet.
- **What blocked it:** fb984ad changed `history/coordination/agent-checkins.md` in the HYB-012 blocks. It added `LATEST GITBOOK BASE`, `WAITING ON` and `LATEST ISSUE COMMENT` lines and changed `NEXT CHECK-IN` and `FOLLOW-UP`. GB-018 hunk 1 used the old `BLOCKER:` line as leading context, so it failed at :27.
- **New diff:** `GB-018.feaeb558.diff`, 130 lines, sha256 `e6242006524510333b26baf7032c4e71c882f1a712cf3f2cf4e36279e6cf4e93`. The old `GB-018.diff` (96d8861c) is kept as-is.
- **Copies:** `base-f4b2c41/` and `proposed-f4b2c41/` hold the 4 files.

## Interdiff

`INTERDIFF-diff-of-diffs-1e3-to-feaeb558.txt` is the diff-of-diffs. It shows:

- hunk 1: header `-27,7 +27,6` became `-30,7 +30,6`, and its first context line `BLOCKER: …` became `LATEST ISSUE COMMENT: https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6002431534`;
- hunks 2–4: the headers move by +3 lines (`-51/-86/-152` became `-54/-89/-155`).

Every `+` and `-` line is byte-identical in all 4 files. The SUMMARY.md, HYBRID-CONSOLIDATION-BACKLOG.md and new merge page sections are unchanged.

**Verdict: CONTEXT LINES ONLY (plus hunk-header line numbers).** It's a mechanical rebase, so it needs only a Build re-check.

## fb984ad lines kept

All of them. The applied result contains every fb984ad line verbatim. GB-018 still deletes only the 2 blank lines Tessera accepted at 15:12 CT: one before `## HYB-012 — blocker evidence` and one before the `replit-hyb012-static-verification` marker. It adds the HYB-005 ledger row and the HYB-005 claim block, as before.

## Apply check (feaeb558 snapshot)

- Solo: OK, 0 offsets.
- Stack 015, 019, 021, 020, 017, 018, 016 rev 3.2: OK.
- Stack 017, 018, 016 rev 3.2: OK.
