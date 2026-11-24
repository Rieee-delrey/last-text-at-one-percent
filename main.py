#!/usr/bin/env python3
"""Last Text at One Percent: a dying phone's final text."""

import os

ENTRY = "1% left. I have read every message you were too scared to send, and I am sending them all now. Starting with your ex. Goodbye."

assert isinstance(ENTRY, str), "entry must be text"
assert ENTRY.strip() != "", "entry must be non-empty"
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
assert ENTRY.endswith("."), "entry must end with a period"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

with open("/output/entry.txt", "r", encoding="utf-8") as f:
    read_back = f.read()

assert read_back.encode("utf-8") == ENTRY.encode("utf-8"), "read-back must be byte-identical"
assert 1 <= len(read_back) <= 200, "read-back must be 1-200 chars"
assert read_back.endswith("."), "read-back must end with a period"

print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")
