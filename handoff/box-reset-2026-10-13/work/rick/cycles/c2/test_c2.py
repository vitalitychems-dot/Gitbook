"""python3 test_c2.py : re-checks cycle-2 claims from result files."""
import json
q=json.load(open("quantum2_results.json")); b=json.load(open("brain2_results.json")); e=json.load(open("empathy2_results.json")); f=json.load(open("forecast_results.json"))
assert all(v["verdict"].startswith("CONFIRMED") for v in q.values())
assert b["coverage"]["c2_files"]==b["bench"]["test_files"]  # all test sources indexed
assert b["S1_rag_numeric_semantic_verifier"]>0.181          # beats c1 baseline
assert b["S1_citation_check"]["precision_accepted"]>=b["S1_rag_numeric_semantic_verifier"]
assert b["P_unified_pipeline"]["saved"]>0.5 and b["P_unified_pipeline"]["answer_kept"]>=0.9
assert e["macro_f1"]>e["c1_nb_macro_f1"]
assert f["days"]>=20 and "persistence" in f["models"]
import subprocess,sys; assert subprocess.run([sys.executable,"test_c1.py"],cwd="../c1").returncode==0
print("c2 tests: 8/8 pass (incl. test_c1)")
