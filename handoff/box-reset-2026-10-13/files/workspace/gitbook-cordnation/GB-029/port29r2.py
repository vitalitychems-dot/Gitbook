#!/usr/bin/env python3
"""GB-029 rev 2: rev 1 (port29.py) + GB-022..GB-025 rows -> published (PR #8, 979c35e) + GB-029 status 'in review'. Run on a 4565152 tree."""
import sys, os, subprocess
root = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(here, "port29.py"), root], check=True)
p = os.path.join(root, "intake/log.md"); s = open(p, encoding="utf-8").read()
NOTE = "Four gates cleared (Moderator, Tessera, Security, CI/Build); Father's yes 16:22 CT. Published 979c35e (PR #8, merged 16:30 CT)"
TAIL = f" | published | {NOTE} | Father (final yes) | Build PASS on PR #8 head cba4140d | none | none |"
for old_tail in [
  " | draft |  | Gitbook / Cordnation | git apply --check on ecd9022 | Cordnation hands to Gitbook Moderator (gate 1 of 4) | none |",
  " | draft |  | Gitbook / Cordnation | git apply --check on ecd9022 + GB-022, GB-024, GB-025 | Cordnation hands to Gitbook Moderator (gate 1 of 4) | none |",
  " | draft |  | Gitbook / Cordnation | git apply --check on ecd9022 + GB-022 | Cordnation hands to Gitbook Moderator (gate 1 of 4) | none |",
  " | draft |  | Gitbook / Cordnation | git apply --check on ecd9022 + GB-022, GB-024 | Cordnation hands to Gitbook Moderator (gate 1 of 4) | none |"]:
    assert s.count(old_tail + "\n") == 1, old_tail
    s = s.replace(old_tail + "\n", TAIL + "\n")
old = "| TBD | Moderator: pending |  | Gitbook Moderator |"; assert s.count(old) == 1
s = s.replace(old, "| TBD | in review |  | Gitbook Moderator |")
open(p, "w", encoding="utf-8").write(s); print("rev2 ok")
