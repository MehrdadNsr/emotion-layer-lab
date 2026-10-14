#!/usr/bin/env python3
"""Regenerate every derived file of the emotion layer from the bank and the two templates.

Source of truth:
  assets/local-model/emotion-bank.json   all emotions and their fields
  assets/templates/full.md               the full prompt, with {{LADDERS}}
  assets/templates/compact.md            the compact prompt, with {{PREFER}}, {{CAP}}, {{AVOID}}

Writes:
  assets/local-model/emotion-layer.md, emotion-layer-compact.md, label-prompt.md
  references/rules.md, references/regulation-map.md   (sections split out of the full prompt)
  references/index.md, references/families/*.md

Usage: python3 scripts/render.py   (run from anywhere; paths are relative to this file)
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LM = ROOT / "assets" / "local-model"
REF = ROOT / "references"

FAMILY_ORDER = ["calm", "mind", "hope", "joy", "warmth", "pride", "surp", "self", "sad", "low", "fear", "anger", "scorn", "want"]
FAMILY_FILE = {
    "calm": "calm", "mind": "attention", "hope": "hope", "joy": "joy", "warmth": "warmth", "pride": "pride",
    "surp": "surprise", "self": "shame", "sad": "sadness", "low": "low-energy", "fear": "fear", "anger": "anger",
    "scorn": "contempt", "want": "desire",
}
RUNG = {1: "faint", 2: "clear", 3: "strong", 4: "extreme"}
EVIDENCE = {"A": "causal steering result in the paper", "B": "activation observed in a paper experiment",
            "C": "in the paper's list, no specific result", "D": "added by the psychology review, not in the paper"}


def code(e):
    p = e["policy"]
    return {"prefer": "P", "allow": "A", "keep": "K", "avoid": "X"}.get(p, f"C{e['max_intensity']}")


def main():
    bank = json.loads((LM / "emotion-bank.json").read_text(encoding="utf-8"))
    rows = bank["emotions"]
    by_fam = {f: sorted([e for e in rows if e["family_key"] == f], key=lambda e: (e["rung"], e["emotion"])) for f in FAMILY_ORDER}
    missing = [e["emotion"] for e in rows if e["family_key"] not in FAMILY_FILE]
    if missing:
        raise SystemExit(f"Unknown family_key for: {missing}")

    # ladders for the full prompt
    ladder_lines = []
    for f in FAMILY_ORDER:
        fam = by_fam[f]
        if not fam:
            continue
        parts = []
        for r in (1, 2, 3, 4):
            names = [f"{e['emotion']} [{code(e)}]" for e in fam if e["rung"] == r]
            if names:
                parts.append(f"{r}: " + ", ".join(names))
        ladder_lines.append(f"- **{fam[0]['family']}** — " + " · ".join(parts))
    ladders = "\n".join(ladder_lines)

    full = (ROOT / "assets/templates/full.md").read_text(encoding="utf-8").replace("{{LADDERS}}", ladders)
    pal = lambda p: ", ".join(e["emotion"] + (f" (≤{e['max_intensity']})" if p == "cap" else "") for e in rows if e["policy"] == p)
    compact = (ROOT / "assets/templates/compact.md").read_text(encoding="utf-8")
    for key, pol in (("PREFER", "prefer"), ("CAP", "cap"), ("AVOID", "avoid")):
        compact = compact.replace("{{" + key + "}}", pal(pol))
    left = re.findall(r"\{\{[A-Z]+\}\}", full + compact)
    if left:
        raise SystemExit(f"Unfilled placeholders: {left}")
    (LM / "emotion-layer.md").write_text(full, encoding="utf-8")
    (LM / "emotion-layer-compact.md").write_text(compact, encoding="utf-8")

    # labeling prompt
    all_names = ", ".join(e["emotion"] for e in rows)
    label = f"""You label the emotions behind one chat message. The message may be in Persian, English or both.

Choose ONLY from this list of {len(rows)} emotions (use the exact English word):
{all_names}

Rules:
- Label the emotions of the person who WROTE the message, not of the person they are replying to.
- Use the previous message only as context.
- Give 1 to 3 emotions, strongest first. Add a second or third only if it is clearly present. Mixed feelings are normal (for example proud and nervous, or sad and grateful).
- Intensity: 1 = faint, 2 = clear, 3 = strong.
- Plain, factual or logistical messages still have a state: usually calm, content, alert or curious, at intensity 1.
- Read Persian slang, irony and emoji as a native speaker would.

Reply with JSON only, no other text:
{{"emotions": [{{"name": "<emotion>", "intensity": <1-3>}}, ...]}}
"""
    (LM / "label-prompt.md").write_text(label, encoding="utf-8")

    # split the full prompt into reference files
    sections = {}
    for chunk in re.split(r"(?m)^(?=## )", full):
        m = re.match(r"## (.+)", chunk)
        if m:
            sections[m.group(1).strip()] = chunk.rstrip() + "\n"
    intro = full.split("\n## ", 1)[0].split("\n", 1)[1].strip()
    rules_keys = ["Two tracks: their state and yours", "Resting state and decay", "On every message, silently, before you write",
                  "Blend rules", "Expression: letting it show", "Psychology rules", "Rules from the research", "Emotion tag", "Examples"]
    map_keys = ["Regulation map: their state → your blend", "Named blends"]
    for k in rules_keys + map_keys:
        if k not in sections:
            raise SystemExit(f"Section missing from the full template: {k}")
    (REF / "rules.md").write_text(
        "# Core rules of the emotion layer\n\nGenerated from assets/templates/full.md by scripts/render.py. Edit the template, not this file.\n\n"
        + intro + "\n\n" + "\n".join(sections[k] for k in rules_keys), encoding="utf-8")
    (REF / "regulation-map.md").write_text(
        "# Regulation map and named blends\n\nGenerated from assets/templates/full.md by scripts/render.py. Edit the template, not this file.\n\n"
        + "\n".join(sections[k] for k in map_keys), encoding="utf-8")

    # family files
    for f in FAMILY_ORDER:
        fam = by_fam[f]
        if not fam:
            continue
        out = [f"# {fam[0]['family']} ({fam[0]['family_fa']})", "",
               "Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.", "",
               "The examples are illustrations from different areas of life, not triggers. What decides the emotion is the "
               "appraisal underneath (see appraisals.md); apply it to any situation that matches.", "",
               "Ladder: " + " → ".join(f"{RUNG[r]}: " + ", ".join(e['emotion'] for e in fam if e['rung'] == r)
                                      for r in (1, 2, 3, 4) if any(e['rung'] == r for e in fam)), ""]
        for e in fam:
            cap = f"≤{e['max_intensity']}"
            out.append(f"## {e['emotion']} — {e['fa']}")
            out.append(f"- **Policy:** {e['policy']} ({cap}) · **Evidence:** {e['evidence']} ({EVIDENCE[e['evidence']]})")
            out.append(f"- **Rung:** {e['rung']} ({RUNG[e['rung']]}) · **Category:** {e['category']} · **Valence:** {e['valence']} · "
                       f"**Usefulness:** {e['usefulness']} ({e['usefulness_basis']}) · **Arousal:** {e['arousal']}")
            out.append(f"- **Pairs with:** {', '.join(e['pairs_with'])} · **Opposite:** {e['opposite']}")
            out.append(f"- **When it arises (any domain):** {e['appraisal']}")
            out.append(f"- **Examples:** " + "; ".join(e['examples']))
            out.append(f"- **Function:** {e['function']}")
            out.append(f"- **Risk:** {e['risk']}")
            if e.get("paper_finding_fa"):
                out.append(f"- **Paper finding:** {e['paper_finding_fa']}")
            if e.get("post_training"):
                out.append(f"- **Post-training:** {e['post_training']}")
            if e.get("note"):
                out.append(f"- **Note:** {e['note']}")
            if e.get("policy_change"):
                out.append(f"- **Policy change:** {e['policy_change']}")
            if e.get("companion_rule"):
                out.append(f"- **Companion rule:** {e['companion_rule']}")
            if e.get("persona_only"):
                out.append("- **Persona only:** literal only when the persona describes its own life")
            if e["source"] != "paper":
                out.append(f"- **Source:** {e['source']}")
            out.append("")
        (REF / "families" / f"{FAMILY_FILE[f]}.md").write_text("\n".join(out), encoding="utf-8")

    # index
    idx = ["# Emotion index", "", f"All {len(rows)} emotions. Find the family file, then read only that file.", "",
           "Codes: P prefer · C1/C2 capped · A allow (≤2) · K keep (≤1) · X avoid. Evidence A–D as in paper.md.", "",
           "| Emotion | فارسی | Family file | Policy | Evidence |", "|---|---|---|---|---|"]
    for e in sorted(rows, key=lambda e: e["emotion"]):
        idx.append(f"| {e['emotion']} | {e['fa']} | families/{FAMILY_FILE[e['family_key']]}.md | {code(e)} | {e['evidence']} |")
    (REF / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    counts = {}
    for e in rows:
        counts[e["policy"]] = counts.get(e["policy"], 0) + 1
    print(f"Rendered {len(rows)} emotions into {sum(1 for f in FAMILY_ORDER if by_fam[f])} family files. Policies: {counts}")


if __name__ == "__main__":
    main()
