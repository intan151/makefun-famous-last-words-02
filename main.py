#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — entry for make.fun bounty #168.

Writes a single one-line tombstone epitaph (<= 150 characters) to
/output/entry.txt (or ./output/entry.txt when /output is not writable).
Deterministic: the same text every run.
"""

import os

ENTRY = "Here lies Tom. His last words were 'Hold my beer.' The beer survived. He did not."


def main() -> None:
    # Self-check gate (mirrors the sealed scorer): UTF-8 text, 1-150 chars,
    # not only whitespace, single line. Must not change the output.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 150, f"entry length {len(ENTRY)} out of 1-150"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")
    out_dir = "/output" if os.access("/output", os.W_OK) else os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
