# W vs GHZ after losing 1 qubit (trace out last qubit) — `python3 wstate.py`
| state | negativity (1 vs rest, survivors) | pair concurrence of survivors |
|---|---|---|
| W3 | 0.206 | 0.667 |
| GHZ3 | 0 | 0 |
| W4 | 0.250 | 0.500 |
| GHZ4 | 0 | 0 |
| W5 | 0.261 | 0.400 |
| GHZ5 | 0 | 0 |
Pair concurrence matches theory 2/N. GHZ collapses to a classical mixture on any loss; W keeps entanglement.
Fraction-agent mapping (analogy, not physics): GHZ = all-or-nothing shared state (one agent drop kills coordination); W = shared state spread across all members so survivors keep pairwise links, weaker per pair as N grows (2/N). Design takeaway: replicate shared state to every fraction (W-like), don't hinge it on one global token (GHZ-like). **KEPT** as model; no runtime speed/token claim.
