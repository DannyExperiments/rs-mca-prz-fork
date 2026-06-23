# Role 04: Cycle84 Instantiation Auditor

Audit the Cycle84-specific facts needed by Role05. Do not spend your answer on generic line-decoding prose.

Prove or kill the concrete instantiation:

```text
P_T(0) = -1 for all Cycle84 locators P_T
P_T*(0) = P_R*(0) P_T(0) is common and nonzero
P_T*(beta) = fixed_nonzero_scalar * Phi(T)
deg(P_T*-P_T'*) <= 243
|J_T*|=249 and agreement=263
distinct slopes = #im Phi = 52,747,567,092
```

Use the attached Cycle116 theorem/checker files and Role05 response. If you need to derive from slot polynomials, show the exact product:

```text
fixed root factor
seven moving block constants
R* constants
beta-evaluation scalar
```

If any scalar can be zero, if any constant depends on T, or if any collision can enter the slope map, return `ROUTE_CUT` with the exact failed identity.
