import numpy as np,json,time
from qsim import *; from aqft import *; from qopt2 import lower; import qnoise2
NK=dict(p1=1e-3,p2=1e-2,gamma=1e-3); rng=np.random.default_rng(5); out={'sweep':{},'pe':{}}
def cnt(c): return len(c),sum(len(g[1])==2 for g in c)
t0=time.time()
for n in range(3,11):
    xs=rng.integers(0,2**n,8); x0=int(xs[0]); rows=[]
    ex=[SV(n) for _ in xs]
    for s,x in zip(ex,xs): s.v[:]=0; s.v[x]=1; s.run(qft(n))
    for m in range(1,n+1):
        c=aqft(n,m); fids=[]
        for s,x in zip(ex,xs):
            a=SV(n); a.v[:]=0; a.v[x]=1; a.run(c); fids.append(abs(np.vdot(s.v,a.v))**2)
        L=lower(c); fn=float(np.real(ex[0].v.conj()@qnoise2.run(n,L,init=x0,**NK)@ex[0].v))
        rows.append(dict(m=m,ideal=float(np.mean(fids)),ideal_min=float(np.min(fids)),gates=cnt(L)[0],twoq=cnt(L)[1],noisy=fn))
    b=max(rows,key=lambda r:r['noisy']); out['sweep'][n]=dict(rows=rows,best_m=b['m'],log2n2=np.log2(n)+2)
    print(f'n={n} best m={b["m"]} (log2n+2={np.log2(n)+2:.2f}) t={time.time()-t0:.0f}s')
    for r in rows: print(f'   m={r["m"]:2d} idealF={r["ideal"]:.6f} (min {r["ideal_min"]:.6f}) gates={r["gates"]} 2q={r["twoq"]} noisyF={r["noisy"]:.4f}')
# phase estimation: t counting qubits + 1 eigen ancilla, U=P(2πφ) on |1>
for t in range(3,10):
    phis=rng.random(10); bm=out['sweep'][t]['best_m']; res={}
    for lab,m in (('exact',t),('best_m',bm),('m=2',2)):
        pi_,pn=[],[]
        for phi in phis:
            c=[('X',[t])]+[('H',[k]) for k in range(t)]+[('CP',[k,t],2*np.pi*phi*2**k) for k in range(t)]+inverse(aqft(t,m))
            y=int(round(phi*2**t))%2**t
            p=SV(t+1).run(c).probs(); pi_.append(p[y+2**t])
            L=lower(c); rho=qnoise2.run(t+1,L,**NK); pn.append(float(np.real(rho[y+2**t,y+2**t])))
        res[lab]=dict(m=m,ideal=[float(np.mean(pi_)),float(np.std(pi_))],noisy=[float(np.mean(pn)),float(np.std(pn))])
    out['pe'][t]=res
    print(f'PE t={t}: '+'; '.join(f'{k}(m={v["m"]}) P(correct) ideal {v["ideal"][0]:.4f}±{v["ideal"][1]:.4f} noisy {v["noisy"][0]:.4f}±{v["noisy"][1]:.4f}' for k,v in res.items()))
print('elapsed',round(time.time()-t0,1)); json.dump(out,open('aqft_results.json','w'),default=float)
