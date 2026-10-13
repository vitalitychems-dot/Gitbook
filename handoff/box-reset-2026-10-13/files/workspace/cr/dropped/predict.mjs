/**
 * Next-ask predictor: blends a first-order transition table with recency-decayed topic frequency.
 * `streaming` updates after every observed ask; `frozen` keeps the training-time tables.
 */
export function createPredictor({ decay = 0.85, mix = 0.5 } = {}) {
  const freq = new Map(); const trans = new Map(); let last = null;
  return {
    observe(topic) {
      for (const [k, v] of freq) freq.set(k, v * decay); freq.set(topic, (freq.get(topic) ?? 0) + 1);
      if (last) { const r = trans.get(last) ?? new Map(); r.set(topic, (r.get(topic) ?? 0) + 1); trans.set(last, r); }
      last = topic;
    },
    setLast(t) { last = t; },
    rank() {
      const s = new Map(); const fz = [...freq.values()].reduce((a, b) => a + b, 0) || 1;
      for (const [k, v] of freq) s.set(k, (1 - mix) * v / fz);
      const r = last && trans.get(last); if (r) { const z = [...r.values()].reduce((a, b) => a + b, 0); for (const [k, v] of r) s.set(k, (s.get(k) ?? 0) + mix * v / z); }
      return [...s].sort((a, b) => b[1] - a[1]).map((x) => x[0]);
    },
  };
}
export function mostFrequent(train) { const c = new Map(); for (const t of train) c.set(t, (c.get(t) ?? 0) + 1); return [...c].sort((a, b) => b[1] - a[1]).map((x) => x[0]); }
/** Chronological eval. Returns top1/top3 for baseline, frozen, streaming. */
export function evaluate(seq, split, opts) {
  const train = seq.slice(0, split), test = seq.slice(split); const base = mostFrequent(train);
  const fz = createPredictor(opts), st = createPredictor(opts); for (const t of train) { fz.observe(t); st.observe(t); }
  const acc = { baseline: [0, 0], frozen: [0, 0], streaming: [0, 0] }; let prev = train.at(-1);
  for (const t of test) {
    fz.setLast(prev); const rf = fz.rank(), rs = st.rank();
    for (const [k, r] of [["baseline", base], ["frozen", rf], ["streaming", rs]]) { acc[k][0] += r[0] === t ? 1 : 0; acc[k][1] += r.slice(0, 3).includes(t) ? 1 : 0; }
    st.observe(t); prev = t;
  }
  const n = test.length || 1; const o = { n: test.length }; for (const k in acc) o[k] = { top1: acc[k][0] / n, top3: acc[k][1] / n }; return o;
}
