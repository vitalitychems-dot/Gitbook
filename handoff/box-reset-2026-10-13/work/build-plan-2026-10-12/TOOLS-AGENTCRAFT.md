# AgentCraft — https://github.com/blendi-remade/agentcraft
- What: Fabric mod (Minecraft view) + Node 22/TS "Foreman" that runs a lead + up to 5 Claude Agent SDK workers on a real git repo (task graph, message bus, memory, decision queue, per-task worktrees, guarded merges). WebSocket on 127.0.0.1:7878.
- License: MIT. ~720 stars, last push Oct 7.
- Requirements: Java 25, Node 22+, git, **Minecraft: Java Edition 26.3 (paid licence)**, Fabric Loader 0.19.5+, Fabric API 0.161.0+. Gradle downloads Minecraft/Fabric.
- Cost: `--backend sim` (scripted team) needs no API key; real agents need ANTHROPIC_API_KEY / Bedrock / Vertex / Foundry or a Claude Code login (paid). Playing the game view needs a purchased Minecraft account; Foreman + `npm run tui` runs without the game.
- Risks: agents act on real repos with merge capability (must point at sandbox clone only, never TESSERA main); Claude-only backend (no Grok/xAI backend); Windows/macOS launchers (Linux via tools/unix.mjs); heavy GUI on box.
- **Verdict: SKIP for now / BLOCKED for real use** (needs paid Minecraft + paid Claude). Optional later: run Foreman `sim` backend headless in a sandbox as a visualization/task-graph prototype, or borrow its TaskGraph/DecisionQueue design for our own mesh map.
