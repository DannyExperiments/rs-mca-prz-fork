BANKABLE_LEMMA

## Verdict

No source-valid proof or asymptotic counterpacket follows yet. There is, however, a strict (k)-independent reduction to a smaller rank-one locator-jet theorem, together with an exhaustive bounded checker.

The exact route to a full proof is:

[
\text{source aperiodicity}
\Longrightarrow
\text{aperiodic rank-one locator-jet cap}
\Longrightarrow
|\Gamma\cap M_s|\le n^{O(1)}.
]

The previous failed Fable run is not used.

## 1. Exact dephased rank-one reduction

Put

[
d=\sigma+1,\qquad r=\sigma+2,
\qquad H=\mu_n\subset\mathbb F_p^\times,
]

and for (S\subset H),

[
g_S(X)=\prod_{x\in S}(1-xX).
]

Write

[
\widehat U(X)=1+u_1X+\cdots+u_dX^d\pmod{X^r}.
]

The banked Cycle105 equivalence is

[
\theta\text{ active with witness }S
\iff
\widehat U(X)\equiv(1-\theta X)g_S(X)\pmod{X^r}.
\tag{1}
]

This is the k-free collapse underlying the current wall. 

### Pair-fiber hash

Define

[
\Phi_s(\theta,S)
================

\big[(1-\theta X)g_S(X)\big]_{<r}.
]

Then, exactly,

[
\Theta_s(\widehat U)
====================

\pi_\theta\big(\Phi_s^{-1}(\widehat U)\big).
\tag{2}
]

If (g_S(X)=\sum a_jX^j), the hash key is

[
u_0=1,\qquad
u_j=a_j-\theta a_{j-1},\quad 1\le j\le d.
\tag{3}
]

Thus an exact all-(\widehat U) finite scan requires

[
p\binom ns
]

pair records, not enumeration of (p^d) possible prefixes.

Now let (T=H\setminus S), with (m=n-s). Since

[
g_S(X)g_T(X)=1-X^n\equiv1\pmod{X^r},
]

provided (r\le n), (1) becomes

[
\widehat U(X)
\equiv
(1-\theta X)g_T(X)^{-1}
\pmod{X^r}.
\tag{4}
]

Hence the exact all-(\widehat U) scan may use whichever layer is smaller:

[
p\binom{n}{\min(s,n-s)}.
\tag{5}
]

This is already a substantial computational reduction.

### Dephasing around one incidence

Fix one active complement witness ((\theta_0,T_0)), and write

[
h_0=g_{T_0}.
]

Then

[
\widehat U=(1-\theta_0X)h_0^{-1}\pmod{X^r}.
]

For another (m)-subset (T), define

[
B_T(X)=(1-\theta_0X)g_T(X)-h_0(X)\pmod{X^r}.
\tag{6}
]

Let

[
\lambda_T=[X]B_T.
]

Then:

[
T\text{ is active}
\iff
[X^j]B_T
========

\lambda_T[X^{j-1}]h_0,
\qquad 2\le j\le r-1.
\tag{7}
]

When (7) holds, its active value is

[
\theta_T=-\lambda_T.
\tag{8}
]

Indeed, activity is equivalent to

[
(1-\theta_0X)g_T=(1-\theta_TX)h_0\pmod{X^r},
]

so

[
B_T=-\theta_TXh_0.
]

Conversely, (7) says exactly that (B_T=\lambda_TXh_0), giving (\theta_T=-\lambda_T).

This is the strict smaller wall: after selecting one base incidence, (\widehat U) disappears and all other incidences are rank-one conditions on locator jets.

## 2. Exact local-exchange checker

Fix a direct active pair ((\theta_0,S_0)). Write every candidate support as

[
S=(S_0\setminus B)\cup A,
]

where

[
B\subset S_0,\qquad
A\subset H\setminus S_0,\qquad
|A|=|B|=q.
]

Canceling the common locator factor in (1) gives

[
(1-\theta_0X)g_B(X)
\equiv
(1-\phi X)g_A(X)
\pmod{X^r}.
\tag{9}
]

The coefficient of (X) determines the candidate readout without looping over (\phi):

[
\boxed{
\phi=\theta_0+\sum_{b\in B}b-\sum_{a\in A}a.
}
\tag{10}
]

A bounded exchange scan therefore checks exactly

[
\sum_{q=0}^{q_{\max}}
\binom sq\binom{n-s}{q}
\tag{11}
]

records. For

[
q_{\max}=\min(s,n-s),
]

this is exhaustive for the fixed (\widehat U).

## 3. Close collisions are completely classified

Suppose ((\theta,S)) and ((\phi,T)) are witnesses for the same (\widehat U), with (\theta\ne\phi). Put

[
C=S\cap T,\qquad
A=S\setminus T,\qquad
B=T\setminus S,\qquad
q=|A|=|B|.
]

After canceling (g_C),

[
(1-\theta X)g_A(X)
\equiv
(1-\phi X)g_B(X)
\pmod{X^r}.
\tag{12}
]

If (q\le\sigma), both sides have degree at most

[
q+1\le\sigma+1=r-1.
]

Thus (12) is equality as polynomials. Unique factorization, (A\cap B=\varnothing), and (\theta\ne\phi) force

[
q=1,\qquad
A={\phi},\qquad
B={\theta},\qquad
\theta,\phi\in H.
\tag{13}
]

Therefore every close distinct-(\theta) collision is exactly a contained delete-one packet:

[
R\subset H,\quad |R|=s+1,\qquad
S_\theta=R\setminus{\theta},\qquad
\widehat U=g_R.
\tag{14}
]

It contributes at most (s+1\le n) active values.

Consequently, any two distinct **external** witnesses satisfy

[
\boxed{|S\setminus T|\ge\sigma+1.}
\tag{15}
]

In complement notation the same bound is

[
|T\setminus T'|\ge r-1.
]

### Exact packing consequences

Choose one support for each external active (\theta), and let their number be (L). Since (k=s-\sigma), (15) implies that no (k)-subset lies in two chosen supports. Hence

[
\boxed{
L\binom sk\le\binom nk.
}
\tag{16}
]

For complement size (m=n-s):

* if (m\le\sigma), then (L\le1);
* if (m>\sigma), putting (q=m-\sigma),

[
\boxed{
L\binom mq\le\binom nq.
}
\tag{17}
]

These bounds close the extreme layers. They remain exponential in the central constant-rate regime, so they are not the final theorem.

## 4. Literal periodic/coset-swap packets cannot enlarge the numerator

Let (K<H) be a nontrivial subgroup of order (M). Suppose two equal-size supports (S,T) have

[
1_S-1_T
]

constant on each (K)-coset.

After canceling common points, (S\setminus T) and (T\setminus S) are unions of complete (K)-cosets. For a coset (yK),

[
\prod_{x\in yK}(1-xX)=1-y^MX^M.
\tag{18}
]

Since (M\ge2), the residual locator polynomials have zero linear coefficient. The common-(\widehat U) equation

[
(1-\theta X)g_{S\setminus T}
============================

(1-\phi X)g_{T\setminus S}
\pmod{X^r}
]

then yields, from the coefficient of (X),

[
\boxed{\theta=\phi.}
\tag{19}
]

Thus literal whole-coset swaps may create many witnesses for one (\theta), but they cannot create more distinct active values. They are not counterpackets for the requested numerator.

This is stronger than merely filtering periodic families: it proves that this specific periodic mechanism is numerator-harmless.

## 5. Naive tensor inflation is impossible

A finite far-collision seed cannot be converted into exponentially many distinct readouts by independently multiplying a bounded number of Möbius locator ratios.

Fix (\theta_0). Suppose (t) block choices satisfy

[
R_i(X)
======

\frac{1-\theta_0X}{1-\theta_iX}
\pmod{X^r},
]

and their product is again a valid single active ratio:

[
\prod_{i=1}^tR_i(X)
===================

\frac{1-\theta_0X}{1-\theta_*X}
\pmod{X^r}.
]

Then

[
\prod_{i=1}^t(1-\theta_iX)
==========================

(1-\theta_0X)^{t-1}(1-\theta_*X)
\pmod{X^r}.
\tag{20}
]

If (t\le d), both sides have degree (t<r), so (20) is polynomial equality. Unique factorization gives

[
{\theta_1,\ldots,\theta_t}
==========================

{\theta_*,\theta_0,\ldots,\theta_0}
\tag{21}
]

as multisets.

Therefore at most one block is nontrivial. A valid counterpacket inflation must use either:

1. more than (d) nontrivial factors in one macro-step; or
2. a non-product/telescoping construction that preserves the rank-one equations.

This cuts the most obvious inflation of a small finite collision.

## 6. Exact checker specification

### Inputs

The checker accepts:

[
p,\ n,\ \sigma,\ s,
]

with

[
p\text{ prime},\qquad
n\mid p-1,\qquad
\sigma+2\le n,\qquad
\sigma+1\le s\le n.
]

It computes

[
d=\sigma+1,\qquad
r=\sigma+2,\qquad
k=s-\sigma,\qquad
H=\mu_n.
]

It has two modes.

**All-(\widehat U) mode:** no (\widehat U) input is needed. It enumerates exact pair fibers using (3) or (4).

**Local-exchange mode:** input additionally includes one active base pair

[
\theta_0,\qquad S_0\subset H,\qquad |S_0|=s,
]

and reconstructs

[
\widehat U=(1-\theta_0X)g_{S_0}\pmod{X^r}.
]

### Exact finite obstruction predicate

The supplied Cycle106 packet names “aperiodic above corrected reserve,” but does not state a formal predicate (AP_{\rm src}) or the corrected-reserve inequality. The Cycle106 prompt nevertheless requires that hypothesis rather than a generic list-size argument. 

The checker therefore uses the following exact diagnostic only:

[
AP_{\rm block}(\mathcal F,\widehat U)
]

holds when all three conditions hold:

1. **Trivial jet stabilizer**
   [
   {\zeta\in H:
   u_j\zeta^j=u_j
   \text{ for every }0\le j\le d}
   ={1}.
   ]

2. **Trivial support stabilizers**
   [
   {\zeta\in H:\zeta S=S}={1}
   ]
   for every witness support (S).

3. **No whole-coset difference**
   For every two distinct witness supports (S,T), and every proper nontrivial subgroup (K<H),
   [
   1_S-1_T
   ]
   is not constant on the (K)-cosets.

This predicate is exact, but it is not asserted to equal the missing project predicate (AP_{\rm src}).

### Output contract

Because the source gate is absent, the current checker always emits

```text
ROUTE_CUT_FINITE_MODEL_TOO_WEAK
```

as its formal decision.

It additionally records the decision that would apply after a source-valid gate is supplied:

```text
PASS_NO_SUPERPOLY_PATTERN_IN_WINDOW
```

when the exact finite maximum is below the predeclared alarm, or

```text
COUNTERPACKET_CANDIDATE
```

when an exact (AP_{\rm block}) family reaches the alarm.

### Implementable pseudocode

```text
INPUT p,n,sigma,s
d := sigma+1
r := sigma+2
H := mu_n in F_p

ALL_U_MODE:
    if s <= n-s:
        side := direct
        ell := s
    else:
        side := complement
        ell := n-s

    preflight_records := p * binom(n,ell)
    refuse if preflight_records exceeds declared bound

    table := map Uhat_prefix -> bitset of theta values

    for E in combinations(H,ell):
        J := product_{x in E}(1-xX) mod X^r

        if side == complement:
            J := inverse_series(J) mod X^r

        for theta in F_p:
            key := (1-theta X)J mod X^r
            table[key].theta_bitset.add(theta)

    rank keys by:
        number of external theta,
        then total number of theta

    for every extremal or alarm key:
        replay the layer
        reconstruct all support witnesses
        verify each equation exactly
        split theta in H from theta outside H
        verify close-collision classification
        verify whole-coset swaps imply same theta
        evaluate AP_block
        emit all theta values and all witnesses

LOCAL_EXCHANGE_MODE:
    INPUT active base theta0,S0 and qmax
    Uhat := (1-theta0 X)g_S0 mod X^r

    preflight_records :=
        sum_{q=0}^{qmax} binom(s,q)binom(n-s,q)
    refuse if preflight_records exceeds declared bound

    for q=0,...,qmax:
        for B subset S0 with |B|=q:
            for A subset H\S0 with |A|=q:
                phi := theta0 + sum(B) - sum(A)
                S := (S0\B) union A

                if (1-phi X)g_S == Uhat mod X^r:
                    record distinct pair (phi,S)

    if qmax=min(s,n-s):
        mark exhaustive_for_fixed_Uhat := true

    verify and emit as in ALL_U_MODE
```

For counterexample hunting, the first nontrivial exchange shell is

[
q=d=\sigma+1,
]

because (q<d) cannot produce two distinct external values by the close-collision theorem.

## 7. Exact finite results

### Exhaustive all-(\widehat U) window

[
(p,n,\sigma,s)=(29,7,3,4).
]

The complement layer has size (3), so the exact scan contains

[
29\binom73=1015
]

pair records and (931) distinct relevant (\widehat U)-prefixes.

Results:

[
\max_{\widehat U}|\Theta(\widehat U)|=5,
\qquad
\max_{\widehat U}|\Theta_{\rm ext}(\widehat U)|=1.
]

The five-value maximum is entirely an internal delete-one packet. Formal output:

```text
ROUTE_CUT_FINITE_MODEL_TOO_WEAK
```

Prospective source-gated output:

```text
PASS_NO_SUPERPOLY_PATTERN_IN_WINDOW
```

### Cycle102 replay

For

[
p=29,\ n=7,\ \sigma=3,\ s=4,\quad
\theta_0=2,\quad
S_0={\omega^3,\omega^4,\omega^5,\omega^6},
]

the exhaustive fixed-(\widehat U) scan checks all

[
\binom74=35
]

supports and finds exactly one external active value:

[
\Theta_{\rm ext}={2}.
]

### Exact far-collision seed

For

[
p=97,\quad n=16,\quad \sigma=2,\quad s=8,\quad k=6,
]

with (\omega=8) and base pair

[
\theta_0=13,\qquad
S_0={0,3,7,8,10,12,14,15}
]

in subgroup-exponent notation, the exhaustive scan checks all

[
\binom{16}{8}=12870
]

supports. It obtains

[
\widehat U=(1,96,86,56)
]

and

[
\Theta={13,17,27,45,54,58,77},
]

with

[
\Theta_{\rm ext}={13,17,45,54,58,77}.
]

The complete witness packet is:

| (\theta) | support exponents     |
| -------: | --------------------- |
|       13 | (0,3,7,8,10,12,14,15) |
|       17 | (0,1,2,6,7,12,13,14)  |
|       27 | (1,3,4,7,10,11,12,13) |
|       45 | (2,4,6,7,8,9,10,12)   |
|       54 | (1,3,5,8,9,11,12,15)  |
|       58 | (0,1,4,7,8,9,10,11)   |
|       77 | (4,5,8,9,11,13,14,15) |

Every witness equation verifies. The close-collision theorem verifies. The family satisfies (AP_{\rm block}): no jet stabilizer, no support stabilizer, and no whole-coset difference.

This is **not** a counterpacket because:

* (\sigma=2) is a fixed sub-reserve instance;
* the actual (AP_{\rm src}) predicate is unavailable;
* there is no reserve-preserving inflation;
* the distinct support is only six external values;
* the Möbius tensor-rigidity lemma rules out the naive bounded-factor product inflation.

It does prove that “trivial stabilizers plus no literal coset swaps” is too weak to imply uniqueness or a very small absolute cap.

## 8. Exact next lemma for a full proof

The next theorem should be:

```text
L-CYCLE106-SOURCE-APERIODIC-RANKONE-JET-CAP
```

Let (AP_{\rm src}) be the actual source predicate, and assume the exact corrected-reserve inequality. Fix an active base ((\theta_0,T_0)), put (h_0=g_{T_0}), and define

[
B_T=(1-\theta_0X)g_T-h_0\pmod{X^r}.
]

Prove that the set of external readouts

[
\left{
-[X]B_T:
\begin{array}{l}
|T|=m,\
[X^j]B_T=[X]B_T[X^{j-1}]h_0,\
2\le j\le r-1
\end{array}
\right}
\tag{22}
]

after removing or charging every source-defined quotient/configuration template, has cardinality

[
\boxed{\le n^C}
]

for an absolute (C) independent of (m,s,k).

Before (22) can be applied source-validly, one needs the exact adapter:

```text
L-CYCLE106-APERIODICITY-TRANSFER
```

which translates

[
AP_{\rm src}(\widehat U)
\quad\text{and corrected reserve}
]

into a condition on the base locator (h_0) excluding every uncharged large rank-one jet fiber.

Those two statements would prove the Cycle106 target. The first line requiring new source information is the adapter, not the algebraic reduction.

## 9. Counterpacket conversion target

A real counterpacket requires:

```text
L-CYCLE106-APERIODIC-FIBER-INFLATION
```

Construct a sequence

[
(p_i,n_i,\sigma_i,s_i,\widehat U_i)
]

such that:

1. (k_i=s_i-\sigma_i) grows;
2. the exact corrected-reserve condition holds;
3. (AP_{\rm src}(\widehat U_i)) holds;
4. the number of **distinct external** readouts satisfying the rank-one equations is superpolynomial in (n_i).

Replicating many witnesses at the same (\theta) is irrelevant. Literal coset swaps give the same (\theta), and bounded-factor independent Möbius tensoring is ruled out by (21). A plausible counterpacket must therefore use a (>d)-factor macro-gadget or an exact telescoping/Prouhet-type system.

## Self-audit

**What did I prove?**
The pair-fiber equivalence, smaller-side enumeration, dephased rank-one reduction, local exchange readout, exact close-collision classification, external petal-distance bound, extreme-layer packings, literal-coset-swap same-readout theorem, bounded-factor Möbius tensor-rigidity, and exhaustive finite certificates.

**What did I not prove?**
The formal source aperiodicity transfer, corrected-reserve applicability, the central-layer polynomial rank-one cap, or an asymptotic counterpacket.

**Prize relevance.**
The algebraic reduction is directly relevant to the official upper-side route. The finite JSON outputs are research/model certificates only. No official prize conclusion follows.

**First possible failure in the reduction chain.**
Identifying (AP_{\rm block}) with the omitted (AP_{\rm src}), or assuming the omitted corrected-reserve inequality. After a valid adapter, the next failure point is exactly theorem (22).

**Field ledgers and (2^{-128}).**
(q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and (2^{-128}) are not used. That is correct: this is a single-field structural wall, not the finite prize-frontier accounting step.

**Numerator reductions.**
Contained/internal incidences contribute at most (n). Literal periodic/coset swaps force the same (\theta). The map (\theta\mapsto\Gamma(\theta)) is injective because its first coordinate is

[
g_1(\theta)=u_1+\theta.
]

Thus same-slope collisions cannot merge different (\theta)’s. Affine color normalization is bijective and likewise cannot reduce the distinct-(\theta) numerator. More subtle nonliteral quotient/configuration trades remain precisely what the source adapter must classify.

**Confidence.**
High for the algebraic lemmas and finite certificates; unknown for the source aperiodicity transfer and central rank-one cap.

[Full mathematical report](sandbox:/mnt/data/cycle106_role07_bankable_lemma.md)
[Replayable bounded checker](sandbox:/mnt/data/cycle106_kfree_stress_checker.py)
[Exhaustive (p=29) certificate](sandbox:/mnt/data/cycle106_sample_p29_n7_s4.json)
[Cycle102 replay certificate](sandbox:/mnt/data/cycle106_cycle102_replay_p29.json)
[Exact (p=97) far-collision seed](sandbox:/mnt/data/cycle106_candidate_p97_n16_s8.json)
