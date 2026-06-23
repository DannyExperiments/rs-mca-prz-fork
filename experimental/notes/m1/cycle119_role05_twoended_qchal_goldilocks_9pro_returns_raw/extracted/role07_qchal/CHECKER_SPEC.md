# V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT — Checker Specification

## Scope

This checker is a finite sampler-map/model checker for the banked Cycle116 source-scoped support-wise MCA line. Even a positive sampler terminal closes only the sampler layer; strict/closed radius, row admissibility, and official-prize adoption remain separate contracts. No terminal is an official-prize decision unless those contracts and an independent authority trust channel are also supplied.

The pinned constants are

```text
K = F_17^32
Q = |K| = 2367911594760467245844106297320951247361
N = 52,747,567,092
n = 512
k = 256
agreement = 262
radius = 125/256
threshold = 2^-128
```

The attached sources define one sampled variable `z in F`, uniformly counted with denominator `|F|`; they do not define an independent official `q_chal`.

## Exact stdout vocabulary

The checker prints exactly one line, chosen from:

```text
DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
BALANCED_CHALLENGE_PROJECTION_NO_LOSS
IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

Any malformed, unauthenticated, unsupported, or inconsistent state maps to the last terminal. Diagnostics are optional stderr only.

## Source binding

The source-definition root is

```text
89ebe887c02064a52b840c5e96992ff4f328575280a8f6dbed86e2b7dd7e7327
```

It is the SHA-256 of the domain-separated concatenation `CYCLE119_QCHAL_SOURCE_DEFINITION_V1\0` and, in order:

```text
context/base_cycle118_context/source/RS_disproof_v3.tex lines 110..115
context/base_cycle118_context/source/slackMCA_v3.tex lines 639..653
```

including each fixed path, line range, exact UTF-8/LF slice, and NUL separators. The individual slice hashes are:

```text
e65dbc3b34be54e4e6c3a45c48da32a2adf519047ec7a006d60e6201e28572d9
197663dd490be2970fc80a78116acf6a937f1922cf67de91adb6e146477bf046
```

The checker also pins the full files and requires the Cycle117 expected and observed receipts to be byte-identical and to state:

```text
primary_terminal = SOURCE_CONTRACT_MISSING_NO_CLAIM
q_gen = q_code = q_line = Q
q_chal = null
LD_sw lower bound = N
agreement = 262
radius = 125/256
```

## Authority root

The receipt cannot self-authorize. Define

```text
payload = canonical JSON of the receipt after deleting authority_root
root = SHA256("CYCLE119_QCHAL_AUTHORITY_PAYLOAD_V1\0" || payload)
```

Canonical JSON means UTF-8, sorted keys, no insignificant whitespace, and no NaN/Infinity. A positive terminal requires all three equalities:

```text
receipt.authority_root = root
--trusted-authority-root = root
source_definition_hash = pinned source-definition root
```

The CLI trust pin must arrive independently. Merely placing a hash inside the receipt proves integrity, not authority.

## Supported defined sampler states

Positive classification is deliberately narrow.

### Direct source-field sampling

```text
challenge_space = K
challenge_distribution = uniform
q_chal = Q
line_field = K
map = identity K -> K
base event = exact preimage of the N certified Cycle116 bad slopes
all filter/duplicate/quotient/charge stages retain challenge occurrences
```

Output:

```text
DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
```

### Balanced projection

For `r >= 2`:

```text
challenge_space = E = F_17^(32r), uniform
q_chal = Q^r
line_field = K
map = coordinate-zero projection E = K^r -> K
challenge encoding = an authority-bound ordered K-basis coordinate tuple
map basis_id = challenge-space basis_id
fiber size = Q^(r-1)
```

The exact certified preimage count is `N Q^(r-1)`. If every event-processing stage retains challenge occurrences, output:

```text
BALANCED_CHALLENGE_PROJECTION_NO_LOSS
```

### Identity scalar extension

For `r >= 2`:

```text
challenge_space = line_field = E = F_17^(32r), uniform
map = identity E -> E
line = the original K-valued Cycle116 line, scalar-extended to E
```

The full bad set is contained in K, hence has size at most Q. Since `Q/|E| <= 1/Q < 2^-128`, output:

```text
IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
```

This terminal uses the full-line upper bound Q, not the certified lower bound N.

### Official processing crosses the threshold downward

The event pipeline is ordered:

```text
exact map pullback/filter
then duplicate policy
then quotient-or-charge policy
then final retained numerator
```

Every stage records exact integer input and output counts; outputs cannot exceed inputs. `RETAIN`, `COUNT_CHALLENGE_OCCURRENCES`, and `NONE` force equality. A nontrivial stage must strictly decrease the count.

The filter terminal is emitted only when the map's pre-processing **Cycle116-certified packet** density is above threshold but the exact final retained certified-packet density is at or below threshold:

```text
2^128 * prefilter_numerator > q_chal
2^128 * final_retained_numerator <= q_chal
```

Output:

```text
OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD
```

This cuts the Cycle116 certificate route. It does **not** prove that every uncatalogued bad slope or the full official bad-event set is below threshold.

`q_chal` is always the cardinality of the actual official challenge space. A quotient-class count may not be divided by the pre-quotient `q_chal`; if the authority changes the sample space, the receipt must replace `challenge_space`, `challenge_distribution`, and `q_chal` accordingly. Otherwise the checker treats quotient/charge output only as an exact retained challenge-mass count.

A lossy pipeline that remains above threshold is intentionally not mislabeled “no loss”; because the mandated terminal vocabulary has no name for it, it fails closed to `UNDEFINED_MAP_NO_OFFICIAL_CLAIM`.

## Decision order

```text
1. Verify pinned source bytes and source-definition hash.
2. Require an independently trusted authority root.
3. Require a uniform finite challenge space and exact q_chal cardinality.
4. Validate line field, map, and exact pullback count.
5. Validate the ordered nonincreasing event-processing ledger.
6. If proper identity scalar extension, emit scalar-extension-killed.
7. If a direct/balanced prefilter violation crosses below threshold through processing, emit filter-drops.
8. If direct K with exact no loss, emit direct-K-retained.
9. If balanced projection with exact no loss, emit balanced-no-loss.
10. Otherwise emit undefined/no-official-claim.
```

## Exact integer threshold tests

No floating point is used.

```text
above threshold  <=>  2^128 * numerator > denominator
at/below         <=>  2^128 * numerator <= denominator
```

For Cycle116:

```text
floor(Q / 2^128) = 6
2^128 * N > Q
Q > 2^128
```

## Current packet terminal

The packet contains no independently trusted authority root and its Cycle117 receipt explicitly states that no authority-pinned official contract was supplied. Therefore the bundled current receipt deterministically returns:

```text
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```
