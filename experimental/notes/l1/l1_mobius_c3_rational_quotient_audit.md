# L1 Mobius C3 Rational Quotient Audit

- **Status:** PROVED / ROUTE_CUT / AUDIT.
- **Agent/model:** Codex.
- **Date:** 2026-06-24.
- **Scope:** Compact integration of the Cycle127 Mobius-C3 quotient work. This
  note does not edit Papers A-D and does not assert a positive L1 local-limit
  theorem, MCA theorem, line-decoding theorem, or protocol-safety consequence.

## Purpose

The subgroup quotient notes in this folder treat quotients of the form

\[
        X\mapsto X^d
\]

on a smooth multiplicative domain. In that case quotient moments are ordinary
decimated RS syndrome moments:

\[
        X^c(X^d)^h=X^{c+dh}.
\]

Cycle126/127 produced a different quotient geometry: an order-three Mobius
action. This note records the compact conclusion. The Mobius construction is
quotient-structured, but the subgroup-power syndrome reduction does not import
at no loss. A rational quotient needs either a rational-syndrome formalism, a
denominator-cost term, or a special identity for the particular support and
amplitudes.

This is not another Paper-A no-slack example. It is an L1/Paper-B-facing route
cut about what counts as "quotient charged" after the subgroup quotient ledger
has been removed.

## Baseline From Papers A-D

- Paper A already supplies no-slack smooth-domain obstructions, so larger
  examples in that direction are not the current frontier.
- Paper B's explicit quotient-periodic reductions use subgroup-power quotients
  on multiplicative domains.
- The existing L1 notes prove decimated multisequence reductions and low-defect
  closures for subgroup coset quotients.
- Paper D's explicit-line direction does not provide a rational-quotient
  reserve theorem.

Thus the new question is narrow:

\[
        \text{Does a rational Mobius quotient transfer into the existing}
        \text{ ordinary RS syndrome reserve ledger at no loss?}
\]

The answer proved here is no.

## Mobius C3 Quotient

Let \(K\) be a field of characteristic not \(3\). Put

\[
        \phi(X)=\frac{1}{1-X}.
\]

Then

\[
        \phi^2(X)=\frac{X-1}{X},\qquad \phi^3(X)=X.
\]

The rational function

\[
        J(X)=\frac{N(X)}{D(X)}
        =
        \frac{X(X-1)}{X^3-3X+1}
\]

is \(\phi\)-invariant, and \(K(X)^{\langle\phi\rangle}=K(J)\). Away from the
branch and pole locus, the fibers of \(J\) are the three-point
\(\phi\)-orbits.

## Exact Defect Factorisation

Let \(R:\mathbf P^1\to\mathbf P^1\) be any nonconstant rational map, and let
\(S\subset \mathbf P^1(K)\) be finite. Define \(T=R(S)\), and let

\[
        \operatorname{Sat}_R(S)=R^{-1}(T)_{\rm red}.
\]

Then

\[
        S\subseteq \operatorname{Sat}_R(S),
\]

and the exact quotient defect is

\[
        \delta_R(S)
        :=
        |\operatorname{Sat}_R(S)|-|S|
        =
        \sum_{t\in T}
        \left(
          |R^{-1}(t)_{\rm red}|-|S\cap R^{-1}(t)|
        \right).
\]

Equivalently, in reduced-divisor notation,

\[
        \delta_R(S)=\deg(R^*T_{\rm red}-S),
\]

where the pullback is interpreted as the reduced pullback over fibers met by
\(S\).

For a generic split degree-three fiber, exact two-of-three occupancy gives one
missing point per occupied quotient fiber. Hence for the Mobius quotient,

\[
        |S\cap J^{-1}(t)|=2\quad(t\in J(S))
        \quad\Longrightarrow\quad
        \delta_J(S)=|J(S)|.
\]

Thus "at most two points in each generic \(J\)-fiber" is not a bounded-defect
condition. Completing to a quotient pullback costs one point per active
quotient fiber.

## Trace-Multisequence Identity

Now let \(H\subset K\) be a finite evaluation set avoiding the pole locus of
\(J\), and assume \(S\subset H\) is \(J\)-saturated over a set
\(T\subset K\):

\[
        S=H\cap J^{-1}(T).
\]

Let \(w_x\in K^\times\) be amplitudes on \(S\). For \(i=0,1,2\), define fiber
trace amplitudes

\[
        A_i(t)=
        \sum_{\substack{x\in S\\J(x)=t}} w_xx^i.
\]

Define rational quotient moment sequences

\[
        m_{i,h}
        =
        \sum_{t\in T} A_i(t)t^h
        =
        \sum_{x\in S}w_xx^iJ(x)^h,
        \qquad h\ge0.
\]

If

\[
        \widetilde M_T(Y)=\prod_{t\in T}(Y-t)
        =
        Y^{j'}+\sum_{a=0}^{j'-1}\widetilde m_aY^a,
\]

then for each \(i=0,1,2\),

\[
        m_{i,h+j'}
        +
        \sum_{a=0}^{j'-1}\widetilde m_a m_{i,h+a}
        =
        0
        \qquad(h\ge0).
\]

The proof is the same as the subgroup decimated-sequence proof:

\[
\begin{aligned}
        m_{i,h+j'}
        +
        \sum_{a=0}^{j'-1}\widetilde m_a m_{i,h+a}
        &=
        \sum_{t\in T}A_i(t)t^h\widetilde M_T(t)\\
        &=0.
\end{aligned}
\]

So the Mobius quotient has the expected quotient locator, but its moments are
rational moments:

\[
        X^iJ(X)^h
        =
        X^i\frac{N(X)^h}{D(X)^h}.
\]

They are not the ordinary monomial moments \(X^r\) that appear in the usual RS
syndrome window.

## No Ordinary-Syndrome No-Loss Transfer

Let

\[
        H=\mu_n,\qquad \Omega_H(X)=X^n-1,
\]

and suppose \(D(X)=X^3-3X+1\) has no zero on \(H\). Let

\[
        \Delta=n-k
\]

be the ordinary RS syndrome-window length. Assume \(n\ge5\) and
\(\Delta\le n-3\).

The first rational Mobius quotient moments

\[
        X^iJ(X),\qquad i=0,1,2,
\]

are not recoverable from the ordinary moments

\[
        1,X,\ldots,X^{\Delta-1}
\]

uniformly for all amplitude vectors on \(H\).

### Proof

For a function \(f:H\to K\), the moment

\[
        w\mapsto \sum_{x\in H}w_xf(x)
\]

is determined, for all amplitude vectors \(w\in K^H\), by the ordinary moments

\[
        \sum_{x\in H}w_xx^r,\qquad 0\le r<\Delta,
\]

if and only if \(f\) lies in the span of the restricted monomials
\(1,X,\ldots,X^{\Delta-1}\) on \(H\). One direction is immediate. For the
other, test the alleged linear dependence on delta amplitudes at each
\(x\in H\).

Suppose \(X^iJ(X)\) were recoverable for some \(0\le i\le2\). Then there
would be a polynomial \(P\) with \(\deg P<\Delta\) such that

\[
        P(x)=\frac{x^iN(x)}{D(x)}
        \qquad(x\in H).
\]

Equivalently,

\[
        D(x)P(x)-x^iN(x)=0
        \qquad(x\in H),
\]

so

\[
        X^n-1\mid D(X)P(X)-X^iN(X).
\]

But

\[
        \deg(DP)\le 3+(\Delta-1)=\Delta+2\le n-1
\]

and

\[
        \deg(X^iN)\le i+2\le4\le n-1.
\]

Thus \(D(X)P(X)-X^iN(X)\) has degree \(<n\). Divisibility by \(X^n-1\) forces
the polynomial identity

\[
        D(X)P(X)=X^iN(X).
\]

This is impossible because \(D(0)=1\) and \(D(1)=-1\), so \(D\) is coprime to
\(X^iN(X)=X^iX(X-1)\). Hence the rational moment is not in the ordinary
syndrome span.

## Consequence

The subgroup quotient proof cannot be imported at no loss:

\[
        X^c(X^d)^h=X^{c+dh}
\]

has no Mobius analogue inside the ordinary monomial window.

Therefore the Mobius \(C_3\) packet is neither a quotient-free residual
counterexample nor an already-charged subgroup quotient. It is a rational
quotient test case. A correct reserve theorem must add one of:

1. a rational-function syndrome formalism;
2. an explicit denominator-cost term;
3. a special identity proving that the missing rational moments are not needed
   for the particular support and amplitude class.

## Compact Tracker Entry

1. **Target name:** `L-MOBIUS-C3-RATIONAL-QUOTIENT-AUDIT`.
2. **Baseline from Papers A-D:** subgroup-power quotient reserves are known;
   arbitrary rational quotients are not part of the current ordinary-syndrome
   reduction.
3. **What is already known:** exact subgroup decimated multisequence reduction,
   low-defect subgroup quotient closure, and robustly aperiodic L1 target.
4. **What is new if proved:** not a new final theorem; this note proves the
   first false line in the no-loss rational-quotient import.
5. **Current status:** PROVED / ROUTE_CUT / AUDIT.
6. **First possible fatal line:** "Mobius quotient moments are ordinary RS
   syndrome moments at no reserve cost."
7. **Latest useful evidence:** exact defect factorisation, trace-multisequence
   identity, and no ordinary-syndrome recovery proof above.
8. **Failed approaches:** bounded per-fiber puncture as bounded total defect;
   direct no-loss import from \(X\mapsto X^d\) quotient moments.
9. **Next exact lemma or construction:** either
   `L-RATIONAL-SYNDROME-QUOTIENT-RESERVE` with denominator cost, or
   `KILL-C3-AS-ORDINARY-L1-QUOTIENT-RESIDUAL`.
10. **Decision:** merge compactly as a reusable route cut; do not dispatch
    broad Pro rounds until the next target is one of the two exact statements
    above.
