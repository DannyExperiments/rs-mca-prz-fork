BANKABLE_LEMMA

Verdict — confidence high. No fatal flaw appears in the 464-point construction. Assuming a concrete y∈F
17
48
	​

∖F
0
	​

 satisfies μ
proj
	​

(y)≤8, the construction is one [464,232] GRS code, one transverse affine syndrome line, and it clears the official finite target.

The missing result is still the explicit separator census. In particular, the present material does not prove μ
proj
	​

(U)≤8.

Bankable conditional theorem

Let

F
0
	​

=F
17
	​

[X]/(X
16
+X
8
+3),D=⟨η⟩=μ
256
	​

,β=X+2.

Let P
0
	​

 be the banked packet, with

P=∣P
0
	​

∣=52747567104,N=
	​

{P
T
	​

(β):T∈P
0
	​

}
	​

=52747567092.

Every T∈P
0
	​

 avoids μ
32
	​

∖{1}. Set

Z
0
	​

={η
8b
:1≤b≤24},D
−
=D∖Z
0
	​

,

so ∣D
−
∣=232 and every packet support remains contained in D
−
.

Take E=F
17
48
	​

, choose y∈E∖F
0
	​

, and set c=β−y. Define

D
y
	​

=D
−
⊔(c+D
−
),∣D
y
	​

∣=464,

and

S(T
1
	​

,T
2
	​

)=T
1
	​

⊔(c+T
2
	​

),∣S(T
1
	​

,T
2
	​

)∣=226.

Then there is a single [464,232] GRS code C
y
	​

 and a single affine syndrome line such that every S(T
1
	​

,T
2
	​

) is a full-coordinate transverse incidence, with line parameter

z
T
1
	​

,T
2
	​

	​

=
P
T
1
	​

	​

(β)P
T
2
	​

	​

(y)
1
	​


up to one common affine bijection.

If

μ
proj
	​

(y)=
κ∈E
×
/F
0
×
	​

max
	​

#{T∈P
0
	​

:[P
T
	​

(y)]=κ}≤8,

then

M
C
y
	​

	​

(6)≥
8
NP
	​

=347788229344751517696>338617018271848945628=⌊
2
128
17
48
	​

⌋.
Proof of the 464 construction
One GRS code

For x∈D
y
	​

, use the parity-check column

h
x
	​

=
	​

1
x
⋮
x
230
(β−x)
−1
	​

	​

∈E
232
.

Here β∈
/
D
y
	​

: it is not in D, and β=c+d would imply y=d∈F
0
	​

.

Multiply column h
x
	​

 by the nonzero scalar β−x. The resulting rows are evaluations of

1,β−Y,Y(β−Y),…,Y
230
(β−Y).

These form a basis of E[Y]
≤231
	​

, since every polynomial f of degree at most 231 has the unique decomposition

f(Y)=f(β)+(β−Y)Q(Y),degQ≤230.

Thus the 232×464 matrix is row- and nonzero-column-equivalent to a Vandermonde parity-check matrix. Its kernel is one [464,232] GRS code.

The word “shortening” must not be interpreted as ordinary puncturing while preserving an old dimension. That assertion would be false. The valid statement is that the deleted coordinates are unused by all witnesses and the displayed matrix independently defines a new [464,232] GRS code.

One affine syndrome line

For a packet support T, write

J
T
	​

(t)=
x∈T
∏
	​

(1−xt).

The banked common-jet identity is

J
T
	​

(t)≡1−t(modt
6
).

Translation gives

J
c+T
	​

(t)=(1−ct)
113
J
T
	​

(
1−ct
t
	​

)≡(1−ct)
112
(1−(c+1)t)(modt
6
).

Hence every combined support S=T
1
	​

⊔(c+T
2
	​

) has the same six-jet

J
S
	​

(t)≡(1−t)(1−ct)
112
(1−(c+1)t)(modt
6
).

Write

J
S
	​

(t)
−1
≡h
0
	​

+h
1
	​

t+⋯+h
5
	​

t
5
(modt
6
);

the h
i
	​

 are independent of T
1
	​

,T
2
	​

.

Let P
S
	​

(Y)=∏
x∈S
	​

(Y−x) and a
x
	​

=P
S
′
	​

(x)
−1
. Partial fractions give

P
S
	​

(Y)
1
	​

=
x∈S
∑
	​

Y−x
a
x
	​

	​

.

Comparison at infinity yields

x∈S
∑
	​

a
x
	​

x
r
={
0,
h
r−225
	​

,
	​

0≤r≤224,
225≤r≤230.
	​


Evaluation at Y=β gives

x∈S
∑
	​

β−x
a
x
	​

	​

=
P
S
	​

(β)
1
	​

.

Consequently all supports hit the one affine line

ℓ(z)=(
225
0,…,0
	​

	​

,h
0
	​

,…,h
5
	​

,z)⊂E
232

at

z=P
S
	​

(β)
−1
.

Moreover,

P
S
	​

(β)=P
T
1
	​

	​

(β)P
c+T
2
	​

	​

(β)=P
T
1
	​

	​

(β)P
T
2
	​

	​

(y).

This is the reciprocal-product composition. There are not two independent syndrome coordinates.

Transversality and full coordinates

Every a
x
	​

=P
S
′
	​

(x)
−1
 is nonzero because S is squarefree.

The direction of the line is e
232
	​

. If e
232
	​

 lay in the span of the columns indexed by S, projection onto the first 231 coordinates would give a linear dependence among the 226 distinct columns

(1,x,…,x
230
)
T
,x∈S.

The 231×226 Vandermonde matrix has full column rank. Hence the incidence is transverse and no support span contains the line.

Exact collision charge

Choose a subset R⊂P
0
	​

 containing one support for each distinct value

ρ(T)=P
T
	​

(β).

Then ∣R∣=N, and ρ is injective on R.

Consider

F:R×P
0
	​

⟶E
×
,F(T
1
	​

,T
2
	​

)=ρ(T
1
	​

)P
T
2
	​

	​

(y).

If two pairs have the same image, then

P
T
2
′
	​

	​

(y)
P
T
2
	​

	​

(y)
	​

=
ρ(T
1
	​

)
ρ(T
1
′
	​

)
	​

∈F
0
×
	​

.

Thus T
2
	​

,T
2
′
	​

 lie in one projective class. For a fixed T
2
	​

 and a fixed product value, ρ(T
1
	​

) is uniquely determined, and hence so is T
1
	​

. Therefore every product fiber has size at most μ
proj
	​

(y).

Reciprocal inversion and any common affine reparametrization are bijections, so they cause no further loss.

The bound 8 is genuinely the required threshold for this coarse argument:

⌊
9
NP
	​

⌋=309145092750890237952<T
line
	​

.

Thus μ≤9 alone would not suffice, although the exact slope occupancy could still clear the target.

Generic existence survives

The canonical candidate U is unproved, but the separator route itself cannot be killed by a failure at U.

Let q
0
	​

=17
16
 and fix any cubic extension E/F
0
	​

. For distinct supports T,T
′
 and λ∈F
0
×
	​

,

P
T
	​

(Y)−λP
T
′
	​

(Y)

is a nonzero polynomial of degree at most 113. For λ

=1, its leading coefficient is 1−λ; for λ=1, distinct monic locators cannot be equal.

Hence the total number of extension elements causing any projective collision is at most

113(q
0
	​

−1)(
2
P
	​

)=7649552973225252456065323325775618181693440.

But

∣E∖F
0
	​

∣=q
0
3
	​

−q
0
	​

=115225400457255426923013053222916919834602504327802018460160.

Therefore some y∈E∖F
0
	​

 has

μ
proj
	​

(y)=1.

This proves mathematical existence inside a cubic extension. It does not identify a replayable coefficient tuple.

Exact correction to the current wall

The statement that

V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS

is “equivalent” to the explicit-separator theorem is false.

The valid implications are

μ
proj
	​

(U)≤8⟹explicit 464 counterpacket,

but neither

some good y⟹μ
proj
	​

(U)≤8

nor

μ
proj
	​

(U)>8⟹two-copy route fails

is valid. U is only the canonical first candidate.

Narrower replay checker materialized

For E=F
0
	​

[U]/(U
3
−β), the projective group has order

Q=∣E
×
/F
0
×
	​

∣=q
0
2
	​

+q
0
	​

+1.

It has the smooth 66-bit divisor

A
	​

=3⋅7⋅13⋅73⋅307⋅1321⋅72337⋅83233
=48661191882642625923.
	​


Projection from the full projective group to its cyclic A-component only merges classes. Therefore

μ
A
	​

(U)≤8⟹μ
proj
	​

(U)≤8.

All prime factors of A are at most 83233, so the 336 slot factors admit exact Pohlig–Hellman logarithms. Also,

A<3⋅2
64
,

allowing the same low-64-bit plus kernel-three exact replay architecture used in Cycle84.

I materialized a deterministic front end which:

verifies 1+7U
2
 as a primitive element;

reproduces the canonical 336 raw slot-factor hash;

emits exact projected slot logs modulo A;

emits the ordered 464-point domain;

verifies injectivity of the 110592-record three-slot table and the 5308416-record four-slot table.

It does not execute the full 52747567104-record census.

Replay front end and emitted artifacts

The exact next checker should be

V-CYCLE87-U-A-PREFILTER-FULL-REPLAY-MMAX8-CENSUS-464

with three stages:

Enumerate all admissible tuples using the exact A-component logs and retain low-64 runs of size at least 9.

Lift those runs to exact residues modulo A.

Only for exact A-runs of size at least 9, replay the full normalized projective keys in E
×
/F
0
×
	​

.

This has no false negatives: every full projective fiber of size at least 9 survives all three filters. A PASS proves the active target; a FAIL must emit nine supports with the same full projective key.

Self-audit

Proved:

μ
proj
	​

(y)≤8⟹one transverse [464,232] GRS line with M
C
	​

(6)>T
line
	​

.

I also proved that some cubic-extension y has μ
proj
	​

(y)=1.
Not proved: μ
proj
	​

(U)≤8, nor any concrete separator census.

The implication is official-profile and prize-relevant: a concrete PASS adds an official finite MCA fail row. The current result and front end remain a research/certification component, not that row and not the full prize theorem.

Given the banked packet and common six-jet, the first unproved line is exactly

μ
proj
	​

(y)≤8

for a concretely emitted y. For the canonical route it is μ
proj
	​

(U)≤8.

The construction uses

q
gen
	​

=q
code
	​

=q
line
	​

=q
chal
	​

=17
48
.

The target is computed only from q
line
	​

:

T
line
	​

=⌊17
48
/2
128
⌋.

F
0
	​

=F
17
16
	​

 is a coefficient subfield, not the target denominator field.

The first-copy double fibers are removed by selecting N representatives. Quotient and periodic structure are charged exactly by μ
proj
	​

. Same-slope collisions are bounded by the projective fiber argument. Contained incidences are excluded by Vandermonde transversality. Common affine normalization and inversion are bijective and cause no numerator loss.

This is not a PLAN. The exact conversion object is the checker
V-CYCLE87-U-A-PREFILTER-FULL-REPLAY-MMAX8-CENSUS-464, or an equivalent explicit-y full projective census.

A route to the active full solve exists: execute that exact checker for U; if its full replay finds a ninefold projective class, move to the lexicographically first separator guaranteed by the cubic root-count theorem.