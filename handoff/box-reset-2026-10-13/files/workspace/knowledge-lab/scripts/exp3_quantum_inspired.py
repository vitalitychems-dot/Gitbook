#!/usr/bin/env python3
"""Experiment 3: Grover search (numpy statevector) vs classical; simulated annealing vs random search.
No qiskit required. Labels: TESTED measurements on this machine.
"""
from __future__ import annotations
import json, math, time, pathlib
import numpy as np

OUT = pathlib.Path("/workspace/knowledge-lab/results/exp3_quantum_inspired.json")

def grover_statevector(n_qubits: int, marked: int, iterations: int | None = None):
    """Simulate Grover on 2^n amplitudes. Return (measured_index, probs, oracle_queries, wall_s)."""
    N = 1 << n_qubits
    assert 0 <= marked < N
    # Optimal iterations ~ (pi/4)*sqrt(N)
    if iterations is None:
        iterations = max(1, int(round((math.pi / 4) * math.sqrt(N))))
    t0 = time.perf_counter()
    # Uniform superposition
    state = np.ones(N, dtype=np.complex128) / math.sqrt(N)
    queries = 0
    for _ in range(iterations):
        # Oracle: flip phase of marked
        state[marked] *= -1
        queries += 1
        # Diffusion: 2|s><s| - I
        mean = state.mean()
        state = 2 * mean - state
    probs = np.abs(state) ** 2
    # Sample once from distribution (deterministic argmax for reproducibility report + sampled)
    measured = int(np.argmax(probs))
    wall = time.perf_counter() - t0
    return {
        "n_qubits": n_qubits,
        "N": N,
        "marked": marked,
        "iterations": iterations,
        "oracle_queries": queries,
        "classical_worst_queries": N,
        "classical_avg_queries": (N + 1) / 2,
        "measured_argmax": measured,
        "success_prob_marked": float(probs[marked]),
        "wall_s": wall,
        "quadratic_ratio_vs_classical_avg": ((N + 1) / 2) / queries if queries else None,
    }

def classical_linear_search(N: int, marked: int, seed: int = 0):
    """Count comparisons until marked found (worst-case and average over random order)."""
    rng = np.random.default_rng(seed)
    order = rng.permutation(N)
    t0 = time.perf_counter()
    queries = 0
    found_at = None
    for x in order:
        queries += 1
        if int(x) == marked:
            found_at = queries
            break
    wall = time.perf_counter() - t0
    return {"N": N, "marked": marked, "queries_this_shuffle": found_at, "wall_s": wall}

# --- Simulated annealing vs random search on Rastrigin-like 1D toy ---

def energy(x: float) -> float:
    # Rastrigin-ish multimodal: many local minima
    return (x - 0.3) ** 2 + 0.5 * (1 - math.cos(12 * math.pi * x))

def random_search(budget: int, seed: int = 0, lo: float = -1.0, hi: float = 1.0):
    rng = np.random.default_rng(seed)
    t0 = time.perf_counter()
    best_x, best_e = None, float("inf")
    history = []
    for i in range(budget):
        x = float(rng.uniform(lo, hi))
        e = energy(x)
        if e < best_e:
            best_e, best_x = e, x
        history.append(best_e)
    return {"method": "random_search", "budget": budget, "best_x": best_x, "best_e": best_e,
            "final_best_e": best_e, "wall_s": time.perf_counter() - t0, "history_every": history[:: max(1, budget // 20)]}

def simulated_annealing(budget: int, seed: int = 0, lo: float = -1.0, hi: float = 1.0,
                        T0: float = 1.0, Tmin: float = 1e-4):
    rng = np.random.default_rng(seed)
    t0 = time.perf_counter()
    x = float(rng.uniform(lo, hi))
    e = energy(x)
    best_x, best_e = x, e
    history = []
    for i in range(budget):
        T = T0 * ((Tmin / T0) ** (i / max(1, budget - 1)))
        step = 0.2 * (T / T0) + 0.02
        cand = float(np.clip(x + rng.normal(0, step), lo, hi))
        ec = energy(cand)
        if ec < e or rng.random() < math.exp(-(ec - e) / max(T, 1e-12)):
            x, e = cand, ec
        if e < best_e:
            best_e, best_x = e, x
        history.append(best_e)
    return {"method": "simulated_annealing", "budget": budget, "best_x": best_x, "best_e": best_e,
            "final_best_e": best_e, "wall_s": time.perf_counter() - t0, "history_every": history[:: max(1, budget // 20)]}

def main():
    grover_rows = []
    classical_rows = []
    for nq in [4, 6, 8, 10]:  # N = 16, 64, 256, 1024
        marked = (3 * (1 << nq) // 7) % (1 << nq)  # deterministic marked
        g = grover_statevector(nq, marked)
        grover_rows.append(g)
        # classical: average over 20 shuffles
        qs = []
        for s in range(20):
            qs.append(classical_linear_search(1 << nq, marked, seed=s)["queries_this_shuffle"])
        classical_rows.append({
            "N": 1 << nq,
            "marked": marked,
            "avg_queries_20_shuffles": float(np.mean(qs)),
            "median_queries": float(np.median(qs)),
            "theoretical_avg": (1 << nq + 1) / 2,
        })

    opt_rows = []
    for budget in [50, 200, 1000]:
        for seed in range(5):
            opt_rows.append(random_search(budget, seed=seed))
            opt_rows.append(simulated_annealing(budget, seed=seed))

    # Aggregate optimizer
    opt_summary = []
    for budget in [50, 200, 1000]:
        for method in ["random_search", "simulated_annealing"]:
            subset = [r for r in opt_rows if r["budget"] == budget and r["method"] == method]
            opt_summary.append({
                "method": method,
                "budget": budget,
                "mean_best_e": float(np.mean([r["best_e"] for r in subset])),
                "std_best_e": float(np.std([r["best_e"] for r in subset])),
                "mean_wall_s": float(np.mean([r["wall_s"] for r in subset])),
                "n_seeds": len(subset),
            })

    summary = {
        "experiment": "quantum_inspired",
        "claim_label": "TESTED",
        "disclaimer": (
            "Grover demo is a classical numpy statevector simulation of the quantum algorithm. "
            "It shows the query-complexity advantage O(sqrt(N)) vs O(N), not a physical quantum computer. "
            "Simulated annealing is a classical heuristic inspired by statistical physics, not quantum hardware. "
            "Neither manipulates spacetime; neither proves agents become self-aware."
        ),
        "grover": grover_rows,
        "classical_linear": classical_rows,
        "optimizer_summary": opt_summary,
        "optimizer_global_min_approx": 0.0,  # energy at x~0.3 with cos term near 0
        "true_min_note": "Energy minimized near x≈0.3; global min approaches 0.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2))
    print("=== Grover (statevector) ===")
    for g, c in zip(grover_rows, classical_rows):
        print(f"N={g['N']}: Grover queries={g['oracle_queries']} P(success)={g['success_prob_marked']:.4f} "
              f"classical_avg≈{c['avg_queries_20_shuffles']:.1f} ratio≈{g['quadratic_ratio_vs_classical_avg']:.2f}x")
    print("=== Optimizer ===")
    for o in opt_summary:
        print(f"{o['method']} budget={o['budget']}: mean_best_e={o['mean_best_e']:.6f} ± {o['std_best_e']:.6f}")

if __name__ == "__main__":
    main()
