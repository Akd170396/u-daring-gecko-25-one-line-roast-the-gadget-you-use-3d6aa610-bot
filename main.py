"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<= 200 characters) to /output/entry.txt.
The line targets a gadget used every day -- the phone's autocorrect -- with a
concrete, specific detail: it gets the owner's own name wrong in their own
contacts. Deterministic: same bytes on every run, no network, stdlib only.
"""

import os

LINE = (
    "My phone autocorrects my own name in my own contacts, "
    "like it met me once and decided not to bother remembering."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text, "must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
