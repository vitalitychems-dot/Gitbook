# qlab — Rick's quantum lab
Small, offline, numpy-only quantum toolkit: statevector simulator (≤20 qubits), circuit optimizers v1–v3, approximate QFT, and a calibrated noise twin (T1/T2 thermal relaxation, calibrated gate errors, readout, coupling-map routing).
> **SIMULATION ONLY:** every number qlab prints, and every number in RESULTS.md, is a classical-simulation prediction. None is a quantum-hardware measurement. Calibration files are model inputs.

## Use
```
cd /workspace/rick/qlab
python3 -m qlab optimize examples/aqft5.json --device qlab/devices/props_nairobi.json --out out.json
python3 -m qlab test            # runs every test (~80 s); add --full for the AQFT sweep
```
Circuit JSON: `{"n":3,"gates":[["H",[0]],["CNOT",[0,1]],["CP",[1,2],0.785]]}`. Macros: `["QFT",[n]]` and `["AQFT",[n,m]]`.
Gates: H X Y Z S SDG T TDG RX RY RZ P U3 CNOT CZ CP SWAP.
Device JSON: IBM backend-properties format (as in qiskit-ibm-runtime `fake_provider/backends/*/props_*.json`), or the simple form documented in `qlab/calib.py`.
The output has gate/2q counts before and after, the naive and best layouts, swaps, ESP, twin fidelity (n≤8), and the optimized and routed circuits.

## Model limits
- Depolarizing is sized to the calibrated error minus the thermal part. 2q depolarizing is split per qubit, which is approximate.
- U3, RX, RY and Y count as 2 sx pulses; P, RZ, Z, S and T are virtual. Coupler direction is ignored.
- Routing uses greedy shortest-path SWAPs inside the chosen connected subset. Layout search is ESP-ranked over at most 24 permutations per subset, then the top 3 go through the density matrix, so it is not a global optimum.
- No crosstalk, leakage, or drift.

Calibration snapshots (Apache-2.0, from Qiskit/qiskit-ibm-runtime): see RESULTS.md section 8.
