"""Empathy baseline: GoEmotions (Apache-2.0) single-label rows -> 4 sentiment groups; multinomial Naive Bayes (numpy). Held-out = official test split."""
import re, json, collections, numpy as np
POS={0,1,4,5,8,13,15,17,18,20,21,23}; NEG={2,3,9,10,11,12,14,16,19,24,25}; AMB={6,7,22,26}
grp=lambda l: "pos" if l in POS else "neg" if l in NEG else "amb" if l in AMB else "neu"
tok=lambda s: re.findall(r"[a-z']+|[!?:(]+", s.lower())
def load(p): return [(tok(t), grp(int(l))) for t,l,_ in (x.rstrip("\n").split("\t") for x in open(p)) if "," not in l]
tr, te = load("data/ge_train.tsv"), load("data/ge_test.tsv"); C=["pos","neg","amb","neu"]
cnt={c:collections.Counter() for c in C}; prior=collections.Counter(y for _,y in tr)
for w,y in tr: cnt[y].update(w + [a+"_"+b for a,b in zip(w,w[1:])])
V=set().union(*cnt.values()); tot={c:sum(cnt[c].values()) for c in C}
def pred(w):
    f=w+[a+"_"+b for a,b in zip(w,w[1:])]
    return max(C,key=lambda c: np.log(prior[c])+sum(np.log((cnt[c][t]+.5)/(tot[c]+.5*len(V))) for t in f if t in V))
P=[pred(w) for w,_ in te]; Y=[y for _,y in te]
def f1(c): tp=sum(p==y==c for p,y in zip(P,Y)); fp=sum(p==c!=y for p,y in zip(P,Y)); fn=sum(y==c!=p for p,y in zip(P,Y)); return 2*tp/max(1,2*tp+fp+fn)
maj=prior.most_common(1)[0][0]
R=dict(train=len(tr),test=len(te),acc=round(np.mean([p==y for p,y in zip(P,Y)]),3),macro_f1=round(np.mean([f1(c) for c in C]),3),per_class={c:round(f1(c),3) for c in C},
 majority_class=maj,majority_acc=round(np.mean([y==maj for y in Y]),3))
json.dump(R,open("empathy_results.json","w"),indent=1); print(R)
