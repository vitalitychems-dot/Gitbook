# Code index

Reusable research code under `research/code/`, plus related scripts already in `/workspace/knowledge-lab/scripts/`. Status labels follow `README.md`. Every `research/code/` script has a paired test file; pass/fail counts are from real runs on this box (America/Chicago).

**Caveat (global):** Finite verification and toy simulations are not proofs of open conjectures.

---

## research/code/ (this section)

### CI-001 — `goldbach_verify.py`

| Field | Value |
|-------|--------|
| **Purpose** | Verify Goldbach’s conjecture (every even n = p+q for primes p,q) for all even n in [4, LIMIT] via sieve of Eratosthenes. |
| **How to run** | `python3 research/code/goldbach_verify.py --limit 1000000` |
| **Log** | `research/code/goldbach_verify.log` |
| **Tests** | `python3 research/code/test_goldbach_verify.py` → log `test_goldbach_verify.log` |
| **Test result** | **passed=4 failed=0 total=4** (sieve primes ≤30; all even ≤100; partition check; all even ≤1000) |
| **Experiment result (LIMIT=10^6)** | even_numbers_checked=499999; all_verified=True; failures=[]; primes≤10^6=78498; hardest_example=(503222, 523, 502699); sieve_seconds=0.1045; check_seconds=0.5554; **total_seconds=0.66** |
| **Status** | **TESTED** |
| **Caveat** | Finite range only; not a proof. Weak Goldbach is proven (Helfgott); strong form remains open. |

### CI-002 — `collatz_max_stopping.py`

| Field | Value |
|-------|--------|
| **Purpose** | Find maximum Collatz stopping time (steps to 1) for starting values in [1, LIMIT], with memoization. |
| **How to run** | `python3 research/code/collatz_max_stopping.py --limit 1000000` |
| **Log** | `research/code/collatz_max_stopping.log` |
| **Tests** | `python3 research/code/test_collatz_max_stopping.py` → log `test_collatz_max_stopping.log` |
| **Test result** | **passed=5 failed=0 total=5** (n=1; **stopping time of 27 = 111**; max≤10 is 19 at 9; max≤27 is 111 at 27; max≤100 matches brute force) |
| **Experiment result (LIMIT=10^6)** | **max_stopping_time=524**; **argmax_start=837799**; cache_size=2168611; **total_seconds=1.3337** |
| **Status** | **TESTED** |
| **Caveat** | Finite search only; not a proof of the Collatz conjecture. |

### Test policy (Father, 2026-10-05)

- Every new script in `research/code/` must include `test_<stem>.py` with asserts against known values.
- Run tests as you build; record pass/fail in this index before claiming TESTED.
- Stdlib or numpy only unless a later item explicitly expands the stack.

---

## Related: `/workspace/knowledge-lab/scripts/` (pre-existing lab)

These are outside `research/code/` but part of the same knowledge-lab tree. Indexed for discoverability; re-run status not refreshed in this draft unless noted.

| ID | Path | Purpose | How to run (typical) | Results artifact | Status note |
|----|------|---------|----------------------|------------------|-------------|
| CI-L01 | `scripts/exp1_multivalued_encoding.py` | Compare multi-radix encodings on Gitbook sample text; density/speed. | `python3 scripts/exp1_multivalued_encoding.py` | `results/exp1_multivalued_encoding.json` | Prior lab run present (REPORTED from existing JSON; not re-executed in this research draft). |
| CI-L02 | `scripts/exp2_self_consistency.py` | Self-consistency / majority vote on a small GSM8K subset. | `python3 scripts/exp2_self_consistency.py` (needs Ollama/client) | (no `results/exp2_*.json` in tree at index time) | UNKNOWN / possibly BLOCKED without model endpoint. |
| CI-L03 | `scripts/exp3_quantum_inspired.py` | Grover (numpy statevector) vs classical; simulated annealing vs random. | `python3 scripts/exp3_quantum_inspired.py` | `results/exp3_quantum_inspired.json` | Prior lab JSON present (REPORTED from artifact). |
| CI-L04 | `scripts/exp4_collective_observation.py` | Preregistered null test: software “observation” of seeded RNG. | `python3 scripts/exp4_collective_observation.py` | `results/exp4_collective_observation.json` | Prior lab JSON present (REPORTED from artifact). |
| CI-L05 | `scripts/ollama_client_seeded.py` | Helper: Ollama client with per-call seed. | import from exp2 | — | Support module; not a standalone experiment. |

Agents adding lab scripts into the research catalog should either move/copy under `research/code/` with tests or link them here with honest status.

---

## Summary table (research/code only)

| ID | Script | Tests | Experiment | Status |
|----|--------|-------|------------|--------|
| CI-001 | goldbach_verify.py | 4/4 pass | 4..10^6 all verified in 0.66 s | TESTED |
| CI-002 | collatz_max_stopping.py | 5/5 pass | max 524 at 837799 (≤10^6) in 1.3337 s | TESTED |
