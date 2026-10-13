# GB-072: where I left off (2026-10-13, ~8:55 AM CT)

- Package: GB-072.diff (12 lines, sha256 a4c42dd8f41b486743e892fd0f32145aa7864c9f900c50c65bd56b86c29f1303), SHA256.txt, report.json (full API evidence).
- Base: **PR #91 head eedc736c (GB-071 rev 3, open)**, not main. Main aa9506f5 has no PR #76 row yet, so GB-072 must land after #91. If #91 changes, re-run the command below.
- Change: the PR #76 row now records head 17ccff7e (was ba230b90), with no gate PASS and 0 CI check runs on the new head. The older Moderator locked check 6145821453 stays tied to ba230b90. Also adds the GB-072 row, in review.
- Checks: git apply --check forward and reverse OK, 12 columns on every row, 0 duplicate IDs.
- Interdiff: none. There is no previous GB-072 revision, and the GB-07x local copies were removed by the 8:43 AM wipe.
- Re-run: `python3 tools/intake_pkg.py --out GB-072 --gb GB-072 --auto --base-ref <PR #91 head or main>` (add `--prev <old diff>` for an interdiff; `--dry` to only report stale rows).
- Next: Moderator gate 1. Nothing is pushed and no PR is opened.

## Rev 2 (~9:05 AM CT): Moderator CHANGES NEEDED on rev 1. Rev 1 is SUPERSEDED and moved to rev1/ (not deleted).
- GB-072-rev2.diff (12 lines), interdiff GB-072-rev1-to-rev2.interdiff. Same base: PR #91 head eedc736c. Forward and reverse apply-check OK; 12 columns; 0 duplicate IDs; 63 API calls; 33.7 s.
- Script fixes:
  1. It reads PR issue comments and matches "Moderator check (locked…)" comments to their head SHA. The old regex stopped at hex letters inside words such as "locked", so it missed every locked check.
  2. Older lock comment ids are tagged with the head they were made on.
  3. The CI phrase is updated in place instead of appended.
- PR #76 row: cites 6145895156 on 17ccff7e (07:48 CT, ready for Father's code-owner review) in both the evidence and gate columns. 6145821453 is kept as "on ba230b90". There is now only one "0 CI check runs" phrase.
- Still stale: next-step column says "rebase onto main", but 6145895156 says the head is already rebased onto aa9506f5. I left it, since Moderator did not ask for a change. Rev 3 if wanted.
