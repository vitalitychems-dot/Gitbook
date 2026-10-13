"""Independent random-sign projection (JL sketch) for the live fallback embedder.
Target: neural-embeddings.ts localFallbackEmbedding (used whenever TESSERA_EMBED_MODEL is unset).
Its bit for dimension i is ((h1>>>(i%32)) ^ (h2>>>((i*7)%32))) & 1, which depends only on i mod 32:
the 256-d vector is 8 copies of a 32-d sketch. Candidate: identical bag, weights, tanh and norm, but each of
the 256 dims gets its own sign bit (8 FNV-1a hashes with different seeds -> 256 bits).
Data: real TESSERA docs paragraphs. Metrics: mean |sketch cos - exact weighted-bag cos| on random pairs
(lower better) and top-1 retrieval of 8-word snippets (higher better)."""
import sys, re; sys.path.insert(0, "..")
from common import *
from collections import Counter
STOP = set("the a an and or but if then of to in on at by for with as is are was were be been being have has had do does did this that these those it its from so not no yes i you he she we they them us our your their my me".split())
DIM = 256; I = np.arange(DIM)
def fnv(s, seed=2166136261):
    h = seed & 0xFFFFFFFF
    for ch in s: h ^= ord(ch); h = (h * 16777619) & 0xFFFFFFFF
    return h
def toks(t): return [w for w in re.sub(r"[^a-z0-9\s]", " ", t.lower()).split() if len(w) >= 2 and w not in STOP]
def bag(text):
    t = toks(text); b = Counter()
    for w in t: b[w] += 1
    for g in zip(t, t[1:]): b[" ".join(g)] += .6
    for g in zip(t, t[1:], t[2:]): b[" ".join(g)] += .35
    return b
_bits = {}
def bits(term, fixed):
    k = (term, fixed)
    if k not in _bits:
        if not fixed:
            h1, h2 = fnv(term), fnv(term, 40503)
            _bits[k] = ((h1 >> (I % 32)) ^ (h2 >> ((I * 7) % 32))) & 1
        else:
            hs = np.array([fnv(term, 2166136261 + 7919 * j) for j in range(DIM // 32)], dtype=np.uint64)
            _bits[k] = ((hs[I // 32] >> (I % 32).astype(np.uint64)) & 1).astype(int)
    return _bits[k]
def embed(text, fixed):
    b = bag(text)
    if not b: return np.zeros(DIM)
    s = np.zeros(DIM); tw = 0
    for term, w in b.items(): tw += w; s += np.where(bits(term, fixed), w, -w)
    v = np.tanh(s / (tw / DIM * 4 + 1)); n = np.linalg.norm(v); return v / n if n else v
def exact(a, b):
    A, B = bag(a), bag(b); num = sum(A[k] * B[k] for k in A)
    d = np.sqrt(sum(x * x for x in A.values()) * sum(x * x for x in B.values())); return num / d if d else 0
P = paragraphs(); EMB = {f: np.array([embed(p, f) for p in P]) for f in (False, True)}
def pair_err(fixed):
    def f(seed):
        r = vtk.rng(seed); E = [abs(EMB[fixed][i] @ EMB[fixed][j] - exact(P[i], P[j])) for i, j in r.integers(0, len(P), (300, 2)) if i != j]
        return float(np.mean(E))
    return f
def hit(fixed):
    def f(seed):
        r = vtk.rng(seed); ok = 0
        for i in r.integers(0, len(P), 200):
            t = tok(P[i]); st = r.integers(0, len(t) - 8); q = " ".join(t[st:st + 8])
            ok += int(np.argmax(EMB[fixed] @ embed(q, fixed)) == i)
        return ok / 200
    return f
if __name__ == "__main__":
    v = EMB[False][0]; print("baseline period-32 check: max|v[i]-v[i+32]| =", float(np.abs(v[:-32] - v[32:]).max()))
    report([vtk.bench("04 fallback embed: cosine error vs exact bag", pair_err(False), pair_err(True), 20, False, "mean |cos err|"),
            vtk.bench("04 fallback embed: top-1 snippet retrieval", hit(False), hit(True), 20, True, "top-1 hit rate")], "results.json")
