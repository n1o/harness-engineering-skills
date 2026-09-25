#!/usr/bin/env python3
"""Structural checks for the harness-engineering skill.

Verifies:
1. Rule files: `# <id>` matching filename, `>` summary, `## Why It Matters`,
   `## Scope`, `## Source` with URL, `## See Also` with valid sibling links.
   Every rule id uses a known category prefix.
2. SKILL.md: parseable YAML frontmatter with required keys; category table
   counts match the rules/ directory; all start-here links resolve.
3. INDEX.md: lists every rule exactly once, links valid, one-line summaries
   match the rule files' `>` lines.
4. Attribution sanity: flags source labels whose named publisher has no
   matching domain among the URLs in the same Source section (review list,
   not proof of error).

Run: python3 checks/validate.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "rules"
SKILL = ROOT / "SKILL.md"
INDEX = ROOT / "INDEX.md"

PREFIXES = [
    "ctx", "ver", "run", "tool", "guard",
    "eval", "struct", "obs", "ops", "prin",
]

# publisher label -> acceptable URL substrings
PUBLISHER_DOMAINS = {
    "anthropic": ["anthropic.com"],
    "openai": ["openai.com"],
    "humanlayer": ["humanlayer.dev", "12factoragents"],
    "manus": ["manus.im"],
    "fowler": ["martinfowler.com"],
    "thoughtworks": ["martinfowler.com", "thoughtworks.com"],
    "openhands": ["openhands.dev", "all-hands.dev"],
    "langchain": ["langchain.com", "langchain.dev", "blog.langchain.com", "langchain-ai"],
    "opentelemetry": ["opentelemetry.io", "open-telemetry", "otel"],
    "spend rails": ["joeyycli.github.io"],
    "loop & retry": ["loopandretry.github.io"],
    "loop and retry": ["loopandretry.github.io"],
    "distributed retry": ["loopandretry.github.io"],
    "simon willison": ["simonwillison.net"],
    "12 factor agents": ["humanlayer.dev"],
}

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def main():
    # ---------- 1. rule files ----------
    files = sorted(RULES.glob("*.md"))
    if not files:
        err("no rule files found in rules/")

    rule_summaries = {}
    for f in files:
        text = f.read_text()
        stem = f.stem
        prefix = stem.split("-")[0]
        if prefix not in PREFIXES:
            err(f"{f.name}: unknown category prefix '{prefix}-'")

        m = re.match(r"^# ([a-z0-9-]+)\n\n> (.+)", text)
        if not m:
            err(f"{f.name}: missing '# <id>' header or '> summary' line")
            continue
        if m.group(1) != stem:
            err(f"{f.name}: header id '{m.group(1)}' != filename '{stem}'")
        rule_summaries[stem] = m.group(2)

        for section in ("## Why It Matters", "## Scope", "## Source", "## See Also"):
            if section not in text:
                err(f"{f.name}: missing required section '{section}'")

        # section order: Why It Matters < Scope < Source < See Also
        positions = [text.find(s) for s in
                     ("## Why It Matters", "## Scope", "## Source", "## See Also")]
        if -1 in positions:
            continue
        if positions != sorted(positions):
            err(f"{f.name}: sections out of order (expected: Why It Matters, Scope, Source, See Also)")

        # source must have a URL
        src = text.split("## Source", 1)[-1].split("## See Also", 1)[0]
        if "http" not in src:
            err(f"{f.name}: Source section has no URL")

        # attribution sanity: label mentions publisher whose domain is absent
        src_lower = src.lower()
        for label, domains in PUBLISHER_DOMAINS.items():
            if re.search(rf"\b{re.escape(label)}\b", src_lower):
                if not any(d in src_lower for d in domains):
                    warn(f"{f.name}: Source mentions '{label}' but no {domains[0]} URL found")

        # See Also links resolve to sibling rules
        see = text.split("## See Also", 1)[-1]
        for link in re.findall(r"\[([a-z0-9-]+)\]\(\1\.md\)", see):
            if link == stem:
                err(f"{f.name}: See Also links to itself")
            if not (RULES / f"{link}.md").exists():
                err(f"{f.name}: See Also links to missing rule '{link}'")

    file_ids = [f.stem for f in files]

    # ---------- 2. SKILL.md ----------
    skill = SKILL.read_text()
    fm = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not fm:
        err("SKILL.md: missing YAML frontmatter")
    else:
        for key in ("name:", "description:", "license:"):
            if key not in fm.group(1):
                err(f"SKILL.md: frontmatter missing '{key}'")

    # category table counts match directory
    for row in re.findall(r"`(\w+)-` \((\d+)\)", skill):
        pfx, n = row
        actual = sum(1 for i in file_ids if i.startswith(pfx + "-"))
        if actual != int(n):
            err(f"SKILL.md: category '{pfx}-' claims {n} rules, directory has {actual}")

    # all relative links in SKILL.md resolve
    for target in re.findall(r"\]\((?!http)([^)#]+?\.md)\)", skill):
        if not (ROOT / target).exists():
            err(f"SKILL.md: broken link '{target}'")

    # ---------- 3. INDEX.md ----------
    index = INDEX.read_text()
    listed = re.findall(r"^- \[`([a-z0-9-]+)`\]\(rules/([a-z0-9-]+)\.md\) - (.+)$",
                        index, re.MULTILINE)
    listed_ids = [a for a, b, _ in listed]
    for a, b, _ in listed:
        if a != b:
            err(f"INDEX.md: link text '{a}' != target '{b}'")
        if not (RULES / f"{a}.md").exists():
            err(f"INDEX.md: links to missing rule '{a}.md'")
    for r in sorted(set(file_ids) - set(listed_ids)):
        err(f"INDEX.md: rule '{r}' not listed")
    for r in sorted(set(listed_ids) - set(file_ids)):
        err(f"INDEX.md: lists unknown rule '{r}'")
    dupes = {x for x in listed_ids if listed_ids.count(x) > 1}
    for r in sorted(dupes):
        err(f"INDEX.md: rule '{r}' listed more than once")

    for rid, _, summary in listed:
        rule_text = (RULES / f"{rid}.md").read_text()
        m = re.match(r"^# [a-z0-9-]+\n\n> (.+)$", rule_text, re.MULTILINE)
        if m and m.group(1).strip() != summary.strip():
            err(f"INDEX.md: summary for '{rid}' differs from rule file")

    # ---------- report ----------
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"OK: {len(files)} rules, SKILL.md and INDEX.md in sync, "
          f"all sections present ({len(warnings)} attribution warning(s))")


if __name__ == "__main__":
    main()
