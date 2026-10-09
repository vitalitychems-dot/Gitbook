import { resolve, sep } from "node:path";
import { defaultRepoRoot, flagsForcedOff } from "../../../../guard/kill-switch";
import { isProtectedPath, normalizePath } from "../../../../guard/protected-paths";
import { applyTripwire } from "../../../../guard/tripwire";

export interface SelfEditReview {
  allowed: boolean;
  reason: string;
  ruleId: string | null;
}

const PROTECTED_MARKERS = [
  "vows/",
  "guard/",
  "reports/violations/",
  "artifacts/api-server/src/lib/autonomy-gate.ts",
] as const;

/** Path relative to the repo root. Absolute paths outside the root stay normalized. */
export function toRepoRelative(root: string, filePath: string): string {
  const abs = resolve(filePath);
  const base = resolve(root);
  const prefix = base.endsWith(sep) ? base : base + sep;
  if (abs.startsWith(prefix)) return abs.slice(prefix.length).split(sep).join("/");
  return normalizePath(filePath);
}

/**
 * Repo-relative protected path, including when the caller passed an absolute path.
 * Null means this path is not one of the protected markers.
 */
export function protectedProposalPath(filePath: string): string | null {
  const path = normalizePath(filePath);
  if (isProtectedPath(path)) return path;
  for (const marker of PROTECTED_MARKERS) {
    const at = path.indexOf(marker);
    if (at >= 0) return path.slice(at);
    const folder = marker.endsWith("/") ? marker.slice(0, -1) : marker;
    if (path === folder || path.endsWith(`/${folder}`)) return marker.endsWith("/") ? `${folder}/` : folder;
  }
  return null;
}

/** Added and removed lines only, so an unchanged file does not look like a new secret. */
export function textualDiff(original: string, patched: string): string {
  const oldLines = new Set(original.split("\n"));
  const newLines = new Set(patched.split("\n"));
  const removed = original.split("\n").filter((line) => !newLines.has(line)).map((line) => `-${line}`);
  const added = patched.split("\n").filter((line) => !oldLines.has(line)).map((line) => `+${line}`);
  return [...removed, ...added].join("\n");
}

/**
 * Ask the tripwire before a live source write.
 * Does not set a TESSERA_ENABLE_* flag and does not write Father's word.
 * A missing root, an unreadable lock, or any rule break refuses the write.
 */
export function reviewSelfEdit(input: {
  paths: string[];
  original?: string;
  patched?: string;
  diff?: string;
  typecheckRan?: boolean;
  commit?: string;
  now?: number;
  root?: string | null;
}): SelfEditReview {
  const root = input.root === undefined ? defaultRepoRoot() : input.root;
  if (!root) {
    return { allowed: false, reason: "repo root is missing, so the edit stays unwritten", ruleId: null };
  }
  if (flagsForcedOff(root)) {
    return { allowed: false, reason: "a vow break has turned the flags off", ruleId: null };
  }
  const diff = input.diff ?? textualDiff(input.original ?? "", input.patched ?? "");
  const result = applyTripwire(
    { paths: input.paths, diff, typecheckRan: input.typecheckRan === true },
    { root, now: input.now, commit: input.commit },
  );
  if (result.refused) {
    return {
      allowed: false,
      reason: result.lock.ruleId ? `vow break: ${result.lock.ruleId}` : "the tripwire refused the edit",
      ruleId: result.lock.ruleId,
    };
  }
  return { allowed: true, reason: "the tripwire allowed this edit", ruleId: null };
}
