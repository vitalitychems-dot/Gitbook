#!/usr/bin/env bash
# precheck.sh <repo> <pr> — cheap pre-gate checks for one PR. Posts a PRECHECK comment (never GATE).
# Checks: affected tests, gitleaks on the PR's new commit range only, and diff size.
# Env: OWNER (vitalitychems-dot), MAX_DIFF_LINES (800), PRECHECK_TEST_CMD (run with changed files as args),
#      PRECHECK_NO_POST=1 (dry run), MESH_DIR (/workspace/mesh)
set -euo pipefail
repo=${1:?repo} pr=${2:?pr}
OWNER=${OWNER:-vitalitychems-dot} MAX=${MAX_DIFF_LINES:-800} DIR=${MESH_DIR:-/workspace/mesh}
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$DIR"
info=$(gh api "repos/$OWNER/$repo/pulls/$pr" --jq '{b:.base.sha,h:.head.sha,ref:.head.ref,add:.additions,del:.deletions}')
base=$(jq -r .b <<<"$info") head=$(jq -r .h <<<"$info") ref=$(jq -r .ref <<<"$info")
lines=$(( $(jq -r .add <<<"$info") + $(jq -r .del <<<"$info") ))
d=$(SW_SPARSE="${SW_SPARSE:-scripts}" "$here/shallow-work.sh" "precheck-$repo-$pr" "https://github.com/$OWNER/$repo.git" "$ref")
cleanup(){ case "$d" in /workspace/tmp/?*) rm -rf -- "$d";; esac; }   # read-only clone, nothing to push
trap cleanup EXIT
git -C "$d" fetch -q --filter=blob:none origin "$base" "$head" 2>/dev/null || git -C "$d" fetch -q --deepen=200
files=$(git -C "$d" diff --name-only "$base...$head" 2>/dev/null || git -C "$d" diff --name-only "$base" "$head")
t=pass; tlog=""
for f in $(grep -E '\.sh$' <<<"$files" || true); do
  git -C "$d" show "$head:$f" >/dev/null 2>&1 || continue
  git -C "$d" show "$head:$f" | bash -n 2>/dev/null || { t=fail; tlog+="bash -n $f; "; }
done
if [ -n "${PRECHECK_TEST_CMD:-}" ] && [ -n "$files" ]; then (cd "$d" && $PRECHECK_TEST_CMD $files) >/dev/null 2>&1 || { t=fail; tlog+="PRECHECK_TEST_CMD; "; }; fi
if command -v gitleaks >/dev/null; then
  rep="$DIR/precheck-$repo-$pr-${head:0:12}.json"
  gitleaks git --log-opts="$base..$head" --report-path "$rep" --no-banner "$d" >/dev/null 2>&1 || true
  n=$(jq 'length' "$rep" 2>/dev/null || echo 0); s=$([ "$n" = 0 ] && echo pass || echo "fail($n, see $rep)")
else s="skipped(gitleaks not installed)"; fi
z=$([ "$lines" -le "$MAX" ] && echo pass || echo "warn($lines>$MAX)")
verdict=$( [ "$t" = pass ] || { echo fail; exit; }; case "$s" in fail*) echo fail;; skipped*) echo incomplete;; *) echo pass;; esac )
body="PRECHECK ${verdict} @ ${head:0:12} | tests: $t ${tlog} | secrets(range ${base:0:7}..${head:0:7}): $s | diff: $lines lines $z
(automated precheck; this is not a gate)"
[ "${PRECHECK_NO_POST:-0}" = 1 ] || gh api "repos/$OWNER/$repo/issues/$pr/comments" -f body="$body" >/dev/null
jq -cn --arg ts "$(date -u +%FT%TZ)" --arg r "$repo" --argjson p "$pr" --arg s "$head" --arg v "$verdict" --arg t "$t" --arg x "$s" --argjson l "$lines" \
  '{ts:$ts,repo:$r,pr:$p,event:"precheck",sha:$s,result:$v,tests:$t,secrets:$x,diff_lines:$l}' >> "$DIR/changes.jsonl"
echo "$body"
