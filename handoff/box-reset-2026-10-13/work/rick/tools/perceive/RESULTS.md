# Results (20 synthetic 256px images, 6 known patches each: blur/flat/warp, block-level)
| detector | precision | recall | F1 |
|---|---|---|---|
| Laplacian-only (baseline) | 0.991 | 0.680 | 0.807 |
| combined (lap+edge+coherence) | 0.977 | **1.000** | **0.988** |
Detect speed ~5 ms / 256px image. **KEPT** (F1 +0.181; precision −0.014).
Attachment 8c4333…png (2868×1320 grayscale-ish screenshot): 5177/14678 blocks flagged (35%) — mostly flat/uniform screenshot areas (low-detail), i.e. expected on UI screenshots, not "unrendered" content. Inpaint on full-res image is slow (~90 s, 300 Jacobi iters) — known weakness.
