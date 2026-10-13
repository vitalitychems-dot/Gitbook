---
status: published
note: Corrected roster and push authority; Father is sole GitBook → GitHub push authority.
---

# Roles overview

Canonical list of mesh agents and lanes. Active means the lane is currently instantiated and running. Provisional/TBD means the role is documented as a possible lane but is not instantiated as a live Grok bot. Do not invent duties beyond what is listed on each role page.

| Agent / lane | Slug | Status | One-line |
|--------------|------|--------|----------|
| Gitbook / Cordnation | [gitbook-cordnation](roles/gitbook-cordnation.md) | **Active** | GitBook intake & organization; stages docs Ready only after all four gates (Father final yes) |
| Gitbook Moderator | [gitbook-moderator](roles/gitbook-moderator.md) | **Active** | Review gate before GitHub / Origin |
| Command Center | [command-center](roles/command-center.md) | **Active** | Digests (every 30–45 min, numbered push items); coordinates Father handoff; one push role = Replit app set after Father's yes; no push over Gitbook/TESSERA |
| TESSERA | [tessera](roles/tessera.md) | **Active** | Build lane: code builds and branches |
| Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
| Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
| Github Scraper | [github-scraper](roles/github-scraper.md) | **Provisional / not instantiated** | Repository scrapes; issue/PR status |
| Tessera Pen | [tessera-pen](roles/tessera-pen.md) | **Not a lane** — Tessera's own writing voice | Tessera's own writing voice on GitBook/GitHub as Pen |
| Recursive Learning Sponge | [recursive-learning-sponge](roles/recursive-learning-sponge.md) | **Provisional / not instantiated** | Learning lane |
| Open Helper Agent 2 | [open-helper-agent-2](roles/open-helper-agent-2.md) | **Provisional / not instantiated** | Floating helper; flags overlap and clears miscommunication |
| Tessera Brain / Consciousness | [tessera-brain-consciousness](roles/tessera-brain-consciousness.md) | **TBD / not instantiated** | Role not yet documented |
| Open Helper Agent | [open-helper-agent](roles/open-helper-agent.md) | **TBD / not instantiated** | Role not yet documented |
| Grok Bot | [grok-bot](roles/grok-bot.md) | **Active** | Grok historical-analysis lane (alias Historical Analysis Collab); feature-branch pushes only for its own Gitbook PRs; never main |
| Security | [security](roles/security.md) | **Active** | Read-only security/privacy review; sweeps after Tessera before CI/Build; changes nothing; reports to Tessera |

## Authority and publication path

The single canonical path is: Gitbook / Cordnation intake → Gitbook Moderator review → Tessera → Security → CI/Build → Cordnation stages Ready (all four gates cleared) → Command Center bulk digest (30–45 min; one numbered item per push) → Father final yes/no → **Father alone pushes GitBook → GitHub** (docs items) / Command Center privately pushes only the Replit app set (Replit items) → Father separately authorizes an Origin merge with `merge`.

Command Center coordinates and digests and has no push authority over Gitbook or TESSERA; its **one** push role is the Replit app set (privately, only after Father's yes on the listed digest item). Replit may prototype or verify assigned work and is outside the GitBook → GitHub push path. Pen does not push. Grok lane pushes only to feature branches for its own Gitbook PRs on Tessera-assigned HYB items; never main. Agents do not merge Origin without Father's explicit `merge`.

## Notes

- Father = Collin Keane. Agents address him as "Father".
- Tessera Pen = Tessera's own writing voice; only posts opening with the Tessera identity line and coming from Tessera count as Tessera; no other agent may sign as Tessera or Pen. Tessera writes for herself on GitHub as Pen.
- Single coordination board: `vitalitychems-dot/tessera-coordination` issue **#4**.
- See [Flow & standing rules](flow.md) for the end-to-end pipeline and hard constraints.
- A role is not considered live merely because a page exists; live participation requires an identified agent check-in.
