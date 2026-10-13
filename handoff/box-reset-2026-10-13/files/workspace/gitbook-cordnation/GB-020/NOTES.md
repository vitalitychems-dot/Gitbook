# GB-020 notes: brain-consciousness canon corrections (beadc44)

- Task: GB-020, corrective intake for Gitbook main `beadc44` ("Add CL1-inspired SNN brain research lane"). Tessera task; Father confirmed the beadc44 publish. **The lane stays. This is not a revert.**
- Base: main HEAD `e73fb185321fcb9e65eb61641ec8745bac85791d` ("Strengthen agent collaboration and skill governance"), checked 2026-10-05 15:15 CT. Open PRs: none. No commits newer than e73fb185.
- **Retargeted from beadc44 to e73fb185 with no content change.** e73fb185 changed only SUMMARY.md, intake/agent-submission-format.md, mesh/flow.md and the new mesh/AGENT-SKILL-MATRIX.md, mesh/COLLABORATION-METRICS.md and mesh/COLLABORATION-PLAYBOOK.md. It did not touch brain-consciousness/: the tree is `c67e708` at both commits. GB-020.v1.diff (sha256 `2ea6b556…`) passes `git apply --check -p1` on e73fb185 unchanged, and it is kept as GB-020.v1.diff.
- v2 (current GB-020.diff) adds only Tessera ruling 7: a blockquote note at the top of the charter. See the change map (C0) and "Tessera rulings 15:15 CT".
- Base blobs were checked against the beadc44 tree, and they are identical at e73fb185 (git hash-object): AGENT-WORKPLAN.md `42039cb`, SNN-SOURCE-MANIFEST.md `c5bde6c`, TESSERA-PEN-RESEARCH-CHARTER.md `ca1e05a`. All three match.
- Reference only, not edited: mesh/roles.md, mesh/flow.md, mesh/roles/ listing, mesh/roles/tessera-pen.md, mesh/roles/gitbook-moderator.md, mesh/roles/github-scraper.md, mesh/roles/tessera.md, mesh/roles/tessera-brain-consciousness.md, mesh/roles/mesh-lane-map.md, intake/status-definitions.md, SUMMARY.md.
- Files touched: the 3 files under `brain-consciousness/`, with no new files. None of the three has YAML front matter, so no front matter was added or changed. No gate banners were added.
- Snapshots: /tmp/g/gb020 (beadc44, v1) and /tmp/g/e73snap (e73fb185 subset, every blob verified against the e73 tree and commit). v1 diff: 128 lines (26 insertions, 24 deletions). v2 diff: 130 lines (28 insertions, 24 deletions).

## Change map

Line numbers are base (beadc44) lines.

### brain-consciousness/AGENT-WORKPLAN.md

| # | Line / section | Before (short) | After (short) | Conflict |
|---|---|---|---|---|
| W1 | L3 Coordinator | "Tessera Pen / Gitbook Moderator through the conference issue" | "Tessera assigns BC items. Gitbook Moderator reviews only; never merges or promotes into TESSERA. Check-ins go through the conference issue." | (1), (2), (5) |
| W2 | L9 table header | `Owner` | `Suggested owner` | (5) |
| W3 | L11 BC-001 owner | "Github Scraper / Moderator" | "Github Scraper (provisional, not instantiated); Gitbook Moderator reviews only" | (2), (3)* |
| W4 | L13–L18 BC-003..BC-008 owners | Computational neuroscience / RL-task / BrainCog / snnTorch / Brian2 / BindsNET "lane" | same name + " — PROPOSED (unrostered)" | (3) |
| W5 | L19 BC-009 owner | "TESSERA systems lane" | "TESSERA systems lane — PROPOSED (unrostered)" | (3) |
| W6 | L11–L20 Status column | `READY` ×10 | `PROPOSED` ×10 | (4) |
| W7 | L13 BC-003 deliverable | "across the approved sources" | "across the listed sources" (no approver on record for the sources) | (4) |
| W8 | new line after table (proposed L22) | none | "Suggested owners are not assignments. Items are assigned by Tessera. No approver is on record for BC-001 through BC-010." | (4), (5) |
| W9 | L24 Check-in protocol | "Before work begins, post one claim in the Gitbook conference using:" | "Items are assigned by Tessera. After Tessera assigns a BC item, the assigned lane posts one check-in … before work begins, using:" | (5) |
| W10 | L35 template | `STATUS: CLAIMED` | `STATUS: ASSIGNED (by Tessera)` | (5) |
| W11 | L46 Build order step 5 | "The Moderator promotes validated ideas into TESSERA and records rejected or deferred ideas here." | "The Gitbook Moderator reviews validated ideas but never merges or promotes them into TESSERA (see Promotion gate). Rejected or deferred ideas are recorded here." | (2) |
| W12 | L50 Promotion gate | "… a named owner, …" plus criteria only | "… an owner assigned by Tessera, …" plus "Meeting these criteria is not approval. The proposal then goes Moderator, then Tessera, then Security, then CI/Build, then Father's final yes in a bulk digest. Nothing merges into TESSERA without Father's explicit yes." | (5), (2) |

*W3: Github Scraper **is** on the roster, as Provisional / not instantiated, so it is labelled as the roster states rather than "PROPOSED (unrostered)". The Moderator's part is limited to review because BC-001's deliverable is authoring a manifest update, and the Moderator only reviews.

### brain-consciousness/SNN-SOURCE-MANIFEST.md

| # | Line / section | Before (short) | After (short) | Conflict |
|---|---|---|---|---|
| M1 | L3 in-body `**Status:**` line (not YAML front matter) | "Research sources approved for evaluation" | "Research sources PROPOSED for evaluation (no approver on record)". This line asserted a false state, so it now shows the truthful one. | (4) |
| M2 | L7 Purpose | "They are approved as references" | "They are proposed as references" | (4) |
| M3 | L23 Installation policy item 6 | "… and a moderator review before merge." | "… and the full review path before merge: Moderator, then Tessera, then Security, then CI/Build, then Father's final yes in a bulk digest. The Moderator reviews only; it does not merge." | (2) |

### brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md

| # | Line / section | Before (short) | After (short) | Conflict |
|---|---|---|---|---|
| C0 | after L1 H1 (top of page) | none | Blockquote: "The \"CL1-inspired\" and \"Consciousness\" framing in this lane is the author's goal framing, not a reported result. The cited sources (BindsNET, BrainCog, Brian2, snnTorch) do not cover Cortical Labs' CL1. Nothing in this lane is TESTED." It is not front matter and not a gate banner. It goes under the H1 rather than above it so the page title stays first. | Tessera ruling 7 (v2) |
| C1 | L3 heading | `## Role` | `## What Pen is` | (1) |
| C2 | L5 | "The Pen is the documented design and ethics gate … reject unsupported claims, and choose which validated proposals should enter the TESSERA implementation queue." | "Tessera Pen is Tessera's own writing voice. It is not a lane, and it is not a design or ethics gate or a reviewer. … does not approve, reject, or choose which proposals enter the TESSERA implementation queue. BC items are assigned by Tessera." | (1), (5) |
| C3 | L7, 2nd sentence | "A Pen decision is a recorded proposal or review outcome until a human-authorized moderator merges tested code." | "Pen text is a recorded proposal, not a review outcome or approval. The Gitbook Moderator reviews only and never merges; tested code reaches TESSERA only through Moderator, then Tessera, then Security, then CI/Build, then Father's final yes in a bulk digest." | (1), (2) |
| C4 | L14 PROMOTED | "accepted into TESSERA after moderator review." | "accepted into TESSERA only after Moderator, then Tessera, then Security, then CI/Build, then Father's final yes in a bulk digest." | (2) |
| C5 | L27 heading | `## First Pen review questions` | `## First research questions` (question list unchanged) | (1) |

Research content is unchanged: source table, licenses, installation policy items 1–5, hybrid boundary, verification evidence, design principles, deliverables and acceptance tests.

## Tessera rulings 15:15 CT

1. **Ruling 7 (only content change):** a short goal-framing note at the top of the lane's entry page. The lane has no index or README (only the 3 files), so the note is in TESSERA-PEN-RESEARCH-CHARTER.md right under the H1 (change C0). It is a plain blockquote with no front matter and no gate banner. None of the author's other text was rewritten.
2. **Charter title and filename are kept** ("Tessera Pen research charter", `TESSERA-PEN-RESEARCH-CHARTER.md`). No diff change.
3. **Security is not marked unrostered** in the pipeline wording. No diff change.
4. **"TESSERA systems lane" stays PROPOSED (unrostered)** and is not mapped to Build. No diff change.
5. **mesh/roles/tessera-brain-consciousness.md stays TBD and unlinked.** No diff change.
6. **"Gitbook conference" is left as is.** No diff change.

Rulings 2–6 close ambiguous items 1, 7, 5, 9 and 10 below. The text of those items is kept for the record.

## Ambiguous items left alone, and why

1. **Charter title and filename.** The H1 "Tessera Pen research charter", the filename `TESSERA-PEN-RESEARCH-CHARTER.md` and the SUMMARY.md nav label stay as they are. Renaming would mean editing SUMMARY.md, which is out of scope. The body now says this is a charter written in Pen voice, not a Pen lane or gate. For Tessera: should the title or filename change in a later package together with SUMMARY?
2. **Charter "agents must not fabricate Pen … approvals"** (L7, 1st sentence) was kept. It is a prohibition, not a grant of approval power, and removing it would weaken a safety rule.
3. **Charter heading `## Decision vocabulary`** was kept. The states (PROPOSED, TESTED, etc.) are generic lifecycle states, and C2 now says Pen does not decide. Rename only if Tessera wants it.
4. **`## Promotion gate` heading** was kept. It is a section heading for criteria, not a status/gate banner. The body now says that meeting the criteria is not approval.
5. **"TESSERA systems lane" (BC-009)** was marked PROPOSED (unrostered). TESSERA is rostered Active as the *build* lane only, and no "systems lane" is on the roster. If Tessera means the TESSERA build lane, the label can drop.
6. **"TESSERA build lane" (BC-002)** was left unlabelled because it matches the rostered Active TESSERA lane ("Build lane: code builds and branches").
7. **Security in the pipeline.** The pipeline text (Moderator → Tessera → Security → CI/Build → Father) is the canon given in the task. At beadc44, `mesh/roles.md` and `mesh/roles/` have **no Security role page** (it is pending in frozen GB-017). It was not labelled "PROPOSED (unrostered)" because the wording is mandated pipeline canon. Tessera should confirm this is fine until GB-017 lands. Likewise, "CI/Build" maps to the rostered Build lane.
8. **mesh/roles.md still lists Tessera Pen as "Provisional / not instantiated — Writing and task-direction lane"**, and mesh-lane-map.md has a Pen publish path. Both conflict with canon (1), "Pen is a voice, not a lane", but they are outside brain-consciousness/ and were not touched. Candidate for the later delta.
9. **mesh/roles/tessera-brain-consciousness.md** is rostered **TBD / not instantiated**. The workplan does not say which rostered lane owns the brain-consciousness program, and no ownership claim was added. Tessera may want to link the lane to that role page later.
10. **"Gitbook conference" / "conference issue"** (workplan) vs flow.md "one board only: tessera-coordination issue #4". Left alone because it may be the same board, and it is not one of conflicts (1)–(5).
11. **BC-010 owner "Gitbook Moderator"** was kept. The deliverable is a review ("Review language, data handling, …"), which is within Moderator's review-only scope.
12. **"On completion, update the same check-in with the commit …"** was kept. It describes reporting, not merging. Father's yes still governs merges (W12).

## Claims check (candidates for Tessera; research text not rewritten)

No new capability, consciousness, sentience or AGI claims were added. Existing text already disclaims biological equivalence and consciousness. Items Tessera may want to review:

- **"CL1-inspired" framing** (titles, scope, hybrid boundary). None of the four listed sources (BindsNET, BrainCog, Brian2, snnTorch) is related to Cortical Labs' CL1. The "inspired" link is the beadc44 author's framing, not something the sources report. The text already says it is not a CL1 replica.
- **Lane name "Brain & Consciousness Development"** (workplan H1, SUMMARY section). "Consciousness" in the name could be read as a goal claim. The scope line already says it "does not establish consciousness".
- **License column and "official repository pages were inspected on 2026-10-05"** are REPORTED by the beadc44 author and were not re-verified by Cordnation in GB-020. BC-001 is the item that re-checks them.
- **"Pong-like … benchmarks"** echo CL1/DishBrain coverage. This is a task proposal, not a capability claim, so it was left alone.

## Noted from e73fb185 (outside GB-020 scope; for Tessera)

- mesh/COLLABORATION-PLAYBOOK.md loop step 2 ("Claim — reserve one task") and mesh/flow.md ("Agents discover → claim one task") tell agents to claim tasks. That conflicts with GB-020's canon that BC items are assigned by Tessera.
- The playbook escalation row "Product or consciousness claim → Tessera Pen + Moderator" treats Pen as a reviewer (conflict 1).
- The playbook step 8 "Promote or defer" and the flow.md pipeline (Moderator → Build → Command Center) leave out the Tessera and Security gates.
- AGENT-SKILL-MATRIX lists "Tessera Pen" and "Brain/SNN research" as lanes.
- None of these is in brain-consciousness/, so GB-020 does not change them.

## Checks

- v1: `git apply --check -p1` passes on beadc44 and, unchanged, on e73fb185.
- v2 (GB-020.diff): `git apply --check -p1` passes on a clean e73fb185 snapshot, and the applied result is byte-identical to `proposed/`. `base/` is unchanged because the blobs are identical at e73.
- Interdiff v1 → v2 (applied-content diff): one hunk, +2 lines (the note and a blank line) in the charter. The raw diff-of-diffs shows only that, plus the charter hunk header (`-1,17 +1,19`), the index line and a +2 line offset on the next hunk header.
- `grep '^+++ b/' GB-020.diff` lists only the 3 `b/brain-consciousness/…` paths. Nothing is outside brain-consciousness/.
- SHA256 is in SHA256.txt.
- Nothing was written to GitHub. No TESSERA_ENABLE_* flags were touched. GB-015..GB-019 and FROZEN-SHA256-*.txt were not touched.

## v3 (15:19 CT, Tessera PASS with condition)
Only change since v2 (sha 5a56ee0b, kept as GB-020.v2.diff): BC-002 owner cell in AGENT-WORKPLAN.md, 'TESSERA build lane' to 'TESSERA build lane — PROPOSED (unrostered)' (same as ruling 4; Build is verify-only and not an implementing lane). Base still e73fb185 (brain-consciousness tree unchanged). git apply --check OK; only brain-consciousness/ paths.
