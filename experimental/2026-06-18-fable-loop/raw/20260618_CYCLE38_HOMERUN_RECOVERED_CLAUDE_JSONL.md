I have completed the investigation. File-writing, code-execution (Jupyter), and shell are all denied in this harness, so I cannot bank a freshly-run certificate or write to `output_files/`. I deliver everything inline, which is sufficient because the obstruction turned out to be a single mistyped line that I can repair and audit statically against already-validated machinery.

---

# Cycle 38 Homerun Result — `W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT`

Classification: `AUDIT` (checker repair, provable statically) + `BANKABLE_LEMMA` (source-validity gates, explicit constants) + `EXACT_NEW_WALL` (symbolic certificate + good-reduction) + `EXPERIMENTAL` (the one finite fact still needing a run). No `PROOF`, no `COUNTERPACKET`, no `S_4` banked.

## 1. Root-cause diagnosis (exact, single line)

The Cycle 37 checker fails at line 133 of `…_unrun_model_checker.py`:

```python
w1,w2,w3,w4=(OF,ZF),(ZF,OF),(OF,OF),(OF,ZF)     # W_{n-1..n-4}, fixed free data
```

`OF=(1,0)`, `ZF=(0,0)`, `ALPHA=(0,1)` are **F-elements** (pairs of ints). But `w1..w4` are consumed only inside `qres` via `fmul`/`fsub`, which require F-elements. The literals above are **residue-pairs** (pairs of F-elements, i.e. elements of `A=F[X]/E`). So `fmul(w1,t1)` computes `((OF,ZF)[0]*… )%P` = `tuple % int` →

```text
TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
```

The author conflated two type layers and also conflated the residue variable `X` with the field generator `alpha`. The Cycle 37 JSON itself states the intent: `W_{n-1..n-4} = 1, alpha, 1+alpha, 1`. As F-elements that is `OF, ALPHA, OF+ALPHA, OF`. Nothing else in the file is mistyped (`u`, `b_res`, `ell` are correctly residue-pairs; `lam` correctly lifts `tau_i` to `(x,0)`).

## 2. The repair (minimal, 1 line) + static-equivalence audit

Replace line 133 with:

```python
w1,w2,w3,w4 = OF, ALPHA, fadd(OF,ALPHA), OF   # W_{n-1..n-4}=1,alpha,1+alpha,1 (F-elements)
```

Everything else in the Cycle 37 file is left unchanged. I audited the corrected data-flow line-for-line against the **validated** Cycle 32 reference (`20260618_cycle32_t2_j4_monodromy_histogram.py`, whose histograms already match direct support enumeration off `Delta=0`):

| Cycle 38 function | Cycle 32 reference | structural match after fix |
|---|---|---|
| `qres(tau)` (`q3=w1; q2=w2−w1·t1; …`) | `q_residue_from_tau` (`q3=Wn1; q2=Wn2−Wn1·tau1; …`) | identical; `w_i=Wn_i` now both F-elements ✓ |
| `lam(tau)` (`XI[4]−t1·XI[3]+t2·XI[2]−t3·XI[1]+t4`) | `lambda_from_tau` | identical ✓ |
| `eqres` (`(u−z·b)·lam − ell·qres`) | `equation_residue` | identical ✓ |
| `build` (finite-difference columns) | `solve_tau_for_z` | identical ✓ |

Hand-lemma making `build` correct: `eqres(z,·)` is **affine-linear in `tau`** (`lam` is linear in `tau_1..tau_4`; `qres` is affine-linear; `(u−zb)` and `ell` are `tau`-free). Hence `eqres(z,e_i)−eqres(z,0)` is exactly column `i` of `M(z)`, and `M(z)tau=−C_0(z)` is recovered correctly.

The only difference from Cycle 32 is that Cycle 32 derives `(u, W_{n-1..n-4}, b)` from one random interpolated `W`, whereas Cycle 38 fixes them as explicit source-valid free data. So the repaired checker is **correct relative to validated machinery**; whether it *passes* (types `"4"` and `"13"` appear off `Delta`) is the one remaining empirical fact.

Optional hardening to make any run self-validating (prepend to `__main__`):

```python
assert P % 4 == 3 and all((x*x) % P != (P-1) for x in range(P))   # -1 nonresidue
# affine-linearity self-check (guarantees build() extracts M correctly):
import random; rng = random.Random(1)
for _ in range(20):
    z=(rng.randrange(P),rng.randrange(P)); a=[rng.randrange(P) for _ in range(4)]; bb=[rng.randrange(P) for _ in range(4)]
    f0=eqres(z,[0,0,0,0]); fa=eqres(z,a); fb=eqres(z,bb); fab=eqres(z,[(a[i]+bb[i])%P for i in range(4)])
    assert rsub(fab,f0)==rsub(rsub(fa,f0),rsub(f0,fb))   # f(a+b)-f0 == (fa-f0)+(fb-f0)
```

## 3. Source-validity gates — hand-verified with explicit constants (`BANKABLE_LEMMA / AUDIT`)

For `p ≡ 3 mod 4`, `alpha^2=-1`, `E=X^2+alpha X+1`, `b=[Bnum]_E=X`, free data `u=[W]_E=1+X`, `(W_{n-1},…,W_{n-4})=(1,alpha,1+alpha,1)`:

1. **No `F_p` root.** `E(a)=(a^2+1)+alpha·a`; the `alpha`-part is `a`, zero only at `a=0`, and `E(0)=1≠0`. ✓
2. **`E`/`E^tau` separated.** `E−E^tau=2 alpha X`; a common root forces `X=0`, but `E(0)=1`. ✓
3. **`c∉B` branch active.** `c=alpha∉F_p ⇒ c_b≠0`. ✓
4. **`kappa=u_0`.** `kappa=wedge_F(u,[b]_E)`; `[b]_E=(0,1)` so `wedge((u_0,u_1),(0,1))=u_0`. With `u=1+X`, `kappa=1≠0`. ✓
5. **Top symbol nonzero.** `c=alpha,d=1 ⇒ Im(c)=1, Im(d)=0, Im(conj(c)d)=Im(−alpha)=−1`, so `Q_4=N(c_b)·(0−1·(−1))=N(c_b)≠0`. Hence `TopSym(Delta)=−N(kappa)N(z)^2Q_4` is a nonzero polynomial, `Delta` is not identically zero, and the singular locus `Delta=0` contributes `≤4p=O(p)` slopes (Cycle 33 `L-T2J4-A2B-SINGULAR-OP`). ✓

**New gate (closes a source-validity gap Cycle 37 left implicit).** The checker sets `u=[W]_E` and `(W_{n-1..n-4})` independently. This is genuinely source-valid: interpolation `F^n→\{deg≤n-1\}` is a bijection, and `W↦([W]_E, \text{top-4 coeffs})` is an `F`-linear map `F^n→F^2×F^4` that is surjective for `n≥6` (the residue functional restricted to `X^0,…,X^{n-5}` already hits all of `F[X]/E` since it contains `1,X`). For `p0=31`, `n=31≫6`, and any `w∈F^n` splits as `w_0+alpha w_1` with base anchors `w_0,w_1∈B^n`. So the explicit free data is realized by a genuine source-valid base-anchor word. ✓

## 4. What remains unverifiable in this harness

Only one fact: that the off-`Delta` squarefree specializations of `L_tau` on some line `z_1=mz_0+e` at `p0=31` include **both** type `"4"` (4-cycle) and type `"13"` (3-cycle). The corrected Cycle 35/36 criterion is enforced (transitivity comes from the 4-cycle, not the forbidden "irreducible resolvent + nonsquare disc" shortcut; the even type `"13"` simultaneously kills the sign constant-field obstruction, since `G_geom∈\{A_4,S_4\}` and an even degree-one Frobenius is impossible if `G_geom=A_4`). The Cycle 32 *random* instance at `p=29` already exhibited `"4"`, `"13"`, `"1111"` in `S_4` proportions, so generic occurrence is well-evidenced — but the **specific** free data could in principle be non-generic (a forced square `disc_num` would push into `A_4` and suppress `"4"`). That risk is exactly why the run, with the self-checks above, is the cheap high-information next action. Per Cycle 37 discipline I do **not** assert a run occurred and do **not** bank the certificate.

## 5. Route assessment and exact next steps

The chain is intact and now unblocked: Cycle 33 (singular `O(p)`) + Cycle 34 (off-curve birational onto the Cycle 30 quadric, rank-2, surface-sized) + Cycle 35 (finite-place `S_4` ⇒ `Theta(p^2/24)` split density in the local branch) + Cycle 36 (explicit family, reduction to one good prime) + Cycle 38 (working checker). The remaining mathematics is geometric `S_4` of `L_tau/\bar F_p(z_0,z_1)`, uniformly in `p`.

Sharpened `EXACT_NEW_WALL` (replaces the finite-scan dependence):

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
(a) Compute disc_num(z_0,z_1) and resolvent R(y) symbolically from
    tau_i=det M_i/Delta for E=X^2+alphaX+1, b=X, u=1+X, W=(1,alpha,1+alpha,1).
(b) Prove disc_num has nonconstant squarefree part and R(y) is absolutely
    irreducible over \bar F_p(z_0,z_1), plus one explicit "4" slice for transitivity.
(c) Prove L-T2J4-A2B-GOODRED: (a),(b) are good-reduction-open in the p=3 mod4
    family, so one good prime promotes G_geom=S_4 to all but finitely many p,
    with the excluded-prime set recorded; then a uniform-complexity Lang-Weil
    count yields C2 = p^2/24 + O(p^{3/2}) = Theta(q_line) in this local branch.
```

Obstruction ranking for the promotion, by risk: (i) a hidden forced square factor in `disc_num` peculiar to this symmetric `E,b` choice (would be a `ROUTE_CUT`); (ii) constant-field drift across the family (cut *conditional* on geometric `S_4`, must be re-checked uniformly); (iii) uniform control of the Lang-Weil error so it does not swamp the `p^2/24` main term.

---

**Do you see a route to a full solve? If yes, what is the next exact lemma or construction?**

Not to a full prize-level solve, and the route board's ledger separations forbid promoting any of this past a restricted local `t=2,j=4` sub-reserve object (no merge of `q_gen=p` with `q_line=p^2`; no MCA/CA/list/line/curve-MCA/protocol/SNARK status). But there is a concrete two-step route to the next real milestone (the uniform/growing-prime `Theta(q_line)` counterpacket *seed*):

1. **Single-prime confirmation (one run away):** apply the one-line repair of §2 and run `cycle38_checker.py` at `p0=31`; a `PASS` (types `"4"`+`"13"` off `Delta`) banks `G_geom=G_arith=S_4` for that instance via Cycle 35's certificate.
2. **Next exact lemma — `L-T2J4-A2B-GOODRED`:** prove the symbolic `disc_num`/resolvent conditions of §5(a,b) and that they are good-reduction-open in the `p≡3 mod 4` family, promoting one good prime to almost all primes, then attach a uniform-complexity Lang-Weil count. That converts the conditional seed into a genuine restricted local `Theta(q_line)` counterpacket seed — still strictly sub-reserve, never a corrected-reserve or prize statement.
