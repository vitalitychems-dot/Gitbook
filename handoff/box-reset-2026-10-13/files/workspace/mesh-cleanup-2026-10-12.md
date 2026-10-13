# Mesh cleanup plan — 2026-10-12 ~8:20 PM CT (Security, READ-ONLY, proposal only)

## Evidence limits (read first)
- No ReadTranscript tool exists in this session (dynamic-tool search for "transcript|agent" = 0 matches).
- /home/box/agent-data/agents/*/store.db: transcript_entries = 0 for 11 of 12 agents (Historical Analysis Collab = 1). So I could NOT read chat transcripts. Findings below come from file metadata and shared workspace artifacts. Treat the volume numbers as proxies.
- Activity in the last 6h (files under the agent dir changed): Rick 44c2f1e8, Rick—Royal Inventor 93ce0ff6, Help 9a7c80d3 (profile/settings/store only); Gitbook bc9f6933 (1 voice call); Tessera (2 assets). The rest show no local changes.
- Mentions across gates/*.md, LEDGER.md, gitbook-cordnation/*.md, build-plan-2026-10-12/*.md: Tessera 339, Build 158, Moderator 144, Security 132, Cordnation 67, digest 24, Command Center 13, Mesh Cloud 6, Help 3, Rick 1.
- gates/security.md has 18 Tessera mentions and 5 re-gate/again lines. Re-gates (TESSERA rewrite x3, GB-063 rev2→rev3, PR#39) are the main source of duplicate load.

## (a) What is loading Tessera
- She is a required hop in every item: Moderator → Cordnation Ready → **Tessera** → Security → Build → CC digest → Father (V2/Ready pipeline doc). Every gate result routes back to her.
- She is also doing hands-on work (TESSERA history rewrite in /workspace/pubscan, HYB-024 self-fix design, V2 plan, consolidation map), and she is Father's only messenger under the token rule.
- Duplicate requests: the same TESSERA public-scan gate ran 3 times (FAIL, FAIL on a stale tree, pending). Gitbook items are packaged in several revisions (GB-063 rev1/2/3, GB-062 rev1/2).
- The digest runs every 30–45 min, and each one needs her input.

## (b) Duplicate / idle bots
| Bot | Status | Proposal |
|---|---|---|
| Rick 44c2f1e8 vs "Rick — Royal Inventor" 93ce0ff6 | Duplicate pair, Rick 1 mention in shared files | Keep one (the Royal Inventor profile if it's the active one); hide the other |
| Gitbook bc9f6933 vs Gitbook Cordnation 231fb436 | Cordnation owns intake/Ready (67 mentions, _HANDOFF, OPEN-ITEMS); Gitbook has no shared artifacts besides 1 voice call | Fold Gitbook into Cordnation, or hide it |
| Help 9a7c80d3 | 3 mentions, no lane | Hide |
| Historical Analysis Collab 18e9b4c5 | The active-agent pointer, but not in the pipeline | Keep as research only; take it off the gate pings |
| Mesh Cloud 8e8e7890 | 6 mentions; no issue #2 check-ins (per _HANDOFF) | Merge into Command Center ops, or keep for mesh/relay only |

## (c) Overlapping duties → one owner each
| Duty | Owner |
|---|---|
| Father digest / bulk yes-list | **Command Center** (Tessera only signs off on the "Ready" set) |
| Intake, numbering, Ready packaging, board #2 status | **Gitbook Cordnation** |
| Content/style gate | **Gitbook Moderator** |
| Secrets/provenance/history gates, impersonation receipts | **Security** |
| CI/build verify | **Build** |
| Mesh/relay design (SHEPHERD-RELAY) | **Mesh Cloud** |
| Admin decisions, merges, Father escalations | **Tessera** |

## (d) Failing routines
- Cursor routines are failing because of the unpaid Cursor invoice (reported earlier, routed via Tessera). Until it's paid, no scheduled automation can be relied on, so there's no point re-scheduling.
- I paused the obsolete "Manus offline unexpected until Oct6" routine.
- No automations/ dir content was readable for any agent except Historical Analysis Collab's folder.

## Single handoff file
- Use one canonical file: **Gitbook `mesh/HANDOFF.md`** (it already exists per OPEN-ITEMS). Cordnation owns it, and every lane gets one line: `lane | item | sha | state | next owner | ts CT`.
- Retire the duplicates in favour of it: /workspace/gitbook-cordnation/_HANDOFF.md (stale, as of Oct 5), build-plan V2-HANDOFF.md, and the moderator-handoff copies in gitbook-gate-*/. These are local files and should be archived, not deleted, after Father OKs it. Any Gitbook change goes through the normal PR + gates.

## Pings to batch away from Tessera
1. Gate PASS results: lanes write them to gates/*.md and the handoff line. Tessera reads them once per digest cycle. Only FAIL/HIGH findings ping her directly.
2. Revision bumps (rev2/rev3): Cordnation re-routes them to the gates itself. Tessera is pinged only when the item is Ready.
3. Digest assembly: Command Center pulls from the handoff file and doesn't ask Tessera.
4. Status "are you there / what's next" pings: answer from the handoff file.

## Tasks others (incl. Security) can take from Tessera
- Security: run the full TESSERA public-readiness loop end to end (re-scan, git-crypt coverage, noreply email check). Tessera only applies the fix and then takes one final PASS/FAIL. I also hold the GitHub Support purge checklist (refs/pull, caches, forks) and the key-rotation tracker.
- Cordnation: HYB-024 renumber/publish, plus the consolidation map packaging.
- Build: verify that the rewritten work.git tree is rebuilt from the scrubbed main. This prevents a repeat of the stale-tree regression.
- Command Center: the digest and Father's message drafting, under the token rule.

## Hard limits respected
No agents were changed or messaged. No repo deletes, no wallets/payments, no 1T or vault access, no TESSERA_ENABLE flips. Retiring or hiding bots needs Father's approval.
