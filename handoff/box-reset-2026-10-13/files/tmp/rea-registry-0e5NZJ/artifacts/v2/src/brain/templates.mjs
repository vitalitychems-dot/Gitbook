import { readFileSync } from "node:fs";
export const TEMPLATES = {
  gpt2: { file: "gpt2.json", species: "artificial model", kind: "weights", license: "MIT claimed only in source" },
};
export function loadTemplate() { return readFileSync("gpt2.json", "utf8"); }
