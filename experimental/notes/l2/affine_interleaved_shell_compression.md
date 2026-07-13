# Affine interleaved shell compression

## Status

`PROVED` under the hypotheses printed below.

This note gives an arity-independent reduction from a common-column
interleaved list to one-row lists.  It also records the exact scalar-extension
compiler used by the deployed Grand List row.  It does not prove the remaining
base-field one-row list bound.

## Setup

Let `B` be a finite field of size `b`, let `E/B` be an extension, and let `D`
be an evaluation set of size `n`.  Let `C` be a `B`-linear code in `E^D` with
the `K`-point uniqueness property

```text
c != c'  =>  |{x in D : c(x)=c'(x)}| <= K-1.
```

For `X in E^D` and `c in C`, put

```text
A_X(c) = {x in D : X(x)=c(x)},
L_s(X) = #{c in C : |A_X(c)|>=s}.
```

For `U=(U_1,...,U_r)`, define the completed common-column list

```text
Lambda_r(U;s)
  = {(c_1,...,c_r) in C^r :
       |intersection_i A_{U_i}(c_i)| >= s}.
```

Assume throughout that `K<=s<=n` and `b-n+s>0`.

## Affine weighted theorem

For `r>=2` and `lambda=(lambda_2,...,lambda_r) in B^(r-1)`, set

```text
U_lambda = U_1 + sum_{i=2}^r lambda_i U_i.
```

For a listed tuple `c`, put

```text
T(c) = intersection_{i=2}^r A_{U_i}(c_i).
```

Then

```text
sum_{c in Lambda_r(U;s)}
  b^(r-2) (b-n+|T(c)|)
    <= sum_{lambda in B^(r-1)} L_s(U_lambda).             (1)
```

In particular, if

```text
L_B^*(s) = max_{X in E^D} L_s(X),
```

then

```text
|Lambda_r(U;s)|
  <= floor(b L_B^*(s)/(b-n+s)).                           (2)
```

The coefficient in (2) is independent of `r`.

### Proof

Define the exact threshold ladder

```text
s_0=s,                 s_{j+1}=2s_j-K+1.
```

It strictly increases until it exceeds `n`.  Fix a listed tuple `c`, let
`G(c)=intersection_i A_{U_i}(c_i)`, and choose the unique shell `j` with

```text
s_j <= |G(c)| < s_{j+1}.
```

For each coordinate outside `T(c)`, the extra-agreement equation in `lambda`
is a nonzero `B`-linear equation.  Its solution set has size at most
`b^(r-2)`.  Coordinates in `T(c)\G(c)` have no solution.  Therefore at most

```text
b^(r-2) (n-|T(c)|)
```

coefficient vectors raise the combined agreement to the next shell.  At
least

```text
b^(r-2) (b-n+|T(c)|)
```

coefficient vectors keep it in the tuple's current shell.

Fix one coefficient vector and one shell.  If two good tuples produce the
same combined codeword, their common agreement sets both have size at least
`s_j` and their union lies in a one-row agreement set of size at most
`s_{j+1}-1=2s_j-K`.  Their intersection consequently has size at least `K`.
Every pair of corresponding row codewords agrees on this intersection, so
`K`-point uniqueness makes the tuples equal.  Different shells cannot collide
because the one-row agreement count belongs to a unique shell.  Thus all good
tuple incidences inject into the one-row lists.  Summing gives (1).  Since
`|T(c)|>=s`, equation (2) follows.

## Symmetric projective theorem

Write

```text
Pi_j(b)=1+b+...+b^j.
```

For a projective coefficient direction `[alpha] in P^(r-1)(B)`, let
`U_[alpha]=sum_i alpha_i U_i`.  Scaling the representative by a nonzero
element of `B` preserves its one-row list size.  The same shell injection gives

```text
(Pi_{r-1}(b)-(n-s)Pi_{r-2}(b)) |Lambda_r(U;s)|
  <= sum_[alpha] L_s(U_[alpha]),                          (3)
```

where

```text
Pi_{r-1}(b)-(n-s)Pi_{r-2}(b)
  = 1+(b-n+s)Pi_{r-2}(b) > 0.
```

At a coordinate outside a tuple's common agreement set, the projective
annihilators form the projectivization of a proper subspace and number at most
`Pi_{r-2}(b)`.  This proves (3) by the same fixed-direction shell injection.

## Scalar-extension compiler

The completed-list bijection below is the existing extension-coordinate
identity from `experimental/notes/l2/l2_interleaved_dilation_constants.md`,
Section 6, applied rowwise.  It is recalled as an input; the new compiler step
is its composition with (2), yielding (5).

Now assume `D subset B` and

```text
C_B = RS[B,D,K],
C_F = C_B tensor_B F = RS[F,D,K],
[F:B]=e.
```

Choose a `B`-basis of `F` and expand every received row and codeword into its
`e` base coordinates.  Equality at one evaluation point holds over `F` if and
only if all `e` base coordinates agree.  Hence, for every interleaving arity
`mu`, there is an exact completed-list bijection

```text
|Lambda_mu(C_F,U;s)|
  = |Lambda_{e mu}(C_B,Phi(U);s)|.                        (4)
```

Combining (2) and (4) yields

```text
|Lambda_mu(C_F,U;s)|
  <= floor(b L_B^*(s)/(b-n+s)),                           (5)
```

with no exponent depending on `e` or `mu`.

## Arbitrary-subset two-row corollary

Let the two-row code be linear over a field of size `Q`.  For any subset `R`
of completed pairs with common agreement at least `s`, the affine proof with
`r=2` remains injective after restricting to `R` and gives

```text
sum_{(d,c) in R} (Q-n+|A_W(c)|)
  <= sum_{lambda in F_Q} L_s(V+lambda W).                 (6)
```

For the high-anchor residual of PR #695, where
`tau(s)=2s-K+1` and `|A_W(c)|>=tau(s)`, this implies

```text
R_hh^post(V,W;s)
  <= floor(
       sum_lambda L_s(V+lambda W)/(Q-n+tau(s))
     ).                                                   (7)
```

Equation (7) applies after arbitrary completed-pair first-match deletion.  It
does not require a packet owner or a packet-representation count.

## Deployed Grand List ledger

For the deployed sextic row,

```text
p = 2^31-2^24+1              = 2,130,706,433,
q = p^6,
n = 2^21                     = 2,097,152,
K = 2^20                     = 1,048,576,
m                             = 1,116,047,
B* = floor(q/2^128)          = 274,980,728,111,395,087,
p-n+m                        = 2,129,725,328.
```

The exact sufficient base one-row ceiling obtained from (5) is

```text
L_p^*(m) <= T_m,
T_m = floor(((B*+1)(p-n+m)-1)/p)
    = 274,854,110,496,187,592.                             (8)
```

The gap to the necessary repeated-row ceiling is

```text
B*-T_m = 126,617,615,207,495,
```

which is approximately `0.046046%` of `B*`.  The exact projective sufficient
ceiling for two base-coordinate rows is `274,854,110,496,247,017`.  For the
scalar extension, the affine bound (5) applies directly to all `6 mu`
base-coordinate rows, irrespective of their actual quotient rank, so (8) is
the uniform deployed target.

The adjacent unsafe identity-prefix value remains above `B*`.  The missing
safe statement is exactly the one-row inequality (8); it is not proved here.

## Novelty and nonclaims

PR #675 supplies invertible row-span reduction and its threshold recursion.
PR #695 exposes the exact low layer and the residual `R_hh`.  Their maps are
invertible row operations.  The present theorem controls the collisions of
singular one-dimensional projections and works at arbitrary arity.  Repeated
rows show that a one-row maximum cannot be removed from the final statement.

This note does not prove:

- the one-row bound (8);
- a deployed adjacent safe certificate;
- the official Grand List theorem;
- a Grand MCA atlas or any MCA slope payment;
- a replacement of the challenge denominator `q=p^6` by the base field `p`.

The base field enters only in the compression theorem.  The protocol budget
continues to use the literal challenge field.
