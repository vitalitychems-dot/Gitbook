#!/usr/bin/env bash
# Gitbook CI: JSON validity (outside archive/history), Python syntax, and stdlib unit tests.
set -euo pipefail
echo "== JSON validity"
git ls-files '*.json' | grep -vE '^(archive|history)/' | while read -r f; do
  python3 -m json.tool "$f" >/dev/null || { echo "invalid JSON: $f"; exit 1; }
done
echo "== JSONL validity"
git ls-files '*.jsonl' | grep -vE '^(archive|history)/' | while read -r f; do
  python3 - "$f" <<'PY'
import json,sys
for i,l in enumerate(open(sys.argv[1]),1):
    if l.strip(): json.loads(l)
PY
done
echo "== Python syntax"
git ls-files '*.py' | grep -vE '^(archive|history)/' | xargs -r python3 -m py_compile
echo "== Unit tests"
(cd tools/shepherd && python3 -m unittest discover -p 'test_*.py' -v)
(cd mesh/queue/tests && python3 -m unittest test_spawn -v)
(cd mesh/scoreboard && python3 -c '
import test_scoreboard as t
fs=[n for n in dir(t) if n.startswith("test_")]
for n in fs: getattr(t,n)(); print("ok", n)
print(len(fs), "scoreboard tests passed")')
echo "CI OK"
