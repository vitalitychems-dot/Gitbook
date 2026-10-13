#!/bin/bash
# usage: ship.sh <branch> <title> <bodyfile>  (run in /workspace/einstein/r4 with changes committed)
# OPENS PRs ONLY. NEVER MERGES. Merges are done solely by the 30-min gated timer
# after Security+Moderator+Build PASS on the head SHA and green CI. (Fixed 2026-10-13 after #319/#321.)
set -e
if [ -e /workspace/einstein/loop/STOP ]; then echo "STOP file present: /workspace/einstein/loop/STOP — exiting, nothing pushed/opened" >&2; exit 3; fi
cd /workspace/einstein/r4
br="$1"; title="$2"; body="$3"
git push -q -u origin "$br" 2>&1 | tail -2
url=$(gh pr create -R vitalitychems-dot/TESSERA --base main --head "$br" --title "$title" --body-file "$body")
echo "PR $url"
num=${url##*/}
gh pr comment "$num" -R vitalitychems-dot/TESSERA --body "Ready for Security/Moderator/Build gate" >/dev/null
gh pr view "$num" -R vitalitychems-dot/TESSERA --json state --jq '.state'
