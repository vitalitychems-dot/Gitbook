# GATE TESSERA #299 rebased — PASS @9de9f876 (base main e26afd63)
Head unchanged (9de9f8767a55); merge-base = e26afd63. Diff: 3 files (api-server db-optional-boot test, v2 pre-fix fixture, v2-078 test); 0 gitai/agent-login, no DATABASE_URL/key env changes.
TESTED (Node 22.20, pnpm 11.25, frozen+ignore-scripts, DATABASE_URL unset), main vs head identical:
- scripts 23/0; gitai 28/0; v2 137 pass/3 fail (3D browser tests, local env, same on both); api 483 pass/10 skip, 1 file (invention-glb-upload) fails to load locally on both.
- agent-login.test.mjs 10x: main 8 pass/2 FAIL; head 10/10.
ROOT CAUSE (TESTED): flaky test, pre-existing. Test tampers via `ada.apiKey.slice(0,-1)+"0"`; when key's last hex char is already "0" (1/16) the "tampered" key IS the real key, so authenticateAgentKey returns the account (CI actual: last4 '5bc0'). Repro: 400 trials → 26 ends-in-0, 26 hits, exactly matching.
SECURITY: no bypass. 400 trials of real tamper / cross-agent key / wrong handle: 0 accepted. loginAgent returns {ok:false} on mismatch. Note the failure message prints the account's apiKey record (hash/salt/last4, not plaintext) into CI logs — test-only data. Fix: tamper by flipping last char (e.g. '0'↔'1').
REPORTED: CI run 38396986036 on head: only failure is that agent-login test. Main e26afd63 CI 38396938636 red on db-optional-boot (fixed by #299). Last 5 main runs red. mergeable MERGEABLE/UNSTABLE. Emails noreply. gitleaks range: 0 leaks.
