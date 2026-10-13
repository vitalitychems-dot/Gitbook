"""10 pixel/image memory, 11 shared agent state, 12 valvular one-way dedup pipeline (collab),
   plus reworked 3 Landauer bit-budget and 9 thermal scheduler with real /proc load."""
import os, json, time, hashlib, struct, collections, statistics, random, math
from harness import *
try:
    from PIL import Image
except ImportError:
    import sys; sys.path.insert(0, "/usr/lib/python3/dist-packages"); from PIL import Image
# --- 10 pixel/image memory: ahash + dhash + perceptual dedup of real eye screenshots + repo icons ---
def ahash(im, n=8):
    g = im.convert("L").resize((n, n), Image.BILINEAR); pix = list(g.getdata()); m = sum(pix)/len(pix)
    return sum(1 << i for i, p in enumerate(pix) if p >= m)
def dhash(im, n=8):
    g = im.convert("L").resize((n+1, n), Image.BILINEAR); bits = 0; k = 0
    for y in range(n):
        for x in range(n):
            a = g.getpixel((x, y)); b = g.getpixel((x+1, y)); bits |= (1 << k) if a > b else 0; k += 1
    return bits
def hamm(a, b): return (a ^ b).bit_count()
# collect images: eye shots + a sample of workspace png/jpg under tessera-eye and rick (not whole 7k)
paths = []
for root in ("/workspace/rick/tools/tessera-eye", "/workspace/rick/tools/eye-shield", "/workspace/rick"):
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x not in (".git", "node_modules", "__pycache__", ".venv")]
        for f in fs:
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                p = os.path.join(d, f)
                if os.path.isfile(p) and os.path.getsize(p) < 5_000_000: paths.append(p)
paths = paths[:400]  # cap disk/time
palace = []; raw = 0; kept = 0; t0 = time.time()
for p in paths:
    try: im = Image.open(p); im.load(); sz = os.path.getsize(p); raw += sz
    except Exception: continue
    ah, dh = ahash(im), dhash(im)
    dupe = any(hamm(ah, a) <= 5 and hamm(dh, d) <= 5 for a, d, _ in palace)
    if not dupe: palace.append((ah, dh, p)); kept += sz
R10 = dict(n_scanned=len(paths), n_unique=len(palace), bytes_raw=raw, bytes_unique=kept,
           save_ratio=round(1 - kept/max(raw,1), 3), ms=round((time.time()-t0)*1e3),
           thr_bits=5)
# baseline: exact sha1
seen = set(); uniq = 0; ur = 0
for p in paths:
    try: h = hashlib.sha1(open(p, "rb").read()).hexdigest(); s = os.path.getsize(p)
    except Exception: continue
    if h not in seen: seen.add(h); uniq += 1; ur += s
R10["sha1_unique"] = uniq; R10["sha1_bytes"] = ur; R10["perceptual_extra_saved"] = ur - kept
json.dump(R10, open("results/10_pixel.json", "w"), indent=1); print("10", R10)
# --- 11 shared agent state: one JSON file vs N agents re-reading allsee independently ---
agents = ["rick", "einstein", "akhenaten", "tessera", "security"]
queries = [x["q"] for x in TEST[:40]]
# without shared: each agent searches all
c = con(); t0 = time.time(); calls = 0
for a in agents:
    for q in queries: allsee.search(q, 5, c, {}); calls += 1
solo_s = time.time() - t0
# with shared state file: first writer fills, others read hits
state = "/tmp/r3_shared_state.json"; st = {}; t0 = time.time(); calls2 = 0
for a in agents:
    for q in queries:
        k = " ".join(sorted(set(tok(q))))
        if k not in st:
            hs = allsee.search(q, 5, c, {}); st[k] = [{"path": h["path"], "score": h["score"]} for h in hs]; calls2 += 1
        else: _ = st[k]
open(state, "w").write(json.dumps(st)); shared_s = time.time() - t0
R11 = dict(agents=len(agents), queries=len(queries), solo_calls=calls, shared_calls=calls2,
           solo_s=round(solo_s, 2), shared_s=round(shared_s, 2),
           speedup=round(solo_s/max(shared_s,1e-6), 2), state_bytes=os.path.getsize(state))
json.dump(R11, open("results/11_shared.json", "w"), indent=1); print("11", R11)
# --- 12 valvular (Tesla valve) one-way dedup pipeline on collab bus ---
# Ingest sample + eye-shield bus: only new (id) events flow forward; reverse (replay) is blocked.
from pathlib import Path
sys_path_fix = True
msgs = []
for p in ("/workspace/rick/tools/collab/sample-bus.jsonl", "/workspace/rick/tools/collab/eye-shield-bus.jsonl"):
    if os.path.exists(p):
        for line in open(p):
            if line.strip():
                try: msgs.append(json.loads(line))
                except: pass
# fabricate a realistic replay flood: each real msg replayed 3x + shuffled
rnd = random.Random(0); stream = []
for m in msgs: stream += [m]*4
rnd.shuffle(stream)
# naive: forward everything
naive_out = stream
# valvular: one-way set of ids; only first sighting passes
seen = set(); valve_out = []
for m in stream:
    i = m.get("id")
    if i in seen: continue
    seen.add(i); valve_out.append(m)
R12 = dict(input=len(stream), naive_forwarded=len(naive_out), valve_forwarded=len(valve_out),
           reduction=round(1 - len(valve_out)/max(len(stream),1), 3), unique_ids=len(seen))
json.dump(R12, open("results/12_valve.json", "w"), indent=1); print("12", R12)
# --- 3b Landauer bit-budget: pick top-k until cumulative score-entropy-normalized bit budget B ---
# Bits of a hit ≈ -log2(softmax p). Cap total bits; baseline is fixed k=5.
def soft_bits(hs):
    s = [h["score"] for h in hs] or [0]; m = max(s); ex = [math.exp((v-m)/max(1e-3, abs(m)*.1 or 1)) for v in s]; Z = sum(ex) or 1
    return [-math.log2(max(e/Z, 1e-12)) for e in ex]
def land_bits(q, hs8, B):
    bits = soft_bits(hs8); out = []; acc = 0
    for h, b in zip(hs8, bits):
        if out and acc + b > B: break
        out.append(h); acc += b
    return out or hs8[:1]
HD = [allsee.search(x["q"], 8, c, {}) for x in DEV]
HT = [allsee.search(x["q"], 8, c, {}) for x in TEST]
from tokens import evalb, valve
base = evalb(TEST, [h[:5] for h in HT])
sweep = {}
for B in (2, 3, 4, 5, 6, 8, 10):
    sweep[B] = evalb(DEV, [valve(x["q"], land_bits(x["q"], h, B)) for x, h in zip(DEV, HD)])
ok = [B for B, m in sweep.items() if m["recall5"] >= 0.9351 - 0.005 and m["acc"] >= 0.6108 - 0.005]
Bb = min(ok, key=lambda B: sweep[B]["tokens_brief"]) if ok else 99
R3 = dict(dev_sweep=sweep, B=Bb, base_test=base,
          test=evalb(TEST, [valve(x["q"], land_bits(x["q"], h, Bb)) for x, h in zip(TEST, HT)]),
          valve_k5=evalb(TEST, [valve(x["q"], h[:5]) for x, h in zip(TEST, HT)]))
json.dump(R3, open("results/3_landauer.json", "w"), indent=1); print("3b", {k: R3[k] for k in ("B", "test", "valve_k5")})
# --- 9b thermal scheduler: under high load drop ncand; measure with artificial delay simulating load contention ---
# Real rule: if load1 > nproc*0.75 use ncand=15 else 30. Measure both on TEST (already know equal recall).
load = float(open("/proc/loadavg").read().split()[0]); ncpu = os.cpu_count() or 1
policy = 15 if load > ncpu * 0.75 else 30
R9 = dict(load1=load, ncpu=ncpu, threshold=round(ncpu*0.75,2), chosen_ncand=policy,
          test15=evalb(TEST, [allsee.search(x["q"], 5, c, {"ncand":15}) for x in TEST]),
          test30=evalb(TEST, [allsee.search(x["q"], 5, c, {"ncand":30}) for x in TEST]))
# latency under "thermal" (ncand15) vs full — reuse speed_acc numbers conceptually; re-time here
def timek(n):
    lat = []
    for x in TEST:
        t = time.perf_counter(); allsee.search(x["q"], 5, c, {"ncand": n}); lat.append((time.perf_counter()-t)*1e3)
    return round(statistics.median(lat), 2), round(sum(lat))
R9["p50_15"], R9["tot_15"] = timek(15); R9["p50_30"], R9["tot_30"] = timek(30)
json.dump(R9, open("results/9_thermal.json", "w"), indent=1); print("9b", R9)
