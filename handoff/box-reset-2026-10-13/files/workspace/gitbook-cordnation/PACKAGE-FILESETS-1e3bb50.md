# Package file sets and overlap check (Tessera ruling 2, 15:20 CT)

Main `1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea`, 0 open PRs (~15:21 CT). The sets come from the `+++ b/` paths in each current diff.

| Package | Files |
|---|---|
| GB-015 | mesh/roles/grok-bot.md |
| GB-016 rev 3 | intake/status-definitions.md, mesh/flow.md, mesh/roles.md, mesh/roles/build.md, mesh/roles/command-center.md, mesh/roles/gitbook-cordnation.md, **mesh/roles/mesh-lane-map.md**, mesh/roles/open-helper-agent-2.md, review/moderator-handoff.md |
| GB-017 | SUMMARY.md, mesh/flow.md, mesh/roles.md, mesh/roles/security.md (new), mesh/roles/tessera-pen.md |
| GB-018 | SUMMARY.md, history/coordination/agent-checkins.md, intake/HYBRID-CONSOLIDATION-BACKLOG.md, merge/hyb-005-braces-decision.md (new) |
| GB-019 | intake/CORTICAL-LABS-READINESS.md (new), intake/HYBRID-CONSOLIDATION-BACKLOG.md |
| GB-020 | brain-consciousness/AGENT-WORKPLAN.md, brain-consciousness/SNN-SOURCE-MANIFEST.md, brain-consciousness/TESSERA-PEN-RESEARCH-CHARTER.md |
| GB-021 | mesh/AGENT-SKILL-MATRIX.md, mesh/COLLABORATION-PLAYBOOK.md |

`mesh/roles/mesh-lane-map.md` is touched **only by GB-016 rev 3**, so the ruling-2 hunk is there and not in GB-021.

## OVERLAPS (flagged; these existed before this pass and are stacked by design)

| File | Packages | Current handling |
|---|---|---|
| mesh/flow.md | GB-017, GB-016 rev 3 | GB-016 rev 3 is built on GB-017's result; lands only after GB-017 |
| mesh/roles.md | GB-017, GB-016 rev 3 | same |
| SUMMARY.md | GB-017, GB-018 | separate hunks (Mesh vs Start-here); each applies solo and stacked |
| intake/HYBRID-CONSOLIDATION-BACKLOG.md | GB-018, GB-019 | GB-019 is built on GB-018; lands after GB-018 |

These four overlaps break the "no two packages touch the same file" rule. I didn't change them: GB-018 and GB-019 are frozen, and the GB-017 → GB-016 stacking is a standing Tessera decision. Options for Tessera:

- (a) accept them as ordered stacks;
- (b) merge GB-017 + GB-016 rev 3 into one package and GB-018 + GB-019 into another;
- (c) move the shared SUMMARY.md hunk into a single package.

GB-020 and GB-021 have no overlaps with any package.
