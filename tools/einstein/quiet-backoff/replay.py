#!/usr/bin/env python3
"""Replay real TESSERA commit times (data/pushes.txt.zst) through cron policies. Reproduces PR numbers.
Usage: python3 replay.py   (needs python zstandard or the zstd CLI)."""
import random,statistics as S,subprocess,os
from datetime import datetime as D,timedelta as TD
H=os.path.dirname(os.path.abspath(__file__))
def load(n):
    raw=subprocess.run(["zstd","-dc",f"{H}/data/{n}.zst"],capture_output=True,check=True).stdout.decode()
    return raw.splitlines()
P=sorted(D.fromisoformat(l.strip().rstrip("Z")) for l in load("pushes.txt") if l.strip())
def sim(base=5,cap=5,quiet_h=0,etag=False):
    """returns (wakes/day, full checks/day, latencies). quiet_h: back off only after quiet_h hours with no push.
    etag: every base-min tick does a conditional GET (304 free, not counted); full check only on change."""
    s,e=P[0],P[-1];now=s;iv=base;pi=0;last=s;wakes=full=0;lat=[]
    while now<e:
        now+=TD(minutes=iv);wakes+=1;new=[p for p in P[pi:] if p<=now]
        if etag: full+=bool(new)
        else: full+=1
        if new: lat+=[(now-p).total_seconds()/60 for p in new];pi+=len(new);last=new[-1];iv=base
        elif (now-last).total_seconds()>=quiet_h*3600: iv=min(iv*2,cap)
    d=(e-s).total_seconds()/86400;return wakes/d,full/d,lat
def ci(x,seed):
    r=random.Random(seed);b=sorted(S.mean(r.choices(x,k=len(x))) for _ in range(5000));return S.mean(x),b[125],b[4874]
if __name__=="__main__":
    print(f"commits={len(P)} span={(P[-1]-P[0])}")
    for name,kw in [("fixed5",{}),("backoff5-30",{"cap":30}),("backoff5-10",{"cap":10}),("quiet1h-30",{"cap":30,"quiet_h":1}),("quiet2h-30",{"cap":30,"quiet_h":2}),("quiet4h-30",{"cap":30,"quiet_h":4}),("etag5",{"etag":True})]:
        w,f,l=sim(**kw);cs=[ci(l,k) for k in range(5)]
        print(f"{name:12} wakes/day={w:6.1f} full_checks/day={f:6.1f} lat_mean={cs[0][0]:.2f} CI runs=" + " ".join(f"[{a:.2f},{b:.2f}]" for _,a,b in cs)+f" max={max(l):.1f}")
