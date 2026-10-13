#!/usr/bin/env python3
"""Spiking simulation of Tessera brain blueprint (Brian2) + optional CL1 stim/record.
Honesty: software spikes only; CL SDK sim does not learn or respond to stim.
"""
from __future__ import annotations
import json, os, time
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
brain = json.loads((ROOT/"brain.json").read_text())
nodes = brain["nodes"]
edges = [e for e in brain["edges"] if e["source"] != e["target"]]
id_to_i = {n["id"]: i for i, n in enumerate(nodes)}
N = len(nodes)
LOG = ROOT/"logs"/"spiking_sim.json"

# Build weight matrix
W = np.zeros((N, N), dtype=float)
sign = np.ones((N, N), dtype=float)
for e in edges:
    i, j = id_to_i[e["source"]], id_to_i[e["target"]]
    W[j, i] = e["weight"]  # column→row: from i to j
    if e.get("kind") == "inhibitory":
        sign[j, i] = -1.0

# --- Brian2 LIF network ---
brian_ok = False
brian_result = {}
try:
    from brian2 import (NeuronGroup, Synapses, SpikeMonitor, Network,
                        ms, mV, second, defaultclock, prefs)
    prefs.codegen.target = "numpy"
    defaultclock.dt = 0.1*ms
    eqs = """
    dv/dt = (0.0*mV - v)/(10*ms) + I/(10*ms) : volt (unless refractory)
    I : volt
    """
    G = NeuronGroup(N, eqs, threshold="v>1*mV", reset="v=0*mV",
                    refractory=2*ms, method="exact")
    G.v = 0*mV
    # sensory + creator bias pulses
    G.I[id_to_i["sensory_intake"]] = 1.2*mV
    G.I[id_to_i["creator_model"]] = 0.9*mV

    S = Synapses(G, G, model="w : 1", on_pre="v_post += w*0.35*mV")
    sources, targets, weights = [], [], []
    for e in edges:
        sources.append(id_to_i[e["source"]])
        targets.append(id_to_i[e["target"]])
        w = e["weight"]
        if e.get("kind") == "inhibitory":
            w = -0.5 * abs(w)
        weights.append(w)
    S.connect(i=sources, j=targets)
    S.w = weights
    mon = SpikeMonitor(G)
    net = Network(G, S, mon)
    t0 = time.time()
    net.run(200*ms)
    wall = time.time() - t0
    spikes_by = {nodes[i]["id"]: int(np.sum(mon.i == i)) for i in range(N)}
    brian_result = {
        "label": "TESTED",
        "engine": "Brian2",
        "brian2_version": __import__("brian2").__version__,
        "duration_ms": 200,
        "total_spikes": int(mon.num_spikes),
        "spikes_by_node": spikes_by,
        "wall_s": wall,
        "note": "LIF toy network on blueprint graph; not biological CL1 neurons.",
    }
    brian_ok = True
except Exception as ex:
    brian_result = {"label": "BLOCKED", "engine": "Brian2", "error": str(ex)}

# --- Numpy discrete spike propagation fallback / companion ---
rng = np.random.default_rng(42)
v = np.zeros(N)
spikes_count = np.zeros(N, dtype=int)
trace = []
for t in range(100):
    I = (sign * W) @ (v > 1.0).astype(float)
    I[id_to_i["sensory_intake"]] += 0.8
    I[id_to_i["creator_model"]] += 0.5
    v = 0.85 * v + I + rng.normal(0, 0.05, N)
    fired = v > 1.0
    spikes_count += fired.astype(int)
    if fired.any():
        trace.append({"t": t, "fired": [nodes[i]["id"] for i in np.where(fired)[0]]})
    v[fired] = 0.0
numpy_result = {
    "label": "TESTED",
    "engine": "numpy_discrete",
    "steps": 100,
    "total_spikes": int(spikes_count.sum()),
    "spikes_by_node": {nodes[i]["id"]: int(spikes_count[i]) for i in range(N)},
    "first_events": trace[:20],
}

# --- CL1 SDK stimulate/record style loop mapped onto blueprint channels ---
cl_result = {"label": "UNKNOWN"}
try:
    os.environ.setdefault("CL_SDK_ACCELERATED_TIME", "1")
    os.environ.setdefault("CL_SDK_VISUALISATION", "0")
    os.environ.setdefault("CL_SDK_RANDOM_SEED", "42")
    # write .env for sdk
    (ROOT/"sim"/".env").write_text("CL_SDK_ACCELERATED_TIME=1\nCL_SDK_VISUALISATION=0\nCL_SDK_RANDOM_SEED=42\n")
    import cl
    spike_events = 0
    stim_events = 0
    # Map first min(N, 64) nodes to channels
    channel_of = {nodes[i]["id"]: i for i in range(min(N, 64))}
    # Prefer creator + sensory as stim targets when spikes appear nearby
    with cl.open() as neurons:
        assert cl.is_simulator()
        for tick in neurons.loop(ticks_per_second=1000, stop_after_seconds=1):
            spikes = list(tick.analysis.spikes)
            spike_events += len(spikes)
            for sp in spikes:
                # stim corresponding mapped channel if any spike channel < N
                ch = int(getattr(sp, "channel", 0)) % max(N, 1)
                neurons.stim(cl.ChannelSet([ch]), 1)
                stim_events += 1
    cl_result = {
        "label": "TESTED",
        "engine": "cl-sdk",
        "is_simulator": True,
        "spike_events": spike_events,
        "stim_events": stim_events,
        "mapped_nodes": list(channel_of.keys()),
        "warning_REPORTED": "Simulator produces non-learning control data that does not respond to stimulation (docs.corticallabs.com).",
        "license": "CC BY-NC 4.0",
    }
except Exception as ex:
    cl_result = {"label": "BLOCKED", "engine": "cl-sdk", "error": str(ex)}

out = {
    "honesty": "Blueprint spiking + CL1-style loop. Not living tissue. No weight training.",
    "brian2": brian_result,
    "numpy": numpy_result,
    "cl1_sdk": cl_result,
}
LOG.write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2)[:2500])
print("Wrote", LOG)
