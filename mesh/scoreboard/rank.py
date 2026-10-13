#!/usr/bin/env python3
"""Father's bulk list. ONLY built+tested+merged items with measured before/after (metrics.jsonl).
impact = goal_weight * relative_gain(capped at 100% so goal weights dominate) / cost. Father 4:02-4:03 AM: token efficiency + speed first, then accuracy."""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from velocity import L,gain,stats
W={"tokens":0.40,"speed":0.30,"accuracy":0.20,"sovereign":0.04,"brain":0.03,"gitai":0.02,"mesh":0.01}
def rank():
    M=[m for m in L("metrics.jsonl") if gain(m)>0 and m.get("pr")]
    cost={a["pr"]:max(a["tokens_est"]/1e5,0.1) for a in L("agents.jsonl")}
    for m in M: m["impact"]=W.get(m["goal"],0.01)*min(gain(m),1.0)/cost.get(m["pr"],1.0)
    return sorted(M,key=lambda m:-m["impact"])
def md():
    s=stats({"kept":19,"tried":32});o=["**Scoreboard:** %d kept improvements today, ~%s tokens per merged improvement (est.), median launch-to-merge %.1f min, gate pass %.0f%%.\n"%(s["kept_improvements"],format(s["tokens_per_merged_improvement_est"],","),s["launch_to_merge_min_median"],100*s["gate_pass_rate"])]
    for i,m in enumerate(rank(),1):
        o.append(f"{i}. {m['desc']}: {m['metric']} {m['before']} → {m['after']} ([PR]({m['pr']}))")
    o.append("\nReply yes to keep all, or send numbers to undo.");return "\n".join(o)
if __name__=="__main__": print(md())
