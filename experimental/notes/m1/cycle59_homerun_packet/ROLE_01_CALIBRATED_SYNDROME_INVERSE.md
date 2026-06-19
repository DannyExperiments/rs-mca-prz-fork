# ROLE 01 - Prove The Calibrated Syndrome Transverse-Secant Inverse

Attack the main wall directly:

```text
W-MCA-CALIBRATED-SYNDROME-TRANSVERSE-SECANT-INVERSE
```

Goal: prove or sharply advance a theorem of the following form.

Let `C = RS[F,L,k]`, `n=|L|`, `rho=k/n`, `a=k+sigma`, `j=n-a`, and for each `j`-set `T` let

```text
V_T = span{H_RS(:,x): x in T}
```

in syndrome space. For an affine line `ell(z)=u+zv`, bound the number of transverse incidences

```text
ell(z) in V_T,    v notin V_T.
```

Above the corrected entropy reserve, after deleting or charging quotient/action-rank and tangent/common-envelope packets, prove

```text
# transverse bad slopes
  <= n^{1+o(1)} + O(binom(n,k+sigma)/q^{sigma-1})
```

or the strongest finite version you can prove.

Requirements:

1. Work in syndrome space, not only balanced residue coordinates.
2. Cover all denominator degrees implicitly, or state exactly why the syndrome formulation loses none.
3. Include the occupancy/main term explicitly.
4. Identify quotient/action-rank exceptions precisely.
5. Do not hide behind random-anchor averages; this is a maximum-over-lines theorem.

If you cannot prove it, extract the exact smaller lemma that would prove it.

