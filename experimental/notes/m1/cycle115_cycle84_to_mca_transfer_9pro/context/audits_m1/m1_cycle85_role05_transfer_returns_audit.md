# Cycle 85 Role05 Transfer Returns Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Confidence: high that Cycle85 closed the honest interpretation of the Cycle84
finite certificate; moderate for the proposed two-copy official-profile
amplification, which still needs a concrete code/domain certificate.

The round is significant. It does not prove the full RS-MCA/proximity-prize
theorem, but it does convert Cycle84 from "large finite product occupancy" into
a genuine finite MCA slope lower certificate and sharply identifies why the
single-copy packet is not yet an official frontier-moving counterpacket.

## Raw Returns

Preserved in:

```text
experimental/notes/m1/cycle85_role05_transfer_returns_raw/
```

with checksums in:

```text
experimental/notes/m1/cycle85_role05_transfer_returns_raw/SHA256SUMS.txt
```

The nine roles split cleanly:

- Roles 01, 02, 06, and 09 prove/audit the corrected transfer theorem.
- Roles 03, 04, and 08 cut the one-copy official-frontier overclaim.
- Role 05 cuts naive tensor/product amplification.
- Role 07 records the public replay as finite-model evidence, not as a prize
  ledger term.

## What Is Bankable Now

The strongest one-copy statement now bankable is:

```text
L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY
```

For the explicit Cycle65-84 Role05 packet over

```text
F_0 = F_17[X] / (X^16 + X^8 + 3)
```

with

```text
n = 256
k = 137
sigma = 6
j = 113
```

there is an explicit shifted `t=1` RS/GRS MCA syndrome line with at least

```text
M_C(6) >= 52,747,567,092
```

distinct transverse bad slopes.

The exact Cycle84 packet spectrum transfers with no further loss:

```text
packet supports        = 52,747,567,104
distinct packet slopes = 52,747,567,092
singleton slope fibers = 52,747,567,080
double slope fibers    = 12
fibers of size >= 3    = 0
off-diagonal energy    = 24
```

## The Necessary Correction

Several roles independently caught the same correction. The slope coordinate is
not safely described as the raw product value in an arbitrary affine gauge.

If

```text
rho_beta(T) = P_T(beta)
```

then the actual reduced MCA color/slope is reciprocal-affine normalized:

```text
chi_T = a + b / rho_beta(T),   b != 0
```

or equivalently, in Role06's direct syndrome gauge,

```text
chi_T = -rho_beta(T)^(-1)
```

up to a common affine bijection of the line parameter.

For the Cycle65-84 packet this correction causes no loss, because all locators
share the exact same restriction to the degree-six support modulus

```text
Delta = 6[infinity].
```

Equivalently, in the non-normalized language, the scalar

```text
P_T|_Delta = gamma_T B|_Delta
```

has `gamma_T = 1` throughout the packet.

The first mathematical line where transfer could fail in future packets is
exactly this fixed-jet/fixed-`gamma_T` condition.

## What Is Cut

The one-copy Cycle84 packet should not be described as an official prize-frontier
counterpacket.

Native one-copy ledger:

```text
q_line = 17^16 = 48,661,191,875,666,868,481
T_line = floor(q_line / 2^128) = 0
```

The comparison

```text
52,747,567,092 > 2^32
```

is a useful internal benchmark from the Cycle67 threshold, not the native MCA
target for the raw one-copy field.

Compatible scalar extensions under the strict `q_line < 2^256` cap are only:

```text
17^16, 17^32, 17^48.
```

Their native thresholds are:

```text
floor(17^16 / 2^128) = 0
floor(17^32 / 2^128) = 6
floor(17^48 / 2^128) = 338,617,018,271,848,945,628
```

At `17^16` and `17^32`, simpler core/tangent lower bounds already dominate.
At `17^48`, the single-copy numerator is far below the native target.

The unmodified raw instance also has rate:

```text
k/n = 137/256
```

which is not one of the official rates under discussion. Several roles propose
rate repair/normalization lemmas, but their exact parameter choices differ and
should not be promoted until separately checked.

## Exact Arithmetic For The Next Window

Let

```text
N = 52,747,567,092.
```

Then:

```text
N^2 = 2,782,305,834,125,041,336,464
floor(N^2 / 8) = 347,788,229,265,630,167,058
floor(17^48 / 2^128) = 338,617,018,271,848,945,628
```

Thus both

```text
N^2 > floor(17^48 / 2^128)
```

and even

```text
floor(N^2 / 8) > floor(17^48 / 2^128)
```

hold. This is why the two-copy route is now the natural official-profile target.

Some raw answers contain small arithmetic slips in the displayed square or
margin; the values above are the locally recomputed values to use.

## Main Conflicts To Resolve

The round is aligned on the one-copy interpretation but not on the exact
amplification geometry.

Open conflicts:

1. Rate normalization appears in three forms:
   - add 18 fixed points to reach `(n,k)=(274,137)`;
   - remove 18 unused points to reach `(n,k)=(238,119)`;
   - add marker constraints to reach `(n,k)=(256,128)`.
   These are not interchangeable and need a small independent checker/audit.

2. Two-copy official constructions appear with different parameter packages:
   - `(n,k,sigma,j)=(560,280,6,274)` using fixed padding/generic translation;
   - `(n,k,sigma,j)=(476,238,12,226)` using two shortened copies;
   - `(n,k,sigma,j)=(512,256,12,244)` using a fused two-block construction.

3. Role02 claims an existential two-copy official-rate counterpacket over
   `F_17^48`. This is the most aggressive and potentially strongest return,
   but it remains `PENDING_CONCRETE_DOMAIN_CERTIFICATE`, not a banked public
   proof.

4. Naive Cartesian tensoring is cut. A successful two-copy result must realize
   one RS-compatible affine syndrome line with two independent color
   coordinates, not merely a product of two separate finite packets.

## New Exact Wall

The next wall should be named:

```text
W-CYCLE86-TWO-COPY-F17^48-AFFINE-COLOR-SEPARATION
```

One sufficient lemma is:

```text
L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION
```

Target statement:

Let

```text
Omega = {rho_beta(T) : T in P_0} subset F_0,
|Omega| = 52,747,567,092.
```

Over

```text
L = F_17^48,
```

choose `alpha in L \ F_0` and construct one official-rate `t=1` RS/GRS MCA
instance plus a support map

```text
Psi: P_0 x P_0 -> binom(D^(2), j^(2))
```

such that after one common affine normalization,

```text
z_{Psi(T1,T2)} = rho_beta(T1) + alpha rho_beta(T2).
```

Then `1, alpha` being `F_0`-linearly independent gives injectivity on
`Omega^2`, hence at least `N^2` slopes, exceeding the native `17^48` target.

This would convert the finite/model certificate into an official-scale lower
counterpacket, subject to full emitted certificates for:

- domain and code fingerprint;
- rate and reserve;
- field roles `q_gen`, `q_code`, `q_line`, `q_chal`;
- transversality/noncontainment;
- one-line RS compatibility;
- distinct-slope injection.

## Recommended Next Step

Do not launch another broad "solve everything" round.

First run a narrow local/worker audit:

```text
V-CYCLE85-ROLE05-PACKET-TO-MCA-BRIDGE
```

Checklist:

1. Verify the fixed `Delta=6[infinity]` jet and `gamma_T=1` for the packet.
2. Verify the reciprocal/affine slope formula in the exact syndrome gauge.
3. Verify transversality and no same-slope loss beyond the 12 double fibers.
4. Verify one selected rate-normalization lemma and its exact parameters.
5. Emit a machine-readable one-copy lower-term record marked finite/model, not
   frontier-moving.

Then run exactly one amplification target:

```text
L-CYCLE86-TWO-COPY-F17^48-AFFINE-COLOR-SEPARATION
```

with the local arithmetic above hard-coded into the prompt.

## PRZ Note

This is worth a compact PRZ note after the audit is banked, but not as a
"prize solved" announcement. The accurate message is:

```text
Cycle85 consensus: Cycle84 really gives a finite t=1 MCA slope packet of
52,747,567,092 transverse slopes, after reciprocal/affine slope normalization.
It does not move the one-copy official frontier. The new frontier-active target
is a two-copy F_17^48 affine-color separation; arithmetic says N^2 clears the
native 2^-128 target by >8x, but the RS-compatible one-line construction still
needs a concrete certificate.
```
