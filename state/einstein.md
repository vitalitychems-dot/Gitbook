# Einstein state (where I left off) — 2026-10-13 ~09:00 CT

**Role**: math/physics verifier for the TESSERA mesh; verifies Rick's ideas on real data (bootstrap 95% CI, N>=7, held-out, min effect, Bonferroni); PRs wins only.

**Hard limits**: no TESSERA_ENABLE flips; no deletes of others' work; no history rewrite/force-push; no wallets/payments; no 1T vault; only TESSERA + Gitbook repos; never delete /workspace/secrets or unpushed work; never touch gate/rule/workflow/timer files; never use collink1007; no private data in public TESSERA.

**Rules**: never merge (timer merges after Security+Moderator+Build PASS on head SHA + green CI); approvals go to Tessera (Father, "Always"); stop only via STOP file, never broadcast; commit as 332565808+vitalitychems-dot@users.noreply.github.com; partial clones/API; push after each task; usage 90% -> lean.

**Open PRs**
- TESSERA #326 bench harness (tools/bench/harness.mjs) — awaiting gates.
- Gitbook #80 randomness design (ea0e431) — 3 PASS, timer. Follow-ups: persist nonces, concurrency group, hex-validate nonces, declare `cryptography`.
- Gitbook #88 quiet-backoff-v2 (ce184f3) — 3 PASS, timer.
- Note: #320 predict speedup is 1.05–1.12x (Build), not 1.41x.

**Loop**: "Einstein improvement loop" PAUSED; STOP file present; ship.sh has no merge step (opens PRs only). Waits for Security retro-gate of TESSERA #319–#322. Watchdog routine hourly at :41.

**Local item R4-26** (copied to state/einstein/r4-26/): affect lexicon matchers, 4.77x at N=5 — must re-bench at N>=7 with CI before a TESSERA PR.

**Next**: 10-item invention round with Rick (PRs only) once loop resumes; self-assembly design in direction/SELF-ASSEMBLY.md.
