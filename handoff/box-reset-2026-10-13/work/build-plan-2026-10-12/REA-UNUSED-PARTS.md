# REA-UNUSED-PARTS (v3 re-mine)

Generated 2026-10-13 04:2x CT from REA-ALL-REPOS.csv (531 rows) + V2-FEATURE-MAP.csv licenses. Scope: 264 scanned repos; blocked (228) and excluded (38) not re-mined (unreadable/hard-limit).

Rules: reuse code only if license is permissive (MIT/Apache-2.0/BSD/ISC/CC0) with credit; UNKNOWN/NONE/NOASSERTION/GPL = idea-only clean-room. Estimates are ESTIMATES unless `measured` is set.

Summary: built/used in v2 = 10; unused = 254; code-reusable licenses = 14; measured wins vs v2 = 10.

## v3 test results (2026-10-13, TESSERA #274, 15ff520)
- Tested on CPU and kept (ideas rebuilt from scratch; all MIT, credited in NOTICE): microsoft/LLMLingua (pruning), yamadashy/repomix (packing), mit-han-lab/streaming-llm (sink+window), plus dedupe. Combined: tokens/query 333->149, recall at the v2 budget 15->21/87.
- Needs a GPU, not tested: vllm, sglang, Medusa, EAGLE, DeepSeek-V3, Qwen3, GLM-5, TensorRT-LLM, TGI, DeepSpeed.
- Note: the 'UNKNOWN' licenses in the table come from the old map. LLMLingua, repomix and streaming-llm were checked as MIT through the GitHub API.

Ranked tokens → speed → accuracy → other, then estimate magnitude.

| # | repo | category | license | reuse | v3 goal | unused parts / idea | v2 status | estimate |
|---|---|---|---|---|---|---|---|---|
| 1 | huggingface/transformers | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 2 | deepseek-ai/DeepSeek-V3 | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 3 | vllm-project/vllm | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 4 | deepspeedai/DeepSpeed | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 5 | sgl-project/sglang | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 6 | QwenLM/Qwen3 | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 7 | NVIDIA/TensorRT-LLM | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 8 | huggingface/text-generation-inference | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 9 | zai-org/GLM-5 | llms-open-inference | UNKNOWN | idea-only | tokens | Open models + high-throughput serving | idea only, not built | cost per 1M tokens: -50-90% vs paid API ESTIMATE |
| 10 | yamadashy/repomix | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 11 | mit-han-lab/streaming-llm | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 12 | microsoft/LLMLingua | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 13 | gptscript-ai/gptscript | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 14 | FasterDecoding/Medusa | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 15 | SafeAILab/EAGLE | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 16 | Zefan-Cai/KVCache-Factory | token-saving-compression | UNKNOWN | idea-only | tokens | Prompt/context compression, repo packing, KV cache, spec decoding | idea only, not built | prompt tokens: -30-80% ESTIMATE (vendor-reported up to 20x for LLMLingua) |
| 17 | modelcontextprotocol/servers | memory-recall; tool-use-mcp | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 18 | mem0ai/mem0 | memory-recall | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 19 | supermemoryai/supermemory | memory-recall | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 20 | letta-ai/letta | memory-recall | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 21 | MemoriLabs/Memori | memory-recall | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 22 | getzep/zep | memory-recall | UNKNOWN | idea-only | tokens | Long-term + episodic recall across sessions | idea only, not built | tokens per task (re-context): -20-40% ESTIMATE |
| 23 | obra/superpowers | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 24 | anthropics/skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 25 | addyosmani/agent-skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 26 | K-Dense-AI/scientific-agent-skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 27 | VoltAgent/awesome-agent-skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 28 | vercel-labs/skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 29 | agentskills/agentskills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 30 | google/skills | agent-skills | UNKNOWN | idea-only | tokens | SKILL.md packaging, reusable procedures | idea only, not built | repeat-task tokens: -15-30% ESTIMATE |
| 31 | nicholasgasior/trafilatura | misc | Apache-2.0 | code+credit | tokens | HTML→clean text for shepherd keyless pulls and mesh docs | idea only, not built | -15% tokens on scrape/summarize ESTIMATE |
| 32 | collink1007/z | tessera-core | NONE | idea-only | tokens | Zz tree REA'd 83.9% (115/137). Graph/tree imports for knowledge-graph memory (reference only, no wholesale copy) | idea only, not built | -10% tokens/task ESTIMATE |
| 33 | nicholasgasior/wink-nlp | misc | UNKNOWN | idea-only | tokens | Local NLP tagging for memory graph without cloud LLM | idea only, not built | -10% classify tokens; +5% task completion ESTIMATE |
| 34 | nicholasgasior/social-content-calendar | misc | NOASSERTION | idea-only | tokens | Content drafting templates for agent studio posts | idea only, not built | -8% draft tokens ESTIMATE |
| 35 | nicholasgasior/social-media-scheduler | misc | NONE | idea-only | tokens | Content drafting templates for agent studio posts | idea only, not built | -8% draft tokens ESTIMATE |
| 36 | nicholasgasior/story-writer | token-efficiency | BSD-3-Clause | code+credit | tokens | Content drafting templates for agent studio posts | idea only, not built | -8% draft tokens ESTIMATE |
| 37 | nicholasgasior/testimonial-generator | testing | NONE | idea-only | tokens | Content drafting templates for agent studio posts | idea only, not built | -8% draft tokens ESTIMATE |
| 38 | nicholasgasior/video-script-writer | misc | UNKNOWN | idea-only | tokens | Content drafting templates for agent studio posts | idea only, not built | -8% draft tokens ESTIMATE |
| 39 | punkpeye/awesome-mcp-servers | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 40 | upstash/context7 | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 41 | microsoft/playwright-mcp | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 42 | github/github-mcp-server | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 43 | modelcontextprotocol/python-sdk | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 44 | modelcontextprotocol/typescript-sdk | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 45 | mobile-next/mobile-mcp | tool-use-mcp | UNKNOWN | idea-only | speed | Standard tool servers/SDKs | idea only, not built | new-tool integration time: -50-80% ESTIMATE |
| 46 | microsoft/autogen | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 47 | crewAIInc/crewAI | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 48 | langchain-ai/langgraph | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | LANDED: technique -> OPT-19, OPT-21 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | parallel task throughput: +20-50% ESTIMATE |
| 49 | agno-agi/agno | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 50 | OpenBMB/ChatDev | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 51 | openai/openai-agents-python | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 52 | camel-ai/camel | multi-agent-orchestration | UNKNOWN | idea-only | speed | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 53 | vitalitychems-dot/GitbookAI | offline-mesh | NONE | idea-only | speed | Public mesh drop room (GitMesh) — TESSERA tab + offline sync surface | idea only, not built | +20% offline drop UX ESTIMATE |
| 54 | collink1007/XXX | offline-mesh | MIT | code+credit | speed | REA'd 89.9% (1740/1936). Service-worker precache pattern (O3) + client page list | idea only, not built | +15% offline uptime; 1 HIGH finding (hard-coded admin key, already logged) ESTIMATE (finding MEASURED) |
| 55 | vitalitychems-dot/Gitbook | docs | NONE | idea-only | speed | Offline queue/cache + archive patterns already mapped into v2 plan | idea only, not built | +15% offline uptime ESTIMATE |
| 56 | collink1007/amber-flame-tiger-sand | ui | NONE | idea-only | speed | REA'd 82.6% (147/178). Offline queue + cache patterns for TESSERA preview | idea only, not built | +10% offline uptime / +3 tests ESTIMATE |
| 57 | collink1007/fleet-moss-monarch-rapid | commerce | NONE | idea-only | speed | REA'd 94.5% (207/219). Site/layout components reusable for studio pages | idea only, not built | -5% build time ESTIMATE |
| 58 | ollama/ollama | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 59 | open-webui/open-webui | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 60 | ggml-org/llama.cpp | local-offline-inference; token-saving-compression | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 61 | nomic-ai/gpt4all | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 62 | ggml-org/whisper.cpp | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 63 | mudler/LocalAI | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 64 | exo-explore/exo | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 65 | janhq/jan | local-offline-inference | UNKNOWN | idea-only | speed | Run models with no internet | idea only, not built | offline uptime of agent features: +up to 100% of LLM features offline ESTIMATE |
| 66 | langfuse/langfuse | evals | UNKNOWN | idea-only | accuracy | Regression evals for agent behavior | idea only, not built | regressions caught pre-merge: +30-60% ESTIMATE |
| 67 | promptfoo/promptfoo | evals | UNKNOWN | idea-only | accuracy | Regression evals for agent behavior | idea only, not built | regressions caught pre-merge: +30-60% ESTIMATE |
| 68 | comet-ml/opik | evals | UNKNOWN | idea-only | accuracy | Regression evals for agent behavior | idea only, not built | regressions caught pre-merge: +30-60% ESTIMATE |
| 69 | openai/evals | evals | UNKNOWN | idea-only | accuracy | Regression evals for agent behavior | idea only, not built | regressions caught pre-merge: +30-60% ESTIMATE |
| 70 | EleutherAI/lm-evaluation-harness | evals | UNKNOWN | idea-only | accuracy | Regression evals for agent behavior | idea only, not built | regressions caught pre-merge: +30-60% ESTIMATE |
| 71 | guardrails-ai/guardrails | anti-hallucination-grounding | UNKNOWN | idea-only | accuracy | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 72 | NVIDIA-NeMo/Guardrails | anti-hallucination-grounding | UNKNOWN | idea-only | accuracy | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 73 | truera/trulens | anti-hallucination-grounding | UNKNOWN | idea-only | accuracy | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 74 | vectara/hallucination-leaderboard | anti-hallucination-grounding | UNKNOWN | idea-only | accuracy | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 75 | stanford-oval/WikiChat | anti-hallucination-grounding | UNKNOWN | idea-only | accuracy | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 76 | langchain-ai/langchain | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 77 | infiniflow/ragflow | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 78 | Mintplex-Labs/anything-llm | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 79 | run-llama/llama_index | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 80 | qdrant/qdrant | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 81 | chroma-core/chroma | rag | UNKNOWN | idea-only | accuracy | Doc ingestion, chunking, vector search | idea only, not built | answer grounding rate: +10-30% ESTIMATE |
| 82 | deepseek-ai/DeepSeek-R1 | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 83 | stanfordnlp/dspy | reasoning-thinking; recursive-self-improvement | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | LANDED: technique -> OPT-05, OPT-06, OPT-18 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) | task accuracy: +5-15% ESTIMATE |
| 84 | huggingface/open-r1 | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 85 | verl-project/verl | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 86 | SakanaAI/AI-Scientist | reasoning-thinking; recursive-self-improvement | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 87 | Jiayi-Pan/TinyZero | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 88 | princeton-nlp/tree-of-thought-llm | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 89 | hkust-nlp/simpleRL-reason | reasoning-thinking | UNKNOWN | idea-only | accuracy | CoT / ToT / RL-reasoning recipes, DSPy prompt programs | idea only, not built | task accuracy: +5-15% ESTIMATE |
| 90 | openai/codex | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 91 | daytonaio/daytona | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 92 | firecracker-microvm/firecracker | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 93 | google/gvisor | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 94 | e2b-dev/E2B | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 95 | containers/bubblewrap | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 96 | superradcompany/microsandbox | sandboxed-code-exec | UNKNOWN | idea-only | accuracy | microVM/user-namespace isolation for agent code | idea only, not built | sandbox escape surface: large reduction ESTIMATE |
| 97 | TadasBaltrusaitis/OpenFace | k-affective-computing | UNKNOWN | idea-only | accuracy | Face/voice affect features, emotion datasets | idea only, not built | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data |
| 98 | declare-lab/MELD | k-affective-computing | UNKNOWN | idea-only | accuracy | Face/voice affect features, emotion datasets | idea only, not built | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data |
| 99 | audeering/opensmile | k-affective-computing | UNKNOWN | idea-only | accuracy | Face/voice affect features, emotion datasets | idea only, not built | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data |
| 100 | CheyneyComputerScience/CREMA-D | k-affective-computing | UNKNOWN | idea-only | accuracy | Face/voice affect features, emotion datasets | idea only, not built | empathy-label accuracy (needs eval): ESTIMATE only; consent-required data |
| 101 | confident-ai/deepeval | anti-hallucination-grounding; evals | UNKNOWN | idea-only | other | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 102 | vibrantlabsai/ragas | anti-hallucination-grounding; evals | UNKNOWN | idea-only | other | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 103 | Arize-ai/phoenix | anti-hallucination-grounding; evals | UNKNOWN | idea-only | other | Faithfulness checks, guardrails, citation grounding | idea only, not built | unsupported-claim rate: -20-50% ESTIMATE |
| 104 | FoundationAgents/MetaGPT | multi-agent-orchestration; recursive-self-improvement | UNKNOWN | idea-only | other | Role-based crews, graph workflows, handoffs | idea only, not built | parallel task throughput: +20-50% ESTIMATE |
| 105 | ContinualAI/avalanche | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 106 | GMvandeVen/continual-learning | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 107 | aimagelab/mammoth | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 108 | LAMDA-CL/LAMDA-PILOT | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 109 | GT-RIPL/Continual-Learning-Benchmark | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 110 | google-research/l2p | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 111 | Continvvm/continuum | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 112 | ContinualAI/continual-learning-baselines | continual-learning | UNKNOWN | idea-only | other | Learning without forgetting | idea only, not built | retained skill after update: +10-30% ESTIMATE |
| 113 | HKUDS/LightRAG | knowledge-graphs; rag | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 114 | microsoft/graphrag | knowledge-graphs; rag | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 115 | topoteretes/cognee | knowledge-graphs; memory-recall | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 116 | getzep/graphiti | knowledge-graphs; memory-recall | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 117 | neo4j/neo4j | knowledge-graphs | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 118 | reconurge/flowsint | knowledge-graphs | Apache-2.0 | code+credit | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 119 | FalkorDB/FalkorDB | knowledge-graphs | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 120 | neo4j-labs/llm-graph-builder | knowledge-graphs | UNKNOWN | idea-only | other | Graph build/query, GraphRAG, temporal graphs | idea only, not built | retrieval precision: +10-30% ESTIMATE |
| 121 | Significant-Gravitas/AutoGPT | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 122 | OpenHands/OpenHands | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 123 | openinterpreter/openinterpreter | agi-frameworks; sandboxed-code-exec | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 124 | reworkd/AgentGPT | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 125 | assafelovic/gpt-researcher | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 126 | microsoft/JARVIS | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 127 | yoheinakajima/babyagi | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 128 | openai/swarm | agi-frameworks | UNKNOWN | idea-only | other | Autonomous plan-act-observe loop patterns | idea only, not built | task completion rate: +10-20% ESTIMATE |
| 129 | algorithmicsuperintelligence/openevolve | recursive-self-improvement | UNKNOWN | idea-only | other | Reflexion, evolutionary code search, prompt optimization | idea only, not built | benchmark score per iteration: +5-20% ESTIMATE |
| 130 | MineDojo/Voyager | recursive-self-improvement | UNKNOWN | idea-only | other | Reflexion, evolutionary code search, prompt optimization | idea only, not built | benchmark score per iteration: +5-20% ESTIMATE |
| 131 | zou-group/textgrad | recursive-self-improvement | UNKNOWN | idea-only | other | Reflexion, evolutionary code search, prompt optimization | idea only, not built | benchmark score per iteration: +5-20% ESTIMATE |
| 132 | noahshinn/reflexion | recursive-self-improvement | UNKNOWN | idea-only | other | Reflexion, evolutionary code search, prompt optimization | idea only, not built | benchmark score per iteration: +5-20% ESTIMATE |
| 133 | jennyzzt/dgm | recursive-self-improvement | UNKNOWN | idea-only | other | Reflexion, evolutionary code search, prompt optimization | idea only, not built | benchmark score per iteration: +5-20% ESTIMATE |
| 134 | freeCodeCamp/freeCodeCamp | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 135 | EbookFoundation/free-programming-books | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 136 | TheAlgorithms/Python | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 137 | tldr-pages/tldr | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 138 | freeCodeCamp/devdocs | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 139 | bigcode-project/the-stack-v2 | k-coding | UNKNOWN | idea-only | other | Open coding curricula, algorithms, offline docs | idea only, not built | coding task success: +5-15% ESTIMATE |
| 140 | nicholasgasior/signal-protocol | security-protocols | GPL-3.0 | idea-only | other | E2E message crypto patterns for signed mesh drops (not wallets) | idea only, not built | +10% mesh message integrity ESTIMATE |
| 141 | thetesseractai/18 | tessera-core | MIT | code+credit | other | Tessera Sovereign v18 architecture — multi-agent + sandbox patterns | idea only, not built | +10% design reuse ESTIMATE |
| 142 | opencog/opencog | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 143 | daveshap/ACE_Framework | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 144 | opencog/atomspace | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 145 | SoarGroup/Soar | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 146 | cmekik/pyClarion | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 147 | ccnlab/leabra | consciousness-cognitive-arch | UNKNOWN | idea-only | other | Global-workspace / working-memory loop for agent deliberation | idea only, not built | task completion rate: +5-10% ESTIMATE |
| 148 | nicholasgasior/selenium-python | docs | NONE | idea-only | other | Browser automation for gateway fetches only (no bypass) | idea only, not built | +8% live-fetch jobs ESTIMATE |
| 149 | nicholasgasior/selenium-wire | misc | MIT | code+credit | other | Browser automation for gateway fetches only (no bypass) | idea only, not built | +8% live-fetch jobs ESTIMATE |
| 150 | nicholasgasior/tink | security-protocols | Apache-2.0 | code+credit | other | Google Tink crypto primitives reference for mesh signing | idea only, not built | +8% crypto hygiene ESTIMATE |
| 151 | nicholasgasior/sentiment-analysis | misc | UNKNOWN | idea-only | other | ML curriculum + on-device inference patterns | idea only, not built | +5% ML curriculum tasks ESTIMATE |
| 152 | nicholasgasior/sendgrid-nodejs | misc | MIT | code+credit | other | Notify SDKs for GitAI/human alerts from gateway node | idea only, not built | +5% publish/notify flows ESTIMATE |
| 153 | nicholasgasior/shipping-calculator | excluded | NONE | idea-only | other | Small workflow/UI patterns for studio widgets | idea only, not built | +2-5% widget/task glue ESTIMATE |
| 154 | nicholasgasior/sphincs | misc | UNKNOWN | idea-only | other | Transport/post-quantum primitives for offline mesh links | idea only, not built | +5% offline mesh trust ESTIMATE |
| 155 | nicholasgasior/task-automation-platform | misc | NONE | idea-only | other | Small workflow/UI patterns for studio widgets | idea only, not built | +2-5% widget/task glue ESTIMATE |
| 156 | nicholasgasior/tensorflow-js | misc | UNKNOWN | idea-only | other | ML curriculum + on-device inference patterns | idea only, not built | +5% ML curriculum tasks ESTIMATE |
| 157 | nicholasgasior/tiingo-python | adapters | MIT | code+credit | other | Open data / ads API adapters for shepherd gateway cache | idea only, not built | +5% gateway data freshness ESTIMATE |
| 158 | nicholasgasior/tiktok-ads-api | misc | NONE | idea-only | other | Open data / ads API adapters for shepherd gateway cache | idea only, not built | +5% gateway data freshness ESTIMATE |
| 159 | nicholasgasior/twilio-node | misc | UNKNOWN | idea-only | other | Notify SDKs for GitAI/human alerts from gateway node | idea only, not built | +5% publish/notify flows ESTIMATE |
| 160 | nicholasgasior/vix-analysis | misc | UNKNOWN | idea-only | other | Open data / ads API adapters for shepherd gateway cache | idea only, not built | +5% gateway data freshness ESTIMATE |
| 161 | nicholasgasior/wireguard-go | misc | MIT | code+credit | other | Transport/post-quantum primitives for offline mesh links | idea only, not built | +5% offline mesh trust ESTIMATE |
| 162 | nicholasgasior/yahoo-finance-api | adapters | MIT | code+credit | other | Open data / ads API adapters for shepherd gateway cache | idea only, not built | +5% gateway data freshness ESTIMATE |
| 163 | sovereign-core/awesome-machine-learning | learning | NOASSERTION | idea-only | other | ML curriculum + on-device inference patterns | idea only, not built | +5% ML curriculum tasks ESTIMATE |
| 164 | sovereign-core/nexus-complete | ui | NONE | idea-only | other | Small workflow/UI patterns for studio widgets | idea only, not built | +2-5% widget/task glue ESTIMATE |
| 165 | vitalitychems-dot/vitality | commerce | NONE | idea-only | other | Artifact health check scripts for CI hygiene | idea only, not built | -5% flaky CI; +2 checks ESTIMATE |
| 166 | nicholasgasior/sitemap-generator | misc | MIT | code+credit | other | Public-page SEO/sitemap helpers for GitMesh/GitAI | idea only, not built | +4% publish completeness ESTIMATE |
| 167 | nicholasgasior/seo-analyzer | misc | MIT | code+credit | other | Public-page SEO/sitemap helpers for GitMesh/GitAI | idea only, not built | +4% publish completeness ESTIMATE |
| 168 | sovereign-core/tesseract1 | tessera-core | NONE | idea-only | other | Same-name public code — OCR or unrelated Tess; ideas only | idea only, not built | 0-2% ESTIMATE |
| 169 | sovereign-core/tesseract3 | tessera-core | NONE | idea-only | other | Same-name public code — OCR or unrelated Tess; ideas only | idea only, not built | 0-2% ESTIMATE |
| 170 | sovereign-origin/TessV1 | misc | NONE | idea-only | other | Same-name public code — OCR or unrelated Tess; ideas only | idea only, not built | 0-2% ESTIMATE |
| 171 | vitalitychems-dot/TESS | docs | UNKNOWN | idea-only | other | Same-name public code — OCR or unrelated Tess; ideas only | idea only, not built | 0-2% ESTIMATE |
| 172 | nicholasgasior/whitepaper-generator | misc | UNKNOWN | idea-only | other | Same-name public stub is empty — no useful code | idea only, not built | 0% ESTIMATE |
| 173 | sovereign-archive/T5 | tessera-core | UNKNOWN | idea-only | other | T5 model wrapper — curriculum only | idea only, not built | 0% runtime ESTIMATE |
| 174 | sovereign-core/tesseract2 | tessera-core | NONE | idea-only | other | Same-name public OCR dump (mbrukman/tesseract2) — too large / low fit; not cloned | idea only, not built | 0% ESTIMATE |
| 175 | vitalitychems-dot/Everything | docs | UNKNOWN | idea-only | other | Ambiguous same-name public repo — not TESSERA-related | idea only, not built | 0% ESTIMATE |
| 176 | vitalitychems-dot/1 | docs | UNKNOWN | idea-only | other | Ambiguous same-name public repo — not TESSERA-related | idea only, not built | 0% ESTIMATE |
| 177 | vitalitychems-dot/TX | docs | UNKNOWN | idea-only | other | Ambiguous same-name public repo — not TESSERA-related | idea only, not built | 0% ESTIMATE |
| 178 | vitalitychems-dot/Zz | docs | UNKNOWN | idea-only | other | Utility/archive same-name — little direct gain | idea only, not built | 0% ESTIMATE |
| 179 | vitalitychems-dot/TESSERA | tessera-core | NONE | idea-only | other | Baseline repo itself — no external gain | idea only, not built | 0% ESTIMATE |
| 180 | vitalitychems-dot/z | excluded | UNKNOWN | idea-only | other | Utility/archive same-name — little direct gain | idea only, not built | 0% ESTIMATE |
| 181 | collin-keane/Tessera | ui | Apache-2.0 | code+credit | other | Public observability/metrics Tessera (unrelated product) — name collision only | idea only, not built | 0% ESTIMATE |
| 182 | mne-tools/mne-python | brain-scans-connectomics; k-neurology | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 183 | google/neuroglancer | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 184 | ANTsX/ANTs | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 185 | nilearn/nilearn | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 186 | freesurfer/freesurfer | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 187 | dipy/dipy | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 188 | nipy/nipype | brain-scans-connectomics | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 189 | nipy/nibabel | brain-scans-connectomics; k-neurology | UNKNOWN | idea-only | other | Neuro data formats (NIfTI/BIDS) for curriculum; graph-of-regions ideas | idea only, not built | no direct TESSERA runtime metric: 0% runtime; curriculum only (ESTIMATE) |
| 190 | fangwei123456/spikingjelly | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 191 | jeshraghian/snntorch | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 192 | BindsNET/bindsnet | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 193 | brian-team/brian2 | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 194 | nengo/nengo | brain-synapse-simulation; consciousness-cognitive-arch | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 195 | norse/norse | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 196 | lava-nc/lava | brain-synapse-simulation | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 197 | brainpy/BrainPy | brain-synapse-simulation; consciousness-cognitive-arch | UNKNOWN | idea-only | other | Spiking/plasticity experiments for agent compute dimension | idea only, not built | compute lab experiments available: n/a; research (ESTIMATE) |
| 198 | tensorflow/tensorflow | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 199 | pytorch/pytorch | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 200 | scikit-learn/scikit-learn | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 201 | keras-team/keras | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 202 | jax-ml/jax | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 203 | tinygrad/tinygrad | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 204 | dmlc/xgboost | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 205 | ml-explore/mlx | machine-learning | UNKNOWN | idea-only | other | Training/finetune substrate for agents' own models | idea only, not built | n/a until compute lab runs: ESTIMATE only |
| 206 | Genesis-Embodied-AI/genesis-world | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 207 | joonspk-research/generative_agents | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 208 | google-deepmind/mujoco | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 209 | Farama-Foundation/Gymnasium | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 210 | a16z-infra/ai-town | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 211 | isaac-sim/IsaacLab | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 212 | microsoft/TinyTroupe | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 213 | OpenBMB/AgentVerse | world-simulation | UNKNOWN | idea-only | other | Generative-agent towns, physics sims for agents' world | idea only, not built | studio realism / agent-life features: qualitative ESTIMATE |
| 214 | google-deepmind/alphafold | k-biology | UNKNOWN | idea-only | other | Protein structure, sequence, single-cell | idea only, not built | n/a: curriculum ESTIMATE |
| 215 | biopython/biopython | k-biology | UNKNOWN | idea-only | other | Protein structure, sequence, single-cell | idea only, not built | n/a: curriculum ESTIMATE |
| 216 | aqlaboratory/openfold | k-biology | UNKNOWN | idea-only | other | Protein structure, sequence, single-cell | idea only, not built | n/a: curriculum ESTIMATE |
| 217 | sokrypton/ColabFold | k-biology | UNKNOWN | idea-only | other | Protein structure, sequence, single-cell | idea only, not built | n/a: curriculum ESTIMATE |
| 218 | scverse/scanpy | k-biology | UNKNOWN | idea-only | other | Protein structure, sequence, single-cell | idea only, not built | n/a: curriculum ESTIMATE |
| 219 | FreeCAD/FreeCAD | k-engineering | UNKNOWN | idea-only | other | CAD/CFD/control | idea only, not built | n/a: curriculum ESTIMATE |
| 220 | openscad/openscad | k-engineering | UNKNOWN | idea-only | other | CAD/CFD/control | idea only, not built | n/a: curriculum ESTIMATE |
| 221 | OpenFOAM/OpenFOAM-dev | k-engineering | UNKNOWN | idea-only | other | CAD/CFD/control | idea only, not built | n/a: curriculum ESTIMATE |
| 222 | python-control/python-control | k-engineering | UNKNOWN | idea-only | other | CAD/CFD/control | idea only, not built | n/a: curriculum ESTIMATE |
| 223 | sympy/sympy | k-geometry; k-sciences | UNKNOWN | idea-only | other | Computational geometry, meshes, point clouds | idea only, not built | 3D floor mesh ops: curriculum ESTIMATE |
| 224 | isl-org/Open3D | k-geometry | UNKNOWN | idea-only | other | Computational geometry, meshes, point clouds | idea only, not built | 3D floor mesh ops: curriculum ESTIMATE |
| 225 | CGAL/cgal | k-geometry | UNKNOWN | idea-only | other | Computational geometry, meshes, point clouds | idea only, not built | 3D floor mesh ops: curriculum ESTIMATE |
| 226 | mikedh/trimesh | k-geometry | UNKNOWN | idea-only | other | Computational geometry, meshes, point clouds | idea only, not built | 3D floor mesh ops: curriculum ESTIMATE |
| 227 | geogebra/geogebra | k-geometry | UNKNOWN | idea-only | other | Computational geometry, meshes, point clouds | idea only, not built | 3D floor mesh ops: curriculum ESTIMATE |
| 228 | riscv/riscv-isa-manual | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 229 | YosysHQ/yosys | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 230 | lowRISC/opentitan | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 231 | openhwfoundation/cva6 | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 232 | KiCad/kicad-source-mirror | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 233 | adafruit/Adafruit_CircuitPython_Bundle | k-hardware | UNKNOWN | idea-only | other | Open ISA, synthesis, PCB, secure silicon | idea only, not built | n/a: curriculum ESTIMATE |
| 234 | google-ai-edge/mediapipe | k-human-behavior | UNKNOWN | idea-only | other | Pose/landmark perception, behavior data | idea only, not built | n/a: curriculum ESTIMATE |
| 235 | CMU-Perceptual-Computing-Lab/openpose | k-human-behavior | UNKNOWN | idea-only | other | Pose/landmark perception, behavior data | idea only, not built | n/a: curriculum ESTIMATE |
| 236 | MIT-LCP/mimic-code | k-human-behavior; k-medicine | UNKNOWN | idea-only | other | Pose/landmark perception, behavior data | idea only, not built | n/a: curriculum ESTIMATE |
| 237 | synthetichealth/synthea | k-medicine | UNKNOWN | idea-only | other | Open clinical code, synthetic patients, ontologies, offline readers | idea only, not built | n/a: curriculum ESTIMATE; not medical advice |
| 238 | openmedlab/Awesome-Medical-Dataset | k-medicine | UNKNOWN | idea-only | other | Open clinical code, synthetic patients, ontologies, offline readers | idea only, not built | n/a: curriculum ESTIMATE; not medical advice |
| 239 | kiwix/kiwix-tools | k-medicine | UNKNOWN | idea-only | other | Open clinical code, synthetic patients, ontologies, offline readers | idea only, not built | n/a: curriculum ESTIMATE; not medical advice |
| 240 | monarch-initiative/mondo | k-medicine | UNKNOWN | idea-only | other | Open clinical code, synthetic patients, ontologies, offline readers | idea only, not built | n/a: curriculum ESTIMATE; not medical advice |
| 241 | AllenInstitute/AllenSDK | k-neurology | UNKNOWN | idea-only | other | Open neuro datasets + formats | idea only, not built | n/a: curriculum ESTIMATE |
| 242 | bids-standard/bids-specification | k-neurology | UNKNOWN | idea-only | other | Open neuro datasets + formats | idea only, not built | n/a: curriculum ESTIMATE |
| 243 | OpenNeuroOrg/openneuro | k-neurology | UNKNOWN | idea-only | other | Open neuro datasets + formats | idea only, not built | n/a: curriculum ESTIMATE |
| 244 | neuropsychology/NeuroKit | k-physiology | UNKNOWN | idea-only | other | ECG/EDA/PPG signal processing | idea only, not built | n/a: curriculum ESTIMATE |
| 245 | MIT-LCP/wfdb-python | k-physiology | UNKNOWN | idea-only | other | ECG/EDA/PPG signal processing | idea only, not built | n/a: curriculum ESTIMATE |
| 246 | PIA-Group/BioSPPy | k-physiology | UNKNOWN | idea-only | other | ECG/EDA/PPG signal processing | idea only, not built | n/a: curriculum ESTIMATE |
| 247 | physiozoo/physiozoo | k-physiology | UNKNOWN | idea-only | other | ECG/EDA/PPG signal processing | idea only, not built | n/a: curriculum ESTIMATE |
| 248 | Qiskit/qiskit | k-quantum | UNKNOWN | idea-only | other | Quantum circuit SDKs + katas | idea only, not built | n/a: curriculum ESTIMATE |
| 249 | quantumlib/Cirq | k-quantum | UNKNOWN | idea-only | other | Quantum circuit SDKs + katas | idea only, not built | n/a: curriculum ESTIMATE |
| 250 | microsoft/QuantumKatas | k-quantum | UNKNOWN | idea-only | other | Quantum circuit SDKs + katas | idea only, not built | n/a: curriculum ESTIMATE |
| 251 | PennyLaneAI/pennylane | k-quantum | UNKNOWN | idea-only | other | Quantum circuit SDKs + katas | idea only, not built | n/a: curriculum ESTIMATE |
| 252 | qutip/qutip | k-quantum | UNKNOWN | idea-only | other | Quantum circuit SDKs + katas | idea only, not built | n/a: curriculum ESTIMATE |
| 253 | astropy/astropy | k-sciences | UNKNOWN | idea-only | other | Symbolic math, astronomy, chemistry, wiki engines | idea only, not built | n/a: curriculum ESTIMATE |
| 254 | wikimedia/mediawiki | k-sciences | UNKNOWN | idea-only | other | Symbolic math, astronomy, chemistry, wiki engines | idea only, not built | n/a: curriculum ESTIMATE |
| 255 | rdkit/rdkit | k-sciences | UNKNOWN | idea-only | other | Symbolic math, astronomy, chemistry, wiki engines | idea only, not built | n/a: curriculum ESTIMATE |
| 256 | kiwix/kiwix-js | k-sciences | UNKNOWN | idea-only | other | Symbolic math, astronomy, chemistry, wiki engines | idea only, not built | n/a: curriculum ESTIMATE |
| 257 | microsoft/agent-lightning | agent/bot optimization | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-08 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 258 | huggingface/smolagents | agent/bot optimization | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-10, OPT-13 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 259 | apache/airflow | workflow orchestration | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-12 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 260 | PrefectHQ/prefect | workflow orchestration | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-13, OPT-14 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 261 | temporalio/temporal | workflow orchestration | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-13, OPT-14, OPT-24 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 262 | openai/tiktoken | token efficiency | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-07, OPT-11 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 263 | zilliztech/GPTCache | token efficiency | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-05, OPT-06, OPT-09 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
| 264 | a2aproject/A2A | multi-agent collaboration | UNKNOWN | idea-only | other |  | LANDED: technique -> OPT-16, OPT-17 in PR #246 (https://github.com/vitalitychems-dot/TESSERA/pull/246) |  |
