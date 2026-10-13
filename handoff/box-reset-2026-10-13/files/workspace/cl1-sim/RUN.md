# CL1 simulator run log (Tessera mesh prep)

**Operator:** Tessera (admin coordinator) for Father (Collin Keane)  
**When:** 2026-10-05 ~5:38–5:39 PM CT  
**Labels:** TESTED = executed on this box · REPORTED = backed by public URL · GOAL = Father/mesh intent · BLOCKED = stopped (none here)

## Goal

**GOAL** — Use the Cortical Labs CL1 training/simulator path (`cl-sdk`) as Father directed at 5:38 PM CT, 2026-10-05: local closed-loop study only; no Cloud signup, no hardware purchase, no credentials.

## Key URLs (REPORTED)

| What | URL |
| --- | --- |
| Developer Guide / CL API docs | https://docs.corticallabs.com/ |
| PyPI package `cl-sdk` | https://pypi.org/project/cl-sdk/ |
| GitHub simulator source | https://github.com/Cortical-Labs/cl-sdk |
| Jupyter API walk-through notebooks | https://github.com/Cortical-Labs/cl-api-doc |
| CL1 product page | https://www.corticallabs.com/cl1 |
| Cortical Cloud (not used; signup required) | https://corticallabs.com/cloud |
| Purchase page (not used) | https://corticallabs.com/purchase |
| License text (CC BY-NC 4.0) | https://github.com/Cortical-Labs/cl-sdk/blob/main/LICENSE |
| CL API whitepaper (arXiv) | https://arxiv.org/pdf/2602.11632 |
| Gitbook readiness GB-019 | `intake/CORTICAL-LABS-READINESS.md` @ `bc6b32871faed56b13df3dfadc849ec725d60f14` |

## What the simulator models (REPORTED)

From https://docs.corticallabs.com/ and https://github.com/Cortical-Labs/cl-sdk:

- **Spikes / samples:** randomly generated Poisson-like data (default) or replay from an HDF5 recording (`CL_SDK_REPLAY_PATH`).
- **Stimulation API:** same `neurons.stim(...)` / `StimDesign` / `BurstDesign` / stim plans as on-device CL API.
- **Closed-loop:** `neurons.loop(ticks_per_second=..., stop_after_seconds|ticks=...)` exposes `tick.analysis.spikes` and `tick.analysis.stims` each tick (up to 25 kHz on hardware contract).
- **Critical limitation (REPORTED):** Simulator produces **non-learning control data that does not respond to stimulation**. Docs: use only for baseline/control plumbing; not for experimental conclusions about living neurons.
- **Timing modes:** wall-clock (default) or accelerated (`CL_SDK_ACCELERATED_TIME=1`).
- **Jitter:** on-device loop raises `TimeoutError` on budget overrun; simulator warns that jitter detection is unsupported.
- **License (REPORTED):** CC BY-NC 4.0 (non-commercial). Pip install did not require interactive license acceptance, account, waitlist, or payment. Commercial redistribution would need a different grant from Cortical Labs.

## Environment (TESTED)

```
python 3.13.5
cl-sdk==1.0.0
numpy==2.5.3
scipy==1.18.1
tables==3.11.1
pydantic==2.13.5
websockets==17.2
matplotlib==3.11.2
pandas==3.0.6
```

Venv: `/workspace/cl1-sim/.venv`  
Working dir: `/workspace/cl1-sim/`  
`.env` used:

```
CL_SDK_ACCELERATED_TIME=1
CL_SDK_VISUALISATION=0
CL_SDK_RANDOM_SEED=42
```

## Install commands (TESTED)

```bash
mkdir -p /workspace/cl1-sim
cd /workspace/cl1-sim
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install cl-sdk
# Result: Successfully installed ... cl-sdk-1.0.0 ...
```

Full pip transcript: `install.log`.

## Examples run (TESTED)

### 1) `hello_spikes.py` — detect spikes (docs quick-start pattern)

Command:

```bash
source /workspace/cl1-sim/.venv/bin/activate
cd /workspace/cl1-sim
python hello_spikes.py
```

Real output (abbreviated; full in `hello_spikes.out`):

```
Warning: Jitter detection is currently not supported in cl-sdk. ...
Spike(timestamp=10, channel=40)
Spike(timestamp=60, channel=11)
Spike(timestamp=240, channel=61)
Spike(timestamp=252, channel=41)
Spike(timestamp=505, channel=8)
SUMMARY spikes=159 unique_channels=55 first_ts=10 last_ts=49827 wall_s=2.085
Random data source is using seed: 42
```

Interpretation: 2 simulated seconds @ 1000 ticks/s yielded **159** spike events across **55** channels (seed 42). Wall clock ~2.085 s even with accelerated-time env set (accel still incurred startup/producer cost).

### 2) `closed_loop_stim.py` — official closed-loop stim-on-spike (docs 25 kHz example)

Command:

```bash
python closed_loop_stim.py
```

Real output (abbreviated; full in `closed_loop_stim.out`):

```
Warning: Jitter detection is currently not supported in cl-sdk. ...
SUMMARY spike_events=75 stim_events=75 wall_s=4.327
Spike(timestamp=296, channel=28)
Stim(timestamp=299, channel=28)
Spike(timestamp=493, channel=59)
Stim(timestamp=496, channel=59)
...
FIRST_TS=296 LAST_TS=24724
Random data source is using seed: 42
```

Interpretation: 25000 ticks (1 simulated second @ 25 kHz) produced **75** spikes and **75** matching stims; stim timestamps trail spike timestamps by ~3 sample units on the printed pairs. Wall ~4.327 s.

### Not run

- Full Jupyter notebooks from `cl-api-doc` (would require `git clone` + jupyterlab; core closed-loop contract already exercised as scripts).
- Recording → `RecordingView` round-trip (optional; not needed for smoke).
- Cortical Cloud / physical CL1 (**BLOCKED** by policy: signup/purchase/credentials).

## Scripts saved

- `/workspace/cl1-sim/hello_spikes.py`
- `/workspace/cl1-sim/closed_loop_stim.py`
- `/workspace/cl1-sim/.env`
- Capture files: `hello_spikes.out`, `closed_loop_stim.out`, `install.log`

## Status

**TESTED** — Simulator installed and closed-loop example ran successfully on this box with the numbers above. No account, no spend, no credentials.
