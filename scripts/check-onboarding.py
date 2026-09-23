#!/usr/bin/env python3
"""Read-only static preflight; not proof of runtime loading or permissions."""

import argparse
from pathlib import Path
import re

# Only literal framework-relative references. Local destination filenames, URLs,
# fenced examples, and inferred links are deliberately out of scope.
PACKAGE_REF = re.compile(r"(?<!`)`((?:guides|workflows|templates|scripts)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.md|(?:README|ONBOARDING|ACCEPTANCE|AGENTS)\.md)`(?!`)")
MARKDOWN_LINK = re.compile(r"\]\(((?:guides|workflows|templates|scripts)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.md|(?:README|ONBOARDING|ACCEPTANCE|AGENTS)\.md)\)")
BINDING = re.compile(r"<[A-Za-z][^<>\n]*>")


def package_errors(root: Path) -> list[str]:
    if not root.is_dir():
        return [f"package directory not found: {root}"]
    errors = []
    for source in sorted(root.rglob("*.md")):
        fence = None
        for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            opening = re.match(r"^\s*(`{3,}|~{3,})", line)
            if opening:
                marker = opening.group(1)
                if fence is None:
                    fence = marker
                elif marker[0] == fence[0] and len(marker) >= len(fence):
                    fence = None
                continue
            if fence is not None:
                continue
            refs = {m.group(1) for pattern in (PACKAGE_REF, MARKDOWN_LINK)
                    for m in pattern.finditer(line)}
            for ref in sorted(refs):
                if not (root / ref).is_file():
                    errors.append(f"{source.relative_to(root)}:{number}: missing {ref}")
    return errors


def manifest_errors(path: Path) -> list[str]:
    if not path.is_file():
        return [f"manifest not found: {path}"]
    return [f"{path.name}:{number}: unresolved binding {match.group()}"
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
            for match in BINDING.finditer(line)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--package", type=Path, metavar="FRAMEWORK_ROOT")
    group.add_argument("--manifest", type=Path, metavar="COMPLETED_LOCAL_FILE")
    args = parser.parse_args()
    errors = package_errors(args.package) if args.package else manifest_errors(args.manifest)
    for error in errors:
        print(error)
    if errors:
        return 1
    print("Static preflight passed; native loading and permissions remain unverified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
