#!/bin/bash
# DO NOT RUN until: cloud agents paused + Security re-gate PASS + Father go.
# Redoes the scrub on latest remote (paths, blob text, commit messages, mailmap),
# applies tree commits (fa9a92d8 git-crypt + 4f354393 .env widen from tree branch rebased), force-pushes heads only (no tags).
set -euo pipefail; export PATH=$HOME/.local/bin:$PATH; cd /workspace/pubscan
B=/workspace/backups/TESSERA-pre-public-2026-10-12.git
git -C $B fetch -q origin '+refs/*:refs/*'
rm -rf final.git && git clone -q --mirror --no-hardlinks $B final.git && cd final.git
git for-each-ref --format='delete %(refname)' refs/pull | git update-ref --stdin
git filter-repo --force --invert-paths --paths-from-file ../paths2.txt \
  --replace-text ../priv/expr.txt --replace-message ../priv/expr.txt
# remap any new non-noreply emails too
git log --all --format='%ae%n%ce' | sort -u | grep -v '@users.noreply.github.com$' \
  | sed 's/.*/vitalitychems-dot <332565808+vitalitychems-dot@users.noreply.github.com> <&>/' >> ../priv/mailmap.txt || true
git filter-repo --force --mailmap ../priv/mailmap.txt
git reflog expire --expire=now --all && git gc -q --prune=now
H=$(git log --all --format=%B | python3 -c "
import sys;m=sys.stdin.read()
L=[l.rstrip('\n').removeprefix('literal:').split('==>')[0] for l in open('../priv/expr.txt') if l.strip() and not l.startswith('regex:')]
print(sum(m.count(x) for x in L if x))")
[ "$H" = 0 ] || { echo "ABORT: $H secret literals in messages"; exit 1; }
E=$(git log --all --format='%ae%n%ce' | sort -u | grep -vc '@users.noreply.github.com$' || true)
[ "$E" = 0 ] || { echo "ABORT: $E non-noreply emails"; exit 1; }
cd .. && ./gitleaks git final.git --config gl.toml --redact --log-opts=--all
W=$(mktemp -d); git clone -q final.git "$W" && cd "$W"
git fetch -q /workspace/pubscan/tree rebased:tree-rebased
git -c user.name=vitalitychems-dot -c user.email=332565808+vitalitychems-dot@users.noreply.github.com \
  cherry-pick $(git rev-list --reverse 0f5eab28..tree-rebased)
git push -q /workspace/pubscan/final.git HEAD:refs/heads/main --force
cd /workspace/pubscan/final.git && rm -rf "$W"
git remote set-url origin https://github.com/vitalitychems-dot/TESSERA.git
echo FINAL_MAIN=$(git -C /workspace/pubscan/final.git rev-parse main)
