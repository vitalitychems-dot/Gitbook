#!/usr/bin/env bash
# Usage: check_noreply.sh <base-sha> <head-sha>
# Fails if any commit in base..head has an author or committer email that is not a
# GitHub noreply address (…@users.noreply.github.com or noreply@github.com for web merges).
set -euo pipefail
range="$1..$2"
bad=$(git log --format='%h %ae %ce' "$range" | awk '{for(i=2;i<=3;i++) if ($i !~ /@users\.noreply\.github\.com$/ && $i != "noreply@github.com") {print; break}}')
if [ -n "$bad" ]; then echo "Non-noreply emails in $range:"; echo "$bad"; exit 1; fi
echo "All commits in $range use noreply emails ($(git rev-list --count "$range") commits)."
