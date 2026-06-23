# Referee Checklist

Use this as the fastest route to falsify or confirm the packet.

## A. ABF Definition Match

Check:

```text
1. ABF Definition 2.11 admits RS[F,L,k] over finite fields.
2. ABF Definition 2.12 defines smooth domains as multiplicative cosets of
   power-of-two subgroups of F^*.
3. The row H=<theta>, |H|=512, is such a smooth domain.
4. The rate 256/512 is one of the allowed rates.
5. Definition 4.3 samples gamma uniformly from F.
6. Definition 4.3 uses |S| >= (1-delta)n.
7. Definition 4.3 uses same-support noncontainment.
8. No extra endpoint, quotient, periodic, duplicate, charge, or retained-event
   filter appears in the grand MCA definition.
```

Fatal failure if any answer is no.

## B. Cycle116 Finite Chain

Check:

```text
1. Cycle84 occupancy is exactly N=52,747,567,092 distinct Phi values.
2. The fixed-jet bridge proves P_T=X^113-X^112+O(X^107).
3. The product-scalar bridge proves P_T(beta)=4(beta-1)Phi(T).
4. The Cycle116 fixed-jet transfer constructs one line f+zg.
5. The smooth lift gives C=RS[F_17^32,H,256].
6. Agreement is at least 262 on each certified support.
7. Same-support noncontainment is proved, not assumed.
8. The reciprocal-affine slope map introduces no new collisions.
```

Fatal failure if any answer is no.

## C. ABF Threshold Arithmetic

Check:

```text
1. n=512.
2. delta=125/256.
3. (1-delta)n=262.
4. Cycle116 supplies agreement 262.
5. 17^32 =
   2367911594760467245844106297320951247361.
6. floor(17^32/2^128)=6.
7. 52,747,567,092 > 6.
8. Therefore N/17^32 > 2^-128.
```

## D. Cycle119 Strict Addendum

Check:

```text
1. The two-ended theorem uses common top six coefficients plus common constant.
2. It does not use the varying degree-243 coefficient.
3. The augmented co-support has size 249.
4. Agreement is 263.
5. Distance is 249.
6. 249 < 250.
7. The same numerator N is preserved.
```

Cycle119 is not required for ABF closed-threshold Definition 4.3, so a fatal
Cycle119 flaw does not automatically kill the Cycle116 ABF negative result.

## E. Claim Discipline

Reject the note if it claims any of:

```text
exact delta*_C;
ordinary list decoding;
grand list decoding;
protocol soundness failure;
automatic prize award;
peer-reviewed acceptance;
prime-field/deployed-row result.
```

