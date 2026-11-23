import os
from pathlib import Path

ENTRY_LINE = "I told my doctor I don't have time to be sick; she said, 'That's the sickness.'"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
