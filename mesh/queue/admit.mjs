#!/usr/bin/env node
// admit.mjs: reject a drop (commit message or text note) missing a Lane: trailer or a commit SHA.
// Usage: node admit.mjs <drop-file>   |   git log -1 --format=%B | node admit.mjs
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const LANE = /^Lane:[ \t]*\S.*$/im;          // trailer line, non-empty value
const SHA = /(?<![0-9a-f])[0-9a-f]{7,40}(?![0-9a-f])/i;

export function admitDrop(text) {
  if (!text || !text.trim()) return { ok: false, reason: "Empty drop." };
  if (!LANE.test(text)) return { ok: false, reason: "Missing 'Lane:' trailer." };
  if (!SHA.test(text)) return { ok: false, reason: "Missing commit SHA (7-40 hex)." };
  return { ok: true, reason: "Admitted." };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const src = process.argv[2];
  let text;
  try { text = readFileSync(src ?? 0, "utf8"); }
  catch (e) { console.error(`reject: cannot read drop: ${e.message}`); process.exit(2); }
  const r = admitDrop(text);
  if (r.ok) { console.log(`admit: ${r.reason}`); process.exit(0); }
  console.error(`reject: ${r.reason}`); process.exit(1);
}
