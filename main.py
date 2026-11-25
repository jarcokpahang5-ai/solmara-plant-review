"""One Star, Written in Sap -- make.fun entry.

A houseplant leaves a one-star review of its human owner. The plant
was repotted into a mug with no drainage, rebranded as minimalist
living, and is now slowly drowning while its owner acts surprised.
The program checks the review against the bounty gate, prints it,
and writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 One star: he repotted me into a mug with no "
    "drainage, called it 'minimalist living', and now acts surprised "
    "every time I drown a little more."
)

MIN_CHARS = 1
MAX_CHARS = 279
TARGET = "/output/entry.txt"


def validate(text):
    """Check the review against the bounty gate before it is used."""
    if not isinstance(text, str):
        raise ValueError("review must be text")
    if not text.strip():
        raise ValueError("review must not be blank")
    if text != text.strip():
        raise ValueError("review must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "review is %d characters, outside the %d-%d range"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    lowered = text.lower()
    if "one star" not in lowered:
        raise ValueError("review must state its one-star rating")
    if "repotted" not in lowered and "water" not in lowered:
        raise ValueError("review must name a plant-care grievance")
    return text


def main():
    """Validate the review, print it, and store it for judging."""
    review = validate(REVIEW)
    print(review)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(review)


if __name__ == "__main__":
    main()
