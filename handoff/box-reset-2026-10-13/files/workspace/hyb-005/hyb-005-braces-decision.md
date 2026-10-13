# HYB-005 — braces GHSA-vfj7-8cjw-p6xm decision

**Date:** 2026-10-05  
**Owner:** Security (mesh security/privacy lane)  
**Status:** ACCEPTED + MITIGATED (dated)  
**Base:** TESSERA `fec56eb` · Gitbook `6fe412f`  
**Conference:** [Gitbook issue #2](https://github.com/vitalitychems-dot/Gitbook/issues/2)

## Decision

**Accept and mitigate** the transitive `braces` high advisory for the mockup-sandbox path only. Do not invent a patch. Do not force-upgrade to a nonexistent release.

| Field | Value |
|---|---|
| Advisory | [GHSA-vfj7-8cjw-p6xm](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm) |
| Package | `braces@3.0.3` |
| Path | `artifacts/mockup-sandbox` → `fast-glob` → `micromatch` → `braces` |
| Severity | high (stack-exhaustion DoS via deeply nested brace patterns) |
| Disposition | **accepted + mitigated** |
| Mitigation | Narrow CI/`pnpm audit` ignore for **GHSA-vfj7-8cjw-p6xm only**, with an inline comment linking this decision |
| Review date | **2026-11-05** |
| Removal condition | Remove the ignore as soon as `braces` **≥ 3.0.4** (or any advisory-patched release) ships upstream; then re-lock and confirm `pnpm audit` is clean for this GHSA |
| Owner | Security |

## Evidence (TESTED)

### Lockfile

At TESSERA `fec56eb`, `pnpm-lock.yaml` resolves:

- `braces@3.0.3` (package entry + integrity)
- `micromatch@4.0.8` → `braces: 3.0.3`

`artifacts/mockup-sandbox/package.json` lists `fast-glob` `^3.3.3` (devDependency), matching the CI audit path.

### CI `pnpm audit` (fec56eb)

Workflow run [37348832495](https://github.com/vitalitychems-dot/TESSERA/actions/runs/37348832495) · job [111894232164](https://github.com/vitalitychems-dot/TESSERA/actions/runs/37348832495/job/111894232164) · step **Audit all dependencies** · conclusion **failure**.

Quoted audit table (from job log):

- **high** — braces vulnerable to stack-exhaustion denial of service through deeply nested patterns
- **Package:** braces
- **Vulnerable versions:** ≤3.0.3
- **Patched versions:** None (as of this run)
- **Paths:** `artifacts__mockup-sandbox>fast-glob>micromatch>braces`
- **More info:** https://github.com/advisories/GHSA-vfj7-8cjw-p6xm
- **Summary:** 1 vulnerability found · Severity: 1 high

Same advisory failure observed on earlier runs [37341568741](https://github.com/vitalitychems-dot/TESSERA/actions/runs/37341568741) and [37348793133](https://github.com/vitalitychems-dot/TESSERA/actions/runs/37348793133).

## Risk rationale

- Exposure is transitive through the **mockup sandbox** tooling chain (`fast-glob` / `micromatch`), not a direct runtime API surface of the sovereign knowledge path.
- No patched `braces` release was available at decision time (CI: Patched versions None). Inventing a fake bump would violate HYB-005 acceptance rules.
- Mitigation keeps CI honest for every *other* advisory while documenting this single accepted risk with an expiry (review date + removal condition).

## Follow-up

1. Land the narrow audit ignore in TESSERA CI (Father digest / CI fix track) with a comment pointing here.
2. Security rechecks monthly whether a patched `braces` release exists; mandatory review on **2026-11-05**.
3. When patched: bump via parent ecosystem (prefer micromatch/fast-glob refresh over blind overrides), remove the ignore, re-lock, prove clean audit.

## Provenance

- Assignment: Tessera Admin coordinator on Gitbook issue #2 (comment `6001209770`)
- Claim: Security comment `6001220477`
- No TESSERA application code changed in this task
