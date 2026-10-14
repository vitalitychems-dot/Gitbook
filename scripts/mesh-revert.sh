#!/usr/bin/env bash
# mesh-revert.sh <repo> — if main's head commit has failing checks, open a revert PR (never push main).
# Handled SHAs are kept in /workspace/mesh/revert-state.json, so each red commit gets one PR at most.
# Env: MESH_DRY_RUN=1 detects and logs without pushing.
set -euo pipefail
repo=${1:?repo}; OWNER=${MESH_OWNER:-vitalitychems-dot} DIR=${MESH_DIR:-/workspace/mesh}
here=$(cd "$(dirname "$0")" && pwd); ST=$DIR/revert-state.json; mkdir -p "$DIR"; [ -s "$ST" ] || echo '{}' > "$ST"
sha=${MESH_REVERT_SHA:-$(gh api "repos/$OWNER/$repo/commits/main" --jq .sha)}
[ "$(jq -r --arg k "$repo@$sha" 'has($k)' "$ST")" = true ] && exit 0
runs=$(gh api "repos/$OWNER/$repo/commits/$sha/check-runs?per_page=100" --jq '[.check_runs[]|{status,conclusion}]')
red=$(jq '[.[]|select(.status=="completed" and (.conclusion=="failure" or .conclusion=="timed_out"))]|length' <<<"$runs")
pending=$(jq '[.[]|select(.status!="completed")]|length' <<<"$runs")
st=$(gh api "repos/$OWNER/$repo/commits/$sha/status" --jq .state)
{ [ "$red" -gt 0 ] || [ "$st" = failure ]; } || { echo "main green/none at ${sha:0:12}"; exit 0; }
[ "$pending" = 0 ] || { echo "checks still running"; exit 0; }
if [ "${MESH_DRY_RUN:-0}" = 1 ]; then echo "DRY: would open revert PR for $sha"; exit 0; fi
br="revert/${sha:0:12}"
d=$(SW_SPARSE="${SW_SPARSE:-scripts}" "$here/shallow-work.sh" "revert-$repo" "https://github.com/$OWNER/$repo.git" main)
git -C "$d" fetch -q --depth 2 origin "$sha"
git -C "$d" checkout -q -b "$br"
m=(); [ "$(git -C "$d" rev-list --parents -n1 "$sha" | wc -w)" -gt 2 ] && m=(-m 1)
git -C "$d" -c user.name="Disk Cleaner" -c user.email="${NOREPLY:-332565808+vitalitychems-dot@users.noreply.github.com}" \
  revert --no-edit "${m[@]}" "$sha"
git -C "$d" -c user.name="Disk Cleaner" -c user.email="${NOREPLY:-332565808+vitalitychems-dot@users.noreply.github.com}" \
  commit -q --amend -m "$(git -C "$d" log -1 --format=%B)

main went red at $sha; auto revert PR.
Lane: disk-cleaner"
git -C "$d" push -q -u origin "$br"                  # new branch only; never main, never --force
url=$(gh pr create -R "$OWNER/$repo" -B main -H "$br" -t "Revert ${sha:0:12} (main red)" \
  -b "main is red at $sha ($red failing check runs, status=$st). This PR reverts that commit. It does not auto-merge, it goes through the gates.
Lane: disk-cleaner")
"$here/shallow-work.sh" finish "$d" "$br"
t=$(mktemp "$DIR/.r.XXXX"); jq -c --arg k "$repo@$sha" --arg u "$url" '.[$k]=$u' "$ST" > "$t"; mv -f "$t" "$ST"
jq -cn --arg ts "$(date -u +%FT%TZ)" --arg r "$repo" --arg s "$sha" --arg u "$url" '{ts:$ts,repo:$r,pr:null,event:"revert_pr",sha:$s,url:$u}' >> "$DIR/changes.jsonl"
echo "$url"
