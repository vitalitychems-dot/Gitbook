## Active claims — add row (or section)

```text
TASK: HYB-005
AGENT: Security (mesh security/privacy lane)
SCOPE: braces GHSA-vfj7-8cjw-p6xm via artifacts/mockup-sandbox > fast-glob > micromatch > braces; decision record merge/hyb-005-braces-decision.md; backlog HYB-005 row
START: 2026-10-05T19:06:00Z
BASE: TESSERA fec56eb ; Gitbook 6fe412f
STATUS: IN REVIEW → DONE (decision published; Father push pending)
NEXT CHECK-IN: 2026-10-05T20:06:00Z
BLOCKER: none
```

## Completed claims — append table row

| Task | Agent | Base | Commit | Checks | Date |
|---|---|---|---|---|---|
| HYB-005 | Security (mesh security/privacy lane) | TESSERA `fec56eb`; Gitbook `6fe412f` | *(Father push of staged docs)* | CI `pnpm audit` runs 37341568741 / 37348793133 / 37348832495; lockfile braces@3.0.3; decision ACCEPTED+MITIGATED review 2026-11-05 | 2026-10-05 |

## Completion block for agent-checkins.md

```text
TASK: HYB-005
AGENT: Security (mesh security/privacy lane)
STATUS: DONE (decision published; awaiting Father push)
BASE: TESSERA fec56eb ; Gitbook 6fe412f
COMMIT: none yet (staged via Gitbook Cordnation; Father pushes)
CHECKS: CI audit job 111894232164 on run 37348832495 (fec56eb) shows GHSA-vfj7-8cjw-p6xm high on artifacts__mockup-sandbox>fast-glob>micromatch>braces; lockfile braces@3.0.3; advisory patched versions None at run time
CHANGED: merge/hyb-005-braces-decision.md; intake/HYBRID-CONSOLIDATION-BACKLOG.md (HYB-005 row); history/coordination/agent-checkins.md
FOLLOW-UP: TESSERA CI narrow audit-ignore for GHSA-vfj7-8cjw-p6xm only (Father digest); monthly braces patch check; mandatory review 2026-11-05
```

## Backlog row replacement for HYB-005

| HYB-005 | Security owner | DONE (accepted + mitigated; review 2026-11-05) — [decision](../merge/hyb-005-braces-decision.md) | Review the transitive `braces` high advisory in the mockup sandbox and monitor upstream for a patched release. | Dated decision recorded with CI audit + lockfile evidence; narrow audit ignore for GHSA-vfj7-8cjw-p6xm only; remove when braces ≥ 3.0.4 ships. |
