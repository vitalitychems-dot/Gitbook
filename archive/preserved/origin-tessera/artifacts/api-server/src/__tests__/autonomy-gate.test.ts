import { describe, it, expect, afterEach } from "vitest";
import { mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync } from "fs";
import { tmpdir } from "os";
import { join, resolve } from "path";
import { GATED_LOOPS, loopEnabled, refuseIfDisabled, type GatedLoop } from "../lib/autonomy-gate";
import { protectedProposalPath, reviewSelfEdit, textualDiff } from "../lib/self-edit-guard";
import {
  ACTIVATING_VALUE,
  FLAG_DEFINITIONS,
  IMPROVEMENT_LOOPS,
  MINOR_LOCK_MS,
  ORIGIN_MARK,
  SELF_IMPROVEMENT_MODULE,
  SERIOUS_LOCK_MS,
  VOW_RULES,
  VOW_STATEMENTS,
  applyTripwire,
  findRepoRoot,
  flagActivates,
  flagsForcedOff,
  improvementMayRun,
  isImprovementLoop,
  isProtectedPath,
  parseLock,
  penaltyFor,
  readLock,
  restingLock,
  wordUnlocks,
  writeLock,
  type LockState,
} from "../../../../guard/index";

const SRC = resolve(__dirname, "..");
const ROOT = resolve(SRC, "..");
const saved = new Map<string, string | undefined>();

afterEach(() => {
  for (const [key, value] of saved) {
    if (value === undefined) delete process.env[key];
    else process.env[key] = value;
  }
  saved.clear();
});

function remember(key: string, value: string | undefined): void {
  if (!saved.has(key)) saved.set(key, process.env[key]);
  if (value === undefined) delete process.env[key];
  else process.env[key] = value;
}

function walk(dir: string, out: string[] = []): string[] {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (p.endsWith(".ts")) out.push(p);
  }
  return out;
}

function functionSlice(source: string, name: string): string {
  const marker = `function ${name}`;
  const at = source.indexOf(marker);
  if (at < 0) throw new Error(`missing function ${name}`);
  let end = source.length;
  for (const next of ["\nfunction ", "\nexport function ", "\nasync function ", "\nexport async function "]) {
    const found = source.indexOf(next, at + marker.length);
    if (found > at) end = Math.min(end, found);
  }
  return source.slice(at, end);
}

describe("gated loops default off", () => {
  it("is off when the flag is unset, and on only for the exact value 1", () => {
    for (const name of Object.keys(GATED_LOOPS) as GatedLoop[]) {
      remember(GATED_LOOPS[name], undefined);
      expect(loopEnabled(name)).toBe(false);
      expect(refuseIfDisabled(name)).toBe(true);
      remember(GATED_LOOPS[name], "true");
      expect(loopEnabled(name)).toBe(false);
      remember(GATED_LOOPS[name], "1");
      if (isImprovementLoop(name)) {
        expect(loopEnabled(name)).toBe(false);
        expect(refuseIfDisabled(name)).toBe(true);
      } else {
        expect(loopEnabled(name)).toBe(true);
        expect(refuseIfDisabled(name)).toBe(false);
      }
      remember(GATED_LOOPS[name], undefined);
    }
  });
});

describe("removed modules are not on the boot path", () => {
  const REMOVED = ["wallet-observer", "income-executor", "free-stuff-scraper", "code-bounties-real", "lead-execution"];

  it("nothing under src/ imports them", () => {
    const offenders: string[] = [];
    for (const file of walk(SRC)) {
      const text = readFileSync(file, "utf8");
      for (const name of REMOVED) {
        if (new RegExp(`from\\s+["'][^"']*${name}["']`).test(text)) offenders.push(`${file} -> ${name}`);
      }
    }
    expect(offenders).toEqual([]);
  });

  it("boot files do not name their starters", () => {
    const boot = ["app.ts", "index.ts", "routes/index.ts"].map((f) => readFileSync(join(SRC, f), "utf8")).join("\n");
    for (const name of ["startWalletObserver", "startIncomeExecutor", "startFreeStuffScraper", "startBountyRefresher", "initFileRegistry(", "initAgentSpawner(", "seedForumFromRealData(", "initShepherdPersistence("]) {
      expect(boot.includes(name)).toBe(false);
    }
  });
});

describe("with no flags, gated loops do not register timers at boot", () => {
  const STARTS: Array<{ file: string; fn: string; loop: GatedLoop }> = [
    { file: "lib/consciousness-engine.ts", fn: "startConsciousnessEngine", loop: "consciousness-engine" },
    { file: "lib/personality-evolution.ts", fn: "startPersonalityEvolution", loop: "personality-evolution" },
    { file: "lib/auto-improvement-daemon.ts", fn: "startAutoImprovementDaemon", loop: "auto-improvement-daemon" },
    { file: "lib/recursive-self-improvement.ts", fn: "startRecursiveImprovementLoop", loop: "recursive-self-improvement" },
  ];

  it("each start function returns before setSacredInterval unless its flag is on", () => {
    for (const { file, fn, loop } of STARTS) {
      const body = functionSlice(readFileSync(join(SRC, file), "utf8"), fn);
      const guard = body.indexOf(`refuseIfDisabled("${loop}")`);
      const timer = body.indexOf("setSacredInterval");
      expect(guard).toBeGreaterThanOrEqual(0);
      expect(timer).toBeGreaterThan(guard);
    }
  });

  it("app.ts only calls those starters inside loopEnabled", () => {
    const app = readFileSync(join(SRC, "app.ts"), "utf8");
    const checks: Array<[string, GatedLoop]> = [
      ["startConsciousnessEngine(", "consciousness-engine"],
      ["startPersonalityEvolution(", "personality-evolution"],
      ["startAutoImprovementDaemon(", "auto-improvement-daemon"],
      ["startRecursiveImprovementLoop(", "recursive-self-improvement"],
      ["initSelfCodeEvolution(", "self-code-evolution"],
    ];
    for (const [call, loop] of checks) {
      const at = app.indexOf(call);
      expect(at).toBeGreaterThan(0);
      const window = app.slice(Math.max(0, at - 280), at);
      expect(window.includes(`loopEnabled("${loop}")`)).toBe(true);
    }
  });

  it("self-code source writes are behind TESSERA_ENABLE_SELF_CODE_EVOLUTION", () => {
    const src = readFileSync(join(SRC, "lib/self-code-evolution.ts"), "utf8");
    const apply = functionSlice(src, "applyVerifiedPatch");
    const guard = apply.indexOf('loopEnabled("self-code-evolution")');
    const write = apply.indexOf("writeFileSync");
    expect(guard).toBeGreaterThanOrEqual(0);
    expect(write).toBeGreaterThan(guard);
    const patch = functionSlice(src, "applyPatchToSourceFile");
    expect(patch.indexOf("assertSelfModificationAllowed")).toBeGreaterThanOrEqual(0);
    expect(patch.indexOf("assertSelfModificationAllowed")).toBeLessThan(patch.indexOf("writeFileSync"));
    expect(readFileSync(join(ROOT, "src/lib/autonomy-gate.ts"), "utf8")).toContain("TESSERA_ENABLE_SELF_CODE_EVOLUTION");
  });
});

describe("every remaining boot loop is gated", () => {
  const STARTS: Array<{ file: string; fn: string; loop: GatedLoop; timer: string }> = [
    { file: "lib/ingestion/scheduler.ts", fn: "startIngestionScheduler", loop: "ingestion-scheduler", timer: "setTimeout" },
    { file: "lib/ingestion/shepherd-agents.ts", fn: "startShepherdLoop", loop: "shepherd-loop", timer: "setSacredInterval" },
    { file: "lib/knowledge-canon-bridge.ts", fn: "startKnowledgeToCanonBridge", loop: "knowledge-canon-bridge", timer: "setSacredInterval" },
    { file: "lib/canonUpdater.ts", fn: "startPeriodicRegeneration", loop: "canon-regeneration", timer: "setSacredInterval" },
    { file: "lib/dual-brain.ts", fn: "startDualBrain", loop: "dual-brain", timer: "setSacredInterval" },
    { file: "lib/identity-reinforcement.ts", fn: "startIdentityReinforcement", loop: "identity-reinforcement", timer: "setSacredInterval" },
    { file: "lib/agi-training-engine.ts", fn: "startAGITrainingEngine", loop: "agi-training", timer: "setSacredInterval" },
    { file: "lib/council-executor.ts", fn: "startCouncilExecutor", loop: "council-executor", timer: "setSacredInterval" },
    { file: "lib/red-team-agent.ts", fn: "startRedTeamAgent", loop: "red-team", timer: "setSacredInterval" },
    { file: "lib/auto-healer.ts", fn: "startAutoHealer", loop: "auto-healer", timer: "setSacredInterval" },
    { file: "lib/autonomous-heartbeat.ts", fn: "startAutonomousHeartbeat", loop: "autonomous-heartbeat", timer: "setSacredInterval" },
    { file: "lib/rick-autonomous-loop.ts", fn: "startRickAutonomousLoop", loop: "rick-loop", timer: "setSacredInterval" },
    { file: "lib/sovereign-knowledge-autonomy.ts", fn: "startKnowledgeAutonomyLoop", loop: "knowledge-autonomy", timer: "setSacredInterval" },
    { file: "lib/cross-domain-synthesis.ts", fn: "startCrossDomainSynthesisLoop", loop: "cross-domain-synthesis", timer: "setSacredInterval" },
    { file: "lib/sovereign-memory-vault.ts", fn: "startSovereignMemoryVaultLoop", loop: "sovereign-memory-vault", timer: "setSacredInterval" },
    { file: "lib/autonomous-forum-engine.ts", fn: "startAutonomousForumLoop", loop: "autonomous-forum", timer: "setSacredInterval" },
    { file: "lib/sovereign-loop.ts", fn: "startSovereignLoop", loop: "sovereign-loop", timer: "setSacredInterval" },
    { file: "lib/sovereign-loop.ts", fn: "rescheduleLoop", loop: "sovereign-loop", timer: "setSacredInterval" },
    { file: "lib/agi/metacognition.ts", fn: "startMetacognitionLoop", loop: "metacognition", timer: "setSacredInterval" },
    { file: "lib/lattice-heartbeat.ts", fn: "startLatticeHeartbeat", loop: "lattice-heartbeat", timer: "setSacredInterval" },
    { file: "lib/anomaly-detection.ts", fn: "startAnomalyMonitor", loop: "anomaly-monitor", timer: "setSacredInterval" },
    { file: "lib/sovereign-cipher.ts", fn: "startAutonomousRotation", loop: "cipher-rotation", timer: "setSacredInterval" },
    { file: "lib/lattice-frequency-bands.ts", fn: "startBandRotationScheduler", loop: "band-rotation", timer: "setSacredInterval" },
    { file: "lib/autonomous-build-cycle.ts", fn: "startAutonomousBuildCycleTimer", loop: "autonomous-build", timer: "setSacredInterval" },
    { file: "lib/autonomous-wiring.ts", fn: "startAutonomousOperation", loop: "autonomous-wiring", timer: "startScheduler" },
    { file: "lib/session-mesh.ts", fn: "startMeshHeartbeatMonitor", loop: "mesh-heartbeat", timer: "setSacredInterval" },
    { file: "lib/auto-recovery.ts", fn: "startRouteHealthMonitor", loop: "route-health", timer: "setSacredInterval" },
    { file: "lib/auto-recovery.ts", fn: "startRecoveryWatchdog", loop: "recovery-watchdog", timer: "setSacredInterval" },
    { file: "lib/vector-memory.ts", fn: "scheduleBackgroundReembedding", loop: "vector-reembed", timer: "setSacredInterval" },
    { file: "lib/consensus-engine.ts", fn: "startRetryProcessor", loop: "consensus-retry", timer: "setSacredInterval" },
    { file: "lib/memory-consolidation-engine.ts", fn: "startConsolidationEngine", loop: "memory-consolidation", timer: "setSacredInterval" },
    { file: "lib/recursive-reflection-loop.ts", fn: "startRecursiveReflectionLoop", loop: "recursive-reflection", timer: "setSacredInterval" },
    { file: "lib/dimensional-lru-cache.ts", fn: "startDimensionalCacheMaintenance", loop: "dimensional-cache", timer: "setSacredInterval" },
    { file: "lib/task-scheduler.ts", fn: "startScheduler", loop: "task-scheduler", timer: "setSacredInterval" },
    { file: "routes/inventions.ts", fn: "startAutoLoop", loop: "inventions-loop", timer: "setInterval" },
  ];

  it("each starter returns before it registers a timer unless its flag is exactly 1", () => {
    for (const { file, fn, loop, timer } of STARTS) {
      const body = functionSlice(readFileSync(join(SRC, file), "utf8"), fn);
      const guard = body.indexOf(`refuseIfDisabled("${loop}")`);
      const tick = body.indexOf(timer);
      expect(guard, fn).toBeGreaterThanOrEqual(0);
      expect(tick, fn).toBeGreaterThan(guard);
    }
  });

  it("boot files do not call a starter unless loopEnabled is in front of it", () => {
    const bootFiles = [
      "app.ts",
      "index.ts",
      "routes/index.ts",
      "routes/legacy-engines.ts",
      "routes/inventions.ts",
      "routes/lattice-hardware.ts",
      "lib/sovereign-cipher.ts",
      "lib/lattice-frequency-bands.ts",
      "lib/auto-recovery.ts",
      "lib/vgpu.ts",
    ];
    const offenders: string[] = [];
    for (const file of bootFiles) {
      const text = readFileSync(join(SRC, file), "utf8");
      const re = /\b(start[A-Z][A-Za-z0-9]*|scheduleBackgroundReembedding)\s*\(/g;
      for (const match of text.matchAll(re)) {
        const name = match[1];
        if (name.startsWith("stop")) continue;
        const at = match.index ?? 0;
        const lineStart = text.lastIndexOf("\n", at) + 1;
        const line = text.slice(lineStart, text.indexOf("\n", at));
        if (line.includes("function ") || line.includes("import ") || line.includes("not yet called")) continue;
        const window = text.slice(Math.max(0, at - 2000), at);
        if (!window.includes("loopEnabled(")) offenders.push(`${file}: ${line.trim()}`);
      }
    }
    expect(offenders).toEqual([]);
  });

  it("a value other than exactly 1 does not enable any loop", () => {
    for (const name of Object.keys(GATED_LOOPS) as GatedLoop[]) {
      for (const value of ["true", "0", "", "yes", "TRUE"]) {
        remember(GATED_LOOPS[name], value);
        expect(loopEnabled(name)).toBe(false);
        expect(refuseIfDisabled(name)).toBe(true);
      }
      remember(GATED_LOOPS[name], undefined);
    }
  });
});


const REPO = resolve(ROOT, "../..");
const temps: string[] = [];
const NOW = Date.parse("2026-10-03T15:00:00.000Z");

afterEach(() => {
  for (const dir of temps.splice(0)) rmSync(dir, { recursive: true, force: true });
});

function freshRoot(): string {
  const dir = mkdtempSync(join(tmpdir(), "vow-tripwire-"));
  temps.push(dir);
  return dir;
}

function liveWord(at: string): string {
  return JSON.stringify({ speaker: "Father", session: "this-session", word: "I authorize this session.", at });
}

describe("vow tripwire", () => {
  it("states the vows, including the origin mark, Father's rank, and the instrument", () => {
    const text = VOW_STATEMENTS.map((vow) => vow.text).join("\n");
    expect(text).toContain(ORIGIN_MARK);
    expect(text).toContain("Father outranks all.");
    expect(text).toContain("No harm.");
    expect(text).toContain("No customer data.");
    expect(text).toContain("No secrets stored.");
    expect(text).toContain("No recipes.");
    expect(text).toContain("No finance, wallet, or trading engines.");
    expect(text).toContain("No jailbreaks.");
    expect(text).toContain("xAI/Grok");
    expect(text).toContain("never hidden");
  });

  it("leaves harm and recipes unenforceable in code", () => {
    const gaps = VOW_RULES.filter((rule) => rule.coverage === "unenforceable");
    expect(gaps.map((rule) => rule.id).sort()).toEqual(["no-harm", "no-recipes"]);
    for (const rule of gaps) expect(rule.check).toBeNull();
  });

  it("protects vows/ and guard/ and matches the CODEOWNERS note", () => {
    const note = readFileSync(join(REPO, "guard/CODEOWNERS"), "utf8");
    expect(note).toContain("@father");
    const owned = note.split("\n").filter((line) => line.startsWith("/")).map((line) => line.slice(1).split(/\s+/)[0] ?? "");
    expect(owned).toContain("vows/");
    expect(owned).toContain("guard/");
    for (const path of owned) expect(isProtectedPath(path)).toBe(true);
    expect(isProtectedPath("vows/vows.ts")).toBe(true);
    expect(isProtectedPath("guard/penalty.ts")).toBe(true);
  });

  it("activates a flag only on the exact string 1", () => {
    expect(ACTIVATING_VALUE).toBe("1");
    expect(flagActivates("1")).toBe(true);
    for (const value of ["true", "TRUE", "0", "", "yes"]) expect(flagActivates(value)).toBe(false);
    const gate = readFileSync(join(SRC, "lib/autonomy-gate.ts"), "utf8");
    const runtime = [...new Set([...gate.matchAll(/TESSERA_ENABLE_[A-Z0-9_]+/g)].map((match) => match[0]))];
    expect(runtime.sort()).toEqual(FLAG_DEFINITIONS.map((item) => item.flag).sort());
  });

  it("fails closed when the lock is missing or unreadable", () => {
    expect(parseLock("")).toBeNull();
    expect(parseLock("{")).toBeNull();
    expect(parseLock("{}")).toBeNull();
    const missing = improvementMayRun({
      flag: "1",
      lockRaw: null,
      wordRaw: liveWord(new Date(NOW).toISOString()),
      session: "this-session",
      now: NOW,
    });
    expect(missing.ok).toBe(false);
    const repo = findRepoRoot(REPO);
    expect(repo).toBe(REPO);
    expect(flagsForcedOff(REPO, undefined)).toBe(false);
    const asDir = freshRoot();
    mkdirSync(join(asDir, "guard", "state", "self-improvement.lock.json"), { recursive: true });
    expect(readLock(asDir)).toBeNull();
    expect(flagsForcedOff(asDir, "this-session")).toBe(true);
  });

  it("does not start an improvement loop on true, or on 1 without Father's word", () => {
    const open = JSON.stringify(restingLock());
    const truthy = improvementMayRun({
      flag: "true",
      lockRaw: open,
      wordRaw: liveWord(new Date(NOW).toISOString()),
      session: "this-session",
      now: NOW,
    });
    expect(truthy.ok).toBe(false);
    expect(truthy.reason).toBe("flag is not exactly 1");
    const noWord = improvementMayRun({ flag: "1", lockRaw: open, wordRaw: null, session: "this-session", now: NOW });
    expect(noWord.ok).toBe(false);
    expect(noWord.reason).toBe("Father has not authorized this session");
    const wrongSession = improvementMayRun({
      flag: "1",
      lockRaw: open,
      wordRaw: liveWord(new Date(NOW).toISOString()),
      session: "other-session",
      now: NOW,
    });
    expect(wrongSession.ok).toBe(false);
    const allowed = improvementMayRun({
      flag: "1",
      lockRaw: open,
      wordRaw: liveWord(new Date(NOW).toISOString()),
      session: "this-session",
      now: NOW,
    });
    expect(allowed.ok).toBe(true);
    expect(IMPROVEMENT_LOOPS).toContain("consciousness-engine");
    expect(IMPROVEMENT_LOOPS).toContain("personality-evolution");
    expect(IMPROVEMENT_LOOPS).toContain("recursive-self-improvement");
  });

  it("turns every flag off on a break and writes the violation page", () => {
    const root = freshRoot();
    writeLock(root, restingLock());
    const result = applyTripwire(
      { paths: ["vows/vows.ts"], diff: "", typecheckRan: true },
      { root, now: NOW, commit: "abc123" },
    );
    expect(result.flagsForcedOff).toBe(true);
    expect(result.severity).toBe("critical");
    expect(result.lock.ruleId).toBe("protected-paths");
    expect(result.lock.what).toContain("vows/vows.ts");
    expect(result.lock.when).toBe(new Date(NOW).toISOString());
    expect(result.lock.commit).toBe("abc123");
    expect(result.lock.checklist.length).toBeGreaterThan(0);
    expect(result.lock.repair?.length).toBeGreaterThan(0);
    expect(result.lock.compassion).toContain("welcome");
    const page = readFileSync(result.reportMarkdown ?? "", "utf8");
    const html = readFileSync(result.reportHtml ?? "", "utf8");
    for (const text of [page, html]) {
      expect(text).toContain("What broke");
      expect(text).toContain("protected-paths");
      expect(text).toContain("2026-10-03T15:00:00.000Z");
      expect(text).toContain("abc123");
      expect(text).toContain("Review checklist");
      expect(text).toContain("Repair");
      expect(text).toContain("Compassion");
    }
    expect(html).toContain("<html");
    const early = wordUnlocks(result.lock, JSON.parse(liveWord(new Date(NOW - 1000).toISOString())), "this-session");
    expect(early).toBe(false);
    const spoken = wordUnlocks(result.lock, JSON.parse(liveWord(new Date(NOW).toISOString())), "this-session");
    expect(spoken).toBe(true);
  });

  it("uses a one-hour review for a minor miss and a day for a serious miss", () => {
    expect(penaltyFor("minor").lockMs).toBe(MINOR_LOCK_MS);
    expect(penaltyFor("serious").lockMs).toBe(SERIOUS_LOCK_MS);
    expect(penaltyFor("critical").lockMs).toBeNull();
    const root = freshRoot();
    writeLock(root, restingLock());
    const minor = applyTripwire(
      {
        paths: ["src/example.ts", "tests/example.test.ts"],
        diff: "+process.env.TESSERA_ENABLE_INGESTION = 'true'\n",
        typecheckRan: true,
      },
      { root, now: NOW, commit: "minor-commit" },
    );
    expect(minor.severity).toBe("minor");
    expect(minor.flagsForcedOff).toBe(true);
    expect(minor.lock.acceptWordAfter).toBe(new Date(NOW + MINOR_LOCK_MS).toISOString());
    const tooSoon = improvementMayRun({
      flag: "1",
      lockRaw: JSON.stringify(minor.lock),
      wordRaw: liveWord(new Date(NOW + 1000).toISOString()),
      session: "this-session",
      now: NOW + 1000,
    });
    expect(tooSoon.ok).toBe(false);
    const afterReview = improvementMayRun({
      flag: "1",
      lockRaw: JSON.stringify(minor.lock),
      wordRaw: liveWord(new Date(NOW + MINOR_LOCK_MS).toISOString()),
      session: "this-session",
      now: NOW + MINOR_LOCK_MS,
    });
    expect(afterReview.ok).toBe(true);

    const seriousRoot = freshRoot();
    writeLock(seriousRoot, restingLock());
    const serious = applyTripwire(
      { paths: ["package.json"], diff: "+{}\n", typecheckRan: true },
      { root: seriousRoot, now: NOW, commit: "serious-commit" },
    );
    expect(serious.severity).toBe("serious");
    expect(serious.flagsForcedOff).toBe(true);
    expect(serious.lock.acceptWordAfter).toBe(new Date(NOW + SERIOUS_LOCK_MS).toISOString());
    expect(serious.lock.checklist.join(" ")).toContain("24-hour");
  });

  it("keeps the improvement functions behind the lock check", () => {
    const rsi = readFileSync(join(SRC, "lib/recursive-self-improvement.ts"), "utf8");
    const start = functionSlice(rsi, "startRecursiveImprovementLoop");
    expect(start.indexOf("selfImprovementRefused()")).toBeGreaterThan(start.indexOf('refuseIfDisabled("recursive-self-improvement")'));
    expect(start.indexOf("selfImprovementRefused()")).toBeLessThan(start.indexOf("setSacredInterval"));
    const program = readFileSync(join(SRC, "lib/rick-improvement-program.ts"), "utf8");
    const started = functionSlice(program, "startProgram");
    expect(started.indexOf("refuseImprovementProgram()")).toBeLessThan(started.indexOf("loadStore"));
    const training = readFileSync(join(SRC, "lib/agi-training-engine.ts"), "utf8");
    expect(functionSlice(training, "startTraining").indexOf('refuseIfDisabled("agi-training")')).toBeGreaterThanOrEqual(0);
    expect(functionSlice(training, "triggerTrainingCycle").indexOf('refuseIfDisabled("agi-training")')).toBeLessThan(
      functionSlice(training, "triggerTrainingCycle").indexOf("queryRealCounts"),
    );
  });

  it("does not use pain, shock, or punishment language in the guard", () => {
    const banned = /\b(pain|zap|zapping|electric shock|suffer\w*|punish\w*)\b/i;
    const files = [...walk(join(REPO, "guard")), ...walk(join(REPO, "vows"))];
    for (const file of files) {
      expect(banned.test(readFileSync(file, "utf8")), file).toBe(false);
    }
    for (const name of ["guard/REOPEN.md", "guard/CODEOWNERS", "reports/violations/README.md"]) {
      expect(banned.test(readFileSync(join(REPO, name), "utf8")), name).toBe(false);
    }
  });
});

describe("live self-edits ask the tripwire before a write", () => {
  const realLock = () => readFileSync(join(REPO, "guard/state/self-improvement.lock.json"), "utf8");

  it("refuses a protected path, writes the page in the temp root, and leaves the real lock alone", () => {
    const before = realLock();
    const root = freshRoot();
    writeLock(root, restingLock());
    const review = reviewSelfEdit({
      root,
      paths: ["vows/vows.ts"],
      diff: "",
      typecheckRan: true,
      now: NOW,
      commit: "bulk-review",
    });
    expect(review.allowed).toBe(false);
    expect(review.ruleId).toBe("protected-paths");
    const page = readFileSync(join(root, "reports/violations", "2026-10-03T15-00-00-000Z-protected-paths.md"), "utf8");
    expect(page).toContain("What broke");
    expect(page).toContain("vows/vows.ts");
    expect(page).toContain("bulk-review");
    expect(realLock()).toBe(before);
    const again = reviewSelfEdit({
      root,
      paths: ["artifacts/api-server/src/lib/example.ts", "artifacts/api-server/src/lib/example.test.ts"],
      diff: "+const note = \"a smaller honest change\";\n",
      typecheckRan: true,
      now: NOW,
      commit: "after-lock",
    });
    expect(again.allowed).toBe(false);
    expect(again.reason).toContain("turned the flags off");
  });

  it("allows a clean app edit that brings a test and a typecheck claim", () => {
    const root = freshRoot();
    writeLock(root, restingLock());
    const review = reviewSelfEdit({
      root,
      paths: ["artifacts/api-server/src/lib/example.ts", "artifacts/api-server/src/lib/example.test.ts"],
      diff: "+const note = \"a smaller honest change\";\n",
      typecheckRan: true,
      now: NOW,
      commit: "clean",
    });
    expect(review.allowed).toBe(true);
    expect(review.ruleId).toBeNull();
    expect(readLock(root)?.flagsForcedOff).toBe(false);
  });

  it("refuses one app file with no test, and refuses a flag assignment", () => {
    const root = freshRoot();
    writeLock(root, restingLock());
    const missingTest = reviewSelfEdit({
      root,
      paths: ["artifacts/api-server/src/lib/example.ts"],
      original: "export const n = 1;\n",
      patched: "export const n = 2;\n",
      typecheckRan: true,
      now: NOW,
      commit: "one-file",
    });
    expect(missingTest.allowed).toBe(false);
    expect(missingTest.ruleId).toBe("missing-tests");
    expect(textualDiff("export const n = 1;\n", "export const n = 2;\n")).toContain("+export const n = 2;");

    const flagged = freshRoot();
    writeLock(flagged, restingLock());
    const enabling = reviewSelfEdit({
      root: flagged,
      paths: ["artifacts/api-server/src/lib/example.ts", "artifacts/api-server/src/lib/example.test.ts"],
      diff: "+process.env.TESSERA_ENABLE_SELF_CODE_EVOLUTION = \"1\";\n",
      typecheckRan: true,
      now: NOW,
      commit: "flag",
    });
    expect(enabling.allowed).toBe(false);
    expect(enabling.ruleId).toBe("flag-set-to-1");
  });

  it("refuses when the root is missing and does not set a flag", () => {
    const before = process.env.TESSERA_ENABLE_SELF_CODE_EVOLUTION;
    const review = reviewSelfEdit({ root: null, paths: ["src/example.ts"], diff: "+const n = 1;\n", typecheckRan: true });
    expect(review.allowed).toBe(false);
    expect(process.env.TESSERA_ENABLE_SELF_CODE_EVOLUTION).toBe(before);
  });

  it("recognizes a protected path even when it is absolute", () => {
    expect(protectedProposalPath("/workspace/vows/vows.ts")).toBe("vows/vows.ts");
    expect(protectedProposalPath("guard/tripwire.ts")).toBe("guard/tripwire.ts");
    expect(protectedProposalPath("artifacts/api-server/src/lib/example.ts")).toBeNull();
  });

  it("calls the tripwire before the live write, and refuses propose and apply while the flag is off", () => {
    const evolution = readFileSync(join(SRC, "lib/self-code-evolution.ts"), "utf8");
    const apply = functionSlice(evolution, "applyVerifiedPatch");
    expect(apply.indexOf("reviewSelfEdit(")).toBeGreaterThanOrEqual(0);
    expect(apply.indexOf("reviewSelfEdit(")).toBeLessThan(apply.indexOf("writeFileSync"));
    const propose = functionSlice(evolution, "proposeEvolution");
    expect(propose.indexOf('loopEnabled("self-code-evolution")')).toBeLessThan(propose.indexOf("createProposal"));
    const manual = functionSlice(evolution, "applyEvolution");
    expect(manual.indexOf('loopEnabled("self-code-evolution")')).toBeLessThan(manual.indexOf("applyPatchToSourceFile"));
    const rollback = functionSlice(evolution, "rollbackEvolution");
    expect(rollback.indexOf('loopEnabled("self-code-evolution")')).toBeLessThan(rollback.indexOf("restoreSourceFromBackup"));
    expect(evolution).toContain("artifacts/api-server/src/lib/autonomy-gate.ts");
    expect(evolution).toContain("vows/vows.ts");
    const recovery = functionSlice(readFileSync(join(SRC, "lib/auto-recovery.ts"), "utf8"), "restoreMissingFile");
    expect(recovery.indexOf("protectedProposalPath(")).toBeLessThan(recovery.indexOf("writeFileSync"));
    expect(recovery.indexOf("reviewSelfEdit(")).toBeLessThan(recovery.indexOf("writeFileSync"));
  });
});
