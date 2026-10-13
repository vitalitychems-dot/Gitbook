# robustness re-run: noisy fidelity averaged over 4 random basis inputs (n=3..8)
import numpy as np,json
from qsim import *; from aqft import *; from qopt2 import lower; import qnoise2
NK=dict(p1=1e-3,p2=1e-2,gamma=1e-3); rng=np.random.default_rng(11); out={}
for n in range(3,9):
    xs=[int(x) for x in rng.integers(0,2**n,4)]; refs=[]
    for x in xs: s=SV(n); s.v[:]=0; s.v[x]=1; refs.append(s.run(qft(n)).v)
    r=[]
    for m in range(1,n+1):
        L=lower(aqft(n,m)); f=[float(np.real(p.conj()@qnoise2.run(n,L,init=x,**NK)@p)) for x,p in zip(xs,refs)]; r.append((m,np.mean(f),np.std(f)))
    b=max(r,key=lambda z:z[1]); out[n]=dict(best_m=b[0],rows=r)
    print(f'n={n} best m={b[0]} (log2n+2={np.log2(n)+2:.2f}) '+' '.join(f'm{m}:{a:.4f}±{s:.4f}' for m,a,s in r))
json.dump(out,open('aqft_avg_results.json','w'),default=float)
