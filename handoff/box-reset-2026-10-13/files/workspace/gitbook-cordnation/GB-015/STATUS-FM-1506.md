# Status front-matter fix — GB-015 (15:06 CT Tessera ruling)

**Strip baseline:** `GB-015/GB-015.strip.diff`  
**New diff:** `GB-015/GB-015.diff`  
**Line counts:** strip 40 → status-fm 36

## Principle

Shipped `status:` must be true at Father push → **`published`**. No gate or Ready claims in front matter.

## Front matter now shipped

### `GB-015/proposed/mesh/roles/grok-bot.md`

```
---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---
```


## Note lines dropped

(none for this package)

## Notes

- `command-center.md` on main (beadc44) was `corrected-pending-publish`, not `published`; listed under ruling (1) but handled as (2): status → `published`, coordination note kept.
- mesh-lane-map.md: no FM; stale `**Status:**` L13 remains deleted; Instrument line kept.
- New package pages keep no status FM.

## Interdiff (strip.diff → new.diff)

```diff
--- /workspace/gitbook-cordnation/GB-015/GB-015.strip.diff	2026-10-05 15:05:49.691364734 -0500
+++ /workspace/gitbook-cordnation/GB-015/GB-015.diff	2026-10-05 15:07:35.655337696 -0500
@@ -1,12 +1,8 @@
 diff --git a/mesh/roles/grok-bot.md b/mesh/roles/grok-bot.md
 --- a/mesh/roles/grok-bot.md
 +++ b/mesh/roles/grok-bot.md
-@@ -1,24 +1,22 @@
-----
--status: published
--note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
-----
--
+@@ -5,20 +5,23 @@
+ 
  # Grok Bot
  
 -> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**

```
