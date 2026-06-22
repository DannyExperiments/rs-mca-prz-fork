EXACT_NEW_WALL

SOURCE_RECEIPT_MISSING_NO_CLAIM.

Confidence: high for the mathematical obstruction and ledger calculation; unknown for the official-source decision because the packet does not contain the predicate needed to decide it.

Exact prefix obstruction

The interval/overlapping-prefix mechanism can be connected to a precise source-visible invariant, rather than merely described as “additively structured.”

Let σ=2, a=k+2, and

M(X)=X
a
−cX
a−1
,w=M∣
D
	​

.

For S∈(
a
D
	​

), put

L
S
	​

(X)=
x∈S
∏
	​

(X−x)=X
a
−e
1
	​

(S)X
a−1
+⋯.

The unique degree-<a polynomial interpolating w on S is

I
S
	​

=M−L
S
	​

.

Therefore its t=1 interpolation defect is exactly

Φ
w
	​

(S)=[X
k+1
]I
S
	​

=[X
a−1
]I
S
	​

=e
1
	​

(S)−c.
(1)

Thus an equal-sum or overlapping-prefix family is literally a large zero fiber of the official-candidate interpolation-defect map.

For any retained support family Ω⊆(
a
D
	​

), define

ν
Ω
	​

(λ)=
S∈Ω
∑
	​

ψ(λΦ
w
	​

(S)),λ∈F
p
	​

,

where ψ is any nontrivial additive character. If

H
0
	​

=#{S∈Ω:Φ
w
	​

(S)=0},

character orthogonality gives

λ

=0
∑
	​

ν
Ω
	​

(λ)=pH
0
	​

−∣Ω∣,

and hence

λ

=0
∑
	​

∣ν
Ω
	​

(λ)∣≥pH
0
	​

−∣Ω∣.
	​

(2)

This is the exact high-coefficient Fourier witness required by the Cycle112 local-limit interface.

P190 specialization

Take the packet data

T=2
128
,p=130T+1,
m=190,k=1,σ=2,β=0,
M=X
3
,w=M∣
D
	​

,
S
i
	​

={i,m+i,−(m+2i)},1≤i≤190,
D=
i=1
⋃
190
	​

S
i
	​

∪{6
7
},∣D∣=571.

For every three-subset S,

I
S
	​

(X)=X
3
−
x∈S
∏
	​

(X−x)=e
1
	​

(S)X
2
−e
2
	​

(S)X+e
3
	​

(S),

so

Φ
w
	​

(S)=e
1
	​

(S).

Each selected support has e
1
	​

(S
i
	​

)=0. Moreover,

I
S
i
	​

	​

(0)=e
3
	​

(S
i
	​

)=−i(m+i)(m+2i).

The integers i(m+i)(m+2i) are strictly increasing and at most

6m
3
=41154000<p,

so the 190 colors are pairwise distinct.

Now

B=(
3
571
	​

)=30865405.

For the full support universe, (2) gives the exact lower bound

λ

=0
∑
	​

∣ν(λ)∣≥190p−B
=8404974462947180047545352803564674792097985.
(3)

Even after deleting one selected support for the endpoint convention,

λ

=0
∑
	​

∣ν
Ω
	​

(λ)∣≥189p−B
=8360737755247458047295114104598544924608704.
(4)

Consequently, any official clause implying

λ

=0
∑
	​

∣ν
Ω
	​

(λ)∣≤A(
3
571
	​

)

rejects the endpoint-paid packet whenever

A≤270877306008051993722263294604381342.

In particular, every absolute-constant interpolation-defect Fourier bound rejects it with an enormous margin.

Equivalently, if h(y) counts three-subsets having sum y, then

h(0)≥190,
y
∑
	​

h(y)
2
≥190
2
=36100,

so the Cycle112 conditional prefix-energy flatness condition also fails decisively.

The named degeneracies do not presently remove the obstruction

The exact packet calculations give:

Mechanism	Exact P190 status
Restricted sums / short prefix	190 explicit zero-sum triples; this is the obstruction.
Interpolation defect	Φ
w
	​

(S
i
	​

)=0 exactly.
Fourier mass	Lower bounds (3) and (4).
Same-slope collisions	None; the 190 values I
S
i
	​

	​

(0) are distinct.
Contained/delete-one	Empty: XG+1, with G constant, cannot vanish at two distinct points.
Intrinsic t=1	The same degree argument excludes a denominator-degree-zero reduction.
Tangency	None: every L
i
	​

 has three distinct roots, so L
i
′
	​

(x)

=0 on S
i
	​

.
Proper subfield	None because K
line
	​

=F
p
	​

.
Residue quotient/action rank	Vacuous: F
p
	​

[X]/(X)≅F
p
	​

 is one-dimensional.
Fixed affine color normalization	Injective; z↦az+b, a

=0, preserves cardinality.
Affine coefficient pencils	No three witness coefficient points are collinear.
Endpoint	One color has already been conservatively removed.
Final retained normalization	Not defined in the packet.
Broader support-periodic/additive-energy charge	Not defined in the packet.

There is also a stronger exact affine-periodicity exclusion not recorded in the Cycle112 audit: the full P190 domain D has trivial affine stabilizer.

Write

s
j
	​

=
x∈D
∑
	​

x
j
,n=571.

The construction gives s
1
	​

=6
7
=279936, and direct calculation gives

ns
2
	​

−s
1
2
	​

=44695112744810

=0(modp),
n
2
s
3
	​

−3ns
1
	​

s
2
	​

+2s
1
3
	​

=7114785503983305902460

=0(modp).

Both integers are strictly between 0 and p.

If x↦ax+b permutes D, its action fixes the mean
μ=s
1
	​

/n, so x−μ↦a(x−μ). Invariance of the second and third centered moments implies

a
2
=1,a
3
=1.

Hence a=1, and then b=0. Therefore no nonidentity affine permutation of the domain can support an affine-periodic rejection.

This does not exclude an undefined predicate that calls disjoint block matching, short restricted sums, or large Fourier mass “support-periodic.”

Exact ledger consequence

Here

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

but only q
line
	​

 is the final security denominator. The packet also satisfies the stated strong corrected reserve; for example,

16900⋅2
20
=17720934400>571(
3
571
	​

)=17624146255,

which yields the Cycle111 strengthened reserve comparison for p
2
.

The final threshold is

⌊
2
128
q
line
	​

	​

⌋=⌊
T
130T+1
	​

⌋=130.

After one endpoint,

N
retained
	​

≥189,

and

2
128
⋅189−p=59⋅2
128
−1>0.
(5)

Thus at least 59 further units of final-color cardinality must be removed or merged.

The disjoint-support matching cap is exact:

A
block
	​

=⌊
3
571
	​

⌋=190.

But it is not payable:

2
128
A
block
	​

=190T>p.

Even a charge covering only the endpoint-paid 189 colors requires a cap at least 189, and (5) shows that this is still unpayable. Therefore block matching may be an upstream exclusion predicate, but it cannot be an ordinary additive q
line
	​

-funded charge.

Neither q
code
	​

 nor q
chal
	​

 supplies another denominator. The latter is unused, and no protocol-transfer theorem is present.

Why an official rejection is not derivable

The supplied archive contains no complete, pinned object defining:

the official source adapter mapping P190 to an official intrinsic LOW datum;

official AP_corr, including its quantified functions, norm, threshold, and field;

the official endpoint operation;

the final retained color map and tag rule;

the exhaustive affine-color/support-periodic/normalization charge registry.

Therefore both of the following completions remain consistent with the packet:

\text{official `AP_corr` accepts P190},

and

\text{official `AP_corr` rejects P190 by (3), (4), or the prefix energy}.

The exact source-visible obstruction has been computed, but there is no official clause to which it can be attached. Calling the obstruction “periodic,” “high-energy,” or “short-prefix concentrated” would not be source-valid.

The earliest unavailable implication is

P190 intrinsic/model datum⟹datum produced by the official source adapter.
	​


Conditioning on that adapter, the first mathematical descent still missing is

\boxed{ \text{official `AP_corr`}+\text{no frozen named charge} \Longrightarrow \sum_{\lambda\ne0}|\nu_\Omega(\lambda)| \le A|\Omega| }

for an explicit A, or an exact official source-rejection clause.

Exact replay converter

There is a route to a full decision. The first converter is a fail-closed V-CYCLE113-FROZEN-SOURCE-CONTRACT-REPLAY checker taking:

a hash-pinned official source adapter and ordered source clauses;

an executable or formally proved AP_corr evaluator;

endpoint and final retained-color maps;

retained tags and transition-fiber rules;

an exhaustive charge registry with exact charged subsets, caps, overlap rules, and integer q
line
	​

 allocations;

the canonical P190 data.

It must return:

SOURCE_REJECTED at the first false official source/APcorr clause, with its exact evaluated witness;

COLOR_COMPRESSED_OR_CHARGED only if the final quotient has at most 130 classes, or an exact non-double-spent ledger closes;

SOURCE_VALID_LOW_T1_COUNTERPACKET if every source/APcorr test passes and at least 131 exact final uncompressed colors survive;

SOURCE_RECEIPT_MISSING_NO_CLAIM whenever any contract component is absent, unpinned, ambiguous, or nonexhaustive.

Soundness follows because all P190 field operations, witness evaluations, color equalities, quotient fibers, charged-set unions, and integer allocations are finite exact computations. Completeness relative to the supplied contract follows only when its source clauses and charge registry are explicitly declared exhaustive.

Self-audit

Proved: the exact restricted-sum/interpolation-defect identity; the quantitative Fourier obstruction; the 190/189 color calculation; the 59-color deficit; unpayability of the block cap; and triviality of the P190 affine domain stabilizer.

Not proved: official source acceptance, official AP_corr acceptance or rejection, or the official final retained color count.

The result is prize-route-relevant and theorem-level as a conditional obstruction, but P190 remains a finite/model source candidate rather than an official counterpacket.

The first failure line is the missing official source-adapter receipt. After conditioning on it, the next failure is official AP_corr descent to defect-spectrum control.

q_{\rm gen} is used only in corrected reserve; q_{\rm line}=p is the sole final denominator; q_{\rm code} is metadata; q_{\rm chal} is unused; the exact target is 2
128
N
free
	​

≤q
line
	​

.

Quotient/action rank, contained incidences, tangency, same-slope collisions, fixed affine normalization, proper subfields, and affine domain stabilizers do not reduce the displayed numerator. One endpoint removes one. Broader support-periodic and final-normalization effects remain undecidable because their official definitions are missing.

The first theorem converting this result into a source rejection is the explicit official implication from AP_corr to the Fourier bound above. The first checker converting it into either a rejection or a counterpacket is the frozen-contract replay specified above.
