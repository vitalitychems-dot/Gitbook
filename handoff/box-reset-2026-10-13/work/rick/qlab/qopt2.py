"""Noise-aware gate-rewriting optimizer (v2). Native basis: U3 (1q), CNOT, CZ."""
import numpy as np
from qsim import mat, SV
from qopt import optimize as peephole
TWOQ={'CNOT','CZ'}
def u3m(t,p,l): return np.array([[np.cos(t/2),-np.exp(1j*l)*np.sin(t/2)],[np.exp(1j*p)*np.sin(t/2),np.exp(1j*(p+l))*np.cos(t/2)]])
def gm(g):
    if g[0]=='U3': return u3m(*g[2])
    return mat(g[0],g[2] if len(g)>2 else None)
def zyz(U):
    t=2*np.arctan2(abs(U[1,0]),abs(U[0,0])); e=1e-12
    al=np.angle(U[0,0]) if abs(U[0,0])>e else np.angle(U[1,0])
    if abs(U[1,0])>e: p=np.angle(U[1,0])-al; l=np.angle(-U[0,1])-al
    else: p=np.angle(U[1,1])-al; l=0.0
    V=u3m(t,p,l); assert abs(abs(np.vdot(V.reshape(-1),U.reshape(-1)))-2)<1e-8
    return float(t),float(p),float(l)
def is_ident(U): ph=U[0,0] if abs(U[0,0])>1e-9 else 1; return np.allclose(U/ph,np.eye(2),atol=1e-11) and abs(abs(ph)-1)<1e-9
# ---- lowering to native basis ----
def ccz_old(a,b,c): return [('CP',[b,c],np.pi/2),('CNOT',[a,b]),('CP',[b,c],-np.pi/2),('CNOT',[a,b]),('CP',[a,c],np.pi/2)]
def ccz_6cx(a,b,c):  # standard 6-CNOT, 7-T decomposition
    return [('CNOT',[b,c]),('TDG',[c]),('CNOT',[a,c]),('T',[c]),('CNOT',[b,c]),('TDG',[c]),('CNOT',[a,c]),
            ('T',[b]),('T',[c]),('CNOT',[a,b]),('T',[a]),('TDG',[b]),('CNOT',[a,b])]
def lower(c):
    out=[]
    for g in c:
        n=g[0]
        if n=='CP': a,b=g[1];t=g[2]; out+=[('P',[a],t/2),('CNOT',[a,b]),('P',[b],-t/2),('CNOT',[a,b]),('P',[b],t/2)]
        elif n=='SWAP': a,b=g[1]; out+=[('CNOT',[a,b]),('CNOT',[b,a]),('CNOT',[a,b])]
        elif n=='CCZ': out+=lower(ccz_old(*g[1]) if g[2]=='old' else ccz_6cx(*g[1]))
        else: out.append(g)
    return out
# ---- pass: fuse 1q runs ----
def fuse(c):
    pend={}; out=[]
    def flush(q):
        if q in pend:
            U,cnt,orig=pend.pop(q)
            if is_ident(U): return
            out.append(orig if cnt==1 else ('U3',[q],zyz(U)))
    for g in c:
        if g[0] in TWOQ:
            for q in g[1]: flush(q)
            out.append(g)
        else:
            q=g[1][0]; U,cnt,orig=pend.get(q,(np.eye(2,dtype=complex),0,None)); pend[q]=(gm(g)@U,cnt+1,g)
    for q in list(pend): flush(q)
    return out
# ---- pass: 2q templates ----
def _isH(g): return g[0]=='H' or (g[0]=='U3' and np.allclose(abs(u3m(*g[2])),abs(mat('H')),atol=1e-11) and is_ident(u3m(*g[2])@mat('H')))
def templ_hczh(c):
    """H_t CZ(c,t) H_t -> CNOT(c,t); H_t CNOT(c,t) H_t -> CZ(c,t); H_c H_t CNOT(c,t) H_c H_t -> CNOT(t,c)."""
    c=list(c); changed=True
    while changed:
        changed=False
        for i,g in enumerate(c):
            if g[0] not in TWOQ: continue
            cands=[g[1][1]] + ([g[1][0]] if g[0]=='CZ' else [])
            for t in cands:
                ctl=g[1][0] if t==g[1][1] else g[1][1]
                pj=next((j for j in range(i-1,-1,-1) if t in c[j][1]),None); nj=next((j for j in range(i+1,len(c)) if t in c[j][1]),None)
                if pj is None or nj is None or not(_isH(c[pj]) and _isH(c[nj])): continue
                new=('CNOT',[ctl,t]) if g[0]=='CZ' else ('CZ',[ctl,t])
                c[i]=new; del c[nj]; del c[pj]; changed=True; break
            if changed: break
    return c
def cnot_commute_cancel(c):
    """cancel CNOT pairs separated only by gates that commute with them (shared control or shared target, Z-diag on control, X on target)."""
    c=list(c); changed=True
    def comm(a,b):
        if not set(a[1])&set(b[1]): return True
        if a[0]=='CNOT' and b[0]=='CNOT': return a[1][0]==b[1][0] or a[1][1]==b[1][1]
        if b[0]=='CZ': return set(a[1])&set(b[1])=={a[1][0]} if a[0]=='CNOT' else False
        if b[0] in ('Z','S','T','SDG','TDG','RZ','P') : return b[1][0]==a[1][0]
        if b[0] in ('X','RX'): return b[1][0]==a[1][1]
        return False
    while changed:
        changed=False
        for i,g in enumerate(c):
            if g[0]!='CNOT': continue
            for j in range(i+1,len(c)):
                h=c[j]
                if h[0]=='CNOT' and h[1]==g[1]: del c[j]; del c[i]; changed=True; break
                if not comm(g,h): break
            if changed: break
    return c
PASSES={'peephole':lambda c:lower(peephole(c)),'fuse':fuse,'hczh':templ_hczh,'cxcomm':cnot_commute_cancel}
def optimize2(c,scorer,margin=1e-6,rounds=4,log=None):
    c=lower(c); best=scorer(c)
    for _ in range(rounds):
        improved=False
        for name,p in PASSES.items():
            cand=p(c)
            if len(cand)==len(c) and cand==c: continue
            f=scorer(cand)
            ok=f>best+margin
            if log is not None: log.append((name,len(c),len(cand),best,f,ok))
            if ok: c,best=cand,f; improved=True
        if not improved: break
    return c,best
