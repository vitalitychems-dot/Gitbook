# EQ / physiology / neuroscience learning plan (cycle 1). Open data only, verify the license before any use.
| Dataset | What | License (check the source) | Size | Status |
|---|---|---|---|---|
| GoEmotions (google-research) | 58k Reddit comments, 27 emotions + neutral | Apache-2.0 | ~4MB tsv | **Used**: baseline in empathy.py |
| EmpatheticDialogues (Meta) | 25k empathetic conversations, 32 emotions | CC BY-NC 4.0 (non-commercial) | ~28MB | next: response-empathy eval |
| DailyDialog | 13k dialogues with emotion labels | CC BY-NC-SA 4.0 | ~5MB | next |
| WESAD (UCI) | Wearable stress/affect physiology (ECG, EDA, resp) | CC BY 4.0 (UCI) | ~2GB, too big: use summary features only | later, needs disk |
| PhysioNet open-access sets (e.g. MIT-BIH Arrhythmia, Fantasia) | ECG / HRV | ODC-By / PhysioNet open licences, per dataset | 10s-100s MB | single records only (<50MB) |
| Allen Brain Observatory / Cell Types | Neuron morphology and electrophysiology | Allen Institute terms of use (free for research) | API, small slices | read the docs only |
| OpenNeuro | fMRI/EEG (BIDS) | mostly CC0 | large | metadata only |
Curriculum: (1) emotion recognition (GoEmotions macro-F1), (2) empathetic response ranking (EmpatheticDialogues), (3) physiology→arousal (HRV from PhysioNet), (4) neuroscience concepts via the palace (Allen docs). Each step is gated by a held-out metric. Out of scope: secret-society "secrets" (nothing verifiable to measure); public esoteric and historical texts (Project Gutenberg, public domain) can go in the palace as a history/philosophy room.
