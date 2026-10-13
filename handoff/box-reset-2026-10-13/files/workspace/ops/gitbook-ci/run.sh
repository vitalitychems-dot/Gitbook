#!/usr/bin/env bash
# Gitbook box CI. DRY_RUN=1 (default) prints statuses; LIVE=1 posts them.
set -uo pipefail
R=vitalitychems-dot/Gitbook; D=$(cd "$(dirname "$0")"; pwd)
REPO=/workspace/repos/Gitbook; CACHE=$D/cache.tsv; LOG=$D/runs.tsv
SCRIPT=$D/ci-check.pinned.sh; LIVE=${LIVE:-0}; API=0
touch "$CACHE"; [ -f "$LOG" ] || echo -e "run\tpr\tsha\tresult\tsecs\tdisk_kb\tapi" > "$LOG"
RUN=$(date +%s)
if [ ! -d "$REPO" ]; then
  git clone -q --bare --filter=blob:none --no-tags "https://github.com/$R.git" "$REPO" 2>/dev/null \
  || git clone -q --bare --filter=blob:none --no-tags "$(gh auth token >/dev/null && echo https://x-access-token:$(gh auth token)@github.com/$R.git)" "$REPO"
  git -C "$REPO" remote set-url origin "https://github.com/$R.git"
fi
PRS=$(gh api "repos/$R/pulls?state=open&per_page=100" --jq '.[]|"\(.number) \(.head.sha)"'); API=$((API+1))
while read -r N SHA; do
  [ -z "$N" ] && continue
  if grep -q "^$SHA	" "$CACHE"; then echo "PR #$N ${SHA:0:8} cached: $(grep "^$SHA	" "$CACHE"|cut -f2) (0 API, 0 s)"; echo -e "$RUN\t$N\t${SHA:0:8}\tcached\t0\t0\t0" >>"$LOG"; continue; fi
  T0=$(date +%s%3N); B0=$(du -sk "$REPO"|cut -f1)
  git -c credential.helper='!gh auth git-credential' -C "$REPO" fetch -q --filter=blob:none origin "refs/pull/$N/head" 2>/dev/null
  WT=$(mktemp -d /workspace/ops/gitbook-ci/wt.XXXX); git -C "$REPO" worktree add -q --no-checkout --detach "$WT" "$SHA" 2>/dev/null
  # sparse: only what ci-check.sh reads (json/jsonl/py + test dirs), never archive/history
  git -C "$WT" sparse-checkout set --no-cone '/*.json' '*.json' '*.jsonl' '*.py' '/tools/' '/mesh/' '!/archive/' '!/history/' 2>/dev/null
  git -c credential.helper='!gh auth git-credential' -C "$WT" checkout -q --detach "$SHA" 2>/dev/null
  PEAK=$(( $(du -sk "$REPO"|cut -f1) - B0 + $(du -sk "$WT"|cut -f1) ))
  (cd "$WT" && PYTHONDONTWRITEBYTECODE=1 timeout 300 bash "$SCRIPT" >"$WT.log" 2>&1); RC=$?
  [ $RC -eq 0 ] && ST=success || ST=failure
  DESC=$(grep -vE '^(==|ok |test_|Ran |$|OK)' "$WT.log" | tail -1 | cut -c1-120)
  git -C "$REPO" worktree remove --force "$WT"; rm -f "$WT.log"
  S=$(awk "BEGIN{printf \"%.1f\", ($(date +%s%3N)-$T0)/1000}")
  BODY="{\"state\":\"$ST\",\"context\":\"gitbook-ci\",\"description\":\"rc=$RC ${DESC//\"/}\"}"
  if [ "$LIVE" = 1 ]; then gh api -X POST "repos/$R/statuses/$SHA" --input - <<<"$BODY" >/dev/null; API=$((API+1)); A=1
  else echo "WOULD POST repos/$R/statuses/$SHA $BODY"; A=0; fi
  echo -e "$SHA\t$ST" >>"$CACHE"
  [ "$ST" = failure ] && echo "  reason: $DESC"; echo "PR #$N ${SHA:0:8} $ST ${S}s +${PEAK}KB"
  echo -e "$RUN\t$N\t${SHA:0:8}\t$ST\t$S\t$PEAK\t$A" >>"$LOG"
done <<<"$PRS"
git -C "$REPO" worktree prune
echo "API calls this run: $API (list) ; repo size $(du -sh "$REPO"|cut -f1)"
