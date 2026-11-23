import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/tmp/laughout")
ENTRY_PATH = OUTPUT_DIR / "entry.txt"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.unlink(missing_ok=True)

    env = os.environ.copy()
    env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)
    subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )

    raw = ENTRY_PATH.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AssertionError("entry is not UTF-8") from exc

    lines = text.splitlines()
    assert len(lines) == 1, f"expected exactly one line, got {len(lines)}"
    assert 1 <= len(text) <= 200, f"entry length out of range: {len(text)}"
    assert text.strip(), "entry is empty"
    print("PASS")


if __name__ == "__main__":
    main()
