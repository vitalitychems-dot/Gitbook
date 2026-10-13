"""Empathy v2: GoEmotions 4-group (pos/neg/amb/neu), single-label rows. Logistic regression (numpy, softmax, L2, class-balanced) on hashed
unigram+bigram+char-4gram TF-IDF; C and epochs tuned on the official dev split, scored once on test. Baseline = c1 Naive Bayes."""
import re, json, numpy as np, collections
POS={0,1,4,5,8,13,15,17,18,20,21,23}; NEG={2,3,9,10,11,12,14,16,19,24,25}; AMB={6,7,22,26}; CL=["pos","neg","amb","neu"]
grp=lambda l: 0 if l in POS else 1 if l in NEG else 2 if l in AMB else 3
D=2**18
def feats(t):
    t=t.lower(); w=re.findall(r"[a-z']+|[!?:(]+",t); f=w+[a+"_"+b for a,b in zip(w,w[1:])]+["#"+t[i:i+4] for i in range(len(t)-3)]
    return collections.Counter(hash(x)%D for x in f)
def load(p):
    X=[];Y=[]
    for line in open(p):
        t,l,_=line.rstrip("\n").split("\t")
        if "," in l: continue
        X.append(feats(t)); Y.append(grp(int(l)))
    return X,np.array(Y)
import os; os.environ["PYTHONHASHSEED"]="0"
tr,ytr=load("/workspace/rick/cycles/c1/data/ge_train.tsv"); dv,ydv=load("data/ge_dev.tsv"); te,yte=load("/workspace/rick/cycles/c1/data/ge_test.tsv")
df=np.zeros(D); [df.__setitem__(list(x),df[list(x)]+1) for x in tr]; idf=np.log((1+len(tr))/(1+df))+1
class CSR:
    def __init__(s,ptr,col,val,n): s.ptr,s.col,s.val,s.n=ptr,col,val,n
    def __getitem__(s,idx):
        cols=[s.col[s.ptr[i]:s.ptr[i+1]] for i in idx]; vals=[s.val[s.ptr[i]:s.ptr[i+1]] for i in idx]
        return CSR(np.r_[0,np.cumsum([len(c) for c in cols])],np.concatenate(cols),np.concatenate(vals),len(idx))
    def rows(s): return np.repeat(np.arange(s.n),np.diff(s.ptr))
    def __matmul__(s,W): out=np.zeros((s.n,W.shape[1])); np.add.at(out,s.rows(),s.val[:,None]*W[s.col]); return out
    def tmul(s,G): out=np.zeros((D,G.shape[1])); np.add.at(out,s.col,s.val[:,None]*G[s.rows()]); return out
def mat(X):
    r=[];c=[];v=[]
    for i,x in enumerate(X):
        for k,n in x.items(): r.append(i);c.append(k);v.append((1+np.log(n))*idf[k])
    r=np.array(r);v=np.array(v);n=np.sqrt(np.bincount(r,v*v,minlength=len(X)))+1e-9;v=v/n[r]
    return CSR(np.r_[0,np.cumsum(np.bincount(r,minlength=len(X)))],np.array(c),v,len(X))
Xtr,Xdv,Xte=mat(tr),mat(dv),mat(te)
cw=len(ytr)/(4*np.bincount(ytr,minlength=4))
def train(lam,ep,lr=2.0,bs=256,seed=0):
    W=np.zeros((D,4)); rng=np.random.default_rng(seed); Y=np.eye(4)[ytr]
    for e in range(ep):
        for b in np.array_split(rng.permutation(len(ytr)),len(ytr)//bs):
            Z=Xtr[b]@W; P=np.exp(Z-Z.max(1,keepdims=True)); P/=P.sum(1,keepdims=True)
            Xb=Xtr[b]; G=Xb.tmul((P-Y[b])*cw[ytr[b]][:,None])/len(b); W-=lr*(G+lam*W)
    return W
def f1s(y,p): return [2*np.sum((p==c)&(y==c))/max(1,np.sum(p==c)+np.sum(y==c)) for c in range(4)]
best=None
for lam in (1e-6,1e-5,1e-4):
    for ep in (3,6):
        W=train(lam,ep); m=np.mean(f1s(ydv,(Xdv@W).argmax(1)))
        if best is None or m>best[0]: best=(m,lam,ep,W)
m,lam,ep,W=best; p=(Xte@W).argmax(1); f=f1s(yte,p)
c1=json.load(open("/workspace/rick/cycles/c1/empathy_results.json"))
R=dict(model="softmax LR, tfidf word1-2+char4 hashed 2^18, class-balanced",dev_macro_f1=round(m,3),lam=lam,epochs=ep,test_n=len(yte),acc=round(float(np.mean(p==yte)),3),macro_f1=round(float(np.mean(f)),3),
 per_class=dict(zip(CL,[round(x,3) for x in f])),c1_nb_macro_f1=c1["macro_f1"],c1_nb_acc=c1["acc"])
json.dump(R,open("empathy2_results.json","w"),indent=1); print(R)
