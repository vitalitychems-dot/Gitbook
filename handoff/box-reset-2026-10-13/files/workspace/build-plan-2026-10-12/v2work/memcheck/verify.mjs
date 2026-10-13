import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import path from "node:path";

const mem = "/workspace/build-plan-2026-10-12/v2-memory.jsonl";
const transport = new StdioClientTransport({
  command: "npx",
  args: ["-y", "@modelcontextprotocol/server-memory"],
  env: { ...process.env, MEMORY_FILE_PATH: mem },
});
const client = new Client({ name: "v2-memcheck", version: "1.0.0" });
await client.connect(transport);
const tools = await client.listTools();
console.log("TOOLS", tools.tools.map(t => t.name).join(","));
const result = await client.callTool({ name: "read_graph", arguments: {} });
const text = result.content?.map(c => c.text || "").join("") || JSON.stringify(result);
let graph;
try { graph = JSON.parse(text); } catch { graph = null; console.log("RAW_HEAD", text.slice(0,500)); }
if (graph) {
  console.log("LOAD_OK entities=", graph.entities?.length, "relations=", graph.relations?.length);
  // spot check
  const names = new Set(graph.entities.map(e => e.name));
  for (const n of ["TESSERA_v2","module_agents_studio","reconurge/flowsint","@modelcontextprotocol/server-memory","blendi-remade/agentcraft"]) {
    console.log("HAS", n, names.has(n));
  }
}
await client.close();
process.exit(graph ? 0 : 1);
