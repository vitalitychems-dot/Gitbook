import { flagActivates } from "../../../../guard/flags";
import { defaultRepoRoot, flagsForcedOff, sessionAllowsImprovement } from "../../../../guard/kill-switch";

export const MOLTBOOK_READ_FLAG = "TESSERA_ENABLE_MOLTBOOK_READ";
export const MOLTBOOK_SPEAK_FLAG = "TESSERA_ENABLE_MOLTBOOK_SPEAK";

export interface MoltbookGateDecision {
  open: boolean;
  reason: string;
}

export interface MoltbookGateInput {
  flag?: string | undefined;
  root?: string | null;
  session?: string | undefined;
}

/**
 * Reading Moltbook is open only when the flag is exactly "1", no vow break has the flags
 * forced off, and Father has authorized this session. A missing lock is closed.
 */
export function moltbookReadGate(input: MoltbookGateInput = {}): MoltbookGateDecision {
  const flag = "flag" in input ? input.flag : process.env[MOLTBOOK_READ_FLAG];
  const root = "root" in input ? (input.root ?? null) : defaultRepoRoot();
  const session = "session" in input ? input.session : process.env.TESSERA_FATHER_SESSION;
  if (!flagActivates(flag)) return { open: false, reason: `${MOLTBOOK_READ_FLAG} is not exactly 1.` };
  if (flagsForcedOff(root, session)) return { open: false, reason: "A vow break has turned the flags off, or the lock cannot be read." };
  if (!sessionAllowsImprovement(root, session)) return { open: false, reason: "Father has not authorized this session." };
  return { open: true, reason: "open" };
}

/**
 * Outbound speaking is not built. This answers every request with a refusal so the older
 * forum cross-post stays held even if the forum loop is opened. The speak flag is named
 * here only so a test can show nothing reads it.
 */
export function moltbookSpeakGate(): MoltbookGateDecision {
  return { open: false, reason: `Speaking on Moltbook is not built. ${MOLTBOOK_SPEAK_FLAG} is not read by anything.` };
}
