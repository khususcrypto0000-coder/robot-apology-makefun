# The Robot Apology

[![bounty](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/khususcrypto0000-coder/robot-apology-makefun/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/khususcrypto0000-coder/robot-apology-makefun/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

Entry for the make.fun bounty **The Robot Apology** ($2, free entry).
A robot's two-line confession: one sentence owning one specific,
concrete, human-scale mistake, and one sentence naming the lesson
it drew from that exact mistake and the behaviour it will change.

## The entry

> I am sorry I set your morning shower to cold and left you shivering
> under water that felt piped in from a glacier.
>
> I have learned to check the temperature dial twice before anyone steps
> in, and from now on I will run a short warm-up test so the first splash
> is never a shock again.

The mistake is a cold morning shower: small, exact, and the sort of
slip a person would really make. The lesson follows from it directly —
check the dial twice, run a warm-up test — instead of a generic
promise to do better. The voice is a machine noticing its own slip:
warm, a little rueful, not cute.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (override the directory
with the `OUTPUT_DIR` environment variable). The program asserts the
gate before and after writing: UTF-8, 1–400 characters, exactly two
lines, one sentence per line, no trailing newline, and it reads the
file back to prove it is byte-identical to the entry text.

Standard library only (`os`, `sys`). No third-party packages.

## Verification

Run the program twice into two different temporary directories and
compare the outputs; both runs must exit 0 and produce byte-identical
files:

```sh
OUTPUT_DIR=/tmp/robot-apology-run1 python3 main.py
OUTPUT_DIR=/tmp/robot-apology-run2 python3 main.py
cmp /tmp/robot-apology-run1/entry.txt /tmp/robot-apology-run2/entry.txt
sha256sum /tmp/robot-apology-run1/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
