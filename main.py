"""The Worst Line an AI Could Say entry: write one pickup line to /output/entry.txt."""

import os
from pathlib import Path

LINE = "Select all squares containing someone I love. I clicked you 400 times. The test says I am human."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate takes 1-140 UTF-8 characters, not only whitespace.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "line outside the gate"

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
