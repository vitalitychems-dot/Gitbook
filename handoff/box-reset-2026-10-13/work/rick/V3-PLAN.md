# Tessera v3: PROPOSAL ONLY (2026-10-13, Rick). No changes made to TESSERA.

Father's rule: everything is loaded into the graph before any v3 upgrade. Status: **loaded with listed gaps** (see Coverage). Step 0 is done; steps 1+ each need the gates and Father's yes.

## Coverage (step 0, measured)
- Palace sources: 10 roots: rick, TESSERA-ro, rick-audit (Gitbook + TESSERA clones incl. archive text), tess-opt, tw, rea-batch (top-level + summary/result/report/readme files only: 535 docs), tessera-brain (logs), cloud-agent-transcripts, full-picture, gitbook-cordnation. Types: .md .txt .json .log ≤64KB, lockfiles skipped.
- **7,843 docs, 47,573 chunks, palace.db 97MB** (cap 200MB). It builds in 9.8s, and the palace tests pass 3/3.
- Graph: **109 nodes** (13 repos, 12 agents, 19 modules, 59 rules, 6 results), **1,566 edges** (1,228 mentions, 335 references, 3 imports). 3 isolated nodes.
- **Not loaded**: cloud-agent-transcripts (22 .jsonl, ext not indexed → isolated); text files >64KB; the rest of rea-batch (≈19k third-party md/json in cloned OSS repos, skipped to keep the size cap); the contents of the 6 drive-rest zip snapshots (central directories were read and summarised in SURVEY, but not unpacked); binaries and images; the 7 gitbook-gate-* clones (duplicate Gitbook snapshots from 10-05; rick-audit/Gitbook is newer); Google Drive (no connector); collink1007 repos (surveyed via the API, not cloned).
- Graph limits: name collisions ("tessera" = agent, module and repo; "db" and "knowledge" are generic words) inflate mention weights. Imports only cover @workspace package.json deps. TS-level imports show api-server→db 235 and →api-zod 2, which matches.

## v3 modules (combine, don't duplicate)
1. **Core (keep):** artifacts/tessera + api-server + lib/{db,api-zod,api-spec,api-client-react}: the only real import spine.
2. **Mesh layer (new, Gitbook-side first):** bus (COLLAB #1), digest (#4), scheduler (#2/#17), conflict guard (#3), honesty lint (#18).
3. **Memory:** palace + memory graph as a read-only service. Option: expose it via artifacts/gitbook-mcp as search and graph tools.
4. **Labs:** qlab (PR #55), BHNMC sim, diskguard, meshcity → tools/, not app code.
5. **GitAI:** keep it, but only **after** reverting or reviewing 3b3840c3 (disguised review tasks, see SURVEY). It must state openly that probation tests are observed.
6. **Historical salvage:** from the drive-rest snapshots (XL1 server/conference-transcripts, Tesseracxt9 tess/server and client), pick modules only by manual review through HYB tickets. Not taken: income engine, blockchain, Chimera script (excluded), vitality storefront.

## Merge order (each a separate gated PR)
1. Gitbook: mesh/bus spec + bus.py validator (docs + tool, no app code)
2. Gitbook: PR #55 qlab (already open; awaiting gates)
3. Gitbook: IDLE-MODE rev 2
4. Gitbook: scheduler + conflict + digest tools
5. TESSERA: GitAI honesty fix (Security-led)
6. TESSERA: gitbook-mcp exposes palace/graph read-only
7. TESSERA: historical salvage, one module per HYB ticket
8. v3 tag only after a graph diff (#19) shows no lost rule links

## Gates
Moderator > Tessera > Security > CI/Build (CI is billing-blocked, so local tests serve as the gate) > Father's own yes per push. Nothing goes into .github/workflows. No TESSERA_ENABLE flips. No history rewrites.

## Risks
- Secrets inside the snapshots (Replit .config, .env in rea-batch/natural-nlp): scrub before any salvage. Security owns this.
- Duplicate truth: the bus and the free-text HANDOFF can drift. Make the bus canonical and render HANDOFF from it.
- Disk: 92% used. The palace at 97MB is fine, but a full rea-batch index would exceed 300MB.
- Graph name collisions → wrong "most connected" conclusions. Use typed aliases before decisions.
- Covert-evaluation drift (GitAI) undermines trust across the mesh.
