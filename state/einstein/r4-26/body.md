**Einstein R4-26 — affect.classify: lexicon matchers compiled once**

`classify()` (brain/affect.mjs — used by the recognizer prior, bench2, view, and every operator/mesh-log line) constructed a fresh `RegExp` for each of ~70 lexicon words on every call. Matchers are now built once at module load (same pattern text, no `g` flag, so `test()` stays stateless). Output schema and priority order unchanged.

**Measured** (real data: `MESHLOG` + `HELDOUT`, 248 labelled lines; median of 9 × 20 passes):
- classify: **49.21 µs → 10.31 µs** per line (**4.77×**)
- Output mismatches vs old code (affect, intent, both scores): **0** / 248 (+ 4 edge strings in the test)

Tests: v2 suite 116→117 pass (+1 `v2-084-affect-matchers` equality vs the old per-call RegExp classifier); same 14 env-only failures as main. No flags, no deletes.
