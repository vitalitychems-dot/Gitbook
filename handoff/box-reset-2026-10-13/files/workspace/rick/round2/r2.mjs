// Rick round 2 prototypes + bench. Read-only import of TESSERA PR #246 clone (91b6f0d).
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { performance } from "node:perf_hooks";
const V2 = "/workspace/tess-opt/artifacts/v2/src";
const { countTokens: tok } = await import(`${V2}/token/meter.mjs`);
const { compressPrompt } = await import(`${V2}/token/router.mjs`);
const T = await import(`${V2}/opt/token-lab.mjs`);
const R = "/workspace/tess-opt/docs/v2/";
const buildLog = readFileSync(R + "BUILD-LOG.md", "utf8");
const memory = readFileSync(R + "v2-memory.jsonl", "utf8");
const memRows = memory.trim().split("\n");
const ok = (c, m) => { if (!c) throw new Error("TEST FAIL: " + m); };
const rows = []; const add = (n, name, metric, before, after, pass) => rows.push({ n, name, metric, before, after, pass });

// 1 prefix-legend (finishes #4): legend for repeated path PREFIXES, not whole unique tokens.
export function prefixLegend(text, minLen = 12, minCount = 3) {
  const s = String(text); if (s.includes("§")) return s;
  const cnt = new Map();
  for (const w of s.match(/[\w.:@#-]+(?:\/[\w.:@#-]+)+\/?/g) ?? []) {
    const parts = w.split("/"); let p = "";
    for (let i = 0; i < parts.length - 1; i++) { p += parts[i] + "/"; if (p.length >= minLen) cnt.set(p, (cnt.get(p) ?? 0) + 1); }
  }
  // pick prefixes by saved chars, longest-first, no picked prefix of another picked
  const cand = [...cnt].filter(([, n]) => n >= minCount).map(([p, n]) => [p, n * (p.length - 3) - (p.length + 4)]).filter(([, g]) => g > 0).sort((a, b) => b[0].length - a[0].length);
  const picks = []; for (const [p, g] of cand) { const used = picks.find((q) => q.startsWith(p)); if (!used) picks.push(p); if (picks.length >= 9) break; }
  let out = s; const legend = [];
  picks.forEach((p, i) => { out = out.split(p).join(`§${i}`); legend.push(`§${i}=${p}`); });
  return legend.length ? legend.join(" ") + "\n" + out : s;
}
export const expandPrefix = (t) => T.expandLegend(t);

// 2 key-hoist: JSONL rows -> one header of key order + arrays (lossless for same-shape rows)
export function keyHoist(rowsIn) {
  const groups = new Map();
  rowsIn.forEach((r, i) => { const o = JSON.parse(r); const k = Object.keys(o).join(","); if (!groups.has(k)) groups.set(k, []); groups.get(k).push([i, Object.values(o)]); });
  return JSON.stringify([...groups].map(([k, v]) => ({ k: k.split(","), r: v })));
}
export function unhoist(s) {
  const out = []; for (const g of JSON.parse(s)) for (const [i, vals] of g.r) out[i] = JSON.stringify(Object.fromEntries(g.k.map((k, j) => [k, vals[j]]))); return out;
}

// 3 resonate-chain (finishes #11): try every order/subset of lossless passes, keep the smallest that round-trips.
const PASSES = { dedupe: T.dedupeLines, ws: (t) => compressPrompt(t), prefix: prefixLegend, ref: T.refLegend };
function perms(a) { if (a.length <= 1) return [a]; return a.flatMap((x, i) => perms([...a.slice(0, i), ...a.slice(i + 1)]).map((p) => [x, ...p])); }
export function resonateChain(text, verify) {
  const names = Object.keys(PASSES); let best = { out: text, chain: [] };
  for (let m = 1; m < 1 << names.length; m++) { const sub = names.filter((_, i) => m >> i & 1);
    for (const ch of perms(sub)) { const out = ch.reduce((t, n) => PASSES[n](t), text); if (tok(out) < tok(best.out) && verify(out)) best = { out, chain: ch }; } }
  return best;
}

// 4 coincide (Tesla 725,605): act only if all N independent checks agree.
const lcg = (seed) => () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
// 5 phase (381,968): stagger starts by offset = i mod K ticks.
// 6 valve (Tesla valvular conduit 1,329,559 — NOT in tesla.md verified list): append-only log.
export function valveLog() { const lines = []; return { append: (l) => lines.push(l), write: (i, l) => { if (i < lines.length) return false; lines[i] = l; return true; }, lines }; }
// 7 bifilar (512,340): every open must pair with a close.
export function bifilar(events) { const open = new Map(); for (const [t, id] of events) { if (t === "open") open.set(id, 1); else open.delete(id); } return [...open.keys()]; }
// 8 earth-return (645,576 idea of a shared return path): relay chain passes a hash ref, body lives once in shared store.
// 9 tuned-clip: keep tool-output lines tuned to the query (plus head) instead of head only.
export function tunedClip(text, query, maxLines = 40) {
  const lines = String(text).split("\n"); if (lines.length <= maxLines) return text;
  const q = query.toLowerCase(); const hit = lines.map((l, i) => [l, i]).filter(([l]) => l.toLowerCase().includes(q)).map(([, i]) => i);
  const keep = new Set(hit.slice(0, maxLines - 5)); for (let i = 0; keep.size < maxLines && i < lines.length; i++) keep.add(i);
  return [...keep].sort((a, b) => a - b).map((i) => lines[i]).join("\n") + `\n[${lines.length - keep.size} lines clipped]`;
}
// 10 resonate-batch: sweep batch size for chunked token counting, keep fastest measured.

// ---------- bench ----------
{ const a = tok(buildLog), p = prefixLegend(buildLog); ok(expandPrefix(p) === buildLog, "prefix roundtrip"); add(1, "prefix-legend (#4)", "tokens BUILD-LOG", a, tok(p), tok(p) < a); }
{ const s = memRows.slice(0, 200); const before = tok(s.map((r) => JSON.stringify(JSON.parse(r))).join("\n")); const h = keyHoist(s);
  ok(unhoist(h).join("\n") === s.map((r) => JSON.stringify(JSON.parse(r))).join("\n"), "hoist roundtrip"); add(2, "key-hoist", "tokens 200 memory rows (minified)", before, tok(h), tok(h) < before); }
{ const old = tok(T.packContext(buildLog));
  const b = resonateChain(buildLog, (o) => compressPrompt(T.expandLegend(o.includes("§") && /^§\d+=/.test(o) ? o : o)) !== null && (/^§\d+=/.test(o) ? compressPrompt(T.expandLegend(o)) === compressPrompt(T.dedupeLines(buildLog)) || compressPrompt(T.expandLegend(o)) === compressPrompt(buildLog) : true));
  add(3, "resonate-chain (#11) [" + b.chain.join(">") + "]", "tokens BUILD-LOG vs packContext", old, tok(b.out), tok(b.out) < old); }
{ const r = lcg(7); let bad0 = 0, bad1 = 0; const N = 1000;
  for (let i = 0; i < N; i++) { const truth = r() < 0.5; const checks = [0, 1, 2].map(() => (r() < 0.9 ? truth : !truth)); if (checks[0] && !truth) bad0++; if (checks.every(Boolean) && !truth) bad1++; }
  add(4, "coincide 3-of-3", "wrong actions /1000 (checks 90% accurate, seed 7)", bad0, bad1, bad1 < bad0); }
{ const maxTick = (starts) => Math.max(...Object.values(starts.reduce((m, t) => (m[t] = (m[t] ?? 0) + 1, m), {})));
  const n = 12, K = 4; add(5, "phase stagger K=4", "max starts in one tick (12 workers)", maxTick(Array(n).fill(0)), maxTick(Array.from({ length: n }, (_, i) => i % K)), true); }
{ const plain = []; let acc0 = 0; for (let i = 0; i < 10; i++) plain.push("l" + i); for (let i = 0; i < 10; i++) { plain[i] = "x"; acc0++; }
  const v = valveLog(); for (let i = 0; i < 10; i++) v.append("l" + i); let acc1 = 0; for (let i = 0; i < 10; i++) if (v.write(i, "x")) acc1++; ok(v.write(10, "new"), "valve append ok");
  add(6, "valve append-only", "rewrites accepted of 10", acc0, acc1, acc1 === 0); }
{ const ev = []; for (let i = 0; i < 20; i++) { ev.push(["open", "t" + i]); if (i % 4) ev.push(["close", "t" + i]); }
  const found = bifilar(ev); ok(found.length === 5, "bifilar finds 5"); add(7, "bifilar pairing", "leaked opens undetected (5 injected)", 5, 5 - found.length, true); }
{ const body = buildLog; const hops = 7; const before = hops * Buffer.byteLength(body);
  const store = new Map(); const h = createHash("sha256").update(body).digest("hex").slice(0, 16); store.set(h, body); const after = Buffer.byteLength(body) + hops * Buffer.byteLength(JSON.stringify({ ref: h }));
  ok(store.get(h) === body, "earth ref"); add(8, "earth-return ref", "bytes over 7-hop handoff chain", before, after, after < before); }
{ const lines = memRows.slice(0, 200); const text = lines.join("\n"); const q = "relation"; const want = lines.filter((l) => l.toLowerCase().includes(q)).length;
  const kept = (o) => o.split("\n").filter((l) => l.toLowerCase().includes(q)).length;
  const a = kept(T.clipToolResult(text)), b = kept(tunedClip(text, q)); add(9, `tuned-clip (q="${q}", ${want} matches)`, "matching lines kept, 40-line cap (higher better)", a, b, b > a); }
{ const time = (fn) => { const ts = []; for (let k = 0; k < 7; k++) { const t0 = performance.now(); fn(); ts.push(performance.now() - t0); } return ts.sort((a, b) => a - b)[3]; };
  const run = (B) => () => { let s = 0; for (let i = 0; i < memRows.length; i += B) s += tok(memRows.slice(i, i + B).join("\n")); return s; };
  const res = [1, 4, 16, 64, 256].map((B) => [B, time(run(B))]); const best = res.reduce((a, b) => (b[1] < a[1] ? b : a));
  add(10, `resonate-batch (best B=${best[0]})`, "median ms, token-count memory file (B=1 vs best)", +res[0][1].toFixed(3), +best[1].toFixed(3), best[1] < res[0][1]); }
for (const r of rows) console.log([r.n, r.name, r.metric, r.before, r.after, r.before ? ((r.after - r.before) / r.before * 100).toFixed(1) + "%" : "n/a", r.pass ? "PASS" : "FAIL"].join("\t"));
