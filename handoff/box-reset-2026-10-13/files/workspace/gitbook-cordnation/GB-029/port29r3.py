#!/usr/bin/env python3
"""GB-029 rev 3: rev 2 (port29r2.py) + GB-029 title + PR #8 board-receipt link in GB-022..025 notes. Run on a 4565152 tree."""
import sys, os, subprocess
root = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(here, "port29r2.py"), root], check=True)
p = os.path.join(root, "intake/log.md"); s = open(p, encoding="utf-8").read()
old = "Published 979c35e (PR #8, merged 16:30 CT) |"
assert s.count(old) == 4
s = s.replace(old, "Published 979c35e (PR #8, merged 16:30 CT); [board receipt](https://github.com/vitalitychems-dot/Gitbook/issues/2#issuecomment-6003345353) |")
old = "| GB-029 | Intake log backfill for PR #9 and PR #10 |"; assert s.count(old) == 1
s = s.replace(old, "| GB-029 | Intake log backfill for PR #8, PR #9, and PR #10 |")
open(p, "w", encoding="utf-8").write(s); print("rev3 ok")
