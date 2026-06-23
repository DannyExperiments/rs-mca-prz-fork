# Role 01: Two-Ended Proof Builder

Your only job is to prove or repair Role05's theorem:

```text
L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

Read `context/cycle118_returns/05_role05_response.md` carefully.

Build a standalone theorem:

```text
Given locators P_J of degree j with:
  common coefficients in degrees j, j-1, ..., j-(sigma-2)
  common nonzero constant coefficient P_J(0)=c
prove a fixed-line LD_sw lower bound using z_J = -1/P_J(beta).
```

Then instantiate it with:

```text
n=512
k=256
j=249
sigma=7
agreement=263
J_T* = J_T union R*
|R*|=136
|A*|=120
P_T(0) = -1
P_R*(0) nonzero
```

You must explicitly prove:

```text
existence of one global linear functional ell
surjectivity to one common line f+zg
support witnesses of size 263
uniform noncontainment
distinct slope count = 52,747,567,092
strict distance < 250
```

If you find a degree/k mismatch, repair it or return `ROUTE_CUT` with the exact line that fails.
