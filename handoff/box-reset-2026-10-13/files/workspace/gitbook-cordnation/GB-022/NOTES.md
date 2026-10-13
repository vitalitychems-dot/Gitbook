# GB-022: later delta package (DRAFT, held)

- **State:** draft **v3** (Tessera 15:49 rulings applied at 15:50 CT; v2 had the 15:42 rulings). Held; not sent to any gate; not in READY.md or the FROZEN file.
- **What it waits on (Tessera 15:46):** f4b2c41 + GB-017, GB-018 and GB-016 rev 3.2. After those land it gets rebased onto the new main. Until then the main diff stays on the 1e3 + 7-package base below, as Tessera directed.
- **Task:** Tessera, 15:32 CT.
- **Overlap check (~15:33 CT):** Gitbook main is `1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea`, 0 open PRs.
- **Base:** a 1e3bb50 snapshot with the 7 frozen Ready packages applied in push order: GB-015 → GB-017 → GB-018 → GB-019 → GB-021 → GB-020 (`GB-020/GB-020.diff`, 2e3b5400) → GB-016 rev 3.1 (af18bc3b).
  - All 7 apply with 0 offsets, and hashes match FROZEN-SHA256-1e3.txt.
  - GB-022 also touches 3 files outside the 7 packages: `intake/how-to-submit.md`, `intake/agent-submission-format.md` and `intake/log.md`. Their blobs were rebuilt from GitHub at 1e3bb50 and checked with `git hash-object` (7d307d0, 807144b, a21f851).
- **Diff:** `GB-022.diff` v3, 309 lines, 15 files, +51/−47, sha256 `293d264f…` (in SHA256.txt).
  - v2 (305 lines, `5d2a0dd2…`) is kept as `GB-022.v2.diff`. The v2 → v3 interdiff is `INTERDIFF-v2-to-v3.diff`; it moves one tessera-pen.md paragraph.
  - v1 (239 lines, 13 files, `d6cf6d39…`) is kept as `GB-022.v1.diff`.
  - The v1 → v2 interdiff is `INTERDIFF-v1-to-v2.diff`.
  - `base/` = the stacked base. `proposed/` = base + GB-022.
  - Diff format is the same as the GB-016 rev 3.1 diff (no index lines).

## Per-item table

| # | Item | Done / skipped | Reason | File(s) |
|---|---|---|---|---|
| 1 | Father's 3:10 PM overlap-check rule in flow.md + task template | **Done** (partly covered) | Rev 3.1 already has the overlap check in the flow.md pipeline sentence and diagram, but not as a standing rule. Added an "Overlap check" standing-rules row (before starting or claiming any work; record main SHA + open PRs in `OVERLAP CHECK`). Task templates: added an `OVERLAP CHECK` field to the general submission template, and changed the only existing `OVERLAP CHECK` template field (BC check-in) from "<none or linked BC task>" to name the main SHA and the open PRs checked. | mesh/flow.md; intake/agent-submission-format.md; brain-consciousness/AGENT-WORKPLAN.md |
| 2 | Restore "or treated as live" in the Pen paragraph | **Done** | GB-017 dropped it from tessera-pen.md when it rewrote the paragraph (1e3 had: "Nothing is pushed to private Replit or treated as live until Father says yes"). Now: "Nothing is pushed or treated as live until Father's final yes on the listed digest item." It was never in roles.md. | mesh/roles/tessera-pen.md |
| 3 | Link identity-line mentions to tessera-pen.md | **Done** (v2 per ruling 3) | Added a `### Tessera identity line` heading on tessera-pen.md. The bold "**Tessera identity line:**" label became the heading, and the definition text is unchanged. All mentions now link to `#tessera-identity-line`: flow.md, roles.md, mesh-lane-map.md and security.md use `tessera-pen.md#tessera-identity-line`, and the in-page mention in tessera-pen.md uses `#tessera-identity-line`. **v3 (Tessera 15:49):** the "When product intent is unclear…" paragraph was moved above the `### Tessera identity line` heading, so that section holds only identity-line content. Paragraph text is unchanged. | mesh/flow.md; mesh/roles.md; mesh/roles/mesh-lane-map.md; mesh/roles/security.md |
| 4 | flow.md push rule points to exception (3) | **Done** | Added to the canonical push rule: "The only other push is the Grok lane's feature-branch exception — see **Push authority (3)** below." | mesh/flow.md |
| 5 | Who sets BLOCKED | **Done** (v2 per ruling 1; the moderator-handoff.md change was approved by Tessera at 15:49) | BLOCKED row: "Owner or Tessera hold". **Who sets it:** only the task's assigned owner (in its own check-in, with the specific blocker) or Tessera (admin). Father can set any status. Gates, the Gitbook Moderator included, return items as `changes needed` and never set BLOCKED. Notes line: Moderator outcomes are approve / reject / changes-needed. moderator-handoff.md matches: the Decision list has **changes needed** instead of **block**, the checklist says "If changes needed", and the outcome row "Block → `blocked`" became "Changes needed → `changes needed` (the Moderator never sets BLOCKED)". | intake/status-definitions.md; review/moderator-handoff.md |
| 6 | SUMMARY nav for security.md | **Done** | GB-017 didn't add one. Added `[Security](mesh/roles/security.md)` under Roles after Grok Bot, matching the roles.md table order; the label matches the page title "# Security". | SUMMARY.md |
| 7 | Charter title + SUMMARY label | **Done** (v2 per ruling 2) | `brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md` is retitled `# Brain & SNN research charter`, with the matching SUMMARY label `[Brain & SNN research charter]`. Filename kept. The tessera-pen.md SUMMARY label change from v1 is kept. v1 note follows: | Chosen charter: `mesh/roles/tessera-pen.md`, the Pen charter (intake GB-001 "Pen charter"; the page says "Father may refine this charter"). Its title is already "# Tessera Pen (Tessera's writing voice)" after GB-017, but the SUMMARY label still said "Tessera Pen (provisional)", which contradicts "not a lane". The label now matches the title. The page title is unchanged because it's already current. `brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md` was checked: its title and label already match ("Tessera Pen research charter"), so it's unchanged. | SUMMARY.md |
| 8 | intake/log.md Reviewer / Check / Next action / Blocker columns; Ready as formal status | **Done** (columns) / **Skipped** (Ready). Ruling 6: the backfill of legacy cells and real SHAs is GB-023, later. GB-022 only adds the empty columns. | Added the 4 columns, empty for the 14 legacy rows, with an explanatory sentence and a link to Status definitions. `Ready` is already a formal status in status-definitions.md (GB-016), so nothing was added there. Since GB-022 touches log.md, the canon was applied: stale front matter `status: approved` became `status: published` (note reworded), and the gate banner "Status: approved … awaiting Father GitHub push of Ready batches 003–009" was removed. | intake/log.md |
| 9 | roles.md single-path sentence names both tracks | **Done** (partly covered) | Rev 3.1 only mentioned Replit items in a trailing clause. The paragraph now opens with **GitBook docs track** (the single canonical GitBook path; Father pushes), and the trailing clause is now **Replit app-set track** (Command Center private push; not a GitBook path): same four gates → CC marks Ready → own digest item → Father's yes → CC privately pushes only the app set. | mesh/roles.md |
| 10 | Digest rules: one item per push action listing its contents; order merges → docs → Replit → questions | **Done** | Rev 3.1 covered "each push its own numbered item" but not the item contents or the order. Added a "Digest format" paragraph to Command Center's Father digest approval section, and a matching sentence plus a link in flow.md's Digest items row. | mesh/roles/command-center.md; mesh/flow.md |
| 11 | Playbook Security row names the Security lane | **Done** | Escalate-to is now "Security lane + Moderator + human owner". | mesh/COLLABORATION-PLAYBOOK.md |
| 12 | how-to-submit.md: four gates + 30–45 min; keep 1e3 step 4 | **Done** (intro rewrite OK'd, ruling 5) | Step 2 now lists the four gates in order (Moderator → Tessera → Security → CI/Build) and links per-gate states. Step 3: Ready after all four gates, then its own numbered item in the bulk digest every 30–45 min (was "~30 min"). Step 4 is unchanged (1e3 wording kept verbatim). The intro line "or ask Command Center to push until…" contradicted canon (CC never pushes GitBook), so it now says CC never pushes GitBook and points to the Grok exception (3). The old 98fa6c7 gate banner was removed under the 15:04 ruling (confirmed 15:24); `status: published` front matter is kept. | intake/how-to-submit.md |

## File set (15)

SUMMARY.md, brain-consciousness/AGENT-WORKPLAN.md, brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md (v2), intake/agent-submission-format.md, intake/how-to-submit.md, intake/log.md, intake/status-definitions.md, mesh/COLLABORATION-PLAYBOOK.md, mesh/flow.md, mesh/roles.md, mesh/roles/command-center.md, mesh/roles/mesh-lane-map.md, mesh/roles/security.md, mesh/roles/tessera-pen.md, review/moderator-handoff.md (v2).

- **Stacks on the frozen 7, as expected (GB-022 lands after all of them):**
  - SUMMARY.md (017, 018)
  - TESSERA-PEN-RESEARCH-CHARTER.md (020, merged in f4b2c41)
  - moderator-handoff.md (016)
  - AGENT-WORKPLAN.md (020)
  - status-definitions.md (016)
  - COLLABORATION-PLAYBOOK.md (021)
  - flow.md (016, 017)
  - roles.md (016, 017)
  - command-center.md (016)
  - mesh-lane-map.md (016)
  - security.md (017)
  - tessera-pen.md (017)
- **Not in any other package:** agent-submission-format.md, how-to-submit.md, log.md.
- No other draft package touches these files.

## Canon checks

- No gate banners added.
- The only remaining `> **Status…**` blockquote in the stacked result is 1e3's Command Center banner, which is kept.
- 1e3's lane-map `**Status:** PUBLISHED…` line is untouched.
- Existing pages keep (or now carry) `status: published` front matter. No new pages.
- `git diff --check` is clean.
- TESSERA_ENABLE_* untouched. Nothing written to GitHub.

## Apply check

On a fresh 1e3bb50 snapshot, plus the 3 hash-verified intake blobs, applied in order: GB-015 → 017 → 018 → 019 → 021 → 020 → 016 rev 3.1 → **GB-022**.
- All 8 apply with rc=0, 0 offsets, 0 fuzz.
- The result for the 13 files is byte-identical to `proposed/`.

## Needs a Tessera call

1. **Item 5:** who may set BLOCKED (owner self-sets in its check-in, Tessera, or both?). The draft says both, plus the Moderator for review items.
2. **Item 7:** whether "the charter" means tessera-pen.md (as chosen) or the brain-consciousness research charter. If it means the research charter, give the new title.
3. **Item 3:** page-level links vs. adding a `## Tessera identity line` heading in tessera-pen.md so links can point to an anchor.
4. **Item 1:** should the playbook's handoff packet (TASK/IDENTITY/…/NEXT TASK) also get an `OVERLAP CHECK:` line? Not added (minimum edits).
5. **Item 12:** the intro-line rewrite (CC never pushes GitBook; Grok exception) is beyond the literal ask but removes a canon conflict.
6. **Item 8:** legacy log rows GB-004..GB-014 still show `approved`, and no rows exist for GB-015..GB-022. Left alone (out of scope); a later backfill is suggested.
7. **On rebase after Father pushes:** if Father's push lands the 7 packages unchanged, GB-022 should apply as-is. Any change on main to these 13 files needs a re-check.
- **v2 (15:49 CT):** same base and order, with GB-022 v2 (5d2a0dd2) last. All 8 apply with rc=0 and 0 offsets, and the result equals `proposed/` for all 15 files.

## Ruling 4: playbook handoff packet

Added one line after `BASE:` in the Required handoff packet: `OVERLAP CHECK: <Gitbook main SHA checked + open PRs checked (numbers or none)>`. File: mesh/COLLABORATION-PLAYBOOK.md, already in the set.

## Ruling 7: operating-mode sub-diff, `GB-022-operating-mode.f4b2c41.diff` (**HELD until Father answers which page is canonical**)

- **Base:** f4b2c41. The page is unchanged by PR #5: blob `90545f55` is the same at feaeb558 and f4b2c41, and the file is not in PR #5's file list. It does not exist on 1e3bb50.
- **Size (v2, Tessera 15:52 CT Q5 correction):** 52 lines, 1 file, +17/−14, sha256 `1d7f5e35927448ae4e16d5842c7d4a32e563a7f5e9ae569eb202d23ecf3d4a5b`.
  - v1 (50 lines, `f3a44208…`) is kept as `GB-022-operating-mode.f4b2c41.v1.diff`.
  - The diff-of-diffs is `INTERDIFF-operating-mode-v1-to-v2.txt`.
- **Copies:** `operating-mode/base-f4b2c41/` and `operating-mode/proposed-f4b2c41/`.
- **Apply checks (v2, 15:52 CT):** clean with 0 offsets on f4b2c41 (result equals `operating-mode/proposed-f4b2c41/`), on fd3c2ce, and on f4b2c41 + GB-017 + GB-018 + GB-016 rev 3.2. v1 checks:
  - Clean on f4b2c41 and on feaeb558.
  - Clean on f4b2c41 + GB-017 + GB-018 + GB-016 rev 3.2, which never touch this page.
- **Changes, roles table and sync cycle only (nothing else on the page):**
  - **Tessera Pen row (Tessera 15:42 #7 and 15:46 #3):** "Directs the work: frames goals, assigns one scoped task, protects coherence, and records decisions" → "Tessera's own writing voice — not a separate agent, not a lane, not a gate; needs no check-in". Boundary → "Does not assign tasks (Tessera does), push, merge, or approve for the owner". The page never had "Configured / live participation requires check-in" (that text was in roles.md and is fixed by GB-017 plus GB-016 rev 3.2); the canon "needs no check-in" is stated here anyway.
  - **Tessera row:** adds "assigns tasks; second review gate (after Moderator)"; "bypass the review gate" → "gates".
  - **Agents row:** "Must claim one task" → "Must run the overlap check, claim one task only after Tessera assigns it".
  - **Moderator row boundary:** "Approves eligibility for the digest; does not replace owner approval" → "First of four gates (Moderator → Tessera → Security → CI/Build); does not replace the other gates or owner approval".
  - **New Security row:** "Read-only security/privacy sweep (third gate, after Tessera) | Changes nothing; reports to Tessera".
  - **Build row:** adds "(CI/Build, fourth gate)".
  - **Sync cycle:** 11 steps → 13.
    - Step 1: claim → overlap check (main SHA + open PRs).
    - Step 2: "Pen assigns or confirms scope" → "Tessera assigns…; the agent claims it only after assignment".
    - New step 6: Tessera reviews product truth.
    - New step 7: Security sweeps read-only.
    - "Build" → "CI/Build".
    - "only eligible items" → "only items that cleared all four gates (Ready)".
    - Steps 10–13 are the old 8–11, verbatim.
- **Not changed:**
  - **Grok bot / CC row (v2):** Tessera corrected her Q5 ruling at 15:52 CT. The boundary now reads "May ask the owner for `yes`, `no`, or `revise`; never auto-pushes or auto-merges", matching the other pages. The digest-owner wording "Tessera Grok bot / Command Center" is kept, and nothing else changed. This supersedes the 15:49 "yes or no" ruling.
  - The Approval contract, Integrated skill loop and Status truth sections are also unchanged.
  - GB-022.diff v3 (`293d264f`) is unchanged by the sub-diff v2.
- **v3 (15:50 CT):** same base and order, with GB-022 v3 (293d264f) last. All 8 apply with rc=0 and 0 offsets, and the result equals `proposed/` for all 15 files.

## v4: rebased onto ecd9022 (2026-10-05 ~16:15 CT)

**File:** `GB-022-v4.ecd9022.diff`, sha256 `ae288a54…32a1d4`: 364 lines, 16 files, 24 hunks, +68/−61. One package containing v3 (`GB-022.diff` 293d264f, 22 hunks) plus the operating-mode sub-diff v2 (`GB-022-operating-mode.f4b2c41.diff` 1d7f5e35, 2 hunks). The sub-diff is no longer held, because Father's yes on GB-016 settled the four gates.
**Base:** ecd902211abd202711838219b28a1e1b39ae47c4. All 28 touched-file blobs match the real ecd9022 tree.

**Applied unchanged (11 files):** brain-consciousness/AGENT-WORKPLAN.md, TESSERA-PEN-RESEARCH-CHARTER.md, intake/agent-submission-format.md, how-to-submit.md, log.md, status-definitions.md, mesh/COLLABORATION-PLAYBOOK.md, mesh/roles/mesh-lane-map.md, security.md, tessera-pen.md, review/moderator-handoff.md. The operating-mode sub-diff also applies unchanged (blob 90545f55 is unchanged on ecd9022).

**Re-anchored (4 files).** Context moved on main; each added sentence is unchanged:
- `SUMMARY.md`: fd3c2ce added the roadmap nav line, and PR #5 added the operating-model nav line, so context and offsets changed. Same three edits.
- `mesh/flow.md`: GB-016 rev 3.2 on main replaced the "Canonical push rule" blockquote with the "Canonical approval rule" (yes/no/revise). The Push authority (3) sentence goes into the merged blockquote at the same position. In the Digest items row, the item-contents / digest-order sentence is inserted and main's **revise** clause is kept. The overlap-check row and identity link are unchanged.
- `mesh/roles.md`: see conflict 1 below. The identity-link hunk is unchanged, with re-anchored context.
- `mesh/roles/command-center.md`: the Digest format paragraph is inserted above main's approval paragraph, which keeps its **revise** sentence.

**Dropped hunks: none.** No v3 or sub-diff hunk is already satisfied by GB-016/017 on main. Before rebasing I grepped ecd9022 for each addition (OVERLAP CHECK template text, Push authority (3), tessera-identity-line, Security nav, Digest format/order, Brain & SNN label, GitBook docs track, "or treated as live", BLOCKED who-sets); none was present.

**Conflicts with merged GB-016/017 text.** Resolved by keeping main's wording and carrying only GB-022's net change. Nothing was silently reworded:
1. `mesh/roles.md` path sentence. The v3 hunk's −/+ lines were written against the older GB-016 path ("Gitbook / Cordnation intake → … → Father final yes/no → …"). Applied as written, it would have reverted GB-016 rev 3.2's merged "overlap check (main SHA + open PRs) → Tessera assigns … → Father responds `yes`, `no`, or `revise` → Father alone pushes the approved Gitbook changes …", breaking the yes/no/revise canon. v4 keeps the merged sentence verbatim and adds only GB-022's change: the **GitBook docs track** label at the front and the **Replit app-set track** sentence at the end.
2. `mesh/flow.md` blockquote and Digest row, and `command-center.md` approval paragraph. v3 context lacked **revise**; v4 keeps main's revise text (see above). No meaning change.

**Flags for Tessera, outside the GB-022 scope and not edited:**
- `mesh/roles.md:8` "> **Status: published — operating model aligned**" and `mesh/roles/command-center.md:8` "> **Status: published — authority wording aligned**" are status banners on main. GB-022 removes the banners only from how-to-submit.md and log.md.
- `review/moderator-handoff.md`, Approve row: "Father's bulk yes approves every listed item; no with notes holds the items he names". It does not mention **revise**.
