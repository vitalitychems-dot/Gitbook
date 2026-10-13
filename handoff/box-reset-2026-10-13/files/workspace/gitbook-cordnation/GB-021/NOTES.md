# GB-021 notes: e73 collaboration pages canon fixes

- **Task:** Tessera ruling 15:18 CT (Part 2). Scope is limited to e73fb185's three new pages: `mesh/AGENT-SKILL-MATRIX.md`, `mesh/COLLABORATION-PLAYBOOK.md`, `mesh/COLLABORATION-METRICS.md`.
- **Base:** main `e73fb185321fcb9e65eb61641ec8745bac85791d`, 0 open PRs (checked ~15:18 CT). The base blobs were rebuilt from the e73 commit and hash-verified: `c56b3f8` (skill matrix), `2b41319` (playbook), `666973e` (metrics).
- **Base moved to 1e3bb50 (Tessera final rulings 15:20 CT, ruling 3):** main `1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea`, 0 open PRs (~15:21 CT). 1e3bb50 did not touch any of the 3 pages; their blobs are identical at e73 and 1e3. The diff is unchanged and applies on 1e3bb50 with 0 offsets, so `base/` and `proposed/` are valid for 1e3bb50 as they are.
- **Scope (ruling 3):** `review/COLLABORATION-AUDIT-2026-10-05.md` is **not** in GB-021. The audit page stays as it is. GB-021 doesn't touch `mesh/roles/mesh-lane-map.md` either; the ruling-2 lane-map hunk is in GB-016 rev 3.
- **Files touched (2):** `mesh/AGENT-SKILL-MATRIX.md` and `mesh/COLLABORATION-PLAYBOOK.md`.
  - `mesh/COLLABORATION-METRICS.md` was reviewed and **left unchanged**. It doesn't treat Pen as a lane or reviewer, doesn't send consciousness or product claims anywhere, doesn't name the Brain/SNN lane, doesn't promote anything, and doesn't steer agents to claim without assignment. Its "claim" references describe check-ins on tasks that are already held.
- **Diff:** 62 lines (9 insertions, 9 deletions). No front matter (the base pages have none), and no gate banners.

## Change map

| # | File / line | Before (short) | After (short) | Fix |
|---|---|---|---|---|
| S1 | AGENT-SKILL-MATRIX.md L3 | "Use skill IDs in every task claim." | "… in every task claim (a task is claimed only after Tessera assigns it)." | Claim only after Tessera assigns |
| S2 | AGENT-SKILL-MATRIX.md L39 role table | `Tessera Pen \| SK-06, SK-11 \| SK-02, SK-10` | `Tessera Pen \| — (not a lane: Tessera's own writing voice; not a reviewer) \| —` | Pen is a voice, not a lane or reviewer |
| S3 | AGENT-SKILL-MATRIX.md L40 role table | `Brain/SNN research` | `Brain/SNN research — PROPOSED (unrostered)` | Brain/SNN lane PROPOSED, not rostered |
| P1 | COLLABORATION-PLAYBOOK.md L8 loop step 2 | "Claim — reserve one task and exact paths before editing." | "Claim — only after Tessera assigns the task, reserve it and its exact paths before editing. Unassigned tasks are not claimed." | Claim only after Tessera assigns |
| P2 | COLLABORATION-PLAYBOOK.md L13 loop step 7 | "Review — Moderator checks scope, provenance, tests, security, and duplication." | "Review — four gates in order, then Father: Gitbook Moderator (… ; reviews only) → Tessera (admin) → Security (read-only sweep) → CI/Build (independent verification) → Father's final yes in the bulk digest." | Four gates plus Father's yes before Promote |
| P3 | COLLABORATION-PLAYBOOK.md L14 loop step 8 | "Promote or defer — accepted work becomes a TESSERA/Gitbook task; …" | "Promote or defer — only after all four gates and Father's final yes, accepted work becomes …" | Four gates plus Father's yes before Promote |
| P4 | COLLABORATION-PLAYBOOK.md L20 one-task lock | "… obtain a new claim or moderator approval." | "… get a new assignment from Tessera before claiming again." | Claim only after Tessera assigns (and the Moderator reviews only) |
| P5 | COLLABORATION-PLAYBOOK.md L21 one-task lock | "… record the reason, then reassign." | "… record the reason, then Tessera reassigns." | Claim only after Tessera assigns |
| P6 | COLLABORATION-PLAYBOOK.md L61 escalation | `Product or consciousness claim \| Label as proposal/unknown \| Tessera Pen + Moderator` | `… \| Label as GOAL or UNKNOWN \| Gitbook Moderator, then Tessera` | Claims go Moderator → Tessera, labelled GOAL/UNKNOWN; Pen not a reviewer |

Everything else is kept verbatim: skill levels, canonical skills, other roles, training cycle, handoff packet, communication rules, other escalation rows, definition of done, and all of the metrics page.

## Left alone for Tessera's call

1. **Front matter.** These pages have been on main since e73 but never had front matter. The 15:06 rule restores or replaces existing status front matter, and new pages get none. I read that as "don't add front matter here". If Tessera wants `status: published` added to e73 pages, that's 3 more lines.
2. **SK-10 "follow-up assignment"** (skill evidence for Coordination and moderation, held by Moderator, Cordnation and Command Center) may read as those lanes assigning work, which Tessera does. I left it because it's skill evidence, not a process step.
3. **"Replit/Grok collaborator" lane row.** Grok Bot is on the roster (Active via GB-017). "Replit" is not a roster lane. It's not in the fix list, so I didn't mark it.
4. **Loop step 1 "Discover"** doesn't mention the overlap check (main SHA plus open PRs) that the rebased GB-016 flow.md now requires. I didn't add it because it's not in the fix list. It's a one-line add if wanted.
5. **Escalation rows "Moderator + human owner"** (license, security). I left them because they are escalations, not approvals, and Father stays the final yes via step 7.
6. **Metrics "Handoff latency … to moderator decision"** and "Moderator samples closed tasks". These are review-only and consistent with canon, so I left them.

## Checks

- **1e3bb50 (current base):** `git apply --check -p1 GB-021.diff` passes alone. It also passes after the full five-package stack (GB-015 → GB-017 → GB-016 rev 3 [1e3 version] → GB-018 → GB-019), with 0 offset hunks.
- **e73fb185 (earlier base):** passes alone and after the e73 five-package stack. The applied result is byte-identical to `proposed/`.
- `grep '^+++ b/' GB-021.diff` lists only `mesh/AGENT-SKILL-MATRIX.md` and `mesh/COLLABORATION-PLAYBOOK.md`, both inside the allowed 3 paths.
- SHA256 is in SHA256.txt.
- Nothing was written to GitHub, and no TESSERA_ENABLE_* flag was touched.
