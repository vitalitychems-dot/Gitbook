#!/usr/bin/env python3
"""Ritual round: shared problem -> answers on mesh bus -> consensus merge -> scoring.
usage: ritual.py create ROUND BUS | merge ROUND BUS [--weighted] [--questions F] [--answers F]
(live-2 defaults to questions-2.json + ~/.akhenaten-private/answers-2.json) | simulate [TRIALS]
questions.json = what agents see; answers.json = ground truth (never shown to agents).
Answer envelope: kind=result, ref=ROUND, agent=NAME, answers=[20 values], conf=[20 numbers 0..1]."""
import json, sys, random, statistics, collections, datetime, math, os
D=os.path.dirname(os.path.abspath(__file__))
ROUNDS={"live-2":(f"{D}/questions-2.json",os.path.expanduser("~/.akhenaten-private/answers-2.json")),"live-3":(f"{D}/questions-3.json",os.path.expanduser("~/.akhenaten-private/answers-3.json"))}
A1=os.path.expanduser("~/.akhenaten-private/answers.json")
def load(qf=f"{D}/questions.json",af=A1):
    global QS,TR,NCAT
    QS=json.load(open(qf)); T=json.load(open(af))
    TR=[(T[str(q["id"])]["answer"] if isinstance(T[str(q["id"])],dict) else T[str(q["id"])]) for q in QS]
    NCAT=sum(q["type"]=="cat" for q in QS)
def opt(a,k): return a[a.index(k)+1] if k in a else None
load()
def now(): return datetime.datetime.now().astimezone().isoformat(timespec="seconds")
def create(rnd,bus):
    with open(bus,"a") as f: f.write(json.dumps({"id":f"{rnd}-ask","ts":now(),"from":"tessera","to":"all","kind":"ask","ref":rnd,"body":f"Ritual {rnd}: all agents answer now","questions":QS})+"\n")
def collect(rnd,bus):
    out={}
    for l in open(bus):
        if l.strip():
            m=json.loads(l)
            if m.get("ref")==rnd and m["kind"]=="result" and "agent" in m and len(m.get("answers",[]))==len(QS):
                out[m["agent"]]=(m["answers"],m.get("conf",[1]*len(QS)))
    return out
def wmedian(v,w):
    p=sorted(zip(v,w)); half=sum(w)/2; c=0
    for x,ww in p:
        c+=ww
        if c>=half: return x
def merge(ans,weighted=False):
    out=[]
    for i,q in enumerate(QS):
        vw=[(a[i],(c[i] if weighted else 1)) for a,c in ans.values() if a[i] is not None]
        v=[x for x,_ in vw]; w=[max(ww,1e-6) for _,ww in vw]
        if q["type"]=="num": out.append(wmedian(v,w) if weighted else statistics.median(v))
        else:
            cnt=collections.Counter()
            for x,ww in zip(v,w): cnt[x]+=ww
            out.append(cnt.most_common(1)[0][0])
    return out
def score(a):
    ne=[abs(math.log(float(a[i])/t)) for i,(q,t) in enumerate(zip(QS,TR)) if q["type"]=="num"]
    ce=sum(a[i]!=t for i,(q,t) in enumerate(zip(QS,TR)) if q["type"]=="cat")
    return statistics.mean(ne),ce
def report(rnd,bus,weighted=False):
    ans=collect(rnd,bus); cs=score(merge(ans,weighted))
    print(f"round {rnd}: {len(ans)} agents, merge={'weighted' if weighted else 'plain'}")
    for k,(a,_) in sorted(ans.items()):
        s=score(a); print(f"  {k:12s} num_logerr={s[0]:.4f} cat_wrong={s[1]}/{NCAT}")
    print(f"  CONSENSUS    num_logerr={cs[0]:.4f} cat_wrong={cs[1]}/{NCAT}")
def sim_agents(rng,n,shared):
    # shared: per-question bias common to all agents (herding / same training data)
    qb=[rng.gauss(0,0.25) if shared else 0 for _ in QS]
    qwrong=[rng.choice([o.split("=")[0][-1] for o in q["q"].split("?")[1].split() if "=" in o and o.split("=")[0][-1]!=t]) if q["type"]=="cat" else None for q,t in zip(QS,TR)]
    agents=[]
    for _ in range(n):
        skill=rng.uniform(0.1,0.6); over=rng.uniform(-0.3,0.3)  # miscalibration
        a,c=[],[]
        for i,(q,t) in enumerate(zip(QS,TR)):
            noise=rng.gauss(0,skill)
            if q["type"]=="num":
                a.append(round(t*math.exp(qb[i]+noise),3))
                c.append(min(1,max(0.05,1-skill-abs(noise)*0.5+over+rng.gauss(0,0.15))))
            else:
                acc=1-skill*0.8; ok=rng.random()<acc
                if shared and rng.random()<0.3: ok=False; pick=qwrong[i]
                else: pick=t if ok else rng.choice([o.split("=")[0][-1] for o in q["q"].split("?")[1].split() if "=" in o and o.split("=")[0][-1]!=t])
                a.append(pick); c.append(min(1,max(0.05,(0.75 if ok else 0.45)+over+rng.gauss(0,0.2))))
        agents.append((a,c))
    return {f"a{k}":x for k,x in enumerate(agents)}
def simulate(trials=500,n=5):
    for shared in (False,True):
        rng=random.Random(42); R=collections.defaultdict(list)
        for _ in range(trials):
            ans=sim_agents(rng,n,shared); ind=[score(a) for a,_ in ans.values()]
            p=score(merge(ans)); w=score(merge(ans,True)); best=min(ind)
            R["ind_num"].append(statistics.mean(s[0] for s in ind)); R["ind_cat"].append(statistics.mean(s[1] for s in ind))
            R["plain_num"].append(p[0]); R["plain_cat"].append(p[1]); R["w_num"].append(w[0]); R["w_cat"].append(w[1])
            R["w_wins_num"].append(w[0]<p[0]); R["plain_wins_num"].append(p[0]<w[0])
            R["plain_beats_all"].append(all(p[0]<s[0] for s in ind))
        m=lambda k: statistics.mean(R[k])
        print(f"{'SHARED-BIAS' if shared else 'INDEPENDENT'} ({trials} rounds x {n} agents)")
        print(f"  mean individual: num_logerr={m('ind_num'):.4f} cat_wrong={m('ind_cat'):.3f}/{NCAT}")
        print(f"  plain merge:     num_logerr={m('plain_num'):.4f} cat_wrong={m('plain_cat'):.3f}/{NCAT}")
        print(f"  weighted merge:  num_logerr={m('w_num'):.4f} cat_wrong={m('w_cat'):.3f}/{NCAT}")
        print(f"  numbers: weighted better in {sum(R['w_wins_num'])}, plain better in {sum(R['plain_wins_num'])} rounds; plain beats every individual in {sum(R['plain_beats_all'])}")
if __name__=="__main__":
    a=sys.argv[1:]
    if a and a[0] in("create","merge"):
        qf,af=ROUNDS.get(a[1],(f"{D}/questions.json",A1))
        load(opt(a,"--questions") or qf, opt(a,"--answers") or af)
    if not a: print(__doc__)
    elif a[0]=="create": create(a[1],a[2])
    elif a[0]=="merge": report(a[1],a[2],"--weighted" in a)
    elif a[0]=="simulate": simulate(int(a[1]) if len(a)>1 else 500)
