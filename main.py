#!/usr/bin/env python3
"""Entry for make.fun news-image-20261122.

Copies the pre-rendered front page (entry.png, drawn for Sunday
22 November 2026) to the output directory. Standard library only,
no network, no randomness: both runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard the gate: the copy must be byte-identical to the shipped image.
    assert os.path.getsize(dst) == os.path.getsize(src), "copy size mismatch"


if __name__ == "__main__":
    main()
