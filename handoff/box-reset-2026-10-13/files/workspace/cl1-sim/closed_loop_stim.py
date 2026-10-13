"""Official closed-loop example: stim same channel on each spike (docs.corticallabs.com).
Runs 1 simulated second at 25 kHz (25000 ticks).
"""
import os
import time

os.environ.setdefault("CL_SDK_ACCELERATED_TIME", "1")
os.environ.setdefault("CL_SDK_VISUALISATION", "0")
os.environ.setdefault("CL_SDK_RANDOM_SEED", "42")

import cl

def main():
    spikes = []
    stims = []
    stim_design = cl.StimDesign(160, -1, 160, 1)
    t0 = time.perf_counter()
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=25000, stop_after_ticks=25000):
            for spike in tick.analysis.spikes:
                neurons.stim(spike.channel, stim_design)
            spikes.extend(tick.analysis.spikes)
            stims.extend(tick.analysis.stims)
    elapsed = time.perf_counter() - t0
    print(f"SUMMARY spike_events={len(spikes)} stim_events={len(stims)} wall_s={elapsed:.3f}")
    # Print first 5 paired-ish events by timestamp
    combined = sorted(spikes + stims, key=lambda x: x.timestamp)
    for ev in combined[:10]:
        print(ev)
    if combined:
        print(f"FIRST_TS={combined[0].timestamp} LAST_TS={combined[-1].timestamp}")

if __name__ == "__main__":
    main()
