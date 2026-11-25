"""Entry for make.fun bounty "The Word You'd Delete From the Dictionary".

Writes the single word to /output/entry.txt.

The word: defenestration — the act of throwing someone out of a window.
It is a real word every reader recognises, it is funny at first sight because
of its absurd specificity, the humour comes from the word itself (its clunky
sound and the total gap it would leave — no other word names that exact act),
and it is not the first word the field would think of.
"""

import os

WORD = "defenestration"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 77


def validate_word(word):
    """Check the entry against the competition gate: one word, 1-77 chars."""
    if not word or not word.strip():
        raise ValueError("entry must not be blank")
    if len(word) != len(word.strip()) or any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise ValueError(f"entry must be {MIN_LEN}-{MAX_LEN} chars, got {len(word)}")
    if not word.isalpha():
        raise ValueError("entry must be a dictionary word: letters only")
    return word


def write_entry(word, path=OUTPUT_PATH):
    """Validate and write the word to the output path, returning the path."""
    checked = validate_word(word)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(checked)
    return path


def main():
    path = write_entry(WORD)
    print(f"Wrote {len(WORD)} chars to {path}")


if __name__ == "__main__":
    main()
