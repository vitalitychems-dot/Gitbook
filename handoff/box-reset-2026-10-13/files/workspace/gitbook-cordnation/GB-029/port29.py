#!/usr/bin/env python3
"""GB-029: append GB-026, GB-027, GB-028 (published) and GB-029 (Moderator: pending) rows to intake/log.md on 4565152."""
import sys, os
root = sys.argv[1]; p = os.path.join(root, "intake/log.md")
s = open(p, encoding="utf-8").read()
anchor = "| GB-025 | Coordination board moved to Gitbook issue #2 | Tessera (admin) via Cordnation | 2026-10-05 | Father's rule 3:56 PM CT | TBD | draft |  | Gitbook / Cordnation | git apply --check on ecd9022 + GB-022, GB-024 | Cordnation hands to Gitbook Moderator (gate 1 of 4) | none |\n"
assert s.count(anchor) == 1 and s.endswith(anchor)
RC = "[board receipt](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003943663)"
rows = [
 "| GB-026 | Cleanup rulings and Father's Tessera-push rule (rev 3) | Tessera (admin) via Cordnation | 2026-10-05 | Tessera rulings 16:22 and 16:29 CT; Father's rule 3:59 PM CT | TBD | published | "
 f"Four gates cleared (Moderator, Tessera, Security, CI/Build); Ready 16:47 CT; Father's yes 16:49 CT. Published ebe003f (PR #9, merged 17:00 CT; commit 1e107de5); {RC} | Father (final yes) | Build PASS on PR #9 head b23d9eb | none | none |",
 "| GB-027 | Command-center record restore, Origin/TESSERA merge wording, GB-026 leftovers | Tessera (admin) via Cordnation | 2026-10-05 | Tessera assignment; Tessera ruling 16:34 CT | TBD | published | "
 f"Four gates cleared (Moderator, Tessera, Security, CI/Build); Ready 16:47 CT; Father's yes 16:49 CT. Published ebe003f (PR #9, merged 17:00 CT; commit b23d9eb8); {RC} | Father (final yes) | Build PASS on PR #9 head b23d9eb | none | none |",
 "| GB-028 | Replit agents start-here page; HYB-012 IN REVIEW (rev 3) | Tessera (admin) via Cordnation | 2026-10-05 | Tessera task 16:41 CT (Father's 16:40 screenshot); Tessera rulings 16:42, 16:44, 16:47 CT | TBD | published | "
 f"Gates: Moderator 16:48 CT, Tessera (carried over from rev 2), Security 16:50 CT, Build 16:54 CT; Father's yes 16:49 CT. Published 4565152 (PR #10, merged 17:00 CT; commit c507f0c2); {RC} | Father (final yes) | Build PASS on PR #10 head c507f0c2 | none | none |",
 "| GB-029 | Intake log backfill for PR #9 and PR #10 | Gitbook / Cordnation | 2026-10-05 | Tessera assignment 17:01 CT | TBD | Moderator: pending |  | Gitbook Moderator | git apply --check on 4565152 | Gitbook Moderator reviews (gate 1 of 4) | none |",
]
s = s + "\n".join(rows) + "\n"
open(p, "w", encoding="utf-8").write(s)
print("rows added:", len(rows))
