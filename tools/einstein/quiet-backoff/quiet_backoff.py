#!/usr/bin/env python3
"""Quiet-backoff gate timer (Gitbook #72 idea 5). Token-free.
Cron fires every BASE min. `due STATE` exits 1 (skip, no API call) until the backoff interval passes.
`seen STATE SHA` after fetching head: prints RUN on a new sha (interval resets to BASE), else IDLE (interval doubles to CAP).
Worst-case push-detect latency = CAP minutes (default 30)."""
import json,sys,time,os
BASE=int(os.environ.get("QB_BASE",5));CAP=int(os.environ.get("QB_CAP",30))
def due(st,now): return now>=st.get("next",0)
def seen(st,sha,now):
    if st.get("sha")!=sha: return "RUN",{"sha":sha,"iv":BASE,"next":now+BASE*60}
    iv=min(st.get("iv",BASE)*2,CAP); return "IDLE",{"sha":sha,"iv":iv,"next":now+iv*60}
if __name__=="__main__":
    cmd,f=sys.argv[1],sys.argv[2];now=time.time()
    st=json.load(open(f)) if os.path.exists(f) else {}
    if cmd=="due": sys.exit(0 if due(st,now) else 1)
    a,st=seen(st,sys.argv[3],now);json.dump(st,open(f,"w"));print(a)
