# Frozen-five check against main e73fb185 (check only; nothing was edited)

- Checked 2026-10-05 ~15:17 CT by Cordnation. Main HEAD: `e73fb185321fcb9e65eb61641ec8745bac85791d`, parent `beadc44`. Open PRs: none.
- `sha256sum -c FROZEN-SHA256-status.txt`: all 6 OK (GB-015, GB-017, GB-016 rev3, GB-016, GB-018, GB-019).
- Snapshot: /tmp/g/e73snap holds every file the five diffs touch. beadc44 blobs were hash-verified, and the e73 patch was applied to SUMMARY.md and mesh/flow.md. The resulting blobs match e73 exactly: `a23ad3c` and `56f4685`.

## Files e73fb185 changed

- SUMMARY.md (M, +3)
- intake/agent-submission-format.md (M, +8)
- mesh/flow.md (M, +21/−11)
- mesh/AGENT-SKILL-MATRIX.md (A)
- mesh/COLLABORATION-METRICS.md (A)
- mesh/COLLABORATION-PLAYBOOK.md (A)

Two of these overlap with frozen diffs: SUMMARY.md (GB-017, GB-018) and mesh/flow.md (GB-017, GB-016 rev3).

## Apply checks (`git apply --check -p1`)

Stacked:

| Step | Result |
|---|---|
| GB-015 | OK |
| GB-017 | **FAIL**: mesh/flow.md hunk #2 (`@@ -38,6 +38,7`, adds the "Tessera identity" row) and hunk #3 (`@@ -48,6 +49,7`, adds the "Security" lane line) |
| GB-016 rev3 | not checkable (needs GB-017). Informational run with GB-017 partly applied: both mesh/flow.md hunks rejected (`@@ -5,21 +5,29` and `@@ -34,18 +42,22`); its other 8 files apply |
| GB-018 → GB-019 | OK (on e73 + 015 + 017-partial, and also on e73 + 015 only) |

Solo:

| Diff | Result |
|---|---|
| GB-015 | OK |
| GB-018 | OK |
| GB-019 | OK |

Why the checks fail (strict context, no fuzz):

- **GB-017 hunk #2:** the trailing context expects `| Private docs repo |` then a blank line then `## Lane boundaries`. e73 inserted 3 rows (Task lock / Evidence / Status truth) after Private docs repo.
- **GB-017 hunk #3:** the context expects `- **Build** …` followed directly by `- **Provisional/TBD lanes** …`. e73 inserted `- **All lanes** …` between them.
- GB-017's other hunks apply: flow.md hunk #1 (front matter), SUMMARY (offset +3), security.md, tessera-pen.md, roles.md.
- **GB-016 hunk 1** rewrites the End-to-end flow sentence and the mermaid block. Its `-` lines are the beadc44 text, which e73 replaced (discover/claim, Moderator → Build, new node letters).
- **GB-016 hunk 2:** the context expects GB-017's Tessera identity row and the beadc44 rows/lane lines that e73 changed.
- This is a real content conflict, not just context drift. GB-016 and e73 both rewrite the same pipeline sentence and diagram in different ways, so a rebase needs a content decision.

## Silent overwrite / revert risk

- **Applied as diffs:** nothing silently overwrites e73.
  - The SUMMARY hunks (GB-017 Grok Bot line, GB-018 HYB-005 line) don't touch e73's 3 nav lines. Verified after applying: lines 34–36 are still present.
  - flow.md fails loudly.
- **Applied by copying `proposed/` whole files:** this **would** silently revert e73. GB-017/proposed/SUMMARY.md, GB-018/proposed/SUMMARY.md, GB-017/proposed/mesh/flow.md and GB-016/rev3/proposed/mesh/flow.md were all built on beadc44 and contain none of e73's lines. Copying them would:
  - drop the 3 SUMMARY nav links;
  - drop the flow.md discover/claim + Build step, the new mermaid, the 3 standing-rule rows, the All lanes line and the 3 related links.
- Forcing GB-016 hunk 1 by hand would also replace e73's pipeline sentence and diagram.

## What e73 says about pipeline and promotion

- **flow.md:** Agents discover → claim one task → produce work → Cordnation → Moderator → **Build** verifies → Command Center → Father Ready/yes → Father pushes → `merge`. It has **no Tessera or Security gate.** It also adds task-lock, evidence and status-truth rows, plus an "All lanes" check-in line.
- **COLLABORATION-PLAYBOOK.md:** loop Discover → **Claim** → Plan → Build → Verify → Handoff → Review ("Moderator checks scope, provenance, tests, security, and duplication") → "**Promote or defer** — accepted work becomes a TESSERA/Gitbook task". No Tessera or Security gate and no Father yes before promotion. Escalation: "Product or consciousness claim → Tessera Pen + Moderator" (Pen as a reviewer). "Publication or deletion request → Father".
- **AGENT-SKILL-MATRIX.md:** "Use skill IDs in every task claim". It lists Tessera Pen and Brain/SNN research as lanes.
- **intake/agent-submission-format.md:** adds a closure rule and new fields.
- This matches the Moderator's note: "promote" wording, and the pipeline is missing the Tessera and Security gates.
