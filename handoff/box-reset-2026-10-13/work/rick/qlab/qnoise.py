import numpy as np
from qsim import unitary,mat,G
def gate_U(n,g): return unitary(n,[g])
def kron_on(n,K,q):
    ops=[np.eye(2)]*n; ops[n-1-q]=K; M=ops[0]
    for o in ops[1:]: M=np.kron(M,o)
    return M
def run_dm(n,circ,p_dep=0.0,gamma=0.0,mode='local'):
    d=2**n; rho=np.zeros((d,d),complex); rho[0,0]=1
    AD=[np.array([[1,0],[0,np.sqrt(1-gamma)]]),np.array([[0,np.sqrt(gamma)],[0,0]])]
    Pa=[G['X'],G['Y'],G['Z']]
    for g in circ:
        U=gate_U(n,g); rho=U@rho@U.conj().T
        if p_dep:
            if mode=='global': rho=(1-p_dep)*rho+p_dep*np.eye(d)/d
            else:
                for q in g[1]:
                    acc=(1-p_dep)*rho
                    for P in Pa: M=kron_on(n,P,q); acc=acc+p_dep/3*M@rho@M.conj().T
                    rho=acc
        if gamma:
            for q in g[1]:
                Ks=[kron_on(n,K,q) for K in AD]; rho=sum(K@rho@K.conj().T for K in Ks)
    return rho
def fid(psi,rho): return float(np.real(psi.conj()@rho@psi))
