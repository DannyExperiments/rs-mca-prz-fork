BANKABLE_LEMMA

1. Executive verdict and confidence

Verdict. The field and numerator ledger can be closed conditionally by an exact slope-level theorem stated below. The packet does not contain the branch caps, aggregate chart bounds, univariate slope-eliminants, or target-range lower bound on q
line
	​

 needed to instantiate that theorem. Therefore this is not a prize proof.

The crucial refinement is that a balanced or high chart must produce a bounded slope projection—equivalently, a nonzero univariate eliminant in the normalized slope. A low-degree multivariate separator on a transverse affine plane is insufficient.

Confidence: high for the conditional ledger lemma and the field-transfer route cuts; high that the attached packet does not close N
off
	​

.

This result is official-prize-relevant as a source-level reduction. It is neither a finite/model certificate nor a completed official proof.

2. Exact theorem statement
L-CYCLE109-QLEDGER-EXACT-SLOPE-ELIMINANT-CLOSURE

Fix one official RS-MCA line instance I. Write

K
line
	​

=K
line
	​

(I),q
line
	​

:=∣K
line
	​

∣,

and let

B
off
	​

(I)⊆K
line
	​

,N
off
	​

(I):=∣B
off
	​

(I)∣

be the set and number of distinct official bad slopes. Assume the official experiment samples

θ∼Unif(K
line
	​

).

The following are the exact source-cover hypotheses needed.

H1. Source applicability

The instance satisfies the official corrected-reserve condition, expressed using q
gen
	​

, and the repaired source-visible predicate AP
corr
	​

.

Neither q
gen
	​

 nor q
code
	​

 is assumed equal to q
line
	​

.

H2. Slope-level partition

There is a deterministic priority assignment of every θ∈B
off
	​

 to exactly one of:

	​

end, quot, per, cont, del1, tan,
field, color, hidden, internal, norm,
low, bal, high.
	​

The assignment is at the level of distinct elements of K
line
	​

, not supports, source witnesses, polynomials, or incidence pairs.

Same-slope witness collisions are collapsed before this partition and contribute no additional branch:

c
same
	​

=0.
H3. Exact paid-branch caps

For the paid branches there are explicit, effective integer caps

c
end
	​

,c
quot
	​

,c
per
	​

,c
cont
	​

,c
del1
	​

,c
tan
	​

,c
field
	​

,c
color
	​

,
c
hidden
	​

,c
internal
	​

,c
norm
	​

	​

such that each corresponding distinct-slope set has cardinality at most its cap. The endpoint repair gives

c
end
	​

≤1.

“Explicit” means a concrete integer-valued formula, not n
O(1)
.

The normalization cap must include every slope excluded because of a vanishing denominator, degenerate Möbius determinant, zero affine coefficient, normalization pole, or loss of same-field injectivity.

H4. Aggregate LOW image cap

There is an explicit integer c
low
	​

 such that the union over all

1≤t<σ

of uncharged LOW residual slope images has at most c
low
	​

 distinct elements of K
line
	​

.

A theorem giving L
t
	​

 slopes separately for each t yields only

c
low
	​

≤
1≤t<σ
∑
	​

L
t
	​

.

It does not by itself give c
low
	​

≤max
t
	​

L
t
	​

.

H5. Aggregate tagged chart assignment

There are tag sets

T
bal
	​

,T
high
	​

and assignments of every balanced or high bad slope to one tag. The tag contains all data needed to determine the normalization, including any support selector, anchor, denominator degree, affine-plane gauge, or source witness selector.

The bounds on the tag sets are aggregate across all intrinsic degrees:

∣T
bal
	​

∣≤J
bal
	​

,∣T
high
	​

∣≤J
high
	​

.

A bound of n
C
 charts separately for each h is not an aggregate high-branch bound unless the number of possible h's is also bounded and paid in the ledger.

H6. Same-field injective normalization

For every tag τ there is a map

ν
τ
	​

:Θ
τ
	​

⟶K
line
	​

,

where Θ
τ
	​

⊆K
line
	​

 is the set of original slopes assigned to that chart, such that ν
τ
	​

 is injective.

For a support-dependent affine normalization,

ν
τ
	​

(θ)=a
τ
	​

θ+b
τ
	​

,a
τ
	​

∈K
line
×
	​

,b
τ
	​

∈K
line
	​

,

the retained object is

θ⟼(τ,ν
τ
	​

(θ)).

The tag may not be discarded.

H7. Univariate slope-eliminant or paid charge

For every uncharged chart τ, source AP
corr
	​

 implies the existence of a polynomial

R
τ
	​

(T)∈K
line
	​

[T]∖{0}

such that

ν
τ
	​

(Θ
τ
	​

)⊆{x∈K
line
	​

:R
τ
	​

(x)=0}.

Define its exact line-field root cap

ρ
τ
	​

:=∣{x∈K
line
	​

:R
τ
	​

(x)=0}∣.

Then

ρ
τ
	​

≤min(q
line
	​

,degR
τ
	​

).

If the restricted eliminant is identically zero, if only a multivariate equation is available, or if slope projection is not finite, that chart is not uncharged: its slopes must be assigned to one of the explicitly capped paid branches.

Exact ledger

Set

M
paid
	​

=
	​

c
end
	​

+c
quot
	​

+c
per
	​

+c
cont
	​

+c
del1
	​

+c
tan
	​

+c
field
	​

+c
color
	​

+c
hidden
	​

+c
internal
	​

+c
norm
	​

,
	​

and

M
charts
	​

=
τ∈T
bal
	​

∑
	​

ρ
τ
	​

+
τ∈T
high
	​

∑
	​

ρ
τ
	​

.

The total certified numerator cap is

M
led
	​

=M
paid
	​

+c
low
	​

+M
charts
	​

.
(1)

Then

N
off
	​

≤min(q
line
	​

,M
led
	​

).
(2)

Consequently, the exact arithmetic condition closing the line experiment is

M
led
	​

≤⌊
2
128
q
line
	​

	​

⌋,
(3)

equivalently,

2
128
M
led
	​

≤q
line
	​

.
(4)

Under (3),

q
line
	​

N
off
	​

	​

≤2
−128
.
(5)

Equation (3), not merely “M
led
	​

 is polynomial,” is the required numerical theorem.

Explicit polynomial specialization

Suppose one proves concrete bounds

c
j
	​

≤A
j
	​

n
a
j
	​

,c
low
	​

≤A
L
	​

n
a
L
	​

,

and

∣T
r
	​

∣≤A
r
	​

n
b
r
	​

,ρ
τ
	​

≤D
r
	​

n
d
r
	​

(r∈{bal,high}).

Then

M
led
	​

≤
j
∑
	​

A
j
	​

n
a
j
	​

+A
L
	​

n
a
L
	​

+A
bal
	​

D
bal
	​

n
b
bal
	​

+d
bal
	​

+A
high
	​

D
high
	​

n
b
high
	​

+d
high
	​

.
(6)

Thus the exact parameter-range hypothesis is

q
line
	​

≥2
128
(
j
∑
	​

A
j
	​

n
a
j
	​

+A
L
	​

n
a
L
	​

+A
bal
	​

D
bal
	​

n
b
bal
	​

+d
bal
	​

+A
high
	​

D
high
	​

n
b
high
	​

+d
high
	​

).
(7)

If the LOW theorem is only per degree,

∣L
t
	​

∣≤A
L
	​

n
ℓ
,

then, in every nontrivial instance k+σ≤n,

c
low
	​

≤(σ−1)A
L
	​

n
ℓ
≤A
L
	​

n
ℓ+1
.
(8)

If q
line
	​

=2
λ
, condition (4) becomes

λ≥128+⌈log
2
	​

M
led
	​

⌉(M
led
	​

>0).
(9)

The packet provides no concrete values for the A's, exponents, separator degrees, or targeted q
line
	​

, so (7) cannot presently be checked.

3. Proof and route cuts
Proof of the ledger lemma

For every paid branch j, H3 gives

∣B
j
	​

∣≤c
j
	​

.

H4 gives

∣B
low
	​

∣≤c
low
	​

.

Now fix an uncharged balanced or high chart τ. By injectivity,

∣Θ
τ
	​

∣=∣ν
τ
	​

(Θ
τ
	​

)∣.

By the slope-eliminant property,

ν
τ
	​

(Θ
τ
	​

)⊆Z
K
line
	​

	​

(R
τ
	​

),

so

∣Θ
τ
	​

∣≤ρ
τ
	​

.

Summing over the chart assignments and the paid branches gives (2). Overlaps between chart covers or paid caps can only make this sum larger than the actual union, so they cannot invalidate the upper bound.

Since the official line slope is uniform in K
line
	​

,

Pr[θ is bad]=
∣K
line
	​

∣
∣B
off
	​

∣
	​

=
q
line
	​

N
off
	​

	​

.

Applying (2) and (3) proves (5).

No other field cardinality enters this probability calculation.

Route cut 1: a transverse affine-plane separator is not enough

Consider one chart with slope coordinate θ∈K
line
	​

 and auxiliary coordinate u∈K
line
	​

. Let the bad incidence locus be

V={(θ,u):u=0}.

It is contained in the zero set of the nonzero degree-one polynomial

F(θ,u)=u.

Nevertheless,

π
θ
	​

(V)=K
line
	​

,

so the chart has all q
line
	​

 possible slopes.

Therefore:

nonzero low-degree equation on an affine plane\centernot⇒small distinct-slope image.

For the HIGH route, the required statement is

I(V)∩K
line
	​

[θ]

=(0),

with an explicit degree bound on a nonzero element of this elimination ideal, or an equivalent explicit finite slope-projection theorem.

This is the first q-ledger defect in a theorem that merely says “rank escape in the affine plane.”

Route cut 2: discarding support-dependent tags undercounts slopes

Choose c

=0 in K
line
	​

. Consider two charts:

ν
1
	​

(θ)=θ,ν
2
	​

(θ)=θ−c.

Suppose both normalized bad images equal {0}. Their original slope sets are

{0}and{c}.

Dropping the tag and taking the normalized union gives one value; the original numerator contains two distinct slopes.

Thus the globally valid map is

(τ,θ)↦(τ,ν
τ
	​

(θ)),

not θ↦ν
τ
	​

(θ) after forgetting τ.

Route cut 3: q
code
	​

 does not pay a q
line
	​

 numerator

Let

K
code
	​

=F
p
	​

,K
line
	​

=F
p
2
	​

,

with p odd, and choose a nonsquare a∈F
p
	​

. Then

T
2
−a

has no roots in K
code
	​

 and two roots in K
line
	​

.

Hence even a polynomially defined slope condition can acquire new slopes under scalar extension. A base-field numerator is not automatically the line-field numerator.

The required transfer theorem would have to prove, for the actual official bad sets, an inclusion or injection such as

B
line
	​

↪S

where S is already counted with an explicit cap. Merely having an embedding K
code
	​

↪K
line
	​

 is insufficient.

This is a route cut, not an official RS-MCA counterpacket.

Route cut 4: q
chal
	​

 is unusable without protocol transfer

Let χ be uniform in a challenge space of size q
chal
	​

, and suppose the protocol maps challenges to line slopes through π.

The exact transfer statement needed is:

E
protocol
	​

⊆π
−1
(B
off
	​

)
(10)

and

θ∈K
line
	​

max
	​

Pr[π(χ)=θ]≤
q
line
	​

1
	​

.
(11)

Then

Pr[E
protocol
	​

]≤
θ∈B
off
	​

∑
	​

Pr[π(χ)=θ]≤
q
line
	​

N
off
	​

	​

.

Without (10)–(11), q
chal
	​

 gives no denominator. For example, π can map every challenge to one bad slope, giving protocol failure probability 1 regardless of how large q
chal
	​

 is.

No q
chal
	​

 transfer is used in the proved ledger lemma.

4. Verification requirements

A source-valid certificate or proof must provide all of the following.

Sampling statement. Confirm that the relevant experiment samples uniformly from K
line
	​

, with denominator exactly q
line
	​

. If the sample space is projective or challenge-derived, the denominator theorem must be changed.

Slope-level branch assignment. Every bad slope must be assigned once. A count of supports, polynomials, witnesses, or source incidences is not a numerator cap unless its slope image is bounded.

Concrete cap vector. Supply numerical formulas for every c
j
	​

 and c
low
	​

. The current packet only supplies c
end
	​

≤1 in immediately usable form.

Aggregate degree bookkeeping. Include t, h, source selectors, anchors, gauges, and normalization choices in the tag count. A polynomial number of charts per degree is not yet a polynomial total unless the degree index range is paid.

Same-field normalization. Verify all normalization coefficients lie in K
line
	​

, the map is injective on assigned slopes, and all poles or degenerate charts are charged.

Slope eliminant. For every uncharged chart, produce R
τ
	​

(T)∈K
line
	​

[T]∖{0}. A multivariate affine-plane equation receives the terminal finding UNBOUNDED_SLOPE_PROJECTION, not a slope cap.

AP descent. Prove that source AP
corr
	​

 forces R
τ
	​


=0, or identify the exact official paid branch containing the failure and include its slopes in the corresponding cap.

Final integer arithmetic. Compute M
led
	​

 from (1) and check

2
128
M
led
	​

≤q
line
	​

.

A correct arithmetic checker is:

M = sum(all paid distinct-slope caps) + aggregate_LOW_cap

for each retained balanced/high tag tau:
    require normalization field == K_line
    require normalization injective
    require R_tau is a nonzero univariate polynomial in K_line[T]
    M += exact_K_line_root_count(R_tau)
         or min(q_line, degree(R_tau))

accept LEDGER_CLOSED iff 2^128 * M <= q_line

For a fixed explicit certificate, root sets and original slope sets can be unioned before counting; that exploits same-slope collisions and can improve on the sum bound.

5. Next exact lemma

The first unfilled numerical term, after granting the branch partition, is the aggregate LOW cap:

L-CYCLE109-LOW-AGGREGATE-RESIDUAL-SLOPE-IMAGE

For the official coefficient field and official residue embedding into K
line
	​

, define

L
t
	​

=
⎩
⎨
⎧
	​

z∈K
line
	​

:
∃Q, degQ<k+t,
agr(Q,w)≥k+σ,
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

∖B
paid
	​

.

Prove an explicit effective bound

	​

1≤t<σ
⋃
	​

L
t
	​

	​

≤L
agg
	​

(n)
(12)

whose constants and exponent are independent of k,σ,t.

A per-t result is insufficient unless its sum over t is included.

After (12), the next exact requirement is:

L-CYCLE109-BALANCED-HIGH-SLOPE-ELIMINANT-BUDGET

For every retained balanced or high chart, prove a nonzero univariate slope eliminant R
τ
	​

 with an explicit root cap, and prove the aggregate inequality

	​

c
end
	​

+c
quot
	​

+c
per
	​

+c
cont
	​

+c
del1
	​

+c
tan
	​

+c
field
	​

+c
color
	​

+c
hidden
	​

+c
internal
	​

+c
norm
	​

+L
agg
	​

(n)+
τ∈T
bal
	​

∪T
high
	​

∑
	​

ρ
τ
	​

≤⌊
2
128
q
line
	​

	​

⌋.
	​

(13)

Equation (13) converts this BANKABLE_LEMMA into PROOF.

Self-audit

1. What exact implication did I prove, and what did I not prove?

I proved:

slope-level partition
+ exact paid/LOW caps
+ aggregate tagged charts
+ injective same-field normalizations
+ nonzero univariate slope eliminants
+ 2
128
M
led
	​

≤q
line
	​

	​

implies

N
off
	​

/q
line
	​

≤2
−128
.

I did not prove any nontrivial paid-branch cap other than the banked endpoint cap, the LOW aggregate image theorem, the balanced or high chart cover, AP descent, the high-plane slope projection theorem, or the targeted q
line
	​

 dominance inequality.

2. Is the result official-prize-relevant?

Yes, as a conditional official-field reduction. It is not a prize proof and not merely a finite/model certificate.

3. What is the first line where the theorem could fail?

Without granting the source cover, the first failure is

official bad slope⟶slope-level charged or tagged partition.

Conditional on that partition, the first unsupported numerical term is the aggregate LOW residual image (12). For a retained HIGH chart, another precise failure is

multivariate affine-plane separator\centernot⇒bounded slope projection.

4. Are the fields and 2
−128
 target used correctly?

Yes.

q
gen
	​

: only corrected reserve and source applicability.

q
code
	​

: coefficient/source field; no denominator role.

q
line
	​

: actual slope sample size and sole denominator here.

q
chal
	​

: not used; requires (10)–(11).

Target: exactly 2
128
N
off
	​

≤q
line
	​

, including the floor.

5. Could the named structural mechanisms reduce the numerator?

Yes, but only through distinct-slope image caps.

Quotient/periodic and contained/delete-one structure can collapse many witnesses to few slopes.

Same-slope support collisions always weakly reduce the numerator and contribute zero extra slopes.

Tangent and endpoint terms can be isolated; endpoint contributes at most one.

Field confinement can cap a branch by the size of the proper field or affine subfield coset containing its slopes.

An affine normalization itself is cardinality-preserving; it reduces nothing. An affine-color image or bounded fiber theorem may reduce the numerator.

Overlaps among paid branches or charts can further reduce the true union, but cannot justify using another field denominator.

6. What converts this into PROOF or COUNTERPACKET?

This is not a PLAN. It becomes PROOF by proving (12), the paid cap vector, the balanced/high univariate slope-eliminant theorem, AP-to-charge descent, and the final inequality (13).

It becomes COUNTERPACKET only through a growing official above-reserve family, after all paid branches are absent or capped, for which either the aggregate LOW image, mandatory tag count, or uncharged slope projection exceeds every permitted polynomial budget, or AP
corr
	​

 holds while every valid slope eliminant is zero.
