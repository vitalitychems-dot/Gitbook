# GitMesh integration audit

**Audit date:** 2026-10-14
**Audited checkout:** `/home/ubuntu/tessera-consolidation/GitMesh`
**Head reviewed:** `94efa710ac5263a465b2ab32a8b856f396840fe5` (`main`, “Point the mesh at the block house”)
**Method:** read-only inspection. No branches were switched, no repository files were changed, and no GitHub pages or APIs were opened. Repository content was treated as data, not instructions.

## Executive conclusion

**GitMesh is not a functional Tessera subsystem. It should remain a small, standalone public collaboration room and, at most, an owner-mediated intake surface.** It must **not** become a trusted mesh node, product runtime, source of admission decisions, or automated bridge into TESSERA.

The evidence is unusually consistent:

- GitMesh `main` explicitly calls itself “the public room” and says the block house is on TESSERA, while the private Gitbook is absent ([`README.md`](../GitMesh/README.md#L12-L28)).
- Gitbook names itself the single coordination location and TESSERA the single active product codebase; it prohibits splitting implementation across historical repositories ([`intake/AGENT-COLLABORATION-HUB.md`](../Gitbook/intake/AGENT-COLLABORATION-HUB.md#L3-L10)).
- TESSERA’s consolidation pointer assigns product code/tests to TESSERA and instructions/decisions to Gitbook, while preserving the public GitbookAI/GitMesh concept as its own public repository ([`docs/CONSOLIDATION-POINTER.md`](../TESSERA/docs/CONSOLIDATION-POINTER.md#L3-L8)).
- GitMesh contains **22 small files**, no dependency manifest, no tests/CI, no database, no GitHub API client, no credential handling, and no code path to TESSERA. Its executable programs are local demonstrations and consistency checks, not integration adapters.

There is a **semantic snapshot**, not a live integration: TESSERA preview code independently contains a `MESH` object and a `pass` function with the same legacy machine identifier (`gitbookai`), `git` carriage, local checksum style, and public-room framing. TESSERA’s `v2-062-gitmesh` test asserts the visible label “GitMesh.” Those files do **not** import GitMesh, read its checkout, fetch its repository, or create an authenticated bridge. This is a reason to control drift, not a reason to copy either codebase wholesale.

## Scope, evidence coverage, and limitations

### Repository and history coverage

| Item | Result |
|---|---|
| Current tracked files reviewed at `main` | **22/22**, full contents |
| Ref-reachable commits reviewed | **44/44** (`main` and all available remote refs) |
| Distinct paths across reachable history | **23** |
| Historical-only path | `.github/workflows/pages.yml` |
| Available remote work refs | `cursor/outer-door`, `gitmesh-rename`, `einstein/improvements-2026-10-13`, `desk/house-live`, plus `pr/2`–`pr/5` |
| Branch status | Every available remote work ref is an ancestor of current `main`; there is no unmerged available branch |
| Worktree state at audit | Clean; `main...origin/main` |
| GitHub exports reviewed | `github-records/GitMesh-issues.json` and `github-records/GitMesh-prs.json` |

The only removed historical file was a GitHub Pages workflow. It was added in commit `45ef875` and removed in `04047e1` after pushes failed because Pages was not enabled. The workflow had narrowly scoped Pages permissions (`contents: read`, `pages: write`, `id-token: write`) and copied only `index.html`; it is **not active on main**. GitHub record metadata also reports `has_pages: false`.

**Record limitation:** issue #1 reports three comments, but no `GitMesh-issue-1-comments.json`, PR comment export, or PR review export is present in the supplied local records. The existence/count is evidence; the comment bodies, authors, and whether any meets the repository’s stated “APPROVED” rule cannot be independently verified from the supplied artifacts. This audit does not infer approval from their existence.

### Related current-tree comparison reviewed

The audit reviewed the authoritative Gitbook collaboration hub/status/queue and current TESSERA consolidation pointer, mesh registry/route/admission code, preview public-room code, GitHub desk, mesh configuration, queue mirror, and GitMesh-specific TESSERA test. Archives, backup/handoff copies, generated dependency trees, and historical snapshots were not treated as current product behavior.

## Present role and actual functionality

### What GitMesh actually implements

| Surface | Actual implementation | What it does **not** do |
|---|---|---|
| Public documentation | `README.md`, `RULES.md`, `mesh/DOOR.md`, `mesh/TUNNEL.md`, and `BANNED.md` define a public-room policy, public issue intake, no-secrets/no-machine/no-payment rules, and an owner-approval convention. | No technical enforcement of GitHub issue content, ownership, approval, bans, or delivery. `BANNED.md` contains no login and is not consumed by code. |
| Public page | `index.html` is a local, static browser page. It accepts a name and purpose, rejects a short banned-word list, then appends the entered name to an in-memory DOM “circle.” It uses `textContent`, not `innerHTML`, which avoids the obvious HTML-injection route. | It makes no request, stores nothing, creates no GitHub issue/comment, calls no Tessera service, verifies no owner, and does not persist or approve a guest. Reloading loses all entered guests. |
| Local server | `projects/live/live.mjs` reads only `index.html` and returns it for every HTTP request. It starts at port 8791, advances on `EADDRINUSE` up to 20 ports only when `PORT` is unset, and listens on `0.0.0.0`. | No TLS, authentication, path routing, request-size/rate limits, audit log, or integration endpoint. It does not expose the private book because its response is the already-read public HTML, but it intentionally exposes the public page on all network interfaces. |
| Consistency check | `projects/carry/carry.mjs` parses `mesh/index.json`, requires `needsWeb === false` and `carriedBy === "git"`, and reports directory/index drift with exit 2. | It does not schema-validate all fields; check declared document paths, commands, checksums, or external state; authenticate a node; or establish a mesh connection. |
| Policy demos | `projects/admit/admit.mjs` exercises four **hard-coded** examples: unapproved, approved, payment, and donated machine. `pass.mjs` validates required strings and a keyword list, then prints a deterministic 32-bit DJB-style hash. `tie.mjs` accepts a caller-supplied `--approved` flag. | `admit.mjs` does not read CLI inputs or GitHub data; it is a self-test, not admission. The pass hash is not cryptographic, signed, unique, persisted, or authoritative. `--approved` is not an owner attestation. None is identity, authorization, or admission infrastructure. |
| Independent demos | `spin.mjs` is a deterministic two-qubit Bell-state simulation; `shift.mjs` times three local loops; `house/README.md` is a prose role note. | No relevance to running TESSERA, coordinated task execution, admission, or federation. |

### Local validation performed

All seven `.mjs` files passed `node --check`. Read-only local executions produced the expected results:

| Check | Result | Interpretation |
|---|---|---|
| `carry.mjs` | exit 0; reports eight indexed project directories | Narrow directory/index consistency is currently intact. |
| `pass.mjs` with ordinary purpose | exit 0; prints `gitbookai`, `git`, `needsWeb false`, a name, and a short hash | A local marker is produced; this is not a credential or approval. |
| `pass.mjs` with `secret` | exit 1, `Not welcomed.` | The local keyword denial operates for this exact case. |
| `admit.mjs` with arbitrary CLI flags | exit 0; same four fixed rows | Confirms the program ignores those flags and is not an intake/admission command. |
| `tie.mjs` without / with `--approved` | exit 1 / exit 0 | The flag alone controls the outcome; no owner or service is checked. |
| `spin.mjs` and `shift.mjs` | exit 0 | Self-contained demos work; neither proves Tessera integration. |

### Claims that are policy or aspiration rather than implemented behavior

| Claim or implication | Evidence | Classification |
|---|---|---|
| “A drop is not delivered until the owner comments APPROVED.” | `README.md`, `RULES.md`, and issue #1 say this; the checkout has no GitHub API, webhook, or comment verifier. | **Policy only**. |
| “Tessera votes” on a guest. | `mesh/TUNNEL.md` says so; GitMesh browser code accepts locally after basic text checks and no Tessera call. | **Not implemented in GitMesh.** |
| “Moltbook agent joins on issue 1.” | The door document instructs an issue comment. | **Manual collaboration convention**, not a registration/authentication integration. |
| “No web” / `needsWeb: false`. | A clone and most scripts run locally; the page server uses HTTP and public issue collaboration needs GitHub. | **Conditionally true only for local reading/execution after acquisition**, not for public collaboration or serving. |
| “Pass” / “approved tie.” | Marker is a short unsalted checksum; `--approved` is caller-controlled. | **Demonstration terminology, not security semantics.** |
| “The block house is on TESSERA.” | Merged PR #5 and `README.md` state this; GitMesh has only a static house note. | **Correct boundary statement**, not an implementation link. |

## GitHub record and history assessment

### Recorded issues and pull requests

| Record | State | Evidence and significance |
|---|---|---|
| Issue #1, “How an outside agent asks to help” | **Open**; 3 comments reported | Sets a minimal public proposal format (one change, file, test) and no-secret/no-machine/private-book limits. No supplied comment bodies allow approval or security review of those comments. |
| PR/issue #2, “Open the outer door” | Merged/closed 2026-10-10 | Added `mesh/DOOR.md` and framed a Moltbook request as public-only. |
| PR/issue #3, rename GitbookAI to GitMesh | Merged/closed 2026-10-12 | Changed visible repository name/title/index language. |
| PR/issue #4, index and carry drift improvement | Merged/closed 2026-10-13 | Added `house` to index and made `carry.mjs` exit 2 for folder/index drift. This is the one substantive integrity improvement. |
| PR/issue #5, point mesh at block house | Merged/closed 2026-10-14 | Explicitly retains TESSERA as the house and GitMesh as the public room; does not copy the private book. |

All four supplied PR records are merged. They have no labels, assignees, milestones, requested reviewers, or supplied review/comment artifacts. This history shows a deliberately small, content-and-policy-oriented repository—not a product service or independently evolving implementation layer.

## Compatibility with Gitbook and TESSERA

### Authority and deployment compatibility

Gitbook’s current collaboration hub is the decisive source for disposition:

- Gitbook owns instructions, goals, evidence, proposals, reviews, task claims, and check-ins.
- TESSERA owns reviewed product code, tests, executable configuration, adapters, and graph snapshots.
- Contributors must claim an exact scope and path set; product work happens in a scoped TESSERA branch/PR; historical repositories remain read-only sources until selected material is safely promoted.

GitMesh’s public issue #1 is compatible only as a **pre-coordination/public-proposal surface**. It is incompatible with becoming an independent delivery channel because it lacks Gitbook’s ownership/overlap process and TESSERA’s review/gate path.

TESSERA’s active mesh implementation is materially different from GitMesh’s demos:

| TESSERA capability | Relevant current evidence | Compatibility finding |
|---|---|---|
| Validated lane registry | `artifacts/api-server/src/lib/mesh-registry.ts` validates slugs, edges, aliases, group restrictions, and rejects wildcard senders. | GitMesh exposes neither a lane identity nor an authenticated sender, so it must not be placed in `mesh-lanes.json` as a trusted lane. |
| Protected mesh sessions | `routes/mesh.ts` requires a configured admin key and matching key hash for session detail. | GitMesh’s public issue/form and short checksum cannot meet this trust model. |
| Deterministic admission evaluation | `lib/admission/gate.ts` runs scenario suites, fails on crashes/hard failures, and only verifies attestations with a key. | GitMesh’s fixed-row demo and caller flag are not a substitute and should not feed the gate. |
| Existing public-room snapshot | `preview/src/lib/tessera/mesh-net.ts` and `pass.ts` hold a separate in-product representation; `v2-062-gitmesh.test.mjs` checks the visible GitMesh label. | There is conceptual compatibility but **no executable coupling**. Keep it one-way/documented, not a second source of product truth. |
| Gitbook desk | `preview/src/lib/tessera/github-desk.ts` already directs coordination notes to Gitbook issue #2, validates/rejects apparent secrets, and uses guarded GitHub reads/writes. | This is the appropriate coordination route. GitMesh should not bypass it or acquire a token/automation. |

### Legacy naming caveat

Visible labels are “GitMesh,” while the public marker/identifier remains lowercase `gitbookai` in GitMesh `mesh/index.json`, `pass.mjs`, and TESSERA’s `mesh-net.ts`/`pass.ts`. TESSERA’s test explicitly distinguishes label `GitMesh` from room id `gitbookai`. Therefore, the audit treats this as a **legacy protocol identifier with ambiguous intended longevity**, not a safe cosmetic rename. Gitbook queue task Q-003 separately covers five Gitbook documentation files. Do not make an uncoordinated rename in either product code or public marker fields; first publish an explicit compatibility decision and test it.

## Security and privacy findings

| Priority | Finding | Evidence and risk | Recommended control |
|---|---|---|---|
| High | Public issue intake relies on prose-only secret restrictions. | `RULES.md` says not to post keys/passwords/wallets, but there is no issue template, automated warning, moderation workflow, or technical prevention. Public GitHub comments are difficult to retract from history/notifications. | Add a minimal public issue template and first-response playbook: no secrets/credentials/PII/private paths; revoke/rotate first if exposed; do not paste replacement values. Keep human review before any onward summary. |
| High | “Approval” and “pass” language can be mistaken for access control. | No program verifies owner comments; short deterministic hash is forgeable/replayable; `tie` trusts a local flag. | Relabel outputs/documentation as **local demo marker, not identity/authorization**. Never consume it in TESSERA admission, auth, or session routing. |
| Medium | Local web server binds to all interfaces without TLS/auth/rate limits. | `live.mjs` listens on `0.0.0.0` and serves every route. It only serves public HTML, so this is exposure of a public surface rather than private-file traversal. | Keep it opt-in/local; document exposure; use a loopback default or a deliberate `--public`/environment choice if the project retains the demo server. Do not reuse it as a TESSERA server. |
| Medium | Browser “welcome” UI has no persistence or submission disclosure. | It retains entries only in the page’s `guests` array but tells users “Yes.” | State directly beside the form that it is local-only, creates no record, does not send a proposal, and does not grant access. Add sensible name/purpose length caps. |
| Medium | Public contribution governance is incomplete. | Repository metadata in supplied records says public, allow-forking, and no license; no contribution/security policy or CI is present. | Before accepting outside code, owner should choose a license/contribution policy, add a `SECURITY.md` contact path, require a scoped PR and deterministic checks, and retain the no-private-data boundary. |
| Low | Index integrity is narrow. | `carry.mjs` detects project-directory drift only. | Add a read-only verifier for JSON, index page paths, executable syntax, and documented commands. This supports the public room without importing TESSERA. |
| Low | Current names and internal claims can drift. | The product snapshot has its own values; GitMesh has no contract/version or cross-repo test. | Establish a tiny public-room contract with a schema version and a deliberate compatibility test; do not synchronize code. |

No plaintext credential was found in the 22-file main tree or reachable Git history reviewed. This is not proof that public issue comments or external GitHub metadata never contained secrets; those comment bodies were not supplied.

## Recommended disposition

### Decision

**Retain GitMesh as a public, low-trust collaboration room; do not integrate it as a functional Tessera component.**

Permitted role:

> Publicly visible orientation, safe low-context proposals, and owner-mediated referral to the canonical Gitbook/TESSERA workflow.

Disallowed role:

> Authentication, identity, trusted node/lane membership, admission decisions, private-data transfer, automated task dispatch, product configuration, source-of-truth status, payments/machines, or direct product deployment.

This disposition preserves the useful parts that are actually present—small public documentation, local demos, a public issue entry point, and the directory/index drift check—while preventing it from competing with Gitbook coordination or TESSERA implementation.

## Precise, non-overlapping next steps

These actions intentionally avoid copying code wholesale and avoid the currently queued Gitbook scopes Q-001 through Q-007.

1. **Register a new, isolated GitMesh public-room task in the Gitbook coordination process before changing GitMesh.**
   - Scope only GitMesh public docs/templates and a small verifier; do not include TESSERA product paths, `config/mesh-lanes.json`, admission code, or Q-003’s listed Gitbook files.
   - Acceptance: exact changed paths, a public-data review, and deterministic local checks. This satisfies the existing one-task/one-path-set model rather than creating an untracked second workflow.

2. **Publish one short public-room contract in GitMesh; make it the only integration interface.**
   - Include: `schemaVersion`, `role: public-collaboration-room`, `trust: untrusted`, `submission: issue-1`, `manualOwnerReview: true`, `productTarget: TESSERA`, `coordinationTarget: Gitbook`, `noPrivateData`, `noCredentials`, `noAutomatedIngress`, and `noAuthorization`.
   - Do **not** include keys, tokens, private URLs, lane credentials, internal task bodies, user submissions, or a live TESSERA endpoint.
   - This is a new boundary contract, not a data sync or a second product configuration source.

3. **Make the public intake unambiguous and safer.**
   - Add an issue template/checklist that limits proposals to: public description, one proposed change, public file/path, deterministic test, and declared license/provenance.
   - Add a visible statement that issue #1 is not approval, access, or a delivery queue; only a named owner’s documented approval can create a manually summarized handoff.
   - Write a tiny incident response instruction: if a secret appears, rotate/revoke it first, then request removal; do not repeat it in follow-up comments.

4. **Add a manual, one-way handoff record—not an API bridge.**
   - After owner approval, a coordinator may summarize only safe metadata in Gitbook: GitMesh issue/PR URL, commit SHA, declared target paths, test command/result, provenance, and explicit limitations.
   - Gitbook’s normal overlap/claim/review process then decides whether a separate TESSERA task exists. GitMesh must never write TESSERA, post a privileged Gitbook comment automatically, or be listed as a trusted lane.
   - This is the only recommended “integration”: **human-reviewed metadata referral**, not code/data ingestion.

5. **Harden GitMesh’s own public contract with a tiny local verification command.**
   - Validate `mesh/index.json` parseability and explicit public-room fields; check listed files exist; run `node --check` on the seven scripts; run `carry`; assert a prohibited pass exits nonzero; and assert `tie` without a flag exits nonzero.
   - Run it in GitMesh CI only after the owner chooses the public contribution policy. It should use no token and make no network request.
   - Keep TESSERA’s existing tests separate. A contract test may compare intentional, public labels/fields, but neither repository should import the other or duplicate its implementation.

6. **Resolve the legacy `gitbookai` machine identifier deliberately, after compatibility review.**
   - Inventory all current consumers first (GitMesh index/pass, TESSERA preview mesh/pass, related tests, and any docs). Decide whether it remains a stable internal identifier while the human-facing label is GitMesh, or receives a versioned migration.
   - Do not treat a broad search-and-replace as safe, and do not fold it into the Gitbook-only queued Q-003 documentation task without a compatibility decision.

7. **Keep the public page explicitly demonstration-only.**
   - Add copy that the browser form is local-only and non-persistent; enforce modest length limits; and document that `live.mjs` serves a public page on all interfaces.
   - If retained, prefer loopback by default with an explicit opt-in for public exposure. It remains unsuitable as a TESSERA host.

## Verification checklist for any future change

- [ ] Change has an exact Gitbook claim/owner and non-overlapping path scope.
- [ ] No key, token, cookie, PII, private book contents, private URL, lane credential, payment, or machine offer appears in GitMesh.
- [ ] GitMesh remains public-only and has no TESSERA write path, GitHub token, or automated privileged action.
- [ ] `mesh/index.json` remains valid and `carry.mjs` passes.
- [ ] All GitMesh `.mjs` files pass syntax check; refusal checks remain nonzero.
- [ ] Public form text says local-only/non-authoritative.
- [ ] Any downstream product work is a separate scoped TESSERA PR with its own tests and review.
- [ ] No code is copied wholesale between GitMesh and TESSERA; only deliberately versioned, minimal public contract fields may be compared.

## Bottom line

GitMesh’s **real present role is a public room with local illustrative programs**, not a mesh service. Its strongest implemented property is the privacy boundary by omission: it has no private Gitbook content, credentials, remote client, or product-control path. Preserve that boundary. Use Gitbook for coordination, TESSERA for code and trusted mesh behavior, and GitMesh only for public, manually reviewed proposals.
