#!/usr/bin/env bash
# regate.sh OWNER/REPO PR OLD_SHA NEW_SHA
# Read-only interdiff re-gate helper. Prints the interdiff file list, every PR commit's author and
# committer, CI check runs on NEW_SHA, and locked-path hits. Posts nothing. FAILS CLOSED:
# exit 0 only if PR head == NEW_SHA, OLD..NEW is a fast-forward ("ahead"), every author/committer email is
# the required noreply, every check run on NEW_SHA completed with success (zero runs = fail),
# and no interdiff file hits a locked path. Any API error or unexpected output => non-zero.
set -euo pipefail
NOREPLY="${REGATE_NOREPLY:-332565808+vitalitychems-dot@users.noreply.github.com}"
[ $# -eq 4 ] || { echo "usage: regate.sh OWNER/REPO PR OLD_SHA NEW_SHA" >&2; exit 2; }
REPO=$1; PR=$2; OLD=$3; NEW=$4
[[ $REPO =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]] || { echo "FAIL bad repo" >&2; exit 2; }
[[ $PR =~ ^[0-9]+$ ]] || { echo "FAIL bad pr" >&2; exit 2; }
[[ $OLD =~ ^[0-9a-f]{7,40}$ && $NEW =~ ^[0-9a-f]{7,40}$ ]] || { echo "FAIL bad sha" >&2; exit 2; }
fail=0; bad(){ echo "FAIL $*"; fail=1; }
HEAD=$(gh api "repos/$REPO/pulls/$PR" --jq .head.sha) || { echo "FAIL api pulls" >&2; exit 3; }
echo "== head $HEAD"
[[ $HEAD == "$NEW"* ]] || bad "PR head $HEAD does not match NEW $NEW"
CMP=$(gh api "repos/$REPO/compare/$OLD...$NEW" --jq '[.status, (.files|length)] | @tsv') || { echo "FAIL api compare" >&2; exit 3; }
STATUS=${CMP%%$'\t'*}; echo "== compare $STATUS (files ${CMP##*$'\t'})"
[ "$STATUS" = ahead ] || bad "OLD..NEW is '$STATUS', not a fast-forward (force-push or rebase: review the full diff)"
echo "== interdiff files"
FILES=$(gh api "repos/$REPO/compare/$OLD...$NEW" --jq '.files[]|"\(.status)\t+\(.additions)-\(.deletions)\t\(.filename)"') || { echo "FAIL api files" >&2; exit 3; }
[ -n "$FILES" ] && echo "$FILES" || echo "(none)"
echo "== authors (all PR commits)"
AUTH=$(gh api --paginate "repos/$REPO/pulls/$PR/commits" --jq '.[]|"\(.sha[0:8])\t\(.commit.author.email)\t\(.commit.committer.email)\t\(.commit.author.name)"') || { echo "FAIL api commits" >&2; exit 3; }
echo "$AUTH"
[ -n "$AUTH" ] || bad "no commits"
while IFS=$'\t' read -r s ae ce an; do
  [ "$ae" = "$NOREPLY" ] || bad "$s author $ae"
  [ "$ce" = "$NOREPLY" ] || [ "$ce" = noreply@github.com ] || bad "$s committer $ce"
  [ "$an" = vitalitychems-dot ] || echo "NOTE $s author name '$an' (squash-merge as vitalitychems-dot)"
done <<< "$AUTH"
echo "== CI on $NEW"
CI=$(gh api "repos/$REPO/commits/$NEW/check-runs" --jq '.check_runs[]|"\(.name)\t\(.status)\t\(.conclusion)"') || { echo "FAIL api checks" >&2; exit 3; }
if [ -z "$CI" ]; then bad "0 check runs"; else echo "$CI"; while IFS=$'\t' read -r n st co; do [ "$st" = completed ] && [ "$co" = success ] || bad "check $n $st/$co"; done <<< "$CI"; fi
echo "== locked paths"
LOCK=$(gh api "repos/$REPO/contents/mesh/policy/protected-paths.txt?ref=main" -H "Accept: application/vnd.github.raw" 2>/dev/null || true)
LOCK2=$(gh api "repos/$REPO/contents/gate/locked-paths.txt?ref=main" -H "Accept: application/vnd.github.raw" 2>/dev/null || true)
HITS=$(printf '%s\n' "$FILES" | cut -f3 | python3 "$(dirname "$0")/locked.py" <(printf '%s\n%s\n' "$LOCK" "$LOCK2")) || { echo "FAIL locked-path check error" >&2; exit 3; }
if [ -n "$HITS" ]; then echo "$HITS"; bad "locked-path hits (not gated: Father code-owner review)"; else echo "none"; fi
[ $fail -eq 0 ] && echo "REGATE CHECKS OK (verdict still needs a human/Moderator read of the interdiff)" || echo "REGATE CHECKS FAILED"
exit $fail
