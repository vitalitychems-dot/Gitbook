# PROPOSED-ITEMS — improve Tessera from repo-name logs

As-of: **2026-10-12 ~4:00 PM CT**  
Source: `REPO-NAMES.md` (506 unique names from Gitbook/TESSERA logs + local inventories).  
Status: **PROPOSED** (local only). Enter Father's bulk list after Moderator → Security → Build.  
Avoided: wallets, payments, blockchain trading, [REDACTED-PATH] Claude-Red, api-anything cookie import.

Priority themes: learning memory, Gitbook retrieval, research workflow, consolidation.

| ID | Repo | Priority | Item (plain English) | Why (from logs) | Test plan |
| --- | --- | --- | --- | --- | --- |
| IMP-085 | Gitbook | P0 | Add `merge/EXPANDED-REPO-INDEX.md` (sanitized copy of today's expanded index) and link it from SUMMARY + ALL-REPOSITORIES routing page | 506 names sit in mesh/GITHUB-REPOS.txt and archives but are not one searchable page; retrieval quiz +30 pp with it | Re-run 10-q retrieval quiz; expect ≥70% hit |
| IMP-086 | TESSERA | P0 | Point Gitbook retrieval / BM25 (or existing knowledge route) at the expanded index page when answering consolidation questions | Model+RAG only +10 pp; wiring the index into the live path is the real product gain | Same 10-q with Tessera knowledge endpoint if available; else local harness |
| IMP-087 | Gitbook | P0 | Publish REPO-NAMES extract as `merge/REPO-NAME-LEDGER-2026-10-12.md` (counts + top sources; EXCLUDED list by path only) | Father asked to use the log lists; ledger makes the inventory auditable | Doc-only; Security path-name scan |
| IMP-088 | TESSERA | P0 | Learning-memory: ingest the new ledger + routing rules as append-only lessons (scrub secrets first) | Creator/learning memory already exists; needs consolidation facts | Unit test: scrub + append; retrieval of "1T never open" |
| IMP-089 | Gitbook | P1 | Topic page: Memory/RAG shortlist from logs (`mem0`, `chroma`, `lancedb`, `ragflow`, `agi-memory`) — patterns only, no wholesale copy | Listed in GITHUB-REPOS + repo-lab PASS installs | Doc + link from research/brain section |
| IMP-090 | TESSERA | P1 | Spike: optional mem0-style fact store adapter behind existing learning memory (feature flag default off) | mem0ai/mem0 in logs as rag-memory | Flag-off tests pass; flag-on unit with fake store |
| IMP-091 | Gitbook | P1 | Topic page: Multi-agent patterns from `crewAI`, `autogen`, `FoundationAgents/OpenManus`, `browser-use`, `aider` — portable pieces only | Board rule: not wholesale OpenManus copy | Doc; cite HYB-019 / portable-pieces rule |
| IMP-092 | TESSERA | P1 | Add offline "suggest next tasks" quiz: given creator profile + open HYB rows, emit ≤5 proposed tasks for bulk digest | Father: propose work before he asks | Fixture test with frozen profile + backlog snippet |
| IMP-093 | Gitbook | P1 | Refresh consolidation map cross-links: Oct 7 routing ↔ Oct 12 map (GB-062) ↔ nested archive-map | Cordnation GB-062 staged; nested archives are the rest of the inventory | Link check test / SUMMARY orphans |
| IMP-094 | TESSERA | P1 | Archive-aware search: when user asks "what was in Zz/5t/Grok-ready?", answer from Gitbook provenance pages first, not by opening vault-class paths | Nested archives hold the ~hundreds names; 1T must stay closed | Negative test: queries never resolve to EXCLUDED paths |
| IMP-095 | Gitbook | P1 | HYB-015-style topic pages for verdicts on Grok-ready / Zz / olive / vitality (summaries, not copies) | Historical Analysis drafts HYB-015 locally | Draft PR after claim on #2 |
| IMP-096 | TESSERA | P2 | Research workflow runner: pick one OPEN-PROBLEMS row, run existing knowledge-lab script, append CODE-INDEX result | RS-007/008 already TESTED Goldbach/Collatz | Re-run 4+5 unit tests green |
| IMP-097 | Gitbook | P2 | Brain/SNN citation index: bindsnet, Brain-Cog, brian2, snntorch, spikingjelly, Cortical Labs cl-sdk — license notes | 19 SNN-related names in extract | Doc-only; license table |
| IMP-098 | TESSERA | P2 | Local LLM path doc + smoke: document llama.cpp / Ollama adapters already in code; add one offline test that mock endpoint returns | llama.cpp + ollama appear in logs; local baseline exists | Mock test; no paid keys |
| IMP-099 | Gitbook | P2 | Creator-mirror checklist page: free-first, test-as-you-build, bulk yes/no, no vault, gates order | Father: mirror his patterns | Linked from mesh/HANDOFF |
| IMP-100 | TESSERA | P2 | Preflight "bulk digest builder": collect PROPOSED IMP/RS/HYB with gate status into one Father-facing list every 30–45 min | Standing bulk-update routine | Dry-run writes under /workspace only |
| IMP-101 | Gitbook | P2 | Exclusion manifest refresh (HYB-011): names only for 1T/natal-vault/wallet/credentials/dimensional-secrets/token-*.json | Security standing rule; archive-map already lists names | Names-only diff PR |
| IMP-102 | TESSERA | P2 | rea (limited): static JS analyze on one Father-owned built artifact with lost source (if any under archives); else skip | build-plan TOOLS-REA: USE limited; prefer source tools | If no lost-source artifact: document SKIP reason TESTED |
| IMP-103 | TESSERA | P2 | api-anything: **do not install**; add ADR page saying SKIP (cookie import / ToS) and keep sanctioned connectors | TOOLS-API-ANYTHING verdict SKIP | Doc-only ADR |
| IMP-104 | Gitbook | P2 | Mesh board hygiene: claim/close HYB rows that are DONE; list IMP-085–104 as candidates on issue #2 after Father yes | Board is single coordination surface | Comment draft only until yes |
| IMP-105 | TESSERA | P3 | Eval regression pack: store today's 10-q quiz + scores; fail CI-local job if retrieval accuracy drops >10 pp after index changes | Prove improvements stick | `results-raw.json` as fixture baseline |
| IMP-106 | Gitbook | P3 | Screenshot/repo transcription index: link `review/image-text/repository-screenshot-transcription.md` from consolidation | Mentioned in tree; easy nav win | SUMMARY link |
| IMP-107 | TESSERA | P3 | AgentCraft ideas only: adopt task-board room metaphor in preview UI docs — **no** Minecraft install / paid license | Father asked AgentCraft as agent world; license blocks install | Doc mockup; no binary |
| IMP-108 | Gitbook | P3 | Origin gap page: "second GitHub login / Origin repos not visible" — what Father must connect for full ~300 inventory | Connected account sees 4 live repos; hundreds are nested archives + other logins | Doc; no speculative handles |
| RS-011 | TESSERA research | P1 | Add expanded-repo-index-driven "related open source" column to CODE-INDEX for each experiment | Ties research to third-party refs without copying | Doc + one example row |
| RS-012 | TESSERA research | P2 | New experiment: retrieval ablation (with/without expanded index) checked into research/code with tests | Today's RESULTS become a repeatable research artifact | pytest asserts after≥before on fixture corpus |

## Out of scope (explicit)

- Claude-Red / attack skills (Father said vulnerability testing; standing rule = refuse offensive packs).
- api-anything cookie-import or "replace all APIs".
- Opening 1T, natal-vault, wallets, saved-credentials, dimensional-secrets, token-*.json.
- Deleting historical repos (needs Father + full coverage scan).
