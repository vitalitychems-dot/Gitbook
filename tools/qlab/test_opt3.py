import numpy as np,json,time
from qsim import *; from qopt import optimize as v1
from qopt2 import optimize2, lower; from qopt3 import optimize3, gray_mcz, phasepoly
import qnoise2; from test_sim_helpers import rc
NK=dict(p1=1e-3,p2=1e-2,gamma=1e-3)
def m(c): return len(c),depth(c),sum(len(g[1])==2 for g in c)
def ufid(n,a,b): U=unitary(n,a);V=unitary(n,b); return abs(np.trace(U.conj().T@V)/2**n)**2
# MCZ check
for k in (3,4,5):
    U=unitary(k,gray_mcz(list(range(k)))); ref=np.eye(2**k); ref[-1,-1]=-1
    print(f'gray MCZ n={k}: CNOTs={sum(g[0]=="CNOT" for g in gray_mcz(list(range(k))))} fid vs diag={abs(np.trace(ref@U)/2**k)**2:.12f}')
def evalset(name,items):
    rows=[];fm=[1,1,1];log=[]
    for n,c in items:
        L=lower(c); psi=SV(n).run(L).v; sc=lambda x:qnoise2.fidelity(n,x,psi,**NK)
        a=lower(v1(L)); b,_=optimize2(a,sc); d,_=optimize3(b,sc,log=log)
        for i,x in enumerate((a,b,d)): fm[i]=min(fm[i],ufid(n,L,x))
        rows.append(m(a)+m(b)+m(d)+(sc(a),sc(b),sc(d)))
    R=np.array(rows,float); acc={}
    for l in log: acc.setdefault(l[0],[0,0]); acc[l[0]][0]+=1; acc[l[0]][1]+=l[5]
    lab=['gates','depth','2q','F']
    print(f'== {name} N={len(items)} min exact fid v1/v2/v3 = {fm[0]:.12f}/{fm[1]:.12f}/{fm[2]:.12f}  passes(v3 stage) {acc}')
    for j,l in enumerate(lab):
        f='.4f' if l=='F' else '.2f'
        print('   '+l+': '+' -> '.join(f'{R[:,j+3*i if l!="F" else 9+i].mean():{f}}±{R[:,j+3*i if l!="F" else 9+i].std():{f}}' for i in range(3)))
    return dict(fmin=fm,mean=R.mean(0).tolist(),std=R.std(0).tolist(),passes=acc)
out={}; t=time.time(); rng=np.random.default_rng(42); items=[]
for i in range(200):
    n=int(rng.integers(2,7)); items.append((n,rc(n,int(rng.integers(20,60)),rng,redundant=bool(i%2))))
out['random200']=evalset('random200',items)
for n in range(3,9): out[f'qft{n}']=evalset(f'QFT n={n}',[(n,qft(n))])
def grover(n):
    qs=list(range(n)); th=np.arcsin(1/np.sqrt(2**n)); k=int(np.floor(np.pi/(4*th))); mark=2**n-2; M=gray_mcz(qs)
    c=[('H',[i]) for i in qs]
    for _ in range(k):
        xs=[('X',[i]) for i in qs if not (mark>>i)&1]
        c+=xs+M+xs+[('H',[i]) for i in qs]+[('X',[i]) for i in qs]+M+[('X',[i]) for i in qs]+[('H',[i]) for i in qs]
    p=SV(n).run(c).probs()[mark]; print(f'Grover{n}: k={k} P={p:.6f} theory={np.sin((2*k+1)*th)**2:.6f}')
    return c
for n in (3,4,5): out[f'grover{n}']=evalset(f'Grover n={n} (gray MCZ baseline)',[(n,grover(n))])
print('elapsed',round(time.time()-t,1)); json.dump(out,open('opt3_results.json','w'))
