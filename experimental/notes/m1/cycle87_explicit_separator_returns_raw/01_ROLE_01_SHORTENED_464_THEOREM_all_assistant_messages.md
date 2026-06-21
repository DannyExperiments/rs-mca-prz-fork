I will inspect the Cycle87 state, audits, and raw returns, then formalize the 464 two-copy package and identify the first valid implication or failure.

--- ASSISTANT MESSAGE BREAK ---

The key checks are now the common six-jet identity under translation/union and the claimed support incidences of the 232×464 parity-check line.

--- ASSISTANT MESSAGE BREAK ---

BANKABLE_LEMMA

Confidence: high. The 464 package is algebraically valid, provided it is understood as a newly constructed GRS code on two reduced blocks—not as automatic puncturing of the 560-point code. The remaining active wall is solely the explicit separator certificate.

Exact shortened-domain theorem

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
+3),η=6X
9
,D
0
	​

=⟨η⟩,

so ∣D
0
	​

∣=256, and let

β=X+2.

Use the banked packet P
0
	​

⊆(
113
D
0
	​

	​

), with

∣P
0
	​

∣=P=52747567104,

such that, for every T∈P
0
	​

,

J
T
	​

(t):=
x∈T
∏
	​

(1−xt)≡1−t(modt
6
),

and

T∩(⟨η
8
⟩∖{1})=∅.

Write

P
T
	​

(Y)=
x∈T
∏
	​

(Y−x),ρ(T)=P
T
	​

(β),

and let

Ω={ρ(T):T∈P
0
	​

},∣Ω∣=N=52747567092.

Choose one representative T
ω
	​

∈P
0
	​

 for every ω∈Ω.

1. The two shortened blocks

Choose the explicit universally unused set

Z={η
8b
:1≤b≤24}⊆⟨η
8
⟩∖{1},

and put

D
−
	​

:=D
0
	​

∖Z.

Then

∣D
−
	​

∣=232

and every T∈P
0
	​

 remains a subset of D
−
	​

.

Let

L=F
17
48
	​


with its unique embedded subfield F
0
	​

=F
17
16
	​

. For any

y∈L∖F
0
	​

,c=β−y,

define

D
1
	​

=D
−
	​

,D
2
	​

=c+D
−
	​

,D=D
1
	​

⊔D
2
	​

.

The blocks are disjoint: an equality d
1
	​

=c+d
2
	​

, with d
i
	​

∈F
0
	​

, would imply c∈F
0
	​

, contrary to y∈
/
F
0
	​

. Also β∈
/
D
2
	​

, since β=c+d would imply y=d∈F
0
	​

.

Consequently,

∣D∣=232+232=464.

For T
1
	​

,T
2
	​

∈P
0
	​

, define

Ψ(T
1
	​

,T
2
	​

)=T
1
	​

∪(c+T
2
	​

).

The blocks are disjoint, so

∣Ψ(T
1
	​

,T
2
	​

)∣=113+113=226.

Thus

j=226,n−j=464−226=238=k+σ=232+6.

The map (T
1
	​

,T
2
	​

)↦Ψ(T
1
	​

,T
2
	​

) is injective.

2. Deleting the unused coordinates preserves the six-jet

The deletion changes only the ambient domain. It does not change any packet support or its locator, so the original congruence

J
T
	​

(t)≡1−t(modt
6
)

is literally unchanged.

For a translated support,

J
c+T
	​

(t)
	​

=
x∈T
∏
	​

(1−(c+x)t)
=(1−ct)
113
J
T
	​

(
1−ct
t
	​

).
	​


Substituting the banked jet gives

J
c+T
	​

(t)≡(1−ct)
112
(1−(c+1)t)(modt
6
).

Therefore every combined support U=Ψ(T
1
	​

,T
2
	​

) has the same six-jet

J
U
	​

(t)≡J
∗
	​

(t)(modt
6
),

where

J
∗
	​

(t)=(1−t)(1−ct)
112
(1−(c+1)t).

Write

J
∗
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
).

These six coefficients are independent of T
1
	​

,T
2
	​

, and h
0
	​

=1.

Hence the shortening loses no local condition.

3. One GRS code and one affine syndrome line

For each x∈D, define the column

H
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

∈L
232
,

and let H be the 232×464 matrix formed from these columns. Define

C=kerH⊆L
464
.

Multiplying the x-column by β−x changes the rows to evaluations of

1,(β−Y),Y(β−Y),…,Y
230
(β−Y).

These 232 polynomials form a basis of L[Y]
≤231
	​

: if

a+(β−Y)Q(Y)=0,degQ≤230,

then evaluation at Y=β gives a=0, and then Q=0.

Thus H is row- and nonzero-column-equivalent to a 232-row Vandermonde parity-check matrix. Hence C is one GRS code with

[n,k]=[464,232].

It is not a direct sum of two codes.

Now fix U=Ψ(T
1
	​

,T
2
	​

), let

P
U
	​

(Y)=
x∈U
∏
	​

(Y−x),a
U,x
	​

=
P
U
′
	​

(x)
1
	​

.

The partial-fraction identity

P
U
	​

(Y)
1
	​

=
x∈U
∑
	​

Y−x
a
U,x
	​

	​


and the expansion

P
U
	​

(Y)
1
	​

=Y
−226
J
U
	​

(Y
−1
)
−1

give

x∈U
∑
	​

a
U,x
	​

x
m
=
⎩
⎨
⎧
	​

0,
h
m−225
	​

,
	​

0≤m≤224,
225≤m≤230.
	​


Therefore, with

s
∗
	​

=(
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

)∈L
231
,

one has

x∈U
∑
	​

a
U,x
	​

(1,x,…,x
230
)
T
=s
∗
	​

.

Evaluation of the same partial-fraction identity at β gives

x∈U
∑
	​

β−x
a
U,x
	​

	​

=
P
U
	​

(β)
1
	​

.

Hence

He
U
	​

=(s
∗
	​

,
P
U
	​

(β)
1
	​

),

where e
U
	​

 is supported on U and has coordinates a
U,x
	​

.

Thus all combined supports meet the single affine syndrome line

ℓ={(s
∗
	​

,z):z∈L}.

Since all a
U,x
	​


=0, the error support is exactly U, not a proper subset. Any affine lift of ℓ to the received-word space therefore supplies an exact agreement set of size

464−226=238=k+σ.
4. Transversality and noncontainment

The direction of ℓ is the last coordinate vector e
232
	​

.

Suppose e
232
	​

 belonged to the span of the columns indexed by a combined support U. Projecting onto the first 231 coordinates would give a dependence among the 226 columns

(1,x,…,x
230
)
T
,x∈U.

The resulting 231×226 Vandermonde matrix has full column rank, since the 226 points are distinct. All coefficients would therefore vanish, contradicting e
232
	​


=0.

Hence every incidence is transverse, and no support span contains the affine line.

5. Exact slope formula and projective collision bound

For U=Ψ(T
1
	​

,T
2
	​

),

P
U
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

(β)=ρ(T
1
	​

)P
T
2
	​

	​

(y).

Thus a direct line coordinate is

z(T
1
	​

,T
2
	​

)=
ρ(T
1
	​

)P
T
2
	​

	​

(y)
1
	​

.

A sign, scaling, or translation of z is one common affine reparametrization and preserves cardinality.

Use the support family

{Ψ(T
ω
	​

,T):ω∈Ω, T∈P
0
	​

},

which contains exactly NP distinct supports.

Suppose two such supports have the same slope. Then

ωP
T
	​

(y)=ω
′
P
T
′
	​

(y),

so

[P
T
	​

(y)]=[P
T
′
	​

(y)]in L
×
/F
0
×
	​

.

For a fixed final product and a fixed second support T, the first value
ω is uniquely determined. Therefore every final-slope fiber has size at most

μ
proj
	​

(y).

Consequently,

#{distinct slopes}≥⌈
μ
proj
	​

(y)
NP
	​

⌉.

In particular, if

μ
proj
	​

(y)≤8,

then

M
C
	​

(6)≥
8
NP
	​

=347788229344751517696.

The official line-field target is

T
line
	​

=⌊
2
128
17
48
	​

⌋=338617018271848945628,

so the exact excess is

9171211072902572068.

There is no hidden factor of two: the first-block double fibers have already been removed by choosing one representative T
ω
	​

 per occupied ρ-value.

6. Generic projective separators exist, strongly

The absence of a concrete separator is not an existence problem.

Put

Q=∣F
0
	​

∣=17
16
.

For distinct T,T
′
∈P
0
	​

 and a∈F
0
×
	​

, the polynomial

P
T
	​

(Y)−aP
T
′
	​

(Y)

is nonzero and has degree at most 113. Therefore it has at most 113 roots in L.

The set of elements of L that either lie in F
0
	​

 or produce some projective collision has cardinality at most

Q+113(Q−1)(
2
P
	​

).

Exactly,

Q+113(Q−1)(
2
P
	​

)=7649552973225252456065371986967493848561921,

whereas

∣L∣=17
48
=115225400457255426923013053222916919834651165519677685328641.

Thus some y∈L∖F
0
	​

 satisfies

μ
proj
	​

(y)=1.

For such a y, the selected NP support pairs have NP distinct slopes.

This proves separator existence but does not provide the concrete coefficient-level separator demanded by the active checker.

The precise status of “shortening”

The valid implication is not:

Puncture the previous 560-point GRS code and automatically inherit a [464,232] code and the same syndrome line.

That implication is false in general; puncturing does not give the desired dimension and syndrome data automatically.

The valid construction is:

omit the 48 fixed padding coordinates and their fixed locator factor;

delete Z from the first 256-point block and c+Z from the translated block;

retain the unchanged variable supports;

re-prove the common six-jet;

construct the new 232×464 parity-check matrix H above.

Under this corrected meaning, the 464 package survives. The 560 package remains a separate padded fallback, but it is unnecessary.

Self-audit

Exact implication proved.
From the banked packet axioms and any y∈L∖F
0
	​

, I proved the existence of one [464,232] GRS code, one affine syndrome line, exact 226-point transverse supports, and the slope formula

z=(ρ(T
1
	​

)P
T
2
	​

	​

(y))
−1
.

I proved

μ
proj
	​

(y)≤8⟹M
C
	​

(6)≥NP/8>T
line
	​

.

I also proved existentially that some y has μ
proj
	​

(y)=1.

I did not exhibit such a y, certify a concrete candidate, or produce a public replay artifact.

Prize relevance.
This is an official-profile algebraic theorem: rate 1/2, reserve 6, and line field 17
48
. Under the stated certification standard it is not yet an official counterpacket. It is stronger than a finite-model certificate but weaker than the required explicit/replayable result. It proves neither a scalar-list obstruction nor the full prize theorem.

First possible failure line.
Relative to the banked Cycle84–85 packet facts, the first unresolved line is exactly

μ
proj
	​

(y)≤8

for one serialized concrete y.
The first false line in an incorrect shortening argument would be the assertion that puncturing the old code automatically preserves the desired dimension and syndrome line.

Field and target ledger.
The reduced first block contains 1 and η, hence generates F
0
	​

. The combined domain contains 1 and c+1, hence generates c, and therefore y=β−c. Since [L:F
0
	​

]=3 and y∈
/
F
0
	​

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

=17
48
.

The challenge field is unused; it may be recorded as 17
48
 if required by the schema, but it supplies no denominator credit. The 2
−128
 target is computed only from q
line
	​

.

Possible numerator losses.
Projective quotienting is paid for explicitly by μ
proj
	​

(y). First-block same-ρ collisions are removed by the representative section. Support-pair duplication is impossible because the blocks are disjoint. Contained incidences are excluded by Vandermonde rank. All error coordinates are nonzero. A common affine color normalization is bijective and causes no loss.

Exact next construction.
The next wall is precisely

V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
	​

.

It must emit a concrete cubic-extension element y, prove y∈
/
F
0
	​

, and certify

μ
proj
	​

(y)≤8.

The same replay should instantiate

c=β−y,D
−
	​

,D=D
−
	​

⊔(c+D
−
	​

),H,s
∗
	​

,

and record the lower term NP/8. A passing census converts the result directly into the required explicit two-copy counterpacket; no further algebraic lemma is missing.