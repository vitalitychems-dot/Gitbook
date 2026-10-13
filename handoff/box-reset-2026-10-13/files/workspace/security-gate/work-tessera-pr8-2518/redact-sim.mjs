const SECRET_PATTERNS = [
  /\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{10,}\b/g,
  /\bgithub_pat_[A-Za-z0-9_]{10,}\b/g,
  /\bsk-[A-Za-z0-9]{10,}\b/g,
  /\bxox[bp]-[A-Za-z0-9-]{8,}/gi,
  /\b(?:postgres|postgresql|mysql|mongodb(?:\+srv)?|redis|amqp):\/\/[^:\s/]+:[^@\s/]+@\S+/gi,
  /\b(?:AKIA|ASIA)[0-9A-Z]{16}\b/g,
  /\b(?:aws_secret_access_key|aws_access_key_id)\s*[:=]\s*\S+/gi,
  /\bBearer\s+[A-Za-z0-9\-._~+/]+=*/gi,
  /-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----/g,
  /\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b/g,
  /\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|secret|password|passwd|authorization)\s*[:=]\s*\S+/gi,
];
function redactSecrets(value) {
  let next = value;
  for (const pattern of SECRET_PATTERNS) next = next.replace(pattern, "[REDACTED]");
  return next;
}
const slackBot = ["xoxb", "FAKE", "not-a-real-token"].join("-");
const slackUser = ["xoxp", "FAKE", "not-a-real-token"].join("-");
const databaseUrl = ["postgres://", "demo-user", ":", "example-secret", "@127.0.0.1/tessera"].join("");
const awsKey = ["AKIA", "EXAMPLEONLYKEY12"].join("");
const awsSecret = ["aws_secret_access_key", "example-only-not-real"].join("=");
const input = `bot ${slackBot} user ${slackUser}`;
const output = `db ${databaseUrl} key ${awsKey}`;
const tags = ["password=[REDACTED]", "secret=[REDACTED]", awsSecret];
const visible = [redactSecrets(input), redactSecrets(output), ...tags.map(redactSecrets)].join("\n");
const secrets = [slackBot, slackUser, databaseUrl, awsKey, "example-secret", "example-only", "example-only-not-real"];
console.log("=== PR8 redaction coverage ===");
console.log("redacted visible:\n" + visible);
for (const s of secrets) {
  console.log(`contains "${s}"? ${visible.includes(s) ? "LEAK" : "OK redacted"}`);
}
console.log("has [REDACTED]?", visible.includes("[REDACTED]"));
