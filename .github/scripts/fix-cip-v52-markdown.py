#!/usr/bin/env python3
"""Fix the known Markdown lint issues in the four CIP v5.2 documents.

The script is intentionally narrow and deterministic:
- adds the required blank line between the two opening headings;
- converts the bare contact email into a Markdown mailto link;
- refuses to touch any other file.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = (
    "CIP-Core-v5.2-en.md",
    "CIP-Core-v5.2-fr.md",
    "CIP-v5.2-integral-en.md",
    "CIP-v5.2-integrale-fr.md",
)
EMAIL = "ia.normandie.expert@gmail.com"
EMAIL_LINK = f"[{EMAIL}](mailto:{EMAIL})"

for relative in FILES:
    path = ROOT / relative
    if not path.is_file():
        raise FileNotFoundError(path)

    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    if len(lines) < 3:
        raise ValueError(f"Unexpectedly short Markdown file: {relative}")

    # MD022: separate the level-1 and level-2 headings.
    if lines[0].startswith("# ") and lines[1].startswith("## "):
        lines.insert(1, "\n")

    updated = "".join(lines).replace(EMAIL, EMAIL_LINK)
    if updated == original:
        print(f"unchanged: {relative}")
    else:
        path.write_text(updated, encoding="utf-8")
        print(f"updated: {relative}")

print("CIP v5.2 Markdown fixes applied to the allow-listed files only.")
