"""Erasure coding (classical cousin of a stabilizer code: checksums = syndromes that LOCATE the bad
file, parity = redundancy that REPAIRS it) for critical-file snapshots.
Target: file-integrity.ts + auto-recovery.ts snapshotFile: a full copy of each of the 20 CRITICAL_FILES.
Candidate: XOR parity over groups of k=4 files (sha256 already locates which file is bad = erasure).
Real sizes: the 20 files at the checked-out TESSERA commit. Metrics: snapshot bytes (lower better) and
P(every damaged file restorable) when each file is independently damaged with prob q per check
(q in {0.01, 0.05}), plus a correlated event (whole lib/ directory lost)."""
import sys, os, re; sys.path.insert(0, "..")
from common import *
src = open(f"{REPO}/artifacts/api-server/src/lib/file-integrity.ts").read()
CRIT = re.findall(r'"([^"]+\.ts)"', src[src.index("CRITICAL_FILES"):src.index("];", src.index("CRITICAL_FILES"))])
SZ = np.array([os.path.getsize(f"{REPO}/{f}") if os.path.exists(f"{REPO}/{f}") else 0 for f in CRIT])
K = 4; G = np.arange(len(CRIT)) // K
def parity_bytes(): return int(sum(SZ[G == g].max() for g in np.unique(G)))
def p_ok(q, method, seed, trials=20000):
    r = vtk.rng(seed); L = r.random((trials, len(CRIT))) < q
    if method == "full": return 1.0
    ok = np.ones(trials, bool)
    for g in np.unique(G): ok &= L[:, G == g].sum(1) <= 1
    return float(ok.mean())
if __name__ == "__main__":
    print(len(CRIT), "critical files, present:", int((SZ > 0).sum()), " full-copy bytes:", int(SZ.sum()), " parity bytes:", parity_bytes())
    R = [vtk.bench("10 parity k=4 vs full snapshots", lambda s: float(SZ.sum()), lambda s: float(parity_bytes()), 5, False, "snapshot bytes")]
    for q in (0.01, 0.05):
        R.append(vtk.bench(f"10 restorable at q={q}", lambda s, q=q: p_ok(q, "full", s), lambda s, q=q: p_ok(q, "par", s), 10, True, "P(all restorable)"))
    lib = np.array(["/src/lib/" in f for f in CRIT]); grp_hit = [int(lib[G == g].sum()) for g in np.unique(G)]
    print("correlated event, lib/ dir lost: files lost per parity group =", grp_hit, "-> parity restores all:", all(x <= 1 for x in grp_hit), "; full copies restore all: True")
    report(R, "results.json")
