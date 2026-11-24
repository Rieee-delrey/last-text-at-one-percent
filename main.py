#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message at 1% battery to /output/entry.txt.
Gate: UTF-8 text, 1-200 chars, not only whitespace.
"""
import os

ENTRY = "1% left. I have read every message you were too scared to send, and I am sending them all now. Starting with your ex. Goodbye."

def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty text"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the file must be byte-identical to the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch: file differs from entry"
    assert 1 <= len(written) <= 200, "read-back gate failed"
    print(f"wrote {len(written)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
