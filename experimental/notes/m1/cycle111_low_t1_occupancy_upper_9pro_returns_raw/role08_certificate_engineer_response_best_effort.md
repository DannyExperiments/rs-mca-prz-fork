COUNTERPACKET:
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

# Role 08: Certificate Engineer / Finite Stress Harness

Design the exact checker or proof-carrying harness for the Cycle111 wall.

Focus points:

1. Specify an exact finite replay that tests the t=1 support/product
   formulation and detects structured counterpackets.
2. Terminal labels must be conservative:
   SOURCE_ROUTE_PROOF, FINITE_MODEL_PASS, COUNTERPACKET,
   ROUTE_CUT, RESOURCE_EXHAUSTED_NO_CLAIM.
3. Include source-validity receipts: AP_corr, charge absence/payment,
   field ledger, corrected reserve, distinct slope count, and numerator bound.
4. If a checker can only provide finite/model evidence, state the exact theorem
   needed to lift it.
5. If possible, provide pseudocode or executable skeleton precise enough for
   Codex to implement.

Ambition bar: create a checker spec that can distinguish proof, finite stress,
and false counterpacket without interpretation.

I’ll first inspect the packet’s current-state and Cycle110 audit files, then formulate a conservative finite replay checker with explicit receipts, terminal labels, and lift requirements.

The packet verifies cleanly, and the main wall is promotion: finite 
t
=
1
t=1 enumeration must stay separate from source-route proof without replayable AP_corr, charge, field-transfer, and reserve receipts.

A direct obstruction is now concrete: the literal universal bound fails without a charged/additive remainder, while the harness can still certify support enumeration and Johnson-slice bounds.

Thought for 31m 28s
1. Executive verdict and confidence
ROUTE_CUT

Confidence: high.

The literal Cycle111 target is false. There is no absolute constant 
C
C for which

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
≤
C
(
n
k
+
σ
)
q
g
e
n
σ
−
1
∣{Q(β):degQ≤k, agr 
D
​
 (Q,w)≥k+σ}∣≤C 
q 
gen
σ−1
​
 
( 
k+σ
n
​
 )
​
 
holds for every word, or equivalently on every elementary-symmetric prefix fiber.

This is not yet a COUNTERPACKET: the constructed family has exact affine-involution structure, and the packet does not freeze a source-valid AP_corr verifier or the official affine/periodic charge rule. Thus it refutes the unqualified pointwise theorem but does not refute a corrected free-color source theorem.

I also produced an exact proof-carrying finite harness. It distinguishes finite success, literal route cuts, and source-valid counterpackets without promoting finite sampling to a universal theorem.

2. Exact statements
ROUTE_CUT — no universal pure multiplicative bound
For every 
C
>
0
C>0 and every integer 
m
≥
2
m≥2, choose an odd prime 
q
q satisfying

q
>
max
⁡
{
2
m
+
1
,
 
C
(
2
m
−
1
)
,
 
2
128
C
(
2
m
2
)
}
.
q>max{2m+1,C(2m−1), 
2 
128
 C( 
2
2m
​
 )
​
 }.
Let

K
l
i
n
e
=
K
g
e
n
=
F
q
,
k
=
0
,
σ
=
2
,
β
=
0
,
M
(
X
)
=
X
2
,
K 
line
​
 =K 
gen
​
 =F 
q
​
 ,k=0,σ=2,β=0,M(X)=X 
2
 ,
and choose 
r
1
,
…
,
r
m
∈
F
q
×
r 
1
​
 ,…,r 
m
​
 ∈F 
q
×
​
  with pairwise distinct squares. Put

D
=
{
±
r
1
,
…
,
±
r
m
}
,
w
=
M
∣
D
.
D={±r 
1
​
 ,…,±r 
m
​
 },w=M∣ 
D
​
 .
Then the fiber

{
S
∈
(
D
2
)
:
e
1
(
S
)
=
0
}
{S∈( 
2
D
​
 ):e 
1
​
 (S)=0}
is exactly

S
i
=
{
r
i
,
−
r
i
}
,
1
≤
i
≤
m
.
S 
i
​
 ={r 
i
​
 ,−r 
i
​
 },1≤i≤m.
Its product values are

∏
x
∈
S
i
(
β
−
x
)
=
(
−
r
i
)
(
r
i
)
=
−
r
i
2
,
x∈S 
i
​
 
∏
​
 (β−x)=(−r 
i
​
 )(r 
i
​
 )=−r 
i
2
​
 ,
which are pairwise distinct. Hence the product image, and therefore the corresponding evaluation-color image, has size 
m
m.

But

C
(
2
m
2
)
q
=
C
m
(
2
m
−
1
)
q
<
m
.
C 
q
( 
2
2m
​
 )
​
 =C 
q
m(2m−1)
​
 <m.
Simultaneously, the exact same-field 
t
=
1
t=1 LOW-FIT condition holds:

2
128
C
(
2
m
2
)
≤
q
2
=
q
g
e
n
σ
−
1
q
l
i
n
e
.
2 
128
 C( 
2
2m
​
 )≤q 
2
 =q 
gen
σ−1
​
 q 
line
​
 .
Therefore prize-strength lower-bound reserve does not rescue the pointwise bound. Increasing 
q
q makes the claimed right-hand side smaller while the integer occupancy remains 
m
m.

This proves that the theorem as written requires an additional charged/discrete term or an exact hypothesis excluding this support structure.

BANKABLE_LEMMA — exact support enumeration
Let 
a
=
k
+
σ
a=k+σ. For every 
A
⊆
D
A⊆D of size 
a
a, let 
I
A
I 
A
​
  be the unique polynomial of degree 
<
a
<a interpolating 
w
∣
A
w∣ 
A
​
 . Then

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
a
}
=
{
I
A
(
β
)
:
A
∈
(
D
a
)
,
 
deg
⁡
I
A
≤
k
}
.
{Q(β):degQ≤k, agr 
D
​
 (Q,w)≥a}={I 
A
​
 (β):A∈( 
a
D
​
 ), degI 
A
​
 ≤k}.
Indeed, a witness 
Q
Q contains an 
a
a-subset 
A
A of its agreement set. Since 
Q
Q and 
I
A
I 
A
​
  both have degree 
<
a
<a and agree on 
A
A, they are equal. The converse is immediate.

For a monic anchor 
M
M of degree 
a
a, write

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
Since 
M
M and 
L
S
L 
S
​
  are monic of degree 
a
a,

deg
⁡
(
M
−
L
S
)
≤
k
  
⟺
  
e
j
(
S
)
=
e
j
(
M
)
,
1
≤
j
≤
σ
−
1.
deg(M−L 
S
​
 )≤k⟺e 
j
​
 (S)=e 
j
​
 (M),1≤j≤σ−1.
On this fiber,

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
M(β) preserves image size. This gives an exact, nonheuristic checker reduction.

3. Detailed obstruction and checker construction
Exact Cycle110 failure
The first invalid jump is in the supplied Role 09 synthesis where the calibrated main term is promoted to a pointwise bound and described as essentially the entire budget, with no separate additive term.

That inference fails before any character-sum, incidence, or inverse theorem:

average/codimension scale
⟹̸
pointwise upper bound on every fiber
.
average/codimension scale

⟹pointwise upper bound on every fiber.
When

C
(
n
a
)
/
q
g
e
n
σ
−
1
<
1
,
C( 
a
n
​
 )/q 
gen
σ−1
​
 <1,
the claimed pointwise theorem forces every relevant image to be empty. A single witness already contradicts that. The involution family strengthens this from a one-color integrality issue to an arbitrarily large 
m
m-color structured fiber.

The Cycle110 conclusions that quotient/action rank is vacuous at 
t
=
1
t=1, and that contained/delete-one is absent by degree, do not imply that all discrete or affine-support structure disappears. In particular, they do not establish that the involution packet is free rather than officially charged.

PLAN — exact finite harness
The checker accepts four modes:

general
support_product
anchor
proof_bundle
Its core replay is:

a := k + sigma
colors := empty set

for every a-subset A of D:
    I_A := exact interpolation of w on A
    if degree(I_A) <= k:
        colors.add(I_A(beta))
For support/product mode:

for every a-subset S of D:
    prefix := (e_1(S), ..., e_{sigma-1}(S))
    product := product(beta - x for x in S)
    fiber[prefix].add(product)
Anchor mode additionally verifies:

M is monic of degree a
selected prefix equals the leading sigma-1 coefficients of M
degree(M - L_S) <= k for every selected support
evaluation image = M(beta) - product image
The finite-field layer uses an explicit irreducible polynomial for
K
l
i
n
e
=
F
p
d
K 
line
​
 =F 
p 
d
 
​
 . It computes 
q
g
e
n
q 
gen
​
  as the smallest subfield of 
K
l
i
n
e
K 
line
​
  containing 
D
D, using Frobenius fixed-point tests over divisors of 
d
d.

The exact candidate bound is tested without floating-point arithmetic:

∣
Z
∣
 
C
d
e
n
 
q
g
e
n
σ
−
1
≤
C
n
u
m
(
n
a
)
.
∣Z∣C 
den
​
 q 
gen
σ−1
​
 ≤C 
num
​
 ( 
a
n
​
 ).
The exact ledger tests are

2
128
C
n
u
m
(
n
a
)
≤
C
d
e
n
q
g
e
n
σ
−
1
q
l
i
n
e
2 
128
 C 
num
​
 ( 
a
n
​
 )≤C 
den
​
 q 
gen
σ−1
​
 q 
line
​
 
and, for the final official numerator 
N
o
f
f
N 
off
​
 ,

2
128
N
o
f
f
≤
q
l
i
n
e
.
2 
128
 N 
off
​
 ≤q 
line
​
 .
q_code and q_chal are recorded only as metadata. Neither can be substituted into these denominators.

Source-validity receipts
Promotion beyond a finite/model result requires trusted executable receipts for:

SOURCE_ADAPTER
AP_CORR
ENDPOINT_ABSENT_OR_PAID
TANGENT_ABSENT_OR_PAID
FIELD_CONFINEMENT_ABSENT_OR_PAID
AFFINE_COLOR_ABSENT_OR_PAID
NORMALIZATION_RETAINED_INJECTIVE
A PAID receipt must provide the exact charged color set and an integer cap. The checker verifies the subset relation, cap, overlaps, and forms the literal free-color set.

The following are built into the 
t
=
1
t=1 finite core:

quotient/action-rank: VACUOUS_AT_T1
contained/delete-one: ABSENT_BY_DEGREE
same-slope collisions: exact K_line deduplication
q_chal denominator use: forbidden
q_code denominator use: forbidden
Conservative terminal semantics
SOURCE_ROUTE_PROOF
Only a trusted universal proof bundle can produce this terminal. A finite parameter sweep cannot.

FINITE_MODEL_PASS
The declared finite search completed exhaustively and the tested cap passed. No universal implication follows.

COUNTERPACKET
The exact free-color bound failed, SOURCE_ADAPTER and AP_CORR were verified, every charge was exactly absent or paid, retained normalization was verified, and LOW-FIT held.

ROUTE_CUT
The literal bound failed, but source promotion is blocked by an unresolved or paid structure, missing source predicates, field mismatch, or missing normalization receipt.

RESOURCE_EXHAUSTED_NO_CLAIM
The exhaustive search did not complete.

Included exact replay
The structured example uses

K
l
i
n
e
=
F
3
81
,
q
l
i
n
e
=
q
g
e
n
=
443426488243037769948249630619149892803
,
K 
line
​
 =F 
3 
81
 
​
 ,q 
line
​
 =q 
gen
​
 =443426488243037769948249630619149892803,
with 
n
=
4
,
k
=
0
,
σ
=
2
,
C
=
1
n=4,k=0,σ=2,C=1. Its maximum prefix fiber has two distinct colors.

The report verifies:

2
128
⋅
6
≤
q
g
e
n
q
l
i
n
e
,
2 
128
 ⋅6≤q 
gen
​
 q 
line
​
 ,
so the 
t
=
1
t=1 LOW-FIT test passes, while

2
128
⋅
2
>
q
l
i
n
e
,
2 
128
 ⋅2>q 
line
​
 ,
so the two colors exceed the final 128-bit slope budget. The terminal is nevertheless ROUTE_CUT, not COUNTERPACKET, because the source/AP-correctness/charge receipts are absent and an exact affine involution is detected.

Artifacts:

Checker bundle

Checker specification

Executable Python harness

Structured route-cut replay report

Replay:

python3 cycle111_t1_harness.py example_structured_route_cut.json \
  --output replay.json

python3 cycle111_t1_harness.py example_finite_pass.json \
  --output replay-pass.json
Expected terminals:

example_structured_route_cut.json -> ROUTE_CUT
example_finite_pass.json          -> FINITE_MODEL_PASS
4. Verification and replay requirements
AUDIT

A valid replay must verify all of the following:

The finite-field modulus is irreducible, the points of 
D
D are distinct, and 
β
∉
D
β∈
/
D.

Enumeration is exhaustive over all 
(
n
k
+
σ
)
( 
k+σ
n
​
 ) supports, or the terminal is RESOURCE_EXHAUSTED_NO_CLAIM.

Interpolation and degree tests use exact field arithmetic.

Colors are deduplicated as canonical 
K
l
i
n
e
K 
line
​
  elements.

Any support-dependent normalization retains its chart tag unless an injective transition receipt is verified.

q
g
e
n
q 
gen
​
  is computed rather than assumed.

q_code and q_chal are never used as probability denominators.

Every paid charge names its exact color set and cap.

COUNTERPACKET requires all source receipts; assertions embedded in an input JSON do not count as receipts.

The final 
2
−
128
2 
−128
  test is performed as the integer inequality
2
128
N
o
f
f
≤
q
l
i
n
e
2 
128
 N 
off
​
 ≤q 
line
​
 .

The bundle includes SHA-256 checksums, and both included replays completed with the expected terminals.

5. Next exact lemma
PLAN

The next viable source theorem is not the original pure bound. It is:

L-CYCLE111-T1-FREE-OCCUPANCY-WITH-DISCRETE-CHARGE.

For every official intrinsic t=1 datum satisfying frozen source AP_corr,
there is an exact disjoint partition

  Z_1 =
    Z_endpoint
    ⊔ Z_tangent
    ⊔ Z_field
    ⊔ Z_affine
    ⊔ Z_normalization
    ⊔ Z_1^free

with explicit caps P_endpoint, ..., P_normalization, such that

  |Z_1^free|
    <= C * binom(n,k+sigma) / q_gen^(sigma-1),

and

  2^128 *
  ( floor(C*binom(n,k+sigma)/q_gen^(sigma-1))
    + sum_i P_i )
  <= q_line.
The affine charge must either pay the entire involution family above or prove that official AP_corr excludes it. A bare additive 
+
1
+1 is insufficient: the route-cut family has 
m
m distinct colors for arbitrary 
m
m.

To convert the supplied replay into COUNTERPACKET, one must provide trusted receipts proving:

SOURCE_ADAPTER = verified
AP_CORR = verified
all official charges = ABSENT or exactly PAID
at least two colors remain free
normalization is injective
LOW-FIT = true
The current packet does not contain those frozen verifiers.

Mandatory self-audit
1. Exact implication proved and not proved
Proved:

There is no universal absolute 
C
 for the literal every-word/every-fiber pure bound.
There is no universal absolute C for the literal every-word/every-fiber pure bound.
Also proved: the exact support-interpolation identity and the exact monic-anchor prefix-fiber reduction.

Not proved: that the structured family is uncharged under the official source predicate, that AP_corr holds for it, or that the official prize theorem is false.

2. Relevance classification
This is an official-prize-relevant route cut and an exact finite/model checker certificate.

It is not an official prize proof, not a source-route proof, and not yet a source-valid counterpacket.

3. First possible failure in the reduction chain
The first failure is:

calibrated average/codimension scale
⟹
pointwise bound on every prefix fiber
.
calibrated average/codimension scale⟹pointwise bound on every prefix fiber.
At source level, the corresponding unproved arrow is:

A
P
c
o
r
r
+
uncharged intrinsic 
t
=
1
⟹
∣
Z
1
f
r
e
e
∣
≤
C
(
n
a
)
/
q
g
e
n
σ
−
1
.
AP 
corr
​
 +uncharged intrinsic t=1⟹∣Z 
1
free
​
 ∣≤C( 
a
n
​
 )/q 
gen
σ−1
​
 .
4. Field and 
2
−
128
2 
−128
  use
q
g
e
n
q 
gen
​
 : entropy/occupancy denominator.

q
l
i
n
e
q 
line
​
 : distinct-slope field and sole final security denominator.

q
c
o
d
e
q 
code
​
 : metadata only in this checker.

q
c
h
a
l
q 
chal
​
 : unused; no protocol-transfer theorem exists in the packet.

Final target: exactly 
2
128
N
o
f
f
≤
q
l
i
n
e
2 
128
 N 
off
​
 ≤q 
line
​
 .

t
=
1
t=1 LOW-FIT: exactly

2
128
C
n
u
m
(
n
a
)
≤
C
d
e
n
q
g
e
n
σ
−
1
q
l
i
n
e
.
2 
128
 C 
num
​
 ( 
a
n
​
 )≤C 
den
​
 q 
gen
σ−1
​
 q 
line
​
 .
No mixed-field transfer theorem was proved.

5. Possible numerator reductions
Quotient/action rank is vacuous at 
t
=
1
t=1, and contained/delete-one is absent by degree. Same-slope collisions are deduplicated exactly.

However, the route-cut family has a genuine affine involution 
x
↦
−
x
x↦−x. The explicit finite replay also exhibits proper additive-span structure. Affine-color, periodic, field, tangent, endpoint, and retained-normalization effects could therefore reduce the official free numerator if certified by exact source receipts. This is why the result is not labeled COUNTERPACKET.

6. Exact conversion from PLAN
PROOF requires the free-color theorem with a complete official charge partition, explicit caps, a frozen noncircular AP_corr, and a proved 
q
g
e
n
q 
gen
​
 -to-
q
l
i
n
e
q 
line
​
  ledger.

COUNTERPACKET requires the involution construction—or another growing family—to pass the source adapter and AP_corr, have all charges absent or paid while leaving a violating free set, and satisfy the exact LOW-FIT and 
2
−
128
2 
−128
  arithmetic.