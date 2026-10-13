#!/usr/bin/env bash
# Runs all git72 benches, writes last_result.json (and baseline.json if absent). Aborts if / >=95%.
set -euo pipefail; cd "$(dirname "$0")"
u=$(df --output=pcent / | tail -1 | tr -dc 0-9); [ "$u" -ge 95 ] && { echo "disk ${u}% abort"; exit 1; }
python3 - <<'P'
import json,subprocess
r={k:json.loads(subprocess.check_output(["python3",f"{k}/run_bench.py"])) for k in ["gitweb","offline_queue","disk","speed"]}
json.dump(r,open("last_result.json","w"),indent=1)
import os
if not os.path.exists("baseline.json"): json.dump(r,open("baseline.json","w"),indent=1)
print(json.dumps(r))
P
rm -rf /tmp/git72*
