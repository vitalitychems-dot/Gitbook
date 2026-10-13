---
status: published
note: Command Center and the Tessera Grok bot prepare bulk digests only; Father is sole GitBook → GitHub push authority.
---

# Command Center

> **Status: published — authority wording aligned**

## Lane status

Active.

## Owns

- Evidence-linked bulk digests to Father every **30–45 minutes while work is active**
- One clear owner response request: `yes`, `no`, or `revise`
- Carry-forward of blocked, unresolved, and not-ready items
- Ready-state digest and handoff to Father; no GitHub push authority
- References: issue **#2** / `COMMAND.md`

## Does not do

- Merge without Father's separate explicit `merge`
- Push GitBook → GitHub; Father alone performs that push after Ready/yes
- Add work to a digest without a task ID, owner, scope, checks, provenance, and status
- Treat a missing owner response as approval
- Create new coordination boards (board is issue **#4** only)

## Replit boundary

Replit may prototype or verify an assigned task. Replit is outside the GitBook → GitHub push path. The Tessera Grok bot may prepare and deliver the digest, but it cannot publish or merge. The old private push set is historical and is no longer an active Command Center responsibility.

## Digest minimum

Every digest must identify the Gitbook base commit, TESSERA base/branch, ready and blocked task IDs, changed paths, test results, provenance, limitations, and the exact response requested from Father. See the [Tessera–Gitbook operating model](../TESSERA-GITBOOK-OPERATING-MODE.md).

## Notes

TBD beyond the above.
