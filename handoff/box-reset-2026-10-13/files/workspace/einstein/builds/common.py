import sys, re, subprocess, json, numpy as np
sys.path.insert(0, "/workspace/einstein/toolkit")
import vtk
REPO = "/workspace/TESSERA-ro"
def repo_commit():
    return subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
_par = None
def paragraphs(min_tokens=25):
    """Real TESSERA text: paragraphs of docs/*.md at the checked-out commit."""
    global _par
    if _par is None:
        files = subprocess.run(["git", "-C", REPO, "ls-files", "docs"], capture_output=True, text=True).stdout.split()
        out = []
        for f in sorted(files):
            if not f.endswith(".md"): continue
            t = open(f"{REPO}/{f}", errors="ignore").read()
            for p in re.split(r"\n\s*\n", t):
                p = p.strip()
                if len(tok(p)) >= min_tokens and not p.startswith("|"): out.append(p)
        seen = set(); _par = [p for p in out if not (p in seen or seen.add(p))]
    return _par
def tok(t):  # same rule as vector-memory.ts tokenize
    return [w for w in re.sub(r"[^a-z0-9\s]", " ", t.lower()).split() if w]
def tok3(t):  # hybrid-retrieval.ts tokenize (len>2)
    return [w for w in tok(t) if len(w) > 2]
def bm25(query, docs_tok, k1=1.5, b=0.75):
    q = list(dict.fromkeys(tok3(query))); N = len(docs_tok)
    lens = np.array([len(d) for d in docs_tok], float); avg = lens.mean() or 1
    sets = [set(d) for d in docs_tok]; s = np.zeros(N)
    from collections import Counter
    cnts = [Counter(d) for d in docs_tok]
    for t in q:
        df = sum(t in S for S in sets); idf = np.log(1 + (N - df + .5) / (df + .5))
        for i in range(N):
            f = cnts[i].get(t, 0)
            if f: s[i] += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * lens[i] / avg))
    return s
def report(results, path):
    vtk.save({"tessera_commit": repo_commit(), "results": results}, path)
    for r in results: print(vtk.fmt(r))
