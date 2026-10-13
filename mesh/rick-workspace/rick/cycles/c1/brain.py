"""Cycle-1 SMARTER/FASTER/RECALL prototypes over the palace. python3 brain.py -> brain_results.json
QA set: auto-built cloze questions from /workspace/rick/**/*.md (a number masked in a sentence); dev/test split by file hash (held-out)."""
import sys, re, os, json, time, random, hashlib, collections, sqlite3
sys.path.insert(0, "/workspace/rick/tools/palace"); import palace
random.seed(7); tok = palace.tok; T = lambda s: max(1, len(s) // 4)
NUM = r"\b\d+(?:\.\d+)?%?"
def build_qa(roots=("/workspace/rick", "/workspace/TESSERA-ro"), n=400):
    qa = []
    for d, ds, fs in (w for root in roots for w in os.walk(root)):
        ds[:] = [z for z in ds if z not in palace.SKIP and not z.startswith(".")]
        if "cycles" in d or "__pycache__" in d: continue
        for f in sorted(fs):
            if not f.endswith(".md"): continue
            p = os.path.join(d, f)
            for s in re.split(r"(?<=[.!?])\s+|\n", open(p, errors="replace").read()):
                s = s.strip(" -*|#"); nums = re.findall(NUM, s)
                if 40 < len(s) < 220 and 1 <= len(nums) <= 2 and len(tok(s)) >= 6 and len(nums[0]) >= 2:
                    qa.append(dict(q=s.replace(nums[-1], "___", 1), a=nums[-1], file=p))
                    if s.count(nums[-1]) > 1: qa.pop()
    qa.sort(key=lambda x: (x["file"], x["q"])); random.shuffle(qa); qa = qa[:n]
    for x in qa: x["split"] = "test" if int(hashlib.md5(x["file"].encode()).hexdigest(), 16) % 3 == 0 else "dev"
    return qa
C = sqlite3.connect(palace.DB)
def retrieve(q, k=5):
    m = " OR ".join(f'"{t}"' for t in tok(q))
    return C.execute("select path,l0,l1,chunks.body,bm25(f) from f join chunks on chunks.id=f.rowid where f match ? order by bm25(f) limit ?", (m, k)).fetchall() if m else []
def cands(q, chunk):
    out = []; qt = set(tok(q))
    for s in re.split(r"(?<=[.!?])\s+|\n", chunk):
        st = set(tok(s)); ov = len(qt & st) / max(1, len(qt))
        for n in re.findall(NUM, s): out.append((ov, n, s))
    return out
def answer(q, k=5, boost=None):
    best = None
    for rank, (p, l0, l1, body, sc) in enumerate(retrieve(q, k)):
        w = 1 / (1 + rank) * (1.5 if boost and p in boost else 1)
        for ov, n, s in cands(q, body):
            if best is None or ov * w > best[0]: best = (ov * w, n, p, l0, s, body)
    return best
def s1(x, k=5):
    b = answer(x["q"], k); return b and b[1]
def cited_ok(x, b): return b is not None and b[1] in b[5] and len(set(tok(x["q"])) & set(tok(b[4]))) >= 0.5 * len(set(tok(x["q"])))
def s2(x):
    v = collections.Counter(); t = tok(x["q"])
    for i in range(5):
        r = random.Random(i); q = " ".join(w for w in t if i == 0 or r.random() > .2); b = answer(q)
        if b: v[b[1]] += 1
    return v.most_common(1)[0][0] if v else None
def s3(x):
    for k in (5, 15, 30):
        b = answer(x["q"], k)
        if cited_ok(x, b): return b[1]
    return None
def s4_lib(dev):
    lib = []
    for x in dev:
        b = answer(x["q"])
        if not b or b[1] != x["a"]: lib.append((set(tok(x["q"])), x["file"]))
    return lib
def s4(x, lib):
    qt = set(tok(x["q"])); boost = {f for t, f in lib if len(t & qt) >= 3}; b = answer(x["q"], 10, boost); return b and b[1]
def acc(xs, fn): return round(sum(fn(x) == x["a"] for x in xs) / len(xs), 3)
qa = build_qa(); dev = [x for x in qa if x["split"] == "dev"]; test = [x for x in qa if x["split"] == "test"]
R = {"qa": dict(total=len(qa), dev=len(dev), test=len(test))}
R["baseline_top1_k1"] = acc(test, lambda x: s1(x, 1))
R["S1_rag_k5"] = acc(test, s1)
b_ok = [(x, answer(x["q"])) for x in test]; ac = [x for x, b in b_ok if cited_ok(x, b)]
R["S1_citation_check"] = dict(accepted=len(ac), precision_accepted=round(sum(b[1] == x["a"] for x, b in b_ok if cited_ok(x, b)) / max(1, len(ac)), 3), precision_all=R["S1_rag_k5"])
R["S2_self_consistency"] = acc(test, s2)
ans3 = [(x, s3(x)) for x in test]; R["S3_verifier"] = dict(answered=sum(a is not None for _, a in ans3), acc_all=round(sum(a == x["a"] for x, a in ans3) / len(test), 3), precision=round(sum(a == x["a"] for x, a in ans3 if a) / max(1, sum(a is not None for _, a in ans3)), 3))
lib = s4_lib(dev); R["S4_mistake_library"] = dict(lib_size=len(lib), acc=acc(test, lambda x: s4(x, lib)))
lvl = lambda x: "easy" if len(tok(x["q"])) >= 14 else "medium" if len(tok(x["q"])) >= 9 else "hard"
R["S5_curriculum"] = {L: dict(n=len(g), acc=acc(g, s1)) for L in ("easy", "medium", "hard") for g in [[x for x in test if lvl(x) == L]] if g}
ctx = lambda q, k=5: [r[3] for r in retrieve(q, k)]
def compress(q, chunks):
    qt = set(tok(q)); return ["\n".join(l for l in c.splitlines() if qt & set(tok(l))) for c in chunks]
def has_ans(x, chunks): return any(x["a"] in c for c in chunks)
raw = [(x, ctx(x["q"])) for x in test]
tr = sum(T("".join(c)) for _, c in raw); comp = [(x, compress(x["q"], c)) for x, c in raw]; tc = sum(T("".join(c)) for _, c in comp)
R["F1_prompt_compressor"] = dict(tokens_raw=tr, tokens_comp=tc, saved=round(1 - tc / tr, 3), answer_kept=round(sum(has_ans(x, c) for x, c in comp) / max(1, sum(has_ans(x, c) for x, c in raw)), 3))
cache = []; hits = 0; tl_miss = []; tl_hit = []; stream = []
for x in test:
    t = tok(x["q"]); p = t[:]; random.shuffle(p); stream += [" ".join(t), " ".join(p[1:])]
for q in stream:
    s = set(tok(q)); t0 = time.perf_counter(); h = next((v for k, v in cache if len(s & k) / len(s | k) >= .75), None)
    if h is None: v = answer(q); cache.append((s, v)); tl_miss.append(time.perf_counter() - t0)
    else: hits += 1; tl_hit.append(time.perf_counter() - t0)
R["F2_semantic_cache"] = dict(queries=len(stream), hit_rate=round(hits / len(stream), 3), ms_miss=round(1e3 * sum(tl_miss) / len(tl_miss), 3), ms_hit=round(1e3 * sum(tl_hit) / max(1, len(tl_hit)), 3))
def shingles(s): w = tok(s); return {" ".join(w[i:i + 5]) for i in range(max(1, len(w) - 4))}
def dedup(chunks):
    keep = []
    for c in chunks:
        sh = shingles(c)
        if all(len(sh & shingles(k)) / max(1, len(sh | shingles(k))) < .5 for k in keep): keep.append(c)
    return keep
raw10 = [(x, ctx(x["q"], 10)) for x in test]; t10 = sum(T("".join(c)) for _, c in raw10); dd = [(x, dedup(c)) for x, c in raw10]; td = sum(T("".join(c)) for _, c in dd)
R["F3_context_dedup"] = dict(tokens_raw=t10, tokens_dedup=td, saved=round(1 - td / t10, 3), answer_kept=round(sum(has_ans(x, c) for x, c in dd) / max(1, sum(has_ans(x, c) for x, c in raw10)), 3))
def summ(q, c):
    L = c.splitlines(); qt = set(tok(q)); best = max(L, key=lambda l: len(qt & set(tok(l))), default="")
    return "\n".join(L[:2] + [best])
sf = [(x, [summ(x["q"], c) for c in cs]) for x, cs in raw]; ts_ = sum(T("".join(c)) for _, c in sf)
R["F4_summary_first"] = dict(tokens=ts_, saved=round(1 - ts_ / tr, 3), answer_kept=round(sum(has_ans(x, c) for x, c in sf) / max(1, sum(has_ans(x, c) for x, c in raw)), 3))
small = [x for x in test if cited_ok(x, answer(x["q"]))]
R["F5_router_small_to_large"] = dict(routed_small=round(len(small) / len(test), 3), small_path_acc=acc(small, s1) if small else None, large_tokens_avoided=sum(T("".join(c)) for x, c in raw if x in small), large_tokens_total=tr)
def files_for(q, k):
    seen = []
    for r in retrieve(q, 30):
        if r[0] not in seen: seen.append(r[0])
    return seen[:k]
def rk(fn, k): return round(sum(x["file"] in fn(x["q"], k) for x in test) / len(test), 3)
R["recall_baseline"] = {f"@{k}": rk(files_for, k) for k in (1, 5)}
hot = collections.OrderedDict(); tiers = collections.Counter(); lat = []
def tiered(q, k):
    key = frozenset(tok(q))
    if key in hot: hot.move_to_end(key); tiers["hot"] += 1; return hot[key]
    r = [f for f in files_for(q, 30) if f.startswith("/workspace/rick/")][:k]
    if len(r) < k: r = files_for(q, k); tiers["cold"] += 1
    else: tiers["warm"] += 1
    hot[key] = r
    if len(hot) > 64: hot.popitem(last=False)
    return r
for _ in range(2):
    for x in test: t0 = time.perf_counter(); tiered(x["q"], 5); lat.append(time.perf_counter() - t0)
tiers0 = dict(tiers); R["M1_tiered_memory"] = dict(recall_at5=rk(tiered, 5), tiers_2pass=tiers0, ms_avg=round(1e3 * sum(lat) / len(lat), 3))
G = json.load(open("/workspace/rick/tools/fullpicture/graph.json")); nb = collections.defaultdict(set)
for e in G["edges"]: nb[e["source"]].add(e["target"]); nb[e["target"]].add(e["source"])
name = lambda n: n.split(":", 1)[1].split("/")[-1].lower()
def graph_recall(q, k):
    qt = set(tok(q)); ext = {name(m) for n in list(nb) if name(n) in qt for m in sorted(nb[n], key=lambda m: -len(nb[m]))[:2]}
    base = files_for(q, k)
    if not ext: return base
    more = files_for(q + " " + " ".join(ext), k)
    return (base[:max(1, k - 2)] + [f for f in more if f not in base[:max(1, k - 2)]])[:k]
R["M2_graph_recall"] = {f"@{k}": rk(graph_recall, k) for k in (1, 5)}
reinf = collections.Counter()
for age, x in enumerate(reversed(dev)): reinf[x["file"]] += 0.9 ** (age / 20)
def reinforced(q, k):
    fs = files_for(q, 30); return sorted(fs, key=lambda f: fs.index(f) - 3 * min(1, reinf[f] / 5))[:k]
R["M3_decay_reinforce"] = {f"@{k}": rk(reinforced, k) for k in (1, 5)}
json.dump(R, open("brain_results.json", "w"), indent=1); json.dump(qa, open("qa_set.json", "w"), indent=0)
print(json.dumps(R))
