# Connections

Propose and track links between theories (and between theories and open problems). Every proposal uses the template below and a Tessera status label from `README.md` (`TESTED`, `REPORTED`, `GOAL`, `UNKNOWN`, `BLOCKED`, `RETAINED`).

## Proposal template

Copy this block for each new connection. File via a branch + draft PR after a small check (see `WORKFLOW.md`).

```markdown
### CX-NNN: <short title>

- **Claim:** One sentence stating the proposed link.
- **Theories / problems linked:** IDs from THEORIES.md / OPEN-PROBLEMS.md (e.g. T-M07 ↔ T-M13).
- **Evidence:** Citations or experiment pointers (REPORTED sources must be real; TESTED must cite exact command + log).
- **Test:** A concrete, falsifiable check an agent can run (or BLOCKED with reason).
- **Status:** TESTED | REPORTED | GOAL | UNKNOWN | BLOCKED | RETAINED
- **Caveat:** What this does *not* prove.
- **Owner / date:** agent or human; timestamp in America/Chicago.
```

---

## Worked examples (known connections)

These are honest, well-documented links already in the literature. Status is **REPORTED** (not re-derived here).

### CX-001: Riemann zeta zeros ↔ random matrix theory

- **Claim:** The local statistical distribution of non-trivial zeros of the Riemann zeta function matches eigenvalue spacings of the Gaussian Unitary Ensemble (GUE) in random matrix theory (Montgomery–Odlyzko law / GUE hypothesis for zeta).
- **Theories / problems linked:** T-M07 (analytic number theory), T-M13 (random matrix theory), OP-M04 (Riemann hypothesis).
- **Evidence:**
  - Montgomery, H. L. (1973). “The pair correlation of zeros of the zeta function.” *Analytic Number Theory*, Proc. Sympos. Pure Math. 24, AMS.
  - Odlyzko, A. M. Numerical studies of zeta zero spacings (published tables/papers).
  - Survey: [Wikipedia: Hilbert–Pólya conjecture](https://en.wikipedia.org/wiki/Hilbert%E2%80%93P%C3%B3lya_conjecture); [Wikipedia: Random matrix](https://en.wikipedia.org/wiki/Random_matrix) (applications to number theory).
- **Test:** Compare nearest-neighbor spacing histogram of a published zero table (e.g. Odlyzko’s) against the GUE Wigner surmise on a finite sample; record plots + KS or moment stats as TESTED. Does **not** prove RH.
- **Status:** REPORTED (literature); finite spacing checks may be TESTED later.
- **Caveat:** Statistical agreement on computed zeros is not a proof of RH or of a spectral interpretation.
- **Owner / date:** Tessera draft; 2026-10-05 CT.

### CX-002: AdS/CFT correspondence (gauge/gravity duality)

- **Claim:** A quantum gravity theory in Anti-de Sitter space is equivalent (in precisely defined cases) to a conformal field theory on the conformal boundary—most famously Type IIB string theory on AdS₅×S⁵ dual to N=4 supersymmetric Yang–Mills in 4D (Maldacena 1997).
- **Theories / problems linked:** T-P14 (AdS/CFT), T-P05 (QFT), T-P12 (string theory), OP-P03 (quantum gravity).
- **Evidence:**
  - Maldacena, J. (1998). “The Large N Limit of Superconformal Field Theories and Supergravity.” *Adv. Theor. Math. Phys.* 2, 231–252 (arXiv:hep-th/9711200).
  - [Wikipedia: AdS/CFT correspondence](https://en.wikipedia.org/wiki/AdS/CFT_correspondence)
- **Test:** Reproduce textbook checks (e.g. matching of symmetries / central charges in a standard review example) as REPORTED study notes; lattice or tensor-network toy models of holography are GOAL/TESTED only for the toy, not for “proving” AdS/CFT.
- **Status:** REPORTED (established duality in specific settings; contested as a complete description of our universe’s cosmology).
- **Caveat:** Evidence is extremely strong in controlled supersymmetric settings; it does not by itself solve quantum gravity in our asymptotically de Sitter universe.
- **Owner / date:** Tessera draft; 2026-10-05 CT.

### CX-003: Information theory ↔ thermodynamics (Landauer / Szilard)

- **Claim:** Information-processing constraints link to thermodynamic entropy: erasing one bit of information in a system at temperature T dissipates at least kT ln 2 of heat (Landauer’s principle); related thought experiments include Szilard’s engine connecting information and work.
- **Theories / problems linked:** T-C03 (Shannon information theory), T-P07 (statistical mechanics), T-P08 (thermodynamics).
- **Evidence:**
  - Landauer, R. (1961). “Irreversibility and Heat Generation in the Computing Process.” *IBM J. Res. Dev.* 5 (3): 183–191.
  - Experimental confirmations in carefully controlled systems (e.g. Bérut et al., *Nature* 2012, and follow-ons)—cite primary papers when claiming TESTED externally.
  - [Wikipedia: Landauer's principle](https://en.wikipedia.org/wiki/Landauer%27s_principle); [Wikipedia: Szilard's engine](https://en.wikipedia.org/wiki/Szilard%27s_engine)
- **Test:** Simulate a discrete Szilard/Landauer toy (two-state system + reset) and show average heat ≥ kT ln 2 per bit erased in the model; log as TESTED for the *model*, not a new physical law.
- **Status:** REPORTED.
- **Caveat:** Toy simulations validate understanding of the bound in idealized models; they are not new physics discoveries.
- **Owner / date:** Tessera draft; 2026-10-05 CT.

---

## Index of proposals

| ID | Title | Status |
|----|-------|--------|
| CX-001 | Zeta zeros ↔ RMT / GUE | REPORTED |
| CX-002 | AdS/CFT | REPORTED |
| CX-003 | Information ↔ thermodynamics (Landauer) | REPORTED |

Add new rows as agents propose CX-004+.
