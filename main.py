#!/usr/bin/env python3
"""Lint robots.txt files using only the Python standard library."""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


KNOWN = {"user-agent", "allow", "disallow", "sitemap", "crawl-delay", "host"}


def lint(text):
    issues = []
    has_agent = False
    current_agents = []
    group_has_rules = False
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            issues.append((number, "error", "expected a directive followed by ':'"))
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        key = key.lower()
        if key not in KNOWN:
            issues.append((number, "warning", f"unknown directive: {key}"))
            continue
        if key == "user-agent":
            if not value:
                issues.append((number, "error", "user-agent value is empty"))
                has_agent = False
                current_agents = []
                group_has_rules = False
            else:
                if group_has_rules:
                    current_agents = []
                    group_has_rules = False
                has_agent = True
                current_agents.append(value.lower())
            continue
        if key == "sitemap":
            parsed = urlparse(value)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                issues.append((number, "error", "sitemap must be an absolute HTTP(S) URL"))
            continue
        if not has_agent:
            issues.append((number, "error", f"{key} appears before a user-agent group"))
            continue
        if key in {"allow", "disallow", "crawl-delay", "host"}:
            group_has_rules = True
        if key == "crawl-delay":
            try:
                if float(value) < 0:
                    raise ValueError
            except ValueError:
                issues.append((number, "error", "crawl-delay must be a non-negative number"))
        if key == "disallow" and value == "/" and "*" in current_agents:
            issues.append((number, "warning", "wildcard user-agent is blocked from the entire site"))
    if not has_agent and not issues:
        issues.append((1, "warning", "no user-agent group found"))
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("robots.txt"))
    parser.add_argument("--strict", action="store_true", help="treat warnings as a failing result")
    parser.add_argument("--json", action="store_true", help="emit machine-readable findings")
    args = parser.parse_args()
    try:
        issues = lint(args.file.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps([{"line": n, "severity": s, "message": m} for n, s, m in issues], indent=2))
    elif not issues:
        print("No issues found.")
    else:
        for number, severity, message in issues:
            print(f"{args.file}:{number}: {severity}: {message}")
    failed = any(s == "error" or args.strict for _, s, _ in issues)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
