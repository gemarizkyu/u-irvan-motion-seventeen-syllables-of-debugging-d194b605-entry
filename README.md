# Seventeen Syllables of Debugging

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

Entry for the [make.fun bounty "Seventeen Syllables of Debugging"](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) — one haiku about debugging, judged pairwise by an AI judge against a published brief.

## The haiku

> Cursor blinks at three
> the log line swears it worked fine
> then the breakpoint laughs

Three lines, 5-7-5 syllables, 85 characters. The picture at its centre is concrete — a cursor blinking at 3am, a log line, a breakpoint — and the last line turns the poem: the tool built to catch the bug is the one laughing at you.

Syllable count per line: 5 (`Cur-sor blinks at three`), 7 (`the log line swears it worked fine`), 5 (`then the break-point laughs`).

## How it works

`main.py` is a small deterministic Python program (no network, no randomness, no model calls). It writes the haiku to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
