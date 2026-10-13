import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { spawnSync, execFileSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const script = fileURLToPath(new URL("./admit.mjs", import.meta.url));
const run = (input, args = []) => spawnSync(process.execPath, [script, ...args], { input, encoding: "utf8" });

let repo, head;
before(() => {
  repo = mkdtempSync(join(tmpdir(), "admit-"));
  const g = (...a) => execFileSync("git", ["-C", repo, ...a], { encoding: "utf8" }).trim();
  g("init", "-q");
  g("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "seed");
  head = g("rev-parse", "HEAD");
});
after(() => rmSync(repo, { recursive: true, force: true }));

test("rejects hex-only word 'defaced' as a SHA", () => {
  const r = run("Fix sort, defaced the table\n\nLane: GB-063\n");
  assert.equal(r.status, 1);
  assert.match(r.stderr, /Missing commit SHA/);
});

test("rejects Lane: in the body but not in the trailer block", () => {
  const r = run("Fix sort\n\nLane: GB-063\nRefs 9004959b\n\nThat is all.\n");
  assert.equal(r.status, 1);
  assert.match(r.stderr, /Missing 'Lane: <value>' git trailer/);
});

test("rejects SHA that does not resolve with --repo", () => {
  const r = run("Fix sort\n\nRefs 9004959b\n\nLane: GB-063\n", ["--repo", repo]);
  assert.equal(r.status, 1);
  assert.match(r.stderr, /No SHA resolves to a commit/);
});

test("admits valid drop (no --repo)", () => {
  const r = run("Fix sort\n\nRefs 9004959b\n\nLane: GB-063\n");
  assert.equal(r.status, 0);
  assert.match(r.stdout, /admit: Admitted/);
});

test("admits valid drop whose SHA resolves with --repo", () => {
  const r = run(`Fix sort\n\nRefs ${head.slice(0, 12)}\n\nLane: GB-063\n`, ["--repo", repo]);
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /admit: Admitted/);
});
