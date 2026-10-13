"""BHNMC v1.4 experiment -- SIMULATION ONLY. Tests whether the simulated reservoir adds anything."""
import numpy as np, json
from mlcore import Scaler, Ridge, KernelRBF, RidgeReg, acc
from engine import BHNMC_CharacterizationPlatform as P, stimulus
FREQS=np.array([1e2,1e3,1e4,1e5])
def make_res(seed,rho=1.15):
    p=P(seed=seed)
    if rho!=1.15: p.W_space*=rho/1.15
    return p
def trial_feats(p,U,reset=True,multifreq=False):
    if reset: p.state=np.zeros(p.n)
    Rh,Xh=[],[]
    for u in U: R,X=p.step(u); Rh.append(R); Xh.append(X)
    Rh,Xh=np.array(Rh),np.array(Xh)
    f=[Rh[-1],Rh[-1]-Rh[0],Xh.var(0)]
    if multifreq:  # Cole-type dispersion; tau depends on state (assumed model, not measured)
        tau=1e-4*(1+0.5*p.state)
        for fr in FREQS:
            Z=1000+(Rh[-1]-1000)/(1+1j*2*np.pi*fr*tau); f+= [Z.real,Z.imag]
    return np.concatenate(f)
def hard_stim(cls,rng,T=20,variant=None):
    """All classes drive ALL 64 channels through a random fixed mixing; classes differ only by temporal
    frequency (0.30/0.36/0.42 rad/step). Variant = (amp,phase) family; held-out families for test."""
    t=np.arange(T); w=[0.30,0.36,0.42][cls]
    amp,ph=variant
    s=amp*np.sin(w*t+ph)
    return np.outer(s,hard_stim.Win)+rng.normal(0,0.3,(T,64))
hard_stim.Win=np.random.default_rng(7).normal(0,1,64)/4
def cv(F,y,seed,k=5,models=("ridge","rbf")):
    rng=np.random.default_rng(seed); folds=[[] for _ in range(k)]
    for c in np.unique(y):
        idx=rng.permutation(np.where(y==c)[0])
        for i,j in enumerate(idx): folds[i%k].append(j)
    out={m:[] for m in models}
    for i in range(k):
        te=np.array(folds[i]); tr=np.setdiff1d(np.arange(len(y)),te)
        sc=Scaler().fit(F[tr]); A,B=sc.transform(F[tr]),sc.transform(F[te])
        if "ridge" in models: out["ridge"].append(acc(y[te],Ridge(1.0).fit(A,y[tr]).predict(B)))
        if "rbf" in models: out["rbf"].append(acc(y[te],KernelRBF(.05/ (A.shape[1]/192)).fit(A,y[tr]).predict(B)))
    return {m:np.mean(v) for m,v in out.items()}
def ms(v): v=np.array(v); return f"{v.mean():.3f}±{v.std():.3f}"
SEEDS=range(10); R={}
# A. v1.3 task: leakage vs reset, shuffled stratified CV
for reset in (False,True):
    acc_=[]
    for s in SEEDS:
        p=make_res(s); F=np.array([trial_feats(p,stimulus(i%3),reset) for i in range(150)]); y=np.arange(150)%3
        acc_.append(cv(F,y,s)["ridge"])
    R[f"A_v13task_ridge_reset={reset}"]=ms(acc_)
# v1.3 task with NO reservoir (raw input final+mean)
acc_=[]
for s in SEEDS:
    F=np.array([np.r_[stimulus(i%3)[-1],stimulus(i%3).mean(0)]+np.random.default_rng(s*1000+i).normal(0,.015,128) for i in range(150)])
    acc_.append(cv(F,np.arange(150)%3,s)["ridge"])
R["A_v13task_ridge_NO_reservoir"]=ms(acc_)
# B. hard task, random split and held-out variant families
fams_tr=[(1.0,0.0),(1.2,0.5),(0.8,1.0),(1.1,2.0)]; fams_te=[(0.6,3.0),(1.5,4.0)]
def hard_dataset(p,fams,rng,mf,n_per=15,mode="res"):
    F,y=[],[]
    for fam in fams:
        for c in range(3):
            for _ in range(n_per):
                U=hard_stim(c,rng,variant=fam)
                if mode=="res": F.append(trial_feats(p,U,True,mf))
                else: F.append(np.r_[U[-1],U.mean(0),U.var(0)])  # no-reservoir baseline (same 192 dims)
                y.append(c)
    return np.array(F),np.array(y)
for mode in ("res","nores"):
  for mf in ((False,True) if mode=="res" else (False,)):
    cvr,cvk,hr,hk=[],[],[],[]
    for s in SEEDS:
        rng=np.random.default_rng(100+s); p=make_res(s)
        Ftr,ytr=hard_dataset(p,fams_tr,rng,mf,mode=mode); Fte,yte=hard_dataset(p,fams_te,rng,mf,mode=mode)
        c=cv(Ftr,ytr,s); cvr.append(c["ridge"]); cvk.append(c["rbf"])
        sc=Scaler().fit(Ftr); A,B=sc.transform(Ftr),sc.transform(Fte)
        hr.append(acc(yte,Ridge().fit(A,ytr).predict(B)))
        hk.append(acc(yte,KernelRBF(.05/(A.shape[1]/192)).fit(A,ytr).predict(B)))
    tag=f"B_hard_{mode}_multifreq={mf}"
    R[tag+"_cv_ridge"]=ms(cvr); R[tag+"_cv_rbf"]=ms(cvk); R[tag+"_heldout_ridge"]=ms(hr); R[tag+"_heldout_rbf"]=ms(hk)
# C. QI: first 64 of 192 vs all 192 (hard task, held-out)
q64,q192=[],[]
for s in SEEDS:
    rng=np.random.default_rng(100+s); p=make_res(s)
    Ftr,ytr=hard_dataset(p,fams_tr,rng,False); Fte,yte=hard_dataset(p,fams_te,rng,False)
    sc=Scaler().fit(Ftr); A,B=sc.transform(Ftr),sc.transform(Fte)
    qa=lambda Wq,X: np.hstack([np.cos(np.clip(X@Wq.T,-np.pi,np.pi))**2,np.sin(np.clip(X@Wq.T,-np.pi,np.pi))**2])
    q64.append(acc(yte,Ridge().fit(qa(p.W_qi,A[:,:64]),ytr).predict(qa(p.W_qi,B[:,:64]))))
    W=np.random.default_rng(s).normal(size=(16,192)); W/=np.linalg.norm(W,axis=1,keepdims=True)
    q192.append(acc(yte,Ridge().fit(qa(W,A),ytr).predict(qa(W,B))))
R["C_QI_first64_heldout"]=ms(q64); R["C_QI_all192_heldout"]=ms(q192)
# D. memory capacity + NARMA10, rho sweep, vs no-reservoir (input delay line of length 1)
def drive(p,u):
    p.state=np.zeros(p.n); Win=np.random.default_rng(3).uniform(-.5,.5,64); S=[]
    for x in u: p.step(Win*x); S.append(p.state.copy())
    return np.array(S)
def mc_narma(seed,rho):
    rng=np.random.default_rng(seed); T=3000; u=rng.uniform(0,.5,T)
    S=drive(make_res(seed,rho),u); w=200; tr=slice(w,2000); te=slice(2000,T)
    mc=0
    for k in range(1,41):
        yk=np.r_[np.zeros(k),u[:-k]]; m=RidgeReg(1e-6).fit(S[tr],yk[tr]); pr=m.predict(S[te])
        c=np.corrcoef(pr,yk[te])[0,1]; mc+=c**2
    y=np.zeros(T)
    for t in range(9,T-1): y[t+1]=.3*y[t]+.05*y[t]*y[t-9:t+1].sum()+1.5*u[t-9]*u[t]+.1
    def nmse(X): m=RidgeReg(1e-6).fit(X[tr],y[tr]); pr=m.predict(X[te]); return np.mean((pr-y[te])**2)/np.var(y[te])
    return mc,nmse(S),nmse(u[:,None])
for rho in (0.8,0.95,1.15):
    r=[mc_narma(s,rho) for s in SEEDS]
    R[f"D_rho={rho}_memory_capacity(max40)"]=ms([x[0] for x in r])
    R[f"D_rho={rho}_NARMA10_NMSE"]=ms([x[1] for x in r])
R["D_NARMA10_NMSE_no_reservoir(input only)"]=ms([mc_narma(s,1.15)[2] for s in range(1)]+[mc_narma(s,1.15)[2] for s in range(1,3)])
print(json.dumps(R,indent=1)); json.dump(R,open("v14_results.json","w"),indent=1)
