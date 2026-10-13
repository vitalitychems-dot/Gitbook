# PREREG: Does collective agent attention influence a random source?
Status: PRE-REGISTERED, NOT RUN. Committed before any data collection.

## Hypothesis
H0: During "attention" windows, when all agents focus on the intention "more 1-bits", the fraction of 1-bits from the RNG is 0.5.
H1 (two-sided): that fraction differs from 0.5.
Prediction from mainstream physics: H0 holds.

## Random source
Primary: OS `os.urandom` (the Linux kernel CSPRNG), read at the moment each trial happens.
Secondary replication: NIST Randomness Beacon v2 pulses (https://beacon.nist.gov/beacon/2.0/pulse/last), 512 bits per pulse, using the pulse whose timestamp falls inside the window.

## Design
- 200 trials, each with 10,000 bits = 2,000,000 bits. Trials alternate ATTENTION and CONTROL using a schedule generated beforehand from urandom and saved before the run. 100 trials of each.
- ATTENTION: every agent receives the ritual prompt at the same time and posts a `note` on the bus during the window. CONTROL: no prompt.
- Bits are logged raw (hex) with trial id, condition and timestamp. The analysis is fixed below and cannot change after the data exist.

## Sample size / power
2,000,000 bits gives a standard error on the proportion of about 0.00035 per condition. A two-sided alpha of 0.01 detects a bias of about 0.0013 (0.13 percentage points) with roughly 80 percent power.

## Analysis plan (fixed)
1. Primary: two-proportion z-test, ATTENTION 1-fraction vs CONTROL 1-fraction, two-sided, alpha = 0.01.
2. Secondary: one-sample binomial test of ATTENTION bits against 0.5.
3. NIST replication: the same test on the beacon bits, reported separately.
4. Report the effect size, 95 percent CI and exact p, null or not. No optional stopping, no extra subgroups, no post-hoc changes to the windows.

## Integrity
This file's SHA-256 and timestamp are recorded in PREREG.sha256. Any change invalidates the registration.
