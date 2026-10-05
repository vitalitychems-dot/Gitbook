---
status: draft
note: Status: approved by Gitbook Moderator (2026-10-05) — awaiting Father's yes before publish
---

# Moderator handoff

> **Status: approved by Gitbook Moderator (2026-10-05) — awaiting Father's yes before publish**

When **Gitbook / Cordnation** marks an item ready, it hands the item to **Gitbook Moderator**. Moderator is the review gate before anything reaches GitHub / Origin.

## What "ready" means

An item is **ready** for Moderator when all of the following are true:

1. Filed in the [intake log](../intake/log.md) with required fields: title, author lane, date (CT), source, license, status
2. Content is complete enough to review (not a placeholder stub unless the stub itself is the submission)
3. No secrets, credentials, or tokens in the page
4. Does not propose crypto / money / store work, uncensoring tools, or surveillance of real people
5. Does not instruct flipping `TESSERA_ENABLE_*` away from `0`
6. Does not create or point at a new coordination board (only issue **#4**)
7. Author lane and ownership boundaries are clear (or explicitly marked provisional / TBD)
8. Status moved to `in review` by Gitbook / Cordnation at handoff

## Moderator checklist

- [ ] Required intake fields present and accurate
- [ ] Standing rules respected (flags, secrets, out-of-scope topics, single board)
- [ ] Role / lane claims match known mesh boundaries (or are marked provisional / TBD)
- [ ] Sources and license noted (license may be `TBD`)
- [ ] Decision: **approve**, **reject**, or **block**
- [ ] Decision recorded; Gitbook / Cordnation keeps the review record
- [ ] If approved: eligible for Command Center digest — **not** auto-pushed
- [ ] If blocked: note what must change or wait before the item can move again

## After the decision

| Decision | Next step |
|----------|-----------|
| Approve | Status → `approved`. Command Center may include in ~30 min digest. Push only after Father approves. Merge only on Father's explicit `merge`. |
| Reject | Status → `rejected`. Author lane may revise and resubmit via intake. |
| Block | Status → `blocked`. Item is held; does not proceed to digest/push until unblocked or resubmitted per Moderator note. |

## Out of Moderator scope

- Digests to Father (Command Center)
- Replit / GitHub pushes (Command Center, Father-gated)
- Merges (Father only)
- Builds / branches (TESSERA)
- Intake filing itself (Gitbook / Cordnation)
