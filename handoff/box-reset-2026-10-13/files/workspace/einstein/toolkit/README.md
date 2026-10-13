# Einstein verification toolkit (item 0)
numpy + stdlib only.
- vtk.py: rng/seeds (seeded runs), bootstrap_ci, wilson (binomial CI), find_crossing (log-interp sign change),
  bench(name, baseline(seed), candidate(seed), n_seeds, higher_is_better) -> paired bootstrap CI on the gain,
  verdict KEEP only if the 95% CI lower bound of the gain > 0; fmt/save; svg_plot (no matplotlib).
- gf2.py: GF(2) rref / rank / nullspace.
- surface.py: rotated surface code (code capacity, X noise), exact MWPM via bitmask DP with boundary,
  stabilizer/logical checks asserted. `python3 surface.py SHOTS out.json plot.svg`.
