# Rick — ROUND 2 (2026-10-12)

Source: OPTIMIZE-26 (24/26 PASS; #4 and #11 NOT DONE). Bench: TESSERA PR #246 clone `/workspace/tess-opt` @ 91b6f0d, imported read-only. My prototypes and bench are in `/workspace/rick/round2/r2.mjs`; run `node /workspace/rick/round2/r2.mjs`. Raw output is in `round2/results.tsv`. The tokenizer is the repo's `countTokens`, which is ceil(chars/4). Every number below comes from that run. Nothing was pushed or changed in TESSERA.

| # | Name (Tesla link) | Idea | One runnable step (input → output) | Test | Metric | Before | After | Result |
|---|---|---|---|---|---|---|---|---|
| 1 | prefix-legend, finishes #4 | #4 only made legends for whole repeated tokens. Every PR URL in the log is unique, so it found nothing to shorten. Make legends for repeated path prefixes instead. | `prefixLegend(text)` → `§i=prefix` legend line + body | `expandLegend(out) === input` | tokens, BUILD-LOG | 1675 | 1336 (-20.2%) | PASS |
| 2 | key-hoist | Write the JSONL key names once per row shape, then store only the values as arrays | `keyHoist(rows)` → grouped JSON | `unhoist` gives back exactly the minified rows | tokens, 200 memory rows | 11956 | 10171 (-14.9%) | PASS |
| 3 | resonate-chain, finishes #11 (resonance tuning) | Try every order and subset of the lossless passes and keep the smallest result that passes its check. Here the winner was dedupe>ws>prefix. | `resonateChain(text, verify)` → `{out, chain}` | output expands back to the dedupe+ws text | tokens, BUILD-LOG vs packContext | 1624 | 1286 (-20.8%) | PASS |
| 4 | coincide (725,605) | Act only when all 3 independent checks agree | gate(checks) → act/refuse | 2 of 3 agreeing → refuse | wrong actions per 1000, simulated checks 90% accurate, seed 7 | 44 | 0 | PASS (simulation) |
| 5 | phase (381,968) | Start worker i on tick i mod K | starts[] → staggered starts | no tick has more than ceil(n/K) starts | max starts in one tick, 12 workers | 12 | 3 | PASS (simulation) |
| 6 | valve (valvular conduit) | Log is append-only, so rewriting an existing line is refused | `valveLog().write(i,l)` → bool | rewriting an old index fails, appending succeeds | rewrites accepted out of 10 | 10 | 0 | PASS |
| 7 | bifilar (512,340) | Every open must be matched by a close. Report any open left unmatched. | `bifilar(events)` → unmatched ids | finds all 5 injected leaks | leaks undetected out of 5 | 5 | 0 | PASS |
| 8 | earth-return (645,576, shared return path) | Store a handoff body once and pass a 16-hex hash ref along the chain | body → `{ref}` + shared store | `store.get(ref) === body` | bytes over a 7-hop chain (BUILD-LOG body) | 46879 | 6879 (-85.3%) | PASS |
| 9 | tuned-clip | Clip long tool output by keeping lines that match the query, not just the first lines | `tunedClip(text, q, 40)` → clipped text | every match is kept when matches < cap | lines matching "relation" kept, 40-line cap, 10 matches exist | 1 | 10 | PASS |
| 10 | resonate-batch | Try batch sizes for chunked work and keep the fastest measured one | sweep B ∈ {1,4,16,64,256} → best B | the returned B has the lowest median time | median ms over 7 runs, token-counting the memory file | 0.098 (B=1) | 0.021 (B=16) | PASS, weak (see caveats) |

## Caveats (another lane should verify)
- #3: `dedupe` drops repeated lines. The old packContext does the same, so the comparison is fair, but the chain is not byte-lossless against the raw input.
- #4, #5: the inputs are simulated (an LCG with seed 7, and a synthetic start list). The numbers are real outputs of those simulations, not production data.
- #6: tesla.md's verified list does not include the valvular conduit patent. The link is by name only, so it should be verified before anyone cites it.
- #10: the timings are tiny (under 0.1 ms) and likely include JIT warmup noise. Rerun it on a larger input before trusting -78.6%.
- #8 and #2 change the wire format. Receivers would need the matching expand step.
- None of these are implemented in TESSERA. Per the rules, the build lane implements and gates them.
