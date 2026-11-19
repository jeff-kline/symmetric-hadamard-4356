# An update to the census: symmetric Hadamard matrices of order 4356

Jeffery Kline

**Status: release candidate for version 0.1.0.** The claims are frozen
and audited (see [ADMISSION.md](ADMISSION.md)). There is no tag, archive or
DOI yet, so there is no stable citation. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate.

The note is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

This note updates one entry of the 2025 census of Đoković and Seberry. That
census lists $v=1089$ among the odd $v<2500$ for which the existence of a
symmetric Hadamard matrix of order $4v$ is undecided. No new construction is
involved.

A 1972 theorem of Wallis and Whiteman gives a regular symmetric Hadamard
matrix with constant diagonal of order $(p-1)^2$ whenever $p$ is a prime power
and a symmetric conference matrix of order $p-1$ exists. In 2021 Gritsenko
constructed a strongly regular graph with parameters $(65,32,15,16)$, which
supplies a symmetric conference matrix of order 66. With $p=67$ the theorem
gives a symmetric Hadamard matrix of order $66^2=4356=4\cdot1089$, with
constant diagonal and every row and column sum equal to 66. This repository
builds that matrix and checks it exactly.

## What is new

Both ingredients are published. The only contribution is the observation
that together they settle this census entry, with an explicit matrix and an
exact check. The census names no series based on this theorem, and its
bibliography does not cite Wallis and Whiteman. The same theorem
also settles $v=529$, which the census lists as undecided; a public index has
since decided 529 by another route. Goryainov, Haemers, Konstantinova and Li
(Discrete Appl. Math. 2027; arXiv:2512.16653) list the construction and, separately,
mention Gritsenko's graph in the same section, without drawing the consequence
for order 4356. We found no earlier record of a symmetric
Hadamard matrix of order 4356 in the sources examined
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

## Evidence and limits

| Claim | Status |
|---|---|
| A symmetric Hadamard matrix of order 4356 exists | published theorem (Wallis–Whiteman) with published inputs; certified computation of the explicit matrix |
| The census lists 1089 as undecided | sourced (census text) |
| No earlier record at 4356 | bounded search; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md) |

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
