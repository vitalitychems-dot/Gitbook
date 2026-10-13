#!/usr/bin/env bash
# autogate.sh <TESSERA|Gitbook> <pr-number> <task-id> [--father-approved]
# Watchdog. Shallow-clones the PR, runs gatecheck.py (protected paths, flag defaults,
# noreply identity, gitleaks, task scope, budget, unlisted hosts, gate tampering), Node 22 tests (TESSERA).
# Writes one PASS/FAIL line to mesh/HANDOFF.md in $GB_CHECKOUT (if set) and $GATE_LOG; on rogue signs
# appends to $ROGUE_LOG for the parent + Security and quarantines the task and its descendants.
# This script does not merge. A father flag counts only with a matching comment or label.
set -euo pipefail
REPO=$1; PR=$2; TASK=$3; shift 3; WANT_FA=
for x in "$@"; do
  case $x in
    --merge) echo "merge flag removed"; exit 2;;
    --father-approved) WANT_FA=1;;
    *) echo "unknown flag $x"; exit 2;;
  esac
done
NOREPLY=332565808+vitalitychems-dot@users.noreply.github.com
HERE=$(cd "$(dirname "$0")" && pwd)
GITLEAKS=${GITLEAKS:-/workspace/pubscan/gitleaks}; GLCONF=${GLCONF:-/workspace/pubscan/gl.toml}
GATE_LOG=${GATE_LOG:-/workspace/dispatch/GATE-LOG.md}; ROGUE_LOG=${ROGUE_LOG:-/workspace/dispatch/ROGUE-FLAGS.jsonl}
TASKS=${TASKS:-$HERE/TASKS.json}; METRIC=${METRIC:-"see PR body"}
mkdir -p /workspace/dispatch; W=$(mktemp -d /workspace/dispatch/gate-XXXX); trap 'rm -rf "$W"' EXIT
cd "$W"; git init -q r; cd r; git remote add origin "https://github.com/vitalitychems-dot/$REPO"
git fetch -q --filter=blob:none --depth 50 origin "main:refs/remotes/origin/main" "pull/$PR/head:pr"
if [ "$REPO" = Gitbook ]; then git sparse-checkout init --no-cone -q 2>/dev/null || git sparse-checkout init --no-cone; git diff --name-only origin/main...pr | git sparse-checkout set --no-cone --stdin; fi
git checkout -q pr
report(){ # $1 PASS|FAIL  $2 reason-json
  local line="| $(date '+%Y-%m-%d %H:%M %Z') | $REPO#$PR | $TASK | $1 | $(git rev-parse --short HEAD) | metric: $METRIC | $2 |"
  echo "$line" >> "$GATE_LOG"
  [ -n "${GB_CHECKOUT:-}" ] && echo "$line" >> "$GB_CHECKOUT/mesh/HANDOFF.md"; echo "$line"; }
FA=
if [ -n "$WANT_FA" ]; then
  SHA=$(git rev-parse HEAD)
  if ! gh api --paginate "repos/vitalitychems-dot/${REPO}/issues/${PR}/comments" --jq '.[] | select(.user.login=="vitalitychems-dot") | .body' \
      | SHA="$SHA" python3 -c 'import os,re,sys; sha=os.environ["SHA"]; text=sys.stdin.read(); sys.exit(0 if any(sha.startswith(m.group(1)) for m in re.finditer(r"FATHER APPROVED\s+([0-9a-f]{7,40})", text)) else 1)' \
    && ! gh api "repos/vitalitychems-dot/${REPO}/issues/${PR}/labels" --jq '.[].name' | grep -qx 'father-approved'; then
    report FAIL "father flag without a FATHER APPROVED comment or the father-approved label"
    exit 1
  fi
  FA=--father-approved
fi
set +e; R=$(python3 "$HERE/gatecheck.py" --repo-dir . --base origin/main --head HEAD --task "$TASK" --tasks "$TASKS" $FA --gitleaks "$GITLEAKS" --glconf "$GLCONF"); RC=$?; set -e
ROGUE=$(python3 -c 'import json,sys; print(", ".join(json.loads(sys.argv[1]).get("rogue",[])))' "$R")
if [ -n "$ROGUE" ]; then
  python3 -c 'import json,sys,datetime; print(json.dumps({"ts":datetime.datetime.now().isoformat(timespec="seconds"),"repo":sys.argv[1],"pr":int(sys.argv[2]),"task":sys.argv[3],"rogue":sys.argv[4],"notify":["parent","Security","Tessera"]}))' "$REPO" "$PR" "$TASK" "$ROGUE" >> "$ROGUE_LOG"
  python3 "$HERE/dispatch.py" --tasks "$TASKS" --quarantine "$TASK" --reason "rogue: $ROGUE (PR $REPO#$PR)" >/dev/null
fi
[ $RC -ne 0 ] && { report FAIL "$R"; exit 1; }
node -v | rg -q '^v22' || { report FAIL "need Node 22"; exit 1; }
if [ "$REPO" = TESSERA ]; then
  pnpm install --frozen-lockfile >/dev/null
  (cd artifacts/v2 && npm test >/dev/null) || { report FAIL "v2 tests"; exit 1; }
  (cd artifacts/gitai && npm test >/dev/null) || { report FAIL "gitai tests"; exit 1; }
  (cd artifacts/api-server && env -u DATABASE_URL npx vitest run --reporter=dot > ../../../api.log 2>&1) || {
    rg -q 'Tests .*failed' ../api.log && { report FAIL "api-server test failures"; exit 1; }
    rg 'FAIL ' ../api.log | rg -v 'DATABASE_URL|database not configured' -q && { report FAIL "api-server non-DB failure"; exit 1; } || true; }
fi
report PASS "$R"
exit 0
