# perceive — classical CV anomaly detector (numpy+PIL)
Per 16px block: log Laplacian variance (blur), edge density (low detail), structure-tensor gradient coherence (warp/smear). Robust z-scores (median/MAD), flag if any > 3. Outputs `<pre>_heatmap.png`, `<pre>.json`, `<pre>_inpaint.png` (diffusion inpaint of flagged blocks).
Usage: `python3 perceive.py IMAGE OUTPREFIX` · test: `python3 test_synth.py`
It flags regions that are statistically unusual in an image; it does not see "unrendered reality".
