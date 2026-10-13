---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---

# Status definitions

Statuses used by Gitbook / Cordnation when filing intake items and tracking the review pipeline:

| Status | Meaning |
|--------|---------|
| `draft` | Filed / received; not yet ready for Moderator, or awaiting readiness checklist |
| `in review` | Handed to Gitbook Moderator; decision pending |
| `Moderator: approved, at Tessera gate` | Moderator approved; next gate is Tessera (admin). Example of a **per-gate state** |
| `at Security gate` | Tessera cleared; next gate is Security (read-only sweep) |
| `at CI/Build gate` | Security cleared; next gate is CI/Build verify |
| `changes needed` | A gate returned the item for fixes (e.g. Tessera: changes needed); not Ready |
| `IN REVIEW` | Board/ledger operating state: one agent is actively working a HYB task |
| `BLOCKED` / `blocked` | Board or Moderator hold: a specific dependency, permission, provenance, safety, or product decision is missing; must not proceed to digest/push until resolved |
| `Ready` | **All four gates cleared** (Moderator, Tessera, Security, CI/Build); waiting **only** on Father's final yes in the bulk digest |
| `approved` | Legacy Moderator-only label; prefer per-gate states and `Ready` for the push path |
| `rejected` | Moderator rejected; stays out of GitHub / Origin until reworked and resubmitted |

## Ready and Father's yes

- **Ready** is set by Gitbook / Cordnation (docs) or Command Center (Replit app set) only after all four gates clear.
- Father's bulk **yes** covers **only the numbered items listed in that digest**. A yes never carries over to anything that wasn't listed.
- Ready does **not** mean pushed or merged. Push requires Father's final yes on the listed item; merge requires Father's separate explicit `merge`.

## Notes

- Gitbook / Cordnation keeps the review record and advances per-gate states.
- Only Gitbook Moderator sets Moderator approve / reject / block outcomes.
- Do not use bare `approved` or bare `Ready` as a banner while an item is still inside a gate.
