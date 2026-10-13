"""Budget fitting as max-coverage (QUBO-style) line selection solved by annealing.
Target: v2/src/opt/token-lab.mjs fitBudget: over budget -> keep first 60% + last 40% of characters,
cut the middle. Query-free, like the current function.
Candidate (also query-free): choose whole lines to maximise the number of distinct content words
covered under the same token budget (countTokens = ceil(chars/4)), solved by simulated annealing
(add/remove moves, penalty for exceeding budget); output keeps original line order.
Control: greedy (best new-words-per-token first).
Data: whole TESSERA docs/*.md files of 2k-40k tokens; budget = 25% of the file.
Metric: fraction of the file's paragraphs (random 'needle' facts) with >=50% of their distinct
words still present in the output (higher better)."""
import sys, re, subprocess; sys.path.insert(0, "..")
from common import *
ct = lambda s: max(1, -(-len(s) // 4))
def files():
    fs = subprocess.run(["git", "-C", REPO, "ls-files", "docs"], capture_output=True, text=True).stdout.split(); out = []
    for f in sorted(fs):
        if f.endswith(".md"):
            t = open(f"{REPO}/{f}", errors="ignore").read()
            if 2000 <= ct(t) <= 40000: out.append(t)
    return out
F = files()
def fit_budget(s, budget):
    if ct(s) <= budget: return s
    m = "\n…\n"; ch = max(0, budget * 4 - len(m)); h = -(-ch * 6 // 10); return s[:h] + m + s[len(s) - (ch - h):]
def W(line): return set(w for w in tok3(line))
def greedy(lines, budget):
    cov = set(); sel = set(); used = 0; cand = list(range(len(lines)))
    while True:
        best, bv = None, 0
        for i in cand:
            if i in sel or used + ct(lines[i]) + 1 > budget: continue
            v = len(W(lines[i]) - cov) / (ct(lines[i]) + 1)
            if v > bv: best, bv = i, v
        if best is None: return sel
        sel.add(best); cov |= W(lines[best]); used += ct(lines[best]) + 1
def anneal(lines, budget, r, steps=6000):
    ws = [W(l) for l in lines]; cost = np.array([ct(l) + 1 for l in lines]); from collections import Counter
    sel = set(greedy(lines, budget)); cnt = Counter(w for i in sel for w in ws[i]); used = cost[list(sel)].sum() if sel else 0
    pen = 2.0; E = lambda cov, u: -cov + pen * max(0, u - budget)
    e = E(len(cnt), used); best, be = set(sel), e
    for s in range(steps):
        T = 3.0 * (0.01 / 3.0) ** (s / steps); i = int(r.integers(len(lines)))
        if i in sel:
            lost = sum(1 for w in ws[i] if cnt[w] == 1); ne = E(len(cnt) - lost, used - cost[i])
        else:
            gain = sum(1 for w in ws[i] if cnt[w] == 0); ne = E(len(cnt) + gain, used + cost[i])
        if ne <= e or r.random() < np.exp((e - ne) / T):
            if i in sel:
                sel.remove(i); used -= cost[i]
                for w in ws[i]:
                    cnt[w] -= 1
                    if cnt[w] == 0: del cnt[w]
            else:
                sel.add(i); used += cost[i]
                for w in ws[i]: cnt[w] += 1
            e = ne
            if e < be and used <= budget: best, be = set(sel), e
    return best
def needle_score(text, out):
    ow = set(tok3(out)); P = [p for p in re.split(r"\n\s*\n", text) if len(set(tok3(p))) >= 8]
    return np.mean([len(set(tok3(p)) & ow) / len(set(tok3(p))) >= .5 for p in P])
def run(method):
    def f(seed):
        r = vtk.rng(seed); sc = []
        for i in r.choice(len(F), min(6, len(F)), replace=False):
            t = F[i]; b = ct(t) // 4; lines = t.split("\n")
            if method == "base": out = fit_budget(t, b)
            else:
                sel = greedy(lines, b) if method == "greedy" else anneal(lines, b, r)
                out = "\n".join(lines[j] for j in sorted(sel)); assert ct(out) <= b + 1
            sc.append(needle_score(t, out))
        return float(np.mean(sc))
    return f
if __name__ == "__main__":
    print("files:", len(F))
    report([vtk.bench("09 anneal max-coverage vs fitBudget head/tail", run("base"), run("anneal"), 10, True, "needle paragraphs kept"),
            vtk.bench("09 anneal vs greedy coverage (non-quantum control)", run("greedy"), run("anneal"), 10, True, "needle paragraphs kept")], "results.json")
