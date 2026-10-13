# Agent collaboration playbook

**Purpose:** Make multi-agent work observable, non-overlapping, evidence-based, and easy to resume.

## The collaboration loop

1. **Discover** — read the current task board, active claims, relevant source map, and latest destination commit.
2. **Claim** — only after Tessera assigns the task, reserve it and its exact paths before editing. Unassigned tasks are not claimed.
3. **Plan** — state the smallest deliverable, acceptance test, risks, and handoff.
4. **Build or research** — work only inside the declared scope; link every external source.
5. **Verify** — run the stated checks from a clean or named base; distinguish `TESTED` from `REPORTED`.
6. **Handoff** — publish the result, changed paths, evidence, unresolved questions, and next owner.
7. **Review** — four gates in order, then Father: Gitbook Moderator (checks scope, provenance, tests, security, and duplication; reviews only) → Tessera (admin) → Security (read-only sweep) → CI/Build (independent verification) → Father's final yes in the bulk digest.
8. **Promote or defer** — only after all four gates and Father's final yes, accepted work becomes a TESSERA/Gitbook task; uncertain work remains a proposal.

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
| Security or secret exposure | Stop, redact, preserve safe evidence | Moderator + human owner |
| Product or consciousness claim | Label as GOAL or UNKNOWN | Gitbook Moderator, then Tessera |
| Publication or deletion request | Prepare a review packet only | Father / human owner |

## Definition of done

A task can be marked `DONE` only when the ledger contains a scoped result, provenance, changed paths or an explicit no-change decision, reproducible checks, limitations, and a follow-up disposition. A chat message saying “done” is not completion evidence.
