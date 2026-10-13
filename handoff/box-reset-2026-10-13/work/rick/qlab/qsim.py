import numpy as np
s2=1/np.sqrt(2)
G={'H':np.array([[1,1],[1,-1]])*s2,'X':np.array([[0,1],[1,0]]),'Y':np.array([[0,-1j],[1j,0]]),
   'Z':np.diag([1,-1]),'S':np.diag([1,1j]),'T':np.diag([1,np.exp(1j*np.pi/4)]),
   'SDG':np.diag([1,-1j]),'TDG':np.diag([1,np.exp(-1j*np.pi/4)]),'I':np.eye(2)}
def mat(name,th=None):
    if name=='RX': c,s=np.cos(th/2),np.sin(th/2); return np.array([[c,-1j*s],[-1j*s,c]])
    if name=='RY': c,s=np.cos(th/2),np.sin(th/2); return np.array([[c,-s],[s,c]])
    if name=='RZ': return np.diag([np.exp(-1j*th/2),np.exp(1j*th/2)])
    if name=='P': return np.diag([1,np.exp(1j*th)])
    if name=='U3':
        t,p,l=th; return np.array([[np.cos(t/2),-np.exp(1j*l)*np.sin(t/2)],[np.exp(1j*p)*np.sin(t/2),np.exp(1j*(p+l))*np.cos(t/2)]])
    return G[name].astype(complex)
ONEQ={'U3','H','X','Y','Z','S','T','SDG','TDG','I','RX','RY','RZ','P'}
class SV:
    """statevector; qubit 0 = least significant bit"""
    def __init__(s,n,seed=0): s.n=n; s.v=np.zeros(2**n,complex); s.v[0]=1; s.rng=np.random.default_rng(seed)
    def _t(s): return s.v.reshape([2]*s.n)
    def ax(s,q): return s.n-1-q
    def u1(s,U,q):
        t=np.moveaxis(s._t(),s.ax(q),0); t=np.tensordot(U,t,1); s.v=np.moveaxis(t,0,s.ax(q)).reshape(-1)
    def cu(s,U,c,t):
        T=s._t(); idx=[slice(None)]*s.n; idx[s.ax(c)]=1; sub=T[tuple(idx)]
        a=s.ax(t)-(1 if s.ax(t)>s.ax(c) else 0)
        sub=np.moveaxis(np.tensordot(U,np.moveaxis(sub,a,0),1),0,a); T=T.copy(); T[tuple(idx)]=sub; s.v=T.reshape(-1)
    def apply(s,g):
        name,qs=g[0],g[1]; th=g[2] if len(g)>2 else None
        if name in ONEQ: s.u1(mat(name,th),qs[0])
        elif name=='CNOT': s.cu(G['X'],qs[0],qs[1])
        elif name=='CZ': s.cu(np.diag([1,-1]).astype(complex),qs[0],qs[1])
        elif name=='CP': s.cu(mat('P',th),qs[0],qs[1])
        elif name=='SWAP': T=s._t(); s.v=np.swapaxes(T,s.ax(qs[0]),s.ax(qs[1])).reshape(-1).copy()
        else: raise ValueError(name)
        return s
    def run(s,circ):
        for g in circ: s.apply(g)
        return s
    def probs(s): return np.abs(s.v)**2
    def sample(s,shots): p=s.probs(); return s.rng.choice(len(p),shots,p=p/p.sum())
def unitary(n,circ):
    cols=[]
    for k in range(2**n):
        s=SV(n); s.v[:]=0; s.v[k]=1; cols.append(s.run(circ).v)
    return np.array(cols).T
def qft(n):
    c=[]
    for j in reversed(range(n)):
        c.append(('H',[j]))
        for k in reversed(range(j)): c.append(('CP',[k,j],np.pi/2**(j-k)))
    for i in range(n//2): c.append(('SWAP',[i,n-1-i]))
    return c
def mcz(n):  # multi-controlled Z on all qubits via diagonal (as primitive op, used for Grover oracle)
    return ('MCZ',list(range(n)))
def depth(circ):
    lv={}; d=0
    for g in circ:
        l=max(lv.get(q,0) for q in g[1])+1
        for q in g[1]: lv[q]=l
        d=max(d,l)
    return d
