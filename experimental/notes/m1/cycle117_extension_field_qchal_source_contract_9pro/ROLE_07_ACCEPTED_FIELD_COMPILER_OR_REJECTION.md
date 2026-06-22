# Role 07 - Accepted-Field Compiler Or Rejection

You are the fallback construction specialist.

If the attached source or official interpretation rejects the extension-field
row `F_17^32`, the next target is:

```text
L-CYCLE117-ACCEPTED-FIELD-FIXED-JET-OCCUPANCY-COMPILER
```

Your task is conditional:

1. First decide whether the extension-field row is accepted or rejected by the
   attached source. If accepted, state that and give only a brief compiler audit.

2. If rejected or missing, propose the strongest possible accepted-field
   compiler theorem:

```text
Input: Cycle84 fixed-jet occupancy data
Output: accepted prime/deployed/smooth row with one affine line, witness
supports, noncontainment, and enough distinct slopes
```

3. Determine what must be preserved exactly:
   - common fixed jet;
   - product-to-locator scalar;
   - distinct slope numerator;
   - noncontainment;
   - smooth multiplicative domain;
   - denominator above/below threshold.

4. Either give a plausible proof route, or prove a `ROUTE_CUT` explaining why
   no such compiler can preserve the numerator without new arithmetic input.

5. If you propose a new prompt/round, make it theorem-focused, not enumeration
   focused.

This role is allowed to be ambitious, but every claim must be mechanically
checkable or stated as a named exact wall.
