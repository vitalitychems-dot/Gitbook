#!/usr/bin/env python3
"""Fraction vs siloed retrieval bench on real data (allsee.db chunks, cycles/c1 qa_set test split).
Hit = the original line (blank filled with answer) appears in a returned chunk. Leak guard: qa_set/cycles/fraction paths excluded."""
import sqlite3, json, re, time, random, statistics as st
DB="/workspace/rick/tools/allsee/allsee.db"; QA="/workspace/rick/cycles/c1/qa_set.json"; K=5; HOP=60  # tokens per agent msg hop
c=sqlite3.connect(f"file:{DB}?mode=ro",uri=True)
def silo(root):
    if root in("/workspace/rick","/workspace/rick/src/Gitbook"): return "A"
    if root in("/workspace/TESSERA-ro","/workspace/tess-opt","/workspace/tw"): return "B"
    if "gitbook" in root: return "C"
    return "D"
LEAK=re.compile(r"qa_set|/cycles/|/tools/fraction/|allsee/rounds|synapse")
def q2fts(q):
    w=[x for x in re.findall(r"[A-Za-z0-9]+",q.replace("___"," ")) if len(x)>2][:12]
    return " OR ".join('"%s"'%x for x in w)
SQL="""select ch.id, ch.body, fl.root, fl.path, bm25(f) s from f join chunks ch on ch.id=f.rowid
 join cmap m on m.cid=ch.id join files fl on fl.hash=m.hash where f match ? order by s limit 400"""
def search(q, silos=None, k=K):
    out=[];seen=set()
    for cid,body,root,path,s in c.execute(SQL,(q2fts(q),)):
        if cid in seen or LEAK.search(path): continue
        if silos and silo(root) not in silos: continue
        seen.add(cid); out.append(body)
        if len(out)>=k: break
    return out
def tok(bs): return sum(len(b) for b in bs)//4
qa=[x for x in json.load(open(QA)) if x["split"]=="test"]
rnd=random.Random(7); R={}
def run(name, fn):
    hits=toks=0; lat=[]
    for x in qa:
        t=time.perf_counter(); bs,hops=fn(x); lat.append((time.perf_counter()-t)*1000)
        tgt=x["q"].replace("___",x["a"]); hits+=any(tgt in b for b in bs); toks+=tok(bs)+HOP*hops
    R[name]=dict(hit=round(hits/len(qa),3),tok_per_q=round(toks/len(qa)),ms_p50=round(st.median(lat),1),ms_mean=round(st.mean(lat),1))
own={id(x):rnd.choice("ABCD") for x in qa}
run("siloed_own_only", lambda x:(search(x["q"],{own[id(x)]}),1))
run("siloed_broadcast_4", lambda x:(sum((search(x["q"],{s}) for s in "ABCD"),[]),4))
run("unified_fraction", lambda x:(search(x["q"]),1))
print(json.dumps(dict(n=len(qa),k=K,hop_tokens=HOP,results=R),indent=1))
