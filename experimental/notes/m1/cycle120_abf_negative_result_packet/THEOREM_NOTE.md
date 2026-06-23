# Cycle120 ABF-Facing RS-MCA Negative Result Note

Date: 2026-06-24

## Abstract

Let

```text
K = F_17^32,
H = <theta> subset K^*,
|H| = 512,
C = RS[K,H,256].
```

Assuming the imported Cycle84 finite census and the Cycle116 fixed-jet
transfer theorem, the row satisfies

```text
LD_sw(C,262) >= 52,747,567,092.
```

The printed ABF grand MCA definition uses the closed support threshold

```text
|S| >= (1-delta)n.
```

At `n=512` and `delta=125/256`, this threshold is exactly `262`. Therefore,
under ABF Definition 4.3,

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

Thus the theorem gives an ABF-admissible negative result at
`delta=125/256`: for this row, any largest value `delta*_C` satisfying
`epsilon_mca(C,delta*_C) <= 2^-128` must be strictly below `125/256`, provided
the proof chain is correct.

Cycle119 strengthens the same row to agreement `263`, hence distance at most
`249 < 250 = (125/256)512`. This strict-ball strengthening is not needed for
the printed ABF closed-threshold definition, but it is useful against stricter
external conventions.

This note does not claim the exact value of `delta*_C`, ordinary list decoding,
protocol soundness failure, an asymptotic theorem, or peer-reviewed prize
acceptance.

## 1. ABF Source Gates

Source:

```text
Open Problems in List Decoding and Correlated Agreement
Gal Arnon, Dan Boneh, Giacomo Fenzi
IACR ePrint 2026/680
local PDF SHA-256:
e543ec6a4f3312b4383000e72e5aa23862e79cc9770ce21db2c48db679581de3
```

The ABF grand MCA challenge asks for a Reed-Solomon code
`C = RS[F,L,k]` over a smooth evaluation domain `L subset F`, with rate in
`{1/2,1/4,1/8,1/16}`, and threshold `epsilon* = 2^-128`.

The row

```text
C = RS[F_17^32,H,256],
|H| = 512
```

passes the printed gates:

```text
Field: finite field K = F_17^32.
Domain: H = <theta> is a multiplicative subgroup of K^*.
Smoothness: |H| = 512 = 2^9, so H is a power-of-two subgroup.
Rate: 256/512 = 1/2.
Envelope: 256 <= 2^40 and 17^32 < 2^256.
```

ABF's notation section states that `x <- S` means uniform sampling from `S`.
Definition 4.3 samples

```text
gamma <- F.
```

For this row, the MCA line parameter is therefore sampled uniformly from
`K = F_17^32`. No independent `q_chal` appears in the ABF grand MCA definition.

## 2. ABF MCA Predicate

ABF Definition 4.3 defines `epsilon_mca(C,delta)` as the maximum over words
`f1,f2` of the probability over `gamma <- F` that there exists a support `S`
with:

```text
|S| >= (1-delta)n,
Delta_S(f1 + gamma f2, C) = 0,
Delta_S((f1,f2), C^{==2}) > 0.
```

Equivalently, on the same support `S`:

```text
f1 + gamma f2 is exactly explained by a codeword of C,
but f1 and f2 are not simultaneously explained by codewords of C.
```

This is exactly the support-wise same-support noncontainment predicate used in
the Cycle116 and Cycle119 theorems.

## 3. Imported Finite Theorem

The Cycle84 finite census supplies

```text
N = 52,747,567,092
```

distinct product values on the designated Cycle84 shell. The banked finite
receipt includes:

```text
maximum product fiber size = 2,
exactly 12 double fibers,
no product fiber of size >= 3,
all 336 slot bridge identities.
```

The Cycle116 fixed-jet transfer proves a finite support-wise theorem for the
smooth row

```text
C = RS[F_17^32,H,256], |H|=512:
LD_sw(C,262) >= N.
```

Unpacked into ABF Definition 4.3, this means there are words `f1,f2 in K^H`
and at least `N` distinct values `gamma in K` such that for each such `gamma`
there is a support `S_gamma subset H` satisfying:

```text
|S_gamma| >= 262,
(f1 + gamma f2)|_{S_gamma} is code-explained by C,
(f1,f2)|_{S_gamma} is not simultaneously code-explained by C^{==2}.
```

Thus the proof gives at least `N` ABF-bad line parameters.

## 4. Threshold Arithmetic

For `n=512` and `delta=125/256`,

```text
(1-delta)n
  = (1 - 125/256) * 512
  = (131/256) * 512
  = 262.
```

Therefore the Cycle116 agreement-262 theorem meets ABF Definition 4.3 exactly.

The field size is

```text
17^32 =
2367911594760467245844106297320951247361.
```

The exact threshold comparison is:

```text
floor(17^32 / 2^128) = 6,
52,747,567,092 > 6.
```

Equivalently,

```text
2^128 * 52,747,567,092 > 17^32,
```

so

```text
52,747,567,092 / 17^32 > 2^-128.
```

Since ABF samples `gamma` uniformly from `K`, the ABF MCA probability is at
least this quotient.

## 5. Consequence For The Grand MCA Challenge

ABF says that resolving the grand MCA challenge for a code requires specifying
the largest `delta*_C` such that

```text
epsilon_mca(C,delta*_C) <= 2^-128
```

and proving the corresponding upper and lower sides. The present packet proves
only the negative side at one concrete radius:

```text
epsilon_mca(C,125/256) > 2^-128.
```

Therefore, for this row,

```text
delta*_C(2^-128) < 125/256
```

provided the proof chain is correct. This is prize-facing partial
progress and a negative result against any expectation that this row remains
MCA-secure through radius `125/256`.

## 6. Cycle119 Strict Strengthening

Cycle119 proves a stronger finite/source theorem on the same row:

```text
LD_sw(C,263) >= 52,747,567,092.
```

It uses a two-ended locator theorem rather than the invalid naive multiplication
padding argument. The two-ended evaluator uses:

```text
common top six locator coefficients,
one common nonzero constant coefficient,
selected product degrees 0,250,251,252,253,254,255.
```

It does not assume a common seventh top coefficient.

The resulting witnesses have distance at most

```text
512 - 263 = 249,
```

which is strictly below

```text
(125/256) * 512 = 250.
```

Thus Cycle119 is a one-symbol strict-ball strengthening. It is not needed for
the ABF printed closed condition, but it should remain in the packet as a
robustness addendum.

## 7. Proof Spine To Audit

The shortest proof spine is:

```text
Cycle84 exact product occupancy
  -> fixed-jet/product-scalar bridge
  -> Cycle116 agreement-262 smooth RS transfer
  -> ABF Definition 4.3 at delta=125/256
  -> N / 17^32 > 2^-128.
```

The optional strengthening is:

```text
Cycle84 exact product occupancy
  -> two-ended Cycle119 transfer
  -> agreement-263 strict-ball witnesses
  -> same ABF density lower bound.
```

## 8. Non-Claims

This packet does not prove:

```text
the exact value of delta*_C;
ordinary fixed-word list decoding;
the ABF grand list-decoding challenge;
protocol soundness failure;
an asymptotic theorem;
a deployed prime-field theorem;
peer-reviewed acceptance;
automatic prize award;
an independent q_chal theorem for a separate protocol experiment.
```

## 9. Submission Implications

The Proximity Prize website states that a submission should include a PDF that:

```text
clearly states the claimed results,
explains how they relate to the prize challenge,
situates them with respect to prior work.
```

It also states:

```text
AI-aided submissions are allowed,
human authors are responsible for correctness,
submissions should be public on arXiv or IACR ePrint for timestamping,
peer-reviewed acceptance is required for final prize consideration,
partial progress may be considered,
prize money may be split among multiple submissions.
```

Accordingly, this packet should be turned into a short human-edited PDF note
before any public timestamp or prize email.

