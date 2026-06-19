# ROLE 07 - Scalar List / Full-Support Local-Limit Bridge

Attack the grand list challenge side.

Cycle 58 says that at official scale `epsilon*=2^-128`, correlated interleaving is probably reducible to scalar list/full-support local limit by linear projection. The remaining wall is scalar.

Let `C=RS[F,L,k]`. For a received word `y`, define full agreement supports:

```text
A(P) = { x in L : P(x)=y(x) },   P in C.
```

The raw feasible support family is not valid: a codeword anchor can make all `a`-subsets feasible while the actual list size is one.

Goal: prove or sharply formulate the scalar full-support local-limit theorem above corrected reserve:

```text
# { P in C : |A(P)| >= a }
```

or the number of distinct full-support sets is at most the finite target, after quotient/overagreement templates are charged.

Tasks:

1. Prove the projection theorem for interleaved lists at `2^-128` if not already fully proved.
2. Reduce the official interleaved list threshold to the scalar theorem with exact finite inequalities.
3. Attack the scalar theorem in syndrome coordinates.
4. If false, produce a scalar counterpacket that survives actual-list/full-support canonicalization.

