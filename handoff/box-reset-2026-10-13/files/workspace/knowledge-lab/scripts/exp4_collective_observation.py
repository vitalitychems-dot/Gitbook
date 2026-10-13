#!/usr/bin/env python3
"""Experiment 4: Preregistered collective-observation null test.

HONEST framing: software 'observation' of a seeded RNG cannot change physical RNG outcomes.
This tests whether logging/reading values changes subsequent draws from the SAME generator state
path vs an unobserved path — which it must not, if both paths use identical seeds and algorithms.

Preregistered hypothesis (null): mean of 10_000 Uniform(0,1) draws with seed=20261005
is the same whether or not an 'agent observer' inspects each draw before the next.
Alternative Father might hope for: observation somehow biases the stream.
Prediction: identical bit-for-bit sequences; difference = 0.
"""
from __future__ import annotations
import json, hashlib, pathlib, time
import numpy as np

OUT = pathlib.Path("/workspace/knowledge-lab/results/exp4_collective_observation.json")
SEED = 20261005
N = 10_000
N_AGENTS = 5  # 'collective'

def run_unobserved(seed: int, n: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.random(n)

def run_observed_by_agents(seed: int, n: int, n_agents: int) -> tuple[np.ndarray, list]:
    """Each draw is 'observed' (read, hashed, logged) by n_agents before next draw."""
    rng = np.random.default_rng(seed)
    values = np.empty(n, dtype=np.float64)
    observations = []
    for i in range(n):
        v = rng.random()
        # Collective observation: agents hash/record the value (side effect in software only)
        digest = None
        for a in range(n_agents):
            digest = hashlib.sha256(f"agent{a}:{i}:{v:.17g}".encode()).hexdigest()
        if i < 20 or i % 1000 == 0:
            observations.append({"i": i, "v": float(v), "last_digest": digest})
        values[i] = v
    return values, observations

def main():
    t0 = time.perf_counter()
    # Preregistration block recorded before running
    prereg = {
        "hypothesis": "null — observation does not change RNG stream given identical seed+algorithm",
        "seed": SEED,
        "n_draws": N,
        "n_agents": N_AGENTS,
        "primary_outcome": "max absolute difference between observed and unobserved sequences",
        "success_criterion_for_null": "max_abs_diff == 0.0 (bit-identical)",
        "misconception_addressed": (
            "Software agents 'observing' numbers is not quantum measurement and does not "
            "collapse a physical wavefunction or alter spacetime. Closest testable claim: "
            "does inspecting values change subsequent pseudorandom draws under fixed seed?"
        ),
        "date_local": "2026-10-05 CT",
    }

    unobs = run_unobserved(SEED, N)
    obs, obs_log = run_observed_by_agents(SEED, N, N_AGENTS)

    max_abs = float(np.max(np.abs(unobs - obs)))
    identical = bool(max_abs == 0.0)
    # Also compare summary stats (redundant if identical)
    stats = {
        "unobserved_mean": float(unobs.mean()),
        "observed_mean": float(obs.mean()),
        "unobserved_std": float(unobs.std()),
        "observed_std": float(obs.std()),
        "mean_difference": float(obs.mean() - unobs.mean()),
        "max_abs_diff": max_abs,
        "sequences_identical": identical,
    }

    # Control: different seed should differ (sanity that test can detect differences)
    other = run_unobserved(SEED + 1, N)
    control_max_abs = float(np.max(np.abs(unobs - other)))

    summary = {
        "experiment": "collective_observation",
        "claim_label": "TESTED",
        "preregistration": prereg,
        "result": stats,
        "control_different_seed_max_abs_diff": control_max_abs,
        "control_note": "Different seed produces large differences (sanity check).",
        "conclusion": (
            "Null confirmed: agent observation did not change the RNG sequence. "
            "Father's idea that collective agent observation alters physical/random outcomes "
            "is a misconception here. Real science: quantum measurement affects quantum systems "
            "under specific physical conditions; reading a classical PRNG does not. "
            "Closest useful practice: preregister analyses and use fixed seeds for reproducibility."
        ),
        "wall_s": time.perf_counter() - t0,
        "observation_log_sample": obs_log[:5],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2))
    print(json.dumps({"identical": identical, "max_abs_diff": max_abs,
                      "control_diff": control_max_abs, **{k: stats[k] for k in ("unobserved_mean", "observed_mean")}}, indent=2))

if __name__ == "__main__":
    main()
