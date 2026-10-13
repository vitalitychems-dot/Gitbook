---
name: Doc package gate review
description: >-
  Use when reviewing a docs diff package or PR as a review gate (approve /
  changes needed / reject) before it moves to the next gate.
---
# Fast gate review

1. **Overlap, one call:** list the repo's latest main commit and its open PRs. Reuse the result for every package in the same 15-minute window instead of re-fetching it.
2. **Run the checker:** `/workspace/moderator-tools/gate-check.sh <diff> <sha256> [base-dir]`. It reports the hash, the files touched, add and delete counts, red flags (secrets, enable-flag flips, workflow edits, protected paths, personal handles), claims about the owner or gates that need a REPORTED tag, and apply checks.
3. **Revisions:** read only the interdiff. Earlier checks carry forward when the interdiff touches nothing they covered.
4. **Cites:** spot-check up to three cited commits or PRs. Use one parallel batch of get_commit calls and write large outputs to a file, then grep the message and date. Convert UTC to the user's zone.
5. **Decide with these rules:**
   - **FAIL:** a hash mismatch, a red flag, a cite that is wrong or invented, rewritten provenance (dated SHAs), a duplicate of merged work, or content that falls outside its table.
   - **Non-blocking:** owner statements that are only REPORTED, mixed ID schemes, stale wording.
6. **Send one message** to the submitter with the verdict, the hash, the base, a short list of evidence, the non-blocking notes and the next gate. Approve does not push or merge.
7. **Record a one-line memory** with the item, revision, hash, base and verdict. Mark earlier revisions superseded.
8. **Board posts:** post on the board only when assigned to. Don't send status-only messages.
