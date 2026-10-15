"""Verify archived demo inputs/outputs locally. Does not call an AI service."""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / "manifest.json").read_text())
run = json.loads((ROOT / "run.json").read_text())

for group, prefix in [("prompt_sha256", ""), ("input_sha256", "inputs/"),
                      ("output_sha256", "outputs/")]:
    if not manifest.get(group):
        raise ValueError(f"Missing hash group: {group}")
    for name, expected in manifest[group].items():
        actual = hashlib.sha256((ROOT / (prefix + name)).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"Hash mismatch: {prefix}{name}")

task = (ROOT / "task.txt").read_text()
context = (ROOT / "context-prompt.txt").read_text()
if (ROOT / "baseline-prompt.txt").read_text() != task:
    raise ValueError("Baseline task differs from saved task")
if not context.endswith("<task>\n" + task + "</task>\n"):
    raise ValueError("Context condition does not end with the identical task")
for name in manifest["input_sha256"]:
    expected = f'<file path="{name}">\n' + (ROOT / "inputs" / name).read_text() + "\n</file>"
    if expected not in context:
        raise ValueError(f"Context does not contain the verbatim input: {name}")

print("All archived hashes match. Both conditions use the same task.")
for condition in ["baseline", "context"]:
    if run[condition]["generations"] != 1 or run[condition]["retries"] != 0:
        raise ValueError(f"Run metadata differs from the recorded protocol: {condition}")
    text = (ROOT / "outputs" / f"{condition}.md").read_text()
    # Report the protocol's whitespace count and a prose count without list markers.
    plain = re.sub(r"(?m)^\s*(?:[*+-]|\d+[.)])\s+", "", text)
    print(f"{condition}: {len(text.split())} whitespace tokens, "
          f"{len(plain.split())} words excluding list markers, "
          f"{text.count('!')} exclamation points")
