# M31 defect-67 divisor wall as a planted ternary MDS-code census

## Status

PROVED as an exact equivalence for the repaired paired-prefix conventions in
cap25_v13_m31_c1024_paired_prefix_audit.md.

This note does not decide the resulting codeword census. It replaces the
nonlinear degree-34 divisor wall by one explicit constant-weight ternary
kernel problem.

## Setup

~~~text
p = 2^31-1,
W(Z) = T_1024(2Z-1),
R = {y in F_p : T_2048(y)=0}.
~~~

The roots in R are distinct, nonzero, and stable under y -> -y. Choose
representatives c_1,...,c_1024 of the antipodal pairs, with c_1=eta, where
-eta is the reserved planted root. Define the 33 x 1024 matrix

~~~text
H_(s,j) = c_j^(2s+1),   0<=s<=32.
~~~

## Exact theorem

The following are equivalent.

1. There are a monic polynomial E in F_p[Z] of degree 34 and lambda != 0
   such that

   ~~~text
   D(Z)=E(Z)^2-lambda^2 Z divides W(Z),
   E(eta^2)=lambda eta.
   ~~~

2. The monic degree-68 polynomial

   ~~~text
   F(Y)=E(Y^2)+lambda Y
   ~~~

   divides T_2048(Y) and satisfies F(-eta)=0.

3. There is a vector

   ~~~text
   epsilon in {-1,0,1}^1024,
   wt(epsilon)=68,
   epsilon_1=-1,
   H epsilon=0.
   ~~~

Equivalently, the last condition is the system

~~~text
sum_(j=1)^1024 epsilon_j c_j^(2s+1)=0,   0<=s<=32.
~~~

Moreover, rank(H)=33, every 33 columns are independent, and ker(H) is an
[1024,991,34] MDS generalized Reed-Solomon code. The condition lambda != 0
is automatic in the ternary formulation.

## Proof

The Chebyshev composition identity gives

~~~text
T_2048(Y)=T_1024(T_2(Y))=T_1024(2Y^2-1)=W(Y^2).
~~~

Put

~~~text
F_+(Y)=E(Y^2)+lambda Y,
F_-(Y)=E(Y^2)-lambda Y=F_+(-Y).
~~~

Then F_+(Y)F_-(Y)=D(Y^2). Thus D divides W implies F_+ divides T_2048.
Conversely, if F_+ divides T_2048, then evenness gives F_- divides T_2048.
The two factors are coprime: a common root y would satisfy 2 lambda y=0;
since p is odd, lambda != 0, and T_2048(0)=1, this is impossible. Hence
F_+F_- divides T_2048, and injectivity of Z -> Y^2 in the polynomial ring
gives D divides W. The planted condition is exactly
F_+(-eta)=E(eta^2)-lambda eta=0.

Now suppose F_+ divides T_2048. Coprimality of F_+(Y) and F_+(-Y) also
shows that F_+ cannot contain both members of an antipodal root pair. Its
68 roots therefore select a vector epsilon in {-1,0,1}^1024; the planted
root gives epsilon_1=-1.

All odd coefficients of F_+(Y)=E(Y^2)+lambda Y above degree one vanish.
Since p>68, Newton identities through degree 68 are invertible, so this is
equivalent to vanishing of the 33 odd power sums of degrees 1,3,...,65.
Those power sums are exactly H epsilon=0.

Conversely, a ternary vector satisfying the printed conditions defines

~~~text
F_epsilon(Y)=prod_(epsilon_j!=0) (Y-epsilon_j c_j).
~~~

It is a monic degree-68 divisor of T_2048. Newton identities show that all
odd coefficients above degree one vanish, hence
F_epsilon(Y)=E(Y^2)+lambda Y for a monic degree-34 polynomial E. If
lambda=0, the nonzero root set would be antipodally closed, contrary to
selecting at most one member of each pair. Thus lambda != 0, and the
planted sign supplies the orientation.

Finally, write z_j=c_j^2. The values z_j are distinct and H_(s,j)=c_j z_j^s.
Every 33-column minor is a nonzero column scaling of a Vandermonde
determinant. Therefore rank(H)=33, every 33 columns are independent, and
the kernel has dimension 991 and minimum distance 34.

## Finite-ledger effect

This is a compiler, not a numerical payment. It leaves unchanged:

~~~text
M31 kappa=2 two-shell residual rows: 2,987,412
U(1116023): unchanged
B*: 16,777,215
planted-conditioned target B*-F_2048: 9,980,810
~~~

The value 9,980,810 is a planted lower-floor-conditioned target, not an
upper-ledger subtraction.

The exact next finite question is whether the displayed planted weight-68
ternary codeword exists.

- If the census is empty, the first non-factor-through defect-67 branch is
  eliminated.
- If it is nonempty, every solution must still pass the exact 511-of-956
  even-completion equations, canonical first-match replay, and add-back audit.
- Higher defects remain unpaid.

## Nonclaims

- No codeword emptiness or complete census is proved.
- No M31 upper numerator is reduced.
- No row-sharp-Q inequality is proved.
- No fixed-remainder floor is stacked as an upper payment.
- No deployed row, Grand MCA threshold, or Grand List threshold is closed.
