"""Low-rank (truncated SVD = one-bond tensor-network / Schmidt decomposition) + int8 storage for vectors.
Target: vector-memory.ts searchMemory: loads up to 1000 rows of 256-d embeddings stored as JSON number
arrays and scores all of them. Candidate: project onto the top-r right singular vectors of the stored
matrix (Schmidt truncation), store int8 codes + one scale per row. Embeddings = live fallback embedder
(build 04 fixed version) over real TESSERA docs paragraphs, split 70% fit / 30% held-out rows.
Metrics: bytes per stored vector (lower better) and recall@10 of the exact-cosine neighbours for
held-out queries (must stay >= 0.95 to keep)."""
import sys, json; sys.path.insert(0, "..")
sys.path.insert(0, "../04_signed_hash_embed")
from common import *
import importlib; e4 = importlib.import_module("run")
E = e4.EMB[True]; R = 64
def split(seed):
    r = vtk.rng(seed); o = r.permutation(len(E)); n = int(.7 * len(E)); return E[o[:n]], E[o[n:]]
def json_bytes(seed):
    fit, _ = split(seed); return float(np.mean([len(json.dumps(list(map(float, v)))) for v in fit]))
def lr_bytes(seed): return float(R * 1 + 4)  # int8 codes + float32 scale; basis (R*256*4 B) amortised below
def recall(seed):
    fit, held = split(seed); U, s, Vt = np.linalg.svd(fit, full_matrices=False); B = Vt[:R]
    Z = fit @ B.T; sc = np.abs(Z).max(1, keepdims=True) / 127; Q = np.round(Z / sc).astype(np.int8)
    Zh = Q * sc; hits = []
    for q in held:
        ex = np.argsort(-(fit @ q))[:10]; ap = np.argsort(-(Zh @ (B @ q)))[:10]
        hits.append(len(set(ex) & set(ap)) / 10)
    return float(np.mean(hits))
if __name__ == "__main__":
    res = [vtk.bench(f"08 rank-{R} int8 store vs JSON float", json_bytes, lr_bytes, 10, False, "bytes/vector (excl. basis)")]
    m, lo, hi = vtk.bootstrap_ci([recall(s) for s in vtk.seeds(10)])
    res.append({"name": "08 recall@10 of compressed search", "metric": "recall@10", "n_seeds": 10, "higher_is_better": True,
                "baseline": {"mean": 1.0, "lo": 1.0, "hi": 1.0}, "candidate": {"mean": m, "lo": lo, "hi": hi},
                "improvement": {"mean": m - 1, "lo": lo - 1, "hi": hi - 1}, "verdict": "KEEP" if lo >= .95 else "DROP (recall < 0.95)"})
    print("basis overhead bytes:", R * 256 * 4, " rows in store:", int(.7 * len(E)))
    report(res, "results.json")
