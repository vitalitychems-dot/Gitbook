import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const script = fileURLToPath(new URL("./admit.mjs", import.meta.url));
const run = (input) => spawnSync(process.execPath, [script], { input, encoding: "utf8" });

test("rejects drop missing Lane: trailer", () => {
  const r = run("Fix sort\n\nRefs 9004959b\n");
  assert.equal(r.status, 1);
  assert.match(r.stderr, /Missing 'Lane:' trailer/);
});

test("rejects drop missing commit SHA", () => {
  const r = run("Fix sort\n\nLane: GB-063\n");
  assert.equal(r.status, 1);
  assert.match(r.stderr, /Missing commit SHA/);
});

test("admits valid drop", () => {
  const r = run("Fix sort\n\nRefs 9004959b\nLane: GB-063\n");
  assert.equal(r.status, 0);
  assert.match(r.stdout, /admit: Admitted/);
});
