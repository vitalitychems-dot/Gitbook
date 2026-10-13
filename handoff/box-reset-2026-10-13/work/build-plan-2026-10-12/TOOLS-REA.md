# morluto/rea — REA: Reverse Engineer Anything
- What: MCP server + CLI (`npx rea-agents`) for analysing binaries, JS/Electron apps, .NET, APKs, websites, SQLite, WASM, etc. Returns modules/imports/routes/pseudocode with evidence.
- License: MIT (third-party tools keep their own licenses). ~150k stars, active (pushed Oct 12).
- Install: Node 22.19+/24.11+/26+, npm. `npx rea-agents setup` edits agent MCP configs (backups made). Native analysis needs Ghidra (free) / Hopper / IDA (paid) — not needed for JS/static.
- Paid Claude? No. Works with any MCP agent (Cursor, Codex, Gemini CLI, Grok Build…). Analysis is local.
- Fit for our repos: Partial. REA targets compiled/packaged artifacts *without source*. For our own source repos, plain source tools (tree listing, dependency graphs, ripgrep, `analyze-javascript-application` on a repo dir) suffice. Useful for built Replit/Electron bundles we lost source for.
- Not cloned (npx is enough; no need to vendor).
- Risks: setup mutates agent configs — run only in a sandbox profile; runtime capture modes execute targets; disclaimer: own/authorized software only.
- **Verdict: USE (limited)** — static JS analysis on Father-owned repos only, via `npx -y rea-agents@latest analyze-javascript-application <dir> --json`, after Security gate. No Hopper/IDA, no runtime/device/network-capture modes.
