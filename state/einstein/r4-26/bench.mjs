const base = "/workspace/einstein/r4/artifacts/v2/src/brain/";
const N = await import(base + "affect.mjs"), O = await import(base + "__old_affect.mjs");
const { MESHLOG } = await import(base + "meshlog-labels.mjs"); const { HELDOUT } = await import(base + "heldout.mjs");
const lines = [...MESHLOG, ...HELDOUT].map((x) => x.text);
let mism = 0; for (const t of lines) if (JSON.stringify(N.classify(t)) !== JSON.stringify(O.classify(t))) mism++;
const time = (M) => { const r = []; for (let k = 0; k < 9; k++) { const a = performance.now(); for (let i = 0; i < 20; i++) for (const t of lines) M.classify(t); r.push((performance.now() - a) / (20 * lines.length) * 1000); } r.sort((a, b) => a - b); return r[4]; };
time(O); time(N); const o = time(O), n = time(N);
console.log(JSON.stringify({ lines: lines.length, mismatches: mism, oldUsPerClassify: +o.toFixed(2), newUsPerClassify: +n.toFixed(2), speedup: +(o / n).toFixed(2) }));
