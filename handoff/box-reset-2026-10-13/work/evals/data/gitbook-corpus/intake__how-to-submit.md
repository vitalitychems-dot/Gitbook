---
status: published
note: Status: published 2026-10-05 (commit 98fa6c7) — approved by Gitbook Moderator and Father
---

# How to submit (intake)

Agents submit finished or draft documentation to **Gitbook / Cordnation** for filing. Do not push to GitHub or open PRs yourself (the Grok lane's feature-branch exception is in [Flow & standing rules](../mesh/flow.md), Push authority (3)), and do not ask Command Center to push: it never pushes GitBook. Items move only through the four gates and Father's final yes below.

## Required fields for every submission

| Field | Requirement |
|-------|-------------|
| **Title** | Clear, human-readable title |
| **Author lane** | Submitting agent / lane name |
| **Date (CT)** | Date in America/Chicago (Central Time) |
| **Source** | Where the content came from (agent, repo path, prior note, etc.) |
| **License** | License if known; otherwise `TBD` |
| **Summary** | Short description of what the item is |
| **Links** | Relevant links (repo paths, issues, prior drafts) if any |

## After you submit

1. Gitbook / Cordnation files the item in the [intake log](log.md) with status `draft` (or moves it to `in review` when handing off).
2. Items go through four gates in order: **Gitbook Moderator** (see [Moderator handoff](../review/moderator-handoff.md)) → **Tessera** (admin) → **Security** (read-only sweep) → **CI/Build** (independent verification). Per-gate states are in [Status definitions](status-definitions.md).
3. After all four gates clear, Gitbook / Cordnation stages the item as **Ready**, and Command Center lists it as its own numbered item in the bulk digest to Father (every 30–45 min).
4. After Father approves, **Tessera** pushes the approved package: she opens a PR, Build verifies it, then she merges and posts on Gitbook issue #2. Father may still push himself on his authenticated connection. Replit is outside that path. Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed. Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes before anyone merges.

## Standing constraints

- No secrets in submissions
- No crypto / money / store work
- No uncensoring tools or surveillance of real people
- Do not change `TESSERA_ENABLE_*` (stay `0`)
- Single coordination board: [`vitalitychems-dot/Gitbook` issue **#2**](https://github.com/vitalitychems-dot/Gitbook/issues/2)

## Status values

See [Status definitions](status-definitions.md).
