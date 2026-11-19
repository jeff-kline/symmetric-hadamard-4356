# Verification record

## Environment of the pinned run (2026-11-19)

- macOS 26.6.2, x86_64, one core, run under `nice`.
- Python 3 with numpy (the project venv), one BLAS thread.
- Apple clang 21.0.0, used as `cc -O2`.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2021).

The programs need no network. Their SHA-256 hashes are in
[MANIFEST.sha256](MANIFEST.sha256).

## Commands

```sh
make verify PY=python3 CC=cc
make paper
```

`make verify` runs [code/run-certificates.sh](code/run-certificates.sh). It
writes the matrix and three outputs to `build/certificates/`, and compares each
output byte for byte with its pinned copy in [evidence/](evidence/). The total
running time is a few seconds.

## What each certificate checks

| Step | Program | Pinned output |
|---|---|---|
| The construction. The program checks:<ul><li>the adjacency matrix in `data/` is an SRG(65,32,15,16);</li><li>the bordered Seidel matrix $C$ of order 66 satisfies $C^2=65I$;</li><li>$X$ and $Y$ are Szekeres difference sets of size 16 in $\mathbb Z_{33}$;</li><li>the Wallis–Whiteman lemma relations for $A$ and $B$ hold.</li></ul>It then assembles $H$ and checks entries $\pm1$, symmetry, diagonal $1$, row and column sums $66$, and $HH^{\mathsf T}=4356I$ in full. | `build4356.py` | `build.txt` |
| An independent check of the written matrix, sharing no code with the builder. It checks symmetry, diagonal, row and column sums, and every one of the 9485190 row pairs for orthogonality (bit-packed Hamming distance). A corrupted copy fails. | `check4356.c` | `check.txt` |
| SHA-256 of the matrix (4356 lines of `+` and `-`). | `run-certificates.sh` | `matrix-sha256.txt` |

## Paper build

`make paper` runs pdfLaTeX three times with a fixed `SOURCE_DATE_EPOCH` and
fails on any warning, overfull box or undefined reference.
