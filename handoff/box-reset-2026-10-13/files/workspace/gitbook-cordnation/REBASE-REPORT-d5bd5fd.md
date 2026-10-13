# Rebase report vs Gitbook HEAD

## d5bd5fd (Publish HYB-007 Z-app comparison (#4))

| Package | Class | Diff lines | Notes |
|---------|-------|------------|-------|
| GB-015 | B | see GB-015.diff | grok-bot Active page onto HEAD TBD stub |
| GB-016 | C | 0 (proposed=HEAD) | Father-only push on HEAD conflicts with GB-016 dual-path; edits dropped |
| GB-016 rev 3 | B (additive) | see GB-016/rev3/GB-016-rev3.diff | Additive to HEAD: CC Replit app-set exception + Ready staging/digest rules; stacks after GB-017 |
| GB-017 | B | see GB-017.diff | Security + identity + Grok Active onto HEAD |
| GB-018 | B | see GB-018.diff | HYB-005 close onto HEAD; keep HYB-007 DONE |
| GB-019 | B | see GB-019.diff | HYB-019 + Cortical page; stacked on GB-018 rebased |

## 0af00a1bd86c9f490f81410ae14ee40e02b0b19f (Claim HYB-012 route audit)

Parent of d5bd5fd. Delta for packages: `history/coordination/agent-checkins.md` Active claims now holds HYB-012 IN REVIEW.

| Package | Action |
|---------|--------|
| GB-018 | base/proposed check-ins preserve HYB-012 exactly; HYB-005 status wording → DECIDED, pending push |
| GB-019 | no check-ins file; backlog base = GB-018 proposed (stacking) |
| GB-015/016/017 | no check-ins touch; unchanged by 0af00a1 |

Nothing written to GitHub.

## cc720d3d0bacb2a6d5863d2051c67cb8ec534cc1 (Update active HYB-012 check-in with route collision evidence)

Parent of 0af00a1. Delta: `history/coordination/agent-checkins.md` Active claims updated (two HYB-012 blocks with route-collision evidence).

| Package | Action |
|---------|--------|
| GB-018 | base/proposed Active claims = exact HEAD cc720d3; HYB-005 DECIDED overlay unchanged |
| GB-015/016/017/019 | no check-ins touch |

Also: Tessera Ready-staging ruling applied to GB-016 rev 3 (Ready after all four gates).

---
**Superseded for HEAD claims:** see `REBASE-REPORT-95993af.md`. True lineage: d5bd5fd → 0af00a1 → cc720d3 → 527ee36 → 95993af (each is child of the previous). Final Cordnation pass-2 base is 95993af.
