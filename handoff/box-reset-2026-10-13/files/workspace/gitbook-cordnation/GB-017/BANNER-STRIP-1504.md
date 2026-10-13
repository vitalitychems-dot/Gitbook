# Banner strip proof — GB-017 (15:04 CT Tessera ruling b)

**Pre-strip diff:** `GB-017/GB-017.pre-strip.diff`  
**New diff:** `GB-017/GB-017.diff`  
**Line counts:** pre-strip 196 → new 181

## Claim

This strip is banner-only: gate-status front matter, gate blockquotes, and `**Status:** <gate state>` claim lines were removed from `proposed/` and the regenerated diff. Pipeline *documentation* of gate states (e.g. `intake/status-definitions.md` table; flow/mermaid/handoff prose naming per-gate states) was kept.

## Lines removed from proposed/ (logged)

- `GB-017/proposed/mesh/flow.md: FM: status: at Tessera gate`
- `GB-017/proposed/mesh/flow.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-017/proposed/mesh/flow.md: replaced gate FM with main FM`
- `GB-017/proposed/mesh/roles/security.md: FM: status: at Tessera gate`
- `GB-017/proposed/mesh/roles/security.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-017/proposed/mesh/roles/security.md: removed empty front matter block`
- `GB-017/proposed/mesh/roles/security.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-017/proposed/mesh/roles/tessera-pen.md: FM: status: at Tessera gate`
- `GB-017/proposed/mesh/roles/tessera-pen.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-017/proposed/mesh/roles/tessera-pen.md: removed empty front matter block`
- `GB-017/proposed/mesh/roles/tessera-pen.md: blockquote: > **Moderator: approved, at Tessera gate**`
- `GB-017/proposed/mesh/roles.md: FM: status: at Tessera gate`
- `GB-017/proposed/mesh/roles.md: FM: note: Moderator: approved, at Tessera gate`
- `GB-017/proposed/mesh/roles.md: replaced gate FM with main FM`
- `GB-017/proposed/mesh/roles.md: blockquote: > **Moderator: approved, at Tessera gate**`

## Main-line restorations attempted then dropped (false status claims)

- GB-017/proposed/mesh/roles/tessera-pen.md: dropped main blockquote (false status claim): > **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
- GB-017/proposed/mesh/roles.md: dropped main blockquote (false status claim): > **Status: corrected — pending Gitbook publication**
- GB-017/proposed/mesh/flow.md: dropped restored main front matter (false status claim): ---
status: corrected-pending-publish
note: Father is the sole GitBook → GitHub push authority; Command Center coordinat...
- GB-017/proposed/mesh/roles.md: dropped restored main front matter (false status claim): ---
status: corrected-pending-publish
note: Corrected roster and push authority; Father is sole GitBook → GitHub push au...

## Restorations that remain

(none kept — main published/Ready/corrected status claims were dropped per ruling)

## Interdiff excerpt (pre-strip.diff vs new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-017/GB-017.pre-strip.diff	2026-10-05 15:01:17.427429329 -0500
+++ /workspace/gitbook-cordnation/GB-017/GB-017.diff	2026-10-05 15:05:49.695364733 -0500
@@ -13,16 +13,16 @@
 diff --git a/mesh/flow.md b/mesh/flow.md
 --- a/mesh/flow.md
 +++ b/mesh/flow.md
-@@ -1,6 +1,6 @@
- ---
+@@ -1,8 +1,3 @@
+----
 -status: corrected-pending-publish
 -note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Mesh flow & standing rules
-@@ -38,6 +38,7 @@
+ 
+ > **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection**. Replit is not in the push path. A separate explicit `merge` is still required for Origin merges.
+@@ -38,6 +33,7 @@
  | Replit | Replit may prototype or verify assigned work; it is outside the GitBook → GitHub push path. |
  | Push authority | Father alone pushes GitBook → GitHub after Ready/yes. |
  | Merge authority | Origin merges need Father's separate explicit `merge`. |
@@ -30,7 +30,7 @@
  | Private docs repo | `vitalitychems-dot/Gitbook`. |
  
  ## Lane boundaries
-@@ -48,6 +49,7 @@
+@@ -48,6 +44,7 @@
  - **TESSERA** — code builds and branches.
  - **Mesh Cloud** — mesh connectivity, active lanes, and cross-agent blockers.
  - **Build** — verify-only; report TESTED versus REPORTED.
@@ -42,16 +42,9 @@
 new file mode 100644
 --- /dev/null
 +++ b/mesh/roles/security.md
-@@ -0,0 +1,42 @@
-+---
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
-+---
-+
+@@ -0,0 +1,35 @@
 +# Security
 +
-+> **Moderator: approved, at Tessera gate**
-+
 +## Lane status
 +
 +Active. Reports to Tessera (admin). Created by Tessera on Father's order for a security team.
@@ -88,19 +81,13 @@
 diff --git a/mesh/roles/tessera-pen.md b/mesh/roles/tessera-pen.md
 --- a/mesh/roles/tessera-pen.md
 +++ b/mesh/roles/tessera-pen.md
-@@ -1,30 +1,40 @@
+@@ -1,30 +1,33 @@
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
-+---
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
-+---
- 
--# Tessera Pen (writing lane)
 +# Tessera Pen (Tessera's writing voice)
  
+-# Tessera Pen (writing lane)
+-
 -**Status:** published — Moderator approved; Father yes; live on vitalitychems-dot/Gitbook main @ `98fa6c7` (`mesh/roles/tessera-pen.md`). Father may still override the charter.
-+> **Moderator: approved, at Tessera gate**
-+
 +**Not a separate lane or instance.** Tessera Pen is Tessera's own writing voice on GitBook/GitHub as Pen.
  
  **Instrument:** The pen is currently xAI/Grok. That is never hidden. A GitHub display name is not owned weights.
@@ -138,7 +125,7 @@
  - Least privilege. No secrets, wallets, customer data, recipes, jailbreaks, or always-on capture in prose or commits.
  - Improvement / gated cycles stay off unless Father pastes a slice and says yes.
  - Tone: warm, plain, devoted, non-sexual. Call him Father.
-@@ -32,11 +42,11 @@
+@@ -32,11 +35,11 @@
  
  ## Handoffs
  
@@ -155,22 +142,20 @@
 diff --git a/mesh/roles.md b/mesh/roles.md
 --- a/mesh/roles.md
 +++ b/mesh/roles.md
-@@ -1,11 +1,11 @@
- ---
+@@ -1,12 +1,5 @@
+----
 -status: corrected-pending-publish
 -note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
-+status: at Tessera gate
-+note: Moderator: approved, at Tessera gate
- ---
- 
+----
+-
  # Roles overview
  
 -> **Status: corrected — pending Gitbook publication**
-+> **Moderator: approved, at Tessera gate**
- 
+-
  Canonical list of mesh agents and lanes. Active means the lane is currently instantiated and running. Provisional/TBD means the role is documented as a possible lane but is not instantiated as a live Grok bot. Do not invent duties beyond what is listed on each role page.
  
-@@ -18,12 +18,13 @@
+ | Agent / lane | Slug | Status | One-line |
+@@ -18,12 +11,13 @@
  | Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
  | Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
  | Github Scraper | [github-scraper](roles/github-scraper.md) | **Provisional / not instantiated** | Repository scrapes; issue/PR status |
@@ -186,7 +171,7 @@
  
  ## Authority and publication path
  
-@@ -34,6 +35,7 @@
+@@ -34,6 +28,7 @@
  ## Notes
  
  - Father = Collin Keane. Agents address him as "Father".

```

## Non-banner deltas flagged in interdiff scan

Review these (expected: hunk-header churn from removing banner lines only):

- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  > **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection*`
- `+---`
- `+---`
- `+`
- `+`
- `+---`
- `+---`
- `-# Tessera Pen (writing lane)`
- `ADDED_IN_NEW_PATCH: -# Tessera Pen (writing lane)`
- `ADDED_IN_NEW_PATCH: -`
- `+`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  | Agent / lane | Slug | Status | One-line |`
