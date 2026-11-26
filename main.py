"""Funniest Sign on a Haunted Server Room Door.

Reads the one-line sign from entry.txt next to this file, validates it
against the competition gate (UTF-8 text, 1-120 characters, not only
whitespace), writes it to /output/entry.txt for the sealed scorer, and
prints it.
"""

from pathlib import Path

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def validate_sign(text: str) -> str:
    """Return the single-line sign, or exit if it breaks the gate."""
    line = text.strip()
    if not line:
        raise SystemExit("entry.txt is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def main() -> None:
    entry_path = Path(__file__).with_name("entry.txt")
    text = entry_path.read_text(encoding="utf-8")
    line = validate_sign(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
