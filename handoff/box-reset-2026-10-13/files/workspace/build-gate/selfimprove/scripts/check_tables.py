#!/usr/bin/env python3
"""Check markdown pipe tables: every row has the header's column count, and when the first
column is an ID-like column ("ID", "#", "Entry", ...) its values are unique within the file.
Usage: check_tables.py FILE.md ...   Exit 1 on any problem."""
import re, sys

ID_HEADERS = {"id", "#", "entry", "entry id", "item", "ticket"}

def cells(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"): s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]

def check(path):
    probs, lines = [], open(path, encoding="utf-8").read().splitlines()
    i, in_code = 0, False
    while i < len(lines):
        if lines[i].lstrip().startswith("```"): in_code = not in_code
        if (not in_code and lines[i].lstrip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1])):
            hdr = cells(lines[i]); n = len(hdr); start = i + 1
            sep = cells(lines[i + 1])
            if len(sep) != n: probs.append(f"{path}:{i+2}: separator has {len(sep)} columns, header has {n}")
            idcol = hdr[0].lower() in ID_HEADERS
            seen = {}
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                row = cells(lines[j])
                if len(row) != n: probs.append(f"{path}:{j+1}: row has {len(row)} columns, header has {n}")
                if idcol and row and row[0]:
                    if row[0] in seen: probs.append(f"{path}:{j+1}: duplicate ID {row[0]} (first at line {seen[row[0]]})")
                    else: seen[row[0]] = j + 1
                j += 1
            i = j; continue
        i += 1
    return probs

def main(argv):
    probs = [p for f in argv for p in check(f)]
    for p in probs: print(p)
    print(f"checked {len(argv)} file(s), {len(probs)} problem(s)")
    return 1 if probs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
