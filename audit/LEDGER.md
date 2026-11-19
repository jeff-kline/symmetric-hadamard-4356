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
