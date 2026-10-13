#!/usr/bin/env bash
# diskguard: warn >=85%, clean regenerable caches >=90%. Idempotent; safe to cron.
set -u
WARN=${WARN:-85}; CLEAN=${CLEAN:-90}; LOG=${LOG:-/workspace/einstein/diskguard/diskguard.log}
exec 9>/tmp/diskguard.lock; flock -n 9 || exit 0
pct(){ df --output=pcent / | tail -1 | tr -dc 0-9; }
used(){ df --output=used -B1M / | tail -1 | tr -dc 0-9; }
ts(){ date '+%F %T %Z'; }
P=$(pct)
if [ "$P" -lt "$WARN" ]; then exit 0; fi
echo "$(ts) WARN disk at ${P}%" >>"$LOG"
[ "$P" -lt "$CLEAN" ] && exit 0
B=$(used)
# Only regenerable caches/temp. Never agent-data, /cursor/stores, repos, or other agents' files.
for t in "$HOME/.cache/pip" "$HOME/.cache/uv" "$HOME/.npm/_cacache" "$HOME/.cache/pnpm"; do
  [ -e "$t" ] && rm -rf "$t" 2>/dev/null
done
command -v pnpm >/dev/null && pnpm store prune >/dev/null 2>&1
find /tmp -maxdepth 1 -user "$(id -u)" \( -name 'playwright_chromiumdev_profile-*' -o -name 'node-compile-cache' -o -name 'tmp*' \) -mmin +120 -exec rm -rf {} + 2>/dev/null
find /tmp -maxdepth 1 -user "$(id -u)" -name 'grok-bot-attachment-*' -mtime +1 -exec rm -rf {} + 2>/dev/null
A=$(used)
echo "$(ts) CLEAN ${P}% -> $(pct)% freed $((B-A))MB" >>"$LOG"
