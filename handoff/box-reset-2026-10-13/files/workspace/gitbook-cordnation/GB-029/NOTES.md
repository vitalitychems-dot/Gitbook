# GB-029: intake log backfill for PR #8, PR #9, and PR #10

## Rev 3 (current)
**Status:** DRAFT. Intake status `in review`; not yet handed to the Moderator. Nothing pushed, no PR opened, no `TESSERA_ENABLE_*` change.
- **Ruling:** Tessera, 17:04 CT. Build rev 3 from rev 2 (`dbfc0ad4…7c37`) with exactly two changes.
- **Base:** main `45651521a137c4448673d6abfaa77e1567230f83`, re-confirmed read-only at 17:04 CT.
- **Diff:** `GB-029/GB-029-rev3.4565152.diff`, 19 lines, 1 file (`intake/log.md`), 1 hunk, +8/−4.
- **sha256:** `34285eff247dc1e7519e30eb769fcf3a5891a0879170ee2a75cb777901d7ca83`
- **Interdiff:** `GB-029/GB-029-rev2-to-rev3.interdiff`, 20 lines, 1 file, 1 hunk, +5/−5. sha256 `4980e6affe22985ffdb7540c57581f8239f96c9fafa4df0443fe73d6ea38b3d0`.
  - It contains exactly 5 cell changes. A script compared every removed/added line pair: all other cells are byte-identical.
- **Apply:** on clean 4565152:
  - `git apply --check` rc=0 and forward `git apply` rc=0. The result tree (eae26eda) equals the drafted tree.
  - Reverse `--check` rc=0, and reverse apply rc=0. The tree after reversing equals the 4565152 tree (af90e745).
  - Interdiff `--check` on rev 2's result rc=0.
  - See `VERIFY-APPLY-rev3.txt` and `apply-rev3/`.
- **Reproduce:** run `port29r3.py <tree>` on 4565152. It calls `port29r2.py`, which calls `port29.py`. Regenerating rev 2 still gives dbfc0ad4.

### Rev 3 changes vs rev 2 (exact)
1. **GB-029 title:** "Intake log backfill for PR #9 and PR #10" → "Intake log backfill for PR #8, PR #9, and PR #10".
2. **GB-022, GB-023, GB-024, GB-025 Moderator notes:** "; [board receipt](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003345353)" inserted right after "merged 16:30 CT)".

### Comment check (read-only, 17:04 CT): MATCHED
Issue #2 comment 6003345353 exists. Details:
- Posted 21:30:40Z = 16:30 CT by vitalitychems-dot ("IDENTITY: Tessera Admin coordinator").
- Heading: "Status 16:31 CT: GB-022, GB-024, GB-025, GB-023 merged (TESTED)".
- States: PR #8 merged as 979c35e0be9a27ab143c7dcfc714d979b11e10a0, head pinned to cba4140d.
- Gates: Moderator 16:22, Tessera 16:23, Security 16:24, Build 16:26; Build PASS on PR head cba4140d at 16:30; Father's yes ("Approve all") at 16:22.
- It is the PR #8 merge receipt.
- Minor note, no change made: the comment's heading says 16:31 CT, while its GitHub timestamp and the merge time are 16:30 CT.

## Rev 2 (SUPERSEDED by rev 3; kept for the record)
**Status:** SUPERSEDED by rev 3 (Tessera ruling 17:04 CT). Was DRAFT. Intake status `in review`; not yet handed to the Moderator. Nothing pushed, no PR opened, no `TESSERA_ENABLE_*` change.
- **Ruling:** Tessera, 17:03 CT.
- **Base:** main `45651521a137c4448673d6abfaa77e1567230f83`, re-confirmed read-only at 17:03 CT.
- **Diff:** `GB-029/GB-029-rev2.4565152.diff`, 19 lines, 1 file (`intake/log.md`), 1 hunk, +8/−4.
- **sha256:** `dbfc0ad4a5d26a74d4169be50f8e4af921b982584d05bf6efd92b9a9d80a7c37`
- **Interdiff:** `GB-029/GB-029-rev1-to-rev2.interdiff`, 20 lines, 1 file, +5/−5. sha256 `947a345a4edb4365a9d90403932ad6bc682e598d7316f6e8cde7fafc34e76180`.
- **Apply:** on clean 4565152, `git apply --check` rc=0 and `git apply` rc=0. The result tree (11c708d7) equals the drafted tree; reverse check rc=0. See `VERIFY-APPLY-rev2.txt` and `apply-rev2/`.
  - Rev 2 is a standalone alternative to rev 1 on 4565152. It does not stack on rev 1.
- **Reproduce:** run `port29r2.py <tree>` on 4565152. It calls `port29.py`, then edits the rows.

### Rev 2 changes vs rev 1 (Tessera's 17:03 CT ruling)
1. **GB-026, GB-027, GB-028:** unchanged from rev 1. Status `published`; note "Published <sha> (PR #N, merged 17:00 CT; commit …)" plus the board-receipt link.
2. **GB-022, GB-023, GB-024, GB-025:** folded into the same hunk. In each row only these columns change; ID, title, author lane, date, source and license stay as they were:
   - Status: `draft` → `published`.
   - Moderator note (was empty): "Four gates cleared (Moderator, Tessera, Security, CI/Build); Father's yes 16:22 CT. Published 979c35e (PR #8, merged 16:30 CT)". This matches the GB-015–021 merged-row format.
   - Reviewer: Gitbook / Cordnation → Father (final yes).
   - Check: "git apply --check on ecd9022…" → "Build PASS on PR #8 head cba4140d".
   - Next action: Cordnation hands to Gitbook Moderator (gate 1 of 4) → none.
   - Blocker: none (unchanged).
3. **GB-029:** status `Moderator: pending` → `in review`. That is a defined value ("Handed to Gitbook Moderator; decision pending").

### 16:30 CT check
The GitHub merge commit 979c35e0be9a27ab143c7dcfc714d979b11e10a0 is dated 2026-10-05T21:30:33Z = 16:30:33 CT. Its message is "Merge PR #8: GB-022, GB-024, GB-025, GB-023 (Father's yes 16:22 CT, Build PASS cba4140d)" and its parents are ecd9022 and cba4140d. **No discrepancy**; Tessera's 16:30 CT is used verbatim.

### Rev 2 flags (not changed)
- **GB-029 title** still read "Intake log backfill for PR #9 and PR #10". Resolved in rev 3.
- **GB-022–025 gate order:** per the recorded times (Moderator 16:22, Tessera 16:23, Security 16:24, Build 16:26 CT), Father's yes (16:22 CT) came before three of the four gates. The row uses the existing "Four gates cleared …; Father's yes 16:22 CT" form without per-gate times, as instructed.
- **GB-028 ordering and Replit HYB-012 BLOCKED post (6003881277):** still open from rev 1; see below.
- **No board-receipt link for PR #8 rows.** Resolved in rev 3 (comment 6003345353).

# Rev 1 (SUPERSEDED by rev 2; kept for the record)

**Status:** SUPERSEDED by rev 2 (Tessera ruling 17:03 CT). Was DRAFT. Intake status `Moderator: pending`; not yet handed to the Moderator. Nothing pushed, no PR opened, no `TESSERA_ENABLE_*` change.
- **Assigned:** Tessera, 17:01 CT 2026-10-05. Same pattern as GB-023.
- **Base:** main `45651521a137c4448673d6abfaa77e1567230f83`.
- **Diff:** `GB-029/GB-029.4565152.diff`, 11 lines, 1 file (`intake/log.md`), 1 hunk, +4/−0.
- **sha256:** `67840272e42f5f17c8da41cfd444e70ff4f02208e2bc643ecbecca24e43b67de`
- **Apply:** on clean 4565152, `git apply --check` rc=0 and `git apply` rc=0. The result tree equals the drafted tree; reverse check rc=0. See `apply/`.
  - The local `intake/log.md` blob (dec5f592) equals the 4565152 blob.
- **Reproduce:** run `port29.py <tree>` on 4565152.

## Read-only checks (17:01–17:02 CT)
- **Main:** `45651521…` ("Merge PR #10: GB-028 rev 3 (Father's yes 16:49 CT, Build PASS c507f0c2)", 22:00:51Z = 17:00 CT). Parents: ebe003fe and c507f0c2.
- **PR #9 merge:** `ebe003fe…` ("Merge PR #9: GB-026 rev 3, GB-027 (Father's yes 16:49 CT, Build PASS b23d9eb)", 22:00:46Z = 17:00 CT). Parents: 979c35e and b23d9eb8.
- **Package commits:** GB-026 rev 3 = `1e107de5`, GB-027 = `b23d9eb8`, GB-028 rev 3 = `c507f0c2`.
- **Open PRs:** 0.
- **Board receipt** (issue #2, comment 6003943663, 17:00 CT, Tessera Admin coordinator) confirms:
  - both merges and their Build PASS results
  - "All three packages cleared Moderator, Tessera, Security and Build. Father said yes at 16:49 CT."
- **Landed byte-identical:** the 4565152 tree differs from 979c35e in 35 files. All 35 are byte-identical to our local stack (979c35e + GB-026 rev 3 + GB-027 + GB-028 rev 3), and all 47 local files match 4565152.
- **Other merge-receipt spots** (what GB-023 touched: backlog, agent-checkins, decision records): no pending/backfill placeholder refers to GB-026–028. The only "pending push" text left is the historical HYB-005 check-in blocks, which GB-023 also left. So only `intake/log.md` changes.

## Changes (intake/log.md, appended after the GB-025 row)
- **GB-026**, `published`. Moderator note: four gates cleared; Ready 16:47 CT; Father's yes 16:49 CT; Published ebe003f (PR #9, merged 17:00 CT; commit 1e107de5); board-receipt link. Reviewer: Father (final yes). Check: Build PASS on PR #9 head b23d9eb. Next action and Blocker: none.
- **GB-027**, `published`. Same as GB-026, but commit b23d9eb8.
- **GB-028**, `published`. Gates: Moderator 16:48 CT, Tessera (carried over from rev 2), Security 16:50 CT, Build 16:54 CT; Father's yes 16:49 CT; Published 4565152 (PR #10, merged 17:00 CT; commit c507f0c2); board-receipt link. Check: Build PASS on PR #10 head c507f0c2.
- **GB-029**, new intake entry. Author lane Gitbook / Cordnation; status `Moderator: pending`; Reviewer: Gitbook Moderator; Check: git apply --check on 4565152; Next action: Gitbook Moderator reviews (gate 1 of 4); Blocker: none.
- **Format:**
  - The rows follow the existing 12-column format and the GB-015–021 merged-row wording ("Four gates cleared …; Father's yes …. Published <sha> (PR #N…)", Reviewer "Father (final yes)").
  - "Merged" is recorded as the log's existing status `published`, with "Published <merge sha> (PR #N, merged 17:00 CT)" in the note. No `merged` status value is used anywhere in the log.
  - Author lane is spelled "Gitbook / Cordnation", as the log intro does.
- **Canon:** no gate banners; the front matter `status: published` is untouched; Pen isn't named as a lane (no Pen text added).

## Flags (not changed)
1. **GB-022, GB-023, GB-024, GB-025 still read `draft` in the log**, although PR #8 merged them as 979c35e (Father's yes 16:22 CT; Build PASS cba4140d). The task scoped GB-029 to PR #9 and #10, so I left them. If Tessera wants them backfilled the same way, it's 4 changed rows in the same hunk.
2. **`Moderator: pending`** isn't defined in `intake/status-definitions.md`. The closest defined values are `draft` (not yet ready for Moderator) and `in review` (handed to Moderator, decision pending). It is used because the task specified it.
3. **Order of GB-028's gates:** Father's yes (16:49 CT) came before GB-028's Security (16:50) and Build (16:54) passes, per the given gate times, the merge commit message and the receipt. Canon has Ready (all four gates) before Father's yes. The row records the times as given and doesn't comment on the order.
4. **Replit's latest board post** ([comment 6003881277](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003881277), 21:57Z = 16:57 CT, before the merges) still says HYB-012 `STATUS: BLOCKED`. Reasons given:
   - no isolated writable checkout
   - an unanswered test-first scope question at comment 6001771468

   Not acted on here; reported for Tessera.
