import numpy as np
def rref(M):
    M = M.copy() % 2; r = 0; piv = []
    for c in range(M.shape[1]):
        p = [i for i in range(r, M.shape[0]) if M[i, c]]
        if not p: continue
        M[[r, p[0]]] = M[[p[0], r]]
        for i in range(M.shape[0]):
            if i != r and M[i, c]: M[i] ^= M[r]
        piv.append(c); r += 1
        if r == M.shape[0]: break
    return M[:r], piv
def rank(M): return rref(M)[0].shape[0]
def nullspace(M):
    R, piv = rref(M); n = M.shape[1]; free = [c for c in range(n) if c not in piv]; out = []
    for f in free:
        v = np.zeros(n, np.uint8); v[f] = 1
        for i, c in enumerate(piv): v[c] = R[i, f]
        out.append(v)
    return np.array(out, np.uint8)
