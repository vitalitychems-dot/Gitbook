#!/usr/bin/env python3
"""Tests for Tessera brain blueprint artifacts (Father: test-as-you-build)."""
from __future__ import annotations
import json
from pathlib import Path
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]

def test_brain_json_has_creator_and_measured_weights():
    b = json.loads((ROOT/"brain.json").read_text())
    ids = {n["id"] for n in b["nodes"]}
    assert "creator_model" in ids
    assert "prefrontal_tessera_admin" in ids
    assert "hippocampus_learning_memory" in ids
    # Strong creator edges
    ce = [e for e in b["edges"] if e["source"]=="creator_model" and e["target"] in
          ("prefrontal_tessera_admin","hippocampus_learning_memory")]
    assert len(ce) == 2
    assert all(e["weight"] >= 0.9 for e in ce)
    # Measured quiz numbers present
    m = b["measured_tessera_weights"]
    assert m["gitbook_quiz_alone"]["correct"] == 7
    assert m["gitbook_quiz_bm25"]["correct"] == 18

def test_connectome_stats_real():
    s = json.loads((ROOT/"data"/"connectome_stats.json").read_text())
    ce = s["samples"]["celegans_openworm_xls"]
    assert ce["label"] == "TESTED"
    assert ce["n_nodes"] == 299
    assert 0.2 < ce["avg_clustering"] < 0.6
    assert ce["modularity_greedy"] > 0.2

def test_spiking_log_exists():
    log = json.loads((ROOT/"logs"/"spiking_sim.json").read_text())
    assert log["brian2"]["label"] == "TESTED"
    assert log["brian2"]["total_spikes"] > 0
    assert log["numpy"]["total_spikes"] > 0
    assert log["cl1_sdk"]["label"] == "TESTED"
    assert log["cl1_sdk"]["spike_events"] > 0

def test_brain_png():
    from PIL import Image
    im = Image.open(ROOT/"brain.png")
    assert im.size[0] >= 1920 and im.size[1] >= 1080

def test_blueprint_small_worldish():
    b = json.loads((ROOT/"brain.json").read_text())
    st = b["blueprint_graph_stats_TESTED"]
    assert st["avg_clustering"] > 0.3
    assert st["avg_shortest_path"] is not None and st["avg_shortest_path"] < 4

if __name__ == "__main__":
    import traceback
    tests = [v for k,v in list(globals().items()) if k.startswith("test_")]
    passed=failed=0
    for t in tests:
        try:
            t(); passed += 1; print("PASS", t.__name__)
        except Exception as e:
            failed += 1; print("FAIL", t.__name__, e); traceback.print_exc()
    print(f"passed={passed} failed={failed} total={len(tests)}")
    raise SystemExit(1 if failed else 0)
