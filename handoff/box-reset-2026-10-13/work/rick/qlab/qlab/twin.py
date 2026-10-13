"""Calibrated noise twin: density-matrix sim with per-qubit thermal relaxation (T1/T2, incl. idle time per ASAP layer),
depolarizing sized to the residual calibrated gate error, and readout confusion. Units: T1/T2 us, lengths ns.
Cost model (IBM-like natives sx, x, rz, cx): P/RZ/Z/S/T and daggers are virtual (0 error, 0 ns); H/X/SX = 1 pulse; U3/RX/RY/Y = 2 pulses."""
import numpy as np
from qnoise2 import _ap1,_ap2,CX,CZ
from qopt2 import gm
VIRT={'P','RZ','Z','S','SDG','T','TDG','I'}; ONEP={'H','X'}
PA=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def kraus1(T,Ks,ax,axc):
    return sum(_ap1(_ap1(T,K,ax),K.conj(),axc) for K in Ks)
def relax_kraus(t_ns,T1,T2):
    if t_ns<=0: return None
    t=t_ns/1000.0; g=1-np.exp(-t/T1); c=np.exp(-t/T2)/np.sqrt(1-g); lam=max(0.0,1-min(1.0,c)**2)
    AD=[np.array([[1,0],[0,np.sqrt(1-g)]]),np.array([[0,np.sqrt(g)],[0,0]])]
    PD=[np.array([[1,0],[0,np.sqrt(1-lam)]]),np.array([[0,0],[0,np.sqrt(lam)]])]
    return [b@a for a in AD for b in PD]
def r_thermal(t_ns,T1,T2):  # 1q average infidelity of thermal relaxation
    t=t_ns/1000.0; return 1-(3+np.exp(-t/T1)+2*np.exp(-t/T2))/6
def gate_cost(dev,phys,g):
    """(duration ns, per-qubit Pauli depolarizing prob list)"""
    nm=g[0]; Q=dev['qubits']
    if g[0]=='DELAY': return g[2],[0.0]
    if len(g[1])==1:
        q=Q[phys[g[1][0]]]
        if nm in VIRT: return 0.0,[0.0]
        k=1 if nm in ONEP else 2; t=k*q['t1q']; e=k*(q['ex'] if nm=='X' and q.get('ex') else q['e1q'])
        res=max(0.0,e-r_thermal(t,q['T1'],q['T2'])); return t,[1.5*res]
    a,b=phys[g[1][0]],phys[g[1][1]]; e,t=dev['edges'][frozenset((a,b))]
    rt=r_thermal(t,Q[a]['T1'],Q[a]['T2'])+r_thermal(t,Q[b]['T1'],Q[b]['T2'])
    res=max(0.0,e-rt); return t,[res/1.6,res/1.6]
def layers(c):
    lv={}; L=[]
    for g in c:
        l=max(lv.get(q,0) for q in g[1]); 
        for q in g[1]: lv[q]=l+1
        while len(L)<=l: L.append([])
        L[l].append(g)
    return L
def run(dev,phys,c,n,idle=True,init=0):
    """phys[i]=device qubit for circuit position i. c must be in native basis (1q, CNOT/CZ on coupled pairs)."""
    T=np.zeros((2**n,2**n),complex); T[init,init]=1; T=T.reshape([2]*(2*n))
    r=lambda q:n-1-q; k=lambda q:2*n-1-q; Q=dev['qubits']
    for lay in layers(c):
        busy={}; dur=0
        for g in lay:
            t,ps=gate_cost(dev,phys,g); dur=max(dur,t)
            qs=g[1]
            if g[0]!='DELAY':
                if len(qs)==1: U=gm(g); T=_ap1(_ap1(T,U,r(qs[0])),U.conj(),k(qs[0]))
                else:
                    U=CX if g[0]=='CNOT' else CZ; a,b=qs; T=_ap2(_ap2(T,U,r(a),r(b)),U.conj(),k(a),k(b))
            for q,p in zip(qs,ps):
                if p>0: T=kraus1(T,[np.sqrt(1-p)*np.eye(2)]+[np.sqrt(p/3)*P for P in PA],r(q),k(q))
            for q in qs: busy[q]=t
        for q in range(n):
            tq=dur if idle else busy.get(q,0.0)
            K=relax_kraus(tq,Q[phys[q]]['T1'],Q[phys[q]]['T2'])
            if K: T=kraus1(T,K,r(q),k(q))
    return T.reshape(2**n,2**n)
def readout(dev,phys,probs,n):
    p=probs.reshape([2]*n)
    for q in range(n):
        d=dev['qubits'][phys[q]]; M=np.array([[1-d['readout_p01'],d['readout_p10']],[d['readout_p01'],1-d['readout_p10']]])
        p=np.moveaxis(np.tensordot(M,np.moveaxis(p,n-1-q,0),1),0,n-1-q)
    return p.reshape(-1)
def esp(dev,phys,c):
    """estimated success probability: prod(1-e_gate) * prod exp(-t_total/T1) (cheap layout ranking)"""
    s=1.0; Q=dev['qubits']; tot=0
    for lay in layers(c):
        d=0
        for g in lay:
            t,ps=gate_cost(dev,phys,g); d=max(d,t)
            if g[0] in VIRT: continue
            if len(g[1])==1 and g[0]!='DELAY': s*=1-(2 if g[0] not in ONEP else 1)*Q[phys[g[1][0]]]['e1q']
            elif len(g[1])==2: s*=1-dev['edges'][frozenset((phys[g[1][0]],phys[g[1][1]]))][0]
        tot+=d
    for p in set(phys): s*=np.exp(-tot/1000/Q[p]['T1'])
    return s
