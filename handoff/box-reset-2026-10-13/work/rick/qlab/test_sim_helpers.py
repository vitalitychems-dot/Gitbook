import numpy as np
names=['H','X','Y','Z','S','T','RX','RY','RZ','CNOT','CZ','SWAP']
def rg(n,rng):
    g=names[rng.integers(len(names))]
    if g in ('CNOT','CZ','SWAP'): a,b=rng.choice(n,2,replace=False); return (g,[int(a),int(b)])
    if g.startswith('R'): return (g,[int(rng.integers(n))],float(rng.choice([0.0,rng.uniform(-np.pi,np.pi)],p=[.1,.9])))
    return (g,[int(rng.integers(n))])
def rc(n,L,rng,redundant=False):
    c=[]
    while len(c)<L:
        g=rg(n,rng); c.append(g)
        if redundant and rng.random()<0.3: c.append(g if len(g)==2 else (g[0],g[1],float(rng.uniform(-1,1))))
    return c
