# GB-026 rev 3 — Tessera rulings 16:22 CT and 16:29 CT, plus Father's 3:59 PM CT Tessera-push rule, plus the ruling-4 sources fix

**Current: rev 3 on main 979c35e** (2026-10-05 16:35 CT update). DRAFT, prepared for the four gates; NOT Ready.
- Diff: **`GB-026/GB-026-rev3.979c35e.diff`**
- sha256: `7fe2d5f273ac9826b10eb6bec1358986bb608433a681e1cb98da7a25ed1f7730`
- Size: 563 lines, 23 files, +60/−87 (`git diff --shortstat`)
- Frozen in `FROZEN-SHA256-979c35e.txt`. Rev 2 (1a5949a8) is SUPERSEDED and kept unmodified.
- **The only change from rev 2:** `mesh/roles/tessera-pen.md:52` now reads ``- Merged records from the deleted tessera-coordination repo, in [`history/coordination/`](../../history/coordination/)``. Ruling 4 points at the folder only: no file links, and no mention of COMMAND.md or STATUS.md.
- Proof that only one line changed: `git diff --numstat` rev2-tree → rev3-tree = `1 1 mesh/roles/tessera-pen.md`. `diff` of the two diff files differs only at diff line 505, the single `+` line (`apply-rev3/diff-of-diffs.txt`). The interdiff is `INTERDIFF-rev2-to-rev3.diff` (sha 6faf6ddd…).
- On clean 979c35e: `git apply --check` rc=0 and `git apply` rc=0. The result tree is 3b939545, the reviewed rev 3 tree. Rev 3 alone does not apply on ecd9022 (rc=1, as expected). Details: `VERIFY-APPLY-rev3.txt`, `apply-rev3/`.
- Tessera's 16:34 CT ruling (Origin/TESSERA merges need the literal word) is **not** in rev 3. It goes in GB-027, which stacks on rev 3. Rev 3 stays one line different from rev 2.
- Everything below describes rev 2 and still holds for rev 3, except tessera-pen.md:52.

**Current: rev 2 on main 979c35e** (2026-10-05 16:31 CT update)
- Main moved to 979c35e0be9a27ab143c7dcfc714d979b11e10a0 (PR #8 merged GB-022 v4, 024 v3, 025, 023). All 21 PR #8 blobs are byte-identical to ecd9022 + the four frozen diffs.
- Rev 2 now targets 979c35e as **`GB-026/GB-026-rev2.979c35e.diff`**, frozen in `FROZEN-SHA256-979c35e.txt`. It is byte-identical to the ecd9022-named rev 2 below (same sha 1a5949a8…).
- On clean 979c35e: `git apply --check` rc=0, `git apply` rc=0, result = drafted tree e5c867e9.
- Details: `VERIFY-APPLY-979c35e.txt`. The 8010626 ancestry check against 979c35e passes (`PUBLISH-SHA-EVIDENCE.md`, addendum).
- Line numbers below are the same on 979c35e, because the drafting base tree is identical.

**Rev 2 (pre-merge name):**
- Diff: `GB-026/GB-026-rev2.ecd9022.diff`
- sha256: `1a5949a8191b4b06ca4fc918535a3e91e273048ded51bdfc40210a40805b8ee1`
- Size: 563 lines, 23 files, +60/−87 (`git diff --shortstat`)

**Rev 1 is SUPERSEDED.** It stays on disk unmodified as `GB-026/GB-026.ecd9022.diff`, sha `6b730f73…`. Rev 1 was also +60/−87. The "+60/−58" I reported for it was a grep undercount: my grep skipped removed markdown bullets, which begin with `--`.

**Interdiff rev 1 → rev 2:** `INTERDIFF-rev1-to-rev2.diff` (sha 9306ef4b…, 15 files, +19/−19). It contains only the changes in "Rev 2 changes" below. The rest of the package is the same as rev 1, and the file and line map further down still holds; changed lines are noted there.

## Rev 2 changes (Tessera rulings 16:29 CT)
1. **Merge wording.** Every rev-1 Origin-only merge phrase is replaced with Tessera's text, adapted only for context:
   > "Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed. Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes before anyone merges."

   Where it went:
   - mesh/TESSERA-GITBOOK-OPERATING-MODE.md:44 (step 12)
   - mesh/flow.md:59 (Merge authority row)
   - intake/status-definitions.md:28
   - review/moderator-handoff.md:38 (Approve row; replaces "Origin merge only on Father's explicit `merge`")
   - review/moderator-handoff.md:48 (Out of scope / Merges, shortened form)
   - intake/how-to-submit.md:27 (replaces "Origin merges need a separate explicit `merge`" on the line rev 1 rewrote)
   - mesh/roles/open-helper-agent-2.md:20 ("merges need Father's explicit `merge`" → "every merge needs Father's explicit yes on the listed item", on the line rev 1 rewrote)
   - mesh/flow.md:38: mermaid merge node → "Origin / TESSERA merge: Father's explicit yes?"

   To make sure no Tessera-merge wording reads as if it skips Father:
   - operating-mode:23 Build row and flow.md:79 Build bullet: "verifies Tessera's push PR (opened after Father's yes) before she merges"
   - build.md:15: "each GitBook package Father said yes to"
   - mesh-lane-map.md:50: "the package Father said yes to"

   Re-scan: `rg -i merg` across all 23 files after rev 2. Every Tessera merge is stated after Father's yes, and no line suggests a Gitbook merge skips Father.
2. **Publish notes.** All six GB-004–014 front-matter notes now read "Published 2026-10-05 (commit 801062641f30d2acf45dbea4748323f20c5e30d8)". Evidence is in `PUBLISH-SHA-EVIDENCE.md`: 8010626 is an ancestor of ecd9022 and added all six pages. Only who-tessera-is was edited later (f71e00a0, body only), so the landing SHA is 8010626 for all six.
3. **Body Status lines.** All six `**Status:** REPORTED … awaiting Father GitHub push` in-page lines stay removed, unchanged from rev 1.
4. **tessera-pen.md:52.** No longer links history/coordination/command-center.md, which is 0 bytes at ecd9022 (blob e69de29b). It now links the [`history/coordination/`](../../history/coordination/) folder ("merged records from the deleted tessera-coordination repo (PEN.md, COORDINATION.md, COMMAND.md)") and keeps the STATUS.md link to history/recovered/coordination/STATUS.md (819 bytes).
   - No COMMAND.md copy with content exists on ecd9022. The only "command" files in the tree are history/coordination/command-center.md (0 bytes) and mesh/roles/command-center.md (3349 bytes, the role page, not a COMMAND.md copy).
   - History: f71e00a0 (1:35 PM CT) deleted the 5 content lines of history/coordination/command-center.md.
   - Sizes in history/coordination/: tessera-pen-record.md 1046, coordination-record.md 1058, coordination-repository-readme.md 172, command-center.md 0.
5. **Scope is unchanged.** None of the GB-027 leftovers were added.

---
# Rev 1 base notes (still accurate except where rev 2 changes them above)

- **Diff:** `GB-026/GB-026.ecd9022.diff`
- **sha256:** `6b730f73a9aec2a93a52dba44edeeeb504cf623ce54d88eddc5f562f08a1ee3f`
- **Size (rev 1):** 563 lines, 23 files, +60/−87 (originally misreported as +60/−58) (65 anchored edits in `port26.py` plus 6 in `port26b.py`; each anchor was asserted to occur exactly once)
- **Base:** ecd902211abd202711838219b28a1e1b39ae47c4 + GB-022 v4 (ae288a54) → GB-024 v3 (3fc1fc11) → GB-025 (0a590a0c) → GB-023 (684227c6). GB-026 stacks after GB-023.
- **Frozen diffs:** the four are untouched; they were re-hashed before verification.
- **Format:** diffs only. No `index` lines; `@@` headers carry no function context.
- **Status:** draft, prepared for the four gates (Moderator → Tessera → Security → CI/Build). NOT Ready. Nothing pushed; no PRs.
- **Flags:** no `TESSERA_ENABLE_*` change. The only diff line that mentions the flags is grok-bot.md:18. On that line, only the "Father alone pushes main" clause changed; the text "TESSERA_ENABLE_* stay 0" is unchanged.

Line numbers are on the tree after GB-026 is applied. "was" gives the line on the ecd9022 + four-package stack.

## Ruling 1: tessera-pen.md sources line
- **mesh/roles/tessera-pen.md:52:**
  - Was: `- vitalitychems-dot/tessera-coordination — PEN.md, COORDINATION.md, COMMAND.md, STATUS.md`
  - Now points to `history/coordination/` (merged from the deleted repo). REV 2: now a single folder link plus a STATUS.md link; the per-file links, including the empty command-center.md, are gone. Rev 1 linked each file:
    - PEN.md → history/coordination/tessera-pen-record.md
    - COORDINATION.md → coordination-record.md
    - COMMAND.md → command-center.md
    - STATUS.md → history/recovered/coordination/STATUS.md
  - The mapping comes from merge/exact-duplicates (tessera-coordination:PEN.md etc. ↔ Gitbook history/coordination/*). STATUS.md has no history/coordination/ copy, so the line points at the recovered copy.

## Ruling 2: issue #2 = coordination board; COMMAND.md = Command Center's command file
- **mesh/flow.md:74** (ruling said :73; the stack shifts it by one). CC lane-boundary bullet: "see issue **#2** / `COMMAND.md`" → "Coordination board: [Gitbook issue **#2**](…/issues/2); `COMMAND.md` is Command Center's command file."
- **mesh/roles/command-center.md:21** (was :23): "References: issue **#2** / `COMMAND.md`" → "References: [Gitbook issue **#2**](…) (the coordination board); `COMMAND.md` (Command Center's command file)".

## Ruling 3: stale gate/status banners removed (each banner plus the blank line after it)
- **mesh/roles.md:8:** "> **Status: published — operating model aligned**"
- **mesh/roles/command-center.md:8:** "> **Status: published — authority wording aligned**"
- **Other touched pages:**
  - mesh/roles/gitbook-moderator.md:8 ("published … 98fa6c7" banner)
  - mesh/roles/pen-tone-guide.md:1 (same banner; this page has no front matter, so none was added)
  - The six GB-004–014 banners, listed under ruling 5.
  - The six GB-004–014 body `**Status:** REPORTED — … Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub.` lines, also stale gate/status banners:
    - who-tessera-is:13
    - board-world-chamber:13
    - honesty-banner:13
    - pen-ability-set-framing:12 ("draft for GitBook — not shippable…")
    - pen-gate-refuse-companion:13 → now :11
    - refuse-and-offer:13 → now :11
  - On pen-gate-refuse-companion and refuse-and-offer, the non-status rule sentences were kept as plain lines ("Must match tone guide / refuse-and-offer IDs. No new refuse categories without TESSERA." and "Rule IDs must match pen-gate when that branch lands.").
- After GB-026, none of the 23 touched files has a `> **Status` banner.

## Ruling 4: moderator-handoff Approve row
- **review/moderator-handoff.md:38:** "…no with notes holds the items he names; **revise returns the named items for the stated change**; a yes never carries over…". Father's options now read yes/no/revise, in flow.md's wording.

## Ruling 5: older flags
- **GB-004–014 pages.** Front matter `status: approved` → `status: published`. Note "Status: Ready — awaiting Father GitHub push (…)" → "Published 2026-10-05 (commit 8010626 → REV 2: full SHA 801062641f30d2acf45dbea4748323f20c5e30d8); Father Yes 2026-10-05; testers WAIVED / not checked". The body banner and the body Status line were removed (see ruling 3). Pages and lines:
  - mesh/roles/who-tessera-is.md:2–3, banner :8 (GB-007)
  - mesh/roles/pen-ability-set-framing.md:2–3, :8 (GB-006)
  - mesh/roles/refuse-and-offer.md:2–3, :8 (GB-008)
  - mesh/roles/board-world-chamber.md:2–3, :8 (GB-009)
  - mesh/roles/pen-gate-refuse-companion.md:2–3, :8 (GB-011)
  - mesh/roles/honesty-banner.md:2–3, :8 (GB-012)
  - Already `published` with no banner on ecd9022, so unchanged: open-helper-agent-2 (GB-004), build (GB-010), mesh-lane-map (GB-013/014). GB-005 was a delta on tessera-pen / pen-tone-guide.
  - 8010626 = "Publish Ready GitBook batches 003–009 (GB-004 through GB-014)", 8:25 AM CT.
- **mesh/roles/gitbook-moderator.md:**
  - :15 (was :17): "approve, reject, or block" → "approve, reject, or changes needed".
  - :27 (was :29): Handoffs row "Blocked | … until unblocked or resubmitted" → "Changes needed | … until fixed and resubmitted per Moderator note" (moderator-handoff wording).
- **mesh/roles/who-tessera-is.md:41** (was :45): CC row "…; does not push" → "…; pushes only the Replit app set (privately, after all four gates and Father's yes); never pushes GitBook or TESSERA".
- **mesh/roles/pen-tone-guide.md:**
  - :36 (was :38): item 6 "GitBook draft → Moderator → digest → Father yes → private Replit" → "GitBook draft → Cordnation → Moderator → Tessera → Security → CI/Build → Ready → Command Center digest → Father yes/no/revise → Tessera pushes the approved package (PR, Build verifies, Tessera merges), or Father pushes himself. Replit is never a GitBook path."
  - :66 (was :68): the Hand-off line, also a stale mesh path, now lists the four gates.
- **history/coordination/AGENT-TRAINING-AUTHENTICITY.md:**
  - :18: Pen bullet → "Pen is Tessera's own writing voice (her editorial layer), not a separate agent, lane, or gate … **Tessera**, not Pen, assigns work."
  - :41: Module 3 → "Tessera assigns one task at a time…".
  - :75: audit row "Pen coordination is visible" → "Tessera's assignments are visible".
- **README.md:2:** `status: staged` → `status: published`.

## Ruling 6: Father's 3:59 PM CT rule wherever the push step is described
Rule text used: after Father's yes, **Tessera** pushes the approved GitBook packages. She opens a PR, Build verifies it, then Tessera merges and posts on Gitbook issue #2. Father may still push himself. Every Command Center "only push = private Replit app set" statement is kept unchanged.
- **mesh/TESSERA-GITBOOK-OPERATING-MODE.md:**
  - :17 Tessera row: adds the push/merge duty, bounded to what Father's yes lists
  - :23 Build row: verifies Tessera's push PR
  - :25 Father row: "Final bulk approval; may still push approved Gitbook changes himself"
  - :43: step 11 (full rule, with the issue #2 link and "Father's rule, 3:59 PM CT")
  - :44: step 12 "Origin/main merge" → "Origin merge (`collin-keane/Tessera`)"
- **mesh/flow.md:**
  - :10: canonical rule blockquote
  - :14: end-to-end flow
  - :36: mermaid H node
  - :38: merge node relabelled "Origin merge"
  - :54: Push authority (1)
  - :59: Merge authority adds the Gitbook package PR merge
  - :75: Tessera bullet
  - :79: Build bullet
- **mesh/roles.md:**
  - :3: front-matter note
  - :29: docs-track heading and push step
- **mesh/roles/command-center.md:**
  - :3: note
  - :31: Does not do
  - :42: Replit boundary
  - :46: Replit app set push section
- **mesh/roles/mesh-lane-map.md:**
  - :3: note
  - :29: push row
  - :50: publish path step 11
  - :56: Replit app set section
- **mesh/roles/open-helper-agent-2.md:20**
- **mesh/roles/build.md:**
  - :15: new Owns bullet, "Verify Tessera's PR for each approved GitBook package before she merges it."
  - :18: Does-not-do text
- **mesh/roles/grok-bot.md:18, :23**
- **mesh/roles/gitbook-cordnation.md:35**
- **intake/how-to-submit.md:27**
- **intake/status-definitions.md:28** ("merge requires" → "an Origin merge requires")
- **review/moderator-handoff.md:**
  - :38: Approve row (push step, and "Merge only…" → "Origin merge only…")
  - :46: Out of scope, docs push
  - :48: Out of scope, Merges

## Verification (see VERIFY-APPLY.txt and apply/)
- **Solo GB-026 on clean ecd9022:** rc=1. Five files fail: how-to-submit, operating-mode, flow, roles, moderator-handoff. All five need GB-022 text.
- **Stack check and apply:** 022 → 024 → 025 → 023 → 026 all rc=0.
  - Tree after GB-023 = the drafting base (814dd7a1).
  - Final tree 4983fe6e = the drafted tree.
  - Reverse-check of GB-026 on the stacked tree: rc=0.
- **Ordering:** GB-026 also checks clean (rc=0) on 022 + 024 + 025 without GB-023, so it has no textual dependency on GB-023. It is ordered after GB-023 by instruction.
- **Verification base:** the 10 extra files GB-026 touches were fetched read-only at ecd9022 and blob-verified: README, AGENT-TRAINING-AUTHENTICITY, gitbook-moderator, pen-tone-guide, who-tessera-is, board-world-chamber, honesty-banner, pen-ability-set-framing, pen-gate-refuse-companion, refuse-and-offer.

## Ambiguities / flags for Tessera (not resolved silently)
1. **Merge authority.** RESOLVED in rev 2 by Tessera's 16:29 merge wording (see above). Original rev-1 note: I read Father's yes as also authorizing Tessera's merge of the Gitbook package PR, so it is no longer a separate `merge` word. To keep that consistent, "Origin/main merge" (operating mode step 12), "merge requires" (status-definitions) and "Merge only on Father's explicit `merge`" (moderator-handoff) now say **Origin** merge. Pages still saying "merges to main need Father's word `merge`" were left alone (see 3).
2. **Who "Tessera" is.** "Tessera Grok bot / Command Center … never auto-pushes / cannot publish or merge" (operating mode CC row; command-center.md:42) sits next to "Tessera (admin) pushes". These are different actors; wording left as-is. Tessera may want "Tessera (admin)" spelled out.
3. **Untouched lines that may now read stale against the rule:**
   - who-tessera-is.md:30 "Not a lane that merges to main without Father's word `merge`"
   - who-tessera-is.md Not done: "…sealed on the Ready → GitHub path", "…before final push"
   - board-world-chamber.md:45 "**Waiting on:** Father's GitHub push of this Ready pack (GitBook→GitHub via his connection). No Replit." This is a product desk-note state, and Tessera should say what the Board now waits on.
   - mesh-lane-map.md heading "Delivery sync ≠ Father push" and "not Father's GitHub push"
   - mesh-lane-map.md:52 "Origin main still needs Father's word `merge`" (fine if Origin-only)
   - grok-bot "No merge without Tessera's go and Father's final digest yes" (consistent)
4. **Pen "does not push or merge".** This text (tessera-pen.md, flow.md Pen bullet, operating-mode Pen row, pen-tone-guide Hand-off) is kept. It is the voice, not the admin act, but readers may find it confusing now that Tessera pushes.
5. **yes/no/revise is not yet everywhere.** These lines on touched pages still say "yes/no" without revise; no ruling covered them, so they were not edited:
   - mesh-lane-map.md:49 step 10 and :62 Father digest approval
   - who-tessera-is "Father | Orders, yes/no, merge"
   - board-world-chamber "says yes/no / merge", Quick read "yes/no; merge"
6. **gitbook-cordnation.md.** Line 22 "Moderation (approve / reject / block)" and line 15's `blocked` intake status were not in a ruling, so they were left. Line 22 matches the old Moderator wording.
7. **gitbook-moderator.md Handoffs "Approved → Eligible for Command Center digest".** This skips the Tessera/Security/CI gates. Left as-is (not ruled).
8. **Front-matter notes on GB-004–014 pages.** These were rewritten to "Published 2026-10-05 (commit 8010626)…" so the front matter no longer contradicts `status: published`. Ruling 5 named only the status field and the banner.
9. **Body Status lines.** The GB-004–014 body `**Status:** REPORTED — … awaiting Father GitHub push` lines were treated as stale gate/status banners and removed. Substantive rule sentences on two pages were kept. If Tessera wanted only the blockquote banners removed, drop those 6 hunks.
10. **pen-tone-guide.md has no front matter.** None was added.
11. **pen-tone-guide.md:13 "Speak as the instrument … not as Tessera herself"** may conflict with the "Pen is Tessera's writing voice" canon. Not ruled; left.
12. **AGENT-TRAINING-AUTHENTICITY.md "Applies to: … Tessera, Pen, …"** still lists Pen like an agent. Left (minimal).
13. RESOLVED in rev 2 (the link was removed; f71e00a0 emptied the file). Original rev-1 note: **history/coordination/command-center.md (COMMAND.md's merged copy) is 0 bytes on ecd9022.** The tessera-pen.md:52 link resolves to an empty file. The duplicate ledger says it matched COMMAND.md (sha256 4fd16763…), which is not the empty hash, so the content may have been lost in the merge. Flag for Tessera.
14. **README.md body** still says "The staged consolidation currently preserves all source repositories; it has not deleted any repository." That is stale, since tessera-coordination was deleted. Not ruled; left.
15. **Untouched pages keeping the "published … 98fa6c7" blockquote banner:** tessera.md, mesh-cloud, github-scraper, open-helper-agent, recursive-learning-sponge, tessera-brain-consciousness. Ruling 3 limited removal to pages touched here; a later sweep could remove them.

## Rev 2 observations (not edited; scope fixed; handled in GB-027, see GB-027/NOTES.md)
- **Wording still tied to the word `merge` (pre-existing; does not suggest Gitbook skips Father):**
  - operating-mode:25, Father row authority: "Origin merge requires separate `merge`"
  - flow.md:10 "A separate explicit `merge` is still required for Origin merges"
  - flow.md:14 "Father separately says `merge` for an Origin merge"
  - roles.md:29 "Father separately authorizes an Origin merge with `merge`"
  - command-center.md:25 "merges awaiting Father's `merge`" and :34
  - build.md:20
  - mesh-lane-map.md:52, :66
  - pen-tone-guide:3, :71
  - who-tessera-is:30

  These sit alongside the new "explicit yes" wording for Origin/TESSERA. Tessera may want to say whether Origin still needs the literal word `merge` or just Father's explicit yes.
- **"Tessera's bulk update":** the Grok bot / Command Center prepares the bulk digest (operating mode). I used the phrase as ruled.
