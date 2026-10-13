import numpy as np
from qsim import qft
def aqft(n,m):
    """drop CP with angle < 2pi/2^m (CP(pi/2^d) has angle 2pi/2^(d+1))"""
    return [g for g in qft(n) if not (g[0]=='CP' and g[2] < 2*np.pi/2**m - 1e-15)]
def inverse(c): return [(g[0],g[1],-g[2]) if len(g)>2 else g for g in reversed(c)]
