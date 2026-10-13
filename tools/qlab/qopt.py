import numpy as np
SELF_INV={'H','X','Y','Z','CNOT','CZ','SWAP'}
INV={'S':'SDG','SDG':'S','T':'TDG','TDG':'T'}
ROT={'RX','RY','RZ','P','CP'}
DIAG={'Z','S','T','SDG','TDG','RZ','P','CZ','CP'}
PH={'Z':np.pi,'S':np.pi/2,'SDG':-np.pi/2,'T':np.pi/4,'TDG':-np.pi/4}
def key(g): return (g[0],tuple(g[1]) if g[0] not in ('CZ','SWAP','CP') else tuple(sorted(g[1])))
def commute(a,b):
    if not set(a[1])&set(b[1]): return True
    if a[0] in DIAG and b[0] in DIAG: return True
    # diagonal 1q on CNOT control commutes
    for x,y in ((a,b),(b,a)):
        if y[0]=='CNOT' and x[0] in DIAG and len(x[1])==1 and x[1][0]==y[1][0]: return True
        if y[0]=='CNOT' and x[0] in('X','RX') and x[1][0]==y[1][1]: return True
    return False
def try_merge(a,b):
    """return [] (cancel), [g] merged, or None"""
    if key(a)!=key(b):
        # Z-type phase merging into P on same qubit
        if a[0] in PH.keys()|{'P'} and b[0] in PH.keys()|{'P'} and a[1]==b[1]:
            th=(a[2] if a[0]=='P' else PH[a[0]])+(b[2] if b[0]=='P' else PH[b[0]]); return [('P',a[1],th)]
        if INV.get(a[0])==b[0] and a[1]==b[1]: return []
        return None
    if a[0] in SELF_INV: return []
    if a[0] in ROT: return [(a[0],a[1],a[2]+b[2])]
    if a[0] in PH: return [('P',a[1],2*PH[a[0]])]
    return None
def is_id(g,eps=1e-12):
    if g[0] in ROT:
        t=(g[2]) % (4*np.pi if g[0] in('RX','RY','RZ') else 2*np.pi)
        return min(t,(4*np.pi if g[0] in('RX','RY','RZ') else 2*np.pi)-t)<eps
    return g[0]=='I'
def optimize(circ,maxit=20):
    c=[g for g in circ if not is_id(g)]
    for _ in range(maxit):
        changed=False; out=[]
        for g in c:
            placed=False
            # scan back through commuting gates for a merge partner
            for j in range(len(out)-1,-1,-1):
                m=try_merge(out[j],g)
                if m is not None:
                    new=[x for x in m if not is_id(x)]
                    out[j:j+1]=new; placed=changed=True; break
                if not commute(out[j],g): break
            if not placed: out.append(g)
        c=out
        if not changed: break
    return c
