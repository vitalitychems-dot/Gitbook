"""python3 test_c1.py : re-checks cycle-1 claims from result files (run quantum.py, brain.py, empathy.py first)."""
import json
q=json.load(open("quantum_results.json")); b=json.load(open("brain_results.json")); e=json.load(open("empathy_results.json"))
assert all(v["verdict"].startswith("CONFIRMED") for v in q.values())
assert q["Q1_CHSH"]["classical_max"]==2 and q["Q1_CHSH"]["random_search_max"]<=q["Q1_CHSH"]["tsirelson"]+1e-9
assert abs(q["Q2_no_cloning"]["BH_fidelity"]-5/6)<1e-9
assert abs(q["Q3_grover"]["loglog_slope"]-.5)<.06 and q["Q5_vqe_h2"]["abs_err"]<1.6e-3
assert b["qa"]["test"]>=100 and b["F3_context_dedup"]["answer_kept"]==1.0 and b["F1_prompt_compressor"]["answer_kept"]==1.0
assert b["F2_semantic_cache"]["ms_hit"]<b["F2_semantic_cache"]["ms_miss"]
assert e["macro_f1"]>0.25 and e["acc"]>e["majority_acc"]
print("c1 tests: 7/7 pass")
