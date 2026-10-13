import { it, vi } from "vitest";
import { execSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
// REAL data: every tracked .md file in TESSERA, whole-file text, repo order.
it("cache-key wrong-return bench", async () => {
  delete process.env.TESSERA_EMBED_MODEL;
  const root = execSync("git rev-parse --show-toplevel").toString().trim();
  const files = execSync("git ls-files '*.md'", { cwd: root }).toString().trim().split("\n");
  const texts = files.map(f => readFileSync(`${root}/${f}`, "utf8")).filter(t => t.trim().length > 0);
  const shared = await import("../lib/neural-embeddings");
  const got: number[][] = [];
  for (const t of texts) got.push(await shared.generateEmbedding(t));
  const wrong: number[] = [];
  for (let i = 0; i < texts.length; i++) {
    vi.resetModules();
    const fresh = await import("../lib/neural-embeddings");
    const v = await fresh.generateEmbedding(texts[i]);
    let d = 0; for (let k = 0; k < v.length; k++) d = Math.max(d, Math.abs(v[k] - got[i][k]));
    wrong.push(d > 1e-12 ? 1 : 0);
  }
  writeFileSync(process.env.BENCH_OUT!, JSON.stringify({ n: texts.length, wrong }));
}, 600000);
