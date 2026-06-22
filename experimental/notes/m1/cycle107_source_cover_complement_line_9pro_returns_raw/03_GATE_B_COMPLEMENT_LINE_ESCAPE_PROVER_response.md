# 03_GATE_B_COMPLEMENT_LINE_ESCAPE_PROVER Final Visible Assistant Response

URL: https://chatgpt.com/c/6a3871f5-fdb0-83ec-ac8e-f7d361bb6470
Title: RS-MCA Wall Problem
Status: FINAL_CAPTURED
Completion: FINAL_LABELED
Label: BANKABLE_LEMMA
Extracted: 2026-06-22T00:10:45.826Z

BANKABLE_LEMMA

A full Gate B proof is not obtained. The packet never defines AP_corr, so the decisive implication remains unprovable from the supplied hypotheses:

AP
corr
	​

(
U
)⟹some bounded-degree separator is nonzero on L
U
	​

.

What can be banked is an exact polynomial family, an exact degree choice, a canonical minor certificate, and a sharper necessary counterpacket mechanism.

1. Exact exceptional-closure equations

Write

Q
T
	​

(X)=
x∈T
∏
	​

(1−xX)=1+
j=1
∑
m
	​

q
j
	​

(T)X
j
,∣T∣=m,

and

M
m
(d)
	​

={(q
1
	​

(T),…,q
d
	​

(T)):T⊆H, ∣T∣=m}.

For full coordinates Z
1
	​

,…,Z
m
	​

, define h
r
	​

(Z) by

(1+Z
1
	​

X+⋯+Z
m
	​

X
m
)
−1
=
r≥0
∑
	​

h
r
	​

(Z)X
r
.

Equivalently,

h
0
	​

=1,h
r
	​

=−
i=1
∑
min(r,m)
	​

Z
i
	​

h
r−i
	​

.

Then the full m-subset locus is exactly the radical zero set of

h
n−m+1
	​

=⋯=h
n−1
	​

=0,h
n
	​

=1.
(1)
Proof

For Q
T
	​

, let

R
T
	​

(X)=
x∈H∖T
∏
	​

(1−xX).

Since Q
T
	​

R
T
	​

=1−X
n
,

Q
T
−1
	​

=
1−X
n
R
T
	​

	​

.

Because degR
T
	​

=n−m, this gives

h
n−m+1
	​

(Q
T
	​

)=⋯=h
n−1
	​

(Q
T
	​

)=0,h
n
	​

(Q
T
	​

)=1.

Conversely, suppose Q=1+∑
j=1
m
	​

Z
j
	​

X
j
 satisfies (1), and put

R(X)=
r=0
∑
n−m
	​

h
r
	​

(Z)X
r
.

The inverse-series recurrence gives

QR=1−X
n
.

Indeed, coefficients through degree n−m are those of QQ
−1
=1; the intervening coefficients vanish by (1); and the X
n
-coefficient is −h
n
	​

=−1. Since X
n
−1 is separable and splits over the field, Q is the product of exactly m distinct factors 1−xX, x∈H.

Thus the projected ideal defining M
m
(d)
	​

 is

J
m,d
	​

=
⟨h
n−m+1
	​

,…,h
n−1
	​

,h
n
	​

−1⟩
	​

∩F
p
	​

[Z
1
	​

,…,Z
d
	​

].
(2)

If d>m, one additionally imposes Z
m+1
	​

=⋯=Z
d
	​

=0.

This gives a non-enumerative structural definition of the subset layer.

2. The exact bounded-degree exceptional closure

Let

P
D
	​

=F
p
	​

[Y
1
	​

,…,Y
d
	​

]
≤D
	​

,

and define the degree-D relation space

I
m,D
	​

={F∈P
D
	​

:F(y)=0 for every distinct y∈M
m
(d)
	​

}.

The exceptional closure is

E
m,D
	​

=Z(I
m,D
	​

).
(3)

This uses distinct points of M
m
	​

, not the number of subset witnesses mapping to each point.

Let B
D
	​

={Y
α
:∣α∣≤D}. Define the evaluation matrix

A
m,D
	​

(y,α)=y
α
,y∈M
m
(d)
	​

, α∈B
D
	​

.
(4)

Then coefficient vectors of polynomials in I
m,D
	​

 are exactly

kerA
m,D
	​

.

For V=∑
j=0
d
	​

v
j
	​

X
j
, v
0
	​

=1, define

L
V
	​

(t)=(v
1
	​

−t, v
2
	​

−tv
1
	​

,…,v
d
	​

−tv
d−1
	​

).

Define the restriction matrix

B
D
	​

(V)
ℓ,α
	​

=[t
ℓ
]
j=1
∏
d
	​

(v
j
	​

−tv
j−1
	​

)
α
j
	​

,0≤ℓ≤D.
(5)

Explicitly,

B
D
	​

(V)
ℓ,α
	​

=(−1)
ℓ
r
1
	​

+⋯+r
d
	​

=ℓ
0≤r
j
	​

≤α
j
	​

	​

∑
	​

j=1
∏
d
	​

(
r
j
	​

α
j
	​

	​

)v
j
α
j
	​

−r
j
	​

	​

v
j−1
r
j
	​

	​

.
(6)

The exact criterion is

L
V
	​

⊆E
m,D
	​

⟺B
D
	​

(V)kerA
m,D
	​

=0⟺rowB
D
	​

(V)⊆rowA
m,D
	​

.
(7)

This is the precise form of the Cycle106 rank criterion.

3. Canonical eliminant minors

Let r=rankA
m,D
	​

. Choose r independent rows and pivot columns J so that the corresponding square matrix A
I,J
	​

 has nonzero determinant.

For 0≤ℓ≤D and every nonpivot monomial column β∈
/
J, define

R
ℓ,β
	​

(V)=det(
A
I,J
	​

B
D
	​

(V)
ℓ,J
	​

	​

A
I,β
	​

B
D
	​

(V)
ℓ,β
	​

	​

).
(8)

Then

L
V
	​


⊆E
m,D
	​

⟺∃ℓ,βR
ℓ,β
	​

(V)

=0.
(9)

If R
ℓ,β
	​

(V)

=0, the cofactor vector of (8) gives an explicit polynomial

F
ℓ,β
	​

∈I
m,D
	​


for which

F
ℓ,β
	​

(L
V
	​

(t))

≡0.

Consequently,

#{t∈F
p
	​

:L
V
	​

(t)∈M
m
(d)
	​

}≤D.
(10)

Each R
ℓ,β
	​

 has degree at most D in v
1
	​

,…,v
d
	​

.

Since

V=
U
−1
(modX
d+1
),

each v
j
	​

 has weighted degree j in u
1
	​

,…,u
j
	​

. Hence

deg
U
	​

R
ℓ,β
	​

≤dD.
(11)

Over a finite field, combining the disjunction in (9) into an untagged scalar by summing squares is unsafe. A canonical single tagged eliminant is

R
m,D
	​

(
U
;Z)=
ℓ,β
∑
	​

Z
ℓ,β
	​

R
ℓ,β
	​

(V(
U
)).
(12)

Then

R
m,D
	​

(
U
;Z)

≡
Z
	​

0

is exactly the required rank-escape condition.

4. Exact polynomial degree supplied by the reserve

Put

q
∗
	​

=⌈2
n/d
⌉,D
∗
	​

=d(q
∗
	​

−1).
(13)

The box monomials

Y
α
,0≤α
j
	​

<q
∗
	​

,

number q
∗
d
	​

, and all have total degree at most D
∗
	​

. Moreover,

q
∗
d
	​

≥2
n
>(
m
n
	​

)≥∣M
m
(d)
	​

∣.

Therefore I
m,D
∗
	​

	​


=0.

If the missing corrected-reserve statement contains an absolute constant c>0 such that

d≥c
log
2
	​

n
n
	​

,
(14)

then

D
∗
	​

<d2
n/d
≤n
1+1/c
.
(15)

Thus D
∗
	​

=n
O(1)
, with exponent independent of s, k, and m=n−s.

This proves existence of bounded-degree relations. It does not prove that one of them is nonzero on L
V
	​

.

5. The exact missing AP implication

The unresolved statement is now the finite polynomial assertion

AP
corr
	​

(
U
)⟹∃0≤ℓ≤D
∗
	​

, β∈
/
J:R
ℓ,β
	​

(V(
U
))

=0.
	​

(16)

Equivalently, AP_corr must rule out a signed cubature certificate. Namely, line containment is equivalent to the existence, for every 0≤ℓ≤D, of weights λ
ℓ,y
	​

 satisfying

[t
ℓ
]F(L
V
	​

(t))=
y∈M
m
(d)
	​

∑
	​

λ
ℓ,y
	​

F(y)for every F∈P
D
	​

.
(17)

Thus the exact obstruction is not merely an actual periodic witness family. It can be a low-degree signed pseudodistribution supported on all of M
m
	​

. A definition of AP_corr that only forbids stabilizers or coset swaps does not visibly exclude (17).

The packet supplies no axioms for AP_corr, so item (16) cannot currently be proved or disproved.

6. A sharper direct-count route: RS-dual weighted trades

There is a second exact reduction which bypasses the stronger separator requirement.

For an active pair (t,T), let

P
j
	​

(T)=
x∈T
∑
	​

x
j
.

From

Q
T
	​

(X)≡(1−tX)V(X)(modX
d+1
)

and logarithmic differentiation,

P
j
	​

(T)=a
j
	​

+t
j
,a
j
	​

=j[X
j
]log
U
,1≤j≤d.
(18)

Take distinct active values t
1
	​

,…,t
L
	​

, and choose exactly one complement witness T
i
	​

 for each. Let

Z
i,x
	​

=1
x∈T
i
	​

	​


be the L×n incidence matrix. Let

C
H
	​

=(x
j
)
x∈H
0≤j≤d
	​

	​

,W
Θ
	​

=(t
i
j
	​

)
1≤i≤L
0≤j≤d
	​

	​

.

With a
0
	​

=m−1, equation (18) gives

ZC
H
	​

=1(a
0
	​

,a
1
	​

,…,a
d
	​

)+W
Θ
	​

.
(19)

For 1≤m≤n−1, m

=0 in F
p
	​

, and

1=
m
1
	​

Z1
n
	​

.

Hence

colW
Θ
	​

⊆colZ.
(20)

Therefore any weighted support trade

c
⊤
Z=0
(21)

automatically satisfies

i
∑
	​

c
i
	​

t
i
j
	​

=0,0≤j≤d.
(22)

Because the t
i
	​

 are distinct, the Vandermonde matrix implies that every nonzero c satisfying (22) has support at least d+2.

If L>n, the incidence rows are dependent. Taking a minimal circuit produces

d+2≤r≤n+1
(23)

distinct active values and nonzero coefficients c
1
	​

,…,c
r
	​

 such that

i=1
∑
r
	​

c
i
	​

1
T
i
	​

	​

=0coordinatewise on H,
(24)

and

i=1
∑
r
	​

c
i
	​

t
i
j
	​

=0,0≤j≤d.
(25)

This is an exact necessary counterpacket mechanism: an RS-dual weighted Boolean trade.

The precise next lemma that would give a direct n-bound is:

\boxed{ \begin{minipage}{0.88\linewidth} \textbf{L-CYCLE107-APERIODIC-RS-DUAL-TRADE-EXCLUSION.} Under \(AP_{\rm corr}(\widehat U)\), no family of distinct external active pairs admits a circuit satisfying (23)--(25), unless that circuit belongs to a periodic, quotient, coset-swap, or separately charged contained branch. \end{minipage} } \tag{26}

If (26) is proved, then

#{distinct external active t}≤n.

This would prove the desired numerator bound directly, although it would not by itself prove literal bounded-degree closure escape.

7. The claimed “equivalence” needs correction

The implications are

L
V
	​


⊆E
m,D
	​

⟹#(L
V
	​

∩M
m
	​

)≤D.

The converse is false.

For example, over F
5
	​

, let

S={(0,0),(1,1),(2,4)}⊂A
2
.

No nonzero linear polynomial vanishes on all three noncollinear points, so the degree-one exceptional closure is all of A
2
. Every line is therefore contained in that degree-one closure, while a line such as x=3 has zero intersections with S.

Thus Gate B rank escape is a sufficient mechanism for the numerator bound, not an equivalent reformulation of the numerator bound.

8. Endpoint correction

For d=n, ordinary complement duality must be replaced by

Q
T
	​

(X)≡(1−X
n
)(1−tX)V(X)(modX
n+1
).
(27)

Hence the corrected affine coordinates are

L
j
	​

(t)=v
j
	​

−tv
j−1
	​

,1≤j<n,

and

L
n
	​

(t)=v
n
	​

−tv
n−1
	​

−1.
(28)

In the banked bandwidth parameterization,

d=n,s=σ+k=(n−1)+k,k≥1,s≤n

forces k=1, s=n, and m=0. Thus M
0
	​

 is a singleton and the first coordinate already determines at most one active t. The endpoint contributes at most one distinct value and should be charged separately rather than routed through the central Gate B argument.

9. Exact checker and counterpacket classification

The next checker should output both actual incidence and rank saturation:

Input:
    p,n,m,d,Uhat
    explicit AP_corr adapter
    D = d(ceil(2^(n/d))-1)

Construct:
    distinct M_m points
    A_{m,D}
    B_D(V)
    C_D(V) = B_D(V) * basis(ker A_{m,D})
    radical univariate active eliminant P_{m,V}(T)

Output:
    rank_escape = (C_D(V) != 0)
    one nonzero pivot minor R_{ell,beta}, if present
    one cofactor separator F, if present
    distinct active roots
    distinct external active roots
    degree of the radical eliminant

The decisions are exact:

C_D(V) != 0:
    Gate B finite certificate; active count <= D.

C_D(V) = 0 but deg P_{m,V} <= D:
    separator route is too strong for this instance;
    not a numerator counterpacket.

C_D(V) = 0 and a growing AP_corr-valid family has
super-polynomially many external roots of P_{m,V}:
    source-valid COUNTERPACKET.

AP_corr-valid weighted trade (23)-(25):
    exact obstruction packet for the direct rank route.

The eliminant must be radical, or its roots explicitly deduplicated. Algebraic multiplicity and multiple subset completions must not be reported as distinct slopes.

Self-audit

1. Exact implication proved and not proved.
Proved: equations (1)–(12), the polynomial degree calculation (13)–(15), the separator implication (10), endpoint correction (27)–(28), and the weighted-trade necessity (23)–(25). Not proved: (16), namely AP_corr ⇒ rank escape, and not proved: trade exclusion (26).

2. Prize relevance.
This is a bankable local M1 algebraic reduction and checker specification. It is not an official-prize proof or source-valid counterpacket.

3. First possible failure line.
The first failure is exactly

AP
corr
	​

(
U
)⟹∃ℓ,β R
ℓ,β
	​

(V(
U
))

=0.

The packet does not define AP_corr, and ordinary witness aperiodicity does not automatically exclude the signed cubature certificates (17).

4. Field ledger.
q_gen, q_line, q_code, q_chal, and the 2
−128
 target are not used. No probability denominator or protocol transfer is asserted. They first become relevant after Gate A and the M1 numerator theorem are merged into the official challenge-field ledger.

5. Quotient, periodic, collision, and normalization effects.
Periodic or quotient structure may cause minor vanishing or weighted trades and must be excluded or charged by Gate A/AP_corr. Multiple witnesses at one t do not increase the numerator. Same-slope collisions are deduplicated. Affine normalization that identifies slopes can only reduce a count taken before normalization, but exact agreement with the official numerator remains a Gate A obligation.

6. Exact theorem converting this to a proof.
The literal Gate B theorem is (16). A potentially stronger and more source-interpretable alternative is the weighted-trade exclusion theorem (26), which would directly give at most n distinct external active values.
