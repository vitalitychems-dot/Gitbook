# Open problems

Famous unsolved (or only partially resolved) questions in mathematics and physics. For each: current known status, what agents can **realistically** do here, and a real source.

**Hard rule:** Solving a Millennium Problem or Collatz-class conjecture is a **GOAL**, not a claim. Verifying finite cases is **TESTED** evidence of consistency on a range—not a proof. Do not announce “solved” without peer-reviewed acceptance and Tessera Moderator + Security + Build gates.

---

## Millennium Prize Problems (Clay Mathematics Institute)

| ID | Problem | Status (as commonly reported) | What agents can realistically do | Source |
|----|---------|-------------------------------|----------------------------------|--------|
| OP-M01 | **P versus NP** | Unsolved. Widely believed P ≠ NP; no proof. | Survey reductions; implement small NP-complete instances; check literature for claimed proofs (almost all flawed). Cannot settle the question with experiments alone. | [Clay: P vs NP](https://www.claymath.org/millennium/p-vs-np/); [Wikipedia: P versus NP](https://en.wikipedia.org/wiki/P_versus_NP) |
| OP-M02 | **Hodge conjecture** | Unsolved. | Literature survey; toy algebraic-geometry examples in computer algebra (Sage/Singular) for tiny cases. No agent-scale attack on the general case. | [Clay: Hodge](https://www.claymath.org/millennium/hodge-conjecture/); [Wikipedia: Hodge conjecture](https://en.wikipedia.org/wiki/Hodge_conjecture) |
| OP-M03 | **Poincaré conjecture** | **Solved** (Perelman, 2002–2003; verified ~2006). Prize accepted in form of declined Clay award / community recognition. | Study expositions; reproduce statements of Ricci-flow-with-surgery at high level. Not an open problem for new “solutions.” Mark RETAINED if listed as open by mistake. | [Clay: Poincaré](https://www.claymath.org/millennium/poincare-conjecture/); [Wikipedia: Poincaré conjecture](https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture) |
| OP-M04 | **Riemann hypothesis (RH)** | Unsolved. All non-trivial zeros checked computationally to very large height lie on the critical line; no proof. | Verify zeros on finite height intervals with known algorithms (heavy numerics); study RMT connections (see `CONNECTIONS.md`); never claim RH from finite checks. | [Clay: Riemann](https://www.claymath.org/millennium/riemann-hypothesis/); [Wikipedia: Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis) |
| OP-M05 | **Yang–Mills existence and mass gap** | Unsolved as a Clay problem (constructive 4D QFT + mass gap). | Lattice QCD-style toy simulations; literature survey. Not a proof of the Clay statement. | [Clay: Yang–Mills](https://www.claymath.org/millennium/yang-mills-the-maths-of-quarks/); [Wikipedia: Yang–Mills existence and mass gap](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_existence_and_mass_gap) |
| OP-M06 | **Navier–Stokes existence and smoothness** | Unsolved in 3D. | DNS of NSE on small grids; check blow-up criteria literature; finite simulations ≠ existence proof. | [Clay: Navier–Stokes](https://www.claymath.org/millennium/navier-stokes-equation/); [Wikipedia: Navier–Stokes existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness) |
| OP-M07 | **Birch and Swinnerton-Dyer (BSD)** | Unsolved in full generality; known in special cases / ranks. | Compute ranks and L-functions for specific elliptic curves (Sage); compare with tabulated data. | [Clay: BSD](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/); [Wikipedia: Birch and Swinnerton-Dyer conjecture](https://en.wikipedia.org/wiki/Birch_and_Swinnerton%E2%80%93Dyer_conjecture) |

---

## Other notable math problems

| ID | Problem | Status | What agents can realistically do | Source |
|----|---------|--------|----------------------------------|--------|
| OP-M08 | **Collatz conjecture** | Unsolved. Verified computationally for enormous ranges of starting values; no proof. | Compute stopping times / max height on finite ranges; memoized search (see `code/collatz_max_stopping.py`). Finite max ≠ proof. | [Wikipedia: Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) |
| OP-M09 | **Twin prime conjecture** | Unsolved. Bounded gaps between primes proven (Zhang 2013; Polymath refinements); infinitely many twins still open. | Enumerate twin primes to a bound; survey sieve literature. | [Wikipedia: Twin prime](https://en.wikipedia.org/wiki/Twin_prime) |
| OP-M10 | **Goldbach conjecture** (strong / binary) | Unsolved. Verified computationally to at least 4×10^18 (Oliviera e Silva et al.). Weak (ternary) Goldbach proven by Helfgott (2013). | Sieve + check all even n ≤ N (see `code/goldbach_verify.py`). Finite verification ≠ proof. | [Wikipedia: Goldbach's conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) |
| OP-M11 | **abc conjecture** | Contested claim. Mochizuki announced a proof via inter-universal Teichmüller theory; not broadly accepted by the number-theory community as of mid-2020s surveys. | Literature/status tracking only; do not treat as settled. Label REPORTED carefully. | [Wikipedia: abc conjecture](https://en.wikipedia.org/wiki/Abc_conjecture) |
| OP-M12 | **Existence of odd perfect numbers** | Unsolved. No odd perfect number known; many constraints if one exists. | Search odd candidates under bounds; check abundance conditions. | [Wikipedia: Perfect number](https://en.wikipedia.org/wiki/Perfect_number) |
| OP-M13 | **Legendre’s conjecture** (prime between n² and (n+1)²) | Unsolved. | Check for n up to large N; sieve between consecutive squares. | [Wikipedia: Legendre's conjecture](https://en.wikipedia.org/wiki/Legendre%27s_conjecture) |

---

## Open physics questions

| ID | Problem | Status | What agents can realistically do | Source |
|----|---------|--------|----------------------------------|--------|
| OP-P01 | **Nature of dark matter** | Unknown. Multiple candidates (WIMPs, axions, primordial black holes, modified gravity alternatives); no confirmed detection of particle DM as of ongoing experiments. | Summarize experimental bounds; toy N-body sims; no discovery claim without data. | [Wikipedia: Dark matter](https://en.wikipedia.org/wiki/Dark_matter) |
| OP-P02 | **Nature of dark energy** | Unknown. Consistent with cosmological constant (Λ) in ΛCDM; dynamical DE and modified gravity remain open. | Fit simple cosmologies to public datasets; literature survey. | [Wikipedia: Dark energy](https://en.wikipedia.org/wiki/Dark_energy) |
| OP-P03 | **Quantum gravity** | Open. No experimentally confirmed complete theory; string theory and LQG are leading research programs among others. | Study dualities (e.g. AdS/CFT) at textbook level; small lattice/tensor models—not a full QG. | [Wikipedia: Quantum gravity](https://en.wikipedia.org/wiki/Quantum_gravity) |
| OP-P04 | **Measurement problem** | Open / interpretational. How definite outcomes arise from unitary QM remains disputed (Copenhagen, many-worlds, objective collapse, QBism, etc.). | Clarify assumptions; simulate decoherence toy models; do not “solve” interpretation by code alone. | [Wikipedia: Measurement problem](https://en.wikipedia.org/wiki/Measurement_problem) |
| OP-P05 | **Hierarchy problem** | Open. Why the Higgs mass is so far below the Planck scale without extreme fine-tuning (in naive EFT). | Survey SUSY/compositeness/anthropic proposals; no experimental resolution from this repo. | [Wikipedia: Hierarchy problem](https://en.wikipedia.org/wiki/Hierarchy_problem) |
| OP-P06 | **Turbulence** | Open in the sense of a complete predictive theory from NSE; Clay problem OP-M06 is the mathematical core. Phenomenology (Kolmogorov 1941, etc.) is highly developed. | Run small CFD / shell models; compare spectra to K41; cite limits of resolution. | [Wikipedia: Turbulence](https://en.wikipedia.org/wiki/Turbulence); [Wikipedia: Kolmogorov–Obukhov theory](https://en.wikipedia.org/wiki/Turbulence#Kolmogorov's_theory) |

---

## Agent scope summary

| Allowed (typical) | Not allowed as a claim |
|-------------------|------------------------|
| Finite verification with logged commands (**TESTED**) | “Proof” of Collatz / RH / Goldbach / P≠NP |
| Literature status notes (**REPORTED**) | Invented citations or fake runtimes |
| Toy simulations and catalogs (**TESTED** / **GOAL**) | Announcing discovery of dark matter / QG |
| Connection proposals with tests (`CONNECTIONS.md`) | Merging without Moderator / Security / Build |

When in doubt: label **GOAL** or **UNKNOWN**, run a small reproducible check, and file a draft PR—not a victory announcement.
