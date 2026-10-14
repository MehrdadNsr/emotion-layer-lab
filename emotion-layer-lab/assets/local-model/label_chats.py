#!/usr/bin/env python3
"""Label your own messages with emotions from emotion-bank.json, fully locally through Ollama.

Each message gets 1 to 3 emotions with intensities, so mixed feelings (proud + nervous,
sad + grateful) are captured.

Input:  a JSONL file with one message per line: {"text": "...", "prev": "..."}  (prev is optional)
        (telegram_to_jsonl.py produces this format)
Output: <name>.labels.jsonl    the labels for each message
        <name>.profile.json    your emotional profile: most frequent emotions, most frequent
                               blends, valence mix, and ready-made lines for your persona prompt

Usage:
  python3 label_chats.py my_messages.jsonl --model qwen2.5:14b --limit 500

Nothing leaves your machine: it only talks to Ollama on localhost.
"""
import argparse
import collections
import itertools
import json
import pathlib
import random
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
BANK = json.loads((HERE / "emotion-bank.json").read_text(encoding="utf-8"))
BY_NAME = {e["emotion"]: e for e in BANK["emotions"]}
SYSTEM = (HERE / "label-prompt.md").read_text(encoding="utf-8")


def ask(host, model, text, prev):
    user = (f"Previous message from the other person: {prev}\n\n" if prev else "") + f"Message to label: {text}"
    body = {
        "model": model,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
    }
    req = urllib.request.Request(
        f"{host}/api/chat", data=json.dumps(body).encode("utf-8"), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(json.loads(r.read())["message"]["content"])


def to_int(value, default=2):
    try:
        return min(3, max(1, int(value)))
    except (TypeError, ValueError):
        return default


def clean(label):
    """Return a list of up to 3 {name, intensity} that exist in the bank, strongest first, or None."""
    items = []
    if isinstance(label.get("emotions"), list):
        for e in label["emotions"]:
            if isinstance(e, dict):
                items.append((str(e.get("name", "")).strip().lower(), to_int(e.get("intensity"))))
    elif "primary" in label:  # older single-emotion format
        items.append((str(label.get("primary", "")).strip().lower(), to_int(label.get("intensity"))))
        if label.get("secondary"):
            items.append((str(label["secondary"]).strip().lower(), 1))
    seen, out = set(), []
    for name, intensity in items:
        if name in BY_NAME and name not in seen:
            seen.add(name)
            out.append({"name": name, "intensity": intensity})
    out.sort(key=lambda e: -e["intensity"])
    return out[:3] or None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="JSONL file of your messages")
    ap.add_argument("--model", default="qwen2.5:14b")
    ap.add_argument("--host", default="http://localhost:11434")
    ap.add_argument("--limit", type=int, default=500, help="random sample size (0 = all)")
    ap.add_argument("--seed", type=int, default=13)
    args = ap.parse_args()

    src = pathlib.Path(args.input)
    msgs = [json.loads(l) for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
    if args.limit and len(msgs) > args.limit:
        random.Random(args.seed).shuffle(msgs)
        msgs = msgs[: args.limit]

    out_path = src.with_name(src.stem + ".labels.jsonl")
    primary, anywhere, blends, valence = (collections.Counter() for _ in range(4))
    failed = 0
    with out_path.open("w", encoding="utf-8") as out:
        for i, m in enumerate(msgs, 1):
            try:
                emotions = clean(ask(args.host, args.model, m["text"], m.get("prev", "")))
            except Exception:  # network or JSON problem: count it and move on
                emotions = None
            if not emotions:
                failed += 1
                continue
            names = [e["name"] for e in emotions]
            primary[names[0]] += 1
            valence[BY_NAME[names[0]]["valence"]] += 1
            anywhere.update(names)
            if len(names) > 1:
                blends.update(" + ".join(sorted(p)) for p in itertools.combinations(names, 2))
            out.write(json.dumps({**m, "emotions": emotions}, ensure_ascii=False) + "\n")
            if i % 25 == 0:
                print(f"{i}/{len(msgs)} labeled")

    total = sum(primary.values())
    if not total:
        print("No usable labels. Check that Ollama is running and the model name is right.")
        return
    top = anywhere.most_common(20)
    usable = [e for e, _ in top if BY_NAME[e]["policy"] != "avoid"][:10]
    held_back = [e for e, _ in top if BY_NAME[e]["policy"] == "avoid"]
    top_blends = blends.most_common(10)
    profile = {
        "labeled": total,
        "failed": failed,
        "valence_mix_of_primary": {k: round(v / total, 3) for k, v in valence.items()},
        "top_emotions": [
            {"emotion": e, "share_of_messages": round(n / total, 3), "policy": BY_NAME[e]["policy"], "fa": BY_NAME[e]["fa"]}
            for e, n in top
        ],
        "top_blends": [{"blend": b, "count": n} for b, n in top_blends],
        "persona_lines": [
            "Your usual emotional range, learned from your own messages: " + ", ".join(usable)
            + ". Lean toward these when the palette allows several choices.",
            "Blends you often feel: " + "; ".join(b for b, _ in top_blends[:5]) + "." if top_blends else "",
        ],
        "frequent_but_avoid": held_back,
        "frequent_but_avoid_note": "You often show these, but the emotion layer keeps them in 'notice, never act from'. "
        "Decide whether your twin should show them more; if so, move them to 'allow' in the layer and the bank.",
    }
    prof_path = src.with_name(src.stem + ".profile.json")
    prof_path.write_text(json.dumps(profile, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nLabeled {total}, failed {failed}.")
    for e, n in top[:10]:
        print(f"  {e:<16}{n / total:6.1%}  {BY_NAME[e]['fa']}  [{BY_NAME[e]['policy']}]")
    if top_blends:
        print("\nMost frequent blends:")
        for b, n in top_blends[:5]:
            print(f"  {b}  ({n})")
    print(f"\nLabels:  {out_path}\nProfile: {prof_path}")


if __name__ == "__main__":
    main()
