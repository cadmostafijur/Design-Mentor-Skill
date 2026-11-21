#!/usr/bin/env python3
"""WCAG 2.x contrast checker. No dependencies.

Usage:
  python contrast.py "#475569" "#ffffff"            # one pair
  python contrast.py "#2563eb:#fff" "#64748b:#f8fafc" # several fg:bg pairs
Prints ratio and AA/AAA pass/fail for normal text, large text and UI components.
"""
import sys


def _hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Bad hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def _luminance(rgb):
    def ch(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    l1, l2 = sorted((_luminance(_hex_to_rgb(fg)), _luminance(_hex_to_rgb(bg))), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def report(fg, bg):
    r = ratio(fg, bg)
    ok = lambda x: "PASS" if x else "fail"
    return (f"{fg} on {bg}: {r:.2f}:1 | "
            f"text AA {ok(r >= 4.5)} AAA {ok(r >= 7)} | "
            f"large text AA {ok(r >= 3)} AAA {ok(r >= 4.5)} | "
            f"UI/graphics {ok(r >= 3)}")


def main(args):
    if not args:
        print(__doc__)
        return 1
    pairs = [a.split(":") for a in args] if ":" in args[0] else [args[:2]]
    for fg, bg in pairs:
        print(report(fg, bg))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
