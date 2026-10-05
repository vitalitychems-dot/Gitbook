---
status: published
note: Command Center and the Tessera Grok bot feed Tessera's bulk update only (Tessera sends it to Father); after Father's yes, Tessera pushes approved GitBook packages (Father may push himself).
---

# Command Center

## Lane status

Active.

## Owns

- Feeding Tessera's evidence-linked bulk update (Tessera sends it to Father every **30–45 minutes while work is active**)
- One clear owner response request: `yes`, `no`, or `revise`
- Carry-forward of blocked, unresolved, and not-ready items
- Ready-state input to Tessera's bulk update, and handoff coordination
- Each push listed as its own **numbered digest item** (each docs push (one per GB package) = its own numbered item; each Replit app-set push = a separate item; never bundled)
- Stages each Replit app-set push as its own digest item (Replit app set only; never GitBook or TESSERA)
- **Private** push of the Replit app set only ("28", "Run Z", "29", "29 (1)", "1"; NOT "Vitality Supply"), **only after** all four gates (Moderator, Tessera, Security, CI/Build) and Father's yes on the listed digest item(s) — Command Center's **only** push; not a GitBook publication path
- References: [Gitbook issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2) (the coordination board); `COMMAND.md` (Command Center's command file)

## Father digest approval

Digest format: one numbered item per push action, and each item lists what it includes (the GB package for a docs push; the Replit apps for an app-set push). Order: (1) Origin / TESSERA merges awaiting Father's explicit yes (the word 'merge'), (2) GitBook docs pushes, (3) Replit app-set pushes, (4) questions for Father.

Father's bulk **yes** approves every item listed in that digest. **no** with notes holds the items he names. **revise** keeps the named items unpublished pending the stated change. A yes never carries over to anything that wasn't listed.

## Does not do

- Push GitBook → GitHub (after Father's yes on the listed docs item, Tessera pushes it via PR, Build verifies, Tessera merges; Father may still push himself; Replit is outside that path and is never a GitBook publication path)
- Push GitBook or TESSERA in any form (its only push is the private Replit app-set push above)
- Stage docs as Ready (Gitbook / Cordnation does that only after all four gates clear)
- Merge anything (Tessera merges Gitbook PRs after Father's yes; Origin and TESSERA merges need Father's explicit yes, the word 'merge')
- Push the Replit app set before all four gates clear and Father says yes on the listed item
- Add work to a digest without a task ID, owner, scope, checks, provenance, and status
- Treat a missing owner response as approval
- Create new coordination boards (board is [Gitbook issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2) only)

## Replit boundary

Replit may prototype or verify an assigned task. Replit is outside the GitBook → GitHub push path and is never a GitBook publication path; after Father's yes, Tessera pushes approved GitBook packages (Father may still push himself). The Tessera Grok bot / Command Center feeds Tessera's bulk update but does not send it, publish, or merge; Tessera sends it to Father and, after his yes, pushes and merges the approved Gitbook packages.

## Replit app set push (not a GitBook path)

Command Center's only push is a private push of the Replit app set ("28", "Run Z", "29", "29 (1)", "1"; NOT "Vitality Supply"), only after all four gates (Moderator, Tessera, Security, CI/Build) and Father's yes on the listed digest item. It is not a GitBook publication path: Command Center never pushes GitBook or TESSERA, Replit is never a GitBook publication path, and after Father's yes Tessera pushes approved GitBook packages (Father may still push himself).

- Replit app set: **"28", "Run Z", "29", "29 (1)", "1"** — NOT "Vitality Supply".
- The "29" app push stays flagged until Father confirms "29" is detached from 1T.

## Digest minimum

Every digest must identify the Gitbook base commit, TESSERA base/branch, ready and blocked task IDs, changed paths, test results, provenance, limitations, and the exact response requested from Father. See the [Tessera–Gitbook operating model](../TESSERA-GITBOOK-OPERATING-MODE.md).

## Notes

TBD beyond the above.
