"""Fill remaining invention slots with measurable Tesla/thermo/hardware ideas."""
import json, time, math, collections, statistics, hashlib, random, os, re, threading
from harness import *
from tokens import evalb, valve, free_energy, dedup_lines, hits_for, sents, landauer
c = con(); R = {}
HD = hits_for(DEV); HT = hits_for(TEST)
base_dev = evalb(DEV, [h[:5] for h in HD]); base_test = evalb(TEST, [h[:5] for h in HT])
valve_dev = evalb(DEV, [valve(x["q"], h[:5]) for x,h in zip(DEV,HD)])
valve_test = evalb(TEST, [valve(x["q"], h[:5]) for x,h in zip(TEST,HT)])
# 3c score-gap adaptive k: if top1 dominates, use k=2 else k=5
def gap_k(hs, thr):
    if len(hs)<2: return hs[:5]
    g = (hs[0]["score"]-hs[1]["score"])/max(abs(hs[0]["score"]),1e-6)
    return hs[:(2 if g>=thr else 5)]
sweep = {}
for thr in (0.05,0.1,0.2,0.3,0.5):
    sweep[thr]=evalb(DEV,[valve(x["q"],gap_k(h,thr)) for x,h in zip(DEV,HD)])
ok=[t for t,m in sweep.items() if m["recall5"]>=base_dev["recall5"]-0.005 and m["acc"]>=base_dev["acc"]-0.005]
tb=min(ok,key=lambda t:sweep[t]["tokens_brief"]) if ok else None
R["3_gap_k"]=dict(sweep=sweep, thr=tb, base_valve_test=valve_test,
    test=(evalb(TEST,[valve(x["q"],gap_k(h,tb)) for x,h in zip(TEST,HT)]) if tb is not None else None))
# 4b answer-early: once a numeric sentence matching query tokens exists in top hit, drop later hits' bodies
def early(q, hs):
    qs=set(tok(q)); out=[]; found=False
    for i,h in enumerate(hs):
        if found: out.append({**h,"body":""}); continue
        body=h["body"]; 
        for s in sents(body):
            if re.search(NUM,s) and (set(tok(s))&qs): found=True; break
        out.append(h if not found or i==0 else {**h,"body": body if i==0 else ""})
        # keep body of the hit that found it, blank later
        if found and i>0: out[-1]={**h,"body":""}
    # fix: keep bodies until found inclusive
    out=[]; found=False
    for h in hs:
        if found: out.append({**h,"body":""}); continue
        keep=h["body"]
        for s in sents(keep):
            if re.search(NUM,s) and (set(tok(s))&qs): found=True; break
        out.append({**h,"body":keep})
    return out
R["4_answer_early"]=dict(dev=evalb(DEV,[early(x["q"],valve(x["q"],h[:5])) for x,h in zip(DEV,HD)]),
                         test=evalb(TEST,[early(x["q"],valve(x["q"],h[:5])) for x,h in zip(TEST,HT)]),
                         stacked=evalb(TEST,[early(x["q"],free_energy(x["q"],dedup_lines(valve(x["q"],h[:5])),1.5)) for x,h in zip(TEST,HT)]))
# 8b prepared search: reuse one connection + pre-tok — already; measure idf warmup
allsee._idf.clear()
t0=time.time(); 
for x in TEST: allsee.search(x["q"],5,c,{}); cold=time.time()-t0
t0=time.time()
for x in TEST: allsee.search(x["q"],5,c,{}); warm=time.time()-t0
R["8_idf_warm"]=dict(cold_s=round(cold,2), warm_s=round(warm,2), speedup=round(cold/max(warm,1e-6),3))
# 9c thermal under contention: N parallel searchers; with/without ncand cut
def barrage(nworkers, ncand, nq=40):
    qs=[x["q"] for x in TEST[:nq]]; barrier=threading.Barrier(nworkers); times=[]
    def worker():
        cc=con(); barrier.wait(); t=time.perf_counter()
        for q in qs: allsee.search(q,5,cc,{"ncand":ncand})
        times.append(time.time()-t)  # bug: time vs perf - use perf
    # fix properly
    times.clear(); done=[]
    def worker2():
        cc=con(); barrier.wait(); t=time.perf_counter()
        for q in qs: allsee.search(q,5,cc,{"ncand":ncand})
        done.append(time.perf_counter()-t)
    th=[threading.Thread(target=worker2) for _ in range(nworkers)]
    for t in th: t.start()
    for t in th: t.join()
    return dict(wall_max=round(max(done),2), wall_mean=round(sum(done)/len(done),2), nworkers=nworkers, ncand=ncand)
R["9_thermal_contention"]={f"w{w}_n{n}": barrage(w,n) for w in (4,8) for n in (15,30)}
# 13b zipf boot prefetch into shared bifilar state
rnd=random.Random(2); pool=TEST+DEV; wts=[1/(i+1) for i in range(len(pool))]
# top-50 most "popular" by zipf index
pop=[pool[i]["q"] for i in range(50)]
state={}
for q in pop:
    k=" ".join(sorted(set(tok(q)))); 
    if k not in state: state[k]=True; allsee.search(q,5,c,{})
# stream 600 zipf with case variants
stream=[rnd.choices(pool,wts)[0]["q"] for _ in range(600)]
stream=[q if rnd.random()<0.7 else q.upper()+" " for q in stream]
def replay(pre):
    A={}; B=dict(pre); hit=0; t=time.perf_counter()
    for q in stream:
        if q in A: hit+=1; continue
        k=" ".join(sorted(set(tok(q))))
        if k in B: A[q]=1; hit+=1; continue
        allsee.search(q,5,c,{}); A[q]=1; B[k]=1
    return dict(hit_rate=round(hit/len(stream),3), s=round(time.perf_counter()-t,2))
pre={(" ".join(sorted(set(tok(q))))):1 for q in pop}
R["13_zipf_prefetch"]=dict(cold=replay({}), bifilar=replay({}), prefetch=replay(pre), n_pre=len(pre))
# 14b thermodynamic efficiency pick: maximize acc/tokens on DEV configs
cfgs={"raw": lambda x,h: h[:5],
      "valve": lambda x,h: valve(x["q"],h[:5]),
      "fe1.5": lambda x,h: free_energy(x["q"],valve(x["q"],h[:5]),1.5),
      "dedup": lambda x,h: dedup_lines(valve(x["q"],h[:5])),
      "stack": lambda x,h: free_energy(x["q"],dedup_lines(valve(x["q"],h[:5])),1.5)}
eff={}
for name,fn in cfgs.items():
    m=evalb(DEV,[fn(x,h) for x,h in zip(DEV,HD)]); 
    eff[name]=dict(**m, eta=round(m["acc"]/max(m["tokens_brief"],1)*1000,4))
best=max(eff, key=lambda n: eff[n]["eta"])
R["14_thermo_eta"]=dict(dev=eff, best=best, test=evalb(TEST,[cfgs[best](x,h) for x,h in zip(TEST,HT)]),
                        test_all={n:evalb(TEST,[fn(x,h) for x,h in zip(TEST,HT)]) for n,fn in cfgs.items()})
# 15b hard char cap on each hit body
def cap(hs, n): return [{**h,"body":h["body"][:n]} for h in hs]
sweep={n:evalb(DEV,[cap(valve(x["q"],h[:5]),n) for x,h in zip(DEV,HD)]) for n in (200,400,600,800,1200)}
ok=[n for n,m in sweep.items() if m["recall5"]>=base_dev["recall5"]-0.005 and m["acc"]>=base_dev["acc"]-0.005]
nb=min(ok) if ok else None
R["15_char_cap"]=dict(sweep=sweep, n=nb, test=(evalb(TEST,[cap(valve(x["q"],h[:5]),nb) for x,h in zip(TEST,HT)]) if nb else None))
json.dump(R,open("results/more2.json","w"),indent=1)
print(json.dumps(R,indent=1)[:4000])
