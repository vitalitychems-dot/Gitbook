# GitHub path/ref coverage manifest

Captured on 2026-10-07 (America/Chicago) from the connected GitHub account vitalitychems-dot.

## Scope

- The connected account inventory contained 15 repositories, 65 remote branch refs, 0 tags, 0 releases, and 6 open pull requests at capture.
- This manifest covers the 15 repositories visible to the connected account. It is not the separate approximately 500-repository Replit/MCP pipeline, which has not been located.
- It records current branch-head path/object metadata only. Destination comparisons are against TESSERA/main at commit be9827ea21b1e0b8a2365ce16161104da254f3d2 (tree 548c86217c62c74f880d5883901c4385a63924b0) and Gitbook/main at commit 09ddefe69c3ace84a27411ac87910ca1ca534a50 (tree 4b276805952b1d08e96731b4022d26f8533b049f).
- All 63 distinct repository/tree snapshots were fetched completely, producing 98,248 path/object rows across distinct trees and 99,698 path/ref rows. Six oversized trees were enumerated by subtree because the connector caps a single response at 1 MB; all are complete and non-truncated.

## Files

- path_ref_coverage.csv: one row per file/blob or gitlink path per branch ref, with exact SHA presence against each destination main and same-path SHA matches.
- deduplicated_path_groups.csv: identical repository/path/object records grouped across refs, with ref and commit membership lists.
- branch_refs.csv: every observed branch, commit SHA, tree SHA, protection flag, and matching open PR numbers.
- per_ref_summary.csv: per-branch path counts, unique blob counts/bytes, and destination-main matches.
- repo_inventory.csv: connected account repository inventory and branch/tree counts. Empty repositories with no branch refs remain listed.
- open_pull_requests.csv, tag_refs.csv, release_metadata.csv: current open PR heads and tag/release inventory (tag and release tables are empty at capture).
- tree_fetch_status.csv: distinct tree snapshots, branch membership, fetch method, path counts, and completeness.
- snapshot_summary.json: machine-readable scope and totals.

## Matching semantics

- A same-blob-SHA match means an identical Git blob object exists somewhere in that destination main; it does not imply that the source and destination paths have the same purpose.
- A same-path-and-SHA match means both path and object SHA match exactly. Gitlinks/submodules are listed but are not treated as file-blob content matches.
- Sizes are GitHub tree object sizes for blobs. Empty size cells mean GitHub did not report a blob size for that object type. JSON arrays in CSV cells are encoded as JSON for unambiguous parsing.

## Limits and safeguards

- No file contents were read, copied, committed, or transferred. No repository, branch, issue, or pull request was changed by generating this artifact.
- Branch trees represent only the current remote head of each branch. This does not establish full-history, local/unpushed-ref, deleted-ref, fork, wiki, Git LFS, repository-settings, or submodule-content coverage.
- The manifest is metadata, not approval to copy or delete. Review actual file contents, secrets, personal/runtime data, licensing, review state, and destination behavior before transferring anything.
