#!/usr/bin/env python3
"""Build learning-curve and results-bar charts."""
from __future__ import annotations
import json
from pathlib import Path

RESULTS = Path("/workspace/learning-rate/results")
CHARTS = Path("/workspace/learning-rate/charts")
CHARTS.mkdir(parents=True, exist_ok=True)

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Learning curve
    curve_path = RESULTS / "learning_curve.json"
    if curve_path.exists():
        curve = json.loads(curve_path.read_text())
        xs, ys = [], []
        for p in curve["points"]:
            xs.append(p["feedback_events"])
            held = p["heldout"]
            ys.append(held.get("accuracy", held.get("heldout", {}).get("accuracy", 0)))
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.plot(xs, ys, marker="o", linewidth=2, color="#1f77b4")
        ax.set_xlabel("Feedback events (reflexion lessons from wrong train answers)")
        ax.set_ylabel("Held-out accuracy")
        ax.set_title("Learning curve: held-out accuracy vs feedback (seed=42)")
        ax.set_ylim(0, 1.05)
        ax.grid(True, alpha=0.3)
        for x, y in zip(xs, ys):
            ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)
        fig.tight_layout()
        fig.savefig(CHARTS / "learning_curve.png", dpi=120)
        plt.close(fig)
        print("wrote learning_curve.png")

    # Method comparison bar
    table_path = RESULTS / "table.json"
    # Also gather from individual result files if table incomplete
    summaries = []
    if table_path.exists():
        summaries = json.loads(table_path.read_text())
    else:
        for p in sorted(RESULTS.glob("*.json")):
            if p.name in ("meta.json", "chunk_stats.json", "dense_index.json", "learning_curve.json",
                          "consolidation.json", "selfstudy_lessons.json"):
                continue
            try:
                d = json.loads(p.read_text())
                if "summary" in d and "accuracy" in d["summary"]:
                    summaries.append(d["summary"])
            except Exception:
                pass

    if summaries:
        # dedupe by method keep last
        by_m = {}
        for s in summaries:
            by_m[s["method"]] = s
        summaries = list(by_m.values())
        summaries.sort(key=lambda s: -s["accuracy"])
        names = [s["method"] for s in summaries]
        accs = [s["accuracy"] for s in summaries]
        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.barh(names[::-1], accs[::-1], color="#2ca02c")
        ax.set_xlabel("Accuracy (all questions)")
        ax.set_title("Method accuracy comparison (qwen2.5:3b-instruct, seed=42)")
        ax.set_xlim(0, 1.05)
        ax.axvline(0.72, color="gray", linestyle="--", alpha=0.5, label="prior BM25 baseline 0.72 (n=25)")
        for bar, a in zip(bars, accs[::-1]):
            ax.text(a + 0.01, bar.get_y() + bar.get_height()/2, f"{a:.2f}", va="center", fontsize=8)
        ax.legend(loc="lower right", fontsize=8)
        fig.tight_layout()
        fig.savefig(CHARTS / "method_accuracy.png", dpi=120)
        plt.close(fig)
        print("wrote method_accuracy.png")

    # Split accuracy for best methods
    fig, ax = plt.subplots(figsize=(9, 5))
    methods_of_interest = []
    for s in summaries:
        if s.get("by_split"):
            methods_of_interest.append(s)
    if methods_of_interest:
        import numpy as np
        labels = [s["method"] for s in methods_of_interest]
        seen_a = [s["by_split"].get("seen", {}).get("accuracy", 0) for s in methods_of_interest]
        hold_a = [s["by_split"].get("heldout", {}).get("accuracy", 0) for s in methods_of_interest]
        x = np.arange(len(labels))
        w = 0.35
        ax.bar(x - w/2, seen_a, w, label="seen (n=25)", color="#1f77b4")
        ax.bar(x + w/2, hold_a, w, label="held-out (n=20)", color="#ff7f0e")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("Accuracy")
        ax.set_title("Seen vs held-out accuracy by method")
        ax.legend()
        ax.grid(True, axis="y", alpha=0.3)
        fig.tight_layout()
        fig.savefig(CHARTS / "seen_vs_heldout.png", dpi=120)
        plt.close(fig)
        print("wrote seen_vs_heldout.png")

if __name__ == "__main__":
    main()
