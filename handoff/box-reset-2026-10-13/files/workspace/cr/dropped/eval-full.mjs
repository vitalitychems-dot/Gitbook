/**
 * Local-only eval. Reads the private corpus from TESSERA_CREATOR_DIR (default
 * [REDACTED-PATH] prints aggregate metrics only, writes detail back into that dir.
 * Usage: node src/brain/creator/eval.mjs
 */
import fs from "node:fs"; import path from "node:path";
import { profile, score, auc, update } from "./style.mjs";
import { topicOf } from "./topics.mjs";
import { evaluate, createPredictor } from "./predict.mjs";
import { createProfile } from "./profile.mjs";
const D = process.env.TESSERA_CREATOR_DIR ?? "[REDACTED-PATH]
const jl = (f) => fs.existsSync(path.join(D, f)) ? fs.readFileSync(path.join(D, f), "utf8").split("\n").filter(Boolean).map((l) => JSON.parse(l)) : [];
const father = jl("father-msgs.jsonl"); const others = jl("other-text.jsonl").map((o) => o.text);
// 1. authorship: leave-one-out for creator; others split in half (train/test)
const oTr = others.filter((_, i) => i % 2 === 0), oTe = others.filter((_, i) => i % 2 === 1);
const O = profile(oTr); const pos = father.map((m, i) => score(profile(father.filter((_, j) => j !== i).map((x) => x.text)), O, m.text));
const F = profile(father.map((m) => m.text)); const neg = oTe.map((s) => score(F, O, s));
const lenAuc = auc(father.map((m) => -m.text.length), oTe.map((s) => -s.length));
// 2. predictor: chronological request stream
const stream = jl("request-stream.jsonl").sort((a, b) => a.t - b.t); const seq = stream.map((r) => topicOf(r.text));
const split = Math.floor(seq.length * 0.6); const pred = evaluate(seq, split);
// 3. profile with online sync log
const P = createProfile(); for (const r of stream.filter((r) => r.own)) P.ingest(r);
const p2 = createPredictor(); for (const t of seq) p2.observe(t);
const res = { authorship: { auc: auc(pos, neg), length_only_auc: lenAuc, n_pos: pos.length, n_neg: neg.length }, predictor: pred, stream_n: seq.length, topics: seq, next: p2.rank().slice(0, 5), profile: P.snapshot(), sync_log: P.log };
fs.writeFileSync(path.join(D, "eval-result.json"), JSON.stringify(res, null, 1), { mode: 0o600 });
console.log(JSON.stringify({ authorship: res.authorship, predictor: pred, next: res.next, profile_items: res.profile.length }, null, 1));
