#!/usr/bin/env python3
"""Check mesh/HANDOFF.md and intake/log.md table shape and relative links.

HANDOFF items must be a 6-column table and every relative link in that file
must resolve. Intake log rows must be 12 columns with unique IDs.
Exit 0 on success, 1 on any failure. Prints counts for before/after diffs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

HANDOFF_COLS = 6
LOG_COLS = 12
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in (here, *here.parents):
        if (candidate / "mesh" / "HANDOFF.md").is_file():
            return candidate
    sys.exit("check_handoff: mesh/HANDOFF.md not found")


def split_row(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", text)]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_rows(text: str, header_prefix: str) -> tuple[list[str], list[tuple[int, list[str]]]]:
    """Return header cells and data rows for the table whose header starts with prefix."""
    header: list[str] | None = None
    rows: list[tuple[int, list[str]]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            if header is not None and line.strip():
                break
            continue
        cells = split_row(line)
        if header is None:
            if line.startswith(header_prefix):
                header = cells
            continue
        if is_separator(cells):
            continue
        rows.append((lineno, cells))
    if header is None:
        sys.exit(f"check_handoff: missing table header {header_prefix!r}")
    return header, rows


def link_target(md_file: Path, raw: str) -> Path | None:
    """Return a local path for a relative link, or None for external/anchor links."""
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith(("http://", "https://")):
        # markdown allows (url "title")
        target = target.split(" ", 1)[0]
    if target.startswith(("#", "mailto:")) or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return None
    return (md_file.parent / path).resolve()


def main() -> int:
    root = repo_root()
    handoff_path = root / "mesh" / "HANDOFF.md"
    log_path = root / "intake" / "log.md"
    handoff_text = handoff_path.read_text(encoding="utf-8")
    log_text = log_path.read_text(encoding="utf-8")

    header, rows = table_rows(handoff_text, "| Id |")
    bad_rows = [(lineno, len(cells)) for lineno, cells in rows if len(cells) != HANDOFF_COLS]
    header_ok = len(header) == HANDOFF_COLS

    relative = 0
    unresolved: list[str] = []
    for lineno, line in enumerate(handoff_text.splitlines(), 1):
        for match in LINK_RE.finditer(line):
            dest = link_target(handoff_path, match.group(1))
            if dest is None:
                continue
            relative += 1
            if not dest.exists():
                unresolved.append(f"{lineno}:{match.group(1)}")

    log_header, log_rows = table_rows(log_text, "| ID |")
    log_bad = [(lineno, len(cells)) for lineno, cells in log_rows if len(cells) != LOG_COLS]
    ids = [cells[0] for _, cells in log_rows if cells]
    seen: set[str] = set()
    duplicates: list[str] = []
    for item_id in ids:
        if item_id in seen and item_id not in duplicates:
            duplicates.append(item_id)
        seen.add(item_id)

    print(f"handoff_rows={len(rows)}")
    print(f"handoff_columns={len(header)}")
    print(f"handoff_bad_rows={len(bad_rows)}")
    print(f"handoff_relative_links={relative}")
    print(f"handoff_unresolved_links={len(unresolved)}")
    print(f"log_rows={len(log_rows)}")
    print(f"log_columns={len(log_header)}")
    print(f"log_bad_rows={len(log_bad)}")
    print(f"log_duplicate_ids={len(duplicates)}")

    failed = False
    if not header_ok or bad_rows:
        print("HANDOFF table is not 6 columns", file=sys.stderr)
        for lineno, count in bad_rows:
            print(f"  line {lineno}: {count} columns", file=sys.stderr)
        failed = True
    if unresolved:
        print("unresolved relative links:", file=sys.stderr)
        for item in unresolved:
            print(f"  {item}", file=sys.stderr)
        failed = True
    if len(log_header) != LOG_COLS or log_bad:
        print("intake log table is not 12 columns", file=sys.stderr)
        for lineno, count in log_bad:
            print(f"  line {lineno}: {count} columns", file=sys.stderr)
        failed = True
    if duplicates:
        print("duplicate intake IDs: " + ", ".join(duplicates), file=sys.stderr)
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
