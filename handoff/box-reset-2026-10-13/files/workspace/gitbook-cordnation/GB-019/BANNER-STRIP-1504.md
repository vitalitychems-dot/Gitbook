# Banner strip proof — GB-019 (15:04 CT Tessera ruling b)

**Pre-strip diff:** `GB-019/GB-019.pre-strip.diff`  
**New diff:** `GB-019/GB-019.diff`  
**Line counts:** pre-strip 94 → new 87

## Claim

This strip is banner-only: gate-status front matter, gate blockquotes, and `**Status:** <gate state>` claim lines were removed from `proposed/` and the regenerated diff. Pipeline *documentation* of gate states (e.g. `intake/status-definitions.md` table; flow/mermaid/handoff prose naming per-gate states) was kept.

## Lines removed from proposed/ (logged)

- `GB-019/proposed/intake/CORTICAL-LABS-READINESS.md: FM: status: at Security gate`
- `GB-019/proposed/intake/CORTICAL-LABS-READINESS.md: FM: note: Tessera: approved, at Security gate`
- `GB-019/proposed/intake/CORTICAL-LABS-READINESS.md: removed empty front matter block`
- `GB-019/proposed/intake/CORTICAL-LABS-READINESS.md: blockquote: > **Tessera: approved, at Security gate**`

## Main-line restorations attempted then dropped (false status claims)

(none)

## Restorations that remain

(none kept — main published/Ready/corrected status claims were dropped per ruling)

## Interdiff excerpt (pre-strip.diff vs new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-019/GB-019.pre-strip.diff	2026-10-05 14:58:29.347464178 -0500
+++ /workspace/gitbook-cordnation/GB-019/GB-019.diff	2026-10-05 15:06:00.943361904 -0500
@@ -2,16 +2,9 @@
 new file mode 100644
 --- /dev/null
 +++ b/intake/CORTICAL-LABS-READINESS.md
-@@ -0,0 +1,78 @@
-+---
-+status: at Security gate
-+note: Tessera: approved, at Security gate
-+---
-+
+@@ -0,0 +1,71 @@
 +# Cortical Labs readiness (mesh prep)
 +
-+> **Tessera: approved, at Security gate**
-+
 +**Scope:** docs only; no code, installs, accounts, or spending.  
 +**Assigned:** Tessera (admin) at Father's request (2026-10-05 ~14:23 CT) via Cordnation.  
 +**Label key:** **REPORTED** = backed by a fetched public URL · **GOAL** = Father/mesh intent · **UNKNOWN** = not established from sources or repo inventory.

```

## Non-banner deltas flagged in interdiff scan

Review these (expected: hunk-header churn from removing banner lines only):

- `+---`
- `+---`
- `+`
- `+`
