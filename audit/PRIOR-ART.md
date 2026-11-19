# Prior art and credit

This is a bounded comparison. It is not a claim of global novelty. The searches
are logged in
[searches/prior-art-search-2026-11-19.md](searches/prior-art-search-2026-11-19.md).

**Claim (version 0.2.0):** the census entries 529 and 1089 are settled by the
Wallis–Whiteman theorem with published conference matrices. SageMath already
implements that construction and recognizes both orders, and a public index
records 2116 by another route. Apart from these, we found no earlier record of
either order in the sources examined. Version 0.1.0 claimed no earlier record
at 4356 and did not examine SageMath; see `CORRECTIONS.md`.

| Source | What it records | Bearing |
|---|---|---|
| Đoković–Seberry census (2025-05-28) | 1089 among 595 undecided values; its named series do not include the Wallis–Whiteman construction | the entry updated here |
| Wallis–Whiteman (1972), Theorem 16, Corollary 17 | regular symmetric Hadamard matrix with constant diagonal of order $(p-1)^2$, from a symmetric conference matrix of order $p-1$, $p$ a prime power | the construction |
| Gritsenko (2021) | SRG(65,32,15,16), hence a symmetric conference matrix of order 66 | the input |
| Mathon (1978) | symmetric conference matrix of order 46 | the input for 2116 |
| SageMath 10.8, `hadamard_matrix.py` and `strongly_regular_db.pyx` | `rshcd_from_prime_power_and_conference_matrix` implements Wallis–Whiteman Theorem 16 and Corollary 17; Mathon's graph on 45 vertices and Gritsenko's graph (added 2021, Trac #31394) are in the database; `regular_symmetric_hadamard_matrix_with_constant_diagonal` recognizes 2116 and 4356 | **earlier computational record at both orders; credited** |
| Goryainov–Haemers–Konstantinova–Li (Discrete Appl. Math. 2027; arXiv:2512.16653), §2 | lists the Wallis–Whiteman construction among known constructions and, separately, mentions Gritsenko's graph on 65 vertices (which gives a conference matrix of order 66 by the bordering they recall) | closest prior art: both ingredients side by side, consequence not drawn |
| Egan–Kotsireas–London–Ó Catháin (2026) | cites Gritsenko; no mention of 4356 or 1089 | consistent |
| Đoković (2025), arXiv:2508.17141 | symmetric orders $q(q+1)$, $q\equiv3\pmod8$ | 1089 is not of this form |
| `vatskishan03/Hadamard` (2026-11-06) | skew 4356 only; symmetric 2116 (v = 529) by a propus construction | records 2116; credited |

## Credit

- Wallis and Whiteman: the construction.
- Gritsenko: the strongly regular graph.
- Mathon: the conference matrix of order 46 (for $v=529$).
- The SageMath developers: the implementation that already constructs both orders.
- Goryainov, Haemers, Konstantinova and Li: stated both ingredients in 2025.

## Residuals

- The census is a conference manuscript; whether a later published version
  differs was not checked.
- Of the 14 works citing Gritsenko, four were searched in full text for 4356
  and 1089 (arXiv 2512.16653, 2610.27175, 2608.23691, 2610.08893); the others
  were screened by title. The journal version of 2512.16653 was not compared
  with arXiv v1.
- The Handbook of Combinatorial Designs §8.1.1 (the source of the list in
  2512.16653) and the Seberry–Yamada survey were not read.
- The census PDF (SHA-256 4b61953c0754f7e2da48a136ee8d3db4512c9dfbd96a76abebf2689194d0f04a) carries no venue or
  date in its text; the date is its PDF metadata.
- `gh search repos symmetric hadamard` returned no results; this may be a
  search artifact. The repository was checked directly.
- Unpublished or unindexed observations cannot be excluded.
