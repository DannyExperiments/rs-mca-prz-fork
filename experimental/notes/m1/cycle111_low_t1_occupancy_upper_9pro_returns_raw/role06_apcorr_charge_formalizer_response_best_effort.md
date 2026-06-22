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

# Role 06: AP_corr And Charge Formalizer

Freeze the source predicate and charge ledger needed for the t=1 wall.

Focus points:

1. Define a noncircular AP_corr predicate that is strong enough to support
   L-CYCLE111-LOW-T1-OCCUPANCY-UPPER but does not simply restate the desired
   bound.
2. Prove which charges are impossible or vacuous at t=1.
3. Prove which failures of the occupancy theorem must map to endpoint, field,
   affine-color, tangent, contained, hidden-action-rank, quotient, periodic, or
   retained-normalization charges.
4. If no such predicate can exist, give the formal impossibility mechanism.

Ambition bar: convert the current informal source-validity language into a
lemma that a checker/referee can enforce.

I’ll inspect the packet and required audit files, then formalize a noncircular AP_corr/charge ledger for the t=1 wall while checking which charges are vacuous or enforceable.

The first unresolved step appears definitional: prior AP_corr candidates are either too weak or circular, so I’m isolating a checker-enforceable version and testing surviving t=1 charges.

A concrete obstruction is emerging: arbitrary words may contain sparse disjoint RS patches whose isolated agreement supports create many colors after the usual t=1 algebraic charges vanish.

Thought for 25m 59s
1. Executive verdict and confidence
COUNTERPACKET — literal theorem only, not yet a source-valid prize counterpacket.

L-CYCLE111-LOW-T1-OCCUPANCY-UPPER is false as stated for arbitrary words 
w
w, even under the Cycle110 corrected-reserve inequality

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
There is an explicit infinite family of words formed from disjoint local Reed–Solomon patches for which the number of evaluation colors exceeds every bound

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
C 
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
 
with fixed absolute 
C
C.

This is not yet a SOURCE_VALID_LOW_T1_COUNTERPACKET, because the packet never freezes the source definitions of AP_corr, affine-color, support-periodic, or tangent charges. The construction is visibly an affine-color/local-patch obstruction and a legitimate source predicate may reject it.

The strongest exact replacement is:

BANKABLE_LEMMA. At 
t
=
1
t=1, every occupancy failure decomposes into:

a quantitatively controlled heavy-color term at the desired calibrated scale; and

a new, mechanically certifiable LOW_T1_LIGHT_COLOR_PACKING charge.

A noncircular sufficient predicate can be frozen using Fourier flatness of the interpolation-obstruction map. The missing official implication is precisely:

source 
A
P
c
o
r
r
⟹
interpolation-prefix Fourier flatness or a paid light-color charge
.
source AP 
corr
​
 ⟹interpolation-prefix Fourier flatness or a paid light-color charge.
Confidence:

Literal counterexample: high.

Heavy/light decomposition and spectral predicate: high.

Claim that existing official affine-color or periodic charges necessarily absorb the construction: unknown, because their predicates are not specified in the packet.

Source-valid prize counterpacket status: not established.

2. Exact statements
COUNTERPACKET — arbitrary-word occupancy theorem is false
Fix 
k
=
1
k=1. For integers 
s
≥
2
s≥2 and 
m
≥
1
m≥1, put

σ
=
s
,
a
=
k
+
σ
=
s
+
1
,
n
=
a
m
.
σ=s,a=k+σ=s+1,n=am.
Choose a prime

n
<
p
<
2
n
,
n<p<2n,
let

K
g
e
n
=
K
l
i
n
e
=
K
c
o
d
e
=
F
p
,
K 
gen
​
 =K 
line
​
 =K 
code
​
 =F 
p
​
 ,
take

D
=
{
1
,
…
,
n
}
⊂
F
p
,
β
=
0
,
D={1,…,n}⊂F 
p
​
 ,β=0,
and partition 
D
D into 
m
m disjoint blocks 
S
1
,
…
,
S
m
S 
1
​
 ,…,S 
m
​
 , each of size 
a
a.

Choose distinct 
c
1
,
…
,
c
m
∈
F
p
c 
1
​
 ,…,c 
m
​
 ∈F 
p
​
 , and define

Q
i
(
X
)
=
X
+
c
i
,
w
(
x
)
=
Q
i
(
x
)
(
x
∈
S
i
)
.
Q 
i
​
 (X)=X+c 
i
​
 ,w(x)=Q 
i
​
 (x)(x∈S 
i
​
 ).
Then

deg
⁡
Q
i
≤
1
=
k
,
agr
⁡
D
(
Q
i
,
w
)
=
a
=
k
+
σ
,
degQ 
i
​
 ≤1=k,agr 
D
​
 (Q 
i
​
 ,w)=a=k+σ,
and

Q
i
(
β
)
=
c
i
Q 
i
​
 (β)=c 
i
​
 
are all distinct. Consequently

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
≥
m
.
∣{Q(β):degQ≤k, agr 
D
​
 (Q,w)≥k+σ}∣≥m.
Taking 
m
=
s
m=s and letting 
s
→
∞
s→∞, this violates the proposed inequality for every fixed 
C
C, while corrected reserve eventually holds.

Indeed,

(
n
s
+
1
)
≤
(
e
n
s
+
1
)
s
+
1
=
(
e
s
)
s
+
1
,
( 
s+1
n
​
 )≤( 
s+1
en
​
 ) 
s+1
 =(es) 
s+1
 ,
whereas

p
s
>
n
s
=
(
(
s
+
1
)
s
)
s
.
p 
s
 >n 
s
 =((s+1)s) 
s
 .
Hence

p
s
2
128
(
n
s
+
1
)
>
(
s
+
1
)
s
2
128
e
s
+
1
s
⟶
∞
.
2 
128
 ( 
s+1
n
​
 )
p 
s
 
​
 > 
2 
128
 e 
s+1
 s
(s+1) 
s
 
​
 ⟶∞.
Thus the 
128
128-bit corrected reserve holds for all sufficiently large 
s
s.

On the other hand,

(
n
s
+
1
)
p
s
−
1
<
n
2
(
s
+
1
)
!
,
p 
s−1
 
( 
s+1
n
​
 )
​
 < 
(s+1)!
n 
2
 
​
 ,
so the proposed right-hand side is less than

C
 
(
(
s
+
1
)
s
)
2
(
s
+
1
)
!
.
C 
(s+1)!
((s+1)s) 
2
 
​
 .
Factorial growth gives

C
 
(
(
s
+
1
)
s
)
2
(
s
+
1
)
!
<
s
=
m
C 
(s+1)!
((s+1)s) 
2
 
​
 <s=m
for all sufficiently large 
s
s.

Therefore no absolute 
C
C proves the arbitrary-word statement.

Explicit 128-bit ledger stress instance
Set

s
=
64
,
m
=
2
128
,
a
=
65
,
n
=
65
⋅
2
128
.
s=64,m=2 
128
 ,a=65,n=65⋅2 
128
 .
Choose 
p
p with 
n
<
p
<
2
n
n<p<2n.

Then

p
64
2
128
(
n
65
)
>
65
64
2
256
e
65
>
1
,
2 
128
 ( 
65
n
​
 )
p 
64
 
​
 > 
2 
256
 e 
65
 
65 
64
 
​
 >1,
so the standard Cycle110 corrected reserve holds.

But

∣
Z
1
∣
≥
m
=
2
128
,
∣Z 
1
​
 ∣≥m=2 
128
 ,
whereas

q
l
i
n
e
2
128
=
p
2
128
<
130.
2 
128
 
q 
line
​
 
​
 = 
2 
128
 
p
​
 <130.
Thus this packet exceeds the 
2
−
128
2 
−128
  line-field budget by an enormous factor.

It is not promoted to SOURCE_VALID_LOW_T1_COUNTERPACKET, because it is a block-affine pencil and may correctly trigger the still-undefined affine-color or source-aperiodicity predicate.

BANKABLE_LEMMA — exact witness-support incidence formalism
Let

a
=
k
+
σ
,
r
=
σ
−
1
,
a=k+σ,r=σ−1,
and define

F
w
=
{
S
∈
(
D
a
)
:
∃
Q
S
,
 
deg
⁡
Q
S
≤
k
,
 
Q
S
∣
S
=
w
∣
S
}
.
F 
w
​
 ={S∈( 
a
D
​
 ):∃Q 
S
​
 , degQ 
S
​
 ≤k, Q 
S
​
 ∣ 
S
​
 =w∣ 
S
​
 }.
Because 
a
>
k
a>k, the polynomial 
Q
S
Q 
S
​
  is unique whenever it exists.

Define the color map

χ
β
:
F
w
→
K
l
i
n
e
,
χ
β
(
S
)
=
Q
S
(
β
)
.
χ 
β
​
 :F 
w
​
 →K 
line
​
 ,χ 
β
​
 (S)=Q 
S
​
 (β).
Then exactly

Z
β
(
w
)
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
a
}
=
χ
β
(
F
w
)
.
Z 
β
​
 (w)={Q(β):degQ≤k, agr 
D
​
 (Q,w)≥a}=χ 
β
​
 (F 
w
​
 ).
For 
z
∈
Z
β
(
w
)
z∈Z 
β
​
 (w), define the support multiplicity

μ
(
z
)
=
∣
χ
β
−
1
(
z
)
∣
.
μ(z)=∣χ 
β
−1
​
 (z)∣.
Then

∑
z
∈
Z
β
(
w
)
μ
(
z
)
=
∣
F
w
∣
≤
(
n
a
)
.
z∈Z 
β
​
 (w)
∑
​
 μ(z)=∣F 
w
​
 ∣≤( 
a
n
​
 ).
For an integer threshold 
H
≥
1
H≥1, split

Z
β
=
Z
h
e
a
v
y
⊔
Z
l
i
g
h
t
,
Z 
β
​
 =Z 
heavy
​
 ⊔Z 
light
​
 ,
where

Z
h
e
a
v
y
=
{
z
:
μ
(
z
)
≥
H
}
.
Z 
heavy
​
 ={z:μ(z)≥H}.
Then:

∣
Z
h
e
a
v
y
∣
≤
(
n
a
)
H
.
∣Z 
heavy
​
 ∣≤ 
H
( 
a
n
​
 )
​
 .
Moreover,

∣
Z
l
i
g
h
t
∣
≤
P
(
n
,
k
,
a
)
:
=
(
n
k
+
1
)
(
a
k
+
1
)
.
∣Z 
light
​
 ∣≤P(n,k,a):= 
( 
k+1
a
​
 )
( 
k+1
n
​
 )
​
 .
The second assertion follows by choosing one witness support 
S
z
S 
z
​
  and one witness polynomial 
Q
z
Q 
z
​
  for each light color. If 
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
≠
Q
z
′
Q 
z
​
 

=Q 
z 
′
 
​
 , and

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
,
∣S 
z
​
 ∩S 
z 
′
 
​
 ∣≤k,
since otherwise 
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
  would have at least 
k
+
1
k+1 roots and hence vanish identically, contradicting

Q
z
(
β
)
=
z
≠
z
′
=
Q
z
′
(
β
)
.
Q 
z
​
 (β)=z

=z 
′
 =Q 
z 
′
 
​
 (β).
Therefore the 
(
k
+
1
)
(k+1)-subsets contained in the chosen 
S
z
S 
z
​
 's are pairwise disjoint.

Consequently, for every 
H
H,

∣
Z
β
(
w
)
∣
≤
(
n
a
)
H
+
∣
Z
l
i
g
h
t
∣
,
∣
Z
l
i
g
h
t
∣
≤
P
(
n
,
k
,
a
)
.
∣Z 
β
​
 (w)∣≤ 
H
( 
a
n
​
 )
​
 +∣Z 
light
​
 ∣,∣Z 
light
​
 ∣≤P(n,k,a).
This is an unconditional theorem.

BANKABLE_LEMMA — a noncircular AP_corr
For each 
S
∈
(
D
a
)
S∈( 
a
D
​
 ), let 
P
S
P 
S
​
  be the unique degree-
<
a
<a interpolation polynomial satisfying

P
S
∣
S
=
w
∣
S
.
P 
S
​
 ∣ 
S
​
 =w∣ 
S
​
 .
Define its interpolation-obstruction vector

Φ
w
(
S
)
=
(
[
X
k
+
1
]
P
S
,
…
,
[
X
a
−
1
]
P
S
)
∈
K
l
i
n
e
 
r
.
Φ 
w
​
 (S)=([X 
k+1
 ]P 
S
​
 ,…,[X 
a−1
 ]P 
S
​
 )∈K 
line
r
​
 .
Then

S
∈
F
w
  
⟺
  
Φ
w
(
S
)
=
0.
S∈F 
w
​
 ⟺Φ 
w
​
 (S)=0.
Fix a nontrivial additive character 
ψ
ψ of 
K
l
i
n
e
K 
line
​
 . For
λ
∈
K
l
i
n
e
r
λ∈K 
line
r
​
 , put

ν
^
w
(
λ
)
=
∑
S
∈
(
D
a
)
ψ
(
λ
⋅
Φ
w
(
S
)
)
.
ν
  
w
​
 (λ)= 
S∈( 
a
D
​
 )
∑
​
 ψ(λ⋅Φ 
w
​
 (S)).
Define the normalized spectral defect

Corr
⁡
1
(
Φ
w
)
:
=
q
g
e
n
 
r
(
n
a
)
 
q
l
i
n
e
 
r
∑
λ
≠
0
∣
ν
^
w
(
λ
)
∣
.
Corr 
1
​
 (Φ 
w
​
 ):= 
( 
a
n
​
 )q 
line
r
​
 
q 
gen
r
​
 
​
  
λ

=0
∑
​
 ∣ 
ν
  
w
​
 (λ)∣.
Freeze the predicate

A
P
c
o
r
r
T
1
(
A
)
:
Corr
⁡
1
(
Φ
w
)
≤
A
,
AP 
corr
T1
​
 (A):Corr 
1
​
 (Φ 
w
​
 )≤A,
where 
A
A is an explicit absolute constant.

This predicate is noncircular:

it does not mention 
β
β;

it does not mention evaluation colors or 
∣
Z
β
∣
∣Z 
β
​
 ∣;

it controls every nontrivial Fourier mode of the source-visible interpolation obstruction;

it is invariant under adding a degree-
≤
k
≤k polynomial to 
w
w;

it is invariant under nonzero scaling of 
w
w;

under an affine change of the 
X
X-coordinate, the obstruction vector is transformed by an invertible triangular linear map, so the Fourier spectrum is merely reindexed.

Conditional source-route theorem
If 
A
P
c
o
r
r
T
1
(
A
)
AP 
corr
T1
​
 (A) holds, then for every 
β
∉
D
β∈
/
D,

∣
Z
β
(
w
)
∣
≤
(
A
+
1
)
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
∣Z 
β
​
 (w)∣≤(A+1) 
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
 .
Thus L-CYCLE111-LOW-T1-OCCUPANCY-UPPER holds with

C
=
A
+
1
C=A+1
under this explicitly frozen predicate.

For the monic-anchor word 
w
=
M
∣
D
w=M∣ 
D
​
 , with 
M
M monic of degree 
a
a, one has

P
S
=
M
−
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
P 
S
​
 =M− 
x∈S
∏
​
 (X−x).
Hence 
Φ
w
(
S
)
=
0
Φ 
w
​
 (S)=0 is precisely

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
1.
e 
j
​
 (S)=c 
j
​
 ,1≤j≤σ−1.
Therefore this same predicate proves the product-image target on every elementary-symmetric prefix fiber.

ROUTE_CUT — the current charge list is incomplete without a sparse-color term
Every failure of the desired occupancy bound first produces one of two exact certificates:

PREFIX_SPECTRAL_CONCENTRATION: a nonzero Fourier mode of 
Φ
w
Φ 
w
​
  is large;

LOW_T1_LIGHT_COLOR_PACKING: many colors have support multiplicity below the calibrated threshold.

The currently named 
t
=
1
t=1 algebraic charges do not automatically cover the second mechanism.

A block-affine packet has:

intrinsic 
t
=
1
t=1;

no residue quotient or hidden action-rank loss;

no contained incidence;

no field confinement in a prime field;

no same-slope collisions;

identity normalization;

simple, distinct agreement points;

but it can have arbitrarily many isolated evaluation colors.

Therefore a source predicate formed only from the negations of quotient, hidden-action-rank, contained, field, endpoint, and normalization charges cannot imply the target. It must additionally control interpolation-prefix concentration, affine-color fragmentation, or light-color support packets.

EXACT_NEW_WALL
The source-valid next theorem is:

L-CYCLE111-SOURCE-APCORR-TO-T1-PREFIX-FLATNESS-OR-LIGHT-COLOR-CHARGE.

For every official intrinsic t=1 LOW datum, source AP_corr implies either

  (i) AP_corr^T1(A), with explicit absolute A;

or

  (ii) a mechanically certified endpoint, field, affine-color,
       tangent, support-periodic, or retained-normalization charge;

or

  (iii) LOW_T1_LIGHT_COLOR_PACKING, with a certified cap
        binom(n,k+1)/binom(k+sigma,k+1).

Contained, residue-quotient, and hidden-action-rank terminals are forbidden
at t=1.
Without clause (iii), this implication is false for arbitrary words.

3. Proofs and charge audit
3.1 Proof of the spectral AP_corr theorem
By additive-character orthogonality,

1
{
Φ
w
(
S
)
=
0
}
=
1
q
l
i
n
e
r
∑
λ
∈
K
l
i
n
e
r
ψ
(
λ
⋅
Φ
w
(
S
)
)
.
1 
{Φ 
w
​
 (S)=0}
​
 = 
q 
line
r
​
 
1
​
  
λ∈K 
line
r
​
 
∑
​
 ψ(λ⋅Φ 
w
​
 (S)).
Summing over 
S
∈
(
D
a
)
S∈( 
a
D
​
 ),

∣
F
w
∣
=
(
n
a
)
q
l
i
n
e
r
+
1
q
l
i
n
e
r
∑
λ
≠
0
ν
^
w
(
λ
)
.
∣F 
w
​
 ∣= 
q 
line
r
​
 
( 
a
n
​
 )
​
 + 
q 
line
r
​
 
1
​
  
λ

=0
∑
​
  
ν
  
w
​
 (λ).
Therefore

∣
F
w
∣
≤
(
n
a
)
q
l
i
n
e
r
+
1
q
l
i
n
e
r
∑
λ
≠
0
∣
ν
^
w
(
λ
)
∣
.
∣F 
w
​
 ∣≤ 
q 
line
r
​
 
( 
a
n
​
 )
​
 + 
q 
line
r
​
 
1
​
  
λ

=0
∑
​
 ∣ 
ν
  
w
​
 (λ)∣.
If 
Corr
⁡
1
(
Φ
w
)
≤
A
Corr 
1
​
 (Φ 
w
​
 )≤A, the second term is at most

A
(
n
a
)
q
g
e
n
r
.
A 
q 
gen
r
​
 
( 
a
n
​
 )
​
 .
Since 
K
g
e
n
⊆
K
l
i
n
e
K 
gen
​
 ⊆K 
line
​
 ,

q
g
e
n
≤
q
l
i
n
e
,
q 
gen
​
 ≤q 
line
​
 ,
and hence

(
n
a
)
q
l
i
n
e
r
≤
(
n
a
)
q
g
e
n
r
.
q 
line
r
​
 
( 
a
n
​
 )
​
 ≤ 
q 
gen
r
​
 
( 
a
n
​
 )
​
 .
Thus

∣
F
w
∣
≤
(
A
+
1
)
(
n
a
)
q
g
e
n
r
.
∣F 
w
​
 ∣≤(A+1) 
q 
gen
r
​
 
( 
a
n
​
 )
​
 .
Finally,

∣
Z
β
(
w
)
∣
=
∣
χ
β
(
F
w
)
∣
≤
∣
F
w
∣
.
∣Z 
β
​
 (w)∣=∣χ 
β
​
 (F 
w
​
 )∣≤∣F 
w
​
 ∣.
No 
q
c
o
d
e
q 
code
​
  or 
q
c
h
a
l
q 
chal
​
  denominator is used.

Converse failure certificate
If

∣
Z
β
(
w
)
∣
>
C
(
n
a
)
q
g
e
n
r
,
∣Z 
β
​
 (w)∣>C 
q 
gen
r
​
 
( 
a
n
​
 )
​
 ,
then 
∣
F
w
∣
∣F 
w
​
 ∣ exceeds the same quantity. Consequently

Corr
⁡
1
(
Φ
w
)
>
C
−
(
q
g
e
n
q
l
i
n
e
)
r
≥
C
−
1.
Corr 
1
​
 (Φ 
w
​
 )>C−( 
q 
line
​
 
q 
gen
​
 
​
 ) 
r
 ≥C−1.
In particular, some nonzero 
λ
λ satisfies

∣
ν
^
w
(
λ
)
∣
>
(
n
a
)
 
q
l
i
n
e
r
q
g
e
n
r
(
q
l
i
n
e
r
−
1
)
(
C
−
(
q
g
e
n
q
l
i
n
e
)
r
)
.
∣ 
ν
  
w
​
 (λ)∣> 
q 
gen
r
​
 (q 
line
r
​
 −1)
( 
a
n
​
 )q 
line
r
​
 
​
 (C−( 
q 
line
​
 
q 
gen
​
 
​
 ) 
r
 ).
Thus every occupancy violation has a precise Fourier witness.

3.2 Charges at 
t
=
1
t=1
Write

E
=
X
−
β
,
B
 
m
o
d
 
E
=
b
∈
K
l
i
n
e
×
.
E=X−β,BmodE=b∈K 
line
×
​
 .
The slope 
z
z and evaluation color 
Q
(
β
)
Q(β) differ only by the fixed bijection

Q
(
β
)
=
b
z
.
Q(β)=bz.
Quotient and hidden action rank: vacuous
The residue algebra is

A
E
=
K
l
i
n
e
[
X
]
/
(
X
−
β
)
≅
K
l
i
n
e
.
A 
E
​
 =K 
line
​
 [X]/(X−β)≅K 
line
​
 .
For every source-visible rational 
R
R defined modulo 
E
E,

R
(
[
X
]
E
)
=
R
(
β
)
∈
K
l
i
n
e
,
R([X] 
E
​
 )=R(β)∈K 
line
​
 ,
so

dim
⁡
K
l
i
n
e
K
l
i
n
e
[
R
(
β
)
]
=
1
=
t
.
dim 
K 
line
​
 
​
 K 
line
​
 [R(β)]=1=t.
No charge of the form 
d
R
(
E
)
<
t
d 
R
​
 (E)<t can occur.

There is also no nonzero proper unital 
K
l
i
n
e
K 
line
​
 -algebra quotient of 
A
E
A 
E
​
 .

Contained and delete-
j
j: vacuous
Suppose 
deg
⁡
G
<
k
degG<k and

(
X
−
β
)
G
+
b
(X−β)G+b
vanishes on at least

k
+
σ
−
j
k+σ−j
points of 
D
D. Its degree is at most 
k
k. For 
j
≤
σ
−
1
j≤σ−1,

k
+
σ
−
j
≥
k
+
1.
k+σ−j≥k+1.
It must therefore be the zero polynomial, but evaluating at 
β
β gives 
b
=
0
b=0, a contradiction.

Hence all contained/delete-
j
j charges with

j
≤
σ
−
1
j≤σ−1
are empty.

Same-slope collisions: already collapsed
If distinct 
Q
,
Q
′
Q,Q 
′
  have

Q
(
β
)
=
Q
′
(
β
)
,
Q(β)=Q 
′
 (β),
then 
Q
−
Q
′
Q−Q 
′
  has the off-domain root 
β
β. Therefore their agreement sets with 
w
w can intersect in at most 
k
−
1
k−1 points. The color count already deduplicates all such polynomials.

Normalization
The direct normalization by 
b
−
1
b 
−1
  is a fixed bijection of 
K
l
i
n
e
K 
line
​
 , and 
E
(
x
)
≠
0
E(x)

=0 on 
D
D. No normalization pole or loss of injectivity occurs.

Any support-dependent normalization introduced later must retain its chart tag; it cannot silently merge colors.

Field
Field confinement is not vacuous at 
t
=
1
t=1. If the free colors lie in an affine copy of a proper subfield 
K
′
K 
′
 , they are capped by 
∣
K
′
∣
∣K 
′
 ∣. It is absent in the prime-field construction above.

Affine color
Affine-color concentration is not vacuous. The block-patch counterexample is exactly an affine-pencil packet

Q
i
=
R
+
c
i
.
Q 
i
​
 =R+c 
i
​
 .
A source predicate may correctly charge or exclude it. But the cap must count retained distinct colors; it cannot be declared “paid” when that cap itself exceeds 
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
 .

Tangent
The literal 
t
=
1
t=1 interpolation problem uses distinct simple points and no Hasse derivatives. Thus the residue reduction itself creates no tangent multiplicity.

However, the packet does not define the official tangent predicate. A tangent/singular-phase charge cannot be declared universally vacuous without that definition.

Periodic
This is the exact overstatement in the Cycle110 audit:

periodicity arising from a proper quotient or composition of the degree-one residue algebra is vacuous;

periodicity or quotient structure of the support family or word 
w
w is not vacuous.

Thus “periodic is vacuous at 
t
=
1
t=1” is valid only in the residue-algebra sense.

Endpoint
The literal model has 
β
∉
D
β∈
/
D, so there is no denominator endpoint on 
D
D. An official endpoint-first source partition may nevertheless contribute its external cap, reportedly at most one. That cap requires a separate ledger receipt.

3.3 Corrected-reserve transfer
Under 
A
P
c
o
r
r
T
1
(
A
)
AP 
corr
T1
​
 (A),

∣
Z
β
∣
≤
(
A
+
1
)
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
∣Z 
β
​
 ∣≤(A+1) 
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
 .
If corrected reserve explicitly contains

q
g
e
n
σ
≥
2
128
(
A
+
1
)
(
n
a
)
,
q 
gen
σ
​
 ≥2 
128
 (A+1)( 
a
n
​
 ),
then

2
128
∣
Z
β
∣
≤
q
g
e
n
≤
q
l
i
n
e
.
2 
128
 ∣Z 
β
​
 ∣≤q 
gen
​
 ≤q 
line
​
 .
This is the exact 
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
  transfer. It uses only the certified field inclusion

K
g
e
n
⊆
K
l
i
n
e
.
K 
gen
​
 ⊆K 
line
​
 .
It does not use 
q
c
o
d
e
q 
code
​
 , and 
q
c
h
a
l
q 
chal
​
  remains unusable.

If endpoint, light-color, field, tangent, periodic, or normalization charges are added, one must check the full integer inequality

2
128
(
⌈
(
A
+
1
)
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
⌉
+
N
c
h
a
r
g
e
d
)
≤
q
l
i
n
e
.
2 
128
 (⌈(A+1) 
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
 ⌉+N 
charged
​
 )≤q 
line
​
 .
The calibrated main term cannot consume the entire budget and then silently add polynomial charges.

4. Verification and replay requirements
A deterministic checker should accept:

K_line representation
K_gen embedding into K_line
D, beta, w
k, sigma
E = X-beta and B mod E
A or H
source charge certificates
corrected-reserve receipt
It must:

Verify 
a
=
k
+
σ
≤
n
a=k+σ≤n, distinct 
D
D, and 
β
∉
D
β∈
/
D.

Verify 
E
=
X
−
β
E=X−β, 
B
 
m
o
d
 
E
≠
0
BmodE

=0, and intrinsic 
t
=
1
t=1.

Enumerate every 
a
a-subset 
S
⊆
D
S⊆D, interpolate 
P
S
P 
S
​
 , and compute 
Φ
w
(
S
)
Φ 
w
​
 (S).

Record every admissible support with 
Φ
w
(
S
)
=
0
Φ 
w
​
 (S)=0, its color 
P
S
(
β
)
P 
S
​
 (β), and multiplicity 
μ
(
z
)
μ(z).

Deduplicate colors in 
K
l
i
n
e
K 
line
​
 .

Verify the heavy bound and, for a light-color certificate, choose one support per color and check pairwise intersections are at most 
k
k.

Reject any contained or hidden-action-rank certificate at 
t
=
1
t=1.

Require explicit certificates for field, affine-color, support-periodic, tangent, endpoint, or normalization charges.

Verify the integer ledger using 
q
l
i
n
e
q 
line
​
 , never 
q
c
h
a
l
q 
chal
​
 .

Exact terminal labels:

T1_APCORR_SPECTRAL_PASS
T1_OCCUPANCY_CERTIFIED
T1_PREFIX_SPECTRAL_CONCENTRATION
T1_LIGHT_COLOR_PACKING
T1_FIELD_CHARGE
T1_AFFINE_COLOR_CHARGE
T1_SUPPORT_PERIODIC_CHARGE
T1_TANGENT_CHARGE
T1_ENDPOINT_CHARGE
T1_NORMALIZATION_CHARGE
T1_LEDGER_UNPAID
MODEL_LOW_T1_COUNTERPACKET
SOURCE_APCORR_RECEIPT_MISSING
SOURCE_VALID_LOW_T1_COUNTERPACKET
The checker may emit SOURCE_VALID_LOW_T1_COUNTERPACKET only when it also receives:

the frozen official source AP_corr predicate evaluated true;

exact negative or paid certificates for every named charge;

the official corrected-reserve inequality;

the strict integer inequality

∣
Z
β
∣
>
⌊
q
l
i
n
e
/
2
128
⌋
.
∣Z 
β
​
 ∣>⌊q 
line
​
 /2 
128
 ⌋.
The block-affine family currently terminates at MODEL_LOW_T1_COUNTERPACKET or T1_AFFINE_COLOR_CHARGE, not at the source-valid label.

5. Next exact lemma or construction
EXACT_NEW_WALL
Prove:

L-CYCLE111-SOURCE-APCORR-DESCENT-TO-PREFIX-FOURIER-FLATNESS-OR-SPARSE-CHARGE.

Source AP_corr for an intrinsic t=1 datum implies one of:

1. Corr_1(Phi_w) <= A for an explicit absolute A;
2. a paid field, affine-color, support-periodic, tangent, endpoint,
   or retained-normalization charge;
3. a LOW_T1_LIGHT_COLOR_PACKING certificate whose exact cap fits the
   q_line ledger.
The matching counterpacket construction is:

GENERIC_BLOCK_PATCH_COUNTERPACKET:

prime same field;
intrinsic t=1;
prize-strength corrected reserve;
many disjoint threshold-agreement patches;
patch polynomials not contained in a bounded affine pencil;
generic support partition defeating support-periodic tags;
simple intersections defeating tangent tags;
distinct full-field evaluation colors;
source AP_corr independently certified;
occupancy greater than floor(q_line/2^128).
The existing affine-pencil packet already supplies the reserve and occupancy arithmetic. The missing step is to replace its common affine direction by a generic patch family and replay the frozen affine-color, periodic, tangent, and source-AP_corr predicates.

Mandatory self-audit
Exact implication proved and not proved.
Proved: the arbitrary-word target is false; the witness-support representation; the heavy-color and light-color packing bounds; the Fourier AP_corr implication; 
t
=
1
t=1 contained and action-rank vacuity; the typed reserve transfer.
Not proved: that official source AP_corr implies the spectral predicate; that every spectral failure maps to an existing paid charge; or that the explicit packet passes official source AP_corr.

Relevance level.
The counterexample is an exact theorem-level refutation of the literal target and an official-route warning. The Fourier result is a conditional source-route theorem and q-ledger theorem. The explicit 
s
=
64
s=64 packet is a model counterpacket until source predicates are replayed.

First possible failure in the reduction chain.
The first unsupported implication is

source 
A
P
c
o
r
r
⟹
A
P
c
o
r
r
T
1
(
A
)
 or a paid sparse/affine/periodic charge
.
source AP 
corr
​
 ⟹AP 
corr
T1
​
 (A) or a paid sparse/affine/periodic charge.
Without this implication, arbitrary fragmented words defeat the target.

Field and 
2
−
128
2 
−128
  usage.
q
g
e
n
q 
gen
​
  appears only in the interpolation entropy scale and corrected reserve.
q
l
i
n
e
q 
line
​
  counts colors and is the sole final security denominator.
q
c
o
d
e
q 
code
​
  supplies no denominator.
q
c
h
a
l
q 
chal
​
  is unused.
The exact target is 
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

Could named structures reduce the numerator?
Quotient and hidden action rank cannot at 
t
=
1
t=1. Contained cannot. Same-slope collisions are deduplicated. Field, affine-color, support periodicity, tangent, endpoint, and retained normalization can reduce or charge the numerator only with explicit certificates. The block packet is plausibly affine-color charged; this is why it is not claimed source-valid.

Converter to PROOF or COUNTERPACKET.
PROOF requires the source descent theorem above plus exact charge caps and the final integer ledger.
COUNTERPACKET requires a genericized block-patch family that passes the frozen source AP_corr and all remaining charge checks while retaining the already-proved reserve and 
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
  violation.