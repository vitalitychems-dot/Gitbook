import numpy as np,json
from qsim import *; from qopt import optimize
from test_sim_helpers import rc
rng=np.random.default_rng(42); fids=[];gr=[];dr=[]
for i in range(200):
    n=int(rng.integers(2,7)); c=rc(n,int(rng.integers(20,80)),rng,redundant=True)
    o=optimize(c); U=unitary(n,c);V=unitary(n,o)
    f=abs(np.trace(U.conj().T@V)/2**n)**2; fids.append(f)
    gr.append(1-len(o)/len(c)); dr.append(1-depth(o)/max(depth(c),1))
fids=np.array(fids);gr=np.array(gr);dr=np.array(dr)
print(f'random200: min fid={fids.min():.12f} pass={np.all(fids>1-1e-9)} gate red={gr.mean()*100:.1f}±{gr.std()*100:.1f}% depth red={dr.mean()*100:.1f}±{dr.std()*100:.1f}%')
# pure-random (no injected redundancy)
g2=[];f2=[]
for i in range(200):
    n=int(rng.integers(2,7)); c=rc(n,50,rng,redundant=False); o=optimize(c)
    f2.append(abs(np.trace(unitary(n,c).conj().T@unitary(n,o))/2**n)**2); g2.append(1-len(o)/len(c))
print(f'uniform-random200: min fid={min(f2):.12f} gate red={np.mean(g2)*100:.1f}±{np.std(g2)*100:.1f}%')
# QFT, QFT·QFT^-1-ish, Grover decomposed with H/X/CZ
q=qft(5); oq=optimize(q); print('QFT5',len(q),'->',len(oq))
def inv(c): 
    r=[]
    for g in reversed(c): r.append((g[0],g[1],-g[2]) if len(g)>2 else g)
    return r
qq=qft(5)+inv(qft(5)); o=optimize(qq); print('QFT5·QFT5^-1',len(qq),'->',len(o), 'fid',abs(np.trace(unitary(5,o))/32)**2)
# Grover n=3 with textbook decomposition: oracle X..CCZ..X, diffuser H X CCZ X H; CCZ as CP/CNOT decomposition
def ccz(a,b,c_): return [('CP',[b,c_],np.pi/2),('CNOT',[a,b]),('CP',[b,c_],-np.pi/2),('CNOT',[a,b]),('CP',[a,c_],np.pi/2)]
g=[('H',[i]) for i in range(3)]
for _ in range(2):
    g+= [('X',[0])]+ccz(0,1,2)+[('X',[0])]
    g+= [('H',[i]) for i in range(3)]+[('X',[i]) for i in range(3)]+ccz(0,1,2)+[('X',[i]) for i in range(3)]+[('H',[i]) for i in range(3)]
og=optimize(g); U=unitary(3,g);V=unitary(3,og)
print('Grover3',len(g),'->',len(og),'depth',depth(g),'->',depth(og),'fid',abs(np.trace(U.conj().T@V)/8)**2, 'P(mark=6)',SV(3).run(g).probs()[6].round(6))
json.dump({'fmin':fids.min(),'gr':[gr.mean(),gr.std()],'dr':[dr.mean(),dr.std()],'g2':[np.mean(g2),np.std(g2)],'f2':min(f2)},open('opt_results.json','w'))
