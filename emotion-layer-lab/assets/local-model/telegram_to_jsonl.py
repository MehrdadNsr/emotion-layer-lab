#!/usr/bin/env python3
"""Turn a Telegram Desktop JSON export into a JSONL file of YOUR messages, ready for label_chats.py.

Each output line: {"chat": "...", "date": "...", "text": "<your message>", "prev": "<the other person's message before it>"}

Usage:
  python3 telegram_to_jsonl.py result.json --me "YourName" > my_messages.jsonl
  (--me matches your display name or your from_id, e.g. user123456)

Works with both a full-account export (chats.list) and a single-chat export.
Everything stays on your machine.
"""
import argparse
import json
import sys


def flatten(text):
    """Telegram stores text as a string or as a list of strings and {type, text} parts."""
    if isinstance(text, str):
        return text
    parts = []
    for p in text or []:
        parts.append(p if isinstance(p, str) else p.get("text", ""))
    return "".join(parts)


def chats_of(data):
    if "chats" in data and isinstance(data["chats"], dict):
        return data["chats"].get("list", [])
    if "messages" in data:
        return [data]
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export", help="Telegram export file (result.json)")
    ap.add_argument("--me", required=True, help="your display name or from_id")
    ap.add_argument("--min-chars", type=int, default=3, help="skip messages shorter than this")
    args = ap.parse_args()

    with open(args.export, encoding="utf-8") as f:
        data = json.load(f)

    count = 0
    for chat in chats_of(data):
        prev_other = ""
        for m in chat.get("messages", []):
            if m.get("type") != "message":
                continue
            text = flatten(m.get("text", "")).strip()
            if not text:
                continue
            mine = args.me in (m.get("from"), m.get("from_id"))
            if mine:
                if len(text) >= args.min_chars:
                    out = {"chat": chat.get("name", ""), "date": m.get("date", ""), "text": text, "prev": prev_other}
                    sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
                    count += 1
            else:
                prev_other = text
    print(f"{count} messages written", file=sys.stderr)


if __name__ == "__main__":
    main()
