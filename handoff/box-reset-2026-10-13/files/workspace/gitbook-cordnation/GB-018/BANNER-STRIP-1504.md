# Banner strip proof — GB-018 (15:04 CT Tessera ruling b)

**Pre-strip diff:** `GB-018/GB-018.pre-strip.diff`  
**New diff:** `GB-018/GB-018.diff`  
**Line counts:** pre-strip 120 → new 130

## Claim

This strip is banner-only: gate-status front matter, gate blockquotes, and `**Status:** <gate state>` claim lines were removed from `proposed/` and the regenerated diff. Pipeline *documentation* of gate states (e.g. `intake/status-definitions.md` table; flow/mermaid/handoff prose naming per-gate states) was kept.

## Lines removed from proposed/ (logged)

- `GB-018/proposed/merge/hyb-005-braces-decision.md: FM: status: at Security gate`
- `GB-018/proposed/merge/hyb-005-braces-decision.md: FM: note: Tessera: approved, at Security gate`
- `GB-018/proposed/merge/hyb-005-braces-decision.md: removed empty front matter block`
- `GB-018/proposed/merge/hyb-005-braces-decision.md: blockquote: > **Tessera: approved, at Security gate**`

## Main-line restorations attempted then dropped (false status claims)

(none)

## Restorations that remain

(none kept — main published/Ready/corrected status claims were dropped per ruling)

## Interdiff excerpt (pre-strip.diff vs new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-018/GB-018.pre-strip.diff	2026-10-05 15:01:17.443429326 -0500
+++ /workspace/gitbook-cordnation/GB-018/GB-018.diff	2026-10-05 15:05:49.711364728 -0500
@@ -12,7 +12,15 @@
 diff --git a/history/coordination/agent-checkins.md b/history/coordination/agent-checkins.md
 --- a/history/coordination/agent-checkins.md
 +++ b/history/coordination/agent-checkins.md
-@@ -51,6 +51,7 @@
+@@ -27,7 +27,6 @@
+ BLOCKER: local Replit worktree is a partial snapshot, not canonical TESSERA main; shell access to private remote timed out; cannot safely branch or run required tests
+ ```
+ 
+-
+ ## HYB-012 — blocker evidence
+ 
+ ```text
+@@ -51,6 +50,7 @@
  | HYB-002 | Manus consolidation | exact tracked-file coverage | deletion set confirmed and verified | GitHub inventory verified | 2026-10-05 |
  | HYB-003 | Manus consolidation | `216e4e8` | `fec56eb` | typecheck, tests, build | 2026-10-05 |
  | HYB-004 | Manus consolidation | source repositories | `54839dc` Gitbook record | Gitbook navigation and provenance records published | 2026-10-05 |
@@ -20,7 +28,7 @@
  | HYB-006 | Grok Bot (historical-analysis collaborator) | TESSERA `fec56eb`; Grok-ready `9e3fbca` | `991d3b8` | GitHub tree diff 1275 common / 16 content-diff; no installs; no 1T inspection | 2026-10-05 |
  | HYB-007 | Grok Bot (historical-analysis collaborator) | TESSERA `fec56eb`; Zz `150d4ec` | `e2f1e20` | z-app behavior matrix; no TESSERA code; no 1T inspection | 2026-10-05 |
  
-@@ -86,6 +87,32 @@
+@@ -86,6 +86,32 @@
  - A task is not DONE without a commit, checks, and a source/provenance note.
  - Historical text is evidence until a moderator promotes it into an approved task.
  
@@ -53,6 +61,14 @@
  ## HYB-006 — claim and completion
  
  Claim (IN REVIEW), then close (DONE). Analysis is published as a candidate result; Moderator/Father seal is still outstanding. No TESSERA code was edited and `1T` was not inspected.
+@@ -152,7 +178,6 @@
+ FOLLOW-UP: HYB-008, HYB-009, HYB-011, HYB-013, HYB-014
+ ```
+ 
+-
+ <!-- replit-hyb012-static-verification-2026-10-05 -->
+ ## HYB-012 — Replit canonical source verification (2026-10-05T19:48:23.092Z)
+ 
 diff --git a/intake/HYBRID-CONSOLIDATION-BACKLOG.md b/intake/HYBRID-CONSOLIDATION-BACKLOG.md
 --- a/intake/HYBRID-CONSOLIDATION-BACKLOG.md
 +++ b/intake/HYBRID-CONSOLIDATION-BACKLOG.md
@@ -69,13 +85,7 @@
 new file mode 100644
 --- /dev/null
 +++ b/merge/hyb-005-braces-decision.md
-@@ -0,0 +1,48 @@
-+---
-+status: at Security gate
-+note: Tessera: approved, at Security gate
-+---
-+
-+> **Tessera: approved, at Security gate**
+@@ -0,0 +1,42 @@
 +
 +# HYB-005 — braces GHSA-vfj7-8cjw-p6xm decision
 +

```

## Non-banner deltas flagged in interdiff scan

Review these (expected: hunk-header churn from removing banner lines only):

- `ADDED_IN_NEW_PATCH:  BLOCKER: local Replit worktree is a partial snapshot, not canonical TESSERA main; shell access to private remote timed out; cannot safely branch or run required tests`
- `ADDED_IN_NEW_PATCH:  ````
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  ## HYB-012 — blocker evidence`
- `ADDED_IN_NEW_PATCH:  ```text`
- `ADDED_IN_NEW_PATCH:  FOLLOW-UP: HYB-008, HYB-009, HYB-011, HYB-013, HYB-014`
- `ADDED_IN_NEW_PATCH:  ````
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH:  <!-- replit-hyb012-static-verification-2026-10-05 -->`
- `ADDED_IN_NEW_PATCH:  ## HYB-012 — Replit canonical source verification (2026-10-05T19:48:23.092Z)`
- `+---`
- `+---`
- `+`
