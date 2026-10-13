# #12 Valvular one-way bus id dedup

- **id:** `valve_bus`
- **focus:** Tesla/collab
- **verdict:** **KEPT**

## Spec
Tesla-valve on collab JSONL: only first sighting of each message id forwards; replays blocked.

## Target
sample-bus + eye-shield-bus replayed 4× shuffled

## Metric
forwarded (↓)

## Baseline
naive 32/32 forwarded

## Measured result
valve 8/32 (−75%); 8 unique ids preserved.
