---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---

# Status definitions

> **Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father**

Statuses used by Gitbook / Cordnation when filing intake items:

| Status | Meaning |
|--------|---------|
| `draft` | Filed / received; not yet ready for Moderator, or awaiting readiness checklist |
| `in review` | Handed to Gitbook Moderator; decision pending |
| `approved` | Moderator approved; eligible for Command Center digest / Father-gated push path |
| `rejected` | Moderator rejected; stays out of GitHub / Origin until reworked and resubmitted |
| `blocked` | Moderator blocked; held and must not proceed to digest/push until resolved per Moderator note |

## Notes

- Only Gitbook Moderator sets `approved`, `rejected`, or `blocked`.
- Gitbook / Cordnation sets `draft` / `in review` and keeps the review record.
- `approved` does **not** mean pushed or merged. Push requires Father's approval; merge requires Father's separate explicit `merge`.
