# GB-017 rebase onto e73fb185 (Tessera ruling (a), 15:18 CT)

- **Overlap check:** main is `e73fb185321fcb9e65eb61641ec8745bac85791d` and there are 0 open PRs (checked ~15:18 CT).
- **Old diff:** kept as `GB-017.beadc44.diff`, sha256 `b9848d3c…` (byte-identical to the frozen GB-017.diff). FROZEN-SHA256-status.txt is untouched and stays as history.
- **New diff:** `GB-017.diff`, 180 lines, sha256 `ca3ef7002aa9c75e043019112985c74981484e907b88444cc2c6d25c33576d34`.
  - Its `mesh/roles/security.md`, `mesh/roles/tessera-pen.md` and `mesh/roles.md` sections are **byte-identical** to the beadc44 diff.
  - Only the `SUMMARY.md` and `mesh/flow.md` sections were regenerated.
- **Copies:** `base-e73/` and `proposed-e73/` hold the e73 base and the result for every touched file. The old `base/` and `proposed/` folders are kept as history.

## Content decisions

1. **flow.md "Tessera identity" row:** re-anchored to the end of the Standing rules table, after e73's Task lock / Evidence / Status truth rows. The text is unchanged.
2. **flow.md "Security" lane line:** re-anchored right after `- **Build** —` and before e73's `- **All lanes** —` line. Security is a lane; "All lanes" is a cross-lane rule. The text is unchanged.
3. **flow.md front matter:** e73 left `status: corrected-pending-publish` in place. The `status: published` hunk is kept per the 15:06 ruling (existing page means `published`). The `note:` line is unchanged.
4. **SUMMARY.md:** the Grok Bot (TBD → Active) hunk is re-anchored from `@@ -51` to `@@ -54` because of e73's +3 nav lines. Content is unchanged, and e73's 3 nav links are untouched.
5. **No other content change.** No gate banners were added.

## Interdiff of results (old = beadc44 + old diff; new = e73fb185 + new diff)

Files with identical results: `mesh/roles.md`, `mesh/roles/security.md`, `mesh/roles/tessera-pen.md` (same blob hashes).

The differences below are e73's own additions, kept verbatim, plus the identity row moving down the table.

```diff
--- old result (beadc44 + old diff)
+++ new result (e73fb185 + new diff)
@@ -30,6 +30,9 @@
 ## Mesh
 
 * [Flow & standing rules](mesh/flow.md)
+* [Agent collaboration playbook](mesh/COLLABORATION-PLAYBOOK.md)
+* [Agent skill matrix](mesh/AGENT-SKILL-MATRIX.md)
+* [Collaboration metrics](mesh/COLLABORATION-METRICS.md)
 * [Roles overview](mesh/roles.md)
   * [Gitbook / Cordnation](mesh/roles/gitbook-cordnation.md)
   * [Gitbook Moderator](mesh/roles/gitbook-moderator.md)
--- old result (beadc44 + old diff)
+++ new result (e73fb185 + new diff)
@@ -9,20 +9,23 @@
 
 ## End-to-end flow
 
-Agents produce work → **Gitbook / Cordnation** intake → **Gitbook Moderator** reviews → **Command Center** digests to Father approximately every 30 minutes → Father decides Ready/yes → **Father pushes GitBook → GitHub** → Father separately says `merge` for an Origin merge.
+Agents discover → claim one task → produce work → **Gitbook / Cordnation** intake → **Gitbook Moderator** reviews → **Build** independently verifies → **Command Center** digests to Father approximately every 30 minutes → Father decides Ready/yes → **Father pushes GitBook → GitHub** → Father separately says `merge` for an Origin merge.
 
 ```mermaid
 flowchart TD
-  A[Agents produce work] --> B[GitBook intake<br/>Gitbook / Cordnation]
-  B --> C[Gitbook Moderator<br/>approve / reject]
-  C -->|approved| D[Command Center<br/>digest to Father ~30 min]
-  C -->|rejected| B
-  D --> E{Father Ready / yes?}
-  E -->|no| D
-  E -->|yes| F[Father<br/>pushes GitBook → GitHub]
-  F --> G{Father explicit merge?}
-  G -->|no| H[Stays unmerged]
-  G -->|yes| I[Merge]
+  A[Discover and claim one task] --> B[Agents produce scoped work]
+  B --> C[GitBook intake<br/>Gitbook / Cordnation]
+  C --> D[Gitbook Moderator<br/>scope / provenance review]
+  D -->|approved| E[Build<br/>independent verification]
+  D -->|needs work| C
+  E -->|pass| F[Command Center<br/>digest to Father ~30 min]
+  E -->|fail| C
+  F --> G{Father Ready / yes?}
+  G -->|no| F
+  G -->|yes| H[Father<br/>pushes GitBook → GitHub]
+  H --> I{Father explicit merge?}
+  I -->|no| J[Stays unmerged]
+  I -->|yes| K[Merge]
 ```
 
 ## Standing rules
@@ -38,8 +41,11 @@
 | Replit | Replit may prototype or verify assigned work; it is outside the GitBook → GitHub push path. |
 | Push authority | Father alone pushes GitBook → GitHub after Ready/yes. |
 | Merge authority | Origin merges need Father's separate explicit `merge`. |
-| Tessera identity | Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen. |
 | Private docs repo | `vitalitychems-dot/Gitbook`. |
+| Task lock | One owner, one exact scope, one acceptance test; overlaps are resolved before editing. |
+| Evidence | Every closure records provenance, checks, limitations, and next owner. |
+| Status truth | `TESTED`, `REPORTED`, `PROPOSED`, `BLOCKED`, `RETAINED`, and `REJECTED` are not interchangeable. |
+| Tessera identity | Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen. |
 
 ## Lane boundaries
 
@@ -50,6 +56,7 @@
 - **Mesh Cloud** — mesh connectivity, active lanes, and cross-agent blockers.
 - **Build** — verify-only; report TESTED versus REPORTED.
 - **Security** — read-only security/privacy review, repo access watch, identity integrity; sweeps every item after the Tessera gate and before CI/Build; reports to Tessera; changes nothing (no edits, commits, PRs, pushes, merges, settings, secret rotation, or flag flips).
+- **All lanes** — declare skills used, use the handoff packet, and check in at claim, blocker, candidate result, and closure.
 - **Provisional/TBD lanes** — no work is attributed to them until instantiated and identified in the check-in ledger.
 
 ## Related pages
@@ -58,4 +65,7 @@
 - [Mesh lane map](roles/mesh-lane-map.md)
 - [Command center](../history/coordination/command-center.md)
 - [How to submit](../intake/how-to-submit.md)
+- [Collaboration playbook](COLLABORATION-PLAYBOOK.md)
+- [Agent skill matrix](AGENT-SKILL-MATRIX.md)
+- [Collaboration metrics](COLLABORATION-METRICS.md)
 - [Moderator handoff](../review/moderator-handoff.md)
```

## Checks

- `git apply --check -p1` passes for the full stack on e73fb185, in order GB-015 → GB-017 → GB-016 rev 3 → GB-018 → GB-019.
- Applied-result check after the full stack: every `+` line of e73's flow.md and SUMMARY.md patch is present verbatim. The exceptions are the pipeline sentence, the diagram and the "All lanes" claim qualifier, which GB-016 rev 3 rewrites by design (see GB-016/rev3/REBASE-e73.md). GB-017 alone keeps every e73 line verbatim.
- Status front matter: flow.md and roles.md say `published`. security.md (new page) has none. No `> **Status` banners.
