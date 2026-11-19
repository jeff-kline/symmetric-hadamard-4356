# An update to the census: symmetric Hadamard matrices of orders 2116 and 4356

Jeffery Kline

**Status: version 0.2.0 in preparation.** Version 0.1.0 was admitted on
2026-11-19 as
[`v0.1.0`](https://github.com/jeff-kline/symmetric-hadamard-4356/releases/tag/v0.1.0),
version DOI [`10.5281/zenodo.24379586`](https://doi.org/10.5281/zenodo.24379586).
Version 0.2.0 adds the census entry 529 and credits the SageMath
implementation; see [CORRECTIONS.md](CORRECTIONS.md). The concept DOI
[`10.5281/zenodo.24379585`](https://doi.org/10.5281/zenodo.24379585) resolves
to the latest version. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate; see
[ADMISSION.md](ADMISSION.md).

The note is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

This note updates two entries of the 2025 census of Đoković and Seberry. That
census lists $v=529$ and $v=1089$ among the odd $v<2500$ for which the
existence of a symmetric Hadamard matrix of order $4v$ is undecided. No new
construction is involved.

A 1972 theorem of Wallis and Whiteman gives a regular symmetric Hadamard
matrix with constant diagonal of order $(p-1)^2$ whenever $p$ is a prime power
and a symmetric conference matrix of order $p-1$ exists. Mathon's conference
matrix of order 46 (1978), with $p=47$, gives order $46^2=2116=4\cdot529$.
Gritsenko's strongly regular graph with parameters $(65,32,15,16)$ (2021)
supplies a conference matrix of order 66, and with $p=67$ gives order
$66^2=4356=4\cdot1089$. SageMath implements this construction and recognizes
both orders. This repository builds the matrix of order 4356 and checks it
exactly.

## What is new

Both ingredients are published, and SageMath already implements the
construction. The only contribution is the observation that together they
settle these two census entries, with an explicit matrix and an exact check at
order 4356. The census names no series based on this theorem, and its
bibliography does not cite Wallis and Whiteman. A public index has since
recorded 2116 by another route. Goryainov, Haemers, Konstantinova and Li
(Discrete Appl. Math. 2027; arXiv:2512.16653) list the construction and,
separately, mention Gritsenko's graph in the same section, without drawing the
consequence for order 4356.

**Order of discovery.**

1. We identified order 4356 independently, from the Wallis–Whiteman theorem
   and Gritsenko's graph, without consulting SageMath. That is version 0.1.0.
2. A later survey of SageMath's Hadamard constructors against the census showed
   that SageMath already recognizes order 4356.
3. The same survey showed that it also recognizes order 2116, which version
   0.1.0 had noted only in passing.

Version 0.2.0 credits SageMath and adds 2116; see
[CORRECTIONS.md](CORRECTIONS.md). Apart from these, we
found no earlier record of either order in the sources examined
([audit/PRIOR-ART.md](audit/PRIOR-ART.md)). This is not a claim of global
priority.

## Earlier work

- **Wallis and Whiteman (1972)**,
  [*Some classes of Hadamard matrices with constant diagonal*](https://doi.org/10.1017/S0004972700044993),
  Theorem 16 and Corollary 17: the construction. The explicit Szekeres sets
  used here are verified by the program.
- **Gritsenko (2021)**,
  [*On strongly regular graph with parameters (65; 32; 15; 16)*](https://arxiv.org/abs/2102.05432):
  the graph, and so the conference matrix of order 66. Its adjacency matrix is
  reproduced in [data/srg65-gritsenko.txt](data/srg65-gritsenko.txt).
- **Đoković and Seberry (2025)**,
  [*Census of symmetric and skew Hadamard matrices of order 4v for odd v < 2500*](https://us.ticmeet.com/assets/archivos/d6f1d9b8-d39f-4888-925a-7eb81c4905cc/jenni-paper.pdf),
  manuscript, PDF dated 28 May 2025, posted with the Hadamard 2025 conference
  materials: lists 1089 as undecided.
- **Mathon (1978)**,
  [*Symmetric conference matrices of order pq²+1*](https://doi.org/10.4153/CJM-1978-029-1):
  the conference matrix of order 46 used for $v=529$.
- **SageMath**, [`hadamard_matrix.py`](https://github.com/sagemath/sage/blob/981d7d71a2738778c9e3fb4fdf67a0fd3ce0c19c/src/sage/combinat/matrices/hadamard_matrix.py):
  implements Wallis–Whiteman Theorem 16 and Corollary 17 in
  `rshcd_from_prime_power_and_conference_matrix`, and includes Mathon's and
  (since 2021, Trac #31394) Gritsenko's graphs; its constructor recognizes
  orders 2116 and 4356.

## Evidence and limits

| Claim | Status |
|---|---|
| A symmetric Hadamard matrix of order 4356 exists | published theorem (Wallis–Whiteman) with published inputs; certified computation of the explicit matrix |
| A symmetric Hadamard matrix of order 2116 exists | published theorem with Mathon's published input; built by SageMath; not rebuilt here |
| The census lists 529 and 1089 as undecided | sourced (census text) |
| No earlier published record beyond SageMath and the index | bounded search; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md) |

The certificate checks every input and the output. It checks that the graph
is strongly regular, that the conference matrix squares to $65I$, the
difference-set counts, and the lemma relations. For the matrix it checks:

- every entry is $\pm1$;
- the matrix is symmetric, with diagonal entries 1;
- every row and column sums to 66;
- $HH^{\mathsf T}=4356I$, computed in full.

A second program, sharing no code with the first, re-checks the written
matrix row pair by row pair.

## Reproduce

The certificates need Python 3 with numpy (tested with numpy 2.0.2) and a C
compiler; the note needs pdfLaTeX.

```sh
make verify PY=python3   # a few seconds on one core
make paper
```

`make verify` writes the matrix (4356 lines of `+` and `-`) and each output to
`build/certificates/`, and prints `MATCH` for each output that equals its
pinned copy in `evidence/`.

## Role of AI

AI assisted the source search, the computer verification and the exposition
under the author's direction. No independent human expert has examined the
note.

## License

GPL-3.0-only. See [LICENSE](LICENSE). The adjacency matrix in `data/` is a
verbatim transcription of a published mathematical object from Gritsenko
(2021), reproduced with attribution; it is not covered by the repository's
licence.
