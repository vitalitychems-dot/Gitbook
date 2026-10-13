"""numpy-only stand-ins for sklearn (disk full on box; sklearn could not be installed).
RidgeClassifier: one-vs-rest closed-form ridge on +-1 targets (same math as sklearn RidgeClassifier).
KernelRBFClassifier: RBF kernel ridge one-vs-rest (SUBSTITUTE for sklearn SVC(kernel='precomputed'))."""
import numpy as np
class Scaler:
    def fit(s,X): s.m=X.mean(0); s.sd=X.std(0); s.sd[s.sd==0]=1; return s
    def transform(s,X): return (X-s.m)/s.sd
def _onehot(y,c): return np.where(y[:,None]==c[None,:],1.0,-1.0)
class Ridge:
    def __init__(s,alpha=1.0): s.a=alpha
    def fit(s,X,y):
        s.c=np.unique(y); s.mu=X.mean(0); Xc=X-s.mu; Y=_onehot(y,s.c); s.ym=Y.mean(0)
        n,d=Xc.shape
        if d<=n: s.W=np.linalg.solve(Xc.T@Xc+s.a*np.eye(d),Xc.T@(Y-s.ym))
        else: s.W=Xc.T@np.linalg.solve(Xc@Xc.T+s.a*np.eye(n),Y-s.ym)
        return s
    def decision(s,X): return (X-s.mu)@s.W+s.ym
    def predict(s,X): return s.c[np.argmax(s.decision(X),1)]
class RidgeReg:
    def __init__(s,alpha=1e-6): s.a=alpha
    def fit(s,X,y):
        s.mu=X.mean(0); s.ym=y.mean(); Xc=X-s.mu
        s.w=np.linalg.solve(Xc.T@Xc+s.a*np.eye(X.shape[1]),Xc.T@(y-s.ym)); return s
    def predict(s,X): return (X-s.mu)@s.w+s.ym
def rbf(A,B,g):
    d=(A**2).sum(1)[:,None]+(B**2).sum(1)[None,:]-2*A@B.T; return np.exp(-g*np.maximum(d,0))
class KernelRBF:
    def __init__(s,gamma=.05,alpha=1e-2): s.g=gamma; s.a=alpha
    def fit(s,X,y):
        s.c=np.unique(y); s.X=X; K=rbf(X,X,s.g)
        s.A=np.linalg.solve(K+s.a*np.eye(len(X)),_onehot(y,s.c)); return s
    def predict(s,X): return s.c[np.argmax(rbf(X,s.X,s.g)@s.A,1)]
def acc(y,p): return float((y==p).mean())
