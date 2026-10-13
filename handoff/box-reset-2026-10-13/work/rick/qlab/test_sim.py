import numpy as np,time,tracemalloc,json
from qsim import *
R=[]
def rec(name,ok,info): R.append((name,bool(ok),info)); print(('PASS' if ok else 'FAIL'),name,info)
# Bell
s=SV(2,seed=1).run([('H',[0]),('CNOT',[0,1])]); m=s.sample(100000)
f00=np.mean(m==0); f11=np.mean(m==3); corr=np.mean(m==0)+np.mean(m==3)
rec('Bell 50/50 + correlation',abs(f00-.5)<.01 and corr==1,f'P00={f00:.4f} P11={f11:.4f} P(equal)={corr:.4f} (1e5 shots)')
# GHZ
bad=0;worst=0
for n in range(3,21):
    s=SV(n).run([('H',[0])]+[('CNOT',[0,i]) for i in range(1,n)]); p=s.probs()
    e=abs(p[0]-.5)+abs(p[-1]-.5); worst=max(worst,e,abs(np.linalg.norm(s.v)-1))
rec('GHZ n=3..20',worst<1e-10,f'max |P-0.5|+norm err={worst:.2e}')
# unitarity / norm
rng=np.random.default_rng(7); names=['H','X','Y','Z','S','T','RX','RY','RZ','CNOT','CZ','SWAP']
def rc(n,L,rng):
    c=[]
    for _ in range(L):
        g=names[rng.integers(len(names))]
        if g in ('CNOT','CZ','SWAP'): a,b=rng.choice(n,2,replace=False); c.append((g,[int(a),int(b)]))
        elif g.startswith('R'): c.append((g,[int(rng.integers(n))],float(rng.uniform(-np.pi,np.pi))))
        else: c.append((g,[int(rng.integers(n))]))
    return c
ue=0
for _ in range(20): U=unitary(4,rc(4,40,rng)); ue=max(ue,np.abs(U.conj().T@U-np.eye(16)).max())
s=SV(16).run(rc(16,2000,rng)); ne=abs(np.linalg.norm(s.v)-1)
rec('Unitarity (n=4) & norm (n=16, 2000 gates)',ue<1e-10 and ne<1e-10,f'max|U†U-I|={ue:.2e}, norm err={ne:.2e}')
# QFT vs FFT
qe=0
for n in range(2,11):
    x=rng.normal(size=2**n)+1j*rng.normal(size=2**n); x/=np.linalg.norm(x)
    s=SV(n); s.v=x.copy(); s.run(qft(n)); ref=np.fft.ifft(x)*np.sqrt(2**n); qe=max(qe,np.abs(s.v-ref).max())
rec('QFT == numpy FFT (n=2..10)',qe<1e-10,f'max abs err={qe:.2e}')
# Grover
def grover(n,mark,k):
    s=SV(n); s.v[:]=1/np.sqrt(2**n)
    for _ in range(k):
        s.v[mark]*=-1
        for q in range(n): s.apply(('H',[q]))
        s.v[1:]*=-1; s.v*=-1  # 2|0><0|-I up to global phase
        for q in range(n): s.apply(('H',[q]))
    return s.probs()[mark]
ge=0;rows=[]
for n in range(4,11):
    th=np.arcsin(1/np.sqrt(2**n)); k=int(np.floor(np.pi/(4*th))); p=grover(n,5,k); t=np.sin((2*k+1)*th)**2
    ge=max(ge,abs(p-t)); rows.append(f'n{n}:k={k},P={p:.6f}')
rec('Grover n=4..10 vs sin^2((2k+1)θ)',ge<1e-10,f'max err={ge:.2e}; '+'; '.join(rows))
# Deutsch-Jozsa n=6 constant vs balanced
n=6
def dj(f):
    s=SV(n+1).run([('X',[n])]+[('H',[q]) for q in range(n+1)])
    # oracle: phase kickback equivalent -> (-1)^f(x) on input register
    v=s.v.reshape(2,2**n)  # top bit is ancilla q=n
    for x in range(2**n):
        if f(x): v[:,x]=v[::-1,x].copy()
    s.v=v.reshape(-1); s.run([('H',[q]) for q in range(n)])
    return np.abs(s.v.reshape(2,-1)[:,0]).__pow__(2).sum()
pc=dj(lambda x:1); pb=dj(lambda x:bin(x&0b101101).count('1')%2)
rec('Deutsch-Jozsa n=6',abs(pc-1)<1e-10 and pb<1e-10,f'P(0..0) constant={pc:.6f} balanced={pb:.2e}')
# CHSH
def E(a,b):
    s=SV(2).run([('H',[0]),('CNOT',[0,1]),('RY',[0],-a),('RY',[1],-b)]); p=s.probs()
    return p[0]+p[3]-p[1]-p[2]
a0,a1,b0,b1=0,np.pi/2,np.pi/4,-np.pi/4
S=E(a0,b0)+E(a0,b1)+E(a1,b0)-E(a1,b1)
import itertools
cl=max(abs(A0*B0+A0*B1+A1*B0-A1*B1) for A0,A1,B0,B1 in itertools.product([1,-1],repeat=4))
rec('CHSH = 2√2 (Tsirelson) > classical 2',abs(S-2*np.sqrt(2))<1e-10 and cl==2,f'S={S:.10f} (2√2={2*np.sqrt(2):.10f}); classical max={cl}')
# Hadamard test phase est: U=P(phi) on |1>
he=0
for phi in np.linspace(0,2*np.pi,9):
    s=SV(2).run([('X',[1]),('H',[0]),('CP',[0,1],phi),('H',[0])]); p0=s.probs()[[0,2]].sum()
    est=2*p0-1; he=max(he,abs(est-np.cos(phi)))
    s=SV(2).run([('X',[1]),('H',[0]),('CP',[0,1],phi),('SDG',[0]),('H',[0])]); p0=s.probs()[[0,2]].sum(); he=max(he,abs((2*p0-1)-np.sin(phi)))
rec('Hadamard test Re/Im <ψ|U|ψ> = cos/sin φ',he<1e-10,f'max err={he:.2e} over 9 phases')
# perf
perf=[]
for n in [10,14,16,18,20]:
    c=[('H',[q]) for q in range(n)]+[('CNOT',[q,(q+1)%n]) for q in range(n)]
    tracemalloc.start(); t=time.perf_counter(); SV(n).run(c); dt=time.perf_counter()-t; pk=tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
    perf.append((n,len(c),dt,dt/len(c)*1e3,pk/2**20,2**n*16/2**20)); print('perf',perf[-1])
json.dump({'tests':R,'perf':perf},open('sim_results.json','w'),indent=1)
