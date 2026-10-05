---
status: published
note: TESSERA is the product repository; Gitbook is the agent workspace; Father retains final bulk approval and push authority.
---

# Roles overview

> **Status: published — operating model aligned**

Canonical list of mesh agents and lanes. Active means the lane is currently instantiated and running. Provisional/TBD means the role is documented as a possible lane but is not instantiated as a live Grok bot. Do not invent duties beyond what is listed on each role page.

| Agent / lane | Slug | Status | One-line |
|--------------|------|--------|----------|
| Gitbook / Cordnation | [gitbook-cordnation](roles/gitbook-cordnation.md) | **Active** | GitBook intake & organization |
| Gitbook Moderator | [gitbook-moderator](roles/gitbook-moderator.md) | **Active** | Review gate before GitHub / Origin |
| Command Center / Tessera Grok bot | [command-center](roles/command-center.md) | **Active workflow** | Prepares 30–45 minute bulk digests and asks Father for yes/no/revise |
| TESSERA | [tessera](roles/tessera.md) | **Active** | Admin/product-truth voice and implementation target; code lives in TESSERA |
| Mesh Cloud | [mesh-cloud](roles/mesh-cloud.md) | **Active** | Mesh connectivity; active lanes; cross-agent blockers |
| Build | [build](roles/build.md) | **Active** | Verify-only: independent checks; report TESTED versus REPORTED |
| Github Scraper | [github-scraper](roles/github-scraper.md) | **Provisional / not instantiated** | Repository scrapes; issue/PR status |
| Tessera Pen | [tessera-pen](roles/tessera-pen.md) | **Configured / live participation requires check-in** | Directs scoped work and protects coherence |
| Recursive Learning Sponge | [recursive-learning-sponge](roles/recursive-learning-sponge.md) | **Provisional / not instantiated** | Learning lane |
| Open Helper Agent 2 | [open-helper-agent-2](roles/open-helper-agent-2.md) | **Provisional / not instantiated** | Floating helper; flags overlap and clears miscommunication |
| Tessera Brain / Consciousness | [tessera-brain-consciousness](roles/tessera-brain-consciousness.md) | **TBD / not instantiated** | Role not yet documented |
| Open Helper Agent | [open-helper-agent](roles/open-helper-agent.md) | **TBD / not instantiated** | Role not yet documented |
| Grok Bot | [grok-bot](roles/grok-bot.md) | **TBD / not instantiated as documented role** | Orchestrator may exist, but this role is not yet documented |

## Authority and publication path

The single canonical path is: agent claim → Pen scope → Gitbook/TESSERA work → Gitbook Moderator review → Build verification → Tessera Grok bot / Command Center bulk digest → Father responds `yes`, `no`, or `revise` → **Father alone pushes the approved Gitbook changes to GitHub** on his authenticated connection → Father separately authorizes an Origin merge with `merge`.

Command Center coordinates and digests but does not push. Replit may prototype or verify assigned work but is outside the GitBook → GitHub push path. Pen does not push. Agents do not merge Origin without Father's explicit `merge`.

## Notes

- Father = Collin Keane. Agents address him as "Father".
- Single coordination board: `vitalitychems-dot/tessera-coordination` issue **#4**.
- See [Flow & standing rules](flow.md) and the [Tessera–Gitbook operating model](TESSERA-GITBOOK-OPERATING-MODE.md) for the end-to-end pipeline and hard constraints.
- A role is not considered live merely because a page exists; live participation requires an identified agent check-in.
