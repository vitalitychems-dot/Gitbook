#!/bin/sh
# 7. Cron-able Shepherd runner (NOT installed). Example crontab: */15 * * * * /workspace/rick/tools/tesseract/run_feeds.sh
# Interval gating per feed via stamp files; lock prevents overlap. FIXDIR=... uses offline fixtures.
cd "$(dirname "$0")" || exit 1; S=state; mkdir -p $S; exec 9>$S/lock; flock -n 9 || { echo busy; exit 0; }
due() { f=$S/$1.stamp; now=$(date +%s); [ ! -f $f ] || [ $((now - $(cat $f))) -ge $2 ]; }
mark() { date +%s > $S/$1.stamp; echo "$(date -Is) ran $1" >> $S/runner.log; }
E=../tessera-eye
if due eye ${EYE_EVERY:-900}; then python3 $E/eye.py pull ${FIXDIR:+x $FIXDIR} >/dev/null 2>>$S/runner.err && mark eye; fi
if due feeds2 ${FEEDS2_EVERY:-3600}; then python3 $E/feeds2.py ${FIXDIR:+x x $FIXDIR} >/dev/null 2>>$S/runner.err && mark feeds2; fi
if due store ${STORE_EVERY:-900}; then python3 tesseract.py build >/dev/null && python3 -c "import tess2;print(tess2.health())" > $S/health.json && mark store; fi
