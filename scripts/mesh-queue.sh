#!/usr/bin/env bash
# mesh-queue.sh — orders open PRs for review: smallest diff first; risky PRs
# (auth, secrets, deletions, TESSERA_ENABLE_*) last. Writes /workspace/mesh/queue.json atomically.
# Fetches each PR's details only when its head SHA changes (cache in queue-cache.json).
set -euo pipefail
OWNER=${MESH_OWNER:-vitalitychems-dot} DIR=${MESH_DIR:-/workspace/mesh}
STATE=$DIR/state.json CACHE=$DIR/queue-cache.json
[ -s "$STATE" ] || exit 0; [ -s "$CACHE" ] || echo '{}' > "$CACHE"
hdr=(-H 'Accept: application/vnd.github+json'); [ -n "${GITHUB_TOKEN:-}" ] && hdr+=(-H "Authorization: Bearer $GITHUB_TOKEN")
get(){ curl -sSf "${hdr[@]}" "https://api.github.com$1"; }
cache=$(cat "$CACHE")
while read -r repo pr sha; do
  k="$repo#$pr@$sha"; [ "$(jq -r --arg k "$k" 'has($k)' <<<"$cache")" = true ] && continue
  p=$(get "/repos/$OWNER/$repo/pulls/$pr" | jq -c '{additions,deletions,title,body}') || continue
  f=$(get "/repos/$OWNER/$repo/pulls/$pr/files?per_page=100" | jq -c '[.[]|{filename,status,e:((.patch//"")|test("TESSERA_ENABLE_"))}]') || continue
  e=$(jq -c --argjson p "$p" '{lines:($p.additions+$p.deletions), del:$p.deletions,
     risky: (any(.[]; (.filename|test("auth|secret|credential|token|\\.env";"i")) or .status=="removed" or .e)
             or ($p.deletions > 2*($p.additions+1)) or (($p.title+" "+($p.body//""))|test("TESSERA_ENABLE_|secret|auth";"i")))}' <<<"$f")
  cache=$(jq -c --arg k "$k" --argjson e "$e" '.[$k]=$e' <<<"$cache")
done < <(jq -r 'to_entries[]|.key as $r|.value.prs|to_entries[]|"\($r) \(.key) \(.value.sha)"' "$STATE")
q=$(jq -c --argjson c "$cache" '[to_entries[]|.key as $r|.value.prs|to_entries[]|
     ("\($r)#\(.key)@\(.value.sha)") as $k | select($c[$k])|{repo:$r,pr:(.key|tonumber),sha:.value.sha}+$c[$k]]
     | sort_by(.risky, .lines)' "$STATE")
live=$(jq -c '[.[]|"\(.repo)#\(.pr)@\(.sha)"]' <<<"$q")
t=$(mktemp "$DIR/.c.XXXX"); jq -c --argjson l "$live" 'with_entries(select(.key as $k|$l|index($k)))' <<<"$cache" > "$t"; mv -f "$t" "$CACHE"
t=$(mktemp "$DIR/.q.XXXX"); jq . <<<"$q" > "$t"; mv -f "$t" "$DIR/queue.json"
