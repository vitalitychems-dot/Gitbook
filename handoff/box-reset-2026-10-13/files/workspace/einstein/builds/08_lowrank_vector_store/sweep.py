import importlib.util, numpy as np, json
spec = importlib.util.spec_from_file_location("b8", "run.py"); b8 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b8)
out = {}
for r in (64, 128, 192, 256):
    b8.R = r; out[r] = float(np.mean([b8.recall(s) for s in b8.vtk.seeds(5)])); print(r, round(out[r], 3), "bytes/vec", r + 4)
json.dump(out, open("rank_sweep.json", "w"))
