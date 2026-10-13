import numpy as np,json
from qsim import *; from qnoise import *; from qopt import optimize
from test_sim_helpers import rc
out={}
# 1 global depolarizing: F = (1-p)^k + (1-(1-p)^k)/d exactly
n=3;p=0.02;err=0;rows=[]
for k in [1,5,10,20,40]:
    c=[('H',[i%n]) if i%2==0 else ('CNOT',[i%n,(i+1)%n]) for i in range(k)]
    psi=SV(n).run(c).v; F=fid(psi,run_dm(n,c,p,mode='global')); pred=(1-p)**k+(1-(1-p)**k)/2**n
    err=max(err,abs(F-pred)); rows.append((k,F,pred))
print('global dep max err',err,rows); out['global']=(err,rows)
# 2 1-qubit local depolarizing on X-X... use RX chain: Bloch shrink (1-4p/3)^k -> F=(1+(1-4p/3)^k)/2 for |1>-ish pure states
c=[('RX',[0],0.3)]*1; e2=0
for k in [1,10,50]:
    c=[('RX',[0],0.3)]*k; psi=SV(1).run(c).v; F=fid(psi,run_dm(1,c,p)); pred=(1+(1-4*p/3)**k)/2; e2=max(e2,abs(F-pred))
print('local 1q dep (Bloch shrink) max err',e2); out['local1q']=e2
# 3 amplitude damping: P1 after k idle-ish X on |1>: use I gate? apply k 'I' gates on |1>
psi1=None; e3=0;gm=0.05
for k in [1,10,30]:
    c=[('X',[0])]+[('I',[0])]*k; rho=run_dm(1,c,gamma=gm); pred=(1-gm)**(k+1); e3=max(e3,abs(rho[1,1].real-pred))
print('amp damping P1=(1-γ)^k max err',e3); out['ad']=e3
# 4 optimizer improves fidelity
rng=np.random.default_rng(3); Fo=[];Fr=[];red=[]
for i in range(30):
    n=4; c=rc(n,40,rng,redundant=True); o=optimize(c); psi=SV(n).run(c).v
    Fo.append(fid(psi,run_dm(n,c,0.005,0.002))); Fr.append(fid(psi,run_dm(n,o,0.005,0.002))); red.append(1-len(o)/len(c))
Fo,Fr=np.array(Fo),np.array(Fr)
print(f'noisy fid orig={Fo.mean():.4f}±{Fo.std():.4f} opt={Fr.mean():.4f}±{Fr.std():.4f} gain={((Fr-Fo).mean()):.4f}, improved {np.sum(Fr>Fo)}/30, gate red {np.mean(red)*100:.1f}%')
out['opt']=dict(Fo=[Fo.mean(),Fo.std()],Fr=[Fr.mean(),Fr.std()],wins=int(np.sum(Fr>Fo)))
json.dump(out,open('noise_results.json','w'),default=float)
