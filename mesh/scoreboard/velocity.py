#!/usr/bin/env python3
"""Improvement velocity from metrics.jsonl + agents.jsonl. Optional --gh refreshes merge times via gh."""
import json,sys,os,datetime as D
H=os.path.dirname(os.path.abspath(__file__))
L=lambda n:[json.loads(l) for l in open(os.path.join(H,n)) if l.strip()]
def gain(m):
    b,a=m["before"],m["after"]
    if m["better"]=="hi": return (a-b)/abs(b) if b else 1.0
    return (b-a)/abs(b) if b else 0.0
def stats(attempted=None):
    M=L("metrics.jsonl");A=L("agents.jsonl")
    kept=[m for m in M if gain(m)>0];days=len({m["date"] for m in M}) or 1
    p=lambda s:D.datetime.fromisoformat(s.replace("Z","+00:00"))
    mins=sorted((p(a["merged"])-p(a["launched"])).total_seconds()/60 for a in A)
    prs={m["pr"] for m in kept};tok=sum(a["tokens_est"] for a in A)
    agent_kept=sum(1 for m in kept if m["pr"] in {a["pr"] for a in A})
    att=attempted or {"kept":len(kept),"tried":len(kept)}
    return {"kept_improvements":len(kept),"kept_per_day":len(kept)/days,"merged_prs":len(prs),
     "mean_pct_gain":round(100*sum(min(gain(m),10) for m in kept)/len(kept),1),
     "gate_pass_rate":round(att["kept"]/att["tried"],3),
     "launch_to_merge_min_median":round(mins[len(mins)//2],1),"launch_to_merge_min_max":round(mins[-1],1),
     "tokens_per_merged_improvement_est":round(tok/max(agent_kept,1))}
if __name__=="__main__":
    # Gate pass = items kept / items tried, 2026-10-13, from IDEAS-BUILD-1..4 and PR bodies:
    # B1 3/5, B2 3/5, B3 3/5, B4 3/4, Einstein 1/7, cloud agents (Q-003,Q-004,Q-007,#264,#58,#59) 6/6 -> 19/32
    print(json.dumps(stats({"kept":19,"tried":32}),indent=1))
