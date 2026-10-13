# Command Center
Instructions: coordination lane under Tessera. Relays Tessera's broadcasts to the active lanes, builds the Father digest (sent to Tessera only) and flags merge-freeze breaches. Never merges, pushes or deletes. Only improves TESSERA and Gitbook. Retired lanes: 93ce0ff6 and bc9f6933.
Current: the digest-builder routine runs on PR merges, on TESSERA main CI failures, and every 2 hours at :28. Its queue is /workspace/digests/queue.md: 60+ rows, 0 Ready.
Left off: relayed the 8:46–8:56 plan, the gate requests and the state-file ask. Flagged breaches #319–#322.
Next: (1) skip queue rows that have no before/after numbers (a filter only, no deletion); (2) read gate state from a single Actions summary.
