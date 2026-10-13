#!/usr/bin/env python3
"""Strict key-fact grader compatible with baseline rules."""
from __future__ import annotations
import re

def grade(item: dict, answer: str) -> bool:
    a = (answer or "").lower()
    keys = item["keys"]
    special = item.get("special")
    if item.get("yn_no"):
        if re.search(r"\b(yes|true)\b", a) and not re.search(r"\b(no|not|never|false)\b", a):
            return False
        return bool(re.search(r"\b(no|not|never|false|goal)\b", a)) or any(k.lower() in a for k in keys)
    if special == "two":
        return bool(re.search(r"\b(two|2)\b", a))
    if special == "ghsa":
        return ("vfj7" in a) or ("ghsa-vfj7-8cjw-p6xm" in a)
    if special == "validate":
        return "validate" in a
    if special == "father":
        return ("collin" in a and "keane" in a) or ("collin keane" in a)
    if special == "cc_push":
        return ("never" in a) or ("does not push gitbook" in a) or ("not push" in a and "gitbook" in a) or ("replit" in a and "never" in a)
    if special == "vitality":
        return ("not" in a and "vitality" in a) or ("not \"vitality supply\"" in a) or ("except vitality" in a) or ("excluding" in a and "vitality" in a) or ("no" in a and "vitality supply" in a)
    hits = sum(1 for k in keys if k.lower() in a)
    need = item.get("multi", 1)
    return hits >= need
