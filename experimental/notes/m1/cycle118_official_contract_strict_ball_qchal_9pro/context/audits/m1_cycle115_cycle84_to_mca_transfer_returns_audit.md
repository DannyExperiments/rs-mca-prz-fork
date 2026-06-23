# Cycle115 Cycle84-To-MCA Transfer Returns Audit

## Verdict

```text
PROOF / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Confidence: high that the round produced a real paper-facing finite
RS-MCA/support-wise-line-decoding transfer theorem, conditional only on the
already-banked Cycle84 finite certificate and the Cycle85 fixed-jet RS-line
bridge. Moderate-high that the new smooth `[512,256]` padding/lift theorem is
correct; it still deserves a standalone reviewer note and tiny verifier before
being sent as the final PRZ artifact.

This is significant. It answers PRZ's second question at the finite/paper-facing
level:

```text
Cycle84's color-filtered m_max(beta)=2 certificate can be transferred into
an exact RS support-wise MCA / LD_sw lower-bound statement.
```

It does not prove an official Proximity Prize theorem, does not prove an
ordinary list-decoding lower bound, and does not settle the later M1/Cycle114
official source-contract wall.

## Raw Returns

Preserved in:

```text
experimental/notes/m1/cycle115_cycle84_to_mca_transfer_9pro_returns_raw/
```

Checksums:

```text
experimental/notes/m1/cycle115_cycle84_to_mca_transfer_9pro_returns_raw/SHA256SUMS.txt
```

Local checksum replay passes.

## Main Result To Bank

The round converges on the following theorem schema.

### L-CYCLE115-FIXED-JET-RS-MCA-LD-TRANSFER

Let `D subset F`, `|D|=n`, `beta notin D`, and let `J` range over a family of
`j`-subsets of `D`. Write

```text
P_J(X) = prod_{a in J} (X-a).
```

Assume all `P_J` have the same leading `sigma`-jet at infinity:

```text
deg(P_J - P_J') <= j - sigma.
```

Put

```text
k = n - j - sigma,
C = RS[F,D,k].
```

Then there is one affine line `u_z = f + z g` and one degree-one residue-line
datum `E = X - beta` such that every

```text
z_J = alpha + lambda / P_J(beta)      (lambda != 0)
```

is support-wise MCA-bad for `C` at agreement size `n-j = k+sigma`, with witness
support `S_J = D \ J`.

Consequently

```text
LD_sw(C, k+sigma) >= #{ P_J(beta) : J }
epsilon_mca(C, j/n) >= #{ P_J(beta) : J } / |F|.
```

The reciprocal-affine map is injective, so the bad-slope fiber histogram is
exactly the locator-value/product fiber histogram.

## Cycle84 Native Corollary

For the Cycle84 model:

```text
F0 = F_17[X]/(X^16 + X^8 + 3)
q0 = 17^16
D0 = <eta>, |D0| = 256
beta = X + 2
```

the Cycle84 co-support locators satisfy the fixed six-jet relation

```text
P_T(X) = X^113 - X^112 + O(X^107),
```

and

```text
P_T(beta) = kappa * Phi(T),     kappa != 0.
```

Therefore the standalone Cycle84 product spectrum transfers without loss:

```text
LD_sw(RS[F0,D0,137], 143) >= 52,747,567,092

epsilon_mca(RS[F0,D0,137], 113/256)
  >= 52,747,567,092 / 17^16.
```

This is a clean finite RS-MCA/support-wise-line-decoding theorem. It is not a
prize-frontier theorem: the rate is `137/256`, and

```text
floor(17^16 / 2^128) = 0.
```

## New Smooth Rate-1/2 Lift

Roles 03, 08, and 09 independently identify a stronger clean lift.

Let

```text
K = F0(theta), theta^2 = eta.
```

Since `eta` has order `256` in `F0^*`, it is not a square in `F0`, so

```text
K = F_17^32,
ord(theta) = 512,
H = <theta>, |H| = 512.
```

Using agreement padding on the unused half of `H`, the Cycle84/Cycle85 line
lifts to the ordinary smooth-domain RS code

```text
C = RS[F_17^32, H, 256],
n = 512,
k = 256,
agreement size = 262,
delta = 125/256.
```

The numerator is preserved:

```text
LD_sw(C, 262) >= 52,747,567,092

epsilon_mca(C, 125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

The integer target is tiny:

```text
floor(17^32 / 2^128) = 6,
52,747,567,092 > 6.
```

This is paper-facing and smooth-domain at finite-row level. It still should not
be advertised as a Proximity Prize solve, because the official extension-field /
source / challenge-field contract is not pinned here, and at this small
denominator the `2^-128` comparison is not the hard frontier mechanism. It is
nevertheless a real exact RS-MCA/LD_sw transfer theorem.

## Cycle88/89 Two-Copy Status

The old `[464,232]` row over `F_17^48` remains useful but conditional and not
official smooth-domain.

Conservative arithmetic:

```text
N = 52,747,567,092
P = 52,747,567,104
floor(17^48 / 2^128) = 338,617,018,271,848,945,628
N*P/2 = 1,391,152,917,379,006,070,784
margin = 1,052,535,899,107,157,125,156
```

Thus an exact `[464,232]` row with the stated projective-fiber bound would clear
the `17^48` target. But:

```text
464 = 2^4 * 29
```

so the domain is not a power-of-two multiplicative subgroup/coset. In
`F_17^48`, the largest power-of-two subgroup has order only `256`. The
Cycle88/89 row is therefore finite arbitrary-domain RS/GRS evidence until a new
smooth-domain realization theorem is proved.

## Role Ledger

| Role | Visible label | Conservative audit |
|---|---|---|
| 01 Transfer theorem prover | `PROOF` | Strong proof sketch of fixed-jet transfer, native Cycle84 row, and arbitrary `[464,232]` row. Overstates the two-copy count in places; use conservative `N*P/2` for Cycle88/89. |
| 02 Falsifier | `PROOF` | Useful because it proves finite transfer while cutting official prize promotion. Correctly identifies smooth one-copy/lift versus arbitrary `[464,232]` gap. |
| 03 Official RS object | `PROOF` | Strongest parameter ledger. Adds the `[512,256]` smooth lift and correctly classifies it as finite/paper-facing, not frontier solved. |
| 04 Product-to-slope auditor | `PROOF finite [256,137]` | Confirms reciprocal-affine transfer and fixed-jet condition. Good for the standalone proof. |
| 05 MCA consequence | `PROOF` | Confirms support-wise MCA noncontainment route. Useful for `def:mca` alignment. |
| 06 Line-decoding bridge | `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL` | Correctly says `LD_sw` is basically the support-wise MCA numerator, not ordinary list decoding. Strongest guardrail against overclaiming list decoding. |
| 07 q-ledger auditor | `BANKABLE_LEMMA` | Arithmetic passes. Correctly warns that `q_chal` cannot be used as denominator and that `[464,232]` needs coefficient-level replay. |
| 08 Prize-family embedding | `BANKABLE_LEMMA` | Most important new lift: smooth `[512,256]` over `F_17^32`. Cuts direct `[464,232]` smooth embedding. |
| 09 Referee | `PROOF` | Best synthesis. Gives PRZ-facing statement and exact remaining wall. |

## What This Proves And Does Not Prove

Proved / bankable:

```text
Cycle84 -> finite RS support-wise MCA / LD_sw numerator N
N = 52,747,567,092
native row: RS[F_17^16, <eta>, 137], delta=113/256
smooth lifted row: RS[F_17^32, <theta>, 256], delta=125/256
```

Not proved:

```text
ordinary list-decoding lower bound for one received word
official Proximity Prize counterpacket
protocol soundness failure
asymptotic theorem
official retained-slope theorem after source/charge normalization
lossless smooth-domain realization of the [464,232] / F_17^48 numerator
```

## First Failure Line For Prize Promotion

For the finite RS-MCA theorem, the first line that still deserves standalone
review is the Cycle85 fixed-jet/source contract:

```text
Cycle84 packet supports
  -> one common RS affine line f+zg with reciprocal-affine slope
     z_T = alpha + lambda / P_T(beta)
  -> support-wise noncontained witnesses.
```

The Pro workers give convincing proof sketches, but the reviewable artifact
should be a compact theorem note plus a small verifier, not nine raw Pro
transcripts.

For official/prize promotion, the first missing line is:

```text
smooth extension-field finite RS row
  -> authority-pinned official prize/source/challenge-field admissible row.
```

If extension fields are rejected, the missing theorem becomes:

```text
loss-preserving fixed-jet occupancy compiler into an accepted prime/deployed
smooth multiplicative RS domain.
```

## Exact Next Step

Do not launch another broad search before making this reviewable.

Create:

```text
V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE
```

It should include:

1. a two-page theorem note proving the fixed-jet locator-to-MCA theorem;
2. the Cycle84 native instantiation;
3. the smooth `[512,256]` padding/lift theorem over `F_17^32`;
4. exact q-ledger values;
5. explicit statement that this is finite/paper-facing and not a prize solve;
6. a tiny deterministic verifier for:
   - `ord(eta)=256`;
   - `eta` nonsquare in `F_17^16`;
   - `theta` order `512` in `F_17^32`;
   - `floor(17^32/2^128)=6`;
   - `N>6`;
   - fixed-jet/product-scalar identities already used by Cycle85.

Only after that should this be sent to PRZ as the compact answer to his transfer
question.
