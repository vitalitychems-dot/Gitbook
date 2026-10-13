> **Superseded diff:** after Tessera's 15:20 CT rulings, `GB-016-rev3.diff` is now the 1e3bb50 version (see REBASE-1e3.md). The e73 diff described here is kept as `GB-016-rev3.e73.diff` (sha256 `155ba93b…`).

# GB-016 rev 3 rebase onto e73fb185 (Tessera ruling (a), 15:18 CT)

- **Overlap check:** main is `e73fb185321fcb9e65eb61641ec8745bac85791d` and there are 0 open PRs (checked ~15:18 CT).
- **Stacking:** applies after the rebased GB-017 (never alone).
- **Old diff:** kept as `GB-016-rev3.beadc44.diff`, sha256 `baad1a3c…` (byte-identical to the frozen file). FROZEN-SHA256-status.txt is untouched.
  - **Note:** `GB-016/GB-016.diff` (top level) is also still the beadc44 copy (same hash `baad1a3c…`). Do **not** use it; the e73 diff is `GB-016/rev3/GB-016-rev3.diff`.
- **New diff:** `GB-016-rev3.diff`, 420 lines, sha256 `155ba93b2ddc98f5e4ab45b46c69bc3667d62f72234518eac097cb29cdba491e`.
  - The sections for the other 8 files are **byte-identical** to the beadc44 diff. Their results are also identical (same blob hashes): status-definitions.md, roles.md, build.md, command-center.md, gitbook-cordnation.md, mesh-lane-map.md, open-helper-agent-2.md, moderator-handoff.md.
  - Only the `mesh/flow.md` section was content-rebased.
- **Copies:** `base-e73/` (base = e73 + GB-015 + rebased GB-017) and `proposed-e73/`.

## Content decisions (mesh/flow.md only)

1. **Pipeline sentence:** merged with e73 and set to Father's 2:34 PM CT order:
   - discover → overlap check (main SHA plus open PRs) → Tessera assigns (an agent claims only after Tessera assigns) → produce scoped work → Cordnation intake → Moderator → Tessera → Security → CI/Build → Ready staging → CC digest → Father's final yes → Father pushes → `merge` only on Father's explicit yes.
   - e73's "claim one task" became "claims a task only after Tessera assigns it".
   - e73's "Build independently verifies" is kept as "CI/Build independently verifies", now after Security.
   - GB-016's Ready staging, per-gate state, Replit-item path, numbered digest items and bulk yes/no wording are kept verbatim.
   - "(no merge without Father's explicit yes)" was added after the existing `merge` clause.
2. **Mermaid diagram:** merged.
   - From e73: the Discover start, "Agents produce scoped work", "scope / provenance review" on the Moderator node, `needs work` → intake, Build "independent verification" (now the `CI / Build` node), `fail` → intake, and the Stays unmerged / Merge terminals.
   - New nodes for Father's order: `OC` (overlap check: main SHA + open PRs) and `AS` (Tessera assigns; claim only after assignment).
   - From GB-016: the Tessera gate (`at Tessera gate` state), Security sweep, the docs-Ready and Replit-Ready nodes, the `R0` Replit staging node (now feeding the Moderator node `D`, matching GB-016's R0 → Moderator), the numbered digest, bulk yes/no, the hold-named-items branch, and the docs and Replit push branches.
   - Node letters were reassigned. e73's single "Father Ready / yes?" became GB-016's bulk yes/no.
3. **Canonical push rule blockquote (L7):** GB-016's version, unchanged from the beadc44 diff. e73 did not touch this line. It is an existing content callout, not a gate banner.
4. **Standing rules:**
   - GB-016's Command Center, Replit and Push authority rows replace the old ones verbatim, keeping **Grok exception (3)**.
   - GB-016's Replit push set, Ready staging, Per-gate state and Digest items rows are inserted after Push authority, as before.
   - e73's Task lock / Evidence / Status truth rows and GB-017's Tessera identity row (last) are kept.
5. **Lane boundaries:**
   - GB-016's Cordnation and Command Center lines are kept verbatim.
   - e73's "All lanes" line is kept, with one qualifier: "check in at claim **(only after Tessera assigns)**", per the claim-after-assignment rule.
   - GB-017's Security line is kept.
6. **Kept verbatim from e73:** front matter (via GB-017), related links, and all other rows and lines.
7. **No gate banners.**

## Interdiff of results for mesh/flow.md (old = beadc44 + old GB-017 + old GB-016; new = e73 + new GB-017 + new GB-016)

```diff
--- old result (beadc44 + old diff)
+++ new result (e73fb185 + new diff)
@@ -9,28 +9,32 @@
 
 ## End-to-end flow
 
-Agents produce work → **Gitbook / Cordnation** intake → **Gitbook Moderator** reviews → on Moderator pass, item state becomes e.g. `Moderator: approved, at Tessera gate` → **Tessera** (admin) review → **Security** sweep (read-only) → **CI/Build** verify → after all four gates clear, **Gitbook / Cordnation** stages docs as **Ready** (waiting only on Father's final yes) (Replit items pass the same Moderator→Tessera→Security→CI/Build gates; then Command Center marks each Replit item Ready) → **Command Center** one bulk digest to Father every 30–45 min with each push as its own numbered digest item (each docs push (one per GB package) = its own numbered item; each Replit app-set push = a separate item; never bundled) → Father's bulk **yes** approves every item listed / **no** with notes holds the items he names (a yes never carries over to anything that wasn't listed) → for listed docs items, **Father** alone pushes GitBook → GitHub (Replit outside that path) → for listed Replit items, Command Center privately pushes ONLY the Replit app set → Father separately says `merge` for an Origin merge.
+Agents discover → run the overlap check (main SHA plus open PRs) → **Tessera** assigns the task (an agent claims a task only after Tessera assigns it) → produce scoped work → **Gitbook / Cordnation** intake → **Gitbook Moderator** reviews → on Moderator pass, item state becomes e.g. `Moderator: approved, at Tessera gate` → **Tessera** (admin) review → **Security** sweep (read-only) → **CI/Build** independently verifies → after all four gates clear, **Gitbook / Cordnation** stages docs as **Ready** (waiting only on Father's final yes) (Replit items pass the same Moderator→Tessera→Security→CI/Build gates; then Command Center marks each Replit item Ready) → **Command Center** one bulk digest to Father every 30–45 min with each push as its own numbered digest item (each docs push (one per GB package) = its own numbered item; each Replit app-set push = a separate item; never bundled) → Father's bulk **yes** approves every item listed / **no** with notes holds the items he names (a yes never carries over to anything that wasn't listed) → for listed docs items, **Father** alone pushes GitBook → GitHub (Replit outside that path) → for listed Replit items, Command Center privately pushes ONLY the Replit app set → Father separately says `merge` for an Origin merge (no merge without Father's explicit yes).
 
 ```mermaid
 flowchart TD
-  A[Agents produce work] --> B[GitBook intake<br/>Gitbook / Cordnation]
-  B --> C[Gitbook Moderator<br/>approve / reject]
-  C -->|approved| T[Tessera admin review<br/>state: at Tessera gate]
-  C -->|rejected| B
-  T --> SEC[Security sweep]
-  SEC --> CI[CI / Build verify]
-  CI --> S[Cordnation stages docs Ready<br/>all four gates cleared]
-  CI --> RR[CC marks Replit item Ready<br/>all four gates cleared]
-  S --> D[Command Center digest<br/>numbered items 30–45 min]
-  RR --> D
-  R0[CC stages Replit app set<br/>each push its own item] --> C
-  D --> E{Father bulk yes/no?}
-  E -->|no + notes| H0[Hold named items]
-  E -->|yes — listed docs item| F[Father pushes<br/>GitBook → GitHub<br/>Replit outside that path]
-  E -->|yes — listed Replit item| R[Command Center<br/>private push Replit app set only]
-  F --> G{Father explicit merge?}
-  G -->|no| H[Stays unmerged]
-  G -->|yes| I[Merge]
+  A[Discover] --> OC[Overlap check<br/>main SHA + open PRs]
+  OC --> AS[Tessera assigns task<br/>claim only after assignment]
+  AS --> B[Agents produce scoped work]
+  B --> C[GitBook intake<br/>Gitbook / Cordnation]
+  C --> D[Gitbook Moderator<br/>scope / provenance review]
+  R0[CC stages Replit app set<br/>each push its own item] --> D
+  D -->|approved| T[Tessera admin review<br/>state: at Tessera gate]
+  D -->|needs work| C
+  T --> SEC[Security sweep<br/>read-only]
+  SEC --> CI[CI / Build<br/>independent verification]
+  CI -->|fail| C
+  CI -->|pass: docs| S[Cordnation stages docs Ready<br/>all four gates cleared]
+  CI -->|pass: Replit| RR[CC marks Replit item Ready<br/>all four gates cleared]
+  S --> F[Command Center digest<br/>numbered items 30–45 min]
+  RR --> F
+  F --> G{Father bulk yes/no?}
+  G -->|no + notes| H0[Hold named items]
+  G -->|yes — listed docs item| H[Father pushes<br/>GitBook → GitHub<br/>Replit outside that path]
+  G -->|yes — listed Replit item| R[Command Center<br/>private push Replit app set only]
+  H --> I{Father explicit merge?}
+  I -->|no| J[Stays unmerged]
+  I -->|yes| K[Merge]
 ```
 
 ## Standing rules
@@ -50,8 +54,11 @@
 | Per-gate state | Before Ready, an item carries the gate it is at (examples: `Moderator: approved, at Tessera gate`; `at Security gate`; `at CI/Build gate`). Ready is only set after all four clear. |
 | Digest items / Father yes | Each push is its own numbered digest item (each docs push (one per GB package) = its own numbered item; each Replit app-set push = separate item; never bundled). Father's bulk **yes** approves every item listed; **no** with notes holds the items he names. A yes never carries over to anything that wasn't listed. |
 | Merge authority | Origin merges need Father's separate explicit `merge`. |
-| Tessera identity | Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen. |
 | Private docs repo | `vitalitychems-dot/Gitbook`. |
+| Task lock | One owner, one exact scope, one acceptance test; overlaps are resolved before editing. |
+| Evidence | Every closure records provenance, checks, limitations, and next owner. |
+| Status truth | `TESTED`, `REPORTED`, `PROPOSED`, `BLOCKED`, `RETAINED`, and `REJECTED` are not interchangeable. |
+| Tessera identity | Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen. |
 
 ## Lane boundaries
 
@@ -62,6 +69,7 @@
 - **Mesh Cloud** — mesh connectivity, active lanes, and cross-agent blockers.
 - **Build** — verify-only; report TESTED versus REPORTED.
 - **Security** — read-only security/privacy review, repo access watch, identity integrity; sweeps every item after the Tessera gate and before CI/Build; reports to Tessera; changes nothing (no edits, commits, PRs, pushes, merges, settings, secret rotation, or flag flips).
+- **All lanes** — declare skills used, use the handoff packet, and check in at claim (only after Tessera assigns), blocker, candidate result, and closure.
 - **Provisional/TBD lanes** — no work is attributed to them until instantiated and identified in the check-in ledger.
 
 ## Related pages
@@ -70,4 +78,7 @@
 - [Mesh lane map](roles/mesh-lane-map.md)
 - [Command center](../history/coordination/command-center.md)
 - [How to submit](../intake/how-to-submit.md)
+- [Collaboration playbook](COLLABORATION-PLAYBOOK.md)
+- [Agent skill matrix](AGENT-SKILL-MATRIX.md)
+- [Collaboration metrics](COLLABORATION-METRICS.md)
 - [Moderator handoff](../review/moderator-handoff.md)
```

## Checks

- `git apply --check -p1` passes for the full stack on e73fb185 (GB-015 → GB-017 → GB-016 rev 3 → GB-018 → GB-019).
- Applied-result check: every e73 `+` line in mesh/flow.md and SUMMARY.md is present verbatim, except the e73 pipeline sentence, 8 diagram lines and the "All lanes" line. Those were merged as listed above, and each still carries its e73 content (Discover, scoped work, Build verification, needs-work/fail loops, merge terminals, the All lanes check-in rule).
