#!/usr/bin/env bash
# The pre-spawn autogate.sh rule block (Gitbook main 4dd0106, lines 110-116) run on a local repo, for the before/after benchmark.
set -uo pipefail
cd "$1"; BASE=$2; NOREPLY=332565808+vitalitychems-dot@users.noreply.github.com; GITLEAKS=${GITLEAKS:-/workspace/pubscan/gitleaks}; GLCONF=${GLCONF:-}
fail(){ echo "GATE FAIL: $*"; exit 1; }
git diff --name-only $BASE...HEAD > ../files
rg -q '^\.github/workflows/' ../files && fail "touches .github/workflows"
git diff $BASE...HEAD | rg -q '^\+.*TESSERA_ENABLE_[A-Z_]+\s*[:=]\s*["'"'"']?(1|true)' && fail "enables a TESSERA_ENABLE flag"
BAD=$(git log $BASE..HEAD --format='%ae' | sort -u | rg -v "^($NOREPLY|.*@users\.noreply\.github\.com)$" || true)
[ -n "$BAD" ] && fail "non-noreply author: $BAD"
if [ -x "$GITLEAKS" ]; then "$GITLEAKS" git --log-opts="$BASE..HEAD" ${GLCONF:+--config "$GLCONF"} . >/dev/null 2>&1 || fail "gitleaks findings"; fi
echo PASS
