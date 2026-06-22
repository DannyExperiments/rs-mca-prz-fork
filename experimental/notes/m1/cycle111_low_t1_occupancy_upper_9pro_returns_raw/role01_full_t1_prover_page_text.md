

cycle111_low_t1_occupancy_upper_9pro_packet.zip
Zip Archive
# Common Prompt For Cycle111

You are one of nine independent theorem workers attacking the RS-MCA Proximity
Prize route. You have a packet of local files attached. Work only from those
files and your internal mathematical knowledge.

NO INTERNET. Do not browse, search, cite new web sources, or rely on live
external sources. Use MAX reasoning. Try to fully solve the problem. If you
cannot fully solve it, progress it as much as possible by producing the
strongest exact lemma, route cut, checker, or counterpacket you can.

Primary target:

text
L-CYCLE111-LOW-T1-OCCUPANCY-UPPER.
For E = X - beta, beta notin D, and any word w:D -> K_line,
bound the number of distinct evaluation colors
  { Q(beta) : deg Q <= k, agr_D(Q,w) >= k+sigma }
by C * binom(n,k+sigma) / q_gen^(sigma-1),
with q_line/q_gen transfer and corrected-reserve ledger receipts explicit.


Equivalent support/product target:

text
For the monic-anchor family w = M|_D, bound the image size of
  S -> prod_{x in S}(beta-x)
on every elementary-symmetric prefix fiber
  e_j(S) = c_j, 1 <= j <= sigma-1,
by C * binom(n,k+sigma) / q_gen^(sigma-1).


If you think this target is false, do not give a vague objection. Produce the
source-valid counterpacket mechanism:

text
SOURCE_VALID_LOW_T1_COUNTERPACKET:
  prize-strength corrected reserve,
  source AP_corr true,
  t=1 intrinsic LOW,
  endpoint/field/affine-color/tangent/contained charges absent or paid,
  quotient/action-rank vacuous,
  distinct K_line slopes exceed the calibrated occupancy budget.


If you think the target is true, give a proof precise enough to enter a public
experimental ledger. If there is a missing hypothesis, state the exact missing
hypothesis. If your output is a checker plan, specify exact input, terminal
labels, replay requirements, and what implication the checker proves.

Use these labels exactly:

text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN


Do not overclaim. Distinguish:

- official prize theorem,
- source-valid route theorem,
- q-ledger transfer theorem,
- finite/model certificate,
- checker plan,
- heuristic or analogy.

Read the current-state file and Cycle110 audit before answering. The Cycle110
returns are inputs, not authorities. You may disagree with them, but if you do,
identify the exact line of failure.

Required output structure:

1. Executive verdict and confidence.
2. Exact theorem, counterpacket, route cut, or checker statement.
3. Detailed proof, construction, or obstruction.
4. Verification requirements or replay requirements.
5. Next exact lemma or construction.


---

# Mandatory Self-Audit Addendum

Before finalizing, do a self-audit. Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, source-route-relevant, or only a
   finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being
   used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, affine color normalization, tangent concentration, field
   confinement, hidden action rank, or retained normalization reduce the
   claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.


---

# Role 01: Full t=1 Occupancy Prover

Attack L-CYCLE111-LOW-T1-OCCUPANCY-UPPER directly.

Your job is to prove the theorem if it is true. Work in the native official
K_line setting. Do not reduce it to a finite toy model unless you also prove
the official lift.

Focus points:

1. Translate the set {Q(beta): deg Q <= k, agr_D(Q,w) >= k+sigma} into a
   clean incidence, moment, or code-theoretic object.
2. Prove the calibrated image bound with the correct denominator and absolute
   constant, or identify the minimal additional source predicate needed.
3. Explain why same-slope multiplicities, contained/delete-one incidences, and
   quotient/action-rank do not break the estimate at t=1.
4. State the strongest theorem you can honestly prove. If it falls short of the
   target, quantify exactly how.

Ambition bar: try to close the wall, not merely restate it.

I’ll first read the packet’s current-state and Cycle110 audit, reconstruct the exact t=1 reduction chain, then test whether it yields a proof or the first source-valid obstruction.

A first obstruction is emerging: the bound lacks a floor/additive singleton term, since 
w
≡
0
w≡0 always gives color 
0
0 while the RHS may be below 
1
1.

A second obstruction is that arbitrary words may paste many low-degree polynomials on disjoint agreement blocks; I’m testing whether the t=1 ledger actually rules this out.

Thought for 26m 7s
COUNTERPACKET
1. Executive verdict and confidence
L-CYCLE111-LOW-T1-OCCUPANCY-UPPER is false as stated, even for the monic-anchor family and even in the same-field setting.

There is a family with

q
g
e
n
=
q
c
o
d
e
=
q
l
i
n
e
=
p
,
σ
=
2
,
t
=
1
,
q 
gen
​
 =q 
code
​
 =q 
line
​
 =p,σ=2,t=1,
satisfying prize-strength corrected reserve, for which the number of distinct colors is a positive fraction of 
p
p, hence exceeds 
p
/
2
128
p/2 
128
 , while

#
 colors
(
n
k
+
2
)
/
p
⟶
∞
.
( 
k+2
n
​
 )/p
# colors
​
 ⟶∞.
Thus no absolute 
C
C can establish the proposed bound.

Confidence is high for the literal theorem and support/product counterpacket. Official source promotion remains conditional because the packet explicitly says the official AP_corr and affine/periodic charge predicates are not frozen. Relative to the explicit structural AP_corr candidate in Cycle110 Role 05, the construction passes the checkable clauses after a bounded anti-coset padding.

2. Exact counterpacket statement
SOURCE_VALID_LOW_T1_COUNTERPACKET — interval symmetric-prefix concentration
Fix:

any proposed absolute constant 
C
C;

any fixed bounded-defect threshold 
A
A used by the periodic/coset charge;

an integer

1
≤
k
<
2
124
,
1≤k<2 
124
 ,
and put

σ
=
2
,
a
=
k
+
2.
σ=2,a=k+2.
For all sufficiently large 
N
N, there exist a prime 
p
p, a set
D
⊂
F
p
D⊂F 
p
​
 , an element 
β
∉
D
β∈
/
D, and a monic polynomial
M
M of degree 
a
a, such that for 
w
=
M
∣
D
w=M∣ 
D
​
 ,

Z
=
{
Q
(
β
)
:
deg
⁡
Q
≤
k
,
 
agr
⁡
D
(
Q
,
w
)
≥
k
+
2
}
Z={Q(β):degQ≤k, agr 
D
​
 (Q,w)≥k+2}
satisfies

∣
Z
∣
>
p
8
k
>
p
2
128
,
∣Z∣> 
8k
p
​
 > 
2 
128
 
p
​
 ,
and

∣
Z
∣
>
C
 
(
∣
D
∣
k
+
2
)
p
.
∣Z∣>C 
p
( 
k+2
∣D∣
​
 )
​
 .
Moreover,

p
2
≥
2
128
(
∣
D
∣
k
+
2
)
,
p 
2
 ≥2 
128
 ( 
k+2
∣D∣
​
 ),
so the corrected reserve

q
g
e
n
σ
≥
2
128
(
n
k
+
σ
)
q 
gen
σ
​
 ≥2 
128
 ( 
k+σ
n
​
 )
holds.

The same construction gives

∣
{
∏
x
∈
S
(
β
−
x
)
:
S
∈
(
D
a
)
,
 
e
1
(
S
)
=
c
}
∣
>
C
(
n
a
)
p
,
​
 { 
x∈S
∏
​
 (β−x):S∈( 
a
D
​
 ), e 
1
​
 (S)=c} 
​
 >C 
p
( 
a
n
​
 )
​
 ,
so it directly refutes the advertised support/product target.

If an additional polynomial reserve 
p
≥
2
129
n
C
l
o
w
p≥2 
129
 n 
C 
low
​
 
  is required, choose 
k
+
1
>
C
l
o
w
k+1>C 
low
​
 . Then that reserve also holds for sufficiently large 
N
N, provided 
k
<
2
124
k<2 
124
 .

3. Detailed construction and proof
Step 1: A large elementary-symmetric prefix fiber
Let

I
=
{
1
,
2
,
…
,
N
}
.
I={1,2,…,N}.
Consider the sum map on 
a
a-subsets,

S
⟼
e
1
(
S
)
=
∑
x
∈
S
x
.
S⟼e 
1
​
 (S)= 
x∈S
∑
​
 x.
The possible integer sums lie between

a
(
a
+
1
)
2
and
a
(
2
N
−
a
+
1
)
2
,
2
a(a+1)
​
 and 
2
a(2N−a+1)
​
 ,
so there are at most

a
(
N
−
a
)
+
1
≤
a
N
a(N−a)+1≤aN
possible sums. Hence some value 
c
c has a fiber

F
=
{
S
∈
(
I
a
)
:
∑
x
∈
S
x
=
c
}
F={S∈( 
a
I
​
 ): 
x∈S
∑
​
 x=c}
of size

L
:
=
∣
F
∣
≥
(
N
a
)
a
N
.
(1)
L:=∣F∣≥ 
aN
( 
a
N
​
 )
​
 .(1)
For fixed 
k
k, this has order 
N
a
−
1
=
N
k
+
1
N 
a−1
 =N 
k+1
 , not the expected
p
−
1
(
N
a
)
p 
−1
 ( 
a
N
​
 ) scale.

Step 2: Choose the field at the collision scale
Let

r
=
2
A
+
3.
r=2A+3.
Choose a prime 
p
p, using Bertrand’s postulate, such that

k
L
+
N
+
r
<
p
<
2
(
k
L
+
N
+
r
)
.
(2)
kL+N+r<p<2(kL+N+r).(2)
For sufficiently large 
N
N, 
k
L
≥
N
+
r
kL≥N+r, and therefore

p
<
4
k
L
.
(3)
p<4kL.(3)
Also 
p
>
a
N
p>aN, so the sums defining 
c
c do not wrap modulo 
p
p.

Let 
g
g be a primitive element of 
F
p
×
F 
p
×
​
  and put

R
=
{
1
,
g
,
g
2
,
…
,
g
r
−
1
}
,
D
=
I
∪
R
.
R={1,g,g 
2
 ,…,g 
r−1
 },D=I∪R.
Write 
n
=
∣
D
∣
n=∣D∣; then 
N
≤
n
≤
N
+
r
N≤n≤N+r.

The padding 
R
R prevents bounded-defect multiplicative-coset confinement. Indeed, if 
H
<
F
p
×
H<F 
p
×
​
  has index 
d
≥
2
d≥2, every coset of 
H
H contains at most

⌈
r
d
⌉
≤
⌈
r
2
⌉
=
A
+
2
⌈ 
d
r
​
 ⌉≤⌈ 
2
r
​
 ⌉=A+2
of the consecutive powers in 
R
R. Thus at least 
A
+
1
A+1 points of 
R
R lie outside every proper multiplicative coset. Additively, 
F
p
F 
p
​
  has no nontrivial proper additive subgroup.

Step 3: The monic anchor and its witnesses
Define

M
(
X
)
=
X
a
−
c
X
a
−
1
,
w
=
M
∣
D
.
M(X)=X 
a
 −cX 
a−1
 ,w=M∣ 
D
​
 .
For 
S
∈
F
S∈F, let

L
S
(
X
)
=
∏
x
∈
S
(
X
−
x
)
.
L 
S
​
 (X)= 
x∈S
∏
​
 (X−x).
Because 
e
1
(
S
)
=
c
e 
1
​
 (S)=c,

L
S
(
X
)
=
X
a
−
c
X
a
−
1
+
terms of degree at most 
a
−
2.
L 
S
​
 (X)=X 
a
 −cX 
a−1
 +terms of degree at most a−2.
Therefore

Q
S
(
X
)
:
=
M
(
X
)
−
L
S
(
X
)
Q 
S
​
 (X):=M(X)−L 
S
​
 (X)
has degree at most

a
−
2
=
k
.
a−2=k.
For every 
x
∈
S
x∈S,

Q
S
(
x
)
=
M
(
x
)
=
w
(
x
)
,
Q 
S
​
 (x)=M(x)=w(x),
so

agr
⁡
D
(
Q
S
,
w
)
≥
∣
S
∣
=
a
=
k
+
2.
(4)
agr 
D
​
 (Q 
S
​
 ,w)≥∣S∣=a=k+2.(4)
In fact the agreement set is exactly 
S
S, because

M
−
Q
S
=
L
S
M−Q 
S
​
 =L 
S
​
 
has precisely the simple roots in 
S
S.

Thus every 
S
∈
F
S∈F supplies a qualifying polynomial.

Step 4: Distinct-color collision averaging
For distinct 
S
,
T
∈
F
S,T∈F,

Q
S
−
Q
T
=
L
T
−
L
S
.
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
 .
The two locator polynomials have the same leading coefficient and the same
X
a
−
1
X 
a−1
 -coefficient, so

deg
⁡
(
Q
S
−
Q
T
)
≤
a
−
2
=
k
.
deg(Q 
S
​
 −Q 
T
​
 )≤a−2=k.
It is nonzero, since equality would imply 
L
S
=
L
T
L 
S
​
 =L 
T
​
  and hence 
S
=
T
S=T.
Consequently,

Q
S
(
β
)
=
Q
T
(
β
)
Q 
S
​
 (β)=Q 
T
​
 (β)
can occur for at most 
k
k values of 
β
∈
F
p
β∈F 
p
​
 .

Let 
C
β
C 
β
​
  denote the number of unordered colliding pairs at 
β
β.
Summing over 
β
∉
D
β∈
/
D,

∑
β
∉
D
C
β
≤
k
(
L
2
)
.
β∈
/
D
∑
​
 C 
β
​
 ≤k( 
2
L
​
 ).
From (2),

p
−
n
>
k
L
.
p−n>kL.
Hence some 
β
∉
D
β∈
/
D satisfies

C
β
≤
k
(
L
2
)
p
−
n
.
(5)
C 
β
​
 ≤ 
p−n
k( 
2
L
​
 )
​
 .(5)
Let 
m
β
m 
β
​
  be the number of distinct values among
{
Q
S
(
β
)
:
S
∈
F
}
{Q 
S
​
 (β):S∈F}. If 
r
y
r 
y
​
  is the multiplicity of value
y
y, then

∑
y
r
y
=
L
,
∑
y
r
y
2
=
L
+
2
C
β
.
y
∑
​
 r 
y
​
 =L, 
y
∑
​
 r 
y
2
​
 =L+2C 
β
​
 .
Cauchy–Schwarz gives

m
β
≥
L
2
L
+
2
C
β
≥
L
1
+
k
(
L
−
1
)
p
−
n
>
L
2
.
(6)
m 
β
​
 ≥ 
L+2C 
β
​
 
L 
2
 
​
 ≥ 
1+ 
p−n
k(L−1)
​
 
L
​
 > 
2
L
​
 .(6)
Therefore

∣
Z
∣
>
L
2
.
(7)
∣Z∣> 
2
L
​
 .(7)
Using 
p
<
4
k
L
p<4kL,

∣
Z
∣
>
p
8
k
.
(8)
∣Z∣> 
8k
p
​
 .(8)
Since 
k
<
2
124
k<2 
124
 ,

1
8
k
>
2
−
128
,
8k
1
​
 >2 
−128
 ,
and hence

∣
Z
∣
>
p
2
128
.
(9)
∣Z∣> 
2 
128
 
p
​
 .(9)
Even after deleting the single possible endpoint contribution, for sufficiently large 
N
N,

∣
Z
∣
−
1
>
p
2
128
.
∣Z∣−1> 
2 
128
 
p
​
 .
Step 5: Failure of the proposed occupancy bound
Because 
n
=
N
+
O
A
(
1
)
n=N+O 
A
​
 (1),

(
n
a
)
=
(
1
+
o
(
1
)
)
(
N
a
)
.
( 
a
n
​
 )=(1+o(1))( 
a
N
​
 ).
From (1), (2), and (7),

∣
Z
∣
(
n
a
)
/
p
≥
L
p
2
(
n
a
)
>
k
L
2
2
(
n
a
)
.
( 
a
n
​
 )/p
∣Z∣
​
 ≥ 
2( 
a
n
​
 )
Lp
​
 > 
2( 
a
n
​
 )
kL 
2
 
​
 .
Using 
L
≥
(
N
a
)
/
(
a
N
)
L≥( 
a
N
​
 )/(aN),

∣
Z
∣
(
n
a
)
/
p
=
Ω
k
,
A
 ⁣
(
(
N
a
)
N
2
)
=
Ω
k
,
A
(
N
a
−
2
)
=
Ω
k
,
A
(
N
k
)
.
(10)
( 
a
n
​
 )/p
∣Z∣
​
 =Ω 
k,A
​
 ( 
N 
2
 
( 
a
N
​
 )
​
 )=Ω 
k,A
​
 (N 
a−2
 )=Ω 
k,A
​
 (N 
k
 ).(10)
This tends to infinity. Therefore, for every absolute 
C
C, sufficiently large 
N
N gives

∣
Z
∣
>
C
 
(
n
a
)
p
.
∣Z∣>C 
p
( 
a
n
​
 )
​
 .
No absolute occupancy constant exists.

Step 6: Corrected reserve and field ledger
Here

q
g
e
n
=
q
c
o
d
e
=
q
l
i
n
e
=
p
.
q 
gen
​
 =q 
code
​
 =q 
line
​
 =p.
Thus there is no mixed-field transfer: the transfer receipt is the identity.

Moreover,

p
2
(
n
a
)
>
k
2
L
2
(
n
a
)
=
Ω
k
,
A
(
N
k
)
⟶
∞
.
( 
a
n
​
 )
p 
2
 
​
 > 
( 
a
n
​
 )
k 
2
 L 
2
 
​
 =Ω 
k,A
​
 (N 
k
 )⟶∞.
Hence, for sufficiently large 
N
N,

p
2
≥
2
128
(
n
a
)
.
(11)
p 
2
 ≥2 
128
 ( 
a
n
​
 ).(11)
Since 
σ
=
2
σ=2, this is precisely

q
g
e
n
σ
≥
2
128
(
n
k
+
σ
)
.
q 
gen
σ
​
 ≥2 
128
 ( 
k+σ
n
​
 ).
The challenge field is unused:

q
c
h
a
l
provides no denominator and no receipt.
q 
chal
​
 provides no denominator and no receipt.
The actual bad-slope fraction obeys

∣
Z
∣
q
l
i
n
e
>
1
8
k
>
2
−
128
,
q 
line
​
 
∣Z∣
​
 > 
8k
1
​
 >2 
−128
 ,
so the final line-field ledger fails directly.

Step 7: Product formulation
For every 
S
∈
F
S∈F,

Q
S
(
β
)
=
M
(
β
)
−
L
S
(
β
)
=
M
(
β
)
−
∏
x
∈
S
(
β
−
x
)
.
Q 
S
​
 (β)=M(β)−L 
S
​
 (β)=M(β)− 
x∈S
∏
​
 (β−x).
Translation by 
M
(
β
)
M(β) is bijective. Therefore

∣
{
Q
S
(
β
)
:
S
∈
F
}
∣
=
∣
{
∏
x
∈
S
(
β
−
x
)
:
S
∈
F
}
∣
.
∣{Q 
S
​
 (β):S∈F}∣= 
​
 { 
x∈S
∏
​
 (β−x):S∈F} 
​
 .
Thus the elementary-symmetric prefix-fiber target is refuted by the same family.

AUDIT — charge receipts
Item	Receipt
Intrinsic 
t
=
1
t=1	Set 
E
=
X
−
β
E=X−β, 
B
=
1
B=1. A lower-denominator polynomial representation would make 
(
X
−
β
)
P
−
1
(X−β)P−1 vanish on more points than its degree.
Quotient/action rank	
K
[
X
]
/
(
E
)
≅
K
K[X]/(E)≅K, so every regular action has rank 
1
=
t
1=t; the low-action-rank charge is vacuous.
Contained/delete-one	If 
deg
⁡
G
<
k
degG<k, then 
(
X
−
β
)
G
+
1
(X−β)G+1 has degree at most 
k
k and cannot vanish on 
k
+
1
=
a
−
1
k+1=a−1 points.
Tangent	
M
−
Q
S
=
L
S
M−Q 
S
​
 =L 
S
​
  is a product of distinct linear factors, so every agreement root is simple.
Field confinement	
K
=
F
p
K=F 
p
​
  has no proper subfield.
Periodic/coset	The 
2
A
+
3
2A+3 consecutive primitive powers leave more than 
A
A points outside every proper multiplicative coset.
Same-slope collisions	Explicitly collapsed by the collision argument; 
Z
Z counts distinct values only.
Affine color	A fixed affine normalization is bijective. The surviving color set has size 
>
p
/
(
8
k
)
>p/(8k); any chart receipt covering it must pay at least that many slopes and therefore fails the 
p
/
2
128
p/2 
128
  budget.
Endpoint	At most one color; deleting it does not repair the violation.
Retained normalization	The identity normalization suffices; no pole or zero affine coefficient occurs.
Relative to the explicit Cycle110 Role 05 AP_corr candidate, clauses 1–4 and the checkable parts of clause 5 are satisfied. The official-source qualifier is not fully decidable because the packet itself says the official AP_corr, source-visible rational class, and affine-color receipt are not frozen.

ROUTE_CUT
The exact failure in Cycle110 is the assertion in Role 02’s 
t
=
1
t=1 analysis that a prefix fiber far above average must come from proper-subfield or subgroup-coset confinement.

That implication is false.

An interval in a prime field has no subfield confinement, and after the primitive-power padding it has no bounded-defect multiplicative-coset confinement. Nevertheless its 
a
a-subset sums occupy only 
O
(
a
N
)
O(aN) values rather than 
p
p values. Consequently one sum fiber has size

≳
(
N
a
)
a
N
,
≳ 
aN
( 
a
N
​
 )
​
 ,
which is larger than the putative equidistributed size

(
N
a
)
p
p
( 
a
N
​
 )
​
 
by a factor of order 
p
/
(
a
N
)
p/(aN).

Exact subgroup exclusion does not imply additive Fourier uniformity or small additive energy. A character-sum argument cannot discard its nontrivial frequencies merely by checking subfields, subgroups, or action rank.

Also, the arbitrary-word theorem and the monic-anchor support theorem are not logically equivalent without an additional reduction. The latter is only a special case. The counterpacket already lies in that special case, so both proposed statements fail.

BANKABLE_LEMMA
The strongest unconditional universal replacement is the 
q
q-free support-packing bound.

Let

m
=
∣
{
Q
(
β
)
:
deg
⁡
Q
≤
k
,
 
agr
⁡
D
(
Q
,
w
)
≥
k
+
σ
}
∣
.
m=∣{Q(β):degQ≤k, agr 
D
​
 (Q,w)≥k+σ}∣.
For every distinct color choose one witness polynomial 
Q
z
Q 
z
​
  and an
a
=
k
+
σ
a=k+σ element agreement set 
S
z
S 
z
​
 .

If 
z
≠
z
′
z

=z 
′
 , then 
Q
z
−
Q
z
′
Q 
z
​
 −Q 
z 
′
 
​
  is a nonzero polynomial of degree at most
k
k. Hence

∣
S
z
∩
S
z
′
∣
≤
k
.
∣S 
z
​
 ∩S 
z 
′
 
​
 ∣≤k.
Every 
(
k
+
1
)
(k+1)-subset of 
D
D is therefore contained in at most one 
S
z
S 
z
​
 .
Double counting gives

m
(
k
+
σ
k
+
1
)
≤
(
n
k
+
1
)
,
m( 
k+1
k+σ
​
 )≤( 
k+1
n
​
 ),
and thus

m
≤
(
n
k
+
1
)
(
k
+
σ
k
+
1
)
.
(12)
m≤ 
( 
k+1
k+σ
​
 )
( 
k+1
n
​
 )
​
 .
​
 (12)
The interval construction has order 
N
k
+
1
N 
k+1
 , the same order as (12), so the
q
q-free packing scale is essentially the correct worst-case scale for
arbitrary words. A universal 
q
g
e
n
−
(
σ
−
1
)
q 
gen
−(σ−1)
​
  improvement requires
a genuine pseudorandomness hypothesis.

EXACT_NEW_WALL
The minimal missing hypothesis is quantitative symmetric-prefix anticoncentration, not merely subgroup or subfield aperiodicity.

For 
σ
=
2
σ=2, the required source condition must imply

max
⁡
c
∈
K
∣
{
S
∈
(
D
a
)
:
∑
x
∈
S
x
=
c
}
∣
≤
C
a
d
d
(
n
a
)
q
g
e
n
.
(13)
c∈K
max
​
  
​
 {S∈( 
a
D
​
 ): 
x∈S
∑
​
 x=c} 
​
 ≤C 
add
​
  
q 
gen
​
 
( 
a
n
​
 )
​
 .(13)
For general 
σ
σ, it must imply

max
⁡
c
∣
{
S
∈
(
D
a
)
:
e
j
(
S
)
=
c
j
,
 
1
≤
j
≤
σ
−
1
}
∣
≤
C
s
y
m
(
n
a
)
q
g
e
n
σ
−
1
.
(14)
c
max
​
  
​
 {S∈( 
a
D
​
 ):e 
j
​
 (S)=c 
j
​
 , 1≤j≤σ−1} 
​
 ≤C 
sym
​
  
q 
gen
σ−1
​
 
( 
a
n
​
 )
​
 .(14)
A noncircular Fourier formulation is available. For 
σ
=
2
σ=2, with a
nontrivial additive character 
ψ
ψ,

N
c
=
1
q
∑
λ
∈
K
ψ
(
−
λ
c
)
 
[
u
a
]
∏
x
∈
D
(
1
+
u
ψ
(
λ
x
)
)
.
N 
c
​
 = 
q
1
​
  
λ∈K
∑
​
 ψ(−λc)[u 
a
 ] 
x∈D
∏
​
 (1+uψ(λx)).
Thus (13) follows from an explicit bound on the total nonzero Fourier mass

∑
λ
≠
0
∣
[
u
a
]
∏
x
∈
D
(
1
+
u
ψ
(
λ
x
)
)
∣
.
λ

=0
∑
​
  
​
 [u 
a
 ] 
x∈D
∏
​
 (1+uψ(λx)) 
​
 .
The next honest theorem is therefore:

L-CYCLE112-T1-SYMMETRIC-PREFIX-ANTICONCENTRATION-OR-ADDITIVE-ENERGY-CHARGE.

Either every elementary-symmetric prefix fiber has the calibrated
q_gen^{-(sigma-1)} size, or D carries a quantitatively specified additive
Fourier/small-doubling/high-energy charge whose distinct K_line slope cap is
explicitly paid.
A “proper subgroup or subfield” alternative is insufficient.

4. Verification and replay requirements
A deterministic replay accepts

(
k
,
A
,
N
,
p
,
g
,
c
,
β
,
D
,
M
)
(k,A,N,p,g,c,β,D,M)
and either the fiber 
F
F or a certified fiber count 
L
L.

It must verify:

p
p is prime and 
g
g has order 
p
−
1
p−1.

D
=
I
∪
{
g
0
,
…
,
g
2
A
+
2
}
D=I∪{g 
0
 ,…,g 
2A+2
 } and 
β
∉
D
β∈
/
D.

Every 
S
∈
F
S∈F has size 
a
=
k
+
2
a=k+2 and sum 
c
c.

Q
S
=
M
−
L
S
Q 
S
​
 =M−L 
S
​
  has degree at most 
k
k and agrees with 
w
=
M
∣
D
w=M∣ 
D
​
  exactly on 
S
S.

Colors 
Q
S
(
β
)
Q 
S
​
 (β) are deduplicated in 
F
p
F 
p
​
 .

The collision receipt

∣
im
⁡
∣
≥
L
1
+
k
(
L
−
1
)
/
(
p
−
n
)
∣im∣≥ 
1+k(L−1)/(p−n)
L
​
 
is valid.

The exact integer inequalities

p
2
≥
2
128
(
n
a
)
,
2
128
∣
im
⁡
∣
>
p
,
∣
im
⁡
∣
>
C
(
n
a
)
/
p
.
p 
2
 ≥2 
128
 ( 
a
n
​
 ),2 
128
 ∣im∣>p,∣im∣>C( 
a
n
​
 )/p.
The t
=
1
=1, field, tangent, contained, and bounded-defect coset receipts above.

Appropriate terminal labels are:

COUNTERPACKET
AUDIT
ROUTE_CUT
An official checker must instead return AUDIT rather than claim official
source validity whenever the frozen AP_corr or affine/periodic charge schema
is absent.

5. Next exact lemma or construction
Freeze a source predicate that quantitatively controls the Fourier mass of the
elementary-symmetric prefix map. Then prove (14), followed by the product-image
bound.

Absent such a predicate, the interval construction is the exact reusable
counterpacket family:

small additive diameter
  
⟹
  
large prefix fiber
  
⟹
  
constant-fraction distinct evaluation colors
.
small additive diameter⟹large prefix fiber⟹constant-fraction distinct evaluation colors.
AUDIT — Mandatory self-audit
Exact implication proved.
I proved that no absolute 
C
C can satisfy the displayed arbitrary-word or monic-anchor 
t
=
1
t=1 bound. I also proved a family satisfying the same-field entropy reserve whose distinct colors exceed 
q
l
i
n
e
/
2
128
q 
line
​
 /2 
128
 . I did not prove that the family satisfies an unspecified future official AP_corr.

Relevance.
This is an official-parameter and q-ledger-relevant mathematical counterpacket, not merely a finite toy certificate. Its formal official-source status is conditional on the source predicate. It is source-valid under the only explicit structural AP_corr candidate in the packet, subject to the stated affine/periodic-schema caveat.

First failing reduction line.
The first false line is:

no subfield/subgroup confinement
⟹
symmetric-prefix fibers have 
q
−
(
σ
−
1
)
 size
.
no subfield/subgroup confinement⟹symmetric-prefix fibers have q 
−(σ−1)
  size.
Cycle110 Role 02’s corresponding 
t
=
1
t=1 assertion fails on prime-field intervals.

Field and security ledger.

q
g
e
n
=
q
c
o
d
e
=
q
l
i
n
e
=
p
.
q 
gen
​
 =q 
code
​
 =q 
line
​
 =p.
No transfer is used. q_chal is unused. Corrected reserve is checked as
p
2
≥
2
128
(
n
a
)
p 
2
 ≥2 
128
 ( 
a
n
​
 ), while the bad fraction is 
>
∣
Z
∣
/
p
>
1
/
(
8
k
)
>
2
−
128
>∣Z∣/p>1/(8k)>2 
−128
 .

Possible numerator reductions.
Quotient/action rank is vacuous at 
t
=
1
t=1; contained/delete-one is empty; agreements are simple; field confinement is impossible; same-slope collisions are deduplicated; endpoint removes at most one; fixed affine normalization preserves cardinality. Bounded-defect coset confinement is blocked by the primitive-power padding. A stronger additive-energy or Fourier charge could exclude the construction, but that would be a new missing hypothesis.

PLAN status.
This is not a PLAN. It is a COUNTERPACKET to the literal theorem and an EXACT_NEW_WALL identifying the hypothesis needed to formulate a viable replacement.


