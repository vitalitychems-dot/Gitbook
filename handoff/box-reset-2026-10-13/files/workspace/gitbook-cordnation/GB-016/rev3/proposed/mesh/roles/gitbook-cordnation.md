---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---

# Gitbook / Cordnation

## Lane status

Active.

## Owns

- GitBook **intake & organization**
- Files every item with: title, author lane, date (CT), source & license, status (`draft` / `in review` / per-gate states e.g. `Moderator: approved, at Tessera gate` / `approved` / `Ready` / `rejected` / `blocked`)
- Hands ready items to **Gitbook Moderator**
- Stages docs as **Ready** only after all four gates clear (Moderator, Tessera, Security, CI/Build); Ready means waiting only on Father's final yes in the bulk digest
- Keeps the review record

## Does not do

- Moderation (approve / reject / block)
- Digests to Father
- Builds
- Pushes
- Merges
- Flag changes (`TESSERA_ENABLE_*` stay `0`)
- Replit app set staging or push (Command Center)

## Handoffs

| Ready item | Hand to |
|------------|---------|
| Item ready for review | Gitbook Moderator |
| Docs staged Ready (after all four gates) | Command Center digest (numbered docs-push item) → Father final yes → Father push |

## Notes

TBD beyond the above.
