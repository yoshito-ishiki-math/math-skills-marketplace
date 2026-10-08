#!/usr/bin/env python3
"""Issue, locate, and check literal paragraph IDs without editing TeX sources."""
from __future__ import annotations

import argparse
import re
import secrets
from pathlib import Path

ID = re.compile(r"p-[0-9a-f]{12}\Z")
LITERAL = {"verbatim", "verbatim*", "Verbatim", "BVerbatim", "lstlisting", "minted", "comment"}
SKIP = {".git", "build", "dist", "output", ".venv", ".uv-cache", "__pycache__"}


def visible_source(text: str, include_comments: bool = False) -> str:
    """Blank comments and common literal environments, preserving offsets."""
    chars = list(text)
    i = 0
    while i < len(text):
        end = i
        if text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            if include_comments:
                i = end
                continue
        elif text[i] == "\\":
            env = re.match(r"\\begin\s*\{([^}]+)\}", text[i:])
            verb = re.match(r"\\verb\*?(?![A-Za-z])", text[i:])
            if env and env[1] in LITERAL:
                close = re.search(r"\\end\s*\{" + re.escape(env[1]) + r"\}", text[i + env.end():])
                end = len(text) if close is None else i + env.end() + close.end()
            elif verb and i + verb.end() < len(text):
                start = i + verb.end()
                close = text.find(text[start], start + 1)
                end = len(text) if close < 0 else close + 1
            else:
                # Consume escaped % and other control symbols as a unit.
                token = re.match(r"\\(?:[A-Za-z@]+|.)", text[i:])
                i += token.end() if token else 1
                continue
        if end > i:
            for j in range(i, end):
                if chars[j] != "\n":
                    chars[j] = " "
            i = end
        else:
            i += 1
    return "".join(chars)


def occurrences(root: Path, include_comments: bool = False):
    paths = [root] if root.is_file() else sorted(root.rglob("*.tex"))
    for path in paths:
        relative = path.relative_to(root) if root.is_dir() else Path(path.name)
        if any(part in SKIP for part in relative.parts) or path.is_symlink():
            continue
        text = path.read_text(encoding="utf-8")
        clean = visible_source(text, include_comments)
        for match in re.finditer(r"\\paraid(?![A-Za-z@])\s*\{([^{}]*)\}", clean):
            yield match[1], path, text.count("\n", 0, match.start()) + 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["new", "check", "find"])
    parser.add_argument("identifier", nargs="?")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--include-comments", action="store_true",
                        help="include commented tags in find/check; new always reserves them")
    args = parser.parse_args(argv)
    if not args.root.exists():
        parser.error("--root does not exist")
    if args.action == "find" and not args.identifier:
        parser.error("find requires an ID")
    if args.count < 1:
        parser.error("--count must be positive")
    rows = list(occurrences(args.root, args.action == "new" or args.include_comments))
    if args.action == "new":
        used = {row[0] for row in rows}
        for _ in range(args.count):
            while (value := "p-" + secrets.token_hex(6)) in used:
                pass
            used.add(value)
            print("\\paraid{" + value + "}")
        return 0
    if args.action == "find":
        found = [row for row in rows if row[0] == args.identifier]
        for value, path, line in found:
            print(f"{path}:{line}: {value}")
        return 0 if found else 1
    seen = {}
    errors = 0
    for value, path, line in rows:
        if not ID.fullmatch(value):
            print(f"INVALID {path}:{line}: {value}")
            errors += 1
        elif value in seen:
            print(f"DUPLICATE {path}:{line}: {value}; first at {seen[value]}")
            errors += 1
        else:
            seen[value] = f"{path}:{line}"
    print(f"{len(rows)} marker(s), {errors} error(s).")
    return int(errors > 0)


if __name__ == "__main__":
    raise SystemExit(main())
