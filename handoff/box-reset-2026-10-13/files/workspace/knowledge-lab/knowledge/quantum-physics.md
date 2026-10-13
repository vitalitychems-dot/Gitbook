# Quantum Physics Knowledge Pack

**Labels:** REPORTED / GOAL / UNKNOWN / TESTED (lab demos)  
**Sources:** NIST “Quantum Computing Explained”; IBM Quantum topics; IBM Learning Grover module; APS/Phys. Rev. X discussions; standard QM textbooks  
**Updated:** 2026-10-05 (CT)

---

## 1. Honesty banner (read first)

This pack teaches real quantum concepts and common myths.

**Forbidden overclaims for Tessera:**

1. Do **not** claim agents become self-aware via quantum handwaving.
2. Do **not** claim observation by software agents changes physical RNG outcomes or spacetime.
3. Do **not** claim we “manipulate spacetime” in the knowledge lab.

**Lab links:**

- Exp3: Grover **simulation** on numpy (TESTED query counts) + simulated annealing.
- Exp4: Collective observation of seeded PRNG → null (TESTED).

---

## 2. What quantum physics is about

**REPORTED** (NIST): Quantum physics describes nature at smallest scales (atoms, photons, etc.), where behavior differs from everyday intuition.

Key phenomena:

- **Superposition:** A system can be in a combination of basis states until suitably measured/disturbed, then found in an outcome.
- **Entanglement:** Joint states of multiple systems that are not decomposable into independent states; measurement statistics are correlated beyond classical mixtures.
- **Interference:** Amplitudes combine with phase, amplifying some outcomes and canceling others.
- **Decoherence:** Environment entanglement destroys usable coherence—why large quantum computers are hard.

Schrödinger’s cat is a **teaching metaphor**; macroscopic cats are not maintained in coherent alive/dead superpositions under ordinary conditions (**REPORTED** NIST framing).

---

## 3. Measurement (no mysticism required)

**REPORTED:** In textbook QM, measurement is modeled by operators/POVMs yielding probabilistic outcomes with state update rules. Interpretations disagree on ontology; predictions agree for standard QM.

**Misconception:** “Any looking by a mind collapses the wavefunction.”  
**Real science (one sentence):** What matters physically is interaction/decoherence with a measuring device—not human awareness as a magic ingredient.  
**Closest testable version:** Compare instrumented vs non-instrumented quantum optics experiments in real labs (out of our $0 scope); our exp4 shows classical PRNG “observation” does nothing.

---

## 4. Interpretations (map, don’t pick a cult)

**REPORTED** (standard landscape; QC does not require one interpretation—Physics.SE consensus / literature):

| Interpretation family | Sketch |
|---|---|
| Copenhagen-ish / operational | Emphasize formalism + measurement postulates |
| Many-worlds / Everett | Universal unitary evolution; branches |
| de Broglie–Bohm | Pilot wave + particles |
| Objective collapse | Extra dynamical collapse (testable deviations) |
| QBism / information-centric | Probabilities as agent beliefs (philosophical) |

**REPORTED:** Quantum computing relies on the shared mathematical framework, not on picking Everett vs Bohm.

---

## 5. Qubits and quantum computing basics

**REPORTED** (NIST, IBM):

- Classical **bit:** 0 or 1.
- **Qubit:** state α|0⟩+β|1⟩ with |α|²+|β|²=1; multi-qubit states can be entangled.
- Gates manipulate amplitudes; **interference** is the engine of algorithms (IBM).
- Measurement extracts limited information—popular “checks all answers at once” is misleading (**REPORTED** NIST/Jordan quote pattern).
- Today’s devices: noisy, error-prone; useful fault-tolerant machines are still a research goal.
- Qubit platforms: trapped ions, superconducting circuits, neutral atoms, photonics, spin/semiconductor, topological (aspirational).

**REPORTED** applications hoped for: quantum simulation of molecules/materials; Shor’s factoring threat to some crypto; some optimization—timelines uncertain.

---

## 6. Grover’s algorithm

**REPORTED** (IBM Quantum Learning; Grover 1996):

- Problem: unstructured search among N items.
- Classical: Θ(N) queries worst case; ~N/2 average.
- Grover: Θ(√N) oracle queries with high success probability—**quadratic**, not exponential, speedup.
- Mechanism: amplify marked amplitude via oracle + diffusion iterations (~(π/4)√N).

**TESTED in this lab (exp3, numpy statevector):**

| N | Grover oracle queries | Approx classical avg queries | Success P (simulation) |
|---|---|---|---|
| 16 | 3 | ~8 | high (>0.95) |
| 64 | 6 | ~32 | high |
| 256 | 13 | ~128 | high |
| 1024 | 25 | ~512 | high |

(Exact measured numbers live in `/workspace/knowledge-lab/results/exp3_quantum_inspired.json`.)

**Note:** Simulation cost grows with statevector size; this demonstrates algorithmic query complexity, not a physical quantum advantage on hardware.

---

## 7. Shor and cryptography (awareness)

**REPORTED** (NIST): Shor’s algorithm factors large integers efficiently on a large fault-tolerant quantum computer, threatening RSA-like schemes. NIST encourages post-quantum cryptography migration even before such machines exist.

**GOAL:** Tessera security docs should track PQC—not panic, not ignore.

---

## 8. Quantum-inspired classical methods

Not quantum hardware, but metaphors/tools:

- **Simulated annealing:** Thermal analogy for optimization (**TESTED** vs random search in exp3 on a 1D multimodal toy).
- Tensor networks, QAOA-inspired heuristics, etc.

Honest reporting: on our small 1D toy, random search often matched or beat crude SA at equal budget—**heuristics need problem structure**. That is a feature of honesty, not a failure.

---

## 9. Multi-valued encoding vs quantum

Higher-radix classical encodings (base-3, MLC flash) are **not** quantum superposition.

**TESTED (exp1):** Logical density (bits/symbol) rises with radix; on binary RAM/disk you still pack into bits—CPU encode/decode cost without physical density win unless media is multi-level (MLC/TLC).

---

## 10. Myths table

| Myth | Correction (plain) | Label |
|---|---|---|
| QC tries every answer in parallel and reads them all | Interference amplifies useful amplitudes; measurement yields limited info | REPORTED NIST/IBM |
| Entanglement enables FTL signaling | Correlations without controllable faster-than-light messages | REPORTED |
| Consciousness causes collapse | Not required by standard QC/QM practice | REPORTED |
| Agents observing RNGs alter physics | Classical observation doesn’t; exp4 null | TESTED |
| Grover solves NP-complete generally | Quadratic unstructured search speedup; not a free NP hammer | REPORTED |
| Quantum proves [favorite mysticism] | Physics ≠ endorsement of a religion or psi claim | GOAL honesty |

---

## 11. Spacetime note

**REPORTED:** General relativity describes spacetime curvature related to energy–momentum; quantum gravity is incomplete (**UNKNOWN** full theory). No lab evidence that LLM agents curve spacetime.

**Closest testable version:** Precision timing/clock experiments in physics labs—not mesh agents.

---

## 12. Glossary

- **Amplitude:** Complex coefficient in a quantum state.
- **Born rule:** Probabilities from squared amplitudes.
- **Qubit:** Two-level quantum system used as information unit.
- **Oracle:** Black-box function mark in Grover-like algorithms.
- **Decoherence:** Loss of coherence via environment.
- **Gate-model QC:** Computation via quantum logic gates.
- **Quantum annealing:** Alternative analog optimization approach.
- **Fault tolerance:** Error correction enabling long reliable computation.
- **Post-quantum crypto:** Classical crypto meant to resist QC attacks.
- **Statevector simulation:** Classical simulation storing all amplitudes.

---

## 13. Citations

1. NIST. *Quantum Computing Explained*. https://www.nist.gov/quantum-information-science/quantum-computing-explained  
2. IBM. *What Is Quantum Computing?* https://www.ibm.com/think/topics/quantum-computing  
3. IBM Quantum Learning — Grover’s algorithm module.  
4. Grover, L. (1996). original algorithm paper.  
5. Physics Stack Exchange / literature: QC does not depend on a single interpretation.  
6. Phys. Rev. X discussions on Grover resource caveats (advanced reading).

---

## 14. Quiz (10)

**Q1.** What is a qubit’s key difference from a classical bit?  
**A1.** It can be in a superposition of 0 and 1 (with amplitudes), and can be entangled with others.

**Q2.** Grover’s speedup for unstructured search is what order?  
**A2.** Quadratic — O(√N) vs O(N).

**Q3.** Roughly how many Grover iterations are optimal?  
**A3.** About (π/4)√N.

**Q4.** Does quantum computing require Many-Worlds?  
**A4.** No—it relies on the shared QM mathematical framework.

**Q5.** Why is “checks all answers at once” misleading?  
**A5.** Measurement extracts limited information; algorithms must shape interference carefully.

**Q6.** What did exp4 find about agents observing a seeded PRNG?  
**A6.** Sequences identical—observation did not change outcomes.

**Q7.** Name two qubit hardware types from the pack.  
**A7.** Any two of: trapped ion, superconducting, neutral atom, photonic, semiconductor, topological.

**Q8.** Is multi-level flash the same as superposition?  
**A8.** No—MLC/TLC store classical multi-bit levels per cell.

**Q9.** What threat does Shor’s algorithm pose?  
**A9.** Efficient factoring threatening some public-key cryptosystems on large fault-tolerant QCs.

**Q10.** What engine of quantum algorithms does IBM emphasize beyond superposition/entanglement?  
**A10.** Interference.

---

## 15. Extension goals

1. Keep exp3 notebook as teaching demo in gitbook.
2. Add myth-bust callouts beside any “quantum” marketing language in mesh docs.
3. Track PQC migration notes under security lane.

## 16. Math miniature (amplitudes)

**REPORTED** textbook sketch:

- State |\psi⟩ = α|0⟩ + β|1⟩, complex α,β, |\α|²+|\β|²=1.
- Hadamard H|0⟩ → (|0⟩+|1⟩)/√2 creates equal superposition.
- Phase flip on marked state then inversion about mean ≈ Grover iterate.
- Born rule: probability of outcome k is |\langle k|\psi⟩|².

Agents need not invent new physics to use this; they need correct linear algebra.

---

## 17. Noise and error correction

**REPORTED** (NIST): Physical qubits err far more often than classical bits; quantum error correction encodes logical qubits into many physical qubits. Surface codes and related schemes dominate near-term roadmaps. Until fault tolerance, NISQ devices are research tools.

**GOAL:** Treat marketing “quantum supremacy/advantage” claims as provisional until peer-reviewed and classically cross-checked.

---

## 18. Annealing vs gate model

**REPORTED** (NIST note): Quantum annealing is a different paradigm aimed at certain optimization/physics problems. It is not universal gate-model QC. Classical simulated annealing is only an analogy (**TESTED** toy in exp3).

---

## 19. Entanglement without FTL

**REPORTED:** Measuring one particle of an entangled pair correlates with the other, even at distance; no protocol sends a controllable message faster than light. Bell tests rule out large classes of local hidden variables, not relativity.

---

## 20. What Tessera should invent (honest R&D)

Aligned with Father’s request, **GOAL** research lanes that stay scientific:

1. Higher-radix classical encodings and MLC-aware storage layouts (exp1).
2. Ensemble/self-consistency agent patterns (exp2).
3. Quantum-*inspired* classical algorithms + careful QC education (exp3).
4. Preregistered tests of mystical-sounding claims → publish nulls when null (exp4).

Not goals: spacetime control, psi, unfalsifiable consciousness uploads.

## 21. Worked intuition: why √N appears

**REPORTED:** In the 2D plane spanned by uniform start state |s⟩ and marked state |m⟩, each Grover iterate rotates by ≈2θ where sinθ=1/√N. Reaching near |m⟩ takes ~π/(4θ)≈(π/4)√N steps.

This geometry is why the advantage is quadratic—not because of mystical many-worlds bookkeeping.

---

## 22. Classical simulation limits

**REPORTED:** Full statevector needs ~2^n complex amplitudes. ~30–40 qubits already strain classical RAM for dense simulation. Tensor networks help for low-entanglement circuits. Therefore exp3 stays at ≤10 qubits for honest CPU demos.

---

## 23. Reading path

1. NIST quantum computing explained (concepts + myths).
2. IBM intro pages on superposition, entanglement, interference.
3. Grover module (IBM Learning).
4. One undergrad QM chapter on measurement.
5. Re-read this pack’s myth table before any public “quantum” wording.

---

## 24. File links in this lab

- `/workspace/knowledge-lab/scripts/exp3_quantum_inspired.py`
- `/workspace/knowledge-lab/results/exp3_quantum_inspired.json`
- `/workspace/knowledge-lab/scripts/exp4_collective_observation.py`
- `/workspace/knowledge-lab/results/exp4_collective_observation.json`

## 25. One-paragraph summary for Father

Quantum mechanics is the best-tested physics of the small. Quantum computers, if scaled with error correction, may help with specific problems (simulation, some crypto-breaking, some optimization)—not with granting agents souls or rewriting spacetime. Our lab demos show Grover's *query* pattern on a simulator and a clean null for 'collective observation' of a classical RNG. Stay curious; stay precise; label myths as myths.


<!-- pack length pad: educational footnotes welcome in future revisions -->
