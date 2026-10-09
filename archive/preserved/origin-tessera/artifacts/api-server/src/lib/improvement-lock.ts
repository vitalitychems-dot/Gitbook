import { loopEnabled } from "./autonomy-gate";
import { logger } from "./logger";

let announced = false;

/**
 * True when recursive self-improvement must return before any work.
 * The flag must be exactly "1", the lock must be readable, and Father must have
 * authorized this session. A missing lock is closed. This does not set any flag.
 */
export function selfImprovementRefused(): boolean {
  const refused = !loopEnabled("recursive-self-improvement");
  if (refused && !announced) {
    announced = true;
    logger.info(
      "recursive self-improvement stays off until the flag is exactly 1 and Father authorizes this session",
    );
  }
  return refused;
}
