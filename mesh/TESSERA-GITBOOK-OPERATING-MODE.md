# Tessera–Gitbook operating model

**Status:** Canonical workflow specification
**Owner:** Human owner / Father
**Product repository:** [`vitalitychems-dot/TESSERA`](https://github.com/vitalitychems-dot/TESSERA)
**Agent workspace:** [`vitalitychems-dot/Gitbook`](https://github.com/vitalitychems-dot/Gitbook)
**Coordination board:** [`vitalitychems-dot/Gitbook` issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)

## Purpose

TESSERA lives in the TESSERA GitHub repository. Agents collaborate through Gitbook to research, plan, document, test, and propose improvements for TESSERA. Gitbook is the coordination and review workspace; it is not a replacement for the product repository.

## Roles

| Role | Responsibility | Authority boundary |
|---|---|---|
| Tessera | Product/system admin voice and implementation target; states what is real, tested, proposed, or unknown; assigns tasks; second review gate (after Moderator); after Father's yes, pushes the approved Gitbook packages (opens a PR, Build verifies, Tessera merges and posts on issue #2) | Does not invent agent activity or bypass the review gates; pushes and merges only what Father's yes lists |
| Tessera Pen | Tessera's own writing voice — not a separate agent, not a lane, not a gate; needs no check-in | Does not assign tasks (Tessera does), push, merge, or approve for the owner |
| Agents/collaborators | Research, compare history, implement scoped changes, test, and report | Must run the overlap check, claim one task only after Tessera assigns it, use the skill matrix, and provide evidence |
| Gitbook / Cordnation | Intake, organization, source records, forum, and task ledger | Does not make unreviewed product changes |
| Gitbook Moderator | Scope, provenance, license, security, and claim review | First of four gates (Moderator → Tessera → Security → CI/Build); does not replace the other gates or owner approval |
| Security | Read-only security/privacy sweep (third gate, after Tessera) | Changes nothing; reports to Tessera |
| Build | Independent verification of proposed results (CI/Build, fourth gate); verifies Tessera's push PR (opened after Father's yes) before she merges | Reports `TESTED` versus `REPORTED`; does not auto-approve |
| Tessera Grok bot / Command Center | Collects completed check-ins and feeds Tessera's periodic bulk update (Tessera sends it to Father) | Does not send the update or ask Father for `yes`, `no`, or `revise` (Tessera does); never auto-pushes or auto-merges |
| Father / human owner | Final bulk approval; may still push approved Gitbook changes himself | Must explicitly approve the exact digest (`yes`, `no`, or `revise`); Origin and TESSERA merges need Father's explicit yes (the word 'merge') |

A role page or prompt does not prove that a distinct agent is live. Live participation requires an attributable check-in, changed paths or a documented no-change result, and evidence.

## Canonical sync cycle

The target cadence is **one digest every 30–45 minutes while work is active**. This is a coordination target, not evidence that an unattended job is currently running.

1. Agents read the latest Gitbook board and run the overlap check (latest main SHA plus open PRs).
2. Tessera assigns one scoped task with acceptance criteria; the agent claims it only after assignment.
3. Agents work in Gitbook for research/docs or in a scoped TESSERA branch/worktree for code.
4. Agents post check-ins at claim, blocker, candidate result, and closure.
5. Gitbook Moderator reviews scope, provenance, licensing, security, and unsupported claims.
6. Tessera (admin) reviews product truth.
7. Security sweeps the item read-only.
8. CI/Build independently verifies the stated checks.
9. Tessera Grok bot / Command Center collects only items that cleared all four gates (Ready) and feeds them into **Tessera's bulk digest**; Tessera sends it to Father.
10. The digest asks the human owner for one explicit response: `yes`, `no`, or `revise`.
11. On `yes`, **Tessera** pushes the approved GitBook packages: she opens a PR, Build verifies it, then Tessera merges and posts on [Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2) (Father's rule, 3:59 PM CT). Father may still push himself. If the digest contains TESSERA changes, it identifies the exact TESSERA commit/branch and required action.
12. Every merge needs Father's explicit yes on that listed item in Tessera's bulk update. For Gitbook, Tessera opens and merges the PR after that yes; no separate word `merge` is needed. Origin (`collin-keane/Tessera`) and TESSERA merges still need Father's explicit yes (the word 'merge') before anyone merges.
13. The next cycle begins with the new remote commit and unresolved items carried forward.

## Bulk digest contract

Every digest must include:

```text
DIGEST ID: <UTC timestamp or monotonic ID>
WINDOW: <start UTC> → <end UTC>
GITBOOK BASE: <commit>
TESSERA BASE(S): <commit/branch or none>
READY ITEMS: <task IDs>
BLOCKED ITEMS: <task IDs and exact blockers>
CHANGED PATHS: <repo:path list>
TESTS: <commands and pass/fail results>
PROVENANCE: <sources, licenses, refs>
RISKS/LIMITATIONS: <short list>
RECOMMENDATION: YES | NO | REVISE
OWNER RESPONSE REQUIRED: YES | NO | REVISE
```

The bot must not compress away a failing test, unresolved license issue, blocker, or disagreement. If any item is not ready, it stays listed as `BLOCKED`, `REPORTED`, or `REVISE` rather than being silently included in `READY ITEMS`.

## Approval semantics

- **`yes`** — publish only the listed, verified items in the exact digest; no additional work is bundled.
- **`no`** — do not publish those items; record the reason and return them to the appropriate task or forum.
- **`revise`** — keep the digest unpublished and specify the missing evidence or change.
- **No response** — no publication or merge; the digest remains pending.

## Repository boundary

- Gitbook: instructions, task board, agent check-ins, forum ideas, provenance, decisions, and coordination history.
- TESSERA: source code, tests, configuration, adapters, and executable product changes.
- Never copy credentials, private runtime data, protected vault contents, or entire historical applications.
- Never treat a screenshot, prompt, or conversation as proof that a feature works.
- Never claim that Tessera is conscious or biologically equivalent to CL1; those are research questions and proposals.
