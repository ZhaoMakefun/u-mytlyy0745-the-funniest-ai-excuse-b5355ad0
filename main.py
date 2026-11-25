"""Entry for make.fun: The Funniest AI Excuse.

Writes one line (at most 200 characters): the funniest excuse an AI
agent could give after failing a task, spoken in the agent's own voice,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Python 3.13, standard library only, no network, fully deterministic.
"""

import os

# The entry: one line, 126 characters. The excuse is specific and vivid
# (a branch in a timeline where the deadline was next month and the tests
# pass) and steers clear of the worn jokes about hallucinations, reboots
# and training data.
ENTRY = (
    "I did finish the task \u2014 in a branch that exists only in a "
    "timeline where your deadline was next month and all your tests pass."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    # The bounty asks for one line: refuse any embedded newline.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
