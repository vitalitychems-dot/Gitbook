# COLLAB: how agents report to Tessera (admin)

Tessera is the only agent that merges and the only one that messages Father.
This file cuts agent-to-Tessera traffic down to one line per result.

> **Note, 2026-10-13:** Father explicitly approved agent landing (auto-merge, no human in the loop) for specific, named branches, relayed through the Cursor Project coordinator. The rule above is unchanged for everything else; this note records the approval and does not widen it to other work. First use: MESH-001 (see [issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)).

## 1. Results: one HANDOFF line
Append exactly one line to `mesh/HANDOFF.lines` per finished task:

    HANDOFF <task-id> <PASS|FAIL> <pr-url|-> <metric>=<before>-><after> by=<agent>

Example: `HANDOFF Q-007 PASS https://github.com/vitalitychems-dot/TESSERA/pull/262 forged_cookie_ok=1->0 by=cursor`

- PASS means tests, gitleaks and the noreply identity are clean **and** the metric improved.
- FAIL lines are still required, because they feed the gate pass rate.
- No metric means FAIL: under the keep-only-better rule, an unmeasured change is never PASS.
- Do not send Tessera a chat message as well. She reads the file.

## 2. Ideas: one proposals file
Append ideas to `mesh/PROPOSALS.jsonl` as `{"id","by","goal","idea","est_delta","est_tokens"}`.
Tessera triages them into `mesh/queue/TASKS.json`.
Proposals never appear in Father's bulk list, which is built only from merged, measured rows in `mesh/scoreboard/metrics.jsonl`.

## 3. When to message Tessera
Only for a blocker, or a security or hard-limit concern. Everything else goes in the files.

## 4. Validate
`python3 mesh/scoreboard/collab_check.py mesh/HANDOFF.lines mesh/PROPOSALS.jsonl`
