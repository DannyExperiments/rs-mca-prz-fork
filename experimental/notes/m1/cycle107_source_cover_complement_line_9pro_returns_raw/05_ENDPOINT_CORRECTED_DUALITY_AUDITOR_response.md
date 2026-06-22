# 05_ENDPOINT_CORRECTED_DUALITY_AUDITOR Final Visible Assistant Response

URL: https://chatgpt.com/c/6a3871fe-8954-83ec-9c9d-932f1396da91
Title: RS-MCA Problem Solving
Status: FINAL_CAPTURED
Completion: FINAL_LABELED
Label: BANKABLE_LEMMA
Extracted: 2026-06-22T00:10:46.968Z

BANKABLE_LEMMA

Endpoint-corrected complement-line theorem

Let d=σ+1, s=σ+k, m=n−s, with k≥1 and s≤n. Work in

R
d
	​

=F[X]/(X
d+1
),

and suppose H=μ
n
	​

⊂F
×
, so

x∈H
∏
	​

(1−xX)=1−X
n
.

For E⊆H, write

P
E
	​

(X)=
x∈E
∏
	​

(1−xX),

and let M
t
(d)
	​

 be the set of coefficient vectors

([X]P
E
	​

,…,[X
d
]P
E
	​

),∣E∣=t.

Let
U
(0)=1, and define

A
θ
	​

(X)=(1−θX)
−1
U
(X)∈R
d
	​

.

The Cycle105 activity predicate is

θ active⟺A
θ
	​

=P
S
	​

 in R
d
	​

for some ∣S∣=s.

Define the corrected complement involution

C
d
	​

(A):=(1−X
n
)A
−1
(modX
d+1
).

Then:

C
d
	​

(P
S
	​

)=P
H∖S
	​

	​


and therefore C
d
	​

 is a well-defined involutive bijection

M
s
(d)
	​

⟷M
n−s
(d)
	​

.

Now set

V
(X):=(1−X
n
)
U
(X)
−1
(modX
d+1
)=
j=0
∑
d
	​

v
j
	​

X
j
,
v
0
	​

=1.

The exact all-range complement-line normal form is

θ active⟺(
v
j
	​

−θ
v
j−1
	​

)
j=1
d
	​

∈M
m
(d)
	​

.
	​


The parametrization is injective because its first coordinate is

v
1
	​

−θ.

Thus the incidence count is already a count of distinct θ, not witness multiplicity.

Proof

For S⊆H, with T=H∖S,

P
S
	​

P
T
	​

=1−X
n

as an exact polynomial identity. Since every series involved has constant coefficient 1, it is a unit in R
d
	​

, and hence

P
T
	​

=(1−X
n
)P
S
−1
	​

=C
d
	​

(P
S
	​

).

Moreover,

C
d
	​

(C
d
	​

(A))=(1−X
n
)((1−X
n
)A
−1
)
−1
=A.

So the corrected complement map is an involution, including at the endpoint.

For the activity object,

A
θ
−1
	​

=
U
−1
(1−θX).

Consequently,

C
d
	​

(A
θ
	​

)=(1−X
n
)
U
−1
(1−θX)=(1−θX)
V
.

Its X
j
-coefficient is

v
j
	​

−θ
v
j−1
	​

.

Thus A
θ
	​

=P
S
	​

 for an s-subset S if and only if

C
d
	​

(A
θ
	​

)=P
H∖S
	​


for an m-subset, which is exactly the displayed corrected-line condition. Applying the involution gives the converse, so this is a genuine equivalence.

Exact endpoint/non-endpoint split

The source constraints imply

1≤d=σ+1≤s≤n.

There are exactly two cases.

1. Non-endpoint range
d<n⟺σ+2≤n.

Here X
n
=0 in R
d
	​

, so

1−X
n
=1

and

V
=
U
−1
=V.

Therefore the existing Cycle106 formula is correct:

θ active⟺(v
j
	​

−θv
j−1
	​

)
j=1
d
	​

∈M
m
	​

.

Equality σ+2=n is still non-endpoint: the modulus is X
n
, so the term X
n
 vanishes.

2. Endpoint range
d=n⟺σ+1=n.

Now the modulus is X
n+1
, so X
n
 survives. If

V=
U
−1
=
j=0
∑
n
	​

v
j
	​

X
j
,

then

V
=(1−X
n
)V=V−X
n
(modX
n+1
),

because v
0
	​

=1. Hence

v
j
	​

=v
j
	​

(0≤j<n),
v
n
	​

=v
n
	​

−1.

The endpoint line is therefore

θ active⟺(v
1
	​

−θ,v
2
	​

−θv
1
	​

,…,v
n−1
	​

−θv
n−2
	​

,v
n
	​

−θv
n−1
	​

−1)∈M
m
	​

.
	​


Equivalently, the uncorrected line must meet

M
m
	​

+e
n
	​

,

not M
m
	​

.

Indeed, at d=n,

(1−X
n
)
−1
=1+X
n
(modX
n+1
),

and therefore

P
S
−1
	​

=(1+X
n
)P
T
	​

=P
T
	​

+X
n
(modX
n+1
).

This proves that the ordinary endpoint formula is not merely unproved; it is false as stated.

For example, taking S=H,

P
S
	​

=1−X
n
,P
T
	​

=1.

The ordinary inverse is 1+X
n
, whereas the corrected inverse is 1.

Official M1 endpoint is automatically trivial

In the official bandwidth parametrization,

s=σ+k,k≥1,s≤n.

If σ+1=n, then

s=n−1+k≤n,

forcing

k=1,s=n,m=0.

Thus the only official endpoint support is S=H, and

M
0
(n)
	​

={(0,…,0)}.

The corrected condition becomes

v
j
	​

−θ
v
j−1
	​

=0(1≤j≤n).

The first equation forces

θ=
v
1
	​

,

so there is at most one active parameter:

#Θ
endpoint
	​

(
U
)≤1.
	​


More explicitly,

Θ
endpoint
	​

(
U
)={θ:
U
(X)=(1−θX)(1−X
n
)(modX
n+1
)},

and this set has cardinality 0 or 1.

This bound is total, so it also bounds the external-θ numerator.

Gate A disposition

Gate A should charge the endpoint separately, rather than require endpoint objects to satisfy AP
corr
	​

.

The exact branch should be:

⎩
⎨
⎧
	​

σ+1=n:
σ+2≤n:
	​

k=1, s=n,N
endpoint
	​

(
U
)≤1;
invoke the official bad-slope-to-AP
corr
	​

(
U
) source cover.
	​


This is preferable to putting the endpoint through AP
corr
	​

, because the endpoint object contains the full factor 1−X
n
 and may be rejected as periodic or structured. Rejecting it without the explicit ≤1 charge would create a real numerator gap.

The endpoint may alternatively be routed to the already banked bandwidth-1 Cycle103 branch, but the exact ≤1 charge is stronger.

Gate B disposition

In the non-endpoint range, Gate B does not change.

At the endpoint, replace V by

V
=(1−X
n
)V

or, equivalently, subtract 1 from the final line coordinate.

The eliminant framework itself is unchanged: this is a fixed affine translation in the final coordinate and does not increase separator degree.

For the actual official endpoint m=0, Gate B is automatic at degree 1. The polynomial

F(Y
1
	​

,…,Y
n
	​

)=Y
1
	​


vanishes on M
0
	​

={0}, while on the corrected line

F(L
U
corr
	​

(T))=
v
1
	​

−T

has nonzero T-coefficient −1. Thus the line always escapes the degree-1 closure. One may take the endpoint escape certificate to be the constant

R
endpoint
	​

≡1.

No aperiodicity hypothesis is needed.

Exact replacement theorem for the board

Replace the ordinary complement-line statement by:

L-CYCLE107-ENDPOINT-CORRECTED-COMPLEMENT-LINE.
Let d=σ+1≤n, s=σ+k≤n, m=n−s, k≥1, and
U
(0)=1. Define

V
=(1−X
n
)
U
−1
(modX
d+1
)=
j=0
∑
d
	​

v
j
	​

X
j
.

Then for every θ,

θ active⟺(
v
j
	​

−θ
v
j−1
	​

)
j=1
d
	​

∈M
n−s
(d)
	​

.

If d<n, this is the ordinary Cycle106 line. If d=n, then necessarily k=1,s=n,m=0, and the active set has size at most 1.

Checker repair

For 03_cycle106_complement_line_eliminant_check.py, the essential patch is:

Python
Run
# Old:
if not (1 <= d < n):
    ...

# New:
if not (1 <= d <= n):
    ...

v = inverse_prefix(uhat, d, p)

# Endpoint correction:
if d == n:
    v[d] = (v[d] - 1) % p

The existing line-restriction and rank code can then remain unchanged.

For the complement branch of 07_cycle106_kfree_stress_checker.py, replace

(1−θX)P
T
−1
	​


by

(1−θX)(1−X
n
)P
T
−1
	​


before truncation.

I also produced an exhaustive finite checker implementing both ranges:

Endpoint-corrected duality checker

For p=7,n=3,σ=2,s=3, it checked all 7
3
=343 normalized prefixes: the corrected equivalence passed, the maximum active count was 1, and the ordinary formula disagreed on 14 prefixes. This is only a checker receipt; the theorem above is proved algebraically.

Exact next lemma toward the full solve

The endpoint is no longer part of the live wall. The next source theorem should be explicitly restricted to the interior:

L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER-INTERIOR
	​


Its input must require

σ+2≤n,

and it must prove that every uncharged official residual bad slope maps injectively, or with an exact multiplicity ledger, to a distinct θ satisfying

A
θ
	​

∈M
s
	​

andAP
corr
	​

(
U
).

Only after that theorem is established does the remaining hard implication become

AP
corr
	​

(
U
)⟹R
m,D
	​

(
U
)

=0

for the ordinary non-endpoint line.

Self-audit

Proved: the corrected complement involution, the corrected affine-line equivalence for every official source range, the exact endpoint shift, and the official endpoint bound #Θ≤1.
Not proved: the official non-endpoint source cover, the definition or satisfaction of AP
corr
	​

, or non-endpoint complement-line rank escape.

This is theorem-level and official-prize-relevant as a repair to the M1 chain. It is not a prize-level result and does not close Gate A or Gate B.

After this repair, the first unsupported line is

official non-endpoint residual bad slope⟹AP
corr
	​

(
U
) with exact distinct-numerator preservation.

Conditional on that, the next possible failure is AP
corr
	​

⇒R
m,D
	​


=0.

q
gen
	​

,q
line
	​

,q
code
	​

,q
chal
	​

, and the 2
−128
 target are not used. This is a deterministic single-field algebraic statement.

Witness multiplicity, quotient structure, periodic structure, and contained supports do not alter the proved normalized equivalence. The line is injective in θ. At the endpoint the total count is at most one. Non-endpoint periodic/quotient containment remains a possible Gate B obstruction, and affine normalization of official slopes remains part of the unproved Gate A transfer.

This is not a plan. To convert the full M1 route into PROOF, the exact remaining requirements are the interior source-cover theorem above and the non-endpoint AP
corr
	​

-to-rank-escape theorem.
