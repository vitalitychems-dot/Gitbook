"""v3: phase-polynomial region resynthesis (greedy parity network + Gauss-Jordan linear fix-up),
gray-code multi-controlled Z, on top of v2 passes. Native basis U3/P, CNOT, CZ."""
import numpy as np
from qopt2 import PASSES as P2, lower, optimize2
TP=2*np.pi
PHASE={'Z':np.pi,'S':np.pi/2,'SDG':-np.pi/2,'T':np.pi/4,'TDG':-np.pi/4}
PHGATES=set(PHASE)|{'P','RZ','CNOT','CZ','CP'}
def is_phase_gate(g):
    if g[0] in PHGATES: return True
    if g[0]=='U3':  # diagonal U3 (theta≈0) is a phase gate
        t=g[2][0]%TP; return min(t,TP-t)<1e-12
    return False
def pc(x): return bin(x).count('1')
def analyse(n,region):
    st=[1<<q for q in range(n)]; terms={}
    def add(m,a): terms[m]=(terms.get(m,0)+a)%TP
    for g in region:
        nm=g[0]
        if nm=='CNOT': a,b=g[1]; st[b]^=st[a]
        elif nm in('CZ','CP'):
            th=np.pi if nm=='CZ' else g[2]; a,b=g[1]
            add(st[a],th/2); add(st[b],th/2); add(st[a]^st[b],-th/2)
        elif nm=='U3': add(st[g[1][0]],g[2][1]+g[2][2])
        elif nm=='RZ' or nm=='P': add(st[g[1][0]],g[2])
        else: add(st[g[1][0]],PHASE[nm])
    terms={m:a for m,a in terms.items() if min(a,TP-a)>1e-12}
    return terms,st
def synth(n,terms,target):
    st=[1<<q for q in range(n)]; out=[]; terms=dict(terms)
    def cx(j,i): st[i]^=st[j]; out.append(('CNOT',[j,i]))
    def cost(s_): return sum(min(pc(x^m) for x in s_) for m in terms)
    while True:
        for q in range(n):
            if st[q] in terms: out.append(('P',[q],terms.pop(st[q])))
        if not terms: break
        cur=cost(st); best=None
        for j in range(n):
            for i in range(n):
                if i==j: continue
                s2=list(st); s2[i]^=st[j]; c=cost(s2)
                if best is None or c<best[0]: best=(c,j,i)
        if best[0]<cur: cx(best[1],best[2]); continue
        # fallback: build cheapest term exactly
        m=min(terms,key=lambda m:min(pc(x^m) for x in st)); co=coords(st,m)
        sup=[q for q in range(n) if co>>q&1]; i=sup[0]
        for j in sup[1:]: cx(j,i)
    # linear fix-up: make st == target
    B=[coords(target,st[q]) for q in range(n)]
    def row(j,i): B[i]^=B[j]; cx(j,i)
    for c in range(n):
        if not B[c]>>c&1: row(next(r for r in range(c+1,n) if B[r]>>c&1),c)
        for r in range(n):
            if r!=c and B[r]>>c&1: row(c,r)
    assert st==target
    return out
def coords(rows,m):
    n=len(rows)
    for k in range(1<<n):
        v=0
        for q in range(n):
            if k>>q&1: v^=rows[q]
        if v==m: return k
    raise ValueError
def twoq(c): return sum(len(g[1])==2 for g in c)
def phasepoly(c,n=None):
    n=n or (max(q for g in c for q in g[1])+1); out=[]; rem=list(c)
    while rem:
        if not is_phase_gate(rem[0]): out.append(rem.pop(0)); continue
        region=[]; deferred=[]; blocked=set()
        for g in rem:
            if is_phase_gate(g) and not (set(g[1])&blocked): region.append(g)
            else: deferred.append(g); blocked|=set(g[1])
        terms,A=analyse(n,region); new=synth(n,terms,A)
        out+= new if twoq(new)<twoq(region) or (twoq(new)==twoq(region) and len(new)<len(region)) else region
        rem=deferred
    return out
PASSES3=dict(P2); PASSES3['phasepoly']=phasepoly
def optimize3(c,scorer,**kw):
    import qopt2
    old=qopt2.PASSES; qopt2.PASSES=PASSES3
    try: return optimize2(c,scorer,**kw)
    finally: qopt2.PASSES=old
def gray_mcz(qs):
    """ancilla-free C^{m-1}Z as phase polynomial on all subsets, Gray-code parity network: 2^m-2 CNOTs."""
    m=len(qs); ang=lambda S:(-1)**(len(S)+1)*np.pi/2**(m-1); c=[]
    def block(qq):
        t=qq[-1]; ct=qq[:-1]; k=len(ct); c.append(('P',[t],ang([t]))); prev=0
        for i in range(1,2**k):
            g=i^(i>>1); b=(g^prev).bit_length()-1; prev=g
            c.append(('CNOT',[ct[b],t])); c.append(('P',[t],ang([t]+[ct[j] for j in range(k) if g>>j&1])))
        if k: c.append(('CNOT',[ct[prev.bit_length()-1],t]))
        if k: block(ct)
    block(list(qs)); return c
