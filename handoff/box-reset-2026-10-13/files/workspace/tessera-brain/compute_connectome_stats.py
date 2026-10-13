#!/usr/bin/env python3
"""Compute real graph stats from freely downloaded connectome samples.
Labels: TESTED = computed here; REPORTED = cited published numbers.
"""
from __future__ import annotations
import json, math
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd
import networkx as nx

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "connectome_stats.json"

def rich_club_coefficient(G: nx.Graph, k: int) -> float:
    """Undirected rich-club φ(k) = 2E_>k / (N_>k*(N_>k-1))."""
    nodes = [n for n, d in G.degree() if d > k]
    if len(nodes) < 2:
        return float("nan")
    sub = G.subgraph(nodes)
    n = sub.number_of_nodes()
    e = sub.number_of_edges()
    return (2.0 * e) / (n * (n - 1))

def rich_club_curve(G: nx.Graph, ks=None):
    degs = [d for _, d in G.degree()]
    if not degs:
        return {}
    if ks is None:
        mx = max(degs)
        ks = sorted(set([1, 2, 3, 5, 10, 15, 20, max(1, mx // 4), max(1, mx // 2), mx - 1]))
        ks = [k for k in ks if 0 < k < mx]
    return {int(k): rich_club_coefficient(G, int(k)) for k in ks}

def graph_stats(G: nx.Graph | nx.DiGraph, name: str) -> dict:
    und = G.to_undirected() if G.is_directed() else G
    n = und.number_of_nodes()
    m = und.number_of_edges()
    dens = nx.density(und)
    degrees = [d for _, d in und.degree()]
    deg_hist = Counter(degrees)
    # clustering
    try:
        C = nx.average_clustering(und)
    except Exception as e:
        C = None
        cerr = str(e)
    else:
        cerr = None
    # modularity via greedy communities
    try:
        from networkx.algorithms.community import greedy_modularity_communities, modularity
        comms = list(greedy_modularity_communities(und))
        Q = modularity(und, comms)
        n_comm = len(comms)
    except Exception as e:
        Q, n_comm, comms = None, None, []
        qerr = str(e)
    else:
        qerr = None
    # small-world-ish: mean shortest path on largest CC
    try:
        cc = max(nx.connected_components(und), key=len)
        sub = und.subgraph(cc)
        if sub.number_of_nodes() > 1:
            # sample if large
            if sub.number_of_nodes() > 800:
                # approximate with random sample of pairs
                nodes = list(sub.nodes())
                rng = np.random.default_rng(42)
                sample = rng.choice(nodes, size=min(200, len(nodes)), replace=False)
                lengths = []
                for s in sample:
                    lengths.extend(nx.single_source_shortest_path_length(sub, s).values())
                L = float(np.mean(lengths)) if lengths else None
                path_note = "sampled_approx_n200"
            else:
                L = nx.average_shortest_path_length(sub)
                path_note = "exact_lcc"
        else:
            L, path_note = None, "trivial"
    except Exception as e:
        L, path_note = None, str(e)
    rc = rich_club_curve(und)
    # pick a representative rich-club at median degree
    med = int(np.median(degrees)) if degrees else 1
    rc_med = rich_club_coefficient(und, med)
    return {
        "label": "TESTED",
        "name": name,
        "directed_input": G.is_directed(),
        "n_nodes": n,
        "n_edges": m,
        "density": dens,
        "degree_mean": float(np.mean(degrees)) if degrees else None,
        "degree_median": float(np.median(degrees)) if degrees else None,
        "degree_std": float(np.std(degrees)) if degrees else None,
        "degree_min": int(min(degrees)) if degrees else None,
        "degree_max": int(max(degrees)) if degrees else None,
        "degree_histogram_top": dict(sorted(deg_hist.items())[:40]),
        "avg_clustering": C,
        "clustering_error": cerr,
        "modularity_greedy": Q,
        "n_communities_greedy": n_comm,
        "modularity_error": qerr,
        "avg_shortest_path_lcc": L,
        "path_note": path_note,
        "rich_club_phi_at_median_degree": rc_med,
        "rich_club_median_k": med,
        "rich_club_curve": rc,
    }

def load_celegans() -> nx.DiGraph:
    path = ROOT / "data" / "CElegansNeuronTables.xls"
    df = pd.read_excel(path, sheet_name="Connectome")
    # Prefer chemical synapses for directed connectome; include gap junctions as undirected pairs
    G = nx.DiGraph()
    for _, row in df.iterrows():
        a, b = str(row["Origin"]), str(row["Target"])
        w = int(row["Number of Connections"])
        typ = str(row["Type"])
        if typ.lower().startswith("gap"):
            # treat as bidirectional weak chemical-like for graph
            G.add_edge(a, b, weight=G.has_edge(a, b) and G[a][b].get("weight", 0) + w or w, kind="gap")
            G.add_edge(b, a, weight=G.has_edge(b, a) and G[b][a].get("weight", 0) + w or w, kind="gap")
        else:
            if G.has_edge(a, b):
                G[a][b]["weight"] += w
            else:
                G.add_edge(a, b, weight=w, kind="chemical")
    return G

def load_flywire_neuropil_coprojection(max_neurons: int = 50000) -> nx.Graph:
    """Neuropil co-membership graph: edge weight = # neurons with pre sites in both neuropils.
    Built from Zenodo FlyWire per_neuron_neuropil_count_pre_783.feather (CC-BY-4.0).
    Subsamples neurons for tractability (TESTED subsample, seed 42).
    """
    df = pd.read_feather(ROOT / "data" / "flywire_neuropil_pre_783.feather")
    # Restrict to neurons present in at least 2 neuropils
    vc = df.groupby("pre_pt_root_id").size()
    multi = vc[vc >= 2].index
    rng = np.random.default_rng(42)
    multi = np.array(multi)
    if len(multi) > max_neurons:
        multi = rng.choice(multi, size=max_neurons, replace=False)
    sub = df[df["pre_pt_root_id"].isin(multi)]
    # Build co-occurrence
    from itertools import combinations
    weights: Counter = Counter()
    for _, grp in sub.groupby("pre_pt_root_id"):
        nps = sorted(set(grp["neuropil"].tolist()))
        for a, b in combinations(nps, 2):
            weights[(a, b)] += 1
    G = nx.Graph()
    for (a, b), w in weights.items():
        G.add_edge(a, b, weight=w)
    G.graph["subsample_neurons"] = int(len(multi))
    G.graph["total_multi_neuropil_neurons"] = int(len(vc[vc >= 2]))
    return G

def main():
    results = {
        "generated_ct": "2026-10-05 ~19:10 CT",
        "honesty": "Software graph stats from public samples. Not a living brain.",
        "samples": {},
        "reported_literature": {
            "label": "REPORTED",
            "flywire_whole_brain_lin2024": {
                "citation": "Lin et al., Network Statistics of the Whole-Brain Connectome of Drosophila, bioRxiv/PMC (PMC10402125)",
                "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10402125/",
                "clustering_coefficient": 0.0463,
                "clustering_table2_alt": 0.0477,
                "connection_probability": 0.000160,
                "reciprocity": 0.138,
                "rich_club_cutoff_degree": 37,
                "rich_club_fraction_neurons_approx": 0.30,
                "note": "Published whole-brain FlyWire stats; not recomputed from full 852MB edge list (too large for this job).",
            },
            "hemibrain_scheffer2020": {
                "citation": "Scheffer et al., eLife 2020;9:e57443",
                "url": "https://doi.org/10.7554/eLife.57443",
                "approx_neurons": 25000,
                "license": "CC-BY",
                "note": "Full compact matrix download redirected to Google login — BLOCKED without account.",
            },
            "h01_shapsoncoe2024": {
                "citation": "Shapson-Coe et al., Science 2024; H01 release",
                "url": "https://h01-release.storage.googleapis.com/landing.html",
                "approx_cells": 57000,
                "approx_synapses": 150_000_000,
                "license": "CC-BY-4.0",
                "note": "Volumetric EM + synapse Avro exports exist; no small CSV edge list fetched without large downloads.",
            },
        },
    }
    print("Loading C. elegans...")
    Ce = load_celegans()
    print(f"  nodes={Ce.number_of_nodes()} edges={Ce.number_of_edges()}")
    results["samples"]["celegans_openworm_xls"] = {
        **graph_stats(Ce, "C. elegans chemical+gap (OpenWorm c302 tables)"),
        "source_file": "data/CElegansNeuronTables.xls",
        "source_url": "https://raw.githubusercontent.com/openworm/c302/master/c302/data/CElegansNeuronTables.xls",
        "license": "OpenWorm project data (public GitHub raw)",
    }
    print("Building FlyWire neuropil co-projection (subsample)...")
    Fw = load_flywire_neuropil_coprojection(50000)
    print(f"  neuropils={Fw.number_of_nodes()} edges={Fw.number_of_edges()} subsample={Fw.graph.get('subsample_neurons')}")
    s = graph_stats(Fw, "FlyWire neuropil co-projection (pre-site co-membership, 50k neuron subsample)")
    s["source_file"] = "data/flywire_neuropil_pre_783.feather"
    s["source_url"] = "https://zenodo.org/records/10676866"
    s["license"] = "CC-BY-4.0"
    s["subsample_neurons"] = Fw.graph.get("subsample_neurons")
    s["total_multi_neuropil_neurons"] = Fw.graph.get("total_multi_neuropil_neurons")
    s["caveat"] = "Co-projection ≠ synaptic adjacency. Synaptic edge list (852MB) not downloaded this session."
    results["samples"]["flywire_neuropil_coprojection"] = s

    OUT.write_text(json.dumps(results, indent=2))
    print("Wrote", OUT)
    # print key numbers
    for k, v in results["samples"].items():
        print(f"\n== {k} ==")
        for key in ["n_nodes","n_edges","degree_mean","degree_median","avg_clustering","modularity_greedy","n_communities_greedy","rich_club_phi_at_median_degree","rich_club_median_k","avg_shortest_path_lcc"]:
            print(f"  {key}: {v.get(key)}")

if __name__ == "__main__":
    main()
