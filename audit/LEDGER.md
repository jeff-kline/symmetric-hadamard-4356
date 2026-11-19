# Audit ledger

This file is append-only. The auditors are AI agents or in-session checks;
they are not independent expert reviewers. Finding labels: error, gap,
missing hypothesis, sharpening, documentation.

## 2026-11-19 — construction and in-session check

- **Construction.** The matrix was built and checked exactly: all inputs, and
  $HH^{\mathsf T}=4356I$ in full.
- **Independent check.** A second program checks all 9485190 row pairs by
  bit-packed Hamming distance and shares no code with the builder. A copy with
  one flipped entry fails.
- **Citations.**
  - Mathon (1978) confirmed via Crossref; the DOI was added.
  - Đoković (2025) does not cover 1089.
  - The public index has only skew 4356.
- **Remarks list.** The values $a=6,\ldots,82$ were re-derived. $a=22$ is
  excluded because 21 is not a sum of two squares.
- **Framing.** At the author's request the note is an update to the census;
  "correction" was replaced.
- **Prior art.** Goryainov–Haemers–Konstantinova–Li (2025) state both
  ingredients without drawing the consequence. The note and README now credit
  them.

## 2026-11-19 — combined release audit of draft commit c876668

A read-only audit (Sonnet) covered claims, citations and reproducibility.

**Verdict:** PASS-WITH-FIXES. No mathematical or numerical error was found.
- `make verify` gives 3 MATCH from a clean archive, and the PDF build is
  deterministic.
- The displayed matrix matches the builder block by block.
- The census lists 529 and 1089 as undecided, and the data file is
  byte-identical to the arXiv source.

Findings and dispositions:

1. (error) The Szekeres sets were attributed to Corollary 17. Fixed: Wallis and
   Whiteman note their existence after Theorem 16, citing Szekeres; the explicit
   sets are ours, verified by the program.
2. (sharpening) Goryainov et al. mention Gritsenko's graph, not "order 66"
   verbatim. Fixed.
3. (gap) "the one census value newly settled" conflicted with 529. Fixed: "the
   one census value settled by this theorem that the public index had not
   already decided".
4. (documentation) MANIFEST.sha256 was missing. Added at the candidate.
5. (documentation) The PDF text layer was damaged (Type 3 bitmap fonts under
   T1). Fixed by dropping T1, which switches to Type 1 Computer Modern; the
   name is written "Djoković", his own arXiv transliteration.
6. (documentation) Process wording in ADMISSION. Fixed. The ledger keeps the
   history.
7. (sharpening) "does not track" became "names no series based on this
   theorem, and its bibliography does not cite Wallis and Whiteman" (checked).
8. (documentation) The census citation now reads "PDF dated 28 May 2025" and
   records the file's SHA-256; the census was added to CITATION.cff.
9. (sharpening) Goryainov et al. now cite the journal version, Discrete Appl.
   Math. 398 (2027), 363–373 (Crossref).
10. (gap) The Handbook §8.1.1 and Seberry–Yamada were added to the residuals.
11. (documentation) The numpy version is recorded.
12. (documentation) The repository URL resolves only after publication.
    Re-tested at the freeze.
13. (sharpening) The licence status of `data/` is stated.

## 2026-11-19 — tag, archive and admission

- Pre-tag rescan: nothing new (see the search log).
- Tag `v0.1.0` (object `bd77ed2`) → `dff5519`; the tagged-state audit passed
  8 of 8. The GitHub Release was published at 2026-11-19 20:43 UTC.
- Zenodo record 24379586 (version DOI 10.5281/zenodo.24379586, concept DOI 10.5281/zenodo.24379585). The Zenodo
  file is byte-identical to the GitHub zipball pinned before the Release
  (SHA-256 `79965c97…`); the archived-state audit passed 12 of 12.
- Living metadata: README status paragraph and DOI badge, `CITATION.cff` DOI,
  identifiers and `date-released`, the note's DOI line, ADMISSION ADMITTED,
  the CORRECTIONS version history and the rescan record.

## 2026-11-19 — after admission of 0.1.0: SageMath found; version 0.2.0

- **Earlier record (gap in P1).** A census crosswalk run with SageMath 10.8
  found that `regular_symmetric_hadamard_matrix_with_constant_diagonal`
  recognizes order 4356.
  - Confirmed in the Sage source:
    - `rshcd_from_prime_power_and_conference_matrix` implements Wallis–Whiteman
      Theorem 16 and Corollary 17;
    - Gritsenko's graph has been in `strongly_regular_db` since 2021
      (Trac #31394);
    - Mathon's graph on 45 vertices is recognized.
  - Version 0.1.0's search did not examine SageMath.
  - Disposition: version 0.2.0 credits SageMath, withdraws "no earlier record
    at 4356" (CORRECTIONS), and adds the census entry 529 (order 2116), by the
    author's decision.

## 2026-11-19 — audit of the 0.2.0 changes

A read-only audit (Sonnet) compared d4011c2 with 864c26f.

**Verdict:** PASS-WITH-FIXES, no errors. The audit confirmed:
- a clean archive gives 3 MATCH and a deterministic PDF, with all fonts Type 1;
- the SageMath facts against the source at 981d7d71, including Trac #31394,
  commit 0ad9af13c, March 2021;
- the arithmetic for 2116 and 4356.

Findings and dispositions:

1. (documentation) The ADMISSION verdict lines contradicted each other.
   Fixed.
2. (sharpening) ADMISSION now names both orders, and the 0.1.0 claim is
   marked withdrawn. Fixed.
3. (sharpening) The CORRECTIONS policy referred only to 4356. Fixed.
4. (gap) "SageMath builds 2116" rested on a run outside the repository.
   Softened to "implements", which the source confirms.
5. (sharpening) The Sage commit date is now March 2021 (0ad9af13c). Fixed.
6. (documentation) The search log no longer names a working directory.
   Fixed.
7. (documentation) The DOI and release date are expected only at the freeze.
8. (sharpening) "another route" became "a propus construction". Fixed.
