#!/usr/bin/env bash
# Usage: gate-check.sh <diff> <expected-sha256> [base-dir]
# Fast doc-package gate: hash, shape, red flags, apply checks.
set -u
D="$1"; EXP="$2"; BASE="${3:-}"
echo "== hash"; GOT=$(sha256sum "$D"|cut -d' ' -f1); [ "$GOT" = "$EXP" ] && echo "OK $GOT" || echo "MISMATCH got $GOT"
echo "== shape"; echo "lines $(wc -l <"$D")"; grep -E '^\+\+\+ ' "$D" | sed 's/^+++ b\///'
echo "adds $(grep -cE '^\+[^+]' "$D")  dels $(grep -cE '^-[^-]' "$D")"
echo "== red flags (added lines)"
grep -nE '^\+' "$D" | grep -iE 'TESSERA_ENABLE_[A-Z_]*=\s*1|(api[_-]?key|secret|token|password)\s*[:=]\s*\S{8,}|ghp_|sk-[A-Za-z0-9]{20}|BEGIN (RSA|OPENSSH) PRIVATE|\.github/workflows|git push --force|rm -rf' || echo "none"
grep -qE '^\+\+\+ b/\.github/workflows' "$D" && echo "WORKFLOW EDIT"
grep -nE '^\+.*\b1T/' "$D" && echo "^ 1T path referenced (name-only ok)"
grep -nE '^\+.*collin-keane' "$D" && echo "^ personal handle"
echo "== unverified claims (check REPORTED)"; grep -nE '^\+.*(Father (said|yes|merged)|gates? (PASS|cleared))' "$D" | cut -c1-160 || true
if [ -n "$BASE" ]; then echo "== apply"; (cd "$BASE" && git apply --check "$D" && echo "fwd OK"; git apply --check -R "$D" 2>/dev/null && echo "already applied?" || true); fi
