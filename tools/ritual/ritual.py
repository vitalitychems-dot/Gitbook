#!/usr/bin/env python3
"""Ritual rounds: merge ROUND BUS [--weighted] [--answers F]
Lines: {"id","ts","from":AGENT,"to":"tessera","kind":"result","ref":ROUND,"body","agent":AGENT,"answers":[..],"conf":[..]}
Round is REJECTED if any line has from != agent, or any sender wrote more than one line."""
import json,sys,os,math,statistics,collections
D=os.path.dirname(os.path.abspath(__file__)); S="/cursor/stores/store-4a4964c9-b4a7-46f3-b945-b031beec8306"
ROUNDS={"live-3":(f"{D}/questions-3.json",f"{S}/answers-3.json"),"live-4":(f"{D}/questions-4.json",f"{S}/answers-4.json")}
def load_truth(qf,af):
    Q=json.load(open(qf)); T=json.load(open(af)); T=T.get("answers",T)
    return Q,[(lambda v: v["answer"] if isinstance(v,dict) else v)(T[str(q["id"])]) for q in Q]
def collect(rnd,bus,n):
    lines=[json.loads(l) for l in open(bus) if l.strip()]
    lines=[m for m in lines if m.get("ref")==rnd and m.get("kind")=="result"]
    errs=[]; cnt=collections.Counter(m.get("from") for m in lines)
    errs+= [f"sender {s} wrote {c} lines" for s,c in cnt.items() if c>1]
    errs+= [f"line {m.get('id')}: from={m.get('from')} != agent={m.get('agent')}" for m in lines if m.get("from")!=m.get("agent")]
    errs+= [f"line {m.get('id')}: needs {n} answers" for m in lines if len(m.get("answers",[]))!=n]
    if errs: print("ROUND REJECTED:\n  "+"\n  ".join(errs)); sys.exit(2)
    return {m["agent"]:(m["answers"],m.get("conf",[1]*n)) for m in lines}
def wmed(v,w):
    p=sorted(zip(v,w)); h=sum(w)/2; c=0
    for x,ww in p:
        c+=ww
        if c>=h: return x
def merge(ans,Q,weighted):
    out=[]
    for i,q in enumerate(Q):
        v=[a[i] for a,_ in ans.values()]; w=[max(c[i],1e-6) if weighted else 1 for _,c in ans.values()]
        if q["type"]=="num": out.append(wmed(v,w) if weighted else statistics.median(v))
        else:
            k=collections.Counter()
            for x,ww in zip(v,w): k[x]+=ww
            out.append(k.most_common(1)[0][0])
    return out
def err(a,Q,T):
    return statistics.mean(abs(math.log(max(float(a[i]),1e-9)/t)) if q["type"]=="num" else float(a[i]!=t) for i,(q,t) in enumerate(zip(Q,T)))
if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)<3 or a[0]!="merge": print(__doc__); sys.exit(0)
    rnd,bus=a[1],a[2]; qf,af=ROUNDS[rnd]
    if "--answers" in a: af=a[a.index("--answers")+1]
    Q,T=load_truth(qf,af); ans=collect(rnd,bus,len(Q)); w="--weighted" in a
    ind={k:err(v[0],Q,T) for k,v in ans.items()}; c=err(merge(ans,Q,w),Q,T)
    print(f"{rnd}: {len(ans)} agents, merge={'weighted' if w else 'plain'} (mean abs log error, lower is better)")
    for k,e in sorted(ind.items(),key=lambda x:x[1]): print(f"  {k:14s} {e:.4f}")
    print(f"  CONSENSUS      {c:.4f}   mean individual {statistics.mean(ind.values()):.4f}   beats {sum(c<e for e in ind.values())}/{len(ind)}")
