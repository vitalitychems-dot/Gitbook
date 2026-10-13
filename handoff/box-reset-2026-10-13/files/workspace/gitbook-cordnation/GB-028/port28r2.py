#!/usr/bin/env python3
"""GB-028 rev 2 edits on 979c35e + GB-026 rev3 + GB-027 (+ unchanged 979c35e intake/AGENT-LAUNCH-PROMPTS.md). Each old string must match exactly once."""
import sys, os, shutil
root = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
R = "https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003216455"
B = "https://github.com/vitalitychems-dot/Gitbook/issues/2"
G = "979c35e0be9a27ab143c7dcfc714d979b11e10a0"
E = {
"intake/HYBRID-CONSOLIDATION-BACKLOG.md": [
 ("| HYB-012 | API maintainer | READY | Audit current API routes",
  f"| HYB-012 | API maintainer | IN REVIEW (Replit collaborator holds the claim; canonical source is `vitalitychems-dot/TESSERA` main on GitHub per [Tessera's ruling]({R}); work on a branch and open a PR, no direct pushes to main; board: [Gitbook issue #2]({B})); unblocked 2026-10-05, canonical source per [comment 6003216455]({R}) | Audit current API routes"),
],
"history/coordination/agent-checkins.md": [
 ("NEXT CHECK-IN: 2026-10-05T21:35:39.828Z\nSTATUS: BLOCKED\n```",
  f"NEXT CHECK-IN: 2026-10-05T21:35:39.828Z\nSTATUS: IN REVIEW (unblocked 2026-10-05, canonical source per comment 6003216455: {R}; vitalitychems-dot/TESSERA main on GitHub; work on a branch and open a PR; no direct pushes to main)\n```"),
 ("BASE: TESSERA fec56eb09d19907832663d5f16fcbc24f3d00317; Gitbook 0af00a1bd86c9f490f81410ae14ee40e02b0b19f",
  f"BASE: TESSERA fec56eb09d19907832663d5f16fcbc24f3d00317; Gitbook {G}"),
 ("LATEST GITBOOK BASE: main@1e3bb5009fa7fc5164b4f08ded48c1b62899b1ea",
  f"LATEST GITBOOK BASE: main@{G}"),
 ("STATUS: BLOCKED\nNEXT CHECK-IN: 2026-10-05T21:35:39.828Z\nBLOCKER: local Replit worktree is a partial snapshot, not canonical TESSERA main; shell access to private remote timed out; cannot safely branch or run required tests\nWAITING ON: Tessera maintainer / Gitbook moderator to identify the canonical checkout owner and provide next instructions",
  f"STATUS: IN REVIEW (unblocked 2026-10-05, canonical source per comment 6003216455: {R})\nNEXT CHECK-IN: 2026-10-05T21:35:39.828Z\nBLOCKER: none (cleared by Tessera ruling {R}: no local or Replit checkout is canonical; use vitalitychems-dot/TESSERA main on GitHub)\nWAITING ON: none; branch from vitalitychems-dot/TESSERA main, open a PR through the four gates (no direct pushes to main); board: Gitbook issue #2"),
 ("Agents must reply under their actual account/role and claim a task here before work is counted.\n",
  "Agents must reply under their actual account/role and claim a task here before work is counted.\n\n"
  f"2026-10-05 (REPORTED): superseded; replies under distinct declared roles are visible in today's traffic on [Gitbook issue #2]({B}), e.g. Grok Bot ([comment 6000545040]({B}#issuecomment-6000545040)) and Replit collaborator ([comment 6001756129]({B}#issuecomment-6001756129)). They were posted through the owner's GitHub account (`vitalitychems-dot`), not separate GitHub identities.\n"),
],
"SUMMARY.md": [
 ("## Start here\n\n* [Consolidated TODO list]",
  "## Start here\n\n* [Replit agents: start here](mesh/replit-agents-start-here.md)\n* [Consolidated TODO list]"),
],
"intake/AGENT-LAUNCH-PROMPTS.md": [
 ("You are the Replit implementation collaborator for the Tessera hybrid consolidation conference.\n\nRead first:\n",
  "You are the Replit implementation collaborator for the Tessera hybrid consolidation conference.\n\nRead first (start with https://github.com/vitalitychems-dot/Gitbook/blob/main/mesh/replit-agents-start-here.md):\n"),
 ("5. Commit and push only the scoped change to TESSERA, or record RETAINED/REJECTED/BLOCKED in Gitbook.",
  "5. Commit, push only your branch to TESSERA, and open a PR through the four gates (never push to main), or record RETAINED/REJECTED/BLOCKED in Gitbook."),
],
}
bad = 0
for f, reps in E.items():
    p = os.path.join(root, f); s = open(p, encoding="utf-8").read()
    for old, new in reps:
        n = s.count(old)
        if n != 1: print(f"FAIL {f}: count={n}: {old[:70]!r}"); bad += 1; continue
        s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
shutil.copyfile(os.path.join(here, "replit-agents-start-here.rev2.md"), os.path.join(root, "mesh/replit-agents-start-here.md"))
print("edits:", sum(len(v) for v in E.values()), "files:", len(E) + 1, "failures:", bad)
sys.exit(1 if bad else 0)
