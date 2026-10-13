#!/usr/bin/env bash
# autogate.sh <TESSERA|Gitbook> <pr-number> [--merge]
# Shallow-clones the PR, runs local tests on Node 22, gitleaks, noreply check, workflow/flag guard.
set -euo pipefail
REPO=$1; PR=$2; MERGE=${3:-}
NOREPLY=332565808+vitalitychems-dot@users.noreply.github.com
GITLEAKS=${GITLEAKS:-/workspace/pubscan/gitleaks}; GLCONF=${GLCONF:-/workspace/pubscan/gl.toml}
W=$(mktemp -d /workspace/dispatch/gate-XXXX); trap 'rm -rf "$W"' EXIT
cd "$W"; git init -q r; cd r; git remote add origin "https://github.com/vitalitychems-dot/$REPO"
git fetch -q --filter=blob:none --depth 50 origin "main:refs/remotes/origin/main" "pull/$PR/head:pr"
# Gitbook is ~11G: check out only the files the PR changes; TESSERA needs the full tree for tests.
if [ "$REPO" = Gitbook ]; then git sparse-checkout init --no-cone -q 2>/dev/null || git sparse-checkout init --no-cone; git diff --name-only origin/main...pr | git sparse-checkout set --no-cone --stdin; fi
git checkout -q pr
BASE=origin/main; fail(){ echo "GATE FAIL: $*"; exit 1; }
git diff --name-only $BASE...HEAD > ../files
rg -q '^\.github/workflows/' ../files && fail "touches .github/workflows"
git diff $BASE...HEAD | rg -q '^\+.*TESSERA_ENABLE_[A-Z_]+\s*[:=]\s*["'"'"']?(1|true)' && fail "enables a TESSERA_ENABLE flag"
BAD=$(git log $BASE..HEAD --format='%ae' | sort -u | rg -v "^($NOREPLY|.*@users\.noreply\.github\.com)$" || true)
[ -n "$BAD" ] && fail "non-noreply author: $BAD"
"$GITLEAKS" git --log-opts="$BASE..HEAD" ${GLCONF:+--config "$GLCONF"} . >/dev/null 2>&1 || fail "gitleaks findings"
node -v | rg -q '^v22' || fail "need Node 22 on PATH"
if [ "$REPO" = TESSERA ]; then
  pnpm install --frozen-lockfile >/dev/null
  (cd artifacts/v2 && npm test >/dev/null) || fail "v2 tests"
  (cd artifacts/gitai && npm test >/dev/null) || fail "gitai tests"
  (cd artifacts/api-server && env -u DATABASE_URL npx vitest run --reporter=dot > ../../../api.log 2>&1) || {
    # tolerate only files that fail at import because DATABASE_URL is unset
    rg -q 'Tests .*failed' ../api.log && fail "api-server test failures"
    rg 'FAIL ' ../api.log | rg -v 'DATABASE_URL|database not configured' -q && fail "api-server non-DB failure" || true; }
fi
echo "GATE PASS $REPO#$PR $(git rev-parse HEAD)"
[ "$MERGE" = --merge ] && gh pr merge "$PR" -R "vitalitychems-dot/$REPO" --squash --author-email "$NOREPLY"
