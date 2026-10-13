"""Fast density-matrix noise sim (tensor form). p1/p2 depolarizing per qubit after 1q/2q gates, gamma amp-damping."""
import numpy as np
from qopt2 import gm
CX=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],complex).reshape(2,2,2,2)
CZ=np.diag([1,1,1,-1]).astype(complex).reshape(2,2,2,2)
def _ap1(T,U,ax): T=np.tensordot(U,T,axes=([1],[ax])); return np.moveaxis(T,0,ax)
def _ap2(T,U,a,b): T=np.tensordot(U,T,axes=([2,3],[a,b])); return np.moveaxis(T,[0,1],[a,b])
def run(n,c,p1=1e-3,p2=1e-2,gamma=1e-3,init=0):
    T=np.zeros((2**n,2**n),complex); T[init,init]=1; T=T.reshape([2]*(2*n))
    r=lambda q:n-1-q; k=lambda q:2*n-1-q   # row axis, col axis
    A0=np.array([[1,0],[0,np.sqrt(1-gamma)]]); A1=np.array([[0,np.sqrt(gamma)],[0,0]])
    for g in c:
        qs=g[1]
        if len(qs)==1:
            U=gm(g); T=_ap1(_ap1(T,U,r(qs[0])),U.conj(),k(qs[0])); p=p1
        else:
            U=CX if g[0]=='CNOT' else CZ; a,b=qs
            T=_ap2(_ap2(T,U,r(a),r(b)),U.conj(),k(a),k(b)); p=p2
        for q in qs:
            if p:  # depolarize: (1-4p/3)rho + 4p/3 * Tr_q(rho)⊗I/2
                tr=np.take(np.take(T,0,r(q)),0,k(q)-1)+np.take(np.take(T,1,r(q)),1,k(q)-1)
                mix=np.expand_dims(np.expand_dims(tr,r(q)),k(q)); I=np.zeros_like(T)
                e=[slice(None)]*(2*n)
                for s in (0,1):
                    e[r(q)]=slice(s,s+1); e[k(q)]=slice(s,s+1); I[tuple(e)]=mix/2
                T=(1-4*p/3)*T+4*p/3*I
            if gamma:
                T=_ap1(_ap1(T,A0,r(q)),A0,k(q))+_ap1(_ap1(T,A1,r(q)),A1,k(q))
    return T.reshape(2**n,2**n)
def fidelity(n,c,psi,**kw): return float(np.real(psi.conj()@run(n,c,**kw)@psi))
