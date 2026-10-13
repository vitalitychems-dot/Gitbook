# GB-016 rev 3.2: content rebase onto f4b2c41 (Tessera 15:42 and 15:46 CT)

- **Main:** `f4b2c41ee458e54fc4f12cecd4cab941aa8e627c`. PR #5 (GB-015, 019, 021, 020) merged on feaeb558 (Manus operating mode), which sits on fb984ad (Replit), on 1e3bb50. 0 open PRs.
  - PR #5's 8 blobs match a feaeb558 snapshot plus the 4 frozen diffs.
  - PR #5 did not touch flow.md, roles.md or command-center.md.
- **Base:** f4b2c41 + GB-017 (`GB-017.f4b2c41.diff`). Like rev 3.1, this never lands alone; it needs GB-017 first.
- **Diff:** `GB-016-rev3.2.f4b2c41.diff`, 422 lines, 9 files, sha256 `872a885b28bb23f31562edd46a1eb23d152772ef8c94a371686d126db2482007`.
  - `GB-016-rev3.2.diff` is an identical copy.
  - `GB-016-rev3.2.feaeb558-draft.diff` (25464f8e, 416 lines) is the pre-15:46 draft without the Pen row fix.
  - Rev 3.1 (af18bc3b) is kept unchanged.
- **Interdiff:** `INTERDIFF-rev3.1-to-3.2.diff` compares the rev 3.1 result on 1e3 with the rev 3.2 result on f4b2c41, for the 3 files that differ.
- **Copies:** `base-f4b2c41/` and `proposed-f4b2c41/`.
- **Classification: CONTENT CHANGE.** It needs all four gates and a fresh Father yes.

## Section by section

- **Byte-identical to rev 3.1:** `intake/status-definitions.md`, `mesh/roles/build.md`, `mesh/roles/gitbook-cordnation.md`, `mesh/roles/mesh-lane-map.md`, `mesh/roles/open-helper-agent-2.md`, `review/moderator-handoff.md`. Neither feaeb558 nor PR #5 touched these files.
- **Regenerated:** `mesh/flow.md`, `mesh/roles.md`, `mesh/roles/command-center.md`, the files feaeb558 rewrote. Every feaeb558 addition is kept verbatim except the designed merges below.

| Area | feaeb558 has | rev 3.2 result |
|---|---|---|
| flow.md front matter, operating-model link, 3 new standing rows (Product repository, Bulk cadence, Approval response), related-pages link | new | kept verbatim (GB-016 doesn't touch them) |
| flow.md "Canonical approval rule" blockquote | Grok bot/CC digest every 30–45 min; yes/no/revise; Father alone pushes; `merge` | feaeb558 text kept verbatim. Rev 3.1's canon sentences are inserted before the `merge` sentence: Replit never a GitBook path; CC's only push is the private Replit app set "28", "Run Z", "29", "29 (1)", "1", NOT "Vitality Supply", after all four gates + Father's yes; the app-29 flag. |
| flow.md pipeline sentence | "Agents discover → Pen assigns/agent claims one task → work in Gitbook or TESSERA → Moderator → Build → Grok bot/CC digest → Father yes/no/revise → Father pushes → merge" | Rev 3.1's full four-gate sentence (Father's 2:34 rule), with feaeb558's "in Gitbook or TESSERA", "Tessera Grok bot /" and `yes` / `no` / `revise` (revise returns the named items) merged in. "Pen assigns" becomes **Tessera** assigns. |
| flow.md diagram | A[Pen directs and agent claims one task] → … → Build → CC ~30 min → G{yes/no/revise}; no → record decision; revise → C | Rev 3.1 diagram (overlap check → Tessera assigns → Moderator → Tessera → Security → CI/Build → Ready → CC digest → Father → Father pushes), with G = `{Father: yes / no / revise?}`, `no + notes` → H0 "Hold named items / record decision; do not publish", and `revise` → C. |
| flow.md standing rows CC / Replit / Push authority | 1e3 text | rev 3.1 rows, plus Replit push set, Ready staging, Per-gate state and Digest items (now with "**revise** returns the named items") |
| flow.md lane bullets | "Tessera Grok bot / Command Center — … yes/no/revise, and has no push authority" | feaeb558 name and wording, plus rev 3.1's Replit app-set role. "has no push authority" is replaced by "its only push is a private push of the Replit app set … (not a GitBook path). Never pushes GitBook or TESSERA". Cordnation and All-lanes bullets are as in rev 3.1. feaeb558's "Tessera" bullet is kept; the Pen bullet is handled by GB-017. |
| roles.md front matter + banner `> **Status: published — operating model aligned**` | new | kept (feaeb558's 'Status: published' line) |
| roles.md CC row | "Command Center / Tessera Grok bot · **Active workflow** · Prepares 30–45 minute bulk digests and asks Father for yes/no/revise" | name, status and text kept, with rev 3.1's numbered items, Father handoff and Replit-only push clause appended |
| roles.md Cordnation row | unchanged | rev 3.1 |
| roles.md path sentence | "agent claim → Pen scope → … → Build → … yes/no/revise → Father alone pushes the approved Gitbook changes …" | "overlap check → Tessera assigns (claim only after assignment) → Gitbook/TESSERA work → intake → Moderator → Tessera → Security → CI/Build → Ready → Grok bot/CC digest → Father `yes`/`no`/`revise` → Father alone pushes the approved Gitbook changes … (docs items) → `merge`", plus the Replit app-set clause |
| roles.md CC paragraph | 1e3 text | rev 3.1 (Replit app set + app-29 flag) |
| **roles.md Pen row (Tessera 15:46 add)** | feaeb558: "Configured / live participation requires check-in · Directs scoped work and protects coherence". GB-017 already replaces it with "**Not a lane** — Tessera's own writing voice · Tessera's own writing voice on GitBook/GitHub as Pen". | rev 3.2 appends "; not a gate; needs no check-in" to the one-line cell. Minimal wording. With GB-017 applied first, "directs the work" and "Configured / live participation requires check-in" are gone from roles.md. |
| command-center.md note, 3 new Owns bullets, 2 new Does-not-do bullets, Grok bot sentence, Digest minimum section | new | kept verbatim |
| command-center.md Replit boundary | "… The old private push set is historical and is no longer an active Command Center responsibility." | that sentence is dropped (superseded by Father's 2:32 canon, as in rev 3.1); "never a GitBook publication path; Father alone pushes" added; the Grok bot sentence is kept |
| command-center.md "no GitHub push authority" (Owns) | 1e3 text | dropped as in rev 3.1 (CC's only push is the Replit app set) |
| command-center.md Father digest approval | (rev 3.1) yes / no | adds "**revise** keeps the named items unpublished pending the stated change" |
| mesh/TESSERA-GITBOOK-OPERATING-MODE.md | new (feaeb558) | **not touched** |

## Tessera gate condition (four-gate pipeline)

Checked on the stacked result f4b2c41 + GB-017 + GB-018 + GB-016 rev 3.2:
- The flow.md sentence and diagram both carry overlap check → Tessera assigns → Moderator → Tessera → Security → CI/Build → Ready → CC digest → Father's yes → Father pushes.
- No "claim one task", "Pen assigns", "Pen directs", "approximately every 30", "~30 min", "reviews → Build", "Father decides", "directs scoped" or "Configured" anywhere in flow.md, roles.md or command-center.md. The only "configured" hit is feaeb558's "unless separately configured" in the Bulk cadence row.

## Apply checks (f4b2c41 snapshot)

- **Solo:** GB-017 OK and GB-018 OK, both with 0 offsets. GB-016 rev 3.2 alone fails at flow.md:55 and roles.md:11. That is by design: it needs GB-017 first, same as rev 3.1.
- **Stack 017 → 018 → 016 rev 3.2:** all OK, 0 offsets. Result for the GB-016 and GB-017 files equals `proposed-f4b2c41/`. SUMMARY carries both the GB-017 and GB-018 lines.
- **Earlier feaeb558 checks (pre-15:46 draft):** solo, the stack with 015/019/021/020, and the stack without them all passed.
