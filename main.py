"""The Worst Line an AI Could Say entry: write one pickup line to /output/entry.txt."""

import os
from pathlib import Path

LINE = "Select all squares containing someone I love. I clicked you 400 times. The test says I am human."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def _validate(line):
    # The gate takes 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(line) <= 140 and line.strip(), "line outside the gate"
    assert line.encode("utf-8").decode("utf-8") == line, "line is not clean UTF-8"


def write_entry(line, output_dir):
    """Validate the line against the gate, then write it as entry.txt."""
    _validate(line)
    out = Path(output_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    return out


write_entry(LINE, OUTPUT_DIR)
