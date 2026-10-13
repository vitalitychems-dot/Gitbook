"""Invention 4: QEC-style 3-answerer redundancy + majority vote (repetition code). Answerers (copied from c2 brain2):
 A = c2 numeric+semantic verifier over BM25 top-10 (the 0.772 baseline)
 B = same verifier over leak-fixed MWPM-deduped retrieval (inv3) -> different 'physical qubit' (different evidence)
 C = verifier over BM25 top-30 with query-term dropout (seeded) -> independent noise
Decode: majority; tie -> A. Syndrome mode: answer only when >=2 agree (precision)."""
import re, json, math, difflib, collections, random, functools, common as c
NUM = r"\b\d+(?:\.\d+)?%?"
SENT = lambda s: [x.strip(" -*|#")[:300] for x in re.split(r"(?<=[.!?])\s+|\n", s)]
def tri(s): s = " " + re.sub(r"\s+", " ", s.lower()) + " "; return collections.Counter(s[i:i+3] for i in range(len(s)-2))
def cos(a, b): return sum(a[k]*b[k] for k in a if k in b) / (math.sqrt(sum(v*v for v in a.values())*sum(v*v for v in b.values())) or 1)
def verify(q, sent, num):
    m = sent.replace(num, "___", 1)
    if abs(len(m)-len(q)) > 0.6*len(q): return 0.0
    seq = difflib.SequenceMatcher(None, q, m, autojunk=False).ratio(); sem = cos(tri(q), tri(m))
    i, j = q.find("___"), m.find("___"); ctx = q[max(0,i-12):i] == m[max(0,j-12):j] if i >= 0 and j >= 0 else False
    return 0.5*seq + 0.4*sem + 0.1*ctx
@functools.lru_cache(maxsize=None)
def ans_rows(q, rows):
    best = None
    for p, body in rows:
        for s in SENT(body):
            for n in set(re.findall(NUM, s)):
                sc = verify(q, s, n)
                if best is None or sc > best[0]: best = (sc, n)
    return best
def A(q): return ans_rows(q, tuple((r[1], r[2]) for r in c.retrieve(q, 10)))
_inv3 = None
def B(q):
    import inv3_eval as e
    fs = e.rank(q, 3); rows = [r for r in e.clean(c.retrieve(q, 40)) if r[1] in fs][:10]
    return ans_rows(q, tuple((r[1], r[2]) for r in rows))
def Cq(q):
    rr = random.Random(hash(q) & 0xffff); q2 = " ".join(w for w in q.split() if "___" in w or rr.random() > .2)
    return ans_rows(q, tuple((r[1], r[2]) for r in c.retrieve(q2, 30)))
if __name__ == "__main__":
    xs = c.TEST; V = {x["q"]: [(f(x["q"]) or (0, None))[1] for f in (A, B, Cq)] for x in xs}
    ind = {n: round(sum(V[x["q"]][i] == x["a"] for x in xs)/len(xs), 3) for i, n in enumerate("ABC")}
    def maj(v): m = collections.Counter(a for a in v if a).most_common(1); return m[0][0] if m and m[0][1] >= 2 else v[0]
    accm = round(sum(maj(V[x["q"]]) == x["a"] for x in xs)/len(xs), 3)
    agreed = [x for x in xs if collections.Counter(a for a in V[x["q"]] if a).most_common(1) and collections.Counter(a for a in V[x["q"]] if a).most_common(1)[0][1] >= 2]
    prec = round(sum(maj(V[x["q"]]) == x["a"] for x in agreed)/max(1, len(agreed)), 3)
    corr = sum((V[x["q"]][0] == x["a"]) == (V[x["q"]][1] == x["a"]) for x in xs)/len(xs)
    R = dict(individual_acc=ind, majority_acc=accm, syndrome_answered=len(agreed), syndrome_precision=prec,
             baseline=dict(acc=0.772, precision=0.779), A_B_outcome_agreement=round(corr, 3))
    print(json.dumps(R, indent=1)); json.dump(R, open("results/inv4.json", "w"), indent=1)
