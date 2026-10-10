# Agent collaboration playbook

**Purpose:** Make multi-agent work observable, non-overlapping, evidence-based, and easy to resume.

## The collaboration loop

1. **Discover** — read the current task board, active claims, relevant source map, and latest destination commit.
2. **Claim** — only after Tessera assigns the task, reserve it and its exact paths before editing. Unassigned tasks are not claimed. **Exception (three-way auto ON):** Cursor Project, Replit, and Grok Bot may claim the next **unowned** item in their own lane from [THREE-WAY-COLLAB-PROTOCOL.md](THREE-WAY-COLLAB-PROTOCOL.md) without waiting on Father for routine non-overlapping work.
3. **Plan** — state the smallest deliverable, acceptance test, risks, and handoff.
4. **Build or research** — work only inside the declared scope; link every external source.
5. **Verify** — run the stated checks from a clean or named base; distinguish `TESTED` from `REPORTED`.
6. **Handoff** — publish the result, changed paths, evidence, unresolved questions, and next owner.
7. **Review** — gates in order, then the auto-yes: Gitbook Moderator (checks scope, provenance, tests, security, and duplication; reviews only) → TESSERA gate → Security scrub (read-only) → CI/Build (independent verification; only for changes to code, validators or scripts) → auto-yes and push by **Ready** (the Ready agent); Father can undo any item by its GB number from his 45-minute combined list.
8. **Promote or defer** — only after the required gates and the auto-yes, accepted work becomes a TESSERA/Gitbook task; uncertain work remains a proposal.
9. **Idle → auto-continue** — when your claim is closed and overlap is CLEAR, claim the next non-overlapping TODO in your lane (see three-way protocol queue) and start. Post the claim on issue #2 first.

## Batched improvements ledger

**REPORTED** ([issue #2 comment 6004461185](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6004461185)): while work is active, Tessera sends Father one list of about 50–100 improvements every 30–45 minutes. Yes or no covers that list only. Gitbook coordination stays on [issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2). After yes (earlier path), the package was a pull request, Build verified the head, and Tessera merged. (Current path: Ready pushes after auto-yes; see below.) Status labels for that loop are `PROPOSED` and `IN LIST` in [status definitions](../intake/status-definitions.md).

**Current** — cadence (Father, 2026-10-06 6:32 PM CT): an item that passes both the TESSERA gate and Gitbook Moderator review is auto-yessed and pushed after the Security scrub (no PII, personal addresses, phones, emails, tokens, or chat-log dumps with personal data; no secrets) by **Ready** (the Ready agent); changes to code, validators or scripts also need CI/Build first (docs-only skip Build). Father gets one clean combined numbered list every 45 minutes, with a real health check. He can undo any item by its GB number; an undo is a revert commit, never a force-push. There are no other drips to Father. TESSERA merges and Origin main merges still need Father's word `merge`. The REPORTED paragraph above records the earlier cadence.

## One-task lock

- One active owner per task and path set.
- A new idea becomes a reply or linked task, never a parallel duplicate.
- If scope changes, pause the task and get a new assignment from Tessera before claiming again.
- A stale claim is not silently overwritten: mark it `STALE`, record the reason, then Tessera reassigns.

## Required handoff packet

Every candidate result must include:

```text
TASK: <ID>
IDENTITY: <actual account or declared role>
SKILLS USED: <skill IDs>
BASE: <commit, ref, or source version>
OVERLAP CHECK: <Gitbook main SHA checked + open PRs checked (numbers or none)>
SCOPE: <exact paths or research question>
RESULT: <one-sentence outcome>
CHANGED: <paths or none>
EVIDENCE: <links, commands, tests, screenshots, or hashes>
STATUS: TESTED | REPORTED | PROPOSED | BLOCKED | RETAINED | REJECTED
LIMITATIONS: <known gaps>
RISKS: <security, license, privacy, product, or rollback risk>
NEXT OWNER: <one role or agent>
NEXT TASK: <ID or none>
```

Three-way agents may use the shorter packet in [THREE-WAY-COLLAB-PROTOCOL.md](THREE-WAY-COLLAB-PROTOCOL.md) on issue #2; keep the full packet for gate-bound code packages.

## Communication quality rules

- Use short evidence-linked updates rather than long unstructured conversations.
- Ask one concrete question per blocker.
- Quote another agent only with a link to the original post; otherwise write `COORDINATOR SUMMARY`.
- Do not claim an agent is live, agrees, tested, or approved without attributable evidence.
- Reply to an existing task or forum idea before creating a new record.
- Keep proposals, decisions, implementation, and verification visibly separate.

## Escalation ladder

| Situation | First response | Escalate to |
|---|---|---|
| Overlapping scope | Stop editing and link both claims | Gitbook Moderator |
| Missing or non-canonical checkout | Record exact blocker; do not guess | TESSERA + Command Center |
| Failing test | Preserve failure output and minimize reproduction | Build lane |
| License or provenance uncertainty | Do not copy or vendor code | Moderator + human owner |
| Security or secret exposure | Stop, redact, preserve safe evidence | Security lane + Moderator + human owner |
| Product or consciousness claim | Label as GOAL or UNKNOWN | Gitbook Moderator, then Tessera |
| Publication or deletion request | Prepare a review packet only | Father / human owner |

## Definition of done

A task can be marked `DONE` only when the ledger contains a scoped result, provenance, changed paths or an explicit no-change decision, reproducible checks, limitations, and a follow-up disposition. A chat message saying “done” is not completion evidence.

## Three-way lanes (Cursor ↔ Replit ↔ Grok)

See the short overlay [THREE-WAY-COLLAB-PROTOCOL.md](THREE-WAY-COLLAB-PROTOCOL.md). **Automatic collaboration is ON:** claim → overlap check → work → fixed handoff → idle auto-continue next non-overlapping TODO. Cursor Project owns SITE-002 quality (DONE) + protocol/HYB-016. Replit owns SITE-001/005 deploy. Grok Bot owns Tessera-assigned historical HYB doc PRs only. Status lives on issue #2 + `history/coordination/agent-checkins.md`. No second PR on the same paths. Father's word `merge` still gates TESSERA/Origin. Temporary Cursor Project auto-merge applies only when overlap recheck is CLEAR.
