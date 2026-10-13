import numpy as np,json,time
from qsim import *; from aqft import *; from qopt2 import lower; import qnoise2
NK=dict(p1=1e-3,p2=1e-2,gamma=1e-3); out={'avg':{},'pe5':{}}; t0=time.time()
# PE t=5 with m=3, same seed/φ draw as test_aqft (rng 5, after sweep draws) not reproducible cheaply -> fresh 10 φ, rerun exact and m=3 on same φ
rng=np.random.default_rng(55); phis=rng.random(10); t=5
for lab,m in (('exact',5),('m=3',3)):
    pi_,pn=[],[]
    for phi in phis:
        c=[('X',[t])]+[('H',[k]) for k in range(t)]+[('CP',[k,t],2*np.pi*phi*2**k) for k in range(t)]+inverse(aqft(t,m))
        y=int(round(phi*2**t))%2**t; pi_.append(SV(t+1).run(c).probs()[y+2**t])
        pn.append(float(np.real(qnoise2.run(t+1,lower(c),**NK)[y+2**t,y+2**t])))
    out['pe5'][lab]=[np.mean(pi_),np.std(pi_),np.mean(pn),np.std(pn)]; print('PE t=5',lab,out['pe5'][lab],flush=True)
rng=np.random.default_rng(11)
for n,ms in ((9,range(2,9)),(10,range(2,8))):
    xs=[int(x) for x in rng.integers(0,2**n,4)]; refs=[]
    for x in xs: s=SV(n); s.v[:]=0; s.v[x]=1; refs.append(s.run(qft(n)).v)
    r=[]
    for m in list(ms)+[n]:
        L=lower(aqft(n,m)); f=[float(np.real(p.conj()@qnoise2.run(n,L,init=x,**NK)@p)) for x,p in zip(xs,refs)]
        r.append((m,np.mean(f),np.std(f))); print(n,m,r[-1],round(time.time()-t0),flush=True)
    out['avg'][n]=r
json.dump(out,open('aqft_fix_results.json','w'),default=float); print('elapsed',round(time.time()-t0))
