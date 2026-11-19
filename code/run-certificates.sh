#!/bin/sh
# Build the matrix, check it independently, and record its hash.
# Writes outputs to the directory given as $1.
# Environment: PY (Python 3 with numpy), CC (C compiler).
# A few seconds on one core.
set -eu
out=${1:?output directory}
PY=${PY:-python3}
CC=${CC:-cc}
mkdir -p "$out/bin"
if command -v shasum >/dev/null 2>&1; then sha256() { shasum -a 256; }; else sha256() { sha256sum; }; fi

# 1. Build H from the published inputs and check every step, including the
#    full product H H^T = 4356 I.
VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  "$PY" code/build4356.py data/srg65-gritsenko.txt "$out/H4356.txt" > "$out/build.txt"

# 2. Independent check of the written matrix (no shared code).
"$CC" -O2 -o "$out/bin/check4356" code/check4356.c
"$out/bin/check4356" "$out/H4356.txt" > "$out/check.txt"

# 3. Fingerprint of the matrix (4356 lines of '+' and '-').
printf '%s  H4356.txt\n' "$(sha256 < "$out/H4356.txt" | cut -d' ' -f1)" > "$out/matrix-sha256.txt"
