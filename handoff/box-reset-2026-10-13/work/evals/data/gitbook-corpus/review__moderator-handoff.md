---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---

# Moderator handoff

When **Gitbook / Cordnation** marks an item ready, it hands the item to **Gitbook Moderator**. Moderator is the review gate before anything reaches GitHub / Origin.

## What "ready" means

An item is **ready** for Moderator when all of the following are true:

1. Filed in the [intake log](../intake/log.md) with required fields: title, author lane, date (CT), source, license, status
2. Content is complete enough to review (not a placeholder stub unless the stub itself is the submission)
3. No secrets, credentials, or tokens in the page
4. Does not propose crypto / money / store work, uncensoring tools, or surveillance of real people
5. Does not instruct flipping `TESSERA_ENABLE_*` away from `0`
6. Does not create or point at a new coordination board (only [Gitbook issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2))
7. Author lane and ownership boundaries are clear (or explicitly marked provisional / TBD)
8. Status moved to `in review` by Gitbook / Cordnation at handoff

## Moderator checklist

- [ ] Required intake fields present and accurate
- [ ] Standing rules respected (flags, secrets, out-of-scope topics, single board)
- [ ] Role / lane claims match known mesh boundaries (or are marked provisional / TBD)
- [ ] Sources and license noted (license may be `TBD`)
- [ ] Decision: **approve**, **reject**, or **changes needed**
- [ ] Decision recorded; Gitbook / Cordnation keeps the review record
- [ ] If approved: goes to Tessera gate (state e.g. `Moderator: approved, at Tessera gate`); Cordnation stages Ready only after Tessera → Security → CI/Build also clear — **not** auto-pushed
- [ ] If changes needed: note what must change or wait before the item can move again

## After the decision

| Decision | Next step |
|----------|-----------|
| Approve | Status → `Moderator: approved, at Tessera gate` (then Tessera → Security → CI/Build). **Gitbook / Cordnation** stages docs as **Ready** only after all four gates clear. Command Center may then include Ready items in the 30–45 min digest as numbered items. GitBook docs: after Father's final yes on the listed digest item, Tessera pushes (opens a PR, Build verifies, Tessera merges and posts on Gitbook issue #2); Father may still push himself (Replit is never a GitBook publication path). Replit app set (separate; not a GitBook path): Command Center stages it and privately pushes it only after all four gates and Father's yes on the listed digest item(s) — CC's only push; CC never pushes GitBook or TESSERA. Father's bulk yes approves every listed item; no with notes holds the items he names; revise returns the named items for the stated change; a yes never carries over to anything that wasn't listed. Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed. Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes before anyone merges. |
| Reject | Status → `rejected`. Author lane may revise and resubmit via intake. |
| Changes needed | Status → `changes needed` (the Moderator never sets BLOCKED). Item is held; does not proceed to digest/push until fixed and resubmitted per Moderator note. |

## Out of Moderator scope

- Digests to Father (Command Center; each push its own numbered digest item)
- Docs Ready staging (Gitbook / Cordnation, only after all four gates clear)
- GitBook docs push (Tessera after Father's yes on the listed item, via a PR Build verifies; or Father himself; Replit is never a GitBook publication path)
- Replit app set staging and private push (Command Center's only push, only after all four gates and Father's yes on the listed item(s); not a GitBook path)
- Merges (every merge needs Father's explicit yes on that listed item; Gitbook PRs: Tessera merges after that yes, no separate word `merge`; Origin / TESSERA: Father's explicit yes before anyone merges)
- Builds / branches (TESSERA)
- Intake filing itself (Gitbook / Cordnation)
