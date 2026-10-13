#!/usr/bin/env bash
# Offline tests for regate.sh: a stub `gh` serves canned JSON (filtered through real jq). Run: bash tools/gate/tests/test_regate.sh
set -u
HERE=$(cd "$(dirname "$0")" && pwd); RG="$HERE/../regate.sh"; T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/bin"; cat > "$T/bin/gh" <<'STUB'
#!/usr/bin/env bash
# stub: gh api [--paginate] PATH [-H ...] [--jq EXPR]
shift; [ "$1" = --paginate ] && shift; P=$1; shift; JQ=.
while [ $# -gt 0 ]; do case $1 in --jq) JQ=$2; shift 2;; -H) shift 2;; *) shift;; esac; done
[ -n "${STUB_FAIL:-}" ] && [[ $P == *$STUB_FAIL* ]] && { echo "stub fail" >&2; exit 1; }
case $P in
  */pulls/*/commits) J="[{\"sha\":\"aaaaaaaa1\",\"commit\":{\"author\":{\"email\":\"${STUB_AUTHOR:-332565808+vitalitychems-dot@users.noreply.github.com}\",\"name\":\"vitalitychems-dot\"},\"committer\":{\"email\":\"332565808+vitalitychems-dot@users.noreply.github.com\"}}}]";;
  */pulls/*) J="{\"head\":{\"sha\":\"${STUB_HEAD:-bbbbbbbb22}\"}}";;
  */compare/*) J="{\"status\":\"${STUB_STATUS:-ahead}\",\"files\":[{\"status\":\"modified\",\"additions\":1,\"deletions\":0,\"filename\":\"${STUB_FILE:-tools/x.py}\"}]}";;
  */check-runs) J=${STUB_CI:-}; [ -n "$J" ] || J='{"check_runs":[{"name":"validate","status":"completed","conclusion":"success"}]}';;
  */contents/*) exit 1;;
  *) exit 1;;
esac
printf '%s' "$J" | jq -r "$JQ"
STUB
chmod +x "$T/bin/gh"; export PATH="$T/bin:$PATH"
pass=0; failn=0
t(){ local want=$1 name=$2; shift 2; env "$@" bash "$RG" o/r 1 aaaaaaa bbbbbbbb22 >"$T/out" 2>&1; local got=$?; if [ $got -eq $want ]; then pass=$((pass+1)); echo "ok - $name"; else failn=$((failn+1)); echo "not ok - $name (exit $got, want $want)"; cat "$T/out"; fi; }
t 0 "clean interdiff passes"
t 1 "head mismatch fails" STUB_HEAD=cccccccc
t 1 "non-noreply author fails" STUB_AUTHOR=someone@example.com
t 1 "zero CI runs fails" STUB_CI='{"check_runs":[]}'
t 1 "red CI fails" STUB_CI='{"check_runs":[{"name":"validate","status":"completed","conclusion":"failure"}]}'
t 1 "pending CI fails" STUB_CI='{"check_runs":[{"name":"validate","status":"in_progress","conclusion":null}]}'
t 1 "force-push (diverged) fails" STUB_STATUS=diverged
t 1 "locked path fails (.github)" STUB_FILE=.github/workflows/ci.yml
t 1 "locked path fails (mesh/charter)" STUB_FILE=mesh/charter/GATE_RULES.md
t 3 "API error fails closed" STUB_FAIL=compare
bash "$RG" o/r 1 nothex bbbbbbbb >/dev/null 2>&1; [ $? -eq 2 ] && { pass=$((pass+1)); echo "ok - bad sha rejected"; } || { failn=$((failn+1)); echo "not ok - bad sha"; }
bash "$RG" o/r 1 >/dev/null 2>&1; [ $? -eq 2 ] && { pass=$((pass+1)); echo "ok - wrong arg count rejected"; } || { failn=$((failn+1)); echo "not ok - argc"; }
echo "# pass $pass fail $failn"; [ $failn -eq 0 ]
