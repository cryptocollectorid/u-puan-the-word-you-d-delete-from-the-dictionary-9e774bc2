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


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
