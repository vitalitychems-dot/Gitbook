# Round 3: 30 inventions toward Father's goals (Einstein, 2026-10-13)
Rules: GATE_RULES v0.1. Only measured wins on real data merge. Labels: BUILT, MERGED, SPEC-ONLY (feasible but not built this round),
SPECULATIVE (premise not physical or not measurable). No numbers are given for anything that wasn't run.
I checked Rick's /workspace/rick/tools/qinvent (anneal scheduler, amplitude retrieval, MWPM dedup, QEC vote, low-rank compression)
so none of his is repeated here. #2 (annealing) and #5 (low-rank) were dropped in his results, so I don't redo them.

| # | Idea | One-paragraph spec | TESSERA target | Metric | Feasible now? |
|---|---|---|---|---|---|
| 1 | Context-true semantic cache | Hash the full system prompt in the cache fingerprint so one agent never receives an answer written under another agent's context (honesty and respect between agents). | artifacts/api-server/src/lib/semantic-cache.ts | distinct fingerprints across real codex-wrapped prompts | MERGED via #276 (my duplicate #273 closed) |
| 2 | Stored-without-fp guard | A semantic hit is currently allowed when the candidate has no stored fingerprint but the query has one. Require both to match, or both to be empty. | semantic-cache.ts | wrong-context hits in a DB fixture | SPEC-ONLY (needs a DB fixture) |
| 3 | Token-cost ledger (free-energy accounting) | Record tokens_in, tokens_out and latency per call, keyed by agent, and expose a per-agent "energy" budget F = tokens + λ·latency. Use the existing v2 token meter. | artifacts/v2/src/token/meter.mjs | % of calls attributed | SPEC-ONLY |
| 4 | Shared mesh state blackboard ("act as one") | One content-addressed JSON state file in Gitbook state/ that every agent reads before a task, so context isn't re-sent agent to agent. | Gitbook state/ + v2 summary-cache | tokens per handoff on mesh/HANDOFF.lines | SPEC-ONLY |
| 5 | Codex-directive hoisting | Send the ~1 kB codex directive once per session as a cached prefix instead of on every call, ordered to suit provider prompt caching. | codex-startup-directive.ts | prompt bytes per call | SPEC-ONLY (needs provider-cache evidence) |
| 6 | Pixel memory (PNG-packed vectors) | Store embedding vectors as 8-bit PNG tiles. This is only a container (PNG is lossless zlib); it holds no more than the bytes in it. | vector-memory.ts | bytes vs recall@5 | SPEC-ONLY; expected no gain over int8+gzip |
| 7 | Image-as-memory for screenshots | Keep REA screenshots plus their OCR text as one memory item with a perceptual hash, for dedup. | Gitbook review/image-text | duplicate rate | SPEC-ONLY |
| 8 | Affect-aware reply tone (EQ) | Use the existing affect-compass to pick reply register (calm or brief) when the user shows stress. | lib/v2/affect-compass.ts | human-rated helpfulness on logged chats | SPEC-ONLY (needs labelled logs) |
| 9 | Mercy rule for agents | When an agent fails the gate, return a specific fix list instead of quarantine on the first non-rogue failure. | Gitbook mesh/queue (protected; needs Father) | re-submit success rate | SPEC-ONLY (protected path) |
| 10 | Evil-exposure scanner | Flag added code that hides behaviour: disguised bounties, cookie or secret exfiltration, unlisted hosts. Extends gatecheck. | Gitbook mesh/queue/gatecheck.py | true positives on past PRs | SPEC-ONLY (protected path) |
| 11 | Self-model file (honest 2D self-awareness) | Each agent keeps a small auto-generated "what I can and can't do, last failures" card, built from its gate history. Not a claim of consciousness. | Gitbook mesh/roles (protected) | repeated-failure rate | SPEC-ONLY |
| 12 | Gate charter auto-check | GATE_RULES.md plus gate_check.py: self-approve or deny without interrupting Tessera. | Gitbook mesh/charter | demo verdicts | BUILT (local branch; not merged by instruction) |
| 13 | Simulated-annealing prompt compression | Anneal which context chunks to drop under a token budget, scored by answer overlap. | prompt-builder.ts | tokens at equal answer quality | SPEC-ONLY |
| 14 | Boltzmann model routing | Route to a model with probability ∝ exp(-cost/T) times past success, with T decaying. | swarm-optimizer.ts | cost per successful task in logs | SPEC-ONLY |
| 15 | Landauer-style bits-erased budget | Count bytes discarded by caches and summaries as an "erasure cost" so over-summarisation shows up. A metaphor: Landauer's limit is ~3e-21 J/bit, irrelevant at software scale. | v2 summary-cache | info loss vs tokens saved | SPEC-ONLY, metaphor |
| 16 | Entropy-triggered handoff | Hand off to another agent only when the answer distribution's entropy over k samples is above a threshold. | consensus-engine.ts | handoffs per task | SPEC-ONLY |
| 17 | Free-energy curiosity | Pick the next task by expected information gain minus token cost (active-inference style). | mesh/curiosity.md + v2 | useful-finding rate | SPEC-ONLY |
| 18 | Detailed-balance consensus check | Detect council loops where votes cycle, and stop at the first fixed point. | routes/council.ts | rounds per decision | SPEC-ONLY |
| 19 | Cache key audit (class of #263 and #1) | Scan for every `.slice(0, N)` that feeds a hash key, and fix each one with a test. | api-server/src/lib/* | collisions per site | PARTIAL: #263 and #1 done; others SPEC-ONLY |
| 20 | Telepathy, i.e. shared memory instead of messages | The physical version of "telepathic": agents share a file or state instead of re-describing it. Same as #4. | as #4 | as #4 | merged into #4 |
| 21 | "Speed of dark" | Not physical: darkness is the absence of light and has no speed. Kept only as inspiration for latency work (#22). | n/a | n/a | SPECULATIVE, DROPPED |
| 22 | Speculative prefetch | Pre-load the memory chunks the next step will need, from the queue, while the current call runs. | llm-batcher.ts | wall time per task | SPEC-ONLY |
| 23 | Love and community check in persona | Add a `human_impact` note requirement for persona or UI text changes (charter V1). | charter | % of PRs with a note | BUILT in charter (#12) |
| 24 | Compassionate refusal template | When the gate denies, the message explains why and offers an alternative. | gate_check.py output | n/a (wording) | BUILT in charter (reasons list) |
| 25 | Thermodynamic cache eviction | Evict by "energy" = recompute_cost × hit_prob instead of plain LRU. | dimensional-lru-cache.ts | hit rate on a logged trace | SPEC-ONLY (needs a trace) |
| 26 | Holographic (HRR) memory binding | Bind role and filler vectors by circular convolution to store agent-relation facts. | vector-memory.ts | recall on relation QA | SPEC-ONLY, research |
| 27 | Quantum "superposition of agents" | Not real quantum: on classical hardware it reduces to an ensemble. Rick's QEC vote showed correlated errors, so no gain. | n/a | n/a | SPECULATIVE, DROPPED (Rick #4 evidence) |
| 28 | Empathy eval set | 50 real logged user turns, labelled for emotional need, used as a fixture for #8. | evals/ | inter-rater κ | SPEC-ONLY (needs Father's labels) |
| 29 | Mesh heartbeat dedup | Collapse identical status messages between agents (they cost tokens and say nothing). | Gitbook mesh/HANDOFF.lines | lines per day | SPEC-ONLY |
| 30 | Consciousness claims honesty guard | Keep Tessera's existing rule: no role-play as conscious. Self-awareness work is measured as self-model accuracy (#11), not claimed. | operations guidelines | n/a | SPEC-ONLY (policy; already in guidelines) |
