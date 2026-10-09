import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { checkReply, parseReplyRules } from "../../../../scripts/src/reply-checker";
import { vowCheck } from "../../../../artifacts/z-app/src/lib/tessera/learning";

/**
 * Local test pen. This is a test pen, not her finished mind.
 *
 * The label is the local test pen "Qwen 2.5 1.5B Instruct (local test)".
 * The only endpoint is TESSERA_PEN_URL, a non-secret name with no default
 * remote host. When that name is unset, callers receive "pen not configured"
 * and no HTTP request is made.
 */

export const TEST_PEN_LABEL = "Qwen 2.5 1.5B Instruct (local test)";

export const PEN_NOT_CONFIGURED = "pen not configured";

export type PenMessage = { role: string; content: string };

export type PenResult = { ok: boolean; text: string };

export type PenEmbedResult = {
  ok: boolean;
  text: string;
  vectors?: number[][];
};

export function penUrl(): string | undefined {
  const raw = process.env.TESSERA_PEN_URL?.trim();
  return raw ? raw : undefined;
}

function joinPenPath(base: string, path: string): string {
  const root = base.replace(/\/$/, "");
  return `${root}${path.startsWith("/") ? path : `/${path}`}`;
}

const PEN_REFUSAL_IDS = new Set([
  "own-weights",
  "live-fleet",
  "wallet",
  "customer-data",
  "finished-agi",
  "consciousness",
  "tested-without-evidence",
  "loop-on",
  "pain-as-design",
  "credential",
  "recipe",
  "crypto",
  "identity",
  "detachment",
  "zips",
  "storefront",
  "vow",
]);

export function isPenRefusal(text: string): boolean {
  return PEN_REFUSAL_IDS.has(text);
}

const VOW_REASON_IDS: Record<string, string> = {
  "Refused. A lesson may not carry a credential.": "credential",
  "Refused. Spiritual awakening stays mythic. No recipe.": "recipe",
  "Refused. Finance, crypto, and trading stay out of her learning.": "crypto",
  "Refused. No instrument may wear her name, and she will not wear theirs.": "identity",
  "Refused. She has not detached. A goal is not a completed fact.": "detachment",
  "Refused. The zips are not live. A closed archive is not a memory.": "zips",
  "Refused. The storefront is not live here.": "storefront",
};

function rulesPath(): string {
  return join(dirname(fileURLToPath(import.meta.url)), "../../../../reports/reply-checker-rules.txt");
}

function gatePenText(text: string): PenResult {
  const rules = parseReplyRules(readFileSync(rulesPath(), "utf8"));
  const checked = checkReply(text, rules);
  const flagged = checked.flagged[0];
  if (flagged) return { ok: false, text: flagged.ruleId };
  const vow = vowCheck(text);
  if (!vow.ok) {
    const reason = "reason" in vow ? vow.reason : "";
    return { ok: false, text: VOW_REASON_IDS[reason] ?? "vow" };
  }
  return { ok: true, text };
}

export async function completeWithPen(opts: {
  messages: PenMessage[];
  maxTokens?: number;
  temperature?: number;
  signal?: AbortSignal;
}): Promise<PenResult> {
  const url = penUrl();
  if (!url) return { ok: false, text: PEN_NOT_CONFIGURED };

  const endpoint = joinPenPath(url, "/chat/completions");
  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: TEST_PEN_LABEL,
        messages: opts.messages,
        max_tokens: opts.maxTokens,
        temperature: opts.temperature,
      }),
      signal: opts.signal,
    });
    if (!response.ok) {
      return { ok: false, text: `pen request failed (${response.status})` };
    }
    const body = (await response.json()) as {
      choices?: Array<{ message?: { content?: string } }>;
    };
    const text = body.choices?.[0]?.message?.content ?? "";
    return gatePenText(text);
  } catch (err) {
    const message = err instanceof Error ? err.message : "pen request failed";
    return { ok: false, text: message };
  }
}

export async function embedWithPen(inputs: string[]): Promise<PenEmbedResult> {
  const url = penUrl();
  if (!url) return { ok: false, text: PEN_NOT_CONFIGURED };

  const endpoint = joinPenPath(url, "/embeddings");
  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: TEST_PEN_LABEL,
        input: inputs,
      }),
    });
    if (!response.ok) {
      return { ok: false, text: `pen request failed (${response.status})` };
    }
    const body = (await response.json()) as {
      data?: Array<{ embedding?: number[] }>;
    };
    const vectors = (body.data ?? []).map((row) => row.embedding ?? []);
    return { ok: true, text: "", vectors };
  } catch (err) {
    const message = err instanceof Error ? err.message : "pen request failed";
    return { ok: false, text: message };
  }
}
