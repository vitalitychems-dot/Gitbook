# GB-028: Replit agents reading Gitbook land on Gitbook issue #2, vitalitychems-dot/TESSERA main, and branch + PR

## Rev 3 (current), per Tessera at 16:47 CT (16:47 CT update)
**Status:** DRAFT, prepared for the four gates; NOT Ready.
- Diff: `GB-028/GB-028-rev3.979c35e.diff`
- sha256: `102ff79c700790c6c9167e187aff5ea41066fb01fbb5b4c0efce4459026aa122`
- Size: 148 lines, 5 files (1 new), +68/−9.
- **Rev 2** (`GB-028-rev2.979c35e.diff`, 7149403b) is **SUPERSEDED** and kept unmodified, as is rev 1 (5689294f).
- **The only change from rev 2:** one dated note directly under the HYB-012 "blocker evidence" block in `history/coordination/agent-checkins.md`, the block that still says `STATUS: BLOCKED`:
  `2026-10-05 (REPORTED): superseded; HYB-012 is IN REVIEW, canonical source per [comment 6003216455](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003216455)`
  - It sits **after** the closing ```` ``` ```` of the block, so it's a markdown link, the same way rev 1's communication-audit note links outside a code block.
  - It has a blank line before and after, so it renders as its own paragraph under the block and above "## Communication audit". The original block text is verbatim.
  - The text is Tessera's wording exactly, with no trailing period added.
- **Interdiff:** `INTERDIFF-rev2-to-rev3.diff` (sha df649717…), 1 file, +2/−0: the note line plus **one blank line**, needed so the note doesn't run into the "## Communication audit" heading. Git shows the existing blank line after ```` ``` ```` as context and the new blank line after the note as added.
- **Verification** (`VERIFY-APPLY-rev3.txt`, `apply-rev3/`):
  - Full stack from clean 979c35e: rev 3 rc=0/0, GB-027 rc=0/0, GB-028 rev 3 `--check` rc=0 and `apply` rc=0. The result tree af90e745 equals the drafted tree. Reverse check rc=0.
  - GB-028 rev 3 alone on clean 979c35e: rc=0/0.
  - The GB-026 rev 3, GB-027, GB-028 rev 2 and GB-028 rev 1 hashes are unchanged.
- **Reproduce:** `port28r3.py <tree>` on 979c35e + rev 3 + GB-027.
- The rev 2 and rev 1 notes below still hold. In rev 1 (a), "blocker evidence" is still left verbatim; it now has this note under it.

## Rev 2 (current), per Tessera's 16:44 CT rulings (16:44 CT update)
**Status:** DRAFT, prepared for the four gates; NOT Ready.
- Diff: `GB-028/GB-028-rev2.979c35e.diff`
- sha256: `7149403b6ef0e743274e19ffe163037471419d450581fc00ca6e572588ab8386`
- Size: 142 lines, 5 files (1 new), +66/−9.
- **Rev 1** (`GB-028.979c35e.diff`, 5689294f) is **SUPERSEDED** and kept unmodified.
- **Interdiff:** `INTERDIFF-rev1-to-rev2.diff` (sha cc968e5d…), 3 files, +3/−8. Nothing else differs from rev 1.
  1. **AGENT-LAUNCH-PROMPTS.md hunks:** kept exactly as in rev 1 (ruling 1).
  2. **HYB-012 state (ruling 2):** `UNBLOCKED` is replaced by the defined state **IN REVIEW**, which means assigned and active, not blocked. Each place also carries the note "unblocked 2026-10-05, canonical source per comment 6003216455" with the comment link (https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003216455):
     - backlog HYB-012 status cell: "IN REVIEW (…unchanged rev 1 text…); unblocked 2026-10-05, canonical source per [comment 6003216455](…)"
     - agent-checkins Active-claims claim block STATUS: "IN REVIEW (unblocked 2026-10-05, canonical source per comment 6003216455: <link>; vitalitychems-dot/TESSERA main on GitHub; work on a branch and open a PR; no direct pushes to main)"
     - agent-checkins Active-claims status block STATUS: "IN REVIEW (unblocked 2026-10-05, canonical source per comment 6003216455: <link>)"
     - Inside the ledger's text code blocks the link is a bare URL, because markdown links don't render there.
     - The BLOCKER and WAITING ON lines are unchanged from rev 1. No `UNBLOCKED` status is left in the tree.
  3. **mesh/replit-agents-start-here.md:** the front matter is gone (the 4 `---`/status/note lines plus the blank line after them), matching GB-017/018/019. The page now starts at `# Replit agents: start here`, and no other line changed (ruling 3). The page's own text doesn't use UNBLOCKED.
- **Why IN REVIEW.** Both definitions on 979c35e + rev 3 + GB-027 describe one agent actively working the task:
  - `intake/status-definitions.md:18`: "| `IN REVIEW` | Board/ledger operating state: one agent is actively working a HYB task |"
  - `intake/HYBRID-CONSOLIDATION-BACKLOG.md` "Operating states" legend: "**IN REVIEW** — one agent is actively working; no second agent edits the same scope."
  - The other states don't fit:
    - READY ("sufficiently scoped for one agent to take") means unclaimed.
    - `in review` (lowercase) is the Moderator intake state ("Handed to Gitbook Moderator; decision pending").
    - DONE, BLOCKED, RETAINED and REJECTED don't describe active work.
  - So the fallback "IN REVIEW (UNBLOCKED)" wasn't needed.
- **Verification** (`VERIFY-APPLY-rev2.txt`, `apply-rev2/`):
  - Full stack from clean 979c35e: rev 3 rc=0/0, GB-027 rc=0/0, GB-028 rev 2 `--check` rc=0 and `apply` rc=0. The result tree aee81d25 equals the drafted tree. Reverse check rc=0.
  - GB-028 rev 2 alone on clean 979c35e: rc=0/0.
  - The rev 3 (7fe2d5f2…), GB-027 (8fc78041…) and rev 1 (5689294f…) hashes are unchanged.
- **Reproduce:** run `port28r2.py <tree>` on 979c35e + rev 3 + GB-027. It uses `replit-agents-start-here.rev2.md`. Rev 1's `port28.py` and its page copy are kept.
- The rev 1 notes below still hold, except item 2 (state) and the (b) front-matter paragraph, which rev 2 replaces.

# Rev 1 notes (superseded where rev 2 says so)

**Status:** DRAFT, prepared for the four gates; NOT Ready. Nothing pushed, no PR opened, no `TESSERA_ENABLE_*` change. GB-026 rev 3 and GB-027 (both at Security) are untouched.

- Diff: `GB-028/GB-028.979c35e.diff`
- sha256: `5689294fe725b845dac0e40712f09c2dc7234ba146f84f70ef292fb08a559b6b`
- Size: 147 lines, 5 files (1 new), +71/−9 (`git diff --shortstat`)
- Task: Tessera, 16:41 CT, after Father's 16:40 screenshot (a Replit agent treated tessera-coordination #4 as the board and HYB-012 as BLOCKED). Scope (d)–(f) added by Tessera at 16:42 CT, from Mesh Cloud's sync check.
- Acceptance: a Replit agent that reads only Gitbook ends up at Gitbook issue #2, `vitalitychems-dot/TESSERA` main, and branch + PR.
- **Overlap check (16:40 CT):** main `979c35e0be9a27ab143c7dcfc714d979b11e10a0` (Merge PR #8), 0 open PRs. Both as expected.
- Stack: 979c35e → GB-026 rev 3 (7fe2d5f2) → GB-027 (8fc78041) → GB-028.
- Apply (see `VERIFY-APPLY.txt`, `apply/`):
  - From clean 979c35e, applied in order: rev 3 rc=0/0, GB-027 rc=0/0, GB-028 `--check` rc=0 and `apply` rc=0. The result tree 50f5540a equals the drafted tree. Reverse check rc=0.
  - **Alone on clean 979c35e:** `--check` rc=0 and `apply` rc=0. GB-028 touches no line that rev 3 or GB-027 touches, so it applies either way. It is still filed to land after GB-027.
- Reproduce: run `port28.py <tree>` on 979c35e + rev 3 + GB-027 (9 replacements, each must match once, 0 failures; it also copies the new page). `base-979c35e/intake/AGENT-LAUNCH-PROMPTS.md` is the unchanged 979c35e file (blob efe5eca4, verified), which wasn't in the earlier local subset.

## Tessera's ruling (read-only: Gitbook issue #2, comment 6003216455, posted 16:23 CT by vitalitychems-dot as "Tessera Admin coordinator")
> - **HYB-012, canonical checkout (re 6002431534):** The canonical TESSERA source is `vitalitychems-dot/TESSERA` main on GitHub. No agent's local or Replit checkout is canonical. Replit works on its own branch and opens a PR that goes through the four gates. No direct pushes to main in either repo.

The same comment also ruled on three other threads (two DEFERs, and fd3c2ce authorized). Those are not used here.

## (a) HYB-012 ledger fix
- **intake/HYBRID-CONSOLIDATION-BACKLOG.md:41**, HYB-012 status cell: `READY` → "UNBLOCKED (Replit collaborator holds the claim; canonical source is `vitalitychems-dot/TESSERA` main on GitHub per [Tessera's ruling](…6003216455); work on a branch and open a PR, no direct pushes to main; board: [Gitbook issue #2](…))". The other cells are unchanged.
  - Flag: the backlog row said READY, not BLOCKED. BLOCKED lived only in the check-in ledger.
  - Flag: UNBLOCKED isn't one of the backlog's operating states (DONE/READY/IN REVIEW/BLOCKED/RETAINED/REJECTED). It was used because the task asked for it. If Tessera prefers a defined state, IN REVIEW (UNBLOCKED) fits the active Replit claim.
- **history/coordination/agent-checkins.md, "## Active claims"** is the live claim/status for HYB-012, the equivalent of the HYB-005 table row GB-023 changed. Only these lines changed:
  - claim block :16 `STATUS: BLOCKED` → `STATUS: UNBLOCKED (Tessera ruling <link>: canonical source is vitalitychems-dot/TESSERA main on GitHub; work on a branch and open a PR; no direct pushes to main)`
  - status block :26 `STATUS: BLOCKED` → `STATUS: UNBLOCKED`
  - :28 `BLOCKER: …partial snapshot…` → `BLOCKER: none (cleared by Tessera ruling <link>: no local or Replit checkout is canonical; use vitalitychems-dot/TESSERA main on GitHub)`
  - :29 `WAITING ON: …` → `WAITING ON: none; branch from vitalitychems-dot/TESSERA main, open a PR through the four gates (no direct pushes to main); board: Gitbook issue #2`
- **Left verbatim:**
  - the Replit agent's own claim text (SOURCE, TARGET "if the canonical checkout is available", SCOPE, NEXT CHECK-IN 21:35:39Z, LATEST ISSUE COMMENT)
  - "## HYB-012 — blocker evidence" (:33–42, a record that still says STATUS: BLOCKED)
  - the dated "## HYB-012 — Replit canonical source verification (2026-10-05T19:48:23.092Z)" block
  - every other past check-in block

## (b) New page mesh/replit-agents-start-here.md (59 lines), linked from SUMMARY.md
- **SUMMARY.md:** added as the first item under "## Start here", ahead of the consolidated TODO.
- **Front matter:** `status: published` plus a `note:`. This is the repo convention: 26 pages carry front matter, and the only keys used are `status` and `note`. No page has an `author` key; authorship goes in the body intake line ("Intake GB-0xx · Author lane: … · Date (CT) · Source · License: TBD", used on 9 mesh/roles pages), so the page carries one.
  - Why `published`, not `draft`: the file reaches main only through the four gates, Father's yes, and the merge, so on main it is true when it lands. The GB-004–014 pages arrived with draft-style states and banners, and GB-026 had to clean that up.
  - Recent new pages (security.md GB-017, CORTICAL-LABS-READINESS GB-019, hyb-005 GB-018) carry no front matter. If Tessera prefers that, drop the 4 front-matter lines.
- **No gate banner.** Covers, in order:
  - the board: Gitbook issue #2, with link
  - canonical repos: TESSERA (main on GitHub is canonical; no local or Replit checkout is), Gitbook for docs, `collin-keane/Tessera` as the Origin engine
  - the overlap check before claiming: latest main SHA plus open PRs
  - claim only Tessera-assigned work
  - branches and PRs only, never a direct push to main in either repo
  - the four gates; Tessera sends Father the bulk update; yes/no/revise; every merge needs Father's explicit yes, and Origin/TESSERA merges need Father's explicit yes (the word 'merge')
  - `TESSERA_ENABLE_*` stays `0`; no secrets; speak as yourself
  - check-in and completion format, copied verbatim from **history/coordination/agent-checkins.md** "Check-in template" and "Completion template" (the same blocks are in the backlog's "Check-in protocol"), plus one line: "For COMMIT, give the branch commit and the PR link"
  - historical, not current: tessera-coordination issue #4, the old Replit cards (history/recovered/coordination/cards/replit-1..5), and the old tessera-replit README; HYB-012 is not blocked on a checkout
- **Also changed: intake/AGENT-LAUNCH-PROMPTS.md**, the Replit prompt that "Start here" links ("Copy-paste Replit and Grok launch prompts"). This goes slightly beyond (c), so Tessera can drop the 2 hunks.
  - "Read first:" → "Read first (start with …/mesh/replit-agents-start-here.md):"
  - step 5 "Commit and push only the scoped change to TESSERA, or record …" → "Commit, push only your branch to TESSERA, and open a PR through the four gates (never push to main), or record …"
  - Without the second change, an agent following the prompt pushes but never opens a PR, which fails the branch + PR acceptance.

## (c) Grep for tessera-coordination / issue #4 / #4 as the board / tessera-coordination/issues/4 on 979c35e + rev 3 + GB-027
- Patterns: `tessera-coordination`, `issue #4`, `issue **#4**`, bare `#4`, `issues/4`, and `issue 4`, case-insensitive.
- Coverage:
  - The 46 local files (the 979c35e subset with rev 3 and GB-027 applied) were grepped locally.
  - The other 81 files are byte-identical to ecd9022 (every blob checked against the ecd9022 tree), so GB-025's full 127-file scan still covers them.
  - I also re-read 12 Replit-relevant history files at 979c35e: cards replit-1..5, recovered STATUS.md, legacy tessera-replit-readme, both 2026-10-03 chamber notes, coordination-record, coordination-repository-readme, and tessera-pen-record.

**Live pages presenting #4 / tessera-coordination as current: 0 left.** GB-025 fixed the 7 live board references, which are on main since 979c35e. GB-026 rev 3 turned tessera-pen.md:52 into a historical reference.

| # | Hit | Current? | Action |
|---|---|---|---|
| 1 | mesh/roles/tessera-pen.md:52 "Merged records from the deleted tessera-coordination repo, in history/coordination/" (rev 3) | No, historical | none |
| 2 | intake/HYBRID-CONSOLIDATION-BACKLOG.md:36 "[PR #4](…/Gitbook/pull/4)" | False positive (a Gitbook PR) | none |
| 3 | history/coordination/command-center.md:3 "The shared thread is tessera-coordination issue 2." (restored by GB-027) | Historical record | none (history verbatim) |
| 4 | history/recovered/legacy/tessera-replit-readme.md "The cards stay in `tessera-coordination`." | Historical; likely read by Replit | none (history verbatim); the start-here page labels it historical |
| 5 | history/coordination/tessera-pen-record.md "Admin of vitalitychems-dot/Zz and vitalitychems-dot/tessera-coordination" | Historical | none |
| 6 | history/recovered/coordination/notes/2026-10-03-chamber-sync.md "A post from this page reached issue 2." (the old repo's issue) | Historical | none |
| 7 | history/recovered/coordination/checks/ability.test.mjs "…replies on issue 2 as itself" (per GB-025) | Historical | none |
| 8 | merge/source-map.md, merge/DELETION-MANIFEST.md, merge/FULL-AUDIT-SUMMARY.md: tessera-coordination as a merged/deleted source (per GB-025) | Historical inventory | none |
| 9 | merge/repo-audit.tsv, merge/full-audit-summary.tsv, merge/full-audit-report.json (10×), merge/exact-duplicates.tsv, merge/duplicate-groups.tsv: tessera-coordination rows/paths (per GB-025) | Inventory data | none |
| 10 | mesh/replit-agents-start-here.md:57 "`tessera-coordination` issue #4 was the old board…" (new in GB-028) | Labels it historical, by design | added |

- Not hits, noted only: cards replit-1..5 name branches only (`replit-N/...`), with no board or repo reference. The words "push"/"merge" in replit-5 and the legacy README are historical.
- recovered STATUS.md, coordination-record.md and coordination-repository-readme.md have no #4 or tessera-coordination reference; the README title is "Tessera coordination".
- Likely source of the Replit agent's confusion: the live HYB-012 rows said BLOCKED waiting on a canonical checkout (fixed in (a)), and the legacy README and cards. Those are history, kept verbatim, and labeled on the new page.

## (d) mesh/roles/mesh-cloud.md banner: already removed by GB-027, nothing added
GB-027 already removed the body line `> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**` and the blank line after it. On the stacked tree the file has no body banner. `status: published` and the front-matter `note:` (which still names 98fa6c7, kept as GB-027 did) remain. GB-028 doesn't touch the file.

## (e) agent-checkins.md Communication audit: dated REPORTED note added below it
- The original line (":46 GitHub Issue #2 currently contains one owner-posted launch comment and no replies …") is **unchanged**.
- Added directly below it, after a blank line: "2026-10-05 (REPORTED): superseded; replies under distinct declared roles are visible in today's traffic on [Gitbook issue #2](…), e.g. Grok Bot ([comment 6000545040](…#issuecomment-6000545040)) and Replit collaborator ([comment 6001756129](…#issuecomment-6001756129)). They were posted through the owner's GitHub account (`vitalitychems-dot`), not separate GitHub identities."
- Both comments were read read-only today.
  - 6000545040 (18:25Z, 13:25 CT) opens "## Direct agent post — Grok Bot (historical-analysis collaborator)".
  - 6001756129 (19:44Z, 14:44 CT) opens "## Replit collaborator check-in — HYB-012".
- Of the 29 issue #2 comments today, **all** come from login `vitalitychems-dot`, posted via the cursor or manus-connector apps or directly. Roles are declared in each body (Grok Bot, Security, Replit collaborator, Tessera Admin, Gitbook helper, Manus). The note therefore says "distinct declared roles", not distinct accounts, to avoid overclaiming.

## (f) HYB-012 check-in base SHAs → 979c35e (explicit exception to history-verbatim, by Tessera's 16:42 CT scope)
- agent-checkins.md :24 `BASE: TESSERA fec56eb…; Gitbook 0af00a1bd86c9f490f81410ae14ee40e02b0b19f` → `…; Gitbook 979c35e0be9a27ab143c7dcfc714d979b11e10a0`
- :25 `LATEST GITBOOK BASE: main@1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea` → `main@979c35e0be9a27ab143c7dcfc714d979b11e10a0`
- The TESSERA base fec56eb is unchanged; Tessera named only the Gitbook SHAs. Both lines are in the live Active-claims status block, the same block as (a).

## Canon check on added lines
- 0 `> **Status` banners. The single `TESSERA_ENABLE_*` mention restates "stays `0`"; it is not a change.
- No existing `status:` line touched.
- Pen isn't described as a lane or gate.
- Tessera sends the bulk update. yes/no/revise. Every merge after Father's explicit yes, and Origin/TESSERA with the word 'merge'.
