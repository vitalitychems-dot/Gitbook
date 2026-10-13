# Status front-matter fix — GB-016 (15:06 CT Tessera ruling)

**Strip baseline:** `GB-016/rev3/GB-016-rev3.strip.diff`  
**New diff:** `GB-016/rev3/GB-016-rev3.diff`  
**Line counts:** strip 414 → status-fm 406

## Principle

Shipped `status:` must be true at Father push → **`published`**. No gate or Ready claims in front matter.

## Front matter now shipped

### `GB-016/rev3/proposed/mesh/flow.md`

```
---
status: published
note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
---
```
### `GB-016/rev3/proposed/mesh/roles.md`

```
---
status: published
note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
---
```
### `GB-016/rev3/proposed/mesh/roles/build.md`

```
---
status: published
---
```
### `GB-016/rev3/proposed/mesh/roles/command-center.md`

```
---
 status: published
 note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
---
```
### `GB-016/rev3/proposed/mesh/roles/gitbook-cordnation.md`

```
---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---
```
### `GB-016/rev3/proposed/mesh/roles/mesh-lane-map.md`

```
(no front matter; L13 Status stays deleted)
```
### `GB-016/rev3/proposed/mesh/roles/open-helper-agent-2.md`

```
---
status: published
---
```
### `GB-016/rev3/proposed/review/moderator-handoff.md`

```
---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---
```
### `GB-016/rev3/proposed/intake/status-definitions.md`

```
---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---
```


## Note lines dropped

- `mesh/roles/build.md` note dropped: `Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)`
- `mesh/roles/open-helper-agent-2.md` note dropped: `Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)`

## Notes

- `command-center.md` on main (beadc44) was `corrected-pending-publish`, not `published`; listed under ruling (1) but handled as (2): status → `published`, coordination note kept.
- mesh-lane-map.md: no FM; stale `**Status:**` L13 remains deleted; Instrument line kept.
- New package pages keep no status FM.

## Interdiff (strip.diff → new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-016/rev3/GB-016-rev3.strip.diff	2026-10-05 15:06:00.939361905 -0500
+++ /workspace/gitbook-cordnation/GB-016/rev3/GB-016-rev3.diff	2026-10-05 15:07:45.259335205 -0500
@@ -1,12 +1,8 @@
 diff --git a/intake/status-definitions.md b/intake/status-definitions.md
 --- a/intake/status-definitions.md
 +++ b/intake/status-definitions.md
-@@ -1,24 +1,29 @@
-----
--status: published
--note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-----
--
+@@ -5,20 +5,30 @@
+ 
  # Status definitions
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
@@ -47,7 +43,8 @@
 diff --git a/mesh/flow.md b/mesh/flow.md
 --- a/mesh/flow.md
 +++ b/mesh/flow.md
-@@ -1,20 +1,28 @@
+@@ -5,21 +5,29 @@
+ 
  # Mesh flow & standing rules
  
 -> **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection**. Replit is not in the push path. A separate explicit `merge` is still required for Origin merges.
@@ -82,7 +79,7 @@
    F --> G{Father explicit merge?}
    G -->|no| H[Stays unmerged]
    G -->|yes| I[Merge]
-@@ -29,18 +37,22 @@
+@@ -34,18 +42,22 @@
  | Crypto / money / store | Out of scope for the current consolidation. |
  | Uncensoring / surveillance | No uncensoring tools. No surveillance of real people. |
  | Coordination board | **One board only:** GitHub `vitalitychems-dot/tessera-coordination` issue **#4**. |
@@ -113,12 +110,13 @@
 diff --git a/mesh/roles/build.md b/mesh/roles/build.md
 --- a/mesh/roles/build.md
 +++ b/mesh/roles/build.md
-@@ -1,15 +1,7 @@
-----
+@@ -1,15 +1,11 @@
+ ---
 -status: approved
 -note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)
-----
--
++status: published
+ ---
+ 
  # Build
  
 -> **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
@@ -129,7 +127,7 @@
  ## Lane status
  Active. Corrected 2026-10-05: verify-only. Earlier Command Center provisional Replit assignment is superseded. Father said ask TESSERA first on product questions.
  
-@@ -18,7 +10,7 @@
+@@ -18,7 +14,7 @@
  - Mark TESTED only from output Build ran itself; otherwise REPORTED.
  
  ## Does not do
@@ -141,12 +139,13 @@
 diff --git a/mesh/roles/command-center.md b/mesh/roles/command-center.md
 --- a/mesh/roles/command-center.md
 +++ b/mesh/roles/command-center.md
-@@ -1,32 +1,38 @@
-----
+@@ -1,32 +1,43 @@
+ ---
 - status: corrected-pending-publish
-- note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
-----
--
++ status: published
+  note: Command Center coordinates only; Father is sole GitBook → GitHub push authority.
+ ---
+ 
  # Command Center
  
 -> **Status: corrected — pending Gitbook publication**
@@ -195,12 +194,8 @@
 diff --git a/mesh/roles/gitbook-cordnation.md b/mesh/roles/gitbook-cordnation.md
 --- a/mesh/roles/gitbook-cordnation.md
 +++ b/mesh/roles/gitbook-cordnation.md
-@@ -1,12 +1,5 @@
-----
--status: published
--note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-----
--
+@@ -5,8 +5,6 @@
+ 
  # Gitbook / Cordnation
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
@@ -208,7 +203,7 @@
  ## Lane status
  
  Active.
-@@ -14,8 +7,9 @@
+@@ -14,8 +12,9 @@
  ## Owns
  
  - GitBook **intake & organization**
@@ -219,7 +214,7 @@
  - Keeps the review record
  
  ## Does not do
-@@ -26,12 +20,14 @@
+@@ -26,12 +25,14 @@
  - Pushes
  - Merges
  - Flag changes (`TESSERA_ENABLE_*` stay `0`)
@@ -315,12 +310,13 @@
 diff --git a/mesh/roles/open-helper-agent-2.md b/mesh/roles/open-helper-agent-2.md
 --- a/mesh/roles/open-helper-agent-2.md
 +++ b/mesh/roles/open-helper-agent-2.md
-@@ -1,15 +1,7 @@
-----
+@@ -1,15 +1,11 @@
+ ---
 -status: approved
 -note: Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)
-----
--
++status: published
+ ---
+ 
  # Open Helper Agent 2 (floating helper lane)
  
 -> **Status: Ready — awaiting Father GitHub push (Father Yes 2026-10-05; testers WAIVED / not checked)**
@@ -331,7 +327,7 @@
  **Status:** draft for GitBook intake. Not canon until Moderator pass and Father's yes.
  
  ## What this lane owns
-@@ -21,7 +13,8 @@
+@@ -21,7 +17,8 @@
  
  ## What this lane does not do
  
@@ -344,7 +340,7 @@
 diff --git a/mesh/roles.md b/mesh/roles.md
 --- a/mesh/roles.md
 +++ b/mesh/roles.md
-@@ -4,9 +4,9 @@
+@@ -9,9 +9,9 @@
  
  | Agent / lane | Slug | Status | One-line |
  |--------------|------|--------|----------|
@@ -356,7 +352,7 @@
  | TESSERA | [tessera](roles/tessera.md) | **Active** | Build lane: code builds and branches |
  | Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
  | Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
-@@ -21,9 +21,9 @@
+@@ -26,9 +26,9 @@
  
  ## Authority and publication path
  
@@ -371,12 +367,8 @@
 diff --git a/review/moderator-handoff.md b/review/moderator-handoff.md
 --- a/review/moderator-handoff.md
 +++ b/review/moderator-handoff.md
-@@ -1,12 +1,5 @@
-----
--status: published
--note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-----
--
+@@ -5,8 +5,6 @@
+ 
  # Moderator handoff
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
@@ -384,7 +376,7 @@
  When **Gitbook / Cordnation** marks an item ready, it hands the item to **Gitbook Moderator**. Moderator is the review gate before anything reaches GitHub / Origin.
  
  ## What "ready" means
-@@ -30,21 +23,23 @@
+@@ -30,21 +28,23 @@
  - [ ] Sources and license noted (license may be `TBD`)
  - [ ] Decision: **approve**, **reject**, or **block**
  - [ ] Decision recorded; Git
```
