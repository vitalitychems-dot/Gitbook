"""Fast checks of the result files and core invariants (run: .venv/bin/python test_qinvent.py)."""
import json, networkx as nx
L = lambda n: json.load(open(f"results/inv{n}.json"))
def test_inv3_kept():
    r = L(3)["leak_fixed"]; assert r["clean_mwpm_dev_prior"]["top1"] > max(r["clean_prior_only"]["top1"], r["clean_baseline"]["top1"])
    assert r["clean_mwpm_dev_prior"]["recall5"] >= 0.94
def test_matching_merges_duplicates():
    import inv3_mwpm_dedup as m
    body = "alpha beta gamma delta epsilon zeta eta theta iota kappa " * 3
    lab, _ = m.clusters([(1, "/a", body, 0), (2, "/b", body, 0), (3, "/c", "totally different words here now ok", 0)])
    assert lab[0] == lab[1] != lab[2]
def test_inv2_dropped(): r = L(2); assert r["on_inv3"]["chosen_r"] == 0 and r["raw"]["chosen_r"] == 0
def test_inv4_vote_no_gain_over_best_single(): r = L(4); assert r["majority_acc"] <= max(r["individual_acc"].values())
def test_inv1_tie(): r = L(1); assert r["anneal_best"] == r["longest_chain"] == 25 and r["fifo"] == 32 and r["lower_bound"] <= 25
def test_inv5_dropped(): assert L(5)["chosen_on_dev"] is None
if __name__ == "__main__":
    n = 0
    for k, f in list(globals().items()):
        if k.startswith("test_"): f(); n += 1; print("PASS", k)
    print(n, "passed")
