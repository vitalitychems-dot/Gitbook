# Banner strip proof — GB-015 (15:04 CT Tessera ruling b)

**Pre-strip diff:** `GB-015/GB-015.pre-strip.diff`  
**New diff:** `GB-015/GB-015.diff`  
**Line counts:** pre-strip 43 → new 40

## Claim

This strip is banner-only: gate-status front matter, gate blockquotes, and `**Status:** <gate state>` claim lines were removed from `proposed/` and the regenerated diff. Pipeline *documentation* of gate states (e.g. `intake/status-definitions.md` table; flow/mermaid/handoff prose naming per-gate states) was kept.

## Lines removed from proposed/ (logged)

- `GB-015/proposed/mesh/roles/grok-bot.md: FM: status: at Security gate`
- `GB-015/proposed/mesh/roles/grok-bot.md: FM: note: Tessera: approved, at Security gate`
- `GB-015/proposed/mesh/roles/grok-bot.md: replaced gate FM with main FM`
- `GB-015/proposed/mesh/roles/grok-bot.md: blockquote: > **Tessera: approved, at Security gate**`

## Main-line restorations attempted then dropped (false status claims)

- GB-015/proposed/mesh/roles/grok-bot.md: dropped main blockquote (false status claim): > **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
- GB-015/proposed/mesh/roles/grok-bot.md: dropped restored main front matter (false status claim): ---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---...

## Restorations that remain

(none kept — main published/Ready/corrected status claims were dropped per ruling)

## Interdiff excerpt (pre-strip.diff vs new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-015/GB-015.pre-strip.diff	2026-10-05 14:58:29.339464180 -0500
+++ /workspace/gitbook-cordnation/GB-015/GB-015.diff	2026-10-05 15:05:49.691364734 -0500
@@ -1,19 +1,16 @@
 diff --git a/mesh/roles/grok-bot.md b/mesh/roles/grok-bot.md
 --- a/mesh/roles/grok-bot.md
 +++ b/mesh/roles/grok-bot.md
-@@ -1,24 +1,29 @@
- ---
+@@ -1,24 +1,22 @@
+----
 -status: published
 -note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-+status: at Security gate
-+note: Tessera: approved, at Security gate
- ---
- 
+----
+-
  # Grok Bot
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**
-+> **Tessera: approved, at Security gate**
- 
+-
  ## Lane status
 -
 -**TBD** — role not yet documented.

```

## Non-banner deltas flagged in interdiff scan

Review these (expected: hunk-header churn from removing banner lines only):

- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: ----`
- `ADDED_IN_NEW_PATCH: -`
- `ADDED_IN_NEW_PATCH: -`
