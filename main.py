"""The Robot Apology -- make.fun entry.

Writes a two-line robot apology to /output/entry.txt:

- Line 1: one sentence, the robot apologising for one specific,
  concrete, human-scale mistake (a cold morning shower).
- Line 2: one sentence, what it learned and what it will do
  differently -- a changed behaviour that follows from that
  exact mistake, not a generic promise to do better.

Standard library only (os, sys).
"""

import os
import sys

ENTRY = (
    "I am sorry I set your morning shower to cold and left you shivering "
    "under water that felt piped in from a glacier.\n"
    "I have learned to check the temperature dial twice before anyone steps "
    "in, and from now on I will run a short warm-up test so the first splash "
    "is never a shock again."
)

OUTPUT_FILENAME = "entry.txt"


def _check_entry(text):
    """Guard the gate: 1-400 chars, exactly 2 lines, one sentence each."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert not text.endswith("\n"), "no trailing newline at end of file"
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly 2 lines"
    for line in lines:
        assert line.strip(), "each line must not be blank"
        assert line.count(".") == 1, "each line must be exactly one sentence"
        assert "!" not in line and "?" not in line, "no other sentence enders"
        assert line.endswith("."), "each line must end with a period"


def main():
    _check_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and prove the file on disk is byte-identical to ENTRY.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch: file is not byte-identical"
    assert back.decode("utf-8") == ENTRY, "read-back text differs"
    print("wrote {} ({} characters, 2 lines)".format(path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
