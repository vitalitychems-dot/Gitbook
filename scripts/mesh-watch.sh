#!/usr/bin/env bash
# mesh-watch.sh — no-token PR watcher for cron. Writes only changes to changes.jsonl.
set -euo pipefail
OWNER=${MESH_OWNER:-vitalitychems-dot}
REPOS=${MESH_REPOS:-"TESSERA Gitbook"}
DIR=${MESH_DIR:-/workspace/mesh}
STATE=$DIR/state.json CHANGES=$DIR/changes.jsonl
command -v jq >/dev/null || { echo "mesh-watch: jq required" >&2; exit 1; }
mkdir -p "$DIR"; [ -s "$STATE" ] || echo '{}' > "$STATE"
exec 9>"$DIR/.lock"; flock -n 9 || exit 0
CALLF=$(mktemp); trap 'rm -f "$CALLF"' EXIT
api(){ # api <path> -> body on stdout; returns 2 on rate limit
  local out code; out=$(mktemp)
  code=$(curl -sS -o "$out" -w '%{http_code}' -H 'Accept: application/vnd.github+json' \
    ${GITHUB_TOKEN:+-H "Authorization: Bearer $GITHUB_TOKEN"} "https://api.github.com$1") || code=000
  echo >> "$CALLF"
  if [ "$code" = 200 ]; then cat "$out"; rm -f "$out"; return 0; fi
  rm -f "$out"
  if [ "$code" = 403 ] || [ "$code" = 429 ]; then echo "mesh-watch: rate limited ($1), skipping run" >&2; return 2; fi
  echo "mesh-watch: HTTP $code for $1" >&2; return 1
}
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
new='{}' ; events=""
old=$(cat "$STATE")
for repo in $REPOS; do
  prev=$(jq -c --arg r "$repo" '.[$r] // {}' <<<"$old")
  since=$(jq -r '.since // "1970-01-01T00:00:00Z"' <<<"$prev")
  pulls=$(api "/repos/$OWNER/$repo/pulls?state=open&per_page=100" | jq -c '[.[]|{number,head:{sha:.head.sha}}]') || { rc=$?; new=$(jq -c --arg r "$repo" --argjson p "$prev" '.[$r]=$p' <<<"$new"); [ $rc = 2 ] && break; continue; }
  # one call for all new comments in the repo since last run (incremental GATE counts)
  com=$(api "/repos/$OWNER/$repo/issues/comments?since=$since&sort=created&per_page=100" | jq -c '[.[]|select(.body|test("GATE"))|{created_at,issue_url,body:"GATE"}]') || { rc=$?; new=$(jq -c --arg r "$repo" --argjson p "$prev" '.[$r]=$p' <<<"$new"); [ $rc = 2 ] && break; continue; }
  cur=$(jq -c --argjson o "$(jq -c '.prs // {}' <<<"$prev")" --argjson c "$com" --arg since "$since" '
    [.[]|{k:(.number|tostring),sha:.head.sha}] | map(. as $p |
      {key:$p.k, value:{sha:$p.sha,
        gate:(($o[$p.k].gate // 0) + ([$c[]|select(.created_at>$since and (.issue_url|endswith("/"+$p.k)) and (.body|test("GATE")))]|length))}}) | from_entries' <<<"$pulls")
  ev=$(jq -c -n --arg ts "$ts" --arg r "$repo" --argjson o "$(jq -c '.prs // {}' <<<"$prev")" --argjson c "$cur" '
    ($c|to_entries[]| . as $e | ($o[$e.key]) as $p |
      if $p==null then {ts:$ts,repo:$r,pr:($e.key|tonumber),event:"opened",sha:$e.value.sha}
      else (if $p.sha!=$e.value.sha then {ts:$ts,repo:$r,pr:($e.key|tonumber),event:"pushed",sha:$e.value.sha} else empty end),
           (if $e.value.gate>$p.gate then {ts:$ts,repo:$r,pr:($e.key|tonumber),event:"gate_comment",sha:$e.value.sha,gate:$e.value.gate} else empty end)
      end)')
  for n in $(jq -r --argjson c "$cur" 'keys[]|select($c[.]==null)' <<<"$(jq -c '.prs // {}' <<<"$prev")"); do
    d=$(api "/repos/$OWNER/$repo/pulls/$n") || exit 0
    sha=$(jq -r .head.sha <<<"$d")
    if [ "$(jq -r .merged <<<"$d")" = true ]; then
      ev+=$'\n'$(jq -cn --arg ts "$ts" --arg r "$repo" --argjson n "$n" --arg s "$sha" '{ts:$ts,repo:$r,pr:$n,event:"merged",sha:$s}')
      ev+=$'\n'$(jq -cn --arg ts "$ts" --arg r "$repo" --argjson n "$n" --arg s "$sha" '{ts:$ts,repo:$r,pr:$n,event:"DONE",sha:$s}')
    else
      ev+=$'\n'$(jq -cn --arg ts "$ts" --arg r "$repo" --argjson n "$n" --arg s "$sha" '{ts:$ts,repo:$r,pr:$n,event:"closed",sha:$s}')
    fi
  done
  events+=$ev$'\n'
  new=$(jq -c --arg r "$repo" --arg t "$ts" --argjson c "$cur" '.[$r]={since:$t,prs:$c}' <<<"$new")
done
# first run only seeds state (no flood of "opened")
if [ "$old" != '{}' ]; then printf '%s' "$events" | sed '/^$/d' >> "$CHANGES"; fi
tmp=$(mktemp "$DIR/.state.XXXX"); echo "$new" > "$tmp"; mv -f "$tmp" "$STATE"
echo "mesh-watch: api_calls=$(wc -l < "$CALLF")" >&2

# (b) refresh the review queue when something changed (cached by head SHA)
if [ -n "$(printf %s "$events" | tr -d "\n")" ] && [ -x "$(dirname "$0")/mesh-queue.sh" ]; then "$(dirname "$0")/mesh-queue.sh" || true; fi
