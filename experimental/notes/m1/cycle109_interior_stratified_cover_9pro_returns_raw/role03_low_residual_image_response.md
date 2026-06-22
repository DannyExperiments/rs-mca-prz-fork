BANKABLE_LEMMA

1. Executive verdict

Verdict: the stated pure polynomial LOW bound is not proved, and the current reserve/list reduction cannot prove it. I proved a sharper obstruction: residue-line slicing can retain a genuine occupied-color main term

≍
q
σ−1
(
k+σ
n
	​

)
	​

in the same-field case, even after collapsing all support multiplicity at the same slope. Thus the correct LOW target is a main-term-plus-inverse/charge theorem, not an unconditional n
C
 theorem.

This is not an official counterpacket. The construction has not been shown to survive the exact source AP
corr
	​

, quotient/periodic, tangent, and affine-color charge predicates. It is, however, an official-route-relevant bankable lemma identifying the exact mechanism that any LOW proof must charge or bound.

Confidence: high in the algebraic lemma and proof; moderate in the proposed calibrated upper theorem; unknown for the missing AP
corr
	​

-to-charge implication.

The previously banked injection

∣Z
t
	​

∣≤L
K
line
	​

	​

(D;k+t,k+σ)

is correct, but the relevant agreement surplus is only σ−t. The original σ-reserve does not transfer: the residual entropy margin loses tlogq
gen
	​

, and ordinary shifted list size can be at least

⌈
q
gen
σ−t
	​

(
k+σ
n
	​

)
	​

⌉.

05_all_denominator_mca_auditor

05_all_denominator_mca_auditor

For t=1, the existing exact generalized-Jacobian analysis independently identifies the numerator as the number of occupied thickened colors, not the number of supports, and leaves precisely the quotient-conditioned color-occupancy bound open.

ROLE_05_T1_MCA_GJ_COLOR_RESULT

2. Exact theorem proved

Let K=F
q
	​

, let D⊂K have size n, and put

a=k+σ≤n,1≤t<σ,s=σ−t.

For E,N∈K[X], define

Z
t
	​

(E,N,w):=
⎩
⎨
⎧
	​

z∈K:
∃Q∈K[X]
<k+t
	​

,
agr(Q,w)≥a,
[Q]
E
	​

=z[N]
E
	​

	​

⎭
⎬
⎫
	​

.
Theorem: L-CYCLE109-LOW-RESIDUE-SLICING-RETAINS-OCCUPANCY

Assume

q−n≥t,n>k+2t−2.

Define

L
0
	​

:=⌈
q
σ−t
(
a
n
	​

)
	​

⌉

and

λ
t
	​

:=
(
t
q−n
	​

)
(
t
min{k+t−1,q−n}
	​

)
	​

.

Then there exist:

distinct β
1
	​

,…,β
t
	​

∈K∖D;

the squarefree denominator

E(X)=
i=1
∏
t
	​

(X−β
i
	​

);

N=1;

a received word w:D→K;

such that:

the direction g=−1/E has intrinsic denominator degree exactly t;

every produced slope is noncontained;

the number of distinct slopes obeys

∣Z
t
	​

(E,1,w)∣≥⌈
q
t−1
(1+λ
t
	​

(L
0
	​

−1))
L
0
	​

	​

⌉;
	​

the count is already reduced modulo all same-slope support collisions.

For t=1, assuming q−n≥k,

∣Z
1
	​

(E,1,w)∣≥
1+
q−n
k
	​

(L
0
	​

−1)
L
0
	​

	​

≥
2
1
	​

min{L
0
	​

,
k
q−n
	​

},
	​

where

L
0
	​

=⌈
q
σ−1
(
a
n
	​

)
	​

⌉.

Consequently, residue-line slicing alone does not turn the residual list obstruction into a polynomial-size image. Its natural same-field baseline has total codimension

(σ−t)+(t−1)=σ−1,

and hence scale

q
σ−1
(
a
n
	​

)
	​

.

After division by the slope field,

q
1
	​

⋅
q
σ−1
(
a
n
	​

)
	​

=
q
σ
(
a
n
	​

)
	​

,

which is exactly the occupancy/reserve scale that an MCA upper ledger must pay.

3. Proof
Step 1: a large locator-prefix fiber

For every a-subset S⊆D, let

L
S
	​

(X):=
x∈S
∏
	​

(X−x).

This is monic of degree a.

Record the first s=σ−t coefficients below the leading coefficient. There are at most q
s
 possible records. Therefore some fiber

F⊆(
a
D
	​

)

has size

L:=∣F∣≥⌈
q
s
(
a
n
	​

)
	​

⌉=L
0
	​

.

Choose S
0
	​

∈F and put M=L
S
0
	​

	​

. For every S∈F, define

Q
S
	​

:=M−L
S
	​

.

Because M and L
S
	​

 have their leading coefficient and next s coefficients in common,

degQ
S
	​

≤a−s−1.

But

a−s−1=k+σ−(σ−t)−1=k+t−1,

so

Q
S
	​

∈K[X]
<k+t
	​

.

Define

w(x):=M(x),x∈D.

For every x∈S,

Q
S
	​

(x)=M(x)−L
S
	​

(x)=M(x)=w(x).

Thus

agr(Q
S
	​

,w)≥∣S∣=a.

This recovers the exact residual-list lower mechanism, but we now retain only the residue-line image rather than counting the whole list.

Step 2: choose external residue coordinates with few collisions

Let

U:=K∖D,∣U∣=q−n.

Choose an unordered t-subset

B={β
1
	​

,…,β
t
	​

}⊂U.

Associate to S∈F the vector

v
S
	​

(B):=(Q
S
	​

(β
1
	​

),…,Q
S
	​

(β
t
	​

))∈K
t
.

For S

=T,

Q
S
	​

−Q
T
	​

=L
T
	​

−L
S
	​

is nonzero and has degree at most k+t−1. Hence it has at most

min{k+t−1,q−n}

roots in U. Therefore

B
Pr
	​

[v
S
	​

(B)=v
T
	​

(B)]≤λ
t
	​

.

The expected number of colliding pairs is at most

λ
t
	​

(
2
L
	​

).

Consequently, some choice of B has collision count

C
B
	​

≤λ
t
	​

(
2
L
	​

).

Let m
v
	​

 denote the multiplicity of vector v, and let V be the number of distinct vectors. Then

v
∑
	​

m
v
	​

=L

and

v
∑
	​

(
2
m
v
	​

	​

)=C
B
	​

.

Thus

v
∑
	​

m
v
2
	​

=L+2C
B
	​

≤L+λ
t
	​

L(L−1).

Cauchy–Schwarz gives

L
2
≤V
v
∑
	​

m
v
2
	​

,

so

V≥
1+λ
t
	​

(L−1)
L
	​

.

This is the first explicit collapse of same-slope candidates: only distinct evaluation vectors survive.

Step 3: force the vectors onto one scalar residue line

Partition the distinct vectors by their difference signatures

δ(v):=(v
2
	​

−v
1
	​

,…,v
t
	​

−v
1
	​

)∈K
t−1
.

There are at most q
t−1
 signatures. Therefore one signature class contains at least

q
t−1
V
	​

distinct vectors.

Fix such a class, with common signature

(δ
2
	​

,…,δ
t
	​

).

There is a unique polynomial R∈K[X]
<t
	​

 satisfying

R(β
1
	​

)=0,R(β
i
	​

)=−δ
i
	​

(2≤i≤t).

Replace

M⟼M+R,Q
S
	​

⟼Q
S
′
	​

:=Q
S
	​

+R,w⟼w
′
:=w+R∣
D
	​

.

Since degR<t<k+t, every Q
S
′
	​

 still has degree <k+t, and it still agrees with w
′
 on S.

For every S in the selected signature class,

Q
S
′
	​

(β
1
	​

)=Q
S
′
	​

(β
2
	​

)=⋯=Q
S
′
	​

(β
t
	​

)=:z
S
	​

.

Therefore

E∣Q
S
′
	​

−z
S
	​

,

or equivalently

[Q
S
′
	​

]
E
	​

=z
S
	​

[1]
E
	​

.

If z
S
	​

=z
T
	​

, then the two original vectors have equal first coordinate and equal difference signature, hence are equal. Since the vectors in the class were chosen distinct,

S

=T⟹z
S
	​


=z
T
	​

.

Thus the slopes are genuinely distinct in K, and support multiplicity at one slope contributes only once.

Step 4: intrinsic denominator degree

The displayed direction is

g=−
E
1
	​

.

Suppose it had a lower-degree representation on D:

−
E
1
	​

=R
0
	​

−
E
′
B
0
	​

	​

on D,

where

degR
0
	​

<k,degE
′
=u<t,degB
0
	​

<u.

Multiplying by EE
′
, the polynomial

H:=R
0
	​

EE
′
−B
0
	​

E+E
′

vanishes on all n elements of D.

Its degree satisfies

degH≤k+t+u−1≤k+2t−2<n.

Hence H=0 identically. Reducing modulo E gives

E
′
≡0(modE),

which is impossible because degE
′
<degE.

Therefore the intrinsic denominator degree is exactly t.

Step 5: automatic noncontainment

If a polynomial G∈K[X]
<k
	​

 agreed with −1/E on an a-element support, then

EG+1

would have at least a roots. But

deg(EG+1)≤k+t−1<k+σ=a.

Therefore EG+1=0, which would imply E∣1, impossible.

So every constructed witness is noncontained.

4. What this proves about the LOW route

The construction identifies the exact missing constraint count:

the shifted locator/list fiber costs only σ−t field coordinates;

requiring a t-dimensional residue to lie on one scalar line costs only t−1 further coordinates;

total cost: σ−1, not σ.

Thus a calibrated same-field LOW theorem should have the form

∣Z
t
uncharged
	​

∣≤⌈
q
σ−1
(
k+σ
n
	​

)
	​

⌉+n
C
0
	​

,
	​

or an exact effective-group analogue, with every excess over this baseline forcing an official quotient/periodic/tangent/field/affine-color charge.

The earlier audit had already concluded that a pure n
1+o(1)
 target must be replaced by a main-term-plus-inverse statement containing an occupancy contribution.

m1_cycle58_5p5_upper_audit

For t=1, the exact replacement is not hypothetical: the distinct numerator is the number of occupied elements of the thickened generalized-Jacobian lift fiber,

#{g∈π
−1
(b
Δ
	​

):N
Δ
+
,j
+
	​

(g)>0},

and no official finite local-limit estimate for that occupied set is currently banked.

ROLE_05_T1_MCA_GJ_COLOR_RESULT

A plain shifted-list theorem remains sufficient on the residual-safe subrange:

L
K
line
	​

	​

(D;k+t,a)≤n
C
0
	​

⟹∣Z
t
	​

∣≤n
C
0
	​

.

What is false is the implication

reserve at σ⟹shifted-list bound at surplus σ−t.
5. Verification requirements

A deterministic checker for the new lemma should accept

(K,D,k,σ,t,F,β
1
	​

,…,β
t
	​

,R)

and verify:

D is distinct and every β
i
	​

∈
/
D;

every S∈F has size a=k+σ;

all locators L
S
	​

 have the same first σ−t nonleading coefficients;

each Q
S
′
	​

=M+R−L
S
	​

 has degree <k+t;

Q
S
′
	​

=w
′
 on S;

Q
S
′
	​

(β
i
	​

)=z
S
	​

 for all i;

the emitted z
S
	​

 values are pairwise distinct;

E=∏
i
	​

(X−β
i
	​

) is squarefree and nonvanishing on D;

n>k+2t−2, certifying intrinsic degree t;

the exact integer lower bound obtained from the vector-collision census.

For official promotion, the checker must additionally evaluate, rather than merely name:

the official endpoint predicate;

the shifted quotient/action-rank profile;

the official periodic/support quotient charges;

the tangent-support predicate;

field-confinement status;

affine-color normalization, including its retained chart tag;

the exact source AP
corr
	​

;

the corrected-reserve inequality;

the same-field or field-transfer certificate.

The compact source material still does not expose a formally checkable AP
corr
	​

 and corrected-reserve adapter, so no source-valid conclusion can be attached to the construction yet.

cycle107_p17_n8_s4_gate_b_separ…

cycle106_role07_bankable_lemma

The supplied Cycle109 packet itself passed its listed SHA-256 checks.

6. Next exact lemma

The first missing LOW theorem is:

L-CYCLE109-LOW-CALIBRATED-OCCUPANCY-OR-OFFICIAL-CHARGE
Exact same-field statement

Let

q
gen
	​

=q
code
	​

=q
line
	​

=q.

For every official intrinsic 1≤t<σ datum satisfying the corrected reserve and exact AP
corr
	​

, prove that either:

the slopes belong to an explicitly capped endpoint, quotient/periodic, contained, tangent, field, or affine-color charge; or

after retaining every support-dependent normalization tag,

∣Z
t
primitive
	​

∣≤⌈
q
σ−1
(
k+σ
n
	​

)
	​

⌉+n
C
low
	​

,
	​

where C
low
	​

 is independent of k,σ,t.

For t=1, this must specialize to the quotient-conditioned thickened generalized-Jacobian occupancy theorem, not to an uncolored support count.

For unequal fields, the next statement must include an explicit bridge. One may not silently replace the same-field denominator q
σ−1
 by either q
gen
σ−1
	​

 or q
line
σ−1
	​

. The natural mixed constraint count suggests

q
gen
σ−t
	​

q
line
t−1
	​

,

but this is not a proved transfer formula.

The final checker must then establish the exact integer inequality

U
LOW
	​

+U
BALANCED
	​

+U
HIGH
	​

+U
charges
	​

≤⌊
2
128
q
line
	​

	​

⌋

with the correct sum/max program for disjoint branches versus exclusive cases.

For native MCA, q
line
	​

 is the decision denominator; q
code
	​

 may replace it only under equality or an exact registered bridge, and q
chal
	​

 never pays either the MCA numerator or the q
gen
	​

 entropy bill.

ROLE_06_FRONTIER_CHECKER_LEDGER

7. Self-audit
1. Exact implication proved and not proved

Proved:

large locator-prefix fiber⟹a same-field intrinsic LOW line with the displayed distinct-slope lower bound.

Also proved:

shifted list cap⟹LOW residue-image cap.

Not proved:

AP
corr
	​

+official charge exclusions⟹∣Z
t
	​

∣≤n
C
.

I also did not prove the calibrated upper bound, field transfer, or the final numerator inequality.

2. Official relevance

The lemma is official-prize-relevant structural progress, because it constructs actual distinct LOW slopes and identifies the unavoidable reserve-scale term.

It is not a prize proof, official counterpacket, or merely a finite enumeration. Its official promotion is blocked by the absent source-valid charge and AP
corr
	​

 verification.

3. First possible failure line

The first unproved line is

AP
corr
	​

+quotient/periodic/field/tangent exclusions⟹polynomial deviation from residue-color occupancy.

For promoting the lower construction to a counterpacket, the first possible failure is that its large locator-prefix/color fiber is classified by an official quotient, tangent, field, or affine-color charge.

4. Field and 2
−128
 ledger

The proved construction is deliberately same-field:

q
gen
	​

=q
code
	​

=q
line
	​

=q.

It does not use q
chal
	​

.

In the general problem:

q
gen
	​

 pays locator/prefix entropy;

distinct slopes are counted in K
line
	​

;

q
code
	​

 is the code alphabet;

q
chal
	​

 is irrelevant absent a protocol theorem;

the exact MCA target is

⌊q
line
	​

/2
128
⌋.

That target has not been proved.

5. Can the listed mechanisms reduce the numerator?

Same-slope support collisions: already collapsed in the theorem.

Contained incidences: absent by the degree argument.

Finite endpoint/pole terms: the chosen E has no roots on D, but the complete official endpoint predicate has not been audited.

Quotient/periodic structure: may charge part or all of a constructed fiber; not excluded.

Tangent supports: noncontainment is proved, but the broader official tangent charge may still apply.

Field confinement: avoidable in a prime-field or field-generating specialization, but not source-certified here.

Affine-color normalization: one common affine bijection cannot reduce the number of slopes. A support-dependent affine normalization can only be used with its chart tag retained; merging tags would be unsound.

6. Exact conversion to PROOF or COUNTERPACKET

A PROOF requires L-CYCLE109-LOW-CALIBRATED-OCCUPANCY-OR-OFFICIAL-CHARGE, exact paid-branch caps, a field-transfer theorem where fields differ, and the final integer numerator inequality.

A COUNTERPACKET requires a growing or exact official instance satisfying corrected reserve and source AP
corr
	​

, verifying that none of the official charges absorbs the construction, and showing either superpolynomial primitive image or

∣Z
t
	​

∣>⌊
2
128
q
line
	​

	​

⌋.
