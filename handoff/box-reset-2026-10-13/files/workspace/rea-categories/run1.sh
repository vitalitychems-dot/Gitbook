#!/bin/bash
r=$1; s=${r//\//__}; d=repos/$s
export PATH=/workspace/tools/node22/bin:$PATH
[ -d $d ] || timeout 300 git clone -q --depth 1 --single-branch --filter=blob:limit=1m https://github.com/$r $d 2>/dev/null || { echo '{"status":"clone_failed"}' > rea/$s.json; exit; }
js=$(cd $d && git ls-files | grep -cE '\.(js|mjs|cjs|ts|tsx|jsx)$'); py=$(cd $d && git ls-files | grep -c '\.py$'); tot=$(cd $d && git ls-files | wc -l)
timeout 420 npx -y rea-agents@6.4.0 analyze-javascript-application $d --json > rea/$s.raw 2> rea/$s.err; rc=$?
python3 extract.py rea/$s.raw | jq -c --arg rc $rc --argjson js $js --argjson py $py --argjson tot $tot --arg r $r '.+{repo:$r,exit:($rc|tonumber),files_total:$tot,js_ts_files:$js,py_files:$py}' > rea/$s.json
rm -f rea/$s.raw; rm -rf $d
