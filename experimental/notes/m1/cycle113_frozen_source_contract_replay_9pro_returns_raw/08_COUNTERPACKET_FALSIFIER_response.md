BANKABLE_LEMMA

Terminal: SOURCE_RECEIPT_MISSING_NO_CLAIM.

The P190 arithmetic is sound, but its 190 supports are pairwise disjoint, placing it directly inside the already identified disjoint-threshold-block mechanism. That label is not payable here—its cap is at least 190 while q
line
	​

/2
128
<131—but the disjointness remains its clearest structural weakness.

A stronger overlapping repair exists.

The overlapping C
284
	​

 packet

Set

T=2
128
,p=130T+1,

so

⌊
T
p
	​

⌋=130.

The P190 Proth certificate proves that p is prime and that 6 is primitive.

Use

q
gen
	​

=q
code
	​

=q
line
	​

=p,k=1,σ=2,β=0,E=X,B=1.

Let m=284. For 1≤i≤m, put

x
i
	​

=i
2
,y
i
	​

=−(i
2
+(i+1)
2
)(modp),

and

S
i
	​

={x
i
	​

,x
i+1
	​

,y
i
	​

}.

Set

h=6
7
=279936,D=
i=1
⋃
284
	​

S
i
	​

∪{h},w(x)=x
3
.

The positive square points, the negative y
i
	​

, and h are disjoint, giving

n=∣D∣=285+284+1=570.

Let

L
i
	​

(X)=
x∈S
i
	​

∏
	​

(X−x),Q
i
	​

(X)=X
3
−L
i
	​

(X).

Writing u
i
	​

=i(i+1), the three roots in S
i
	​

 sum to zero and

Q
i
	​

(X)=(3u
i
2
	​

+4u
i
	​

+1)X−u
i
2
	​

(2u
i
	​

+1).

Thus

degQ
i
	​

=1=k,Q
i
	​

(x)=w(x)(x∈S
i
	​

).

Moreover X
3
−Q
i
	​

=L
i
	​

 has exactly the three distinct roots S
i
	​

, so

agr
D
	​

(Q
i
	​

,w)=3=k+σ.

At β=0, the colors are

z
i
	​

=Q
i
	​

(0)=−u
i
2
	​

(2u
i
	​

+1).

Since u
i
	​

 and u
i
2
	​

(2u
i
	​

+1) are strictly increasing positive integers and

u
284
2
	​

(2u
284
	​

+1)=1060528340451600<p,

the 284 colors are pairwise distinct in F
p
	​

.

Exact security violation

Before endpoint processing:

N
displayed
	​

=284.

After deletion of any one displayed color:

N
retained
	​

≥283.

Hence

283−130=153,

and exactly

2
128
⋅283−p=153⋅2
128
−1>0.

Therefore an official source operation must reject the datum or remove/merge at least 153 additional endpoint-paid colors to avoid a counterpacket.

This improves the P190 target

189⟶283,59⟶153.
The disjoint-block objection no longer resolves the packet

The support intersections are exactly

S
i
	​

∩S
j
	​

={
{(i+1)
2
},
∅,
	​

j=i+1,
j≥i+2.
	​


Thus the support-intersection graph is the path P
284
	​

, rather than a disjoint collection.

Its maximum pairwise-disjoint subfamily has size

ν=⌈
2
284
	​

⌉=142,

realized by the odd-indexed supports.

After deletion of any one color, at least 141 of these pairwise-disjoint colors remain. But

2
128
⋅141−p=11⋅2
128
−1>0.

Consequently, even the surviving disjoint subpacket is above the entire q
line
	​

 capacity. An official disjoint-block predicate could reject or compress it, but an ordinary additive charge with cap at least 141 cannot be allocated from q
line
	​

=p.

Corrected-reserve check

The stronger Cycle111 calibration also holds. Since

(
3
570
	​

)=30703240

and

570(
3
570
	​

)=17500846800<17720934400=16900⋅2
20
,

we obtain

p
2
	​

>(130T)
2
=16900T
2
>2
236
⋅570(
3
570
	​

).
	​


This reserve is not used as a final denominator; it is only the model calibration. The final denominator remains q
line
	​

=p.

Obvious-charge audit
Intrinsic t=1

Here E(D)

=0 and BmodE=1. A degree-zero reduction would require a constant G such that

XG+1

vanishes at two distinct domain points. A nonzero polynomial of degree at most one cannot do so. Hence the denominator degree is intrinsically t=1.

Contained/delete-one

For j≤σ−1=1, the standard contained/delete-j branch would again require XG+1 to vanish at at least

k+σ−j≥2

points. It is therefore empty.

Quotient and hidden residue-action rank
F
p
	​

[X]/(X)≅F
p
	​


has no nonzero proper unital F
p
	​

-algebra quotient, and its nonzero residue action has rank 1=t.

Same-slope collisions

The z
i
	​

 are pairwise distinct, so no same-slope or same-color deduction occurs.

Tangency

Every L
i
	​

 is squarefree. For x∈S
i
	​

,

L
i
′
	​

(x)=
y∈S
i
	​

∖{x}
∏
	​

(x−y)

=0.
Field and multiplicative-coset confinement

The field is prime, so there is no proper subfield or nontrivial proper additive subgroup.

The domain contains 1 and h=6
7
. Since 6 is primitive and

gcd(7,p−1)=1,

h is primitive. Thus D is not contained in a coset of a proper multiplicative subgroup.

Also p≡2(mod3), so cubing is an automorphism of F
p
	​

. Hence w(D)=D
3
 contains 1 and the primitive element h
3
, and is likewise not properly multiplicatively confined.

Support quotient and periodic orbit compression

Because cubing is injective on F
p
	​

, w∣
D
	​

 is injective. Any quotient of D through whose fibers w is constant therefore has only singleton fibers. Thus there is no nontrivial w-preserving support quotient of the affine-involution type.

This does not decide a broader undefined official “support-periodic” predicate.

Affine coefficient pencils

The coefficient point of Q
i
	​

 is

P(u
i
	​

)=(3u
i
2
	​

+4u
i
	​

+1,−2u
i
3
	​

−u
i
2
	​

).

For distinct u,v,r,

det
	​

3u
2
+4u+1
3v
2
+4v+1
3r
2
+4r+1
	​

−2u
3
−u
2
−2v
3
−v
2
−2r
3
−r
2
	​

1
1
1
	​

	​


equals

2(u−v)(u−r)(v−r)(3uv+3ur+3vr+4u+4v+4r+2).

Here 1≤u
i
	​

≤284⋅285=80940, and the final factor is positive and at most

9(80940)
2
+12(80940)+2=58962523682<p.

Every factor is therefore nonzero modulo p. No three witness polynomials lie in one affine coefficient pencil. A union of J affine pencils contains at most 2J displayed colors.

Affine stabilizer

The decorated support hypergraph has edge-intersection graph P
284
	​

. Its only possible edge permutations are identity and reversal.

Identity fixes the consecutive shared vertices 2
2
 and 3
2
, forcing an affine map to be the identity.

Reversal would require one affine slope to satisfy simultaneously

3
2
−2
2
283
2
−284
2
	​

=
5
−567
	​


and

4
2
−3
2
282
2
−283
2
	​

=
7
−565
	​

,

but

567⋅7=3969

=2825=565⋅5.

Thus the decorated packet has trivial affine stabilizer.

Affine and retained normalization

A fixed affine color map z↦az+b, a

=0, preserves all 284 colors. A support-dependent normalization with retained chart/support tags is likewise injective.

Any official normalization claiming at most 130 final colors must supply the explicit quotient map and exhibit at least 153 additional removals or identifications after the one-color endpoint allowance.

Fourier obstruction

Every displayed support has interpolation defect zero. The exact inverse Fourier bound from Cycle112 therefore gives, for the full three-subset universe,

Δ≥p⋅284−(
3
570
	​

)=284p−30703240.

Thus C
284
	​

 is emphatically not Fourier-flat. Any theorem

official AP
corr
	​

+NoCharge⟹bounded defect-Fourier mass

would reject this packet at that implication. The packet contains no such official theorem or evaluator.

Missing official receipts

The first unavailable implication is

C
284
	​

 satisfies the reconstructed intrinsic scaffold⟹official source adapter accepts and official AP
corr
	​

=1.

The archive supplies none of the following:

The literal official source-adapter predicate applied to C
284
	​

.

A frozen official AP_corr evaluator or proof receipt.

The official endpoint convention.

The final normalized K
line
	​

-color map and retained-tag rule.

The exhaustive charge registry, exact charged color sets, caps, and non-double-spent q
line
	​

 allocations.

Accordingly, neither official acceptance nor official rejection is derivable. The exact current terminal is SOURCE_RECEIPT_MISSING_NO_CLAIM.

Decisive replay checker

The first checker capable of converting this result into an official terminal is:

V-CYCLE113-CHAIN284-FROZEN-SOURCE-REPLAY

Its inputs must be:

hash-pinned official source contract and ordered clauses
official AP_corr evaluator or checked proof object
the canonical C284 constants, domain, word, supports and witnesses
endpoint and final-normalization evaluator
complete official charge registry
exact q_line allocation/composition rule

It must:

Recompute all arithmetic and the 284 displayed colors.

Evaluate source and AP_corr clauses in their official order.

Apply endpoint processing and the official final color map.

Canonicalize and deduplicate the exact final colors.

Evaluate every registered charge, disjointize ownership, and verify every cap and allocation.

Check the integer inequality 2
128
N
final
	​

≤q
line
	​

.

Its terminal decisions are:

SOURCE_REJECTED
  first false official clause and its exact witness

COLOR_COMPRESSED_OR_CHARGED
  exact final map or charged subsets, final count <= 130,
  caps and complete q_line allocation

SOURCE_VALID_LOW_T1_COUNTERPACKET
  all official predicates true and final count >= 131

SOURCE_RECEIPT_MISSING_NO_CLAIM
  any missing, ambiguous, unpinned or unevaluable receipt

Relative to a total frozen evaluator and exhaustive registry, this checker has no false positives because every positive terminal requires exact recomputation and checked receipts. It has no false negatives because all 284 displayed witnesses, their final images, and every registered charge are exhaustively evaluated; unprovided semantics fail closed rather than being guessed.

Self-audit

Proved: the explicit same-field intrinsic t=1 construction, exact reserve, 284 distinct model colors, 283 after any one deletion, a 141-color disjoint retained subpacket after any deletion, absence of the listed algebraic degeneracies, trivial affine stabilizer, maximum affine-pencil occupancy two, and the strict q
line
	​

 violations.

Not proved: official source-adapter acceptance, official AP_corr, absence of a broader official support-periodic or affine-color exclusion, or injectivity of an unspecified official final normalization.

The result is prize-route relevant and analytically exact, but remains a model/source-replay counterpacket certificate rather than an official counterpacket.

The field ledger is:

q
gen
	​

=q
code
	​

=q
line
	​

=p,

with q
gen
	​

 used only in the calibrated reserve, q
line
	​

 the sole final denominator, q
code
	​

 supplying no additional denominator, and q
chal
	​

 unused.

There is a direct route to a full decision, but not from the supplied files alone: freeze the official contract and run the replay above. Acceptance with at least 131 final colors yields COUNTERPACKET; otherwise the replay must expose the first rejecting clause or an explicit 153-color compression.
