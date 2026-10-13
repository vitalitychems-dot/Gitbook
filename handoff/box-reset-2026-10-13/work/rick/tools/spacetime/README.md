# spacetime — space+time trail composite
48 synthetic frames of 3 objects at depths 1/2/3.5 (z-buffered). Each frame is depth-shaded (nearer = brighter) and max-blended with exponential age decay (0.9^age), producing long-exposure "light-field-style" motion trails. Honest: a temporal composite + depth shading, not a real light field capture.
Run: `python3 spacetime.py` → `sample_trail_depth.png`, `baseline_mean.png`, `results.json`.
