#!/usr/bin/env python3
"""
example.py

A simple “random” Python script with a few functions:
  - A naive factorial function
  - A function that reads a text file and counts word frequencies
  - A small CLI entry point that ties them together
"""

import sys
import os
from collections import Counter
from typing import Dict


def factorial(n: int) -> int:
    """
    Compute factorial of n (n!), for n >= 0.
    This is a naive recursive implementation, just for demonstration.
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def count_word_frequencies(path: str) -> Dict[str, int]:
    """
    Read a text file at `path` and return a dict mapping each word
    to the number of times it appears (case-insensitive).
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No such file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Very basic splitting by whitespace/punctuation
    words = [w.strip(".,!?;:\"'()[]") for w in text.split()]
    words = [w.lower() for w in words if w]

    freqs = Counter(words)
    return dict(freqs)


def print_top_words(freqs: Dict[str, int], top_n: int = 10) -> None:
    """
    Print the top_n most common words from a frequency dict.
    """
    print(f"Top {top_n} words:")
    for word, count in Counter(freqs).most_common(top_n):
        print(f"  {word!r}: {count}")


def main():
    """
    If you run `python example.py [filename] [--factorial N]`,
    it will:
      1) If --factorial is provided, compute factorial(N) and print.
      2) If a filename is provided, count word frequencies in it.
    """
    # Basic CLI parsing:
    args = sys.argv[1:]
    if not args:
        print("Usage: python example.py <textfile> [--factorial N]")
        sys.exit(1)

    # Check for --factorial flag
    if "--factorial" in args:
        idx = args.index("--factorial")
        try:
            n_val = int(args[idx + 1])
        except (IndexError, ValueError):
            print("Error: --factorial must be followed by an integer")
            sys.exit(1)

        try:
            result = factorial(n_val)
        except Exception as e:
            print(f"Error computing factorial: {e}", file=sys.stderr)
            sys.exit(1)

        print(f"{n_val}! = {result}")
    else:
        n_val = None

    # If a text filename is provided, count words
    # We assume the first positional argument is the file path
    textfile = args[0]
    try:
        freqs = count_word_frequencies(textfile)
        print_top_words(freqs, top_n=5)
    except Exception as e:
        print(f"Error reading '{textfile}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
