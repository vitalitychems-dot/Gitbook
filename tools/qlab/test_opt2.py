import numpy as np,json,time,sys
from qsim import *; from qopt import optimize as v1
from qopt2 import *; import qnoise, qnoise2
from test_sim_helpers import rc
NK=dict(p1=1e-3,p2=1e-2,gamma=1e-3)
def m(c): return len(c),depth(c),sum(len(g[1])==2 for g in c)
def ufid(n,a,b): U=unitary(n,a);V=unitary(n,b); return abs(np.trace(U.conj().T@V)/2**n)**2
# 0 cross-check fast DM vs reference DM (local depolarizing, same p for all gates)
rng=np.random.default_rng(0); xe=0
for _ in range(5):
    c=lower(rc(3,15,rng)); psi=SV(3).run(c).v
    a=qnoise.fid(psi,qnoise.run_dm(3,c,0.01,0.002)); b=qnoise2.fidelity(3,c,psi,p1=0.01,p2=0.01,gamma=0.002); xe=max(xe,abs(a-b))
print('fast DM vs reference DM max diff',xe)
# zyz check
ze=0
for _ in range(500):
    X=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); U,_=np.linalg.qr(X); V=u3m(*zyz(U)); ze=max(ze,1-abs(np.trace(U.conj().T@V)/2)**2)
print('ZYZ 500 random U: max infidelity',ze)
def evalset(name,items):
    rows=[];fmin=1;log=[]
    for n,c in items:
        base=lower(v1(lower(c)))  # v1 baseline in native basis
        psi=SV(n).run(lower(c)).v
        sc=lambda x:qnoise2.fidelity(n,x,psi,**NK)
        o,fo=optimize2(base,sc,log=log)
        fb=sc(base); fmin=min(fmin,ufid(n,lower(c),o))
        rows.append(m(lower(c))+m(base)+m(o)+(sc(lower(c)),fb,fo))
    R=np.array(rows,float)
    lab=['raw gates','raw depth','raw 2q','v1 gates','v1 depth','v1 2q','v2 gates','v2 depth','v2 2q','F raw','F v1','F v2']
    acc={}
    for l in log: acc.setdefault(l[0],[0,0]); acc[l[0]][0]+=1; acc[l[0]][1]+=l[5]
    print(f'== {name}: N={len(items)} min exact fidelity={fmin:.12f} pass={fmin>1-1e-9}')
    for i,l in enumerate(lab): print(f'   {l}: {R[:,i].mean():.4f}±{R[:,i].std():.4f}' if l.startswith('F') else f'   {l}: {R[:,i].mean():.2f}±{R[:,i].std():.2f}')
    print('   passes tried/accepted',acc)
    return dict(fmin=fmin,mean=dict(zip(lab,R.mean(0).tolist())),std=dict(zip(lab,R.std(0).tolist())),passes=acc,rows=R.tolist())
out={}
t=time.time()
rng=np.random.default_rng(42)
items=[]
for i in range(200):
    n=int(rng.integers(2,7)); items.append((n,rc(n,int(rng.integers(20,60)),rng,redundant=bool(i%2))))
out['random200']=evalset('random200',items)
for n in range(3,9): out[f'qft{n}']=evalset(f'QFT n={n}',[(n,qft(n))])
def grover(n,variant):
    # n=3: CCZ; n=4,5: multi-controlled Z via ancilla-free recursive... use CCZ ladder with one ancilla-free trick: for n<=5 use MCZ built from CCZ+CP? keep n=3 exact, n=4/5 via V-chain needs ancillas -> use C^{n-1}Z via CP gray-code decomposition
    def mcz(qs):
        if len(qs)==3: return [('CCZ',qs,variant)]
        # C^{k}Z by gray-code CP ladder: phase pi split into 2^(k) controlled phases (Barenco lemma 7.1 style using CP + CNOT)
        k=len(qs)-1; t=qs[-1]; ctr=qs[:-1]; c=[]; ang=np.pi/2**(k-1)
        prev=0
        for i in range(1,2**k):
            gray=i^(i>>1); diff=gray^prev; prev=gray
            bit=diff.bit_length()-1; hi=(gray).bit_length()-1
            if bin(gray).count('1')>1 or i>1:
                pass
            # parity-network: build parity of controls in gray onto highest set control
            c.append(('_GRAY',gray))
        # simpler exact construction: use diagonal phase polynomial via CNOT parity network
        return phasepoly(qs)
    def phasepoly(qs):
        # MCZ = exp(i pi x1..xn) = product over nonempty subsets S of exp(i*pi*(-1)^{|S|+1}/2^{n-1} * parity(S))... implemented with P on parities
        m_=len(qs); c=[]
        for S in range(1,2**m_):
            bits=[qs[j] for j in range(m_) if S>>j&1]; th=np.pi*(-1)**(len(bits)+1)/2**(m_-1)
            tgt=bits[-1]
            for b in bits[:-1]: c.append(('CNOT',[b,tgt]))
            c.append(('P',[tgt],th))
            for b in reversed(bits[:-1]): c.append(('CNOT',[b,tgt]))
        return c
    qs=list(range(n)); th=np.arcsin(1/np.sqrt(2**n)); k=int(np.floor(np.pi/(4*th))); mark=2**n-2
    c=[('H',[i]) for i in qs]
    for _ in range(k):
        xs=[('X',[i]) for i in qs if not (mark>>i)&1]
        c+=xs+mcz(qs)+xs
        c+=[('H',[i]) for i in qs]+[('X',[i]) for i in qs]+mcz(qs)+[('X',[i]) for i in qs]+[('H',[i]) for i in qs]
    return c,mark,k,th
for n in (3,4,5):
    c,mark,k,th=grover(n,'old'); p=SV(n).run(lower(c)).probs()[mark]
    print(f'Grover{n}: k={k} P(mark)={p:.6f} theory={np.sin((2*k+1)*th)**2:.6f}')
    out[f'grover{n}']=evalset(f'Grover n={n} (CCZ=old 8-CX lowering)' if n==3 else f'Grover n={n}',[(n,c)])
    if n==3:
        c6,_,_,_=grover(3,'6cx'); out['grover3_6cx']=evalset('Grover n=3 with 6-CNOT CCZ',[(3,c6)])
print('elapsed s',round(time.time()-t,1))
json.dump(out,open('opt2_results.json','w'))
