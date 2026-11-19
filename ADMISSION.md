# Admission record

**Current state:** CANDIDATE (version 0.2.0); version 0.1.0 ADMITTED

Current verdict: NOT YET ADMITTED (version 0.2.0); version 0.1.0 ADMITTED 2026-11-19

**Version:** 0.1.0

**Tag:** `v0.1.0` → `dff5519416f001ec9006c60167e84a025b303a83`

**Version DOI:** [`10.5281/zenodo.24379586`](https://doi.org/10.5281/zenodo.24379586) · **Concept DOI:** `10.5281/zenodo.24379585` · **Record:** <https://zenodo.org/records/24379586>

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** On 2026-11-19 the author made these choices:

- a short note, separate from the skew work;
- titled and described as an update to the census, not a new construction;
- the abstract and README introduction approved.

## Version 0.2.0 (in preparation)

After admission of 0.1.0, a scan of SageMath found that it already implements
the construction and recognizes orders 2116 and 4356. Version 0.2.0 credits SageMath,
withdraws the 0.1.0 statement "no earlier record at 4356", and adds the census
entry 529 (order 2116), which follows from the same theorem. The author
approved this scope and its abstract and README introduction on 2026-11-19.
For 0.2.0: P1 PARTIAL (SageMath credited; residuals as in `audit/PRIOR-ART.md`);
A1 PASS (an audit of the 0.2.0 changes, findings and dispositions in
`audit/LEDGER.md`); R1 in progress (`make verify` 3 MATCH and a deterministic
`make paper` from a clean archive; no 0.2.0 tag or DOI yet). The gates below
describe 0.1.0.

## Principal claim (version 0.1.0; the no-earlier-record statement is withdrawn in 0.2.0, see CORRECTIONS.md)

A regular symmetric Hadamard matrix with constant diagonal of order
$4356=4\cdot1089$ exists, by Wallis–Whiteman (1972) applied to Gritsenko's
conference matrix of order 66. The Đoković–Seberry census of 2025 lists 1089
as undecided. We found no earlier record of the order in the sources examined.

## Gates

| Gate | Status | Evidence or residual |
|---|---|---|
| P1 prior work and credit | PARTIAL, residual accepted | `audit/PRIOR-ART.md` and the search log of 2026-11-19. Closest prior art: Goryainov–Haemers–Konstantinova–Li (2025) state both ingredients; credited. Residuals: most works citing Gritsenko screened by title only; the Handbook of Combinatorial Designs §8.1.1 and the Seberry–Yamada survey were not read. A rescan on 2026-11-19 at 20:39 UTC, before the tag, found nothing new. The author approved the freeze with these residuals stated |
| A1 claim and artifact consistency | PASS | A pre-audit check (citations, source claims, transcription, independent matrix check) and one combined release audit (claims, citations, reproducibility); findings and dispositions in `audit/LEDGER.md` |
| R1 release and stewardship | PASS | See below |

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS | fresh `git archive` extraction of the draft and of the candidate: `make verify` 3 MATCH; deterministic `make paper`, byte-identical to the committed PDF |
| Artifact integrity | PASS | `MANIFEST.sha256` covers every tracked file |
| Hygiene | PASS | README, verification and prior-art math rendered by GitHub, every span recognized |
| Stewardship | PASS | `CORRECTIONS.md` |
| Immutable semantic tag | PASS | annotated `v0.1.0` (object `bd77ed2`) → `dff5519`; tagger is the GitHub noreply identity |
| Public permanent archive with provider byte identity | PASS | the pinned GitHub `zipball/v0.1.0` (downloaded twice, identical) and the Zenodo file are byte-identical: 297732 bytes, SHA-256 `79965c9701f90fb55dce4706137cc4a051daf2061a23b25c2dba3ef30d246619`; Zenodo MD5 `8dd1874ec7c51f0ef1343b1d2bd5f24a` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.24379586` redirects to the Zenodo record; README, `CITATION.cff` and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | title, creator Kline, Jeffery, version v0.1.0, publication date 2026-11-19, license `gpl-3.0`, resource type software |
| Machine-readable citation | PASS | `CITATION.cff` with version DOI, concept DOI and `date-released: 2026-11-19` |

**Admission verdict:** ADMITTED (2026-11-19). The P1 residuals and the limits
stated in the README remain. No independent human expert has reviewed the
note.

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 297732 bytes, SHA-256
  `79965c9701f90fb55dce4706137cc4a051daf2061a23b25c2dba3ef30d246619`.
- Zenodo file `jeff-kline/symmetric-hadamard-4356-v0.1.0.zip`: identical to
  the pinned zipball.
- Separate determinism check: `git archive --format=zip v0.1.0`, generated
  twice, identical, 295230 bytes, SHA-256
  `9a3c2248af935c517331bd270f25e02c415763f5125b49a9142978f8c16d97ae`; a
  different file from the provider zipball, not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  12 pass, 0 warnings, 0 fail.

## External actions and owners

| Action | Owner | Status |
|---|---|---|
| Private GitHub repository and push | author authorization | done 2026-11-19 |
| Public visibility, secret scanning and push protection | author authorization | done 2026-11-19 |
| Zenodo enablement before the Release | author, in the Zenodo portal | done 2026-11-19 |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | done 2026-11-19 20:43 UTC: Release "Version 0.1.0" |
| Public-site listing | author authorization | landing entry at <https://jeff-kline.github.io/>; Pages build and live HTML checked for title, blurb, repository link and version DOI before this record was pushed |
| Living-metadata update (this commit) | author authorization | pushed after the site listing was verified live |
