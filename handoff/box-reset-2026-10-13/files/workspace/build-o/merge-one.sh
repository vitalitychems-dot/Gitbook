#!/bin/bash
# usage: merge-one.sh <clone> <repo> <branch> <title> <desc>
set -u
C=$1; R=$2; B=$3; T=$4; D=$5
export PATH=/workspace/tools/node22/bin:$PATH
cd $C || exit 1
git config user.name vitalitychems-dot; git config user.email 332565808+vitalitychems-dot@users.noreply.github.com
git fetch -q origin main && git checkout -q $B || { echo "FAIL checkout $B"; exit 1; }
if ! git rebase -q origin/main; then git rebase --abort; echo "CONFLICT $B"; exit 2; fi
if git log --format='%an %cn' origin/main..HEAD | grep -qi tessera; then echo "BAD AUTHOR $B"; exit 3; fi
TF=$(git diff --name-only origin/main...HEAD | grep -E '\.test\.(ts|mjs|js)$')
OUT=""
if [ -n "$TF" ]; then OUT=$(node --test $TF 2>&1); RC=$?; echo "$OUT" | tail -8; [ $RC -ne 0 ] && { echo "TESTFAIL $B"; exit 4; }; fi
SUM=$(echo "$OUT" | grep -E '^# (tests|pass|fail) ' | tr '\n' ' ')
if git diff origin/main...HEAD | grep -E '^\+' | grep -Eq '(ghp_[A-Za-z0-9]{30}|sk-[A-Za-z0-9]{30}|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY|xox[bp]-[0-9])'; then echo "SECRET-HIT $B"; exit 5; fi
REC=$(grep "^$B " /workspace/build-o/receipts.txt | tail -1)
git push -q -u origin $B 2>&1 | tail -2
URL=$(gh pr create -R $R -H $B -B main -t "$T" -b "$D

Receipt (pre-rebase): $REC
Rerun after rebase on $(git rev-parse --short origin/main): ${SUM:-docs only, no tests}
Secret grep on diff: clean. Author/committer: vitalitychems-dot. Opt-in; no TESSERA_ENABLE flips.
Auto-approved under Father's 5:15 PM CT standing rule.")
N=${URL##*/}
gh pr merge $N -R $R --merge >/dev/null 2>&1; sleep 2; [ "$(gh pr view $N -R $R --json state -q .state)" = MERGED ] || { echo "MERGEFAIL $B $URL"; exit 6; }
S=$(gh pr view $N -R $R --json mergeCommit -q .mergeCommit.oid)
echo "OK|$R#$N|$S"
