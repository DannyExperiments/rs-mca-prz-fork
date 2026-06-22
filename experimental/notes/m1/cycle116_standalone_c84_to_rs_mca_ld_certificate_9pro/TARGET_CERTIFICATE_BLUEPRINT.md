# Target Certificate Blueprint

## Goal

Build a standalone, reviewer-facing finite theorem/certificate:

```text
V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE
```

It should turn the already verified Cycle84 finite packet theorem into a clean
Reed--Solomon support-wise MCA / `LD_sw` theorem, without raw Pro/Fable
transcripts, workflow provenance, or ambiguous prize claims.

## Finite anchor

The Cycle84 standalone certificate verifies:

```text
m_max(beta) = 2
Occ(beta) = 52,747,567,092
D = 24
12 double fibers, no fibers of size >= 3
```

over

```text
F0 = F_17[X]/(X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2.
```

Treat this finite theorem as accepted unless you find an internal contradiction.

## Desired theorem A: fixed-jet locator-to-MCA transfer

Let `D subset F`, `|D|=n`, `beta notin D`, and let `J` range over `j`-subsets
of `D`. Write

```text
P_J(X) = prod_{a in J} (X-a).
```

Assume a common leading `sigma`-jet:

```text
deg(P_J - P_J') <= j - sigma
```

for all pairs. Put

```text
k = n - j - sigma
C = RS[F,D,k].
```

Expected conclusion:

There exists one affine line `u_z = f + z g` and one degree-one residue datum
`E = X - beta` such that every

```text
z_J = alpha + lambda / P_J(beta),   lambda != 0
```

is support-wise MCA-bad for `C` with witness support

```text
S_J = D \ J,   |S_J| = k + sigma.
```

Hence

```text
LD_sw(C,k+sigma) >= #{P_J(beta): J}
epsilon_mca(C,j/n) >= #{P_J(beta): J} / |F|.
```

The proof must explicitly construct or identify `f`, `g`, the explaining
codewords, and the noncontainment argument.

## Desired theorem B: Cycle84 native instantiation

For the Cycle84 family, the support/cosupport locators should satisfy

```text
P_T(X) = X^113 - X^112 + O(X^107)
P_T(beta) = kappa * Phi(T),  kappa != 0.
```

Then

```text
LD_sw(RS[F0,<eta>,137],143) >= 52,747,567,092

epsilon_mca(RS[F0,<eta>,137],113/256)
  >= 52,747,567,092 / 17^16.
```

This is finite RS-MCA / support-wise line-decoding content, not ordinary list
decoding and not a prize solve.

## Desired theorem C: smooth `[512,256]` lift

Let

```text
K = F0(theta),  theta^2 = eta.
```

Since `eta` has exact order `256` in `F0^*`, it should be nonsquare, so

```text
K = F_17^32
ord(theta) = 512
H = <theta>, |H| = 512.
```

Using agreement padding on `H = <eta> union theta<eta>`, lift the native row to

```text
C = RS[F_17^32,H,256]
agreement size = 262
delta = 125/256
```

with preserved numerator:

```text
LD_sw(C,262) >= 52,747,567,092

epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

Integer ledger:

```text
floor(17^32 / 2^128) = 6
52,747,567,092 > 6.
```

The certificate must explain that this is a finite/paper-facing smooth-domain
extension-field row. It is not automatically an official Proximity Prize solve.

## Must not overclaim

The final artifact must explicitly not claim:

```text
ordinary list-decoding lower bound
protocol soundness failure
official Proximity Prize counterpacket
asymptotic theorem
accepted/deployed prime-field theorem
lossless F_17^48 smooth-domain realization of the [464,232] row
```

## Desired verifier

At minimum, propose or write a tiny deterministic verifier for:

```text
irreducibility of X^16 + X^8 + 3 over F_17
eta has order 256
eta is nonsquare in F0
theta^2 = eta gives F_17^32 and theta has order 512
floor(17^32 / 2^128) = 6
52,747,567,092 > 6
Cycle84 certificate values match the standalone certificate
fixed-jet/product-scalar identities are either checked or explicitly imported
  from a named Cycle85 fixed-jet certificate
```

If a needed identity is not currently verifier-backed in the packet, name it as
the exact missing checker clause rather than silently assuming it.
