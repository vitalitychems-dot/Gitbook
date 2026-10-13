# Rebase report vs Gitbook HEAD 95993af

## True lineage (newest first)

| SHA | Parent | Message |
|-----|--------|---------|
| `95993aff649703cf79eb12a2103299781aa8eecf` | 527ee36 | docs: record HYB-012 canonical static verification |
| `527ee3687533f5df848f62cd68dd621b3666e951` | cc720d3 | Record HYB-012 blocker and verified duplicate route evidence |
| `cc720d3d0bacb2a6d5863d2051c67cb8ec534cc1` | 0af00a1 | Update active HYB-012 check-in with route collision evidence |
| `0af00a1bd86c9f490f81410ae14ee40e02b0b19f` | d5bd5fd | Claim HYB-012 route audit |
| `d5bd5fd45410d78808ba2af4f49e91ecec78e730` | 6fe412f (+ PR) | Publish HYB-007 Z-app comparison (#4) |

Note: prior reports that called 0af00a1 the "parent of d5bd5fd" or cc720d3 the "parent of 0af00a1" were **backwards**. Each listed SHA is the **child** of the prior.

## Pass-2 rebase (2026-10-05 ~14:55 CT)

All packages rebased onto `95993af`. Diffs regenerated with repo-relative `a/` / `b/` paths. `git apply --check -p1` clean in stack order: GB-017 → GB-016 rev 3 → GB-015 → GB-018 → GB-019.

| Package | Class | Diff lines | Notes |
|---------|-------|------------|-------|
| GB-015 | B | see GB-015.diff | Feature-branch Gitbook-PR wording; gate banner |
| GB-017 | B | see GB-017.diff | Pen Not a lane; tessera-pen.md; Security privacy/sweep; drop Grok row |
| GB-016 rev 3 | B | see GB-016-rev3.diff | Replit through Moderator; instrument restored; status-definitions.md; stacked on GB-017 |
| GB-018 | B | see GB-018.diff | checkins on 95993af; HYB-012 intact; IN REVIEW pending push; **diff-only for checkins** |
| GB-019 | B | see GB-019.diff | no backlog front matter; stacked on GB-018 backlog |

Nothing written to GitHub. TESSERA_ENABLE_* stay 0.
