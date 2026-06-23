# V-CYCLE120-ABF-DIRECT-ADMISSIBILITY-AUDIT

Date: 2026-06-24

Source:

```text
Open Problems in List Decoding and Correlated Agreement
Gal Arnon, Dan Boneh, Giacomo Fenzi
April 8, 2026
local file:
experimental/notes/m1/cycle119_official_source_audit/abf_pdf_extract/ABF26_680_iacr.pdf
sha256:
e543ec6a4f3312b4383000e72e5aa23862e79cc9770ce21db2c48db679581de3
pages:
47
```

Extracted text files:

```text
ABF26_680_iacr_pdfplumber.txt
sha256:
eac4031f15a8ab430541e7d31af82f1dc10c2686ee31ed9d8c14ef10c78ec344

ABF26_680_iacr_pypdf.txt
sha256:
1f0db1f08b6b00955039eb9376eac866ba2362e5a4ac97d30a95575e4073b255
```

Rendered check pages:

```text
page 5: grand MCA challenge
page 9: RS and smooth-domain definitions
page 17: Definition 4.3, MCA error
```

## Executive Verdict

Under the ABF paper's printed grand MCA formulation, the Cycle116/Cycle119
row, predicate, and sampler are admissible.

The exact answer to the user-facing question is:

```text
YES, under ABF Definition 4.3 and the grand MCA challenge as printed,
RS[F_17^32,H,256] with H=<theta>, |H|=512, is an admissible smooth-domain
Reed-Solomon row; epsilon_mca is the support-wise same-support
noncontainment predicate; gamma is sampled uniformly from the code field;
and the grand MCA definition contains no endpoint, quotient, periodic,
duplicate-slope, charge, or retained-event filter.
```

Therefore the finite theorem gives an ABF-grand-MCA negative certificate at
delta = 125/256:

```text
epsilon_mca(RS[F_17^32,H,256], 125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

Even the Cycle116 agreement-262 theorem is enough for the ABF printed
definition, because ABF uses the closed support condition

```text
|S| >= (1-delta)n.
```

At n=512 and delta=125/256, this threshold is exactly 262. The Cycle119
two-ended agreement-263 theorem is stronger and remains useful against any
external strict-ball convention, but strictness is not required by ABF
Definition 4.3.

This is still not a complete solution of the grand challenge in the sense of
determining the exact largest delta*_C. It proves the upper/negative side:
for this admissible row, delta*_C(2^-128) is strictly below 125/256 if the
finite certificate is correct.

## Gate 1: The Row Is an Admissible Reed-Solomon Row

ABF Definition 2.11 defines:

```text
RS[F,L,k] = functions f:L->F represented by polynomials over F of degree < k.
```

Cycle row:

```text
K = F_17^32
H = <theta> subset K
|H| = 512
k = 256
C = RS[K,H,256]
```

Verdict:

```text
PASS
```

No prime-field-only restriction appears in the grand MCA row definition. ABF
uses a finite field F, and later sections explicitly discuss extension fields.

## Gate 2: The Domain Is Smooth

ABF Definition 2.12 defines smooth as:

```text
L subset F is smooth if it is a multiplicative coset of a subgroup H subset F*
whose order is a power of two.
```

Cycle row:

```text
H = <theta> subset K*
ord(theta) = 512 = 2^9
```

Verdict:

```text
PASS
```

The cycle row is the subgroup case of ABF's smooth-domain definition.

## Gate 3: The Rate And Parameter Envelope Match

The ABF grand MCA challenge permits rates:

```text
{1/2, 1/4, 1/8, 1/16}.
```

Cycle row:

```text
rate = 256/512 = 1/2
k = 256 <= 2^40
|F| = 17^32 < 2^256
```

Verdict:

```text
PASS
```

ABF says the authors are mostly interested in smooth-domain rows with
`k <= 2^40` and `|F| < 2^256`; the cycle row lies well inside this envelope.

## Gate 4: The Predicate Is Support-Wise Same-Support Noncontainment

ABF Definition 4.3 defines `epsilon_mca(C,delta)` as a maximum over
`f1,f2` of the probability over `gamma <- F` that there exists a support `S`
with:

```text
|S| >= (1-delta)n
Delta_S(f1 + gamma f2, C) = 0
Delta_S((f1,f2), C^{==2}) > 0
```

This means:

1. `f1 + gamma f2` is exactly code-explained on S;
2. `f1` and `f2` are not simultaneously code-explained on the same S.

Verdict:

```text
PASS
```

This is exactly the support-wise same-support noncontainment predicate used
by Cycle116/Cycle119.

## Gate 5: The Sampler Is Uniform Gamma From The Code Field

ABF notation section says `x <- S` means uniform sampling from the set S.
Definition 4.3 uses:

```text
gamma <- F
```

Verdict:

```text
PASS
```

For the cycle row, this is uniform sampling:

```text
gamma <- K = F_17^32.
```

No independent `q_chal` appears in ABF Definition 4.3 or in the grand MCA
challenge statement.

## Gate 6: No Extra Event Filters In The Grand MCA Challenge

The ABF grand MCA challenge is stated directly in terms of:

```text
epsilon_mca(C,delta)
```

and Definition 4.3 is exactly the event above.

Verdict:

```text
PASS_FOR_GRAND_MCA
```

The toy protocol in Section 6 adds protocol-specific list-decoding and
spot-check terms, but those are not additional filters inside the grand MCA
definition itself.

## Threshold Arithmetic

For the Cycle116/Cycle119 row:

```text
n = 512
delta = 125/256
(1-delta)n = (131/256) * 512 = 262
```

ABF uses:

```text
|S| >= (1-delta)n.
```

Therefore:

```text
Cycle116: agreement 262 passes ABF Definition 4.3.
Cycle119: agreement 263 passes ABF Definition 4.3 with one-symbol slack.
```

The density comparison is:

```text
17^32 =
2367911594760467245844106297320951247361

floor(17^32 / 2^128) = 6

52,747,567,092 > 6
```

So:

```text
52,747,567,092 / 17^32 > 2^-128.
```

## The Correct Prize-Facing Claim

The strongest defensible claim is:

```text
Assuming the Cycle84 finite census and the Cycle116/Cycle119 transfer proof,
the ABF grand MCA challenge admits the row
RS[F_17^32,H,256], and for that row one has
epsilon_mca(C,125/256) > 2^-128.
```

Equivalently:

```text
delta*_C(2^-128) < 125/256
```

for this specific row, under ABF Definition 4.3.

The result does not determine the exact value of `delta*_C`. Since ABF says
that resolving the challenge for a code requires specifying a delta*_C and
proving both sides, this is not by itself a complete exact-solution theorem.
It is, however, a direct admissible negative certificate at the displayed
radius and is clearly prize-facing partial progress under the public FAQ.

## What To Tell PRZ

If sending one more note, say:

```text
I checked the ABF PDF directly. The four gates appear to pass.

ABF Def. 2.12: smooth means multiplicative coset of a subgroup of F* whose
order is a power of two, so H=<theta>, |H|=512 qualifies.

ABF Def. 4.3: epsilon_mca is exactly the support-wise same-support event,
with gamma sampled uniformly from F. No q_chal or endpoint/quotient/charge
filter appears in the grand MCA definition.

Also ABF uses |S| >= (1-delta)n, so at delta=125/256 and n=512 the threshold
is 262. Cycle116 already matches the printed ABF threshold; Cycle119
agreement-263 is stronger and only needed for stricter external conventions.

So unless I am missing a nonprinted prize-policy restriction, this is an
ABF-admissible negative certificate:
epsilon_mca(RS[F_17^32,H,256],125/256)
>= 52,747,567,092 / 17^32 > 2^-128.
```

