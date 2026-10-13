"""Diverse top-k as a QUBO solved by simulated annealing (the classical analogue of quantum annealing).
Target: hybrid-retrieval.ts hybridRetrieve returns the top 5 by score; memory holds near-duplicates, so
the 5 slots can be spent on copies of one fact. Candidate: from the top 20 pick k=5 minimising
E(x) = -sum rel_i x_i + lam * sum_{i<j} sim_ij x_i x_j + P (sum x - k)^2 by Metropolis annealing.
Data: real TESSERA docs paragraphs; each query mixes key terms from 3 paragraphs (3 subtopics);
0-4 near-duplicates (15% token dropout) of each paragraph are planted. Relevance = BM25 (same formula).
Metric: subtopics covered in the 5 results (0..3, higher better). Also reported: greedy MMR."""
import sys; sys.path.insert(0, "..")
from common import *
K, POOL, LAM = 5, 20, 0.6
def corpus(r):
    P = paragraphs(); docs, src = [], []
    for i, p in enumerate(P):
        t = tok3(p); docs.append(t); src.append(i)
        for _ in range(r.integers(0, 5)):
            docs.append([w for w in t if r.random() > .15]); src.append(i)
    return docs, np.array(src)
def jacc(a, b):
    A, B = set(a), set(b); return len(A & B) / max(1, len(A | B))
def anneal(rel, S, k, r, steps=3000):
    n = len(rel); x = np.zeros(n, int); x[:k] = 1; Pn = 2.0
    E = lambda x: -rel @ x + LAM * (x @ S @ x) / 2 + Pn * (x.sum() - k) ** 2
    e = E(x); best, be = x.copy(), e
    for s in range(steps):
        T = 1.0 * (0.002 / 1.0) ** (s / steps)
        i, j = r.choice(np.flatnonzero(x)), r.choice(np.flatnonzero(1 - x))   # swap move keeps sum=k
        y = x.copy(); y[i], y[j] = 0, 1; ey = E(y)
        if ey < e or r.random() < np.exp((e - ey) / T): x, e = y, ey
        if e < be: best, be = x.copy(), e
    return np.flatnonzero(best)
def mmr(rel, S, k):
    sel = [int(np.argmax(rel))]
    while len(sel) < k:
        sc = [rel[i] - LAM * max(S[i, j] for j in sel) if i not in sel else -1e9 for i in range(len(rel))]
        sel.append(int(np.argmax(sc)))
    return sel
def run(method):
    def f(seed):
        r = vtk.rng(seed); docs, src = corpus(r); P = paragraphs(); cov = []
        for _ in range(25):
            topics = r.choice(len(P), 3, replace=False)
            q = " ".join(w for t in topics for w in r.choice(tok3(P[t]), 4, replace=False))
            s = bm25(q, docs); pool = np.argsort(-s)[:POOL]
            if method == "top": pick = pool[:K]
            else:
                rel = s[pool] / max(s[pool].max(), 1e-9)
                S = np.array([[jacc(docs[a], docs[b]) if a != b else 0 for b in pool] for a in pool])
                pick = pool[anneal(rel, S, K, r) if method == "qubo" else mmr(rel, S, K)]
            cov.append(len(set(src[pick]) & set(topics)))
        return float(np.mean(cov))
    return f
if __name__ == "__main__":
    report([vtk.bench("05 QUBO-anneal diverse top-5 vs current top-5", run("top"), run("qubo"), 12, True, "subtopics covered /3"),
            vtk.bench("05 QUBO-anneal vs greedy MMR (non-quantum control)", run("mmr"), run("qubo"), 12, True, "subtopics covered /3")], "results.json")
