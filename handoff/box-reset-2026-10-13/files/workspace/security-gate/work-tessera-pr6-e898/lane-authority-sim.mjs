// Mirrors assertFileWrite + findLane from e898111ae9fe730ad214ec63f9173d338a9df53e
const lanes = [
  { id: "tessera", name: "Tessera", fileWrites: true },
  { id: "security", name: "Security", fileWrites: false },
  { id: "build", name: "Build", fileWrites: false },
];

function findLane(lanes, laneId) {
  const wanted = laneId?.trim().toLowerCase();
  if (!wanted) return undefined;
  return lanes.find((lane) => lane.id.toLowerCase() === wanted);
}

function assertFileWrite(options, explicitLane) {
  const rawEnvLane = options.agentLane?.trim() ?? "";
  if (!rawEnvLane) {
    throw new Error("GITBOOK_AGENT_LANE is not set. This process is read-only and cannot open draft pull requests.");
  }
  const envLane = findLane(lanes, rawEnvLane);
  if (!envLane) {
    throw new Error(`GITBOOK_AGENT_LANE "${rawEnvLane}" is not a lane in agents.json. File changes are denied.`);
  }
  const requested = explicitLane?.trim();
  if (requested) {
    const requestedLane = findLane(lanes, requested);
    if (!requestedLane || requestedLane.id !== envLane.id) {
      throw new Error(
        `lane "${requested}" cannot override GITBOOK_AGENT_LANE ${envLane.id}. A per-call lane cannot escalate this process.`,
      );
    }
  }
  if (envLane.fileWrites === false) {
    throw new Error(`${envLane.name} is read-only and cannot open draft pull requests`);
  }
}

function tryCase(label, envLane, argLane) {
  try {
    assertFileWrite({ agentLane: envLane }, argLane);
    console.log(`${label}: ALLOWED`);
  } catch (e) {
    console.log(`${label}: BLOCKED (${e.message.split(".")[0]})`);
  }
}

console.log("=== Prior FAIL bypass re-sim (must BLOCK) ===");
tryCase("env=security, arg=tessera", "security", "tessera");
tryCase("env=security, arg=Security", "security", "Security");
tryCase("env=build, arg=nonexistent", "build", "nonexistent");
console.log("=== Additional cases ===");
tryCase("env=security, arg=none", "security", undefined);
tryCase("env=build, arg=none", "build", undefined);
tryCase("env=Security (case), arg=none", "Security", undefined);
tryCase("env=empty, arg=tessera", "", "tessera");
tryCase("env=empty, arg=none", "", undefined);
tryCase("env=unknown, arg=none", "not-a-lane", undefined);
tryCase("env=tessera, arg=none", "tessera", undefined);
tryCase("env=tessera, arg=tessera", "tessera", "tessera");
tryCase("env=tessera, arg=TESSERA (case match)", "tessera", "TESSERA");

console.log("\n=== Loopback host check ===");
const LOOPBACK = new Set(["127.0.0.1", "::1", "localhost"]);
function assertLoopback(host) {
  const normalized = host.trim().toLowerCase();
  if (!LOOPBACK.has(normalized)) {
    throw new Error(`GITBOOK_HTTP_HOST must be loopback. Refusing to start with "${host}".`);
  }
}
for (const h of ["0.0.0.0", "1.2.3.4", "*", "", "127.0.0.1", "localhost", "::1", "LOCALHOST", " 127.0.0.1 "]) {
  try {
    assertLoopback(h || " ");
    console.log(`host="${h}": OK`);
  } catch (e) {
    console.log(`host="${h}": REFUSE`);
  }
}
