# Held-out eval set (private)
Scoring data for the TESSERA held-out runner (`TESSERA/evals/heldout/run.mjs`). Kept here, in the
private repo, so items and answers are not public and agents in the public repo can't edit them.
No item is agent-authored: public benchmarks plus real TESSERA PR outcomes. See LICENSES.md.
`MANIFEST.sha256` pins every data file; the runner fails closed on any mismatch.
Run: `HELDOUT_DIR=$PWD/evals/heldout node <TESSERA>/evals/heldout/run.mjs --baseline`.
Locked: changes need Father's code-owner review.
