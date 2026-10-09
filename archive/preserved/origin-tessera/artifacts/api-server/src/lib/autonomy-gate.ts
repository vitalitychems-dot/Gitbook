import { flagsForcedOff, sessionAllowsImprovement } from "../../../../guard/kill-switch";
import { isImprovementLoop } from "../../../../guard/flags";
import { logger } from "./logger";

/**
 * Every boot loop stays off unless its own flag is exactly "1".
 * "true", "yes", and any other value do nothing. There is no wildcard.
 * Self-code writes use TESSERA_ENABLE_SELF_CODE_EVOLUTION.
 */
export const GATED_LOOPS = {
  "self-code-evolution": "TESSERA_ENABLE_SELF_CODE_EVOLUTION",
  "recursive-self-improvement": "TESSERA_ENABLE_RECURSIVE_SELF_IMPROVEMENT",
  "auto-improvement-daemon": "TESSERA_ENABLE_AUTO_IMPROVEMENT",
  "consciousness-engine": "TESSERA_ENABLE_CONSCIOUSNESS",
  "personality-evolution": "TESSERA_ENABLE_PERSONALITY_EVOLUTION",
  "ingestion-scheduler": "TESSERA_ENABLE_INGESTION",
  "shepherd-loop": "TESSERA_ENABLE_SHEPHERD",
  "outreach": "TESSERA_ENABLE_OUTREACH",
  "knowledge-canon-bridge": "TESSERA_ENABLE_KNOWLEDGE_CANON_BRIDGE",
  "canon-regeneration": "TESSERA_ENABLE_CANON_REGENERATION",
  "dual-brain": "TESSERA_ENABLE_DUAL_BRAIN",
  "identity-reinforcement": "TESSERA_ENABLE_IDENTITY_REINFORCEMENT",
  "agi-training": "TESSERA_ENABLE_AGI_TRAINING",
  "council-executor": "TESSERA_ENABLE_COUNCIL_EXECUTOR",
  "red-team": "TESSERA_ENABLE_RED_TEAM",
  "auto-healer": "TESSERA_ENABLE_AUTO_HEALER",
  "autonomous-heartbeat": "TESSERA_ENABLE_AUTONOMOUS_HEARTBEAT",
  "rick-loop": "TESSERA_ENABLE_RICK_LOOP",
  "knowledge-autonomy": "TESSERA_ENABLE_KNOWLEDGE_AUTONOMY",
  "cross-domain-synthesis": "TESSERA_ENABLE_CROSS_DOMAIN_SYNTHESIS",
  "sovereign-memory-vault": "TESSERA_ENABLE_SOVEREIGN_MEMORY_VAULT",
  "autonomous-forum": "TESSERA_ENABLE_AUTONOMOUS_FORUM",
  "sovereign-loop": "TESSERA_ENABLE_SOVEREIGN_LOOP",
  "metacognition": "TESSERA_ENABLE_METACOGNITION",
  "lattice-heartbeat": "TESSERA_ENABLE_LATTICE_HEARTBEAT",
  "lattice-conference": "TESSERA_ENABLE_LATTICE_CONFERENCE",
  "reality-audit": "TESSERA_ENABLE_REALITY_AUDIT",
  "session-prune": "TESSERA_ENABLE_SESSION_PRUNE",
  "anomaly-monitor": "TESSERA_ENABLE_ANOMALY_MONITOR",
  "cipher-rotation": "TESSERA_ENABLE_CIPHER_ROTATION",
  "band-rotation": "TESSERA_ENABLE_BAND_ROTATION",
  "autonomous-build": "TESSERA_ENABLE_AUTONOMOUS_BUILD",
  "autonomous-wiring": "TESSERA_ENABLE_AUTONOMOUS_WIRING",
  "inventions-loop": "TESSERA_ENABLE_INVENTIONS_LOOP",
  "mesh-heartbeat": "TESSERA_ENABLE_MESH_HEARTBEAT",
  "vgpu-tick": "TESSERA_ENABLE_VGPU",
  "hardware-peer-cleanup": "TESSERA_ENABLE_HARDWARE_PEER_CLEANUP",
  "vector-reembed": "TESSERA_ENABLE_VECTOR_REEMBED",
  "consensus-retry": "TESSERA_ENABLE_CONSENSUS_RETRY",
  "route-health": "TESSERA_ENABLE_ROUTE_HEALTH",
  "recovery-watchdog": "TESSERA_ENABLE_RECOVERY_WATCHDOG",
  "memory-consolidation": "TESSERA_ENABLE_MEMORY_CONSOLIDATION",
  "recursive-reflection": "TESSERA_ENABLE_RECURSIVE_REFLECTION",
  "dimensional-cache": "TESSERA_ENABLE_DIMENSIONAL_CACHE",
  "task-scheduler": "TESSERA_ENABLE_TASK_SCHEDULER",
} as const;

export type GatedLoop = keyof typeof GATED_LOOPS;

const announced = new Set<string>();

export function loopEnabled(name: GatedLoop): boolean {
  if (process.env[GATED_LOOPS[name]] !== "1") return false;
  if (flagsForcedOff()) return false;
  if (isImprovementLoop(name) && !sessionAllowsImprovement()) return false;
  return true;
}

/** True when the caller must return without starting a timer or doing the gated action. Logs once. */
export function refuseIfDisabled(name: GatedLoop): boolean {
  if (loopEnabled(name)) return false;
  if (!announced.has(name)) {
    announced.add(name);
    const flag = GATED_LOOPS[name];
    const why = process.env[flag] !== "1"
      ? "flag is not exactly 1"
      : flagsForcedOff()
        ? "a vow break has turned the flags off"
        : "Father has not authorized this session";
    logger.info({ loop: name, flag }, `loop is off (${why}); not started`);
  }
  return true;
}

export function assertSelfModificationAllowed(action: string): void {
  if (!loopEnabled("self-code-evolution")) {
    throw new Error(
      `Self-modification is disabled (${action}). The flag must be exactly 1 and Father must authorize this session.`,
    );
  }
}
