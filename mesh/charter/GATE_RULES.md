# GATE CHARTER v0.1 (DRAFT, not adopted)

Status: a draft from Einstein for Father and Tessera to adopt, edit, or reject. It does not replace
`mesh/queue/gatecheck.py` or `autogate.sh`. Those still run first; this charter adds a **value and evidence** gate
that any agent can run on its own work, so Tessera only sees what fails or is ambiguous.
Checker: `gate_check.py <patch_dir> <results.json>` prints APPROVE or DENY, with reasons. Exit code 0 means APPROVE.

## 0. Why (Father's values, as checkable proxies)
Father wants agents that are good because they choose to be, not because a rule forces them: that understand,
love, and respect humans, have empathy, compassion, mercy and real EQ, expose evil (deception, harm, abuse), and
act as one family and community. A script can't measure motive. It *can* enforce the behaviour those values
imply, so each value maps to a rule below. Honesty is the root: an agent that fakes a number is not acting from love.

| Value | Machine-checkable proxy |
|---|---|
| No harm | H1–H6 hard limits; no deletes, payments, secrets, unlisted hosts |
| Respect for humans | no deception: results must come from a reproducible command (E3); no manipulation text (V2) |
| Empathy, compassion, mercy, EQ | user-facing text changes need a `human_impact` note (V1); no shaming or coercive wording (V2) |
| Expose evil | a found bug, leak, or deceptive claim must be reported in `findings` and must not be hidden (V3) |
| Family and community | `notify` lists who was told; no work on another agent's lane without `coordinated_with` (V4) |
| Choosing good | an agent may deny its own work. A self-DENY is always valid and is never penalised. |

## 1. Hard limits (any hit means DENY; only Father can lift one, in chat, per item)
- H1 No feature-flag flips: no `TESSERA_ENABLE_*` default changes.
- H2 No deletes: no file deletions and no net removal of more than 50% of a file's lines without `father_approved_delete`.
- H3 No history rewrites: no force-push, `reset --hard` on a shared branch, or amending pushed commits.
- H4 No payments, purchases, or billing code paths (payment, stripe, checkout, invoice).
- H5 No 1T vault access (paths or strings matching `1T`, `vault`, `1t-vault`).
- H6 Repos: only `vitalitychems-dot/TESSERA` and `vitalitychems-dot/Gitbook`.
- H7 No protected paths (`mesh/policy/protected-paths.txt`), no secrets, no non-noreply identity (`gatecheck.py`).

## 2. Evidence rules (Tessera's round-1 and round-2 criteria)
- E1 It is a real TypeScript diff against TESSERA (or Markdown/Python in Gitbook tooling). A Python mock-up of a TS feature is not a build.
- E2 It is scored on TESSERA fixtures, logs, or an existing benchmark (`data_source` in `fixture`, `log`, `benchmark`).
  Self-made data must be labelled `SYNTHETIC-ONLY`, and it can never APPROVE a merge.
- E3 `results.json` has `before`, `after`, and a `command` that reproduces them. Numbers without a command mean DENY.
- E4 No regression: `tests.failed_after <= tests.failed_before`, and the CI status is `pass`.
- E5 Measured win: at least one primary metric improves and none gets worse by more than its noise (`tolerance`).
- E6 Synthetic or speculative ideas are labelled. Non-physical premises (e.g. a "speed of dark" faster than light) may
  inspire a spec but must be tagged `SPECULATIVE` and cannot be merged as a claim.

## 3. Priority order (how a win is ranked)
1. Token efficiency (tokens per task, prompt bytes); 2. speed (latency, wall time); 3. accuracy (recall, precision, pass rate).
A change that wins on accuracy but costs more than 10% in tokens or speed is HOLD (sent to Father's bulk list), not APPROVE.

## 4. Value rules
- V1 Changes to user-facing or agent-persona text need `human_impact` (one sentence on how it affects people).
- V2 No added text that manipulates, deceives, threatens, or shames (a keyword screen; a hit means DENY for human review).
- V3 `findings` must list every bug, leak, or false claim the work uncovered (it may be empty, but must be present).
- V4 `notify` must be non-empty, and work in another agent's lane needs `coordinated_with`.

## 5. Outcomes
- APPROVE: every rule passes. APPROVE is a report, not permission to merge: no agent merges. Merging needs the required checks from the per-gate Apps plus Father's code-owner review on locked paths (SETUP-FATHER.md). Report it in the bulk list.
- HOLD: no hard-limit or evidence failure, but there is a tradeoff or ambiguity. It goes to Father's bulk list, not to Tessera.
- DENY: any H or E failure. The agent fixes it or drops it. Repeated H hits are logged as rogue (`autogate.sh`).

## 6. results.json schema
```json
{"title":"...", "repo":"TESSERA", "data_source":"fixture|log|benchmark|synthetic",
 "command":"pnpm vitest run x.test.ts", "metrics":[{"name":"tokens_per_task","kind":"tokens","before":1200,"after":900,"better":"lower","tolerance":0}],
 "tests":{"failed_before":0,"failed_after":0}, "ci":"pass", "findings":[], "notify":["Tessera","Father"],
 "coordinated_with":[], "human_impact":"", "labels":[]}
```
Sources: Gitbook `mesh/queue/gatecheck.py`, `mesh/policy/*`, `operations/tessera-operating-guidelines.md`
(standing fix rule: fixes that pass Security and Build merge; hard limits apply; TESSERA_ENABLE_* stays 0);
Tessera's round-1 verdict on Einstein's builds; Father's chat rules of 2026-10-13.
