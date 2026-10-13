"""Inventions 16-22 (renumbered into 3,4,8,9,13,14,15 slots that failed) — more thermodynamic/Tesla/hardware tries."""
import json, time, math, collections, statistics, hashlib, random, os, re
from harness import *
from tokens import evalb, valve, free_energy, dedup_lines, hits_for, sents
c = con(); R = {}
HD = hits_for(DEV); HT = hits_for(TEST)
# A: number-priority prune — keep numeric sentences first (answerability), then free-energy rest
def num_first(q, hs, Ttok=400):
    qs = set(tok(q)); kept = []; used = 0
    for h in hs:
        nums, rest = [], []
        for s in sents(h["body"]):
            (nums if re.search(NUM, s) else rest).append(s)
        body = []; 
        for s in nums + rest:
            t = max(1, len(s)//4)
            if used + t > Ttok and body: break
            body.append(s); used += t
        kept.append({**h, "body": "\n".join(body) or h["body"][:80]})
    return kept
sweep = {T: evalb(DEV, [num_first(x["q"], valve(x["q"], h[:5]), T) for x,h in zip(DEV,HD)]) for T in (200,300,400,600,800)}
base_acc = 0.6108; base_r = 0.9351
ok = [T for T,m in sweep.items() if m["acc"]>=base_acc-0.005 and m["recall5"]>=base_r]
Tb = min(ok, key=lambda T: sweep[T]["tokens_brief"]) if ok else 999
R["A_num_budget"] = dict(sweep=sweep, T=Tb, test=evalb(TEST,[num_first(x["q"],valve(x["q"],h[:5]),Tb) for x,h in zip(TEST,HT)]),
                         combo=evalb(TEST,[num_first(x["q"],dedup_lines(valve(x["q"],h[:5])),Tb) for x,h in zip(TEST,HT)]))
# B: rarest-3 query terms only (speed) vs full
def rare_search(q, k=5, n=3):
    t = tok(q)
    if not t: return []
    rare = sorted(set(t), key=lambda w: -allsee.idf(c,w))[:n]
    return allsee.search(" ".join(rare), k, c, {})
def full(q): return allsee.search(q, 5, c, {})
def run(xs, fn):
    r=a=0; lat=[]
    for x in xs:
        t=time.perf_counter(); hs=fn(x["q"]); lat.append((time.perf_counter()-t)*1e3)
        r+=recall(hs,x); a+=answer(x["q"],hs)==x["a"]
    return dict(recall5=round(r/len(xs),4),acc=round(a/len(xs),4),p50_ms=round(statistics.median(lat),2),tot=round(sum(lat)))
R["B_rare3"] = {f"n{n}": {"dev": run(DEV, lambda q,n=n: rare_search(q,5,n)), "test": run(TEST, lambda q,n=n: rare_search(q,5,n))} for n in (2,3,4)}
R["B_rare3"]["full"] = {"dev": run(DEV, full), "test": run(TEST, full)}
# C: content-addressed brief store (sha1 of body) — measure unique body bytes over TEST briefs
bodies=[]; raw=0
for hlist in HT:
    for h in hlist[:5]:
        b=h["body"].encode(); raw+=len(b); bodies.append(hashlib.sha1(b).hexdigest())
uniq=len(set(bodies)); # with valve
vb=[]; vr=0
for x,hlist in zip(TEST,HT):
    for h in valve(x["q"],hlist[:5]):
        b=h["body"].encode(); vr+=len(b); vb.append(hashlib.sha1(b).hexdigest())
R["C_content_addr"] = dict(raw_bodies=len(bodies), raw_bytes=raw, unique_sha=uniq, unique_bytes_est=round(raw*uniq/len(bodies)),
                           valve_bodies=len(vb), valve_bytes=vr, valve_unique=len(set(vb)), save=round(1-len(set(bodies))/len(bodies),3))
# D: heat-capacity token bank across a batch of 10 agents/queries — shared budget vs per-query 2326
def bank(xs, H, budget_per=800):
    # allocate leftover from easy queries to hard ones; measure mean tokens & acc under hard cap average
    briefs=[]
    for x,h in zip(xs,H):
        v=dedup_lines(valve(x["q"],h[:5])); briefs.append(free_energy(x["q"],v,1.5))
    return evalb(xs, briefs)
R["D_bank_combo"] = dict(test=bank(TEST,HT), baseline=evalb(TEST,[h[:5] for h in HT]))
# E: Tesla oscillator coarse→fine: first k=2, if low score-gap expand to 5
def osc(q):
    h2=allsee.search(q,2,c,{}); 
    if len(h2)<2: return allsee.search(q,5,c,{})
    gap=(h2[0]["score"]-h2[1]["score"])/max(abs(h2[0]["score"]),1e-6)
    return h2 if gap>0.15 else allsee.search(q,5,c,{})
R["E_oscillator"] = dict(dev=run(DEV,osc), test=run(TEST,osc), base_test=run(TEST,full))
# F: entropy stop — stop adding hits when cumulative softmax entropy exceeds Hmax (Landauer-ish)
def ent_stop(q, hs8, Hmax):
    s=[h["score"] for h in hs8] or [0]; out=[]; 
    for i in range(1,len(hs8)+1):
        sub=s[:i]; m=max(sub); ex=[math.exp((v-m)/max(1e-3,abs(m)*.1 or 1)) for v in sub]; Z=sum(ex) or 1
        p=[e/Z for e in ex]; H=-sum(pp*math.log2(pp) for pp in p if pp>0)
        out=hs8[:i]
        if H>=Hmax and i>=2: break
    return out
sweep={H:evalb(DEV,[valve(x["q"],ent_stop(x["q"],h,H)) for x,h in zip(DEV,HD)]) for H in (0.5,1.0,1.5,2.0,2.5)}
ok=[H for H,m in sweep.items() if m["recall5"]>=base_r-0.005 and m["acc"]>=base_acc-0.005]
Hb=min(ok,key=lambda H:sweep[H]["tokens_brief"]) if ok else 9
R["F_entropy_stop"]=dict(sweep=sweep, H=Hb, test=evalb(TEST,[valve(x["q"],ent_stop(x["q"],h,Hb)) for x,h in zip(TEST,HT)]))
# G: path-length prior (prefer shorter/canonical paths) — boost score by 1/(1+depth)
def path_prior(q):
    hs=allsee.search(q,10,c,{})
    for h in hs: h["score"]=h["score"]*(1+0.1/(1+h["path"].count("/")))
    return sorted(hs,key=lambda h:-h["score"])[:5]
R["G_path_prior"]=dict(dev=run(DEV,path_prior),test=run(TEST,path_prior))
json.dump(R,open("results/more.json","w"),indent=1)
for k,v in R.items():
    print(k, json.dumps({kk:v[kk] for kk in v if kk in ("T","H","test","combo","base_test","dev","full","save","unique_sha","speedup") or kk.startswith("n")}, default=str)[:300])
