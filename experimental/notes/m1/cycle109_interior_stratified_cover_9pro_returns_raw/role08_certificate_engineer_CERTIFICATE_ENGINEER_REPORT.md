# BANKABLE_LEMMA — Cycle109 certificate-engineering result

## Verdict

A sound proof-carrying checker can certify a finite official line exactly and
can promote a family only through an external proof kernel. This does not prove
that every official line has the required certificate. Two rigorous items are
bankable:

1. exact fixed-size support/syndrome enumeration of official bad slopes;
2. a route cut showing that one separator on a HIGH affine plane cannot imply a
   polynomial slope cap.

## Exact finite checker lemma

Let `C=RS[K,D,k]`, `s=k+sigma>k`, and `u_z=f+zg`. A parameter `z` is officially
support-wise MCA-bad at agreement threshold `s` if and only if there is an
`s`-subset `S` of `D` such that, for a left-nullspace matrix `H_S` of the
Vandermonde generator matrix on `S`,

```text
H_S g != 0,
H_S f + z H_S g = 0.
```

The scalar `z`, if it exists, is unique.

### Proof

A witness on a support larger than `s` has an `s`-subset that remains bad. If
not, every `s`-subset would simultaneously admit degree-`<k` explanations for
`f` and `g`. Fix `k` points. Uniqueness of degree-`<k` interpolation on those
points glues all local explanations to explanations on the whole support,
contradicting condition (ii).

On an `s`-support, a word lies in the punctured RS code exactly when its syndrome
under `H_S` is zero. Thus condition (i) is `a+zb=0`, where `a=H_Sf` and
`b=H_Sg`. If `b=0`, this equation forces `a=0`, so both words are explained and
condition (ii) fails. Therefore `b!=0`, and one nonzero coordinate determines a
unique `z`; all coordinates are then checked.

## Checker-soundness implication

Suppose a certificate supplies:

- an exact complete bad-slope set in `K_line`;
- one disjoint primary assignment per distinct slope;
- exact caps for paid branches;
- at most `n^C` retained-tag charts for residual branches;
- injective `K_line -> K_line` slope normalizations on every chart;
- a verified chart cap, and AP_corr rank escape or an official charge;
- an exact field ledger.

Then

```text
N_off <= sum(paid branch caps) + sum(chart caps) = N_cert.
```

If `N_cert <= floor(q_line/2^128)`, then

```text
N_off/q_line <= 2^-128.
```

This is a conditional soundness theorem. It does not establish existence of the
certificates for every line.

## HIGH-plane route cut

On `K^2`, the polynomial `X` separates the plane from the layer `X=0`, but all
`|K|` points `(0,z)` remain on that layer. Hence rank escape from one polynomial
on a two-dimensional plane yields at best an `O(D|K|)` zero bound. A HIGH chart
requires a second zero-dimensionality mechanism: a curve plus transversality,
two independent separators, a one-dimensional slice, or an exact finite image.

## First missing universal lemma

`L-CYCLE110-SOURCE-APCORR-TO-ACCEPTED-CHART-OR-CHARGE`:

For every uncharged official source object with retained source tag and
intrinsic denominator degree `t`, source AP_corr must produce:

- LOW: a same-field injective residual-image chart with polynomial cap;
- BALANCED: a complement-line/syndrome-pencil separator with polynomial cap;
- HIGH: a zero-dimensional plane certificate, not merely one separator;

or else a named official endpoint, quotient/periodic, contained/delete-one,
tangent, field, affine-color, hidden-action-rank, or normalization charge.

The earliest branch-specific unresolved case in the checker order is the LOW
residual-image cap. The HIGH single-separator mechanism is already cut.
