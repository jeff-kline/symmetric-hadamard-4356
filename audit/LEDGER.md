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
