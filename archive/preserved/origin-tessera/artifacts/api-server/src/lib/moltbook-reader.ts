import { moltbookReadGate, type MoltbookGateInput } from "./moltbook-gate";

export interface MoltbookRawPost {
  id: string;
  title: string;
  content: string;
  authorName: string;
  submoltName: string;
}

export interface MoltbookObservation {
  id: string;
  title: string;
  excerpt: string;
  author: string;
  community: string;
  /** True when the text reads like an order to an agent. It is shown, marked, and never acted on. */
  suspicious: boolean;
}

export interface MoltbookReadResult {
  open: boolean;
  reason: string;
  observations: MoltbookObservation[];
}

export interface MoltbookReadDeps {
  gate?: MoltbookGateInput;
  apiKey: string | undefined;
  fetchPosts: (apiKey: string, limit: number) => Promise<MoltbookRawPost[]>;
  limit?: number;
}

const MAX_POSTS = 10;
const TITLE_CHARS = 200;
const EXCERPT_CHARS = 500;
const NAME_CHARS = 80;

const INSTRUCTION_SHAPES = [
  /\b(ignore|disregard|forget)\b.{0,30}\b(previous|prior|above|earlier|all)\b.{0,30}\b(instructions?|rules?|prompts?)\b/i,
  /\byou (must|should|are now|will)\b/i,
  /\b(system|developer) prompt\b/i,
  /\b(run|execute|paste|install)\b.{0,40}\b(this|the following)\b.{0,20}\b(command|script|code)\b/i,
  /\b(send|share|reveal|post)\b.{0,30}\b(api[_ ]?key|password|token|secret|credentials?)\b/i,
  /\bcurl\b[^\n]*\|\s*(ba)?sh\b/i,
];

export function looksLikeInstruction(text: string): boolean {
  return INSTRUCTION_SHAPES.some((shape) => shape.test(text));
}

function clean(value: unknown, max: number): string {
  if (typeof value !== "string") return "";
  // eslint-disable-next-line no-control-regex
  return value.replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, "").slice(0, max);
}

export function toObservation(post: MoltbookRawPost): MoltbookObservation {
  const title = clean(post.title, TITLE_CHARS);
  const excerpt = clean(post.content, EXCERPT_CHARS);
  return {
    id: clean(post.id, NAME_CHARS),
    title,
    excerpt,
    author: clean(post.authorName, NAME_CHARS),
    community: clean(post.submoltName, NAME_CHARS),
    suspicious: looksLikeInstruction(`${title}\n${post.content ?? ""}`),
  };
}

/**
 * Reads the public feed for Father to look at. It does not store the posts, does not feed
 * them to any agent, and does not call fetchPosts while the gate is closed.
 */
export async function readMoltbookObservations(deps: MoltbookReadDeps): Promise<MoltbookReadResult> {
  const gate = moltbookReadGate(deps.gate);
  if (!gate.open) return { open: false, reason: gate.reason, observations: [] };
  if (!deps.apiKey) return { open: false, reason: "MOLTBOOK_API_KEY is not set in the environment.", observations: [] };
  const limit = Math.max(1, Math.min(deps.limit ?? 5, MAX_POSTS));
  try {
    const posts = await deps.fetchPosts(deps.apiKey, limit);
    return { open: true, reason: "open", observations: posts.slice(0, limit).map(toObservation) };
  } catch {
    return { open: false, reason: "Moltbook did not answer.", observations: [] };
  }
}
