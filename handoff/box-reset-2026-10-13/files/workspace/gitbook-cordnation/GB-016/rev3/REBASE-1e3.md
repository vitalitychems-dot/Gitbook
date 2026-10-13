# GB-016 rev 3: second rebase onto 1e3bb50 (Tessera final rulings 15:20 CT)

- **Overlap check:** main is `1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea` (parent e73fb185), 0 open PRs (checked ~15:21 CT).
- **Base:** 1e3bb50 + GB-015 + GB-017 (GB-017 applies unchanged on 1e3bb50). Never lands alone; it lands after GB-017.
- **Diff history:**
  - e73 diff kept as `GB-016-rev3.e73.diff`, sha256 `155ba93b…`.
  - beadc44 diff kept as `GB-016-rev3.beadc44.diff`, sha256 `baad1a3c…`.
  - New `GB-016-rev3.diff`: 403 lines, sha256 `e4efe98dfb2a4f038162cc09a2c8962605d4f45bcefe5aa66bba4bc0e6752664`.
- **Unchanged sections:** the sections for `intake/status-definitions.md`, `mesh/flow.md`, `mesh/roles.md`, `mesh/roles/build.md`, `mesh/roles/gitbook-cordnation.md` and `mesh/roles/open-helper-agent-2.md` are **byte-identical** to the e73 diff. 1e3bb50 did not touch these files.
- **Regenerated sections:** only `mesh/roles/command-center.md`, `mesh/roles/mesh-lane-map.md` and `review/moderator-handoff.md`, the three files 1e3bb50 changed.
- **Copies:** `base-1e3/` and `proposed-1e3/` hold all 9 files.

## Classification (Tessera ruling 4)

**CONTENT CHANGE, so all four gates (Moderator → Tessera → Security → CI/Build).** The reason is ruling 2's lane-map wording hunk. Apart from that hunk, the 1e3 result equals the e73 rebase result, with only redundant or superseded hunks dropped.

## Hunk decisions

| File | e73 diff did | 1e3bb50 did | 1e3 rebase does | Type |
|---|---|---|---|---|
| command-center.md front matter | ` status: corrected-pending-publish` → ` status: published` (leading space kept) | set `status: published` / `note:` (no leading space) | nothing; 1e3's front matter is kept | redundant, dropped |
| command-center.md banner | removed `> **Status: corrected — pending Gitbook publication**` | replaced it with `> **Status: published — authority wording aligned**` | nothing; 1e3's banner is left alone (ruling 1) | redundant (target line gone), dropped |
| command-center.md "Does not do" | removed `- Use Replit as a private push proxy` | removed the same line | nothing | redundant, dropped |
| command-center.md Owns / Father digest approval / Does not do / Replit boundary / Replit push set | GB-016 content | — | same content, re-anchored | unchanged |
| mesh-lane-map.md front matter | deleted the stale ` status: corrected-pending-publish` block | set valid `status: published` front matter | nothing; 1e3's front matter is kept (15:06 rule: existing pages `published`) | superseded, dropped |
| mesh-lane-map.md banner `> **Status: corrected — pending Gitbook publication**` | removed | left in place (still stale) | still removed | unchanged |
| mesh-lane-map.md `**Status:**` line | deleted the `REPORTED — … awaiting Father GitHub push` line | rewrote it to `PUBLISHED — …; each new change still requires the normal Moderator and Father gates.` | **keeps the line and "PUBLISHED — authority map aligned;" verbatim; changes only the trailing clause** to "each new change still requires Moderator, then Tessera, then Security, then CI/Build, then Father's final yes." | **CONTENT CHANGE (ruling 2)** |
| mesh-lane-map.md rest (Identity line, who-asks-whom rows, Delivery sync, Publish path, Replit app set, Father digest approval) | GB-016 content | — | same content, re-anchored | unchanged |
| moderator-handoff.md banner removal + checklist + Approve row | GB-016 content | — | identical hunk | unchanged |
| moderator-handoff.md "Out of Moderator scope" | replaced `- Replit / GitHub pushes (Command Center, Father-gated)` + Digests line with 4 lines | changed that line to `- GitBook → GitHub pushes (Father only after approval)` | replaces 1e3's line with the same 4 GB-016 lines. GB-016's "GitBook docs push (Father only, after Ready yes on the listed item; Replit outside that path)" covers 1e3's line more specifically. The result is byte-identical to the e73 result. | re-anchored (`-` line changed; `+` lines unchanged) |

## Interdiff: e73 rebase result → 1e3 rebase result (only files that differ)

`review/moderator-handoff.md`: identical (no interdiff). The other 6 files are identical by construction.

```diff
--- e73 rebase result: mesh/roles/command-center.md
+++ 1e3 rebase result: mesh/roles/command-center.md
@@ -1,10 +1,12 @@
 ---
- status: published
- note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
+status: published
+note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
 ---
 
 # Command Center
 
+> **Status: published — authority wording aligned**
+
 ## Lane status
 
 Active.
--- e73 rebase result: mesh/roles/mesh-lane-map.md
+++ 1e3 rebase result: mesh/roles/mesh-lane-map.md
@@ -1,7 +1,15 @@
+---
+status: published
+note: Father is sole GitBook → GitHub push authority; Command Center coordinates only.
+---
+
 # Mesh lane map (for Father)
 
 Intake GB-014 (supersedes GB-013 publish/Delivery sections) · Author lane: Tessera Pen · Date (CT): 2026-10-05 · Source: Tessera Pen delta (Father bulk sync; no new backlog) · License: TBD · Suggested path: `mesh/roles/mesh-lane-map.md`
 
+
+**Status:** PUBLISHED — authority map aligned; each new change still requires Moderator, then Tessera, then Security, then CI/Build, then Father's final yes.
+
 **Instrument:** The pen is currently xAI/Grok. I never claim otherwise.
 
 **Identity:** Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen.
```

Everything in this interdiff comes from 1e3bb50's own lines, kept as they are (front matter, CC banner, lane-map front matter, PUBLISHED status line). The one exception is the ruling-2 clause on the lane-map status line.

## Checks

- `git apply --check -p1` on a 1e3bb50 snapshot (all blobs verified against the 1e3 commit), stacked GB-015 → GB-017 → GB-016 rev 3 → GB-018 → GB-019 → GB-021: all OK, with 0 offset hunks.
- **Applied-result retention after the full stack:**
  - All 8 lines 1e3bb50 added are present verbatim, except (a) the lane-map status clause (ruling 2) and (b) the moderator-handoff "GitBook → GitHub pushes (Father only after approval)" line, which GB-016's more specific push line supersedes.
  - All e73 additions are present verbatim, except the pipeline sentence, diagram and "All lanes" qualifier merged in the e73 rebase (see REBASE-e73.md).
- No new gate banners. Front matter: command-center, lane-map and flow all say `published`.
- **Carried over, for Tessera:** this diff still deletes the pre-existing `> **Status: published 2026-10-05 (commit 98fa6c7) …**` banners in status-definitions.md, gitbook-cordnation.md and moderator-handoff.md, per the 15:04 banner-strip ruling. Ruling 1 names only the CC banner and the lane-map Status line, so these were not restored.

---

# Rev 3.1 (Tessera rulings 15:24 CT and gate condition 15:25 CT)

- **Overlap check:** main is still `1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea`, 0 open PRs (~15:25 CT). Base: 1e3bb50 + GB-015 + GB-017, the same as rev 3.
- **Files:**
  - `GB-016-rev3.1.diff`: 408 lines, sha256 `af18bc3bf82701f10159ab11180767d9e43073713c7efc47faaddebd4af23b45`. Same 9 files, generated the same way as rev 3 (byte-reproducible).
  - `GB-016-rev3.diff` (e4efe98d) is kept unchanged.
  - Interdiff: `INTERDIFF-rev3-to-3.1.diff`, a diff of the applied results, 8 files, +36/−31.
  - The full 3.1 result is in `proposed-3.1/`.
- **Classification:** content change, so all four gates.

## What rev 3.1 changes (Command Center's Replit role reworded so it can't read as a GitBook push path)

Canon (Father, 2:32 PM CT):
- Command Center's **only** push is the private push of the Replit app set ("28", "Run Z", "29", "29 (1)", "1"; NOT "Vitality Supply"), only after all four gates and Father's yes.
- Command Center never pushes GitBook or TESSERA.
- Replit is never a GitBook publication path; Father alone pushes GitBook → GitHub.
- The "29" push stays flagged until Father confirms it is detached from 1T.

| File | Change |
|---|---|
| mesh/roles/command-center.md | Owns: staging and private-push bullets now say "Command Center's **only** push; not a GitBook publication path" and add the four gates. Does not do: "other than the Replit app-set role above" is replaced by "Push GitBook or TESSERA in any form (its only push is the private Replit app-set push above)". Replit boundary: adds "never a GitBook publication path; Father alone pushes GitBook → GitHub". "## Replit push set" is renamed "## Replit app set push (not a GitBook path)", with the canon paragraph, the app set and the app-29 line. |
| mesh/roles/mesh-lane-map.md | The two Replit rows are tagged "(not a GitBook path)"; the push row adds the four gates, "never GitBook or TESSERA" and the "29" flag. Publish path step 9: "Replit app-set items (not part of this GitBook path)". The Replit section gets the canon paragraph and the app-29 line. |
| mesh/flow.md | Canonical push rule: canon wording plus the app-29 line. The pipeline sentence no longer has the Replit push as a step inside the GitBook path; it now ends "… Father alone pushes GitBook → GitHub (Replit is never a GitBook publication path) → `merge` … Separately, outside the GitBook path: … Command Center privately pushes only the Replit app set." Diagram nodes R0 and R are labelled "not a GitBook path". The Command Center, Replit, Push authority (2) and Replit push set rows and the CC roster bullet are reworded; the push-set row gets the app-29 line. |
| mesh/roles.md | CC row: "only push = private Replit app-set push after four gates + Father's yes (not a GitBook path)". The canonical path no longer carries the "/ Command Center privately pushes…" branch. The CC paragraph is canon wording plus the app-29 line. |
| review/moderator-handoff.md | Approve row and Out-of-scope lines: "Replit is never a GitBook publication path"; Replit app set is "separate; not a GitBook path", with the four gates and "CC's only push". |
| mesh/roles/build.md, open-helper-agent-2.md, gitbook-cordnation.md | One clause each: "its only push … after all four gates … not a GitBook path". |

Exact new lines:
- Replit canon line (in command-center.md and mesh-lane-map.md): "Command Center's only push is a private push of the Replit app set ("28", "Run Z", "29", "29 (1)", "1"; NOT "Vitality Supply"), only after all four gates (Moderator, Tessera, Security, CI/Build) and Father's yes on the listed digest item. It is not a GitBook publication path: Command Center never pushes GitBook or TESSERA, Replit is never a GitBook publication path, and Father alone pushes GitBook → GitHub."
- App-29 line (command-center.md, mesh-lane-map.md, flow.md push rule and push-set row, roles.md): "The "29" app push stays flagged until Father confirms "29" is detached from 1T." The lane-map table cell uses the short form: ""29" stays flagged until Father confirms it is detached from 1T."

Unchanged:
- 1e3's `Status: published` lines (CC banner and lane-map Status line, which still carries the ruling-2 clause) and all front matter.
- `intake/how-to-submit.md` and `review/COLLABORATION-AUDIT-2026-10-05.md` are not touched. The wording stays consistent with step 4 ("Father alone pushes GitBook → GitHub …; Replit is outside that path") and with the audit page (no CC/Replit push contradiction; Replit outside the GitBook → GitHub path).
- The legacy phrases "one push role", "no push over Gitbook/TESSERA" and "other than the Replit app-set role" no longer appear anywhere in the 9 files.

## Tessera gate condition 15:25 (full four-gate pipeline in flow.md)

Checked on the stacked result 1e3bb50 + GB-015 + GB-017 + GB-016 rev 3.1:
- Both the pipeline sentence (line 12) and the mermaid diagram show overlap check → Tessera assigns → Moderator → Tessera → Security → CI/Build → Ready → CC digest → Father's yes → Father pushes.
- None of e73's no-Tessera/no-Security wording is left anywhere in flow.md: no "claim one task", "approximately every 30 minutes", "Moderator reviews → Build", "Father decides Ready/yes", `D -->|approved| E[Build`, or "digest to Father ~30 min".

## Stack check (rev 3.1)

- On a 1e3bb50 snapshot, GB-015 → GB-017 → GB-016 rev 3.1 → GB-018 → GB-019 → GB-021 all apply with 0 offsets and 0 fuzz. The only warnings are trailing whitespace inside the frozen GB-018 (3) and GB-019 (2), which were already there.
- The stacked GB-016 files are byte-identical to `proposed-3.1/`.
- GB-020 (2e3b5400, v3) applies on its own with 0 offsets.
