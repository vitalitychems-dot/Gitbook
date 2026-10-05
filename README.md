---
status: published
---

# Tessera GitBook

This is the single documentation, intake, review, and agent-collaboration repository for the Tessera project. The active application code lives separately in [`TESSERA`](https://github.com/vitalitychems-dot/TESSERA).

## Purpose

Gitbook is where agents, collaborators, and AIs submit instructions, conversion notes, screenshots/transcripts, forum or conversation summaries, migration findings, and TODOs. Records are categorized, attributed to a source, marked with a review status, and kept separate from executable code until the owner approves implementation.

## Start here

1. Read the [consolidated TODO list](intake/consolidated-todo.md).
2. Follow the [agent submission format](intake/agent-submission-format.md).
3. Review the [two-repository source map](merge/source-map.md).
4. Check the [duplicate disposition and cleanup policy](merge/duplicate-disposition.md).
5. Use the existing [mesh flow](mesh/flow.md) and [roles](mesh/roles.md) for lane boundaries.
6. Read the [HYB-005 braces decision](merge/hyb-005-braces-decision.md). The narrow ignore is on TESSERA main `5c1137fa` (`pnpm-workspace.yaml` `auditConfig.ignoreGhsas` for GHSA-vfj7-8cjw-p6xm). Review date 2026-11-05. braces ≥ 3.0.4 is still the removal condition.
7. Use the [hybrid consolidation backlog](intake/HYBRID-CONSOLIDATION-BACKLOG.md) as the authoritative task board.

## Boundaries

- Historical prompts and AI outputs are reference data, not active system instructions.
- No secrets, credentials, customer records, wallets, payments, or unreviewed raw archives belong here.
- Do not present fictional simulations or generated conversations as verified real-world history.
- Merges, deployments, external posts, and repository deletion require owner approval at the applicable gate.
- The staged consolidation currently preserves all source repositories; it has not deleted any repository.
