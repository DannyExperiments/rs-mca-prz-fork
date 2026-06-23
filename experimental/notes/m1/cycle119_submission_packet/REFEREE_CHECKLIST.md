# Referee Checklist

This checklist lists the fastest ways the claim could fail.

## A. Abstract Two-Ended Theorem

Check:

```text
1. Does deg(P_J-P_J') <= j-sigma+1 really imply common coefficients
   j, j-1, ..., j-sigma+2?

2. Does the coefficient map
   Q=P_J A -> ([X^0]Q, [X^{j+1}]Q, ..., [X^{j+sigma-1}]Q)
   recover all coefficients of A using one matrix independent of J?

3. Is the matrix triangular with diagonal c,1,...,1?

4. Does ell(P_J A)=A(beta) hold on all P_J F[X]_<sigma?

5. Is W_J^perp = P_J F[X]_<sigma under the weighted Vandermonde pairing?

6. Does y_0+z_J y_1 in W_J follow with z_J=-P_J(beta)^(-1)?

7. Does a common line f,g exist by surjectivity of the parity-check map?

8. Does noncontainment follow from j+1 <= r and beta notin D?
```

Fatal failure if any answer is no.

## B. Cycle84 Instantiation

Check:

```text
1. Native locators satisfy P_T=X^113-X^112+O(X^107).
2. P_T(beta)=4(beta-1)Phi(T).
3. Imported occupancy is exactly 52,747,567,092 distinct Phi(T).
4. A*/R* split has |A*|=120 and |R*|=136.
5. Augmented co-support has j=249.
6. deg(P_T*-P_T'*) <= 136+107=243.
7. j-sigma+1 = 249-7+1 = 243.
8. P_T(0)=-1 on the Cycle84 shell.
9. P_T*(0)=-P_R*(0) != 0.
10. P_R*(beta)4(beta-1) is fixed and nonzero.
11. Multiplication/inversion/negation introduce no new slope collisions.
```

Fatal failure if any answer is no.

## C. Radius And Denominator

Check:

```text
1. Agreement is 263.
2. Distance is at most 512-263=249.
3. Strict target is d < (125/256)*512 = 250.
4. 249 < 250.
5. q_line=17^32 under the source definition.
6. floor(17^32/2^128)=6.
7. 52,747,567,092 > 6.
```

## D. Official Admissibility

Check:

```text
1. Does the official challenge accept F_17^32?
2. Does it accept H=<theta>, |H|=512?
3. Does official epsilon_mca match the support-wise predicate?
4. Is gamma sampled uniformly from F_17^32?
5. Are there no official filters/charges/quotients that reduce the event mass?
```

If any answer is unknown, the correct public status remains:

```text
finite/source theorem plus official-admissibility route cut.
```

