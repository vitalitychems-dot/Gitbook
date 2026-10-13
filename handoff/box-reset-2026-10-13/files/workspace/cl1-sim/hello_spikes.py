"""Official-style hello: detect spikes for 2 seconds (docs.corticallabs.com)."""
import os
import time

# Local simulator knobs (documented in cl-sdk README / docs.corticallabs.com)
os.environ.setdefault("CL_SDK_ACCELERATED_TIME", "1")
os.environ.setdefault("CL_SDK_VISUALISATION", "0")
os.environ.setdefault("CL_SDK_RANDOM_SEED", "42")

import cl

def main():
    spike_count = 0
    channels = set()
    first_ts = None
    last_ts = None
    t0 = time.perf_counter()
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=1000, stop_after_seconds=2):
            for spike in tick.analysis.spikes:
                spike_count += 1
                channels.add(spike.channel)
                if first_ts is None:
                    first_ts = spike.timestamp
                last_ts = spike.timestamp
                if spike_count <= 5:
                    print(spike)
    elapsed = time.perf_counter() - t0
    print(f"SUMMARY spikes={spike_count} unique_channels={len(channels)} "
          f"first_ts={first_ts} last_ts={last_ts} wall_s={elapsed:.3f}")

if __name__ == "__main__":
    main()
