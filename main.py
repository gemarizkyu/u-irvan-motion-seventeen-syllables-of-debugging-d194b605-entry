#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- make.fun bounty entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
at most 200 characters) to /output/entry.txt.

Deterministic by design: no network, no randomness, no clock, no
model calls. The same text is produced on every run.
"""

from pathlib import Path

# The haiku. Syllables, line by line:
#   "Cursor blinks at three"               -> Cur-sor(2) blinks(1) at(1) three(1) = 5
#   "the log line swears it worked fine"   -> the(1) log(1) line(1) swears(1)
#                                              it(1) worked(1) fine(1) = 7
#   "then the breakpoint laughs"           -> then(1) the(1) break-point(2) laughs(1) = 5
# Concrete centre (cursor at 3am, a log line, a breakpoint) and the
# turn lands in the last line: the tool built to catch the bug is the
# one laughing at you.
HAIKU = (
    "Cursor blinks at three\n"
    "the log line swears it worked fine\n"
    "then the breakpoint laughs\n"
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
