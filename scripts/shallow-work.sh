#!/usr/bin/env bash
# shallow-work.sh — disposable shallow clones for bot lanes.
#   shallow-work.sh <lane> <repo-url> [branch] [-- cmd...]   clone; print dir; optionally run cmd inside
#   env SW_SPARSE="dir1 dir2" limits checkout to those dirs (recommended for big repos)
#   shallow-work.sh finish <dir> [branch]                       verify HEAD == origin, then rm -rf dir
set -euo pipefail
ROOT=/workspace/tmp
die(){ echo "shallow-work: $*" >&2; exit 1; }
guard(){
  case "$1" in *agent-data*|/workspace/scan|/workspace/scan/*|/workspace/secscan|/workspace/secscan/*) die "refused protected path: $1";; esac
  local p; p=$(realpath -m -- "$1")
  case "$p" in *agent-data*|/workspace/scan|/workspace/scan/*|/workspace/secscan|/workspace/secscan/*) die "refused protected path: $p";; esac
  case "$p" in "$ROOT"/?*) ;; *) die "refused path outside $ROOT/: $p";; esac
  [ "$(dirname "$p")" = "$ROOT" ] || die "refused nested path: $p"
  printf '%s' "$p"
}
if [ "${1:-}" = finish ]; then
  [ $# -ge 2 ] || die "usage: finish <dir> [branch]"
  dir=$(guard "$2")
  [ -d "$dir/.git" ] || die "not a clone: $dir"
  br=${3:-$(git -C "$dir" rev-parse --abbrev-ref HEAD)}
  local_sha=$(git -C "$dir" rev-parse HEAD)
  remote_sha=$(git -C "$dir" ls-remote origin "refs/heads/$br" | cut -f1)
  [ -n "$remote_sha" ] || die "branch $br not on origin; keeping $dir"
  [ "$local_sha" = "$remote_sha" ] || die "HEAD $local_sha != origin/$br $remote_sha; keeping $dir"
  [ -z "$(git -C "$dir" status --porcelain)" ] || die "uncommitted changes; keeping $dir"
  rm -rf -- "$dir"; echo "removed $dir"; exit 0
fi
[ $# -ge 2 ] || die "usage: <lane> <repo-url> [branch] [-- cmd...] | finish <dir> [branch]"
lane=$1 url=$2; shift 2
[[ "$lane" =~ ^[A-Za-z0-9._-]+$ ]] || die "bad lane name"
br=""; if [ $# -gt 0 ] && [ "$1" != "--" ]; then br=$1; shift; fi
[ "${1:-}" = "--" ] && shift
mkdir -p "$ROOT"
dir=$(guard "$ROOT/$lane-$(date +%Y%m%d-%H%M%S)")
if [ -n "${SW_SPARSE:-}" ]; then  # e.g. SW_SPARSE="scripts docs": only check out these dirs
  git clone --depth 1 --filter=blob:none --sparse ${br:+--branch "$br"} -- "$url" "$dir" >&2
  git -C "$dir" sparse-checkout set $SW_SPARSE >&2
else
  git clone --depth 1 --filter=blob:none ${br:+--branch "$br"} -- "$url" "$dir" >&2
fi
echo "$dir"
if [ $# -gt 0 ]; then (cd "$dir" && "$@"); fi
