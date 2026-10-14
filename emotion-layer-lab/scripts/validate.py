#!/usr/bin/env python3
import os
"""Check that the emotion layer is internally consistent. Run after every edit and after render.py.

Checks:
- every bank entry has the required fields, a known policy, and pairs/opposites that exist in the bank
- every blend (examples, regulation map, named blends, compact starting blends, eval expectations)
  uses only bank emotions; every intensity-tagged blend has a Prefer anchor, respects caps,
  totals 6 or less, has at most one intensity 3, and contains no avoid state
- the full prompt's ladders list every emotion exactly once

Usage: python3 scripts/validate.py   (exit code 1 if anything fails)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LM = ROOT / "assets" / "local-model"
REQUIRED = ["emotion", "fa", "source", "evidence", "valence", "usefulness", "usefulness_basis", "category", "family",
            "family_fa", "family_key", "rung", "arousal", "policy", "max_intensity", "pairs_with", "opposite", "function", "risk", "appraisal", "examples"]
POLICIES = {"prefer", "cap", "allow", "keep", "avoid"}


def main():
    bank = {e["emotion"]: e for e in json.loads((LM / "emotion-bank.json").read_text(encoding="utf-8"))["emotions"]}
    full = (LM / "emotion-layer.md").read_text(encoding="utf-8")
    compact = (LM / "emotion-layer-compact.md").read_text(encoding="utf-8")
    evals = (LM / "eval-prompts.md").read_text(encoding="utf-8")
    problems = []

    for name, e in bank.items():
        miss = [k for k in REQUIRED if k not in e]
        if miss:
            problems.append(f"bank {name}: missing {miss}")
            continue
        if e["policy"] not in POLICIES:
            problems.append(f"bank {name}: unknown policy {e['policy']}")
        for other in e["pairs_with"] + [e["opposite"]]:
            if other not in bank:
                problems.append(f"bank {name}: refers to unknown emotion '{other}'")

    def check(parsed, label):
        for n, i in parsed:
            if n not in bank:
                problems.append(f"{label}: unknown emotion '{n}'")
            elif i > bank[n]["max_intensity"]:
                problems.append(f"{label}: {n}:{i} is above its cap {bank[n]['max_intensity']}")
            elif bank[n]["policy"] == "avoid":
                problems.append(f"{label}: avoid state '{n}' in a blend")
        if sum(i for _, i in parsed) > 6:
            problems.append(f"{label}: intensities add up to more than 6")
        if sum(1 for _, i in parsed if i == 3) > 1:
            problems.append(f"{label}: more than one state at 3")
        if not any(bank.get(n, {}).get("policy") == "prefer" for n, _ in parsed):
            problems.append(f"{label}: no Prefer anchor")

    def names_exist(names, label):
        for n in names:
            n = re.sub(r"\(\d\)", "", n).strip()
            if n and n not in bank:
                problems.append(f"{label}: unknown emotion '{n}'")

    for m in re.finditer(r'<emo other="([^"]*)" self="([^"]*)"', full + compact):
        parsed = [(x.strip().rsplit(":", 1)[0], int(x.strip().rsplit(":", 1)[1])) for x in m.group(2).split(",")]
        check(parsed, f"tag self=\"{m.group(2)}\"")
        names_exist([x.strip().rsplit(":", 1)[0] for x in m.group(1).split(",") if x.strip() != "neutral"], "tag other")

    map_sec = full.split("## Regulation map")[1].split("## Named blends")[0]
    for line in map_sec.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and not cells[0].startswith(("Their", "---")):
            # "X 2 or Y 2" means alternatives: check each alternative separately
            first, *rest = cells[1].replace(" then ", ", ").split(",")
            options = [o.strip() for o in first.split(" or ")]
            for opt in options:
                items = [opt] + [r.strip() for r in rest]
                parsed = [(re.sub(r" \d$", "", it).strip(), int(it[-1])) for it in items if re.search(r" \d$", it)]
                check(parsed, f"map '{cells[0]}'")

    named = full.split("## Named blends")[1].split("## ")[0]
    for m in re.finditer(r"^- \*\*([^*]+):\*\* (.+)$", named, re.M):
        names_exist(re.split(r",| then | or ", m.group(2).replace("then ", "")), f"named blend '{m.group(1)}'")

    start = compact.split("## Starting blends")[1].split("## ")[0]
    for line in start.splitlines():
        if "→" in line:
            names_exist(line.split("→")[1].split(","), "compact starting blend")

    for line in evals.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and re.match(r"^[۰-۹0-9]+$", cells[0]):
            names_exist(re.split(r",|/", cells[3]), f"eval {cells[0]}")

    ladder = re.findall(r"([a-z][a-z \-]*?) \[(?:P|C\d|A|K|X)\]", full.split("## The emotion ladders")[1].split("## Psychology rules")[0])
    if sorted(ladder) != sorted(bank):
        problems.append(f"ladders: missing {sorted(set(bank) - set(ladder))}, duplicated {sorted({x for x in ladder if ladder.count(x) > 1})}")

    # invisible characters that can break markdown or scripts (ZWNJ, U+200C, is normal in Persian and allowed)
    skill_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bad = {"\u200b": "U+200B zero-width space", "\ufeff": "U+FEFF byte-order mark", "\u2060": "U+2060 word joiner"}
    for d, _, files in os.walk(skill_root):
        for f in files:
            if not f.endswith((".md", ".py", ".sh", ".json")):
                continue
            path = os.path.join(d, f)
            text = open(path, encoding="utf-8").read()
            for ch, name in bad.items():
                if ch in text:
                    problems.append(f"{os.path.relpath(path, skill_root)}: {text.count(ch)} x {name}")

    if problems:
        print("FAILED")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print(f"OK: {len(bank)} emotions, all blends follow the rules, ladders complete, no invisible characters.")


if __name__ == "__main__":
    main()
