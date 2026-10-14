#!/usr/bin/env node
// admit.mjs: reject a drop (commit message or text note) that lacks a real
// `Lane: <value>` git trailer or a commit SHA.
// Usage: node admit.mjs [--repo <path>] [<drop-file>]   (reads stdin if no file)
//   git log -1 --format=%B | node admit.mjs --repo .
// Exit 0 = admitted, 1 = rejected (reason on stderr), 2 = usage/read error.
import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const TRAILER_LINE = /^[A-Za-z0-9][A-Za-z0-9-]*:[ \t]*\S/; // Key: value
const CONTINUATION = /^[ \t]+\S/;                          // folded trailer value
const LANE = /^Lane:[ \t]*(\S.*)$/;
const HEX_WORD = /(?<![0-9A-Za-z])[0-9a-fA-F]{7,40}(?![0-9A-Za-z])/g;

/** Final paragraph, if every line in it is a trailer (git's trailer block). */
export function trailerBlock(text) {
  const paras = text.replace(/\r\n/g, "\n").trim().split(/\n[ \t]*\n/);
  if (paras.length < 2) return null; // a trailer block follows a subject/body
  const lines = paras[paras.length - 1].split("\n");
  if (!TRAILER_LINE.test(lines[0])) return null;
  return lines.every((l) => TRAILER_LINE.test(l) || CONTINUATION.test(l)) ? lines : null;
}

/** Hex words of 7-40 chars containing at least one digit and one letter. */
export function shaCandidates(text) {
  return (text.match(HEX_WORD) ?? []).filter((w) => /\d/.test(w) && /[a-f]/i.test(w));
}

export function resolves(repo, sha) {
  const r = spawnSync("git", ["-C", repo, "cat-file", "-e", `${sha}^{commit}`], { stdio: "ignore" });
  return r.status === 0;
}

export function admitDrop(text, { repo } = {}) {
  if (!text || !text.trim()) return { ok: false, reason: "Empty drop." };
  const block = trailerBlock(text);
  if (!block || !block.some((l) => LANE.test(l)))
    return { ok: false, reason: "Missing 'Lane: <value>' git trailer in the final paragraph." };
  const shas = shaCandidates(text);
  if (shas.length === 0)
    return { ok: false, reason: "Missing commit SHA (7-40 hex, with at least one digit and one letter)." };
  if (repo !== undefined && !shas.some((s) => resolves(repo, s)))
    return { ok: false, reason: `No SHA resolves to a commit in ${repo}: ${shas.join(", ")}.` };
  return { ok: true, reason: "Admitted." };
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--repo") {
      if (!argv[i + 1]) throw new Error("--repo needs a path");
      out.repo = argv[++i];
    } else if (out.file === undefined) out.file = argv[i];
    else throw new Error(`unexpected argument: ${argv[i]}`);
  }
  return out;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  let args, text;
  try { args = parseArgs(process.argv.slice(2)); text = readFileSync(args.file ?? 0, "utf8"); }
  catch (e) { console.error(`reject: ${e.message}`); process.exit(2); }
  const r = admitDrop(text, { repo: args.repo });
  if (r.ok) { console.log(`admit: ${r.reason}`); process.exit(0); }
  console.error(`reject: ${r.reason}`); process.exit(1);
}
