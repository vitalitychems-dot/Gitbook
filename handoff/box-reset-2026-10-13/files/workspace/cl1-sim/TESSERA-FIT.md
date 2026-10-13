# Tessera ↔ CL1 / cl-sdk fit note

**When:** 2026-10-05 ~5:39 PM CT  
**Cross-ref:** Gitbook GB-019 `intake/CORTICAL-LABS-READINESS.md` @ `bc6b32871faed56b13df3dfadc849ec725d60f14`  
**Companion run log:** `/workspace/cl1-sim/RUN.md`  
**Labels:** TESTED / REPORTED / GOAL / BLOCKED as below. No code merged to TESSERA or Gitbook.

---

## Fit summary

### What a Tessera component could realistically do (GOAL + REPORTED)

With **simulator-only** access (Father's 5:38 PM CT directive):

1. **Closed-loop experiment runner (Python adapter)** — Wrap `cl.open()` + `neurons.loop(...)` to drive stimulus–response protocols (spike → stim, bursting, stim plans). Same code shape ports to physical CL1 / Cloud later with minimal change (**REPORTED**: docs claim 1:1 API parity — https://docs.corticallabs.com/).
2. **Data logging / recording bridge** — Call `neurons.record()` and optionally `create_data_stream(...)` to write HDF5 (+ custom streams, e.g. game state / mesh telemetry). Load with `RecordingView` for offline analysis.
3. **Adapter interface for the mesh** — A thin Python service (or subprocess) that Tessera's TypeScript API talks to over local IPC/HTTP, exposing: open/close session, start/stop loop, enqueue stim, stream spike summaries, export recording paths. Keeps CL SDK out of the Node process.
4. **Baseline / control harness** — Use random or replay data sources (`CL_SDK_REPLAY_PATH`, `cl.sim.set_simulator_data_source`) to dry-run timing, serialization, and UI before any live wetware (**REPORTED** limitation: sim does not learn or respond to stim).

### What it cannot / must not do (REPORTED + GOAL)

- **Not an LLM training platform.** CL1 / `cl-sdk` do not train Tessera's language model, weights, or tokenizers. No gradient descent, no backprop through neurons in the public API.
- **Simulator ≠ experimental biology.** Docs state sim data is **non-learning control data that does not respond to stimulation** — must not be used to claim learning, intelligence, consciousness, or mesh “self-improvement” from sim runs (https://docs.corticallabs.com/).
- **Not a drop-in for Tessera web architecture.** CL API is Python, real-time (µs–ms loops up to 25 kHz); Tessera HTTP request/response is a different latency domain. Needs a bridge process, not a direct route handler calling `cl` inside Express.
- **No autonomous recursive self-modification.** Mesh policy (GB-019): recursive improvement limited to Moderator-passed docs with Father digest yes.
- **License caution (REPORTED):** `cl-sdk` is **CC BY-NC 4.0** — non-commercial. Mesh study/local use is fine under NC; any commercial product embedding needs Cortical Labs commercial terms (https://github.com/Cortical-Labs/cl-sdk/blob/main/LICENSE).
- **Cloud / hardware still out of scope here:** Cortical Cloud signup and CL1 purchase remain **BLOCKED** without Father budget/account decisions (URLs: https://corticallabs.com/cloud , https://corticallabs.com/purchase).

---

## Minimal adapter interface proposal (no code merged)

Sketch only — for a future Father-approved digest item:

```
CL1Adapter (Python, runs in /workspace/cl1-sim/.venv or CL1/Cloud later)
  open(session_id, mode=sim|device) -> Session
  close(session_id)
  run_loop(session_id, ticks_per_second, stop_after_seconds|ticks, on_tick_callback_id)
  stim(session_id, channels, StimDesign|int, BurstDesign?=None)
  start_recording(session_id, file_location?=cwd) -> recording_id
  stop_recording(recording_id) -> path
  create_data_stream(session_id, name, attributes) -> stream_id
  append_stream(stream_id, timestamp, payload)
  get_spike_summary(session_id) -> {count, channels, last_ts}   # polled or websocket

Tessera side (TypeScript, api-server):
  POST /cl1/sessions          # start adapter subprocess / attach
  POST /cl1/sessions/:id/loop # configure closed-loop job
  POST /cl1/sessions/:id/stim
  GET  /cl1/sessions/:id/spikes
  POST /cl1/sessions/:id/record/{start|stop}
  # No TESSERA_ENABLE_* flags; explicit boot only; no secrets in this layer
```

Success smoke (minimum Father could accept later): **TESTED**-style numbers — N spikes, M stims, recording file present — without asserting learning.

---

## GB-019 open questions — resolutions from this run

| # | GB-019 item | Status after this job |
| --- | --- | --- |
| 1 | Father preferred access path | **REPORTED (Father directive):** Simulator study only for now — “Use the cl1 training simulator.” (2026-10-05 5:38 PM CT). Cloud/hardware still deferred. |
| 2 | Budget / account ownership if Cloud or hardware | Still **UNKNOWN** / not opened. Cloud signup URL if needed later: https://corticallabs.com/cloud |
| 3 | Single mesh owner for future HYB implementation | Still **UNKNOWN** (process). This job owned by Tessera admin for simulator intake only. |
| 4 | Recursive improvement bounds | Unchanged **GOAL** — docs/skills with Moderator + Father digest yes only. |
| 5 | Minimum success test for first contact | **PROPOSED from TESTED run:** reproduce `closed_loop_stim.py` metrics (spike_events ≈ stim_events; seedable) and log to RUN.md; no learning claims. |
| — | Whether TS apps can talk to CL API without bridge | Still **UNKNOWN** for production, but **REPORTED** CL API is Python-only public surface → bridge is the realistic path. |
| — | Simulator freely installable? | **TESTED:** yes via `pip install cl-sdk` (v1.0.0), Python ≥3.12, no account. License CC BY-NC 4.0. |
| — | What sim models | **REPORTED + TESTED:** spikes/samples (random or replay), stim API, closed-loop loop; stim does **not** alter sim spike generation. |
| — | Price / Cloud tiers | Still **UNKNOWN** for current quote; press figures remain as in GB-019 (IEEE Spectrum). |

---

## Proposed improvement-ledger items (DO NOT edit LEDGER.md)

Same column format as `/workspace/improvements/LEDGER.md`. Status left `PROPOSED`. IDs are suggestions for the next free IMP-* slots after the current seed (IMP-030+); coordinator should renumber on ingest.

| ID | Lane | Repo | Path(s) | Change (one line) | Why | Evidence | Moderator | Tessera | Security | Build | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IMP-031 | Tessera (seed) | Gitbook | `intake/CORTICAL-LABS-READINESS.md` | Record Father 2026-10-05 5:38 PM CT simulator-only path; cite local RUN.md spike/stim smoke (159 spikes / 75+75 closed-loop) | GB-019 Q1 now answered by Father directive + TESTED install | TESTED: `/workspace/cl1-sim/RUN.md`; Father utterance; `cl-sdk==1.0.0`; docs https://docs.corticallabs.com/ | | | | | PROPOSED |
| IMP-032 | Tessera (seed) | Gitbook | `intake/CORTICAL-LABS-READINESS.md`; `SUMMARY.md` | Add REPORTED note: `cl-sdk` license is CC BY-NC 4.0; commercial mesh product needs separate Cortical Labs grant | Avoid accidental commercial redistribution of simulator | REPORTED: https://pypi.org/project/cl-sdk/ License field; https://github.com/Cortical-Labs/cl-sdk/blob/main/LICENSE | | | | | PROPOSED |
| IMP-033 | Tessera (seed) | Gitbook | `intake/HYBRID-CONSOLIDATION-BACKLOG.md` (or new HYB stub) | Add backlog stub “CL1 adapter interface (Python bridge + api-server routes)” gated on Father digest; no code yet | Captures TESSERA-FIT adapter proposal without merging code | TESTED fit note `/workspace/cl1-sim/TESSERA-FIT.md`; GB-019 §(b) UNKNOWN bridge | | | | | PROPOSED |
| IMP-034 | Tessera (seed) | Gitbook | `intake/CORTICAL-LABS-READINESS.md` | Document minimum success test: closed-loop stim-on-spike with seedable counts; forbid learning/AGI claims from simulator | Closes GB-019 Q5 with a concrete, non-overclaiming bar | TESTED: `closed_loop_stim.py` → spike_events=75 stim_events=75; docs non-learning warning https://docs.corticallabs.com/ | | | | | PROPOSED |

---

## Key URLs (quick list)

- https://docs.corticallabs.com/
- https://pypi.org/project/cl-sdk/
- https://github.com/Cortical-Labs/cl-sdk
- https://github.com/Cortical-Labs/cl-api-doc
- https://www.corticallabs.com/cl1
- https://arxiv.org/pdf/2602.11632
