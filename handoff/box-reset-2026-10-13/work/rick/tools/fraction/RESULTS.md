# Fraction-agent unification — measured test

**Question:** does unifying agents as "fractions of Tessera" (shared skills + one shared
memory/index) actually improve Tessera, or is it just a slogan?

## Setup (real data, no synthetic)
- **Corpus:** the live shared index `tools/allsee/allsee.db` (87,147 chunks across TESSERA-ro,
  Gitbook, gitbook-gate clones, rea-batch, rick). Leak guard excludes any path matching
  `qa_set | /cycles/ | /tools/fraction/ | allsee/rounds | synapse` so the held-out answers
  are never in the searchable corpus.
- **Queries:** the held-out **test split** of `cycles/c1/qa_set.json` — **215** real
  fill-in-the-blank questions drawn from actual mesh docs.
- **Hit:** the original line, with its blank filled by the gold answer, appears verbatim in one
  of the top-k=5 returned chunks (strict; no partial credit).
- **Token cost:** retrieved-context tokens (chars/4) + 60 tokens per cross-agent message hop
  (siloed collaboration pays per teammate it has to ask; unified pays one).
- **Latency:** wall-clock per query, BM25 over SQLite FTS5, box-local.
- Runner: `tools/fraction/bench.py` (stdlib only, seed=7). Raw: `bench.json`.

## Three configurations
1. **siloed_own_only** — each agent holds only its own slice (A rick/Gitbook, B TESSERA/opt/tw,
   C gitbook-gates, D rest). A query is routed to one agent's private memory. The pure silo.
2. **siloed_broadcast_4** — siloed memories, but the asking agent broadcasts to all 4 and merges.
   Collaboration *without* a shared index.
3. **unified_fraction** — one shared index, every fraction sees the whole thing in one hop.

## Results (before → after)

| config | hit@5 (accuracy) | tokens/q | latency p50 (ms) | latency mean (ms) |
|---|---|---|---|---|
| siloed_own_only (baseline) | 0.414 | 2,019 | 104.3 | 120.0 |
| siloed_broadcast_4 | 0.777 | 7,693 | 407.9 | 461.2 |
| **unified_fraction** | **0.716** | **3,095** | **101.2** | **116.7** |

## Reading it against Father's priority (tokens + speed first, then accuracy)
- **vs the pure silo (baseline):** unified lifts accuracy **0.414 → 0.716 (+73%)** for +1,076
  tokens/q and *the same* latency. Clear win.
- **vs broadcast (siloing that still collaborates):** unified reaches nearly the same accuracy
  (0.716 vs 0.777, −8% relative) while cutting **tokens 7,693 → 3,095 (−60%)** and
  **latency 408 → 101 ms (−75%)**. That is the token-and-speed win Father asked to rank first.
- Broadcast "wins" accuracy only by paying 2.5x the tokens and 4x the time to poll every silo —
  exactly the approval/coordination tax unifying is meant to remove.

## Verdict: **KEPT**
Unifying agents as fractions with one shared memory measurably improves Tessera: +73% retrieval
accuracy over a lone siloed agent, and at the broadcast accuracy tier it is ~60% cheaper in
tokens and ~75% faster. It is the efficient operating point under the tokens-then-speed-then-
accuracy rule.

**Honest caveats (not dropped, just scoped):**
- This measures the *shared-memory* half of "fractions," which is the testable part. It does not
  prove the governance claim that skipping Tessera's approval is safe — that is why the charter
  keeps Security PASS, Build, and Moderator mandatory and is shipped only as a DRAFT PR for the
  gates, not merged.
- The −8% accuracy gap to broadcast is real; if a task needs max recall over tokens, broadcast
  is still the better mode. Unified is the default, not the only mode.
