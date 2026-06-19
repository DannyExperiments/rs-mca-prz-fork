# Common Prompt For All Six External Instances

Try to fully solve the reserve lift through the Cycle 44 cosupport
moment/landing identity. If you cannot fully solve it, reduce it to the next
exact lemma, construction, or falsifier. No Internet. Take all the time to
reason you need. Use MAX reasoning.

You are working on RS-MCA / Proximity Prize experimental material. Do not edit
main papers. Treat raw model outputs as provenance only. Every mathematical
claim must be tagged as one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
EXPERIMENTAL
```

Keep the ledgers separate:

```text
q_gen = p
B = F_p
F = F_{p^2}
q_line = p^2
q_chal = unused
D = F_p
deg E = t = sigma
A = F[X]/E
j = |T| = n-a
```

Source object: residue-line datum from `tex/slackMCA_v3.tex:def:residue`.
The support/cosupport setup is `T=D\S`, `I_S=interp_S(w)`, and the bad-line
landing condition is

```text
rho(T)=[I_S]_E in F*b,  b=[Bnum]_E.
```

Cycle 44 banked identity:

```text
xi = [X]_E
ell = [X^p-X]_E
Lambda(T) = [L_T]_E
rho(T) = -ell * Lambda(T)^(-1) * N(T)
N(T)=sum_{d in D} w(d)L_T(d)(xi-d)^(-1)
```

Writing

```text
L_T(X)=sum_{m=0}^j (-1)^m e_m(T)X^(j-m),
```

both `N(T)` and `Lambda(T)` are affine-linear in the elementary symmetric
functions `e_m(T)`.

Cycle 44 also banked an exact additive-character landing identity:

```text
#Land = binom(p,j)/p^(2(t-1)) + E_error.
```

The current exact wall is:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION
```

The preferred subwall is:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

Target inequality:

```text
M_2 = sum_z nu(z)^2 <= #Land + (1+o(1)) #Land^2/q_line,
nu(z)=#{T: rho(T)=z b}.
```

Falsifier target:

```text
Find a source-valid growing family with max_z nu(z) >= #Land/p^(1+epsilon),
forcing N_split=o(min(q_line, binom(p,j)/p^(2(t-1)))).
```

Do not promote anything to corrected-reserve, generated-field theorem,
MCA/list/line/curve-MCA, protocol, SNARK, prize, or final `COUNTERPACKET`
unless you verify every source hypothesis.

End your answer by saying:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```
