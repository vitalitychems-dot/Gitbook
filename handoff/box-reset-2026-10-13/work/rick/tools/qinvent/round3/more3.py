"""Last slots: sqlite hardware tuning + resonance of brief hashes + MWPM-style alias collapse on tokens."""
import json, time, statistics, sqlite3, collections, hashlib
from harness import *
from tokens import evalb, valve, hits_for
R={}
def time_search(pragma=None, n=215):
    cc=sqlite3.connect(f"file:{DB}?mode=ro",uri=True)
    if pragma:
        for p in pragma: cc.execute(p)
    # warm
    for x in TEST[:5]: allsee.search(x["q"],5,cc,{})
    lat=[]
    for x in TEST[:n]:
        t=time.perf_counter(); allsee.search(x["q"],5,cc,{}); lat.append((time.perf_counter()-t)*1e3)
    return dict(p50=round(statistics.median(lat),2), tot=round(sum(lat)), n=n)
R["15_sqlite_hw"]=dict(
    default=time_search(),
    cache64k=time_search(["PRAGMA cache_size=-64000"]),  # 64MB
    mmap=time_search(["PRAGMA mmap_size=268435456"]),
    both=time_search(["PRAGMA cache_size=-64000","PRAGMA mmap_size=268435456"]),
)
# verify recall unchanged with both
c2=sqlite3.connect(f"file:{DB}?mode=ro",uri=True)
c2.execute("PRAGMA cache_size=-64000"); c2.execute("PRAGMA mmap_size=268435456")
r=sum(1 for x in TEST if recall(allsee.search(x["q"],5,c2,{}),x))
R["15_sqlite_hw"]["recall5_both"]=round(r/len(TEST),4)
# Bonus: resonance brief-hash cache — second pass of same queries hits memory
HT=hits_for(TEST)
cache={}; hits=miss=0; t0=time.time()
for _ in range(2):  # two agents asking same TEST
    for x,h in zip(TEST,HT):
        key=hashlib.sha1((" ".join(sorted(set(tok(x["q"]))))).encode()).hexdigest()
        if key in cache: hits+=1; _=cache[key]
        else: miss+=1; cache[key]=valve(x["q"],h[:5])
R["15b_brief_resonance"]=dict(hits=hits,miss=miss,hit_rate=round(hits/(hits+miss),3),s=round(time.time()-t0,3),entries=len(cache))
json.dump(R,open("results/more3.json","w"),indent=1); print(json.dumps(R,indent=1))
