# BHNMC v1.3 — Unified Spec (Bio-Hybrid Neuromorphic Computing characterization platform)
Status: design spec + software simulation only. Nothing here has been built or tested on biology.
Goal: measure whether a living Physarum network on a graphene-oxide (GO) electrode mesh acts as a useful physical reservoir, and if the data supports it, have AI turn what it learns into a hardware architecture (FPGA first, then ASIC). Every unusual part is treated as a parameter to measure, not something assumed to work.

## 1. FACT (established science; cite primary sources before external use)
- F1 Physarum polycephalum does path optimization (shortest routes and networks) through decentralized shuttle streaming of cytoplasm, driven by local cues.
- F2 Graphene oxide is hydrophilic and biocompatible, supports charge transfer and biochemical functionalization, and is used as an electrochemical sensing material.
- F3 Femtosecond-laser writing changes local refractive index and birefringence in fused silica, which enables 5D long-term optical storage.
- F4 Multi-frequency AC excitation separates the real (R) and imaginary (X) parts of tissue impedance (impedance spectroscopy).

## 2. HYPOTHESIS (testable; each needs a pre-registered metric)
- H1 Physarum spatio-temporal dynamics act as a nonlinear reservoir that increases the separability of inputs. Metric: held-out-stimulus accuracy, memory capacity and NARMA NMSE versus a no-reservoir baseline, with the same readout.
- H2 The living Physarum on porous 3D GO interface shows history-dependent memristive I-V hysteresis. Metric: loop area versus sweep rate, compared with a cell-free GO control and a dead-cell control.
- H3 Quantum-inspired (QI) feature maps extract patterns a linear readout misses. Metric: QI versus matched-size random-feature and RBF baselines. QI must win to stay.
- H4 Pyroelectric harvesting of waste heat from nearby silicon can serve as a usable stimulus source. Metric: harvested µW and the stimulus response it produces, against a sham.
Twin requirement: x_{t+1}=F(x_t,u_t,G) must be validated on stimuli it was not trained on.

## 3. SPECULATIVE (vision only; never in investor claims)
- S1 Self-powered bio-cyborg computing networks.
- S2 Reich "orgone" is kept only as a historical idea. It becomes concrete, measurable shielding and field-control experiments (Faraday or mu-metal enclosure versus open, sham coils). No orgone claims.
- S3 Tesla-inspired field stimulation runs as ordinary branches of the M1–M8 coil experiments.

## 4. Mechanical stack (50 × 50 × 12.5 mm)
|Layer|Function|Thickness mm|Z from mm|
|-|-|-|-|
|L1|PCB (AFE, MUX, MCU header)|1.5|0.0–1.5|
|L2|Actuators: coils M1–M8, hall sensor, LEDs|2.0|1.5–3.5|
|L3|GO 8×8 electrode cartridge|4.0|3.5–7.5|
|L4|Fluidics/medium chamber|2.0|7.5–9.5|
|L5|Quartz cap/optical window|3.0|9.5–12.5|
Sum = 12.5 mm (verified). O-ring groove r = 21–23 mm. Ports: inlet (−22, 0) and outlet (+22, 0). **See the geometry issues in RESULTS.md: ports and corner electrodes conflict with the seal.**

## 5. Coils
|Coil|X|Y|r|
|-|-|-|-|
|M1|−18|+18|25.46|
|M2|0|+20|20.00|
|M3|+18|+18|25.46|
|M4|+20|0|20.00|
|M5|+18|−18|25.46|
|M6|0|−20|20.00|
|M7|−18|−18|25.46|
|M8|−20|0|20.00|

## 6. Electrode CAD table (4.5 mm pitch; row 1 at Y = +15.75, column 1 at X = −15.75; computed by geometry.py)
|ID|X mm|Y mm|r mm|
|-|-|-|-|
|E01|-15.75|+15.75|22.27|
|E02|-11.25|+15.75|19.36|
|E03|-6.75|+15.75|17.14|
|E04|-2.25|+15.75|15.91|
|E05|+2.25|+15.75|15.91|
|E06|+6.75|+15.75|17.14|
|E07|+11.25|+15.75|19.36|
|E08|+15.75|+15.75|22.27|
|E09|-15.75|+11.25|19.36|
|E10|-11.25|+11.25|15.91|
|E11|-6.75|+11.25|13.12|
|E12|-2.25|+11.25|11.47|
|E13|+2.25|+11.25|11.47|
|E14|+6.75|+11.25|13.12|
|E15|+11.25|+11.25|15.91|
|E16|+15.75|+11.25|19.36|
|E17|-15.75|+6.75|17.14|
|E18|-11.25|+6.75|13.12|
|E19|-6.75|+6.75|9.55|
|E20|-2.25|+6.75|7.12|
|E21|+2.25|+6.75|7.12|
|E22|+6.75|+6.75|9.55|
|E23|+11.25|+6.75|13.12|
|E24|+15.75|+6.75|17.14|
|E25|-15.75|+2.25|15.91|
|E26|-11.25|+2.25|11.47|
|E27|-6.75|+2.25|7.12|
|E28|-2.25|+2.25|3.18|
|E29|+2.25|+2.25|3.18|
|E30|+6.75|+2.25|7.12|
|E31|+11.25|+2.25|11.47|
|E32|+15.75|+2.25|15.91|
|E33|-15.75|-2.25|15.91|
|E34|-11.25|-2.25|11.47|
|E35|-6.75|-2.25|7.12|
|E36|-2.25|-2.25|3.18|
|E37|+2.25|-2.25|3.18|
|E38|+6.75|-2.25|7.12|
|E39|+11.25|-2.25|11.47|
|E40|+15.75|-2.25|15.91|
|E41|-15.75|-6.75|17.14|
|E42|-11.25|-6.75|13.12|
|E43|-6.75|-6.75|9.55|
|E44|-2.25|-6.75|7.12|
|E45|+2.25|-6.75|7.12|
|E46|+6.75|-6.75|9.55|
|E47|+11.25|-6.75|13.12|
|E48|+15.75|-6.75|17.14|
|E49|-15.75|-11.25|19.36|
|E50|-11.25|-11.25|15.91|
|E51|-6.75|-11.25|13.12|
|E52|-2.25|-11.25|11.47|
|E53|+2.25|-11.25|11.47|
|E54|+6.75|-11.25|13.12|
|E55|+11.25|-11.25|15.91|
|E56|+15.75|-11.25|19.36|
|E57|-15.75|-15.75|22.27|
|E58|-11.25|-15.75|19.36|
|E59|-6.75|-15.75|17.14|
|E60|-2.25|-15.75|15.91|
|E61|+2.25|-15.75|15.91|
|E62|+6.75|-15.75|17.14|
|E63|+11.25|-15.75|19.36|
|E64|+15.75|-15.75|22.27|

## 7. Pinout (46 pins)
|Pins|Signal|
|-|-|
|1–4|Power (VIN, 3V3, AGND, DGND)|
|5–20|MUX address/enable (4 MUX × 4 bits)|
|21|AFE excitation (AD5940 CE0)|
|22|AFE sense (AD5940 SE0)|
|23–30|Coil PWM M1–M8|
|31|Hall sensor|
|32–35|Optical PWM (4 LED channels)|
|36–37|Valves (inlet, outlet)|
|38–39|I2C SDA/SCL (temperature, humidity)|
|40–43|SPI (AD5940: SCLK, MOSI, MISO, CS)|
|44–45|Ledger UART TX/RX|
|46|Sync/trigger|
AFE: AD5940 plus 4× 16:1 MUX = 64 channels. (The old diagram's "dual ADG706" gives only 32 channels and is superseded.)

## 8. Data and models
State map X(t, f, e): time × excitation frequency × electrode, with R and X at each point. Model tournament on the same splits: ESN, GRU, GNN (electrode adjacency), SNN, Neural ODE, and hybrids. Every model is compared against a no-reservoir baseline (the same readout on raw stimulus features). The QI branch must beat matched-size classical random features or it gets dropped. Archive: hashed ledger over UART. A quartz 5D archive is outsourced and optional.

## 9. Prototype generations
- **A, electronic testbed:** dummy RC/memristor loads in place of biology. Validates the AFE, MUX, coils and the twin pipeline.
- **B, biological:** Physarum on GO, sealed chamber, controls (no cells, dead cells, bare electrode, sham field).
- **C, autonomous:** closed loop with AI-designed geometry, 3D-printed cartridges and automated experiment scheduling.

## 10. Safety
- No blood or human or animal tissue.
- No N2O or other pressurized or anesthetic gases in the home chamber.
- Coil current limits and a thermal cutoff (≤ 40 °C at the chamber).
- Low-voltage (≤ 5 V) excitation only.
- Biological waste is autoclaved or bleached.
- No laser writing at home; fs-laser work is outsourced.

## 11. Benchmarks
- Classification on held-out stimulus families (accuracy, mean ± std over seeds and folds).
- Memory capacity (sum of r² for delays 1–40).
- NARMA-10 NMSE.
- Twin one-step and free-run NMSE on unseen stimuli.
- Hysteresis loop area.
- Energy per inference (J).
- Latency.
- Drift per hour.
- All of the above against CPU, GPU and FPGA software ESNs of matched size.

End goal: an AI-discovered architecture that can be reproduced in FPGA or ASIC. Claim nothing to investors beyond measured results.
