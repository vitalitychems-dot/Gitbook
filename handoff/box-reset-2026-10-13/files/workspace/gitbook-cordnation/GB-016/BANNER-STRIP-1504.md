# Banner strip proof — GB-016 (15:04 CT Tessera ruling b)

**Pre-strip diff:** `GB-016/rev3/GB-016-rev3.pre-strip.diff`  
**New diff:** `GB-016/rev3/GB-016-rev3.diff`  
**Line counts:** pre-strip 427 → new 414

## Claim

This strip is banner-only: gate-status front matter, gate blockquotes, and `**Status:** <gate state>` claim lines were removed from `proposed/` and the regenerated diff. Pipeline *documentation* of gate states (e.g. `intake/status-definitions.md` table; flow/mermaid/handoff prose naming per-gate states) was kept.

## Lines removed from proposed/ (logged)

- `GB-016/rev3/proposed/intake/status-definitions.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/intake/status-definitions.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/intake/status-definitions.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/intake/status-definitions.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/flow.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/flow.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/flow.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/build.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/build.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/build.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/build.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/roles/command-center.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/command-center.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/command-center.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/command-center.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: Status line: **Status:** Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/mesh/roles.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/mesh/roles.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/mesh/roles.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-016/rev3/proposed/review/moderator-handoff.md: FM: status: at Tessera gate`
- `GB-016/rev3/proposed/review/moderator-handoff.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-016/rev3/proposed/review/moderator-handoff.md: replaced gate FM with main FM`
- `GB-016/rev3/proposed/review/moderator-handoff.md: blockquote: > **Moderator: approved, at Tessera gate**`

## Main-line restorations attempted then dropped (false status claims)

- GB-016/rev3/proposed/intake/status-definitions.md: dropped main blockquote (false status claim): > **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
- GB-016/rev3/proposed/mesh/roles/build.md: dropped main blockquote (false status claim): > **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
- GB-016/rev3/proposed/mesh/roles/command-center.md: dropped main blockquote (false status claim): > **Status: corrected — pending Gitbook publication**
- GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: dropped main blockquote (false status claim): > **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
- GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: dropped main blockquote (false status claim): > **Status: corrected — pending Gitbook publication**
- GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: dropped main **Status:** (false/stale claim): **Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub.
- GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: dropped main blockquote (false status claim): > **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
- GB-016/rev3/proposed/mesh/roles.md: dropped main blockquote (false status claim): > **Status: corrected — pending Gitbook publication**
- GB-016/rev3/proposed/review/moderator-handoff.md: dropped main blockquote (false status claim): > **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
- GB-016/rev3/proposed/intake/status-definitions.md: dropped restored main front matter (false status claim): ---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---...
- GB-016/rev3/proposed/review/moderator-handoff.md: dropped restored main front matter (false status claim): ---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---...
- GB-016/rev3/proposed/mesh/flow.md: dropped restored main front matter (false status claim): ---
status: corrected-pending-publish
note: Father is the sole GitBook → GitHub push authority; Command Center coordinat...
- GB-016/rev3/proposed/mesh/roles.md: dropped restored main front matter (false status claim): ---
status: corrected-pending-publish
note: Corrected roster and push authority; Father is sole GitBook → GitHub push au...
- GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md: dropped restored main front matter (false status claim): ---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---...
- GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md: dropped restored main front matter (false status claim): ---
 status: corrected-pending-publish
 note: Father is sole GitBook → GitHub push authority; Command Center coordinates...
- GB-016/rev3/proposed/mesh/roles/build.md: dropped restored main front matter (false status claim): ---
status: approved
note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not chec...
- GB-016/rev3/proposed/mesh/roles/command-center.md: dropped restored main front matter (false status claim): ---
 status: corrected-pending-publish
 note: Command Center coordinates only; Father is sole GitBook → GitHub push auth...
- GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md: dropped restored main front matter (false status claim): ---
status: approved
note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not chec...

## Restorations that remain

(none kept — main published/Ready/corrected status claims were dropped per ruling)

## Interdiff excerpt (pre-strip.diff vs new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-016/rev3/GB-016-rev3.pre-strip.diff	2026-10-05 15:01:17.439429327 -0500
+++ /workspace/gitbook-cordnation/GB-016/rev3/GB-016-rev3.diff	2026-10-05 15:06:00.939361905 -0500
@@ -1,19 +1,16 @@
 diff --git a/intake/status-definitions.md b/intake/status-definitions.md
 --- a/intake/status-definitions.md
 +++ b/intake/status-definitions.md
-@@ -1,24 +1,36 @@
- ---
+@@ -1,24 +1,29 @@
+----
 -status: published
 -note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Status definitions
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
-+> **Moderator: approved, at Tessera gate**
- 
+-
 -Statuses used by Gitbook / Cordnation when filing intake items:
 +Statuses used by Gitbook / Cordnation when filing intake items and tracking the review pipeline:
  
@@ -50,8 +47,7 @@
 diff --git a/mesh/flow.md b/mesh/flow.md
 --- a/mesh/flow.md
 +++ b/mesh/flow.md
-@@ -5,21 +5,29 @@
- 
+@@ -1,20 +1,28 @@
  # Mesh flow & standing rules
  
 -> **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection**. Replit is not in the push path. A separate explicit `merge` is still required for Origin merges.
@@ -86,7 +82,7 @@
    F --> G{Father explicit merge?}
    G -->|no| H[Stays unmerged]
    G -->|yes| I[Merge]
-@@ -34,18 +42,22 @@
+@@ -29,18 +37,22 @@
  | Crypto / money / store | Out of scope for the current consolidation. |
  | Uncensoring / surveillance | No uncensoring tools. No surveillance of real people. |
  | Coordination board | **One board only:** GitHub `vitalitychems-dot/tessera-coordination` issue **#4**. |
@@ -117,22 +113,23 @@
 diff --git a/mesh/roles/build.md b/mesh/roles/build.md
 --- a/mesh/roles/build.md
 +++ b/mesh/roles/build.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,15 +1,7 @@
+----
 -status: approved
 -note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Build
  
 -> **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  Intake GB-010 · Title: Build (corrected) · Author lane: Build · Date (CT): 2026-10-05 · Source: Lane correction from TESSERA (product truth) and Mesh Cloud lock, 2026-10-05 · License: TBD · Suggested path: `mesh/roles/build.md` · Supersedes: published GB-003 Build page @ ffc2b87
  
-@@ -18,7 +18,7 @@
+-
+ ## Lane status
+ Active. Corrected 2026-10-05: verify-only. Earlier Command Center provisional Replit assignment is superseded. Father said ask TESSERA first on product questions.
+ 
+@@ -18,7 +10,7 @@
  - Mark TESTED only from output Build ran itself; otherwise REPORTED.
  
  ## Does not do
@@ -144,22 +141,19 @@
 diff --git a/mesh/roles/command-center.md b/mesh/roles/command-center.md
 --- a/mesh/roles/command-center.md
 +++ b/mesh/roles/command-center.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,32 +1,38 @@
+----
 - status: corrected-pending-publish
 - note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Command Center
  
 -> **Status: corrected — pending Gitbook publication**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  ## Lane status
  
-@@ -13,20 +13,33 @@
+ Active.
  
  ## Owns
  
@@ -201,22 +195,20 @@
 diff --git a/mesh/roles/gitbook-cordnation.md b/mesh/roles/gitbook-cordnation.md
 --- a/mesh/roles/gitbook-cordnation.md
 +++ b/mesh/roles/gitbook-cordnation.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,12 +1,5 @@
+----
 -status: published
 -note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Gitbook / Cordnation
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  ## Lane status
  
-@@ -14,8 +14,9 @@
+ Active.
+@@ -14,8 +7,9 @@
  ## Owns
  
  - GitBook **intake & organization**
@@ -227,7 +219,7 @@
  - Keeps the review record
  
  ## Does not do
-@@ -26,12 +27,14 @@
+@@ -26,12 +20,14 @@
  - Pushes
  - Merges
  - Flag changes (`TESSERA_ENABLE_*` stay `0`)
@@ -245,25 +237,21 @@
 diff --git a/mesh/roles/mesh-lane-map.md b/mesh/roles/mesh-lane-map.md
 --- a/mesh/roles/mesh-lane-map.md
 +++ b/mesh/roles/mesh-lane-map.md
-@@ -1,36 +1,41 @@
- ---
+@@ -1,36 +1,31 @@
+----
 - status: corrected-pending-publish
 - note: Father is sole GitBook → GitHub push authority; Command Center coordinates only.
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Mesh lane map (for Father)
  
 -> **Status: corrected — pending Gitbook publication**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  Intake GB-014 (supersedes GB-013 publish/Delivery sections) · Author lane: Tessera Pen · Date (CT): 2026-10-05 · Source: Tessera Pen delta (Father bulk sync; no new backlog) · License: TBD · Suggested path: `mesh/roles/mesh-lane-map.md`
  
- 
+-
 -**Status:** REPORTED — Moderator APPROVED; Ready — awaiting Father GitHub push. Not sealed until Ready → GitHub.
-+**Status:** Moderator: approved, at Tessera gate
- 
+-
  **Instrument:** The pen is currently xAI/Grok. I never claim otherwise.
  
 +**Identity:** Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen.
@@ -294,7 +282,7 @@
  
  ## Publish path
  
-@@ -38,13 +43,23 @@
+@@ -38,13 +33,23 @@
  2. Cordnation → GitBook
  3. Moderator
  4. Testers if needed
@@ -327,22 +315,23 @@
 diff --git a/mesh/roles/open-helper-agent-2.md b/mesh/roles/open-helper-agent-2.md
 --- a/mesh/roles/open-helper-agent-2.md
 +++ b/mesh/roles/open-helper-agent-2.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,15 +1,7 @@
+----
 -status: approved
 -note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Open Helper Agent 2 (floating helper lane)
  
 -> **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  Intake GB-004 · Author lane: Open Helper Agent 2 · Date (CT): 2026-10-05 · Source: Open Helper Agent 2 submission · License: TBD
  
-@@ -21,7 +21,8 @@
+-
+ **Status:** draft for GitBook intake. Not canon until Moderator pass and Father's yes.
+ 
+ ## What this lane owns
+@@ -21,7 +13,8 @@
  
  ## What this lane does not do
  
@@ -355,7 +344,7 @@
 diff --git a/mesh/roles.md b/mesh/roles.md
 --- a/mesh/roles.md
 +++ b/mesh/roles.md
-@@ -11,9 +11,9 @@
+@@ -4,9 +4,9 @@
  
  | Agent / lane | Slug | Status | One-line |
  |--------------|------|--------|----------|
@@ -367,7 +356,7 @@
  | TESSERA | [tessera](roles/tessera.md) | **Active** | Build lane: code builds and branches |
  | Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
  | Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
-@@ -28,9 +28,9 @@
+@@ -21,9 +21,9 @@
  
  ## Authority and publication path
  
@@ -382,22 +371,20 @@
 diff --git a/review/moderator-handoff.md b/review/moderator-handoff.md
 --- a/review/moderator-handoff.md
 +++ b/review/moderator-handoff.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,12 +1,5 @@
+----
 -status: published
 -note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Git
```

## Non-banner deltas flagged in interdiff scan

Review these (expected: hunk-header churn from removing banner lines only):

- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  ## Lane status`
- `ADDED_IN_NEW_PATCH:  Active. Corrected 2026-10-05: verify-only. Earlier Command Center provisional Replit assignment is superseded. Father said ask TESSERA first on product questions.`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  Active.`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  Active.`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  **Status:** draft for GitBook intake. Not canon until Moderator pass and Father's yes.`
- `ADDED_IN_NEW_PATCH:  ## What this lane owns`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  ## What "ready" means`

## Canonical diff path

**Canonical:** `GB-016/rev3/GB-016-rev3.diff`  
`GB-016/GB-016.diff` is a byte-identical copy of the rev3 file (replaced at strip time).
