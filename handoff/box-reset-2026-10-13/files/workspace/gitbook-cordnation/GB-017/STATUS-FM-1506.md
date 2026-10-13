# Status front-matter fix — GB-017 (15:06 CT Tessera ruling)

**Strip baseline:** `GB-017/GB-017.strip.diff`  
**New diff:** `GB-017/GB-017.diff`  
**Line counts:** strip 181 → status-fm 180

## Principle

Shipped `status:` must be true at Father push → **`published`**. No gate or Ready claims in front matter.

## Front matter now shipped

### `GB-017/proposed/mesh/flow.md`

```
---
status: published
note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
---
```
### `GB-017/proposed/mesh/roles.md`

```
---
status: published
note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
---
```
### `GB-017/proposed/mesh/roles/security.md`

```
(no front matter — new page)
```
### `GB-017/proposed/mesh/roles/tessera-pen.md`

```
(no front matter — new page)
```


## Note lines dropped

(none for this package)

## Notes

- `command-center.md` on main (beadc44) was `corrected-pending-publish`, not `published`; listed under ruling (1) but handled as (2): status → `published`, coordination note kept.
- mesh-lane-map.md: no FM; stale `**Status:**` L13 remains deleted; Instrument line kept.
- New package pages keep no status FM.

## Interdiff (strip.diff → new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-017/GB-017.strip.diff	2026-10-05 15:05:49.695364733 -0500
+++ /workspace/gitbook-cordnation/GB-017/GB-017.diff	2026-10-05 15:07:35.663337694 -0500
@@ -13,16 +13,14 @@
 diff --git a/mesh/flow.md b/mesh/flow.md
 --- a/mesh/flow.md
 +++ b/mesh/flow.md
-@@ -1,8 +1,3 @@
-----
+@@ -1,5 +1,5 @@
+ ---
 -status: corrected-pending-publish
--note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
-----
--
- # Mesh flow & standing rules
++status: published
+ note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
+ ---
  
- > **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection**. Replit is not in the push path. A separate explicit `merge` is still required for Origin merges.
-@@ -38,6 +33,7 @@
+@@ -38,6 +38,7 @@
  | Replit | Replit may prototype or verify assigned work; it is outside the GitBook → GitHub push path. |
  | Push authority | Father alone pushes GitBook → GitHub after Ready/yes. |
  | Merge authority | Origin merges need Father's separate explicit `merge`. |
@@ -30,7 +28,7 @@
  | Private docs repo | `vitalitychems-dot/Gitbook`. |
  
  ## Lane boundaries
-@@ -48,6 +44,7 @@
+@@ -48,6 +49,7 @@
  - **TESSERA** — code builds and branches.
  - **Mesh Cloud** — mesh connectivity, active lanes, and cross-agent blockers.
  - **Build** — verify-only; report TESTED versus REPORTED.
@@ -142,12 +140,13 @@
 diff --git a/mesh/roles.md b/mesh/roles.md
 --- a/mesh/roles.md
 +++ b/mesh/roles.md
-@@ -1,12 +1,5 @@
-----
+@@ -1,12 +1,10 @@
+ ---
 -status: corrected-pending-publish
--note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
-----
--
++status: published
+ note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
+ ---
+ 
  # Roles overview
  
 -> **Status: corrected — pending Gitbook publication**
@@ -155,7 +154,7 @@
  Canonical list of mesh agents and lanes. Active means the lane is currently instantiated and running. Provisional/TBD means the role is documented as a possible lane but is not instantiated as a live Grok bot. Do not invent duties beyond what is listed on each role page.
  
  | Agent / lane | Slug | Status | One-line |
-@@ -18,12 +11,13 @@
+@@ -18,12 +16,13 @@
  | Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
  | Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
  | Github Scraper | [github-scraper](roles/github-scraper.md) | **Provisional / not instantiated** | Repository scrapes; issue/PR status |
@@ -171,7 +170,7 @@
  
  ## Authority and publication path
  
-@@ -34,6 +28,7 @@
+@@ -34,6 +33,7 @@
  ## Notes
  
  - Father = Collin Keane. Agents address him as "Father".

```
