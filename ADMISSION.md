# Admission record

**Current state:** CANDIDATE

Current verdict: NOT YET ADMITTED

**Version:** 0.1.0 (release candidate)

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** On 2026-11-19 the author made these choices:

- a short note, separate from the skew work;
- titled and described as an update to the census, not a new construction;
- the abstract and README introduction approved.

## Principal claim

A regular symmetric Hadamard matrix with constant diagonal of order
$4356=4\cdot1089$ exists, by Wallis–Whiteman (1972) applied to Gritsenko's
conference matrix of order 66. The Đoković–Seberry census of 2025 lists 1089
as undecided. We found no earlier record of the order in the sources examined.

## Gates

| Gate | Status | Evidence or residual |
|---|---|---|
| P1 prior work and credit | PARTIAL | `audit/PRIOR-ART.md` and the search log of 2026-11-19. Closest prior art: Goryainov–Haemers–Konstantinova–Li (2025) state both ingredients; credited. Residuals: most works citing Gritsenko screened by title only; the Handbook of Combinatorial Designs §8.1.1 and the Seberry–Yamada survey were not read |
| A1 claim and artifact consistency | PASS | A pre-audit check (citations, source claims, transcription, independent matrix check) and one combined release audit (claims, citations, reproducibility); findings and dispositions in `audit/LEDGER.md` |
| R1 release and stewardship | IN PROGRESS | `make verify` (3 MATCH) and a deterministic `make paper` pass, also from a clean `git archive`; correction policy, CITATION.cff and MANIFEST.sha256 present. No tag, archive or DOI yet |
