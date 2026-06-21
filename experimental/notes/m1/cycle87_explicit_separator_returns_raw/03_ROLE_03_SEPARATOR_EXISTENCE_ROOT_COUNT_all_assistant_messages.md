I’ll reconstruct the separator setup from the Cycle84–87 materials, formalize the projective collision locus, and test whether root-counting proves μ
proj
	​

≤8 or exposes a concrete obstruction.

--- ASSISTANT MESSAGE BREAK ---

I’ve separated ordinary scalar collisions from projective collisions, and I’m now testing whether the cubic candidate y=U can be certified or only reduced to a finite exclusion check.

--- ASSISTANT MESSAGE BREAK ---

The root-count route now gives an existential result stronger than needed: inside the fixed cubic field, all but a 6.64×10
−17
 fraction of nonbase elements have μ
proj
	​

=1.

--- ASSISTANT MESSAGE BREAK ---

BANKABLE_LEMMA

Confidence: high. The generic separator theorem is true, and the cubic extension already suffices:

∃y∈L∖F
0
	​

μ
proj
	​

(y)=1.

This proves an existential official-rate 464-point two-copy counterpacket from the banked Cycle84/85 facts. It does not identify a concrete coefficient vector y, and therefore does not close the explicit replay wall or certify the proposed fixed candidate y=U.

Generic projective-separator theorem

Let

q
0
	​

=17
16
=48661191875666868481,F
0
	​

=F
q
0
	​

	​

,

and let P
0
	​

 be the banked set of

P=52747567104

distinct 113-element supports T⊂F
0
	​

. Define the monic locator

P
T
	​

(Y)=
x∈T
∏
	​

(Y−x)∈F
0
	​

[Y].

Let L/F
0
	​

 be any cubic extension. For y∈L∖F
0
	​

, all P
T
	​

(y) are nonzero, because every root of every P
T
	​

 lies in F
0
	​

.

For distinct T,T
′
, a projective collision is exactly

[P
T
	​

(y)]=[P
T
′
	​

(y)]⟺P
T
	​

(y)=λP
T
′
	​

(y)

for a unique λ∈F
0
×
	​

.

For each triple (T,T
′
,λ), put

R
T,T
′
,λ
	​

(Y)=P
T
	​

(Y)−λP
T
′
	​

(Y).

This polynomial is nonzero:

if λ

=1, its leading coefficient is 1−λ

=0, so its degree is 113;

if λ=1, distinct supports give distinct monic locators, so P
T
	​

−P
T
′
	​


=0, with degree at most 112.

Consequently,

#{y∈L:R
T,T
′
,λ
	​

(y)=0}≤{
113,
112,
	​

λ

=1,
λ=1.
	​


Taking the union over unordered pairs gives

#B
proj
	​

≤(112+113(q
0
	​

−2))(
2
P
	​

)=(113q
0
	​

−114)(
2
P
	​

).

In particular, the slightly looser convenient bound is

#B
proj
	​

≤113(q
0
	​

−1)(
2
P
	​

)=7649552973225252456065323325775618181693440.

On the other hand,

∣L∖F
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

Thus

113(q
0
	​

−1)(
2
P
	​

)<q
0
3
	​

−q
0
	​

.

Therefore some y∈L∖F
0
	​

 avoids every projective collision, and hence

μ
proj
	​

(y)=1.
	​


The proportion of non-base elements that the union bound permits to be bad is below

6.64×10
−17
.
The cubic field is the full 17
48
 field

Take the concrete Cycle86 model

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
+3),β=X+2.

Direct field arithmetic gives

β
(17
16
−1)/3
=2+5X
8

=1.

Since 17
16
≡1(mod3), this proves that β is not a cube in F
0
	​

. Therefore

U
3
−β

has no root in F
0
	​

, hence is irreducible, and

L=F
0
	​

[U]/(U
3
−β)

is a degree-three extension with

∣L∣=(17
16
)
3
=17
48
.

So the “cubic extension” and the full F
17
48
	​

 are not competing ambient fields: the former is a concrete representation of the latter.

What the argument does not prove is that the particular basis element U is good.

Indeed, no theorem using only “monic, squarefree, degree 113, split over F
0
	​

” can certify U. Choose distinct a,b∈F
0
×
	​

 with a
3
,b
3

=β, and a common monic squarefree split polynomial H of degree 110, disjoint from the six relevant cubic roots. Then

f(Y)=H(Y)(Y
3
−a
3
),g(Y)=H(Y)(Y
3
−b
3
)

are distinct monic squarefree split polynomials of degree 113, but

g(U)
f(U)
	​

=
β−b
3
β−a
3
	​

∈F
0
×
	​

.

This does not exhibit a collision inside the special Cycle84 packet. It proves that U requires a packet-specific census; generic root counting cannot certify it.

Consequence for pair-product slopes

Let

Ω={P
T
	​

(β):T∈P
0
	​

}⊂F
0
×
	​

,∣Ω∣=N=52747567092,

and choose one support T
a
	​

 for every a∈Ω.

For fixed y, consider

Φ
y
	​

:Ω×P
0
	​

⟶L
×
,Φ
y
	​

(a,T)=aP
T
	​

(y).

If

aP
T
	​

(y)=a
′
P
T
′
	​

(y),

then

P
T
′
	​

(y)
P
T
	​

(y)
	​

=
a
a
′
	​

∈F
0
×
	​

.

Hence every fiber of Φ
y
	​

 has size at most μ
proj
	​

(y). Therefore

∣imΦ
y
	​

∣≥
μ
proj
	​

(y)
NP
	​

.

Thus the weaker target μ
proj
	​

(y)≤8 gives

∣imΦ
y
	​

∣≥
8
NP
	​

=347788229344751517696,

whereas

T
line
	​

=⌊
2
128
17
48
	​

⌋=338617018271848945628.

The margin is

9171211072902572068.

For the generic y proved above, μ
proj
	​

(y)=1, so all

NP=2782305834758012141568

pair products are distinct.

The twelve repeated Cycle84 values cause no additional loss: taking one representative per value of Ω handles the first block, while projective multiplicity controls every possible collision involving the second block.

Compatibility with the 464-point package

The separator theorem fits the shortened construction.

Let η have order 256, and put

K
0
	​

=⟨η
8
⟩,∣K
0
	​

∣=32.

From the explicit seven-slot support formula, every support satisfies

T∩K
0
	​

={1}.

Indeed, all non-1 support exponents are congruent to one of 1,…,7(mod8), including after multiplication by −1=η
128
. Hence any fixed 24-element subset

Z
0
	​

⊂K
0
	​

∖{1}

is universally unused. Set

D
−
=D∖Z
0
	​

,∣D
−
∣=232.

For a good y, let

c=β−y,D
y
	​

=D
−
⊔(c+D
−
).

Because y,c∈
/
F
0
	​

, the two blocks are disjoint and β∈
/
D
y
	​

. Define

S
a,T
	​

=T
a
	​

∪(c+T).

Then

∣D
y
	​

∣=464,∣S
a,T
	​

∣=226.

The banked jet identity

J
T
	​

(t)=
x∈T
∏
	​

(1−xt)≡1−t(modt
6
)

gives

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

Therefore every S
a,T
	​

 has the same six-jet.

Use the 232×464 parity-check columns

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

.

After scaling column x by β−x, the rows are evaluations of

1,β−Y,Y(β−Y),…,Y
230
(β−Y),

which form a basis of L[Y]
≤231
	​

. Thus this is one GRS parity-check matrix, giving a single

[464,232]

GRS code.

For S=S
a,T
	​

, take weights

w
x
	​

=
P
S
′
	​

(x)
1
	​

.

Partial fractions show that the first 231 syndrome coordinates depend only on the common six-jet, while the final coordinate is

x∈S
∑
	​

β−x
w
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

=
aP
T
	​

(y)
1
	​

.

Hence all supports lie on one affine syndrome line, and their slopes are the reciprocal products above.

Transversality is also uniform: if the line direction belonged to the span of a support’s columns, projection to the first 231 coordinates would give a dependence among 226 distinct Vandermonde columns. Those columns are independent. All witness coefficients are nonzero because every support is squarefree.

Thus, from the banked Cycle84/85 packet facts,

∃ an official-rate (464,232,6,226) one-line GRS counterpacket with NP distinct slopes.
	​


This is an existential theorem, not the requested explicit replay artifact.

Self-audit

Exact implication proved: the banked distinct-support packet implies the existence of y∈F
17
48
	​

∖F
0
	​

 with μ
proj
	​

(y)=1, and consequently an existential single-code, single-line 464-point GRS packet with NP distinct slopes.
Not proved: μ
proj
	​

(U)≤8, coordinates of any good y, an ordered-domain digest, or a completed public projective census.

The result is official-prize-relevant mathematically: it gives an existential official-rate MCA fail row. It is not yet a public replay artifact and is not the full proximity-prize theorem.

The first possible failure in the generic proof is the hypothesis that the P packet objects are distinct supports, hence distinct monic locators. Duplicate tuple encodings would give identical locators and permanent collisions. For the explicit target, the first unproved line is:

the serialized candidate y satisfies μ
proj
	​

(y)≤8.

The root count uses

q
0
	​

=17
16
,∣L∣=17
48
,

and compares bad elements against ∣L∖F
0
	​

∣. For the 464 construction,

q
gen
	​

=q
code
	​

=q
line
	​

=17
48
.

The challenge field may be declared

q
chal
	​

=17
48
,

but it does not enter the MCA threshold. The 2
−128
 comparison correctly uses only q
line
	​

.

Projective quotient loss is exactly charged by μ
proj
	​

. Periodic or duplicate support encodings must be eliminated before applying the theorem. The twelve same-ρ fibers are removed by choosing one representative per Ω-value. Contained incidences are excluded by Vandermonde rank. Reciprocal and any common affine normalization are injective, so they do not reduce the numerator.

This is not a PLAN. The exact remaining construction is:

V-CYCLE87-DETERMINISTIC-SEPARATOR-MATERIALIZER-464.

It should test U first, then deterministic full-field candidates, and output the first y with μ
proj
	​

(y)≤8, together with its 48 base-17 coefficients, projective-census shard hashes, 464-point domain digest, GRS fingerprint, common-line data, and threshold calculation. The theorem above guarantees that this search has a successful endpoint.

Generic separator replay script

Replay result JSON