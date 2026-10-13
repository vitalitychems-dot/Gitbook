#!/usr/bin/env bash
# Tessera box autoclean: temp/cache purge, hardlink dedup, zstd archiving. Safe-by-default.
set -u; export LC_ALL=C
OPS=/workspace/ops; LOG=$OPS/autoclean.log; WARN=$OPS/DISK-WARN; ARCH=/workspace/archive
DRY=${DRY:-0}; LOCK=/tmp/.autoclean.lock
exec 9>$LOCK; flock -n 9 || { echo "$(date -Is) already running" >>$LOG; exit 0; }
log(){ echo "$(date -Is) $*" >>$LOG; [ -t 1 ] && echo "$*"; }
freeg(){ df -BG --output=avail / | tail -1 | tr -dc 0-9; }
usep(){ df --output=pcent / | tail -1 | tr -dc 0-9; }
# --- protection ---
protected(){ case "$1" in *secrets*|*1T*|*1t-*|*vault*|*Vault*|/home/box/agent-data*|/workspace/ops*|/workspace/archive*) return 0;; esac; return 1; }
recent(){ # any file in $1 modified within $2 minutes (skips .git internals)
  [ -n "$(find "$1" -xdev -path '*/.git' -prune -o -mmin -"$2" -print -quit 2>/dev/null)" ]; }
repo_unsafe(){ # 0 if any git repo under $1 is dirty/unpushed/unknown
  local g r
  while IFS= read -r g; do r=${g%/.git}
    [ -n "$(git -C "$r" status --porcelain 2>/dev/null | head -1)" ] && return 0
    git -C "$r" rev-parse @{u} >/dev/null 2>&1 || return 0
    [ -n "$(git -C "$r" log --oneline @{u}.. 2>/dev/null | head -1)" ] && return 0
    git -C "$r" status >/dev/null 2>&1 || return 0
  done < <(find "$1" -xdev -maxdepth 4 -name .git 2>/dev/null)
  return 1; }
rmsafe(){ protected "$1" && { log "SKIP protected $1"; return; }
  local s; s=$(du -sm "$1" 2>/dev/null | cut -f1); log "rm ${s}M $1"; [ "$DRY" = 1 ] || rm -rf --one-file-system "$1"; }
B=$(freeg); U=$(usep); log "=== start free=${B}G use=${U}% dry=$DRY"
AGE_TMP=120; AGE_NM=360; AGE_ARC=1440
if [ "$U" -ge 85 ]; then AGE_TMP=60; AGE_NM=180; echo "$(date -Is) WARN disk ${U}% free ${B}G -> aggressive" >>$WARN; log "AGGRESSIVE"; fi
# 1. /tmp clones & leftovers
for d in /tmp/gb* /tmp/tessera* /tmp/gate-* /tmp/ts /tmp/tsr /tmp/tmp* /tmp/pip-* /tmp/npm-*; do
  [ -e "$d" ] || continue; recent "$d" $AGE_TMP && continue
  repo_unsafe "$d" && { log "SKIP unpushed/dirty $d"; continue; }; rmsafe "$d"; done
# 2. caches
[ "$DRY" = 1 ] || { npm cache clean --force >/dev/null 2>&1; pnpm store prune >/dev/null 2>&1; pip cache purge >/dev/null 2>&1; }
log "caches pruned (npm/pnpm/pip)"
find /workspace /tmp -xdev -type d -name __pycache__ -mmin +$AGE_TMP -not -path '*secrets*' -not -path '*vault*' -not -path '*1T*' -prune -print 2>/dev/null | while read -r p; do [ "$DRY" = 1 ] || rm -rf "$p"; done
# node_modules in inactive clones (reinstallable)
find /workspace /tmp -xdev -maxdepth 4 -type d -name node_modules -prune -print 2>/dev/null | while read -r nm; do
  p=$(dirname "$nm"); protected "$nm" && continue
  [ -n "$(find "$p" -xdev -path '*/node_modules' -prune -o -path '*/.git' -prune -o -mmin -$AGE_NM -print -quit 2>/dev/null)" ] && continue
  [ -d "$p/.git" ] || [ -f "$p/package.json" ] || continue; rmsafe "$nm"; done
# 3. hardlink dedup on immutable-ish content only (git objects, archives, tarballs)
# git72: git objects are mode 444 and jdupes refuses read-only links (old step reclaimed 0); use util-linux
# hardlink -f on whole .git/objects (names are content hashes => safe). jdupes kept for archive dirs. MB reporting.
freem(){ df -BM --output=avail / | tail -1 | tr -dc 0-9; }
T=$(mktemp); find /workspace /tmp -xdev \( -path '*secrets*' -o -path '*vault*' -o -path '*1T*' -o -path /home/box/agent-data \) -prune -o -type d -path '*/.git/objects' -print 2>/dev/null >$T
if [ -s $T ] && command -v hardlink >/dev/null; then S1=$(freem)
  if [ "$DRY" = 1 ]; then xargs -a $T -d '\n' hardlink -n -f 2>/dev/null | tail -3 >>$LOG
  else xargs -a $T -d '\n' hardlink -q -f >/dev/null 2>&1; fi
  log "git-objects dedup dirs=$(wc -l <$T) reclaimed=$(( $(freem)-S1 ))M"; fi
if command -v jdupes >/dev/null; then
  find /workspace -xdev -maxdepth 2 -type f \( -name '*.tgz' -o -name '*.tar.*' -o -name '*.zst' -o -name '*.zip' \) -not -path '*secrets*' -not -path '*vault*' -not -path '*1T*' -printf '%h\n' 2>/dev/null | sort -u >$T
  if [ -s $T ]; then S1=$(freem)
    if [ "$DRY" = 1 ]; then jdupes -m $(cat $T) 2>/dev/null | tail -2 >>$LOG
    else jdupes -L -q $(cat $T) >/dev/null 2>&1; fi
    log "archive dedup dirs=$(wc -l <$T) reclaimed=$(( $(freem)-S1 ))M"; fi; fi
rm -f $T
# 4. compress finished top-level work dirs (>24h idle, no git repos) into archive
for d in /workspace/*/; do d=${d%/}; n=$(basename "$d")
  case "$n" in repos|archive|ops|secrets|agent-tools|node22|tools|backups) continue;; esac
  protected "$d" && continue; recent "$d" $AGE_ARC && continue
  [ -n "$(find "$d" -xdev -maxdepth 5 -name .git -print -quit)" ] && continue
  a=$ARCH/$n-$(date +%Y%m%d).tar.zst; log "archive $d -> $a"; [ "$DRY" = 1 ] && continue
  tar -C /workspace -cf - "$n" | zstd -19 --long=27 -T0 -q -o "$a" && zstd -t --long=27 -q "$a" \
   && [ "$(zstd -dc --long=27 "$a" | tar -tf - | wc -l)" -ge "$(find "$d" | wc -l)" ] \
   && rm -rf "$d" && log "archived+removed $n ($(du -h "$a"|cut -f1))" || { log "ARCHIVE FAIL $n kept"; rm -f "$a"; }
done
A=$(freeg); U2=$(usep); log "=== end free=${A}G use=${U2}% gained=$((A-B))G"
[ "$U2" -ge 85 ] && echo "$(date -Is) STILL ${U2}% after clean (free ${A}G) - needs list for Father" >>$WARN
exit 0
