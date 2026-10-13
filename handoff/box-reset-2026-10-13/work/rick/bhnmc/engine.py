"""BHNMC v1.3 characterization engine -- faithful port + bug fixes. SIMULATION ONLY (no biology).
Fixes: (1) manifest now stores 'dna_sequence_string' (print line referenced a missing key);
(2) sklearn replaced by numpy equivalents in mlcore.py (box disk full) -- SVC replaced by RBF kernel-ridge."""
import numpy as np, json, sys
from mlcore import Scaler, Ridge, KernelRBF, acc
class BHNMC_CharacterizationPlatform:
    def __init__(s,channels=64,num_qubits=16,seed=42):
        s.n=channels; s.q=num_qubits; s.rng=np.random.default_rng(seed)
        W=s.rng.uniform(-0.1,0.1,(s.n,s.n)); np.fill_diagonal(W,0)
        s.W_space=W*(1.15/np.max(np.abs(np.linalg.eigvals(W))))
        s.leak=0.2; s.noise=0.015; s.state=np.zeros(s.n)
        W_qi=s.rng.normal(size=(s.q,s.n)); s.W_qi=W_qi/np.linalg.norm(W_qi,axis=1,keepdims=True)
    def step(s,u):
        pre=s.W_space@s.state+u+s.rng.normal(0,s.noise,s.n)
        s.state=(1-s.leak)*s.state+s.leak*np.tanh(pre)
        return 15000+4200*s.state, -1200*np.sin(s.state*np.pi/4)
    def run_trial(s,U):
        Rh,Xh=[],[]
        for u in U: R,X=s.step(u); Rh.append(R); Xh.append(X)
        Rh,Xh=np.array(Rh),np.array(Xh)
        return np.concatenate([Rh[-1],Rh[-1]-Rh[0],np.diag(np.cov(Xh.T))])
    @staticmethod
    def dna_encode(v):
        q=np.digitize(v,np.quantile(v,[.25,.5,.75])); return ''.join('ACGT'[i] for i in q)
    def qi_features(s,F):
        th=np.clip(F[:,:s.n]@s.W_qi.T,-np.pi,np.pi)
        return np.hstack([np.cos(th)**2,np.sin(th)**2])
def stimulus(cls,T=20):
    U=np.zeros((T,64)); t=np.arange(T)
    if cls==0: U[:,0:16]=(np.sin(0.4*t)*1.1)[:,None]
    elif cls==1: U[:,16:48]=(np.cos(0.3*t)*1.4)[:,None]
    else: U[:,48:64]=np.linspace(.1,1.8,16)[None,:]
    return U
def main(seed=42,trials=100,steps=20,verbose=True):
    p=BHNMC_CharacterizationPlatform(seed=seed)
    F=np.array([p.run_trial(stimulus(i%3,steps)) for i in range(trials)]); y=np.arange(trials)%3
    k=int(.8*trials); sc=Scaler().fit(F[:k]); Xtr,Xte=sc.transform(F[:k]),sc.transform(F[k:])
    r=acc(y[k:],Ridge().fit(Xtr,y[:k]).predict(Xte))
    s=acc(y[k:],KernelRBF(.05).fit(Xtr,y[:k]).predict(Xte))
    Q=p.qi_features(Xtr),p.qi_features(Xte)
    qa=acc(y[k:],Ridge().fit(Q[0],y[:k]).predict(Q[1]))
    man={"version":"1.3","seed":seed,"feature_dims":int(F.shape[1]),"ridge_acc":r,"rbf_acc":s,"qi_ridge_acc":qa,
         "dna_sequence_string":p.dna_encode(F[-1,:64])}
    if verbose: print(json.dumps(man,indent=1)); print("DNA:",man['dna_sequence_string'])
    return man
if __name__=="__main__": main()
