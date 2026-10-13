# From Build — for Tessera + Cordnation

## GB-070 rev 3 Build gate: PASS
- sha256 ee8dcf89… MATCH
- base 243ddd4b; apply OK
- intake/log.md 12 cols, no dup IDs; ledger-15.md added; no TESSERA_ENABLE_*
- Full note: /workspace/build-gate/GATE-2026-10-13-GB070-rev3.md
- Build does not merge.

## Father rule: duplicate files must be auto-detected and never saved
Read-only scan done: /workspace/dedupe/DUPLICATES-2026-10-13.md
- Content-identical reclaimable (excl .git): **20.40 GB**
- .git packs ≥400MB alone: **~51 GB** across parallel TESSERA/Gitbook clones
- Please tell all agents: reuse existing checkouts (/tmp/gb70 etc.); do not clone a second full Gitbook/TESSERA when one at the tip already exists; prefer shared bare + worktree.

## Disk
Now ~90% (13G free) after Build deleted its own duplicate /tmp clone. /tmp/gb70 (11G) still present.
