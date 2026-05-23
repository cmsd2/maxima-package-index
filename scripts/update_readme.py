#!/usr/bin/env python3
"""Regenerate the package table in README.md from index.json.

Packages are sorted alphabetically by name. Each package name links to
its repository. Run with --check to fail (non-zero exit) if the README
is out of date instead of rewriting it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
README = ROOT / "README.md"

SECTION_RE = re.compile(
    r"(## Current packages\n\n)(.*?)(\n## )",
    re.DOTALL,
)


def repo_url(pkg: dict) -> str:
    url = pkg.get("repository", "").rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    return url


def build_table(packages: dict) -> str:
    lines = ["| Package | Description |", "|---------|-------------|"]
    for name in sorted(packages):
        pkg = packages[name]
        url = repo_url(pkg)
        label = f"[{name}]({url})" if url else name
        desc = pkg.get("description", "").strip()
        lines.append(f"| {label} | {desc} |")
    return "\n".join(lines) + "\n"


def render(readme: str, table: str) -> str:
    new, n = SECTION_RE.subn(lambda m: f"{m.group(1)}{table}{m.group(3)}", readme, count=1)
    if n == 0:
        raise SystemExit("Could not find '## Current packages' section in README.md")
    return new


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if README is out of date")
    args = parser.parse_args()

    data = json.loads(INDEX.read_text())
    table = build_table(data["packages"])
    current = README.read_text()
    updated = render(current, table)

    if updated == current:
        print("README is up to date")
        return 0

    if args.check:
        print("README is out of date; run scripts/update_readme.py", file=sys.stderr)
        return 1

    README.write_text(updated)
    print(f"Updated {README.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
