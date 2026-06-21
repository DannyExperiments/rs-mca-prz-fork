PROOF

Confidence: high, conditional on the banked Cycle84/Cycle85 packet and fixed-six-jet facts.

The active wall is closed with the preferred package

(n,k,σ,j)=(464,232,6,226).

Take

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
+3),β=X+2,

and

L=F
0
	​

[U]/(U
3
−β),y=U.

The exact executed census gives the stronger result

μ
proj
	​

(U)≤2
	​

.
Separator certificate

Let q
0
	​

=17
16
. Exact projective equality is

[a]=[b] in L
×
/F
0
×
	​

⟺a
q
0
	​

−1
=b
q
0
	​

−1
.

The projective quotient has order

q
0
2
	​

+q
0
	​

+1=RM,

where

R=48,661,191,868,691,111,041,
M=48,661,191,882,642,625,923=3⋅7⋅13⋅73⋅307⋅1321⋅72337⋅83233.

The checker uses the coarser exact key

π(z)=z
(q
0
	​

−1)R
.

Every true projective fiber is contained in a π-fiber, so

μ
proj
	​

(U)≤μ
π
	​

(U).

The deterministic 1,536-shard census returned

records
smooth occupancy
D
smooth
	​

μ
π
	​

(U)
	​

=52,747,567,104,
=52,747,567,062,
=84,
=2.
	​


Thus the complete smooth histogram is

n
1
	​

=52,747,567,020,n
2
	​

=42,n
≥3
	​

=0,

and consequently

μ
proj
	​

(U)≤2≤8
	​

.

All 336 slot logarithms were reconstructed through exact prime-factor tables, recombined by CRT, and verified by exponentiation. Hashing is used only for table placement: the full 55-bit shard offset is compared, so hash collisions cannot alter multiplicities. Independent sort-and-run reducers also matched a collision-free shard and a shard containing a double class.

Execution used four threads, 940.49 seconds, and peak RSS 2,299,780 KiB.

One GRS code and one affine syndrome line

Delete

Z
0
	​

={η
8b
:1≤b≤24}

from D=⟨η⟩=μ
256
	​

, and set D
−
=D∖Z
0
	​

. Every packet support remains in D
−
, and ∣D
−
∣=232.

With c=β−U, use the single 464-point domain

D
(2)
=D
−
∪(c+D
−
).

For x∈D
(2)
, take the parity-check column

h
x
	​

=(1,x,…,x
230
,(β−x)
−1
)
T
.

After nonzero column scaling, these are evaluations of a basis of L[Y]
≤231
	​

; hence this is one [464,232] GRS code.

For combined supports

S(v,T)=T
v
	​

∪(c+T),

the common jet is

J
S
	​

(t)≡(1−t)(1−ct)
112
(1−(c+1)t)(modt
6
).

Partial fractions therefore put every such support on one common affine syndrome line. Transversality follows because a putative containment would give a dependence among 226 distinct columns of a 231×226 Vandermonde matrix.

The slope is, up to one common nonzero affine normalization,

z
v,T
	​

=
vP
T
	​

(U)
1
	​

.

Choose one first-block representative for each of the

N=52,747,567,092

occupied values v=P
T
	​

(β), and use all

P=52,747,567,104

second-block supports. Every slope fiber has size at most μ
proj
	​

(U)≤2. Hence

M
C
	​

(6)≥
2
NP
	​

=1,391,152,917,379,006,070,784.

Meanwhile,

T
line
	​

=⌊
2
128
17
48
	​

⌋=338,617,018,271,848,945,628.

The certified margin is

1,052,535,899,107,157,125,156.
Exact failure protocol

An exact always-correct computation of μ
proj
	​

 uses pivot normalization of

z=z
0
	​

+z
1
	​

U+z
2
	​

U
2
:

divide by the first nonzero z
i
	​

, encode the pivot and two remaining F
0
	​

-coordinates, then externally sort exact keys.

If the smooth checker ever reports multiplicity at least nine, that is only REFINEMENT_REQUIRED. It does not kill the route. A route-killing certificate for y=U must emit one exact projective key and nine distinct admissible tuples whose recomputed values are F
0
×
	​

-proportional.

Self-audit

Proved: μ
proj
	​

(U)≤2, one explicit [464,232] GRS code, one transverse affine syndrome line, and the stated official MCA lower numerator. Not proved: the exact value of μ
proj
	​

(U), or the full prize theorem.

This is an official-profile MCA counterpacket, not merely a finite-model certificate. It is not a scalar-list numerator and not yet the complete prize-level reduction.

The first external failure point is the banked assertion that the Cycle84 circuit gives P distinct 113-point supports with the fixed jet J
T
	​

(t)≡1−t(modt
6
) and occupancy N.

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

=q
chal
	​

=17
48
.

Only q
line
	​

 enters ⌊q
line
	​

/2
128
⌋; no extra q
chal
	​

 factor is credited or debited.

Projective loss is explicitly bounded by two; contained incidences are excluded by Vandermonde rank; same-slope collisions are divided out; common affine normalization is bijective; the numerator is NP, not P
2
.

This is not a PLAN. The next exact theorem toward a full solve is

L-CYCLE87-OFFICIAL-MCA-COUNTERPACKET-TO-FULL-PRIZE-REDUCTION,

which must splice this certified official failure row into the complete prize theorem without changing the field ledger or substituting a scalar-list objective.

Proof report
Replay bundle
Master certificate
PASS certificate
Raw census output

Replay bundle SHA-256:

61480c80e35a4775d705b406d75c811dc5fc01075d0082db8314fc3423b3cf54
cycle84_real_selfdual_checker.cpp
File
cycle84_master_proof_certificate.json
File
CYCLE84_MMAX2_PROOF.md
File