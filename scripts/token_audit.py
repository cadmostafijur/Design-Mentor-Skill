#!/usr/bin/env python3
"""Find hardcoded design values that should be tokens. No dependencies.

Usage:
  python token_audit.py <path> [<path> ...]

Scans .css .scss .less .tsx .jsx .ts .js .vue .svelte .html files for:
  - hex / rgb() / hsl() colors used outside token definitions
  - px values for spacing/sizing that are off a 4px grid
  - distinct font-size values (a long list signals a missing type scale)
CSS custom property definitions (--name: value) are treated as token
definitions and ignored. Output is a summary plus file:line occurrences, meant
as evidence for a design-system audit, not a substitute for judgment.
"""
import os
import re
import sys
from collections import Counter

EXT = {".css", ".scss", ".less", ".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".html"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "coverage"}
COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")
PX = re.compile(r"(?<![\w.-])(\d+(?:\.\d+)?)px")
FONT_SIZE = re.compile(r"font-size\s*:\s*([^;\"'}]+)|fontSize\s*:\s*['\"]?([^,'\"}]+)")
TOKEN_DEF = re.compile(r"--[\w-]+\s*:[^;}]*")


def files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for n in names:
                if os.path.splitext(n)[1] in EXT:
                    yield os.path.join(root, n)


def main(paths):
    if not paths:
        print(__doc__)
        return 1
    colors, offgrid, sizes = Counter(), Counter(), Counter()
    hits = []
    for f in files(paths):
        try:
            lines = open(f, encoding="utf-8", errors="ignore").read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            line = TOKEN_DEF.sub("", line)  # token definitions are allowed
            for c in COLOR.findall(line):
                colors[c.lower()] += 1
                hits.append(f"{f}:{i}  color {c}")
            for v in PX.findall(line):
                n = float(v)
                if n > 2 and n % 4:
                    offgrid[v + "px"] += 1
                    hits.append(f"{f}:{i}  off-grid {v}px")
            for a, b in FONT_SIZE.findall(line):
                sizes[(a or b).strip()] += 1

    print("== Summary ==")
    print(f"Hardcoded colors: {sum(colors.values())} uses, {len(colors)} distinct")
    for c, n in colors.most_common(15):
        print(f"  {c}  x{n}")
    print(f"Off-4px-grid values: {sum(offgrid.values())} uses, {len(offgrid)} distinct")
    for v, n in offgrid.most_common(15):
        print(f"  {v}  x{n}")
    print(f"Distinct font-size values: {len(sizes)}" + ("  (more than ~8 suggests no type scale)" if len(sizes) > 8 else ""))
    for s, n in sizes.most_common(15):
        print(f"  {s}  x{n}")
    print("\n== Occurrences (first 200) ==")
    print("\n".join(hits[:200]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
