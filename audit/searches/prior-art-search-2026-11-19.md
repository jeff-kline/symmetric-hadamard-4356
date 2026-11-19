# Prior-art search, 2026-11-19

Each search is logged with its date and query. A failed or rate-limited
search is recorded as NOT PERFORMED, not as a negative result.

## GitHub (2026-11-19T20:16Z, `gh` CLI, authenticated)

- **Positive control:** `gh search code skew hadamard 1528` returned
  `vatskishan03/Hadamard`. Code search was working.
- `gh search code 4356 symmetric hadamard`, `gh search code 1089 symmetric hadamard`,
  `gh search code symmetric conference 66 hadamard`: no hits.
- `gh search repos symmetric hadamard`: no results returned.
- `vatskishan03/Hadamard` (latest commit 2026-11-06):
  - `symmetric/README.md` has no entry for 1089 or 4356, and decides 529 (order 2116) by Miyamoto's lemma in the propus array;
  - the tree has `skew/4356` only.

## Zenodo (2026-11-19, public records API)

- `"symmetric Hadamard"`: 6 records. None concerns order 4356; one is a
  classification dataset for orders up to 32.

## arXiv (2026-11-19, export API, newest first)

- `all:"symmetric Hadamard"`, 12 newest: nothing at order 4356.
  - Đoković, arXiv:2508.17141 (orders $q(q+1)$, $q\equiv3\pmod8$, giving $v=189$, 473 and 1139).
  - Đoković, arXiv:2101.05429 and arXiv:2301.02751.
  - A classification up to order 32, arXiv:2608.06920.

## Citing works (2026-11-19, OpenAlex API, no key or email)

- Works citing Gritsenko, arXiv:2102.05432 (OpenAlex W3128936781): 14
  listed; titles screened. Two were read in the relevant parts:
  - Egan, Kotsireas, London and Ó Catháin, *Recent progress in the
    construction of Hadamard matrices*, arXiv:2610.27175v2: no mention of 4356
    or 1089.
  - Goryainov, Haemers, Konstantinova and Li, arXiv:2512.16653 (December
    2025), §2:
    - lists the Wallis–Whiteman construction (item 4 of ten direct
      constructions of RSHCDs);
    - separately notes that Gritsenko's graph gives a symmetric conference
      matrix of order 66;
    - does not draw the consequence for order 4356 (no occurrence of 4356,
      1089 or 66²). **Closest prior art; credited in the note.**

## Sources read in the relevant parts

- Đoković and Seberry, census PDF dated 2025-05-28:
  - the symmetric series list (pp. 2–4);
  - the 595 undecided values (p. 5), which include 529 and 1089;
  - 169, 225, 441 and 1681 are in the Paley series.
- Wallis and Whiteman (1972): Lemma 15, Theorem 16 and Corollary 17 (pp. 246–248, page images).
- Gritsenko (2021): the construction and the printed adjacency matrix.
- Brouwer and Haemers, *Spectra of Graphs*, §10.5.1.
- Mathon (1978): Crossref metadata (DOI 10.4153/CJM-1978-029-1).

## Pre-tag rescan (2026-11-19T20:39Z)

- GitHub code search: the positive control (`skew hadamard 1528`) hit
  `vatskishan03/Hadamard`. `4356 symmetric hadamard` and `1089 symmetric`
  returned only unrelated hits (language-model logs).
- `vatskishan03/Hadamard`: no symmetric entry at 1089 or 4356; latest commit
  2026-11-06.
- arXiv, newest entries matching "symmetric Hadamard": nothing new.
