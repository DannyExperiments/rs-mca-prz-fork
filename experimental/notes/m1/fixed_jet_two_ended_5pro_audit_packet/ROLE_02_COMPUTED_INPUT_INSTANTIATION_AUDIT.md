# Role 02 - Computed Input And Instantiation Audit

Audit Sections 4-6 of:

```text
fixed_jet_and_two_ended_transfer_note.md
```

Your job is not to rerun a 52-billion product census. Your job is to decide
whether the stated computed input is sufficient for the claimed row
instantiations, and whether any hidden field or disjointness hypothesis is
missing.

## Claims To Audit

Given the computed input:

```text
P_T(X) = X^113 - X^112 + O(X^107),
P_T(beta) = (beta-1)3^28 Phi(T),
#{Phi(T)} = 52,747,567,092,
```

and the field facts:

```text
F0 = F_17[xi]/(xi^16+xi^8+3),
eta = 6 xi^9,
beta = xi+2,
ord(eta)=256,
theta^2=eta,
ord(theta)=512,
H=<theta>=D0 disjoint_union theta D0,
beta notin H,
```

check whether the note correctly proves:

```text
LD_sw(RS[F_17^32,H,256],262) >= 52,747,567,092
```

and:

```text
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092.
```

## Required Checks

- For agreement 262: does adjoining a fixed 137-point odd-coset set really
  give `j=250`, `sigma=6`, `k=256`?
- For agreement 263: does adjoining a fixed 136-point odd-coset set really
  give `j=249`, `sigma=7`, `k=256`?
- Are `J_T` and the odd-coset padding sets disjoint?
- Is `P_R P_T` or `P_R* P_T` square-free as the locator of the union?
- Is `beta notin H` enough to make the evaluation scalars nonzero?
- Does multiplication by the fixed padding locator preserve the distinct
  slope count?
- Does the two-ended constant condition follow from `P_T(0)=-1` and
  `P_R*(0) != 0`?
- Is the support size exactly 262 and 263 respectively?

Find the first false line if one exists.
