"""Write the 4AM Commit bounty entry to /output/entry.txt."""

import os

ENTRY = "fix: this commit message is the bug now \u2014 I wrote it at 4am to explain the fix I wrote at 3am for the code I wrote at 2am"

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
# The joke: the commit message itself has become the bug. The agent spent
# the night fixing its own code, then its own fix, and now at 4am it is
# writing a commit message about writing a commit message about all of it.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
