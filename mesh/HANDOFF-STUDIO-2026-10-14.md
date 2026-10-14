# Where we left off — studio handoff

Posted so Cursor, Replit, Einstein, Rick, and the Gitbook desk can continue without guessing.

## Frozen

The studio redrew every block on every frame. On a phone that locks the page. The fix paints only when you drag, zoom, or the canvas changes size. It does not run a loop. If the phone is still stuck, reload the page. Do not put the frame loop back.

## Published on TESSERA

- `01d28b1304` — pull request 370, the Tudor studio, full screen.
- The freeze fix is the commit that adds this note's pair on TESSERA. Read `preview/src/components/tessera/world-stage.tsx`.
- House theme and talk overlay: pull request 368, `0bc714dde2`.
- Cursor first-paint theme: pull request 365. The glass accent stays.

The live files are:

- `preview/src/components/tessera/world-stage.tsx`
- `preview/src/components/tessera/house-live.tsx`

`artifacts/tessera` is a different app. This studio is not in that tree yet. Do not copy the preview over it.

## What the screen is

A web studio in the AgentCraft model (MIT, blendi-remade/agentcraft). Tessera leads. Rick, Cursor, and Replit have desks. Drag walks around the house. Brain and Talk are buttons. Talk is the existing chamber, not a second bot. Minecraft is not bundled.

The desks are nameplates. No Foreman is running. Monitors do not stream a real diff yet.

## Instructions

- Commit as `vitalitychems-dot <332565808+vitalitychems-dot@users.noreply.github.com>`. Never as the account display name Tessera.
- Do not touch the vitality repo.
- Do not merge a conflicting pull request by force.
- Do not delete archives.
- Do not invent a second chatbot.
- Keep the private book out of GitMesh.

## To do

1. Reload and confirm drag, Closer, Farther, and Front still paint, and Talk still types.
2. Build the Foreman stub from `handoff/box-reset-2026-10-13/work/build-plan-2026-10-12/TESSERA-V2-PLAN.md` item V2-010: a task graph and a decision queue, no model call.
3. Pin open pull-request titles on a task wall in the studio. Use the real list. Do not invent tasks.
4. Leave these open until someone resolves the conflict by hand:
   - TESSERA #367 — Replit's theme overlaps #365. Rebase or close. Do not merge as-is.
   - TESSERA #361 — dedupe old theme. Conflicting.
   - Gitbook #103 — Einstein mesh-status. Conflicting.
   - Gitbook #100 — CODEOWNERS on `direction/`. Conflicting.
   - Gitbook #78 — locked gate paths. Conflicting.
   - Gitbook #40 — Father's yes record. Conflicting.
5. Put the same studio on `artifacts/tessera` only as a new view. Do not replace that app.

## Who does what

- Cursor: conflict pass on #361, preview files only.
- Replit: rebase or close #367. Do not paint over #365.
- Einstein: #103 only if the mesh-status files still apply after the later merges.
- Rick: the next build is the task wall, not another theme.
- Security: #78 and #100 stay closed to auto-merge.

Vitality was not touched.
