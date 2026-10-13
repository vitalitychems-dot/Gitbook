import numpy as np,json,time,sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); import qlab
from calib import load; from twin import run,readout,esp,relax_kraus; from route import route,best_layouts
from qsim import SV,unitary; from qopt2 import lower,u3m,zyz; from aqft import aqft,inverse
D=os.path.join(os.path.dirname(__file__),'devices'); R={}
def ok(name,cond,info): print(('PASS' if cond else 'FAIL'),name,info,flush=True); R[name]=dict(pass_=bool(cond),info=info)
# synthetic 1-qubit device for injected-parameter tests
def dev1(e=0.0,T1=1e9,T2=1e9,t1q=35.0,ro=0.0): return dict(name='syn',qubits=[dict(T1=T1,T2=T2,e1q=e,t1q=t1q,ex=e,readout_p01=ro,readout_p10=ro)],edges={},source='synthetic')
# 1. T1 / T2 analytic decay
d=dev1(T1=100.0,T2=80.0); e1=e2=0
for tus in (5,20,50,100,200):
    rho=run(d,[0],[('X',[0]),('DELAY',[0],tus*1000)],1,idle=False); # X itself costs 1 pulse 35ns
    e1=max(e1,abs(rho[1,1].real-np.exp(-(tus*1000+35)/1000/100)))
    d0=dev1(T1=100.0,T2=80.0,t1q=0.0)  # zero-length pulses so the analytic Ramsey formula is exact
    rho=run(d0,[0],[('H',[0]),('DELAY',[0],tus*1000),('H',[0])],1,idle=False)
    e2=max(e2,abs(rho[0,0].real-(1+np.exp(-tus/80))/2))
ok('T1 decay P1=exp(-t/T1)',e1<1e-9,f'max err {e1:.2e} (T1=100us, t=5..200us)')
ok('T2 Ramsey P0=(1+exp(-t/T2))/2',e2<1e-9,f'max err {e2:.2e} (T2=80us)')
# 2. readout confusion
d=dev1(ro=0.03); p=readout(d,[0],np.array([0.,1.]),1); ok('readout confusion',abs(p[0]-0.03)<1e-12,f'P(0|1)={p[0]:.4f}')
# 3. RB-style injected-parameter recovery
rng=np.random.default_rng(1); res=[]
for e_true in (1e-4,5e-4,2e-3):
    d=dev1(e=e_true/2)  # U3 = 2 pulses -> error e_true per random U3 "Clifford"
    Ms=[1,20,50,100,200,400]; S=[]
    for m in Ms:
        s=[]
        for _ in range(6):
            gs=[('U3',[0],tuple(rng.uniform(0,2*np.pi,3))) for _ in range(m)]
            U=np.eye(2)
            for g in gs: U=u3m(*g[2])@U
            gs.append(('U3',[0],zyz(U.conj().T)))
            s.append(run(d,[0],gs,1)[0,0].real)
        S.append(np.mean(s))
    S=np.array(S); y=np.log((S-0.5)/0.5); Mx=np.array(Ms)+1; a=np.exp(np.polyfit(Mx,y,1)[0]); r=(1-a)/2
    res.append((e_true,r,abs(r-e_true)/e_true))
worst=max(x[2] for x in res)
# 3b. RB on a thermal device: does the fitted error match the calibrated per-U3 error (2*e1q) once T1/T2 are on?
dth=dev1(e=3.5e-4,T1=70.0,T2=60.0,t1q=35.5); S=[]; Ms=[1,20,50,100,200,400]
for m in Ms:
    s=[]
    for _ in range(6):
        gs=[('U3',[0],tuple(rng.uniform(0,2*np.pi,3))) for _ in range(m)]; U=np.eye(2)
        for g in gs: U=u3m(*g[2])@U
        gs.append(('U3',[0],zyz(U.conj().T))); s.append(run(dth,[0],gs,1)[0,0].real)
    S.append(np.mean(s))
S=np.array(S); a=np.exp(np.polyfit(np.array(Ms)+1,np.log((S-0.5)/0.5),1)[0]); rth=(1-a)/2
ok('RB on thermal device recovers calibrated U3 error 2*e1q (tol 10%)',abs(rth-7e-4)/7e-4<0.10,f'fit={rth:.3e} vs 7.0e-4 (relerr {abs(rth-7e-4)/7e-4*100:.1f}%; T1 decay is non-unital so B!=0.5 is a known bias)')
ok('RB injected-error recovery (tol 5%)',worst<0.05,'; '.join(f'e={a:.1e} fit={b:.3e} relerr={c*100:.2f}%' for a,b,c in res))
# 4. real devices
devs={n:load(os.path.join(D,f'props_{n}.json')) for n in ('manila','nairobi','guadalupe')}
for n,d in devs.items():
    e2=[v[0] for v in d['edges'].values()]; Q=d['qubits']
    print(f"{n}: {len(Q)}q, {len(e2)} couplers, T1 med {np.median([q['T1'] for q in Q]):.1f}us, T2 med {np.median([q['T2'] for q in Q]):.1f}us, sx err med {np.median([q['e1q'] for q in Q]):.2e}, cx err med {np.median(e2):.2e}, readout med {np.median([(q['readout_p01']+q['readout_p10'])/2 for q in Q]):.3f}")
# 5. layout + AQFT m per device, n=5 QFT on input |x>
from qsim import qft
def permute(psi,final,n):
    # logical qubit l ends at position final[l]; axis index = n-1-qubit
    T=psi.reshape([2]*n); src=[n-1-l for l in range(n)]; dst=[n-1-final[l] for l in range(n)]
    return np.moveaxis(T,src,dst).reshape(-1)
def fid(d,rc,phys,n,x,final,initpos):
    s=SV(n); s.v[:]=0; s.v[x]=1; psi=permute(s.run(qft(n)).v,final,n)   # reference = EXACT QFT|x>
    xi=sum(((x>>l)&1)<<initpos[l] for l in range(n))                    # |x> placed on initial positions
    return float(np.real(psi.conj()@run(d,phys,rc,n,init=xi)@psi))
    return float(np.real(psi.conj()@run(d,phys,rc,n,init=x)@psi))
def bfs_naive(d,n):
    from calib import neighbors; nb=neighbors(d); order=[0]; i=0
    while len(order)<n:
        for y in sorted(nb[order[i]]):
            if y not in order and len(order)<n: order.append(y)
        i+=1
    return order
R['layout']={}; n=5; xs=[3,22,13,30]
for name,d in devs.items():
    rows=[]
    for m in range(2,n+1):
        c=lower(aqft(n,m)); c=[g for g in c]
        naive=tuple(bfs_naive(d,n)); rcn,ph,swn,fi=route(d,naive,c); fn=np.mean([fid(d,rcn,ph,n,x,fi,list(range(n))) for x in xs])
        top=best_layouts(d,c,n,top=3)
        best=None
        for es,lay,sw in top:
            rc,ph,sw,fi=route(d,lay,c); f=np.mean([fid(d,rc,ph,n,x,fi,list(range(n))) for x in xs])
            if best is None or f>best[0]: best=(f,lay,sw,es)
        rows.append(dict(m=m,naive_F=fn,naive_swaps=swn,best_F=best[0],best_layout=list(best[1]),best_swaps=best[2]))
        print(f'  {name} m={m}: naive layout F={fn:.4f} swaps={swn} | best layout {list(best[1])} F={best[0]:.4f} swaps={best[2]} gain={best[0]-fn:+.4f}',flush=True)
    bm=max(rows,key=lambda r:r['best_F']); R['layout'][name]=dict(rows=rows,best_m=bm['m'])
    print(f'  {name}: best m={bm["m"]} F={bm["best_F"]:.4f}; exact-QFT naive F={rows[-1]["naive_F"]:.4f}')
json.dump(R,open(os.path.join(os.path.dirname(__file__),'..','twin_results.json'),'w'),default=float,indent=1)
