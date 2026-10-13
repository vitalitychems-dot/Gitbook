#!/usr/bin/env bash
# Zero-token offline worker: claim one job via commit+push to local bare repo, apply, record result. Exit 3 if queue empty.
set -euo pipefail; W=$1; cd "$W"
git pull -q --rebase origin main
j=$(ls queue/open/ 2>/dev/null | sort -n | head -1); [ -z "$j" ] && exit 3
mkdir -p queue/claimed results; git mv queue/open/$j queue/claimed/$j
git commit -qm "claim $j" && git push -q origin main || { git reset -q --hard origin/main; exit 0; }
f=$(python3 -c "import json;print(json.load(open('queue/claimed/$j'))['file'])")
l=$(python3 -c "import json;print(json.load(open('queue/claimed/$j'))['line'])")
echo "$l" >> "$f"; echo "{\"job\":\"$j\",\"ok\":true,\"tokens\":0}" > results/$j
git add -A && git commit -qm "done $j" && git push -q origin main
