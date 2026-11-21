#!/usr/bin/env python3
"""News-image-20261121 entry (Python 3.13, standard library only).

The entry image is entry.png beside this file. The program copies it to
/output/entry.png, which is the single image the judge sees. The gate takes
a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the run
must be deterministic: the same bytes every time.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out)
