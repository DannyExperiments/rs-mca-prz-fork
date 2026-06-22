COUNTERPACKET
1. Executive verdict and confidence
The literal L-CYCLE111-LOW-T1-OCCUPANCY-UPPER and its support/product formulation are false.

Confidence: high.

The failure is not primarily product collision. The first broken implication is

“the elementary-symmetric prefix carries 
(
σ
−
1
)
log
⁡
q
g
e
n
 bits of entropy.”
“the elementary-symmetric prefix carries (σ−1)logq 
gen
​
  bits of entropy.”
Even in a prime field, an affine progression can have only 
O
(
n
)
O(n) attainable 
e
1
e 
1
​
 -values on fixed-size subsets, while 
q
g
e
n
q 
gen
​
  is exponentially or polynomially larger. A largest 
e
1
e 
1
​
 -fiber then has size 
≫
(
n
k
+
σ
)
/
n
≫( 
k+σ
n
​
 )/n, not 
≍
(
n
k
+
σ
)
/
q
g
e
n
≍( 
k+σ
n
​
 )/q 
gen
​
 . For a suitable 
β
β, a constant fraction of that fiber gives distinct products.

The construction below satisfies prize-strength corrected reserve and can leave more than 
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
  distinct colors after paying one endpoint color.

Relative to the explicit structural AP_corr proposed in Cycle110, it also passes the listed intrinsic-degree, action-rank, subgroup, subfield, contained, tangent, and normalization tests. The packet nevertheless states that official source AP_corr is not frozen. Therefore this is:

a rigorous COUNTERPACKET to the literal Cycle111 theorem;

a source-route counterpacket under the only explicit Cycle110 AP_corr candidate;

not yet an official-prize counterpacket receipt until the actual source predicate is frozen.

2. Exact counterpacket statement
BANKABLE_LEMMA — prefix-fiber product-image lower bound
Let 
K
K be a finite field of size 
q
q, 
D
⊂
K
D⊂K, 
∣
D
∣
=
n
∣D∣=n, and let

A
=
k
+
σ
.
A=k+σ.
Fix a prefix fiber

F
=
{
S
∈
(
D
A
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
,
L
:
=
∣
F
∣
.
F={S∈( 
A
D
​
 ):e 
j
​
 (S)=c 
j
​
 , 1≤j≤σ−1},L:=∣F∣.
Write

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
Then

max
⁡
β
∈
K
∖
D
∣
{
L
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
≥
L
(
q
−
n
)
q
−
n
+
k
(
L
−
1
)
.
(1)
β∈K∖D
max
​
 ∣{L 
S
​
 (β):S∈F}∣≥ 
q−n+k(L−1)
L(q−n)
​
 .(1)
In particular, if

q
−
n
≥
k
(
L
−
1
)
,
q−n≥k(L−1),
some 
β
∉
D
β∈
/
D satisfies

∣
{
L
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
≥
L
2
.
(2)
∣{L 
S
​
 (β):S∈F}∣≥ 
2
L
​
 .(2)
Thus, when the line field is large enough, the product image is within a factor two of the entire prefix fiber. Same-product degeneracy cannot repair a badly concentrated prefix distribution.

COUNTERPACKET — affine-prefix family
Fix any integer 
A
≥
4
A≥4, set

σ
=
2
,
k
=
A
−
2.
σ=2,k=A−2.
For every proposed absolute constant 
C
C, and all sufficiently large 
n
n, there exist

K
g
e
n
=
K
c
o
d
e
=
K
l
i
n
e
=
F
p
,
K 
gen
​
 =K 
code
​
 =K 
line
​
 =F 
p
​
 ,
an evaluation set 
D
⊂
F
p
D⊂F 
p
​
 , a point 
β
∉
D
β∈
/
D, and a monic-anchor word 
w
=
M
∣
D
w=M∣ 
D
​
 , such that, writing

N
=
(
n
A
)
,
N=( 
A
n
​
 ),
all the following hold:

p
2
≥
2
128
N
,
(3)
p 
2
 ≥2 
128
 N,(3)
but

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
>
C
 
N
p
,
(4)
∣{Q(β):degQ≤k, agr 
D
​
 (Q,w)≥k+σ}∣>C 
p
N
​
 ,(4)
and, for 
k
<
2
128
/
12
k<2 
128
 /12, even after deleting one endpoint color,

2
128
(
#
{
distinct colors
}
−
1
)
>
p
.
(5)
2 
128
 (#{distinct colors}−1)>p.(5)
Taking 
A
=
4
A=4, 
k
=
2
k=2, already gives an infinite counterpacket family.

3. Construction and proof
3.1 A large 
e
1
e 
1
​
 -fiber
Consider the 
A
A-subsets of the integer index set 
[
n
]
[n]. Their sums lie between

1
+
⋯
+
A
and
(
n
−
A
+
1
)
+
⋯
+
n
.
1+⋯+Aand(n−A+1)+⋯+n.
Consequently the number of possible sums is exactly

R
=
A
(
n
−
A
)
+
1.
R=A(n−A)+1.
Choose an integer 
s
0
s 
0
​
  maximizing

I
=
{
I
∈
(
[
n
]
A
)
:
∑
i
∈
I
i
=
s
0
}
.
I={I∈( 
A
[n]
​
 ): 
i∈I
∑
​
 i=s 
0
​
 }.
Put 
L
=
∣
I
∣
L=∣I∣. Pigeonhole gives

L
≥
N
R
.
(6)
L≥ 
R
N
​
 .(6)
For fixed 
A
≥
4
A≥4,

L
≍
A
n
A
−
1
,
R
≍
A
n
.
L≍ 
A
​
 n 
A−1
 ,R≍ 
A
​
 n.
This is already much larger than the proposed 
N
/
q
g
e
n
N/q 
gen
​
  scale once 
q
g
e
n
≍
L
q 
gen
​
 ≍L.

3.2 Choose the field at the collision scale
For sufficiently large 
n
n, arrange

T
:
=
n
+
k
(
L
−
1
)
>
2
64
N
.
(7)
T:=n+k(L−1)>2 
64
  
N
​
 .(7)
By Bertrand’s postulate, choose a prime

T
<
p
<
2
T
.
(8)
T<p<2T.(8)
Then

p
2
>
2
128
N
,
p 
2
 >2 
128
 N,
which is exactly the same-field prize-strength corrected reserve for 
σ
=
2
σ=2.

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
 . Choose one 
I
0
∈
I
I 
0
​
 ∈I and distinct indices 
r
,
s
∈
I
0
r,s∈I 
0
​
 . Define

b
=
s
−
g
r
g
−
1
∈
F
p
b= 
g−1
s−gr
​
 ∈F 
p
​
 
and

D
=
{
b
+
1
,
b
+
2
,
…
,
b
+
n
}
.
D={b+1,b+2,…,b+n}.
The points are distinct because 
p
>
n
p>n. Moreover,

b
+
s
b
+
r
=
g
.
(9)
b+r
b+s
​
 =g.(9)
Hence even the active support 
S
I
0
S 
I 
0
​
 
​
  contains two nonzero elements whose ratio generates 
F
p
×
F 
p
×
​
 . It is therefore not confined to a coset of any proper multiplicative subgroup. Since 
F
p
F 
p
​
  has no nontrivial proper additive subgroup or proper subfield, the listed subgroup and field-confinement mechanisms are absent.

For every 
I
∈
I
I∈I, define

S
I
=
{
b
+
i
:
i
∈
I
}
⊂
D
.
S 
I
​
 ={b+i:i∈I}⊂D.
All these supports have the same first elementary symmetric coordinate:

e
1
(
S
I
)
=
A
b
+
s
0
=
:
c
.
(10)
e 
1
​
 (S 
I
​
 )=Ab+s 
0
​
 =:c.(10)
Thus they lie in one 
σ
−
1
=
1
σ−1=1 prefix fiber.

3.3 Convert the fiber into Reed–Solomon witnesses
Let

M
(
X
)
=
X
A
−
c
X
A
−
1
M(X)=X 
A
 −cX 
A−1
 
and define 
w
=
M
∣
D
w=M∣ 
D
​
 .

For 
I
∈
I
I∈I, set

Q
I
(
X
)
=
M
(
X
)
−
L
S
I
(
X
)
.
Q 
I
​
 (X)=M(X)−L 
S 
I
​
 
​
 (X).
Because 
L
S
I
L 
S 
I
​
 
​
  is monic of degree 
A
A and has 
X
A
−
1
X 
A−1
 -coefficient 
−
c
−c, the degree-
A
A and degree-
(
A
−
1
)
(A−1) terms cancel. Therefore

deg
⁡
Q
I
≤
A
−
2
=
k
.
(11)
degQ 
I
​
 ≤A−2=k.(11)
On every 
x
∈
S
I
x∈S 
I
​
 ,

L
S
I
(
x
)
=
0
,
L 
S 
I
​
 
​
 (x)=0,
so

Q
I
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
.
Q 
I
​
 (x)=M(x)=w(x).
Consequently

agr
⁡
D
(
Q
I
,
w
)
=
A
=
k
+
σ
.
(12)
agr 
D
​
 (Q 
I
​
 ,w)=A=k+σ.(12)
At any 
β
∉
D
β∈
/
D,

Q
I
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
I
(
β
)
.
(13)
Q 
I
​
 (β)=M(β)−L 
S 
I
​
 
​
 (β).(13)
Translation by the fixed value 
M
(
β
)
M(β) preserves cardinality, so distinct colors are exactly distinct subset products 
L
S
I
(
β
)
L 
S 
I
​
 
​
 (β).

3.4 Collision-energy proof of the bankable lemma
For distinct 
S
,
T
∈
F
S,T∈F, the locator polynomials share their first 
σ
−
1
σ−1 subleading coefficients. Hence

deg
⁡
(
L
S
−
L
T
)
≤
A
−
σ
=
k
.
(14)
deg(L 
S
​
 −L 
T
​
 )≤A−σ=k.(14)
Since 
S
≠
T
S

=T, this polynomial is nonzero. Thus it has at most 
k
k roots in 
K
K.

For 
β
∈
K
∖
D
β∈K∖D, let 
C
β
C 
β
​
  be the number of unordered colliding pairs

{
S
,
T
}
⊂
F
,
L
S
(
β
)
=
L
T
(
β
)
.
{S,T}⊂F,L 
S
​
 (β)=L 
T
​
 (β).
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
Therefore some 
β
∉
D
β∈
/
D has

C
β
≤
k
(
L
2
)
q
−
n
.
(15)
C 
β
​
 ≤ 
q−n
k( 
2
L
​
 )
​
 .(15)
Let 
m
y
m 
y
​
  be the number of supports producing product value 
y
y, and let 
V
β
V 
β
​
  be the number of distinct product values. Then

∑
y
m
y
=
L
,
∑
y
m
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
 m 
y
​
 =L, 
y
∑
​
 m 
y
2
​
 =L+2C 
β
​
 .
Cauchy–Schwarz yields

L
2
≤
V
β
(
L
+
2
C
β
)
.
L 
2
 ≤V 
β
​
 (L+2C 
β
​
 ).
Using (15),

V
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
q
−
n
,
V 
β
​
 ≥ 
1+ 
q−n
k(L−1)
​
 
L
​
 ,
which proves (1).

In the construction, 
p
−
n
>
k
(
L
−
1
)
p−n>k(L−1), so some 
β
∉
D
β∈
/
D has

V
β
>
L
2
.
(16)
V 
β
​
 > 
2
L
​
 .(16)
All same-product and same-slope collisions have therefore been explicitly deduplicated.

3.5 Violation of the proposed occupancy bound
For sufficiently large 
n
n, 
L
>
2
L>2. Since

p
>
T
≥
k
(
L
−
1
)
,
p>T≥k(L−1),
we have

N
p
<
N
k
(
L
−
1
)
≤
2
N
k
L
≤
2
R
k
.
(17)
p
N
​
 < 
k(L−1)
N
​
 ≤ 
kL
2N
​
 ≤ 
k
2R
​
 .(17)
On the other hand,

V
β
>
L
2
≥
N
2
R
.
(18)
V 
β
​
 > 
2
L
​
 ≥ 
2R
N
​
 .(18)
Because 
A
≥
4
A≥4 is fixed,

N
R
2
≍
A
n
A
−
2
⟶
∞
.
R 
2
 
N
​
 ≍ 
A
​
 n 
A−2
 ⟶∞.
Thus, for every proposed constant 
C
C, choosing 
n
n sufficiently large gives

V
β
−
1
>
C
 
N
p
.
(19)
V 
β
​
 −1>C 
p
N
​
 .(19)
The subtraction of 
1
1 pays the complete endpoint allowance.

This disproves both the evaluation-color statement and the support/product statement.

3.6 Violation of the 
2
−
128
2 
−128
  numerator budget
For sufficiently large 
n
n, 
n
<
k
L
n<kL, so from (8),

p
<
2
(
n
+
k
L
)
<
4
k
L
.
(20)
p<2(n+kL)<4kL.(20)
Also 
V
β
−
1
≥
L
/
3
V 
β
​
 −1≥L/3 once 
L
L is large. Hence, if

k
<
2
128
12
,
k< 
12
2 
128
 
​
 ,
then

p
2
128
<
4
k
L
2
128
<
L
3
≤
V
β
−
1.
(21)
2 
128
 
p
​
 < 
2 
128
 
4kL
​
 < 
3
L
​
 ≤V 
β
​
 −1.(21)
In particular 
k
=
2
k=2 gives a bad-color density bounded below by a positive constant, rather than 
2
−
128
2 
−128
 , despite corrected reserve.

This is not just an integrality or one-color problem.

3.7 Charge audit
Take

E
=
X
−
β
,
B
=
1.
E=X−β,B=1.
The following receipts are exact.

Intrinsic 
t
=
1
t=1. If 
1
/
(
x
−
β
)
1/(x−β) agreed on 
D
D with a polynomial 
P
P of degree at most 
k
k, then

(
X
−
β
)
P
(
X
)
−
1
(X−β)P(X)−1
would have degree at most 
k
+
1
=
A
−
1
<
n
k+1=A−1<n and vanish on all 
n
n points of 
D
D, impossible.

Quotient/action rank. For 
E
=
X
−
β
E=X−β,

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
,
K[X]/(E)≅K,
so every regular source-visible action has rank 
1
=
t
1=t. A rank-drop charge is vacuous.

Contained incidence. If 
(
X
−
β
)
G
+
1
(X−β)G+1 with 
deg
⁡
G
≤
k
degG≤k vanished on any full support 
S
I
S 
I
​
  of size 
A
=
k
+
2
A=k+2, it would be a degree-
≤
A
−
1
≤A−1 polynomial with 
A
A roots, hence zero; evaluating at 
β
β gives 
1
=
0
1=0.

Tangent. The agreement polynomial is

w
−
Q
I
=
L
S
I
.
w−Q 
I
​
 =L 
S 
I
​
 
​
 .
Every root is simple because the support points are distinct:

L
S
I
′
(
x
)
=
∏
y
∈
S
I
∖
{
x
}
(
x
−
y
)
≠
0.
L 
S 
I
​
 
′
​
 (x)= 
y∈S 
I
​
 ∖{x}
∏
​
 (x−y)

=0.
Field confinement. 
K
=
F
p
K=F 
p
​
  has no proper subfield.

Additive/multiplicative confinement. The additive group of 
F
p
F 
p
​
  has no nontrivial proper subgroup. Equation (9) puts a primitive ratio inside an active support, ruling out confinement to one proper multiplicative coset.

Affine color and normalization. Passing from 
[
n
]
[n] to 
D
=
b
+
[
n
]
D=b+[n] is one global affine normalization. It is bijective and carries one retained tag; it cannot reduce the number of colors. Any support-dependent affine normalization must retain its support tag and likewise cannot merge the distinct values already counted in 
V
β
V 
β
​
 .

Endpoint. At most one color was deleted in (19) and (21).

The unresolved classification is whether an eventual official AP_corr will introduce a new “short restricted prefix image,” “affine progression,” or Prouhet-type charge. No such frozen predicate or charge is present in the packet.

AUDIT
The exact Cycle110 failure is the assertion in the t=1 route cut that a prefix fiber much larger than its 
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
  average must force proper-subfield or subgroup/coset structure.

That implication is false.

Here:

K
g
e
n
=
F
p
K 
gen
​
 =F 
p
​
 ;

there is no proper subfield;

an active support contains a primitive multiplicative ratio;

action rank is automatically full at 
t
=
1
t=1;

nevertheless

max
⁡
c
#
{
S
∈
(
D
A
)
:
e
1
(
S
)
=
c
}
≥
(
n
A
)
A
(
n
−
A
)
+
1
,
c
max
​
 #{S∈( 
A
D
​
 ):e 
1
​
 (S)=c}≥ 
A(n−A)+1
( 
A
n
​
 )
​
 ,
while 
p
≍
L
≫
n
p≍L≫n.

The Cycle110 budget arithmetic is conditionally correct. What fails is treating 
q
g
e
n
q 
gen
​
  as actual prefix min-entropy.

Newton identities do not help: for 
σ
=
2
σ=2, the condition is simply a first-moment constraint. Moment-curve geometry identifies a hyperplane slice containing 
≍
n
A
−
1
≍n 
A−1
  subset points. A finite-field local-limit estimate at scale 
1
/
p
1/p is false because the subset sums occupy only 
O
(
n
)
O(n) field values.

4. Verification and replay requirements
A finite replay accepts

(
n
,
A
,
p
,
g
,
b
,
s
0
,
β
)
(n,A,p,g,b,s 
0
​
 ,β)
and performs:

Verify 
p
p prime, 
g
g primitive, and 
D
=
{
b
+
i
:
1
≤
i
≤
n
}
D={b+i:1≤i≤n} has 
n
n distinct points.

Enumerate or dynamically count the index fiber

I
=
{
I
∈
(
[
n
]
A
)
:
∑
I
=
s
0
}
.
I={I∈( 
A
[n]
​
 ):∑I=s 
0
​
 }.
Check 
L
≥
N
/
[
A
(
n
−
A
)
+
1
]
L≥N/[A(n−A)+1].

Set 
c
=
A
b
+
s
0
c=Ab+s 
0
​
 , 
M
=
X
A
−
c
X
A
−
1
M=X 
A
 −cX 
A−1
 , and verify for every support:

deg
⁡
(
M
−
L
S
I
)
≤
A
−
2
,
agr
⁡
D
(
M
−
L
S
I
,
M
∣
D
)
=
A
.
deg(M−L 
S 
I
​
 
​
 )≤A−2,agr 
D
​
 (M−L 
S 
I
​
 
​
 ,M∣ 
D
​
 )=A.
Compute and deduplicate

{
L
S
I
(
β
)
:
I
∈
I
}
.
{L 
S 
I
​
 
​
 (β):I∈I}.
Verify the integer receipts

p
2
≥
2
128
N
,
p 
2
 ≥2 
128
 N,
m
−
1
>
C
 
N
/
p
,
m−1>CN/p,
2
128
(
m
−
1
)
>
p
.
2 
128
 (m−1)>p.
Verify intrinsic degree, noncontainment, simple roots, prime-field minimality, and primitive-ratio receipts.

Recommended terminal labels:

COUNTERPACKET_LITERAL
COUNTERPACKET_CYCLE110_APCORR
CHARGED_SHORT_PREFIX_IMAGE
OFFICIAL_APCORR_UNDECIDED
REJECT_BAD_REPLAY
COUNTERPACKET_CYCLE110_APCORR is justified against the explicit Cycle110 structural clauses. OFFICIAL_APCORR_UNDECIDED is mandatory until the official source predicate is supplied.

5. Next exact lemma or construction
EXACT_NEW_WALL
L-CYCLE112-PREFIX-MIN-ENTROPY-OR-PTE-CHARGE.
A viable replacement theorem must require or prove, before analyzing products,

max
⁡
c
#
{
S
∈
(
D
A
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
≤
C
p
r
e
f
(
n
A
)
q
g
e
n
σ
−
1
,
(22)
c
max
​
 #{S∈( 
A
D
​
 ):e 
j
​
 (S)=c 
j
​
 , 1≤j≤σ−1}≤C 
pref
​
  
q 
gen
σ−1
​
 
( 
A
n
​
 )
​
 ,(22)
or assign every violation to an explicit paid charge.

By the bankable lemma, when

q
l
i
n
e
−
n
≥
k
(
max
⁡
c
∣
F
c
∣
−
1
)
,
q 
line
​
 −n≥k( 
c
max
​
 ∣F 
c
​
 ∣−1),
condition (22) is necessary up to a factor two for the desired product-image theorem. Product collision estimates cannot substitute for prefix min-entropy.

The structural charge cannot merely exclude proper subfields or subgroup cosets. At minimum it must detect:

∣
{
(
e
1
(
S
)
,
…
,
e
σ
−
1
(
S
)
)
:
S
∈
(
D
A
)
}
∣
≪
q
g
e
n
σ
−
1
,
​
 {(e 
1
​
 (S),…,e 
σ−1
​
 (S)):S∈( 
A
D
​
 )} 
​
 ≪q 
gen
σ−1
​
 ,
including short restricted sumsets and Prouhet–Tarry–Escott trade cubes.

For the latter, if disjoint local trades 
A
i
,
B
i
A 
i
​
 ,B 
i
​
  satisfy

e
j
(
A
i
)
=
e
j
(
B
i
)
,
1
≤
j
≤
σ
−
1
,
e 
j
​
 (A 
i
​
 )=e 
j
​
 (B 
i
​
 ),1≤j≤σ−1,
then every union obtained by independently choosing 
A
i
A 
i
​
  or 
B
i
B 
i
​
  lies in one prefix fiber. If the ratios

∏
x
∈
B
i
(
β
−
x
)
∏
x
∈
A
i
(
β
−
x
)
∏ 
x∈A 
i
​
 
​
 (β−x)
∏ 
x∈B 
i
​
 
​
 (β−x)
​
 
are multiplicatively dissociated, the product image has size 
2
d
2 
d
 . This tensorization shows that banning a single affine progression alone will not be enough; a robust source theorem needs a bounded PTE-trade-rank or prefix-Fourier-flatness hypothesis.

Mandatory self-audit
Exact implication proved. I proved that the literal Cycle111 occupancy upper bound and the equivalent support/product bound fail, even under prize-strength corrected reserve. I also proved a general lower bound converting a large symmetric prefix fiber into a large product image. I did not prove that the construction passes an unpublished or future official AP_corr.

Relevance. This is a theorem-level counterpacket to the stated route theorem and to the explicit Cycle110 structural AP_corr candidate. Official-prize promotion is conditional only on the missing source-predicate replay.

First possible failure in the reduction chain. The first failure is

K
g
e
n
 has size 
q
g
e
n
⟹
prefix fibers have scale 
N
/
q
g
e
n
σ
−
1
.
K 
gen
​
  has size q 
gen
​
 ⟹prefix fibers have scale N/q 
gen
σ−1
​
 .
That implication is false.

Field and security ledgers. The construction uses

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
No field transfer is used. q_chal is unused. Corrected reserve is checked as 
p
2
≥
2
128
N
p 
2
 ≥2 
128
 N, and the final failure is checked as 
2
128
(
m
−
1
)
>
p
2 
128
 (m−1)>p.

Possible numerator reductions. Same-slope collisions are explicitly deduplicated. Quotient and action-rank reductions are vacuous at 
t
=
1
t=1. Contained and tangent incidences are absent. Field confinement is absent. One endpoint is paid. A fixed affine normalization is cardinality-preserving. The only unresolved route is a new periodic/short-prefix/PTE charge not currently frozen.

Conversion to official status. Freeze the official AP_corr and run the listed receipts. If it accepts the datum, this is SOURCE_VALID_LOW_T1_COUNTERPACKET. If it rejects it, the rejection must be recorded as the exact new hypothesis or charge—most naturally SHORT_RESTRICTED_PREFIX_IMAGE or PTE_TRADE_RANK.
