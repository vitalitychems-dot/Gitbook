"""Cycle-1 quantum claims, tested in simulation (numpy + qlab). python3 quantum.py -> quantum_results.json"""
import sys, json, itertools, numpy as np
sys.path.insert(0, "/workspace/rick/qlab"); import qsim, aqft
rng = np.random.default_rng(1); R = {}
X=np.array([[0,1],[1,0]]);Z=np.diag([1.,-1]);Y=np.array([[0,-1j],[1j,0]]);I=np.eye(2)
def haar(n=2):
    v=rng.normal(size=n)+1j*rng.normal(size=n); return v/np.linalg.norm(v)
# Q1 CHSH: classical max 2 (all 16 deterministic strategies), quantum Bell state reaches 2*sqrt2 (Tsirelson)
cl=max(a0*b0+a0*b1+a1*b0-a1*b1 for a0,a1,b0,b1 in itertools.product([1,-1],repeat=4))
phi=np.array([1,0,0,1])/np.sqrt(2); E=lambda A,B: np.real(phi.conj()@np.kron(A,B)@phi)
A0,A1=Z,X; B0=(Z+X)/np.sqrt(2); B1=(Z-X)/np.sqrt(2)
q=E(A0,B0)+E(A0,B1)+E(A1,B0)-E(A1,B1)
# random search: no observable pair beats Tsirelson
def obs(): v=haar(); return 2*np.outer(v,v.conj())-I
best=max(abs(E(a0,b0)+E(a0,b1)+E(a1,b0)-E(a1,b1)) for a0,a1,b0,b1 in ([obs() for _ in range(4)] for _ in range(20000)))
R["Q1_CHSH"]=dict(classical_max=cl,quantum=q,tsirelson=2*np.sqrt(2),random_search_max=best,verdict="CONFIRMED" if abs(q-2*np.sqrt(2))<1e-9 and best<=2*np.sqrt(2)+1e-9 and cl==2 else "FAILED")
# Q2 no-cloning: Buzek-Hillery UQCM isometry fidelity 5/6; CNOT copier avg 2/3; random isometries never exceed 5/6
a,b=np.sqrt(2/3),np.sqrt(1/6)
def k(*bits): v=np.zeros(8); v[int("".join(map(str,bits)),2)]=1; return v
V=np.stack([a*k(0,0,0)+b*(k(0,1,1)+k(1,0,1)), a*k(1,1,1)+b*(k(0,1,0)+k(1,0,0))],1)  # copy1,copy2,ancilla
def fid(V,psi):
    out=V@psi; rho=np.outer(out,out.conj()).reshape(2,2,2,2,2,2)
    r1=np.einsum('abcdbc->ad',rho); return np.real(psi.conj()@r1@psi)
st=[haar() for _ in range(2000)]
f_bh=np.mean([fid(V,s) for s in st])
Vc=np.zeros((8,2)); Vc[0,0]=1; Vc[6,1]=1  # CNOT copy |x>->|x x 0>
f_c=np.mean([fid(Vc,s) for s in st])
def rand_iso():
    M=rng.normal(size=(8,2))+1j*rng.normal(size=(8,2)); Q,_=np.linalg.qr(M); return Q
f_r=max(min(np.mean([fid(W,s) for s in st[:60]]),np.mean([fid(W,s) for s in st[:60]])) for W in (rand_iso() for _ in range(3000)))
R["Q2_no_cloning"]=dict(isometry_ok=bool(np.allclose(V.T@V,np.eye(2))),BH_fidelity=f_bh,bound=5/6,cnot_copier=f_c,random_isometry_best=f_r,
  verdict="CONFIRMED" if abs(f_bh-5/6)<1e-9 and f_r<5/6 else "FAILED")
# Q3 Grover: optimal iterations ~ (pi/4) sqrt(N)
rows=[]
for n in range(2,11):
    N=2**n; t=N-1; v=np.ones(N)/np.sqrt(N); best=(0,0)
    for it in range(1,int(np.pi/4*np.sqrt(N))+3):
        v[t]*=-1; v=2*v.mean()-v; p=abs(v[t])**2
        if p>best[1]: best=(it,p)
    rows.append((N,)+best)
Ns=np.array([r[0] for r in rows]); its=np.array([r[1] for r in rows])
slope=np.polyfit(np.log(Ns[3:]),np.log(its[3:]),1)[0]
R["Q3_grover"]=dict(table=[dict(N=int(a),iters=int(b),p=round(float(c),4)) for a,b,c in rows],loglog_slope=slope,
  verdict="CONFIRMED" if abs(slope-0.5)<0.06 else "FAILED")
# Q4 AQFT: ||QFT-AQFT_m|| vs Barenco-style bound  pi*n*2^-m  (and is the error monotone in m?)
tab=[]
for n in (4,5,6):
    U=qsim.unitary(n,qsim.qft(n))
    for m in range(1,n):
        e=np.linalg.norm(U-qsim.unitary(n,aqft.aqft(n,m)),2); tab.append(dict(n=n,m=m,err=round(float(e),5),bound=round(float(np.pi*n*2.0**-m),5)))
ok=all(t["err"]<=t["bound"] for t in tab)
R["Q4_aqft_bound"]=dict(table=tab,verdict="CONFIRMED (bound holds)" if ok else "DISPROVED (bound violated)")
# Q5 VQE H2 (STO-3G, R=0.735A, 2-qubit reduced Hamiltonian, published-style coefficients) vs exact diagonalization
g=[-1.052373245772859,0.39793742484318045,-0.39793742484318045,-0.01128010425623538,0.18093119978423156]
H=g[0]*np.kron(I,I)+g[1]*np.kron(I,Z)+g[2]*np.kron(Z,I)+g[3]*np.kron(Z,Z)+g[4]*np.kron(X,X)
ex=np.linalg.eigvalsh(H)[0]
def ansatz(t):  # 1-parameter: cos t|01> + sin t|10> (particle-conserving)
    v=np.zeros(4); v[1]=np.cos(t); v[2]=np.sin(t); return v
ts=np.linspace(-np.pi,np.pi,4001); es=[ansatz(t)@H@ansatz(t) for t in ts]; i=int(np.argmin(es))
from math import isclose
lo,hi=ts[max(i-1,0)],ts[min(i+1,len(ts)-1)]
for _ in range(60):
    m1,m2=lo+(hi-lo)/3,hi-(hi-lo)/3
    if ansatz(m1)@H@ansatz(m1)<ansatz(m2)@H@ansatz(m2): hi=m2
    else: lo=m1
ev=ansatz((lo+hi)/2)@H@ansatz((lo+hi)/2)
R["Q5_vqe_h2"]=dict(vqe=ev,exact=ex,abs_err=abs(ev-ex),chem_acc=1.6e-3,note="electronic energy, Hartree; nuclear repulsion ~+0.7199 gives total ~ -1.137",
  verdict="CONFIRMED" if abs(ev-ex)<1.6e-3 else "FAILED")
json.dump(R,open("quantum_results.json","w"),indent=1,default=float)
for k_,v in R.items(): print(k_,v["verdict"],{x:y for x,y in v.items() if x not in("table","verdict")})
