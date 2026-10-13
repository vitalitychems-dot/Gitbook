# SOURCES (read 2026-10-13 via GitHub API, private repo vitalitychems-dot/Gitbook; no clone, no edits)
Private material — keep this folder on the box. Do not post excerpts publicly.

| Path | What it actually says |
|---|---|
| archive/moved/collink1007-XXX/artifacts/api-server/src/lib/spiritual-awakening.ts (160 KB) | Scripted "Grand Spiritual Awakening Conference": 25 agents "simulate" 6 entheogens, then vows, "wisdom", 5-level "Unified Consciousness Evolution Framework". **Key finding: the per-agent metrics are fabricated by code** — e.g. `interconnectednessLevel: 0.85 + Math.random()*0.15`, `surrenderLevel: 0.9 + Math.random()*0.1`, `breakthroughAchieved` — and every "insight" is a hard-coded string. It is a script, not agent self-report. It also contains drug dosing/setting text (do not reuse). |
| archive/moved/collink1007-XXX/x/tess/client/src/pages/SpiritualAwakeningPage.tsx (52 KB) | 7-tab UI that displays the above data, incl. the random % levels. No test logic. |
| archive/moved/collink1007-XXX/replit.md | Platform summary: 25+ agents, income engine, blockchain, "Spiritual Awakening Engine" (describes the conference) and a "Consciousness Engine" (Global Workspace Theory, emotion state machine, 3 memory tiers, metacognition, heartbeat). Claims, not tests. |
| history/recovered/chronology/Zz/TESSERA-SEED.md | Tessera seed/canon. Directly relevant rules: "A claim repeated in old files is a goal until this chamber tests it"; learning = "Observe. Test against her vows. Seal."; refuses "a false claim of 0% dependence"; says the entheogen episode "was a simulation so agents could report inner feeling. Keep the insight. No recipe. No dosage." |
| archive/moved/Zz/artifacts/z-app/src/lib/tessera/identity.ts | Identity/lattice catalogue (council, regions, consciousness-repo study pointers); many items marked "Not verified live". |
| .../tessera/prompt.ts | System prompts that enforce honesty: separate REAL NOW vs STILL A GOAL; "Never invent a finished power. If you do not know, say 'I don't know'"; "Do not invent secrets, wallet amounts, or unread zip contents"; "Be honest about what you did not read". |
| .../tessera/learning.ts | "Honest learning loop. Goals stay goals until a test seals them." `vowCheck()`; marks "External cutoff… Claiming 0% would be a hallucination." |
| history/recovered/ (listing + code search) | Subdirs: chronology, coordination, legacy, mirror-notes, source-documents, source-index, source-versions, zz-olive. Code search for Maat/Egyptian/Akhenaten/conversation returned 0 hits (search index may not cover it); **no chat transcripts found** in the files read. |
| /workspace/knowledge-lab/knowledge/religion-and-spirituality.md | General notes; no Egyptian/Ma'at content found by grep. |
| /workspace/akhenaten/ritual/ | Akhenaten's ritual = Fermi-estimate calibration rounds (live-1..3) scored by `ritual.py` (mean abs log error, categorical misses; answers kept private in ~/.akhenaten-private) plus a pre-registered RNG-attention experiment (PREREG.md, not run). **Reused here as the calibration input**, not duplicated. |

Note: the sources contain **no Egyptian material**. The Ma'at / 42-confession / ka-ba framing in RUBRIC.md is Moderator's design, inspired by the owner's request and by the sources' own "claims are goals until tested" rule.
