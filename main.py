"""Entrypoint: draw the front page and write entry.png to the output dir.

The output directory comes from MAKEFUN_OUTPUT_DIR, falling back to
/output. Runs offline, deterministically, standard library + Pillow only.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import render


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    render().save(path, format="PNG")
    size = os.path.getsize(path)
    if size <= 0 or size > 1048576:
        raise SystemExit("entry.png has an unexpected size: %d bytes" % size)
    print("wrote %s (%d bytes)" % (path, size))


if __name__ == "__main__":
    main()
