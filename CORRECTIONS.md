# Corrections, withdrawals, and supersession

This repository keeps a visible record of material corrections to released
claims and artifacts.

## Policy

- Minor typographical or navigational fixes may be made on the living default
  branch without changing an archived release.
- A change to a statement, citation that affects priority or scope, or
  verification artifact creates a new version. The earlier tag and permanent
  archive remain unchanged and identifiable.
- A material error will be marked prominently in the README and in this file.
  The affected release will not be deleted or silently replaced.
- If an earlier record of a symmetric Hadamard matrix of order 2116 or 4356 is found,
  it will be credited in a new version.

Suspected errors may be reported through the repository's issue tracker:
<https://github.com/jeff-kline/symmetric-hadamard-4356/issues>.

## Version history

### 0.2.0 — released 2026-11-20

- Tag `v0.2.0` at commit `881dc93`; version DOI
  [`10.5281/zenodo.24382706`](https://doi.org/10.5281/zenodo.24382706), concept DOI `10.5281/zenodo.24379585`. The tagged snapshot
  retains its prepublication wording; the living repository carries the DOI.

- **Order of discovery.**
  1. Order 4356 was identified independently, without consulting SageMath
     (version 0.1.0).
  2. A later survey of SageMath's constructors against the census showed
     that SageMath already recognizes 4356.
  3. The same survey showed that it also recognizes 2116.
- **Earlier record found (priority).** SageMath implements the Wallis–Whiteman
  construction (`rshcd_from_prime_power_and_conference_matrix`) and has
  included Gritsenko's graph since 2021 (Trac #31394). Its constructor
  recognizes order 4356. Version 0.1.0 did not examine SageMath and said it
  found no earlier record; that statement is withdrawn and SageMath is
  credited. The census update itself is unchanged.
- **Scope.** The census entry 529 (order 2116), settled by the same theorem
  with Mathon's conference matrix of order 46, is added. It is cited and not
  rebuilt here.

### 0.1.0 — released 2026-11-19

- Tag `v0.1.0` at commit `dff5519`; version DOI
  [`10.5281/zenodo.24379586`](https://doi.org/10.5281/zenodo.24379586), concept DOI `10.5281/zenodo.24379585`.
- The tagged snapshot retains its prepublication “release candidate” wording
  and carries no DOI, because the DOI was minted by Zenodo after the GitHub
  Release. The living repository and paper now carry the active DOI; the
  archived files were not changed.
- Release preparation, before the tag: the dispositions of all audit findings
  are in [audit/LEDGER.md](audit/LEDGER.md).
