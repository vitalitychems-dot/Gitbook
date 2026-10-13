#!/usr/bin/env bash
# autogate.sh <TESSERA|Gitbook> <pr-number> <task-id> [--father-approved]
# Merge gate + watchdog. Shallow-clones the PR, runs gatecheck.py (protected paths, flag defaults,
# noreply identity, gitleaks, task scope, budget, unlisted hosts, gate tampering), Node 22 tests (TESSERA).
# Writes one PASS/FAIL line to mesh/HANDOFF.md in $GB_CHECKOUT (if set) and $GATE_LOG; on rogue signs
# appends to $ROGUE_LOG for the parent + Security and quarantines the task and its descendants.
# --father-approved is only honoured if GitHub shows Father's approval on this PR (see father_ok below).
# This script NEVER merges: merging is a manual step by Tessera after Moderator, Security and Build PASS.
set -euo pipefail
REPO=$1; PR=$2; TASK=$3; shift 3; FA=
for x in "$@"; do case $x in --merge) echo "autogate: --merge was removed; merge manually after all lane PASSes" >&2; exit 2;; --father-approved) FA=--father-approved;; *) echo "autogate: unknown option $x" >&2; exit 2;; esac; done
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
HEAD_SHA=$(git rev-parse HEAD)
# father_ok: --father-approved counts only if, via gh api on THIS PR, either
#  (a) the PR currently has label 'father-approved' and its most recent 'labeled' event was by actor vitalitychems-dot, or
#  (b) a PR comment by vitalitychems-dot contains 'FATHER APPROVED <full head sha>'.
# Fails closed: any gh/api/jq error => not approved.
# CAVEAT: all agents act through the shared vitalitychems-dot account, so this is a speed bump that
# leaves an auditable trail, NOT true separation of duties. Real separation needs a distinct Father
# identity plus branch protection requiring code-owner review.
father_ok(){
  local api="repos/vitalitychems-dot/$REPO/issues/$PR" lab actor cmt
  lab=$(gh api "$api/labels" --paginate --jq '.[].name' 2>/dev/null) || return 1
  if printf '%s\n' "$lab" | rg -qx 'father-approved'; then
    actor=$(gh api "$api/events" --paginate --jq '.[] | select(.event=="labeled" and .label.name=="father-approved") | .actor.login' 2>/dev/null | tail -n1) || return 1
    [ "$actor" = vitalitychems-dot ] && return 0
  fi
  cmt=$(gh api "$api/comments" --paginate --jq ".[] | select(.user.login==\"vitalitychems-dot\") | .body" 2>/dev/null) || return 1
  printf '%s\n' "$cmt" | rg -qF "FATHER APPROVED $HEAD_SHA" && return 0
  return 1
}
if [ -n "$FA" ] && ! father_ok; then
  echo "autogate: --father-approved given but no verifiable Father approval for $REPO#$PR @ $HEAD_SHA (or check could not run); ignoring it" >&2
  FA=
fi
report(){ # $1 PASS|FAIL  $2 reason-json
  local line="| $(date '+%Y-%m-%d %H:%M %Z') | $REPO#$PR | $TASK | $1 | $(git rev-parse --short HEAD) | metric: $METRIC | $2 |"
  echo "$line" >> "$GATE_LOG"
  [ -n "${GB_CHECKOUT:-}" ] && echo "$line" >> "$GB_CHECKOUT/mesh/HANDOFF.md"; echo "$line"; }
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
