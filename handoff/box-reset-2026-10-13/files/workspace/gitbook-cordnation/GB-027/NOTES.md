# GB-027 — Tessera 16:34 CT ruling (Origin/TESSERA merge = the word 'merge'), GB-026 leftovers, command-center.md restore

**Status:** DRAFT, prepared for the four gates (Moderator → Tessera → Security → CI/Build); NOT Ready. Nothing pushed, no PR opened, no `TESSERA_ENABLE_*` change.

- Diff: `GB-027/GB-027.979c35e.diff`
- sha256: `8fc780410bef373aebf06f9c4ac6ba52a1f24e0569d4851d29d2b6d55a803121`
- Size: 488 lines, 22 files, +54/−61 (`git diff --shortstat`)
- Base: main `979c35e0be9a27ab143c7dcfc714d979b11e10a0` + **GB-026 rev 3** (`7fe2d5f2…`). GB-027 must land after rev 3.
- Apply: on 979c35e + rev 3, `--check` rc=0 and `apply` rc=0; result tree 40055667 equals the drafted tree; reverse-check rc=0. Alone on 979c35e it fails, rc=1, in 14 files (expected). See `VERIFY-APPLY.txt` and `apply/`.
- Reproduce: `port27.py <tree>` on 979c35e + rev 3. Every replacement must match exactly once (60 edits, 0 failures). `base-979c35e/` holds the seven unchanged 979c35e files the earlier local subset lacked; each blob was checked against the 979c35e tree.

## Item 1 — restore `history/coordination/command-center.md` (done)
- 979c35e has it as an empty file (blob e69de29b, 0 bytes).
- **Provenance:** wiped in f71e00a0 (Manus roster reconcile). Restored from blob 9916da0b186760f5fa09d5da672347485ec6a785 as read at 1d72e637 (the same blob was first added at eefbe2fd). It matches Security's `/workspace/security-gate/INV-2026-10-05-command-center-md-empty.md` and the duplicate-ledger sha256.
- **Verification:** the applied file has `git hash-object` = 9916da0b…, is 262 bytes, sha256 4fd167637095d521066cad7afdeaeca8676a836cc483c3d9add92fddc59f9202, and has no trailing newline. The diff carries "\ No newline at end of file", and `git apply` recreates the file byte for byte.
- The content is a historical record. It names tessera-coordination issue 2, the old board, and is kept verbatim. The live board is Gitbook issue #2.

## Item 3 — Tessera ruling 16:34 CT: Origin / TESSERA merges need Father's explicit yes (the word 'merge') — DONE
Moved from "pending ruling" to **done**. Every Origin/TESSERA merge line now says "Father's explicit yes (the word 'merge')". The Gitbook merge wording is unchanged from rev 2/rev 3: "Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed." It still appears 5 times, plus the short moderator-handoff form, and the same sentences sit on both sides of each hunk. Rev 3 itself is not changed.

New Origin sentence (rev 2/rev 3 form + the ruling): "Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes (the word 'merge') before anyone merges."

Done (line numbers on the GB-027 result tree):
- mesh/TESSERA-GITBOOK-OPERATING-MODE.md:25 Father row: "Origin merge requires separate `merge`" → "Origin and TESSERA merges need Father's explicit yes (the word 'merge')". Also adds `yes`/`no`/`revise`.
- operating-mode:44 step 12: Origin sentence (rev 3 sentence + the ruling)
- mesh/flow.md:10 rule: "A separate explicit `merge` is still required for Origin merges." → the new Origin sentence
- flow.md:14 flow: "Father separately says `merge` for an Origin merge (…)" → "Origin (…) and TESSERA merges need Father's explicit yes (the word 'merge') before anyone merges."
- flow.md:38 diagram node I: `I{"Origin / TESSERA merge:<br/>Father's explicit yes (the word 'merge')?"}`. The label is quoted so mermaid accepts the parentheses. It was not rendered here.
- flow.md:59 Merge authority row: Origin sentence
- mesh/roles.md:29 path: "Father separately authorizes an Origin merge with `merge`" → "Origin (…) and TESSERA merges need Father's explicit yes (the word 'merge')"
- roles.md:31: "Agents do not merge Origin (`collin-keane/Tessera`) or TESSERA without Father's explicit yes (the word 'merge')."
- mesh/roles/command-center.md:25 digest order: "(1) Origin / TESSERA merges awaiting Father's explicit yes (the word 'merge')"
- command-center.md:34 Does not do: "Merge anything (Tessera merges Gitbook PRs after Father's yes; Origin and TESSERA merges need Father's explicit yes, the word 'merge')"
- intake/status-definitions.md:28, intake/how-to-submit.md:27, review/moderator-handoff.md:38 Approve row: Origin sentence (rev 3 sentence + the ruling)
- review/moderator-handoff.md:48 Out-of-scope short form: "Origin / TESSERA: Father's explicit yes (the word 'merge') before anyone merges"
- mesh/roles/mesh-lane-map.md:52: "Origin main still needs Father’s word `merge`." → the new Origin sentence
- mesh-lane-map.md:66: "`collin-keane/Tessera` main stays put until Father's explicit yes (the word 'merge'). TESSERA merges need the same."
- mesh/roles/build.md:20: "Merge without Father's word 'merge'…" → "Merge anything (Tessera merges Gitbook PRs after Father's yes; Origin and TESSERA merges need Father's explicit yes, the word 'merge'), or push or publish before Father approves."
- mesh/roles/pen-tone-guide.md:3 and :71: "Father’s word `merge`" / "has not said `merge`" → "Father's explicit yes (the word 'merge')"
- mesh/roles/who-tessera-is.md:30: "Not a lane that merges without Father's explicit yes. Tessera merges Gitbook PRs after that yes; Origin and TESSERA merges need Father's explicit yes (the word 'merge')."
- who-tessera-is.md:37 and board-world-chamber.md:43, :62: "merge" → "the word 'merge' for Origin / TESSERA"

Not edited, because these lines restrict an action rather than state merge authority: tessera-pen.md:21 "Push or merge on GitHub / Origin / Replit" (Does not do), build.md:19 "…build or merge on Origin collin-keane/Tessera" (Does not do), mesh-lane-map.md:64 heading "## Origin merge", and :70 "Origin merge still gate". OHA2:20 "every merge needs Father's explicit yes on the listed item" is general, not Origin-specific, so it was left alone.

## Item 2 — leftovers (done, minimal)
- **who-tessera-is.md:30**: aligned to canon (above).
- **board-world-chamber.md:45**: "Waiting on: Father’s GitHub push of this Ready pack…" → "Waiting on: nothing for this page (published in 8010626). New docs follow the gated path: after Father's yes, Tessera pushes (Father may push himself). No Replit."
- **board-world-chamber.md:69**: "Father has not digest-approved this note" contradicted the front matter ("Father Yes 2026-10-05") → "Father's yes covered publishing this note, not the tabs' live state". This line was not in the brief, but it is the same staleness as :45.
- **revise added**: mesh-lane-map.md:49 step 10 and :62; who-tessera-is.md:37; board-world-chamber.md:43 and :62 (Quick read).
- **gitbook-cordnation.md:22**: "Moderation (approve / reject / block)" → "(approve / reject / changes needed)". Line 15's `blocked` intake status was **left**: it is a valid status when the task owner or Tessera sets it (status-definitions:19), and Cordnation only files it.
- **gitbook-moderator.md:25** Approved → "Goes to Tessera → Security → CI/Build; once all four gates clear, Gitbook / Cordnation stages it Ready for Tessera's bulk update to Father (Command Center feeds it)".
- **command-center.md:42**: "The Tessera Grok bot may prepare and deliver the digest, but it cannot publish or merge." → "The Tessera Grok bot / Command Center feeds Tessera's bulk update but does not send it, publish, or merge; Tessera sends it to Father and, after his yes, pushes and merges the approved Gitbook packages."
- **Banner removal on the six pages GB-026 doesn't touch**: tessera.md, mesh-cloud.md, github-scraper.md, open-helper-agent.md, recursive-learning-sponge.md, tessera-brain-consciousness.md. Each loses only the `> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**` line and the blank line after it. `status: published` and the front-matter `note:` are kept, and no front matter line changed.

## Stale CC-digest re-scan (canon: Tessera sends Father one bulk update every 30–45 min; Command Center feeds it)
**Fixed** (each line said or implied that CC/the Grok bot prepares, sends, or delivers the digest to Father):
- operating-mode.md:24 (CC row), :41 (step 9)
- flow.md:3 (front-matter note), :10 (rule), :14 (flow), :31 (diagram node F → "Tessera bulk update — CC feeds it"), :52 (CC row), :74 (lane bullet)
- roles.md:14 (table row), :29 (path), :31 ("coordinates and digests")
- command-center.md:3 (front-matter note), :14, :17 (Owns), :42
- mesh-lane-map.md:27 (table row), :36 (sync path), :48 (step 9)
- how-to-submit.md:26
- moderator-handoff.md:38 (Approve row), :44 (Out of scope)
- gitbook-cordnation.md:35 (Handoffs)
- gitbook-moderator.md:25 (Handoffs)
- who-tessera-is.md:41 (CC row)
- board-world-chamber.md:43 ("Command Center digest path")
- pen-tone-guide.md:36 (item 6)
- grok-bot.md:22 ("Digests (Command Center sends them).")

**Checked and left** (no claim about who sends the update, or accurate as written):
- "numbered digest item" / "listed digest item": the item inside the bulk update (flow:54, :58; roles:29 Replit track; command-center:18–20; mesh-lane-map:30, :31, :56; build:18)
- gitbook-cordnation:23 "Digests to Father" (Does not do), gitbook-moderator:19, :27, OHA2:22, tessera-pen:23 (Does not do lists)
- tessera-pen:46 "Ready for Father digest → Command Center" and OHA2:32 "Status for Father → Command Center": status goes to CC, which feeds Tessera's update
- build:26 "Status and deltas → Command Center", security:27 "Tessera, who routes it to Father's digest"
- operating-mode:31 cadence, :47–73 "Bulk digest contract", command-center:51–53 "Digest minimum": these define content, not the sender
- brain-consciousness/* ("Father's final yes in a bulk digest"), COLLABORATION-PLAYBOOK:13, CORTICAL-LABS-READINESS, AGI roadmap row 20: no sender named
- Records not edited: intake/log.md, history/coordination/agent-checkins.md, merge/hyb-005-braces-decision.md:36

**Outside the local subset.** These were read at 979c35e through cursor-github and contain no digest-sender claims: the six role pages above, operations/tessera-operating-guidelines.md, intake/AGENT-LAUNCH-PROMPTS.md, intake/consolidated-todo.md, intake/CONFERENCE-NEXT-STEPS.md, and forum/IDEA-FORUM.md. history/, merge/ and review/ records outside the subset were not re-read. They are historical records and are not edited. GitHub code search returned no results for this repo, so no index-wide search was possible.

## Canon re-scan of added lines
- No `> **Status` banners added (0). No `TESSERA_ENABLE_*` changes (0). No `status:` line touched.
- Every Tessera merge on an edited line comes after Father's yes. Every Origin/TESSERA merge line carries "the word 'merge'".
- yes/no/revise appears wherever a Father-decision line was edited.
- The Gitbook merge wording is byte-identical to rev 3, and rev 3 is not modified.

## Flags (not resolved silently)
1. `history/coordination/command-center.md` restored content says "The shared thread is tessera-coordination issue 2" and "Do not push Zz main". It is kept verbatim as a historical record. If Tessera wants a "historical" header added, that would change the restore's byte-identity.
2. flow.md:38 now uses a quoted mermaid label. The syntax is valid, but it was not rendered locally.
3. operating-mode "Bulk digest contract" and command-center "Digest format" / "Digest minimum" keep the word "digest". Per the ruling this is Tessera's bulk update, and the term was not renamed.
4. who-tessera-is.md:17 "the yes/no that survives…" is voice text and was left without revise.
