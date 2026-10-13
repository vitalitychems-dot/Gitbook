---
status: published
note: Father is the sole GitBook → GitHub push authority; Command Center coordinates only.
---

# Mesh flow & standing rules

> **Canonical push rule:** Command Center prepares the digest and coordinates the handoff. After Father gives Ready/yes, **Father alone pushes GitBook → GitHub on his authenticated GitHub connection**. Replit is not in the push path. A separate explicit `merge` is still required for Origin merges.

## End-to-end flow

Agents discover → claim one task → produce work → **Gitbook / Cordnation** intake → **Gitbook Moderator** reviews → **Build** independently verifies → **Command Center** digests to Father approximately every 30 minutes → Father decides Ready/yes → **Father pushes GitBook → GitHub** → Father separately says `merge` for an Origin merge.

```mermaid
flowchart TD
  A[Discover and claim one task] --> B[Agents produce scoped work]
  B --> C[GitBook intake<br/>Gitbook / Cordnation]
  C --> D[Gitbook Moderator<br/>scope / provenance review]
  D -->|approved| E[Build<br/>independent verification]
  D -->|needs work| C
  E -->|pass| F[Command Center<br/>digest to Father ~30 min]
  E -->|fail| C
  F --> G{Father Ready / yes?}
  G -->|no| F
  G -->|yes| H[Father<br/>pushes GitBook → GitHub]
  H --> I{Father explicit merge?}
  I -->|no| J[Stays unmerged]
  I -->|yes| K[Merge]
```

## Standing rules

| Rule | Detail |
|------|--------|
| `TESSERA_ENABLE_*` flags | Stay **`0`**. Do not flip them. |
| Secrets | None. No credentials, tokens, or private keys in docs or commits. |
| Crypto / money / store | Out of scope for the current consolidation. |
| Uncensoring / surveillance | No uncensoring tools. No surveillance of real people. |
| Coordination board | **One board only:** GitHub `vitalitychems-dot/tessera-coordination` issue **#4**. |
| Command Center | Digest, status, and handoff coordination only; it does not push GitBook or Origin. |
| Replit | Replit may prototype or verify assigned work; it is outside the GitBook → GitHub push path. |
| Push authority | Father alone pushes GitBook → GitHub after Ready/yes. |
| Merge authority | Origin merges need Father's separate explicit `merge`. |
| Private docs repo | `vitalitychems-dot/Gitbook`. |
| Task lock | One owner, one exact scope, one acceptance test; overlaps are resolved before editing. |
| Evidence | Every closure records provenance, checks, limitations, and next owner. |
| Status truth | `TESTED`, `REPORTED`, `PROPOSED`, `BLOCKED`, `RETAINED`, and `REJECTED` are not interchangeable. |
| Tessera identity | Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen. |

## Lane boundaries

- **Gitbook / Cordnation** — intake and organization only.
- **Gitbook Moderator** — review gate before GitHub / Origin.
- **Command Center** — digests approximately every 30 minutes, tracks readiness, and coordinates the Father handoff; no push authority.
- **TESSERA** — code builds and branches.
- **Mesh Cloud** — mesh connectivity, active lanes, and cross-agent blockers.
- **Build** — verify-only; report TESTED versus REPORTED.
- **Security** — read-only security/privacy review, repo access watch, identity integrity; sweeps every item after the Tessera gate and before CI/Build; reports to Tessera; changes nothing (no edits, commits, PRs, pushes, merges, settings, secret rotation, or flag flips).
- **All lanes** — declare skills used, use the handoff packet, and check in at claim, blocker, candidate result, and closure.
- **Provisional/TBD lanes** — no work is attributed to them until instantiated and identified in the check-in ledger.

## Related pages

- [Roles overview](roles.md)
- [Mesh lane map](roles/mesh-lane-map.md)
- [Command center](../history/coordination/command-center.md)
- [How to submit](../intake/how-to-submit.md)
- [Collaboration playbook](COLLABORATION-PLAYBOOK.md)
- [Agent skill matrix](AGENT-SKILL-MATRIX.md)
- [Collaboration metrics](COLLABORATION-METRICS.md)
- [Moderator handoff](../review/moderator-handoff.md)
