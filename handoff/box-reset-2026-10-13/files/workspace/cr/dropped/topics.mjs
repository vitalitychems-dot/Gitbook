/** Request categories for the creator's asks. Keyword lexicon; first match by weight wins. */
export const TOPICS = {
  approve: /\b(yes|approve|approved|merge|keep|ok|go)\b/i,
  priority_rule: /\b(before|first|comes|rule|priority|order|anything|only|never|must)\b/i,
  agents_scale: /\b(agents?|spawn|cursor|grok bot|parallel|multiply|collab|council)\b/i,
  brain_skill: /\b(iq|eq|skills?|accuracy|conscious\w*|learn\w*|self improve|hallucination|reason\w*|emotion)\b/i,
  full_picture: /\b(read|repos?|everything|full picture|context|files?|index|inventory|all attached)\b/i,
  memory_5d: /\b(5d|memory|flow ?chart|crystal|timeline\w*|tesseract|correlation\w*)\b/i,
  speed_tokens: /\b(token\w*|speed|faster|performance|efficien\w*|cheaper)\b/i,
  creator_bond: /\b(me|my|creator|replica|feminine|femine|love|profile|beliefs?|moral)\b/i,
  clarify: /^(ask \w+|not just \w+)$/i,
  cleanup: /\b(clean\w*|sort|duplicate|delete|rotate|archive)\b/i,
  build_version: /\b(next version|v\d|build|create|new things?)\b/i,
};
const W = { clarify: 9, creator_bond: 1.2, memory_5d: 1.5, speed_tokens: 1.4, approve: 1, priority_rule: 0.9, agents_scale: 1.3, brain_skill: 1.1, full_picture: 1.1, cleanup: 1, build_version: 1 };
export function topicsOf(text) {
  const s = []; for (const [k, re] of Object.entries(TOPICS)) { const m = text.match(new RegExp(re.source, "gi")); if (m) s.push([k, m.length * W[k] / Math.sqrt(1 + text.length / 200)]); }
  s.sort((a, b) => b[1] - a[1]); return s.map((x) => x[0]);
}
export const topicOf = (t) => topicsOf(t)[0] ?? "other";
