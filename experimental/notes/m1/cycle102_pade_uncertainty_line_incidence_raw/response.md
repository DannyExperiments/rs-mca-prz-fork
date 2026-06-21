I'll start by reading the file index, then the key project files.Let me read the key files identified in the prompt. I'll start with the cycle briefs and route board.Let me read the key notes and the cycle101 detailed audit/response files.The cycle101 response is truncated at section 6 as noted. Let me read the cycle100 and cycle99 audits, plus the strategic files.Now let me read the strategic files. Let me start with the README and DIRECTOR_STATE, then the route board.Now let me read the ROUTE_BOARD, ACTIVE_WALLS, BANKED_LEMMAS, and CUTS files to understand the precise constraints.Now let me read the ACTIVE_WALLS, BANKED_LEMMAS, and CUTS files which are central to the constraints.Now let me read the BANKED_LEMMAS file (focusing on the recent cycles) and the CUTS file.Now let me read the CUTS_AND_FALSE_ROUTES file and the cycle102 prompt (which DIRECTOR_STATE referenced).Let me check the NEXT_PROMPT_QUEUE and search for the cycle102 prompt and cycle98 setup to lock down the exact definitions.I have the strategic picture. Let me find the cycle102 prompt and the cycle98 setup files to lock down exact definitions before reasoning.Let me find the cycle102 prompt and the cycle98 setup/raw files in the index.Let me locate the cycle102 prompt and cycle98 setup files specifically.This is a deep research problem. I've now read the strategic files, the cycle 99/100/101 audits, the truncated cycle 101 response, and the cycle 102 prompt. Before finalizing, let me numerically verify the finite falsifier I constructed for the Padé implication, since the whole route-cut rests on its arithmetic.I have enough to answer. The harness exposes only the `Read` tool (no code execution), so I verified the finite falsifier by hand in `F_29`; all modular arithmetic below is hand-checked and reproducible.

## Classification

```text
ROUTE_CUT  (Padé-divisor implication is FALSE — explicit finite falsifier)
+ BANKABLE_LEMMA  (corrected Padé statement + exact window-length obstruction;
                   Ũ-flatness / linear-readout reformulation of |Theta_U|)
+ EXACT_NEW_WALL  (the e_1-image / shifted-moment uncertainty bound)
```

I do **not** prove `|Theta_U| ≤ n^{O(1)}`, and I do **not** produce a superpolynomial aperiodic counterpacket to `L2` itself. I kill the specific Padé sublane the brief asked me to verify, and I sharpen the wall to a precisely stated next theorem.

Route to a full solution: I do **not** see a complete route this cycle. The Padé-divisor lane is dead (Section 1–2). The surviving route is the uncertainty lane, now reduced to one exact arithmetic statement (Section 4). That statement is open and is the honest frontier.

---

## 1. The Padé-divisor implication is FALSE — explicit finite falsifier

Claimed implication (to verify/kill):

```text
theta active  =>  Q_theta (Padé/BM denominator of (theta^j - P_j)_{j=1..sigma+1})
                  is compatible with / divides X^n - 1.
```

**Falsifier.** Take

```text
p = 29,  n = 7  (7 | 28 = p-1),  H = mu_7 = {1, 7, 16, 20, 23, 24, 25} ⊂ F_29^*
sigma = 3   (window length sigma+1 = 4)
m = |S'| = 3,  s = n - m = 4,  k = s - sigma = 1,  deg U = s+1 = 5
```

`n = 7` is prime, so `mu_7` has **no proper nontrivial subgroup**: the prefix is automatically aperiodic, and no quotient-periodic charging applies. This is a clean aperiodic-core instance.

Witness subset and its power-sum window (all computed mod 29):

```text
S' = {1, 16, 24} ⊂ mu_7
a_1 = p_1(S') = 1+16+24            = 12
a_2 = p_2(S') = 1+24+25            = 21    (16^2=24, 24^2=25)
a_3 = p_3(S') = 1+ 7+20            = 28    (16^3= 7, 24^3=20)
a_4 = p_4(S') = 1+25+16            = 13    (16^4=25, 24^4=16)
```

Make `theta = 2` active by choosing the prefix `P_j := theta^j - a_j`:

```text
P_1 = 2-12 = 19,  P_2 = 4-21 = 12,  P_3 = 8-28 = 9,  P_4 = 16-13 = 3.
```

Then `a_j = theta^j - P_j = p_j(S')` for `j=1..4`, so by the banked equivalence `theta=2 ∉ H` is **active**, with genuine `mu_7`-witness `S'={1,16,24}` (and `deg U = 5 ≥ sigma+1 = 4`, so the prefix is realizable by a monic `U`).

Now compute the Padé/Berlekamp–Massey denominator of the window `(12,21,28,13)`.

- No length-1 LFSR fits: `a_2/a_1 = 21·12^{-1} = 21·17 = 9`, but `9·a_2 = 9·21 = 15 ≠ 28 = a_3`.
- A length-2 LFSR `a_j = c_1 a_{j-1} + c_2 a_{j-2}` is forced by the `(a_3,a_4)` equations:

```text
21 c_1 + 12 c_2 = 28
28 c_1 + 21 c_2 = 13     =>   c_1 = 24,  c_2 = -1   (mod 29)
```

Verify: `24·21 - 12 = 11 - 12 = -1 = 28 = a_3`; `24·28 - 21 = 5 - 21 = -16 = 13 = a_4`. ✓

So the minimal connection polynomial / Padé denominator is

```text
Q_theta(t) = 1 - 24 t + t^2,   reciprocal char poly  C(T) = T^2 - 24 T + 1.
```

Discriminant `= 24^2 - 4 = 572 ≡ 21 (mod 29)`. The quadratic residues mod 29 are

```text
{1,4,5,6,7,9,13,16,20,22,23,24,25,28},   and  21 ∉ QR.
```

Hence `C(T)` is **irreducible over `F_29`** — its roots lie in `F_{29^2}\F_29`. But every divisor of `X^7-1` splits completely over `F_29` (since `mu_7 ⊂ F_29`), so its irreducible factors are all linear. Therefore

```text
Q_theta  does NOT divide X^7-1,  and is incompatible with every divisor of X^7-1
(its recurrence "locations" are not 7th roots of unity — not even in F_29).
```

This **falsifies the implication as stated** (and any reading where "compatible with a divisor" means the recurrence locations lie in `mu_n`). Meanwhile the *true* locator of the witness, `(X-1)(X-16)(X-24)`, has all roots in `mu_7` and **does** divide `X^7-1`. The window's BM denominator is a truncation artifact, unrelated to the true locator.

---

## 2. Why it fails, and the corrected statement (BANKABLE)

The failure is a Berlekamp–Massey under-determination, stated exactly:

```text
BM/Padé recovers the minimal recurrence of a sequence of true linear complexity L
ONLY from >= 2L consecutive terms.
```

For an active `theta`, the window `(theta^j - P_j)_{j=1}^{sigma+1} = (p_j(S'))_{j=1}^{sigma+1}` is a truncation of the power-sum sequence of `S'`, whose true linear complexity is `|S'| = m` (distinct nonzero locations, unit amplitudes). We observe only `sigma+1` terms, and in the live regime

```text
sigma+1  ≈  n/log n     while     2m = 2(n-s) = 2((1-rho)n - sigma)  =  Theta(n),
so  sigma+1  ≪  2m.
```

The window is far too short to determine the degree-`m` denominator; BM returns a shorter "Padé under-approximant" (degree `≈ (sigma+1)/2`), generically irreducible and with no divisibility relation to `X^n-1`.

> **Corrected Padé lemma (the only true divisor statement).** If `theta` is active with witness `S'`, then the **full** power-sum sequence `(p_j(S'))_{j≥1}` has connection polynomial `g_{S'}(t)=∏_{x∈S'}(1-xt)`, which divides `1 - t^n` (equivalently the locator `∏_{x∈S'}(X-x) | X^n-1`). This requires the **entire** locator; it is **not** extractable from the length-`(sigma+1)` window and yields **no** usable constraint on `theta` beyond the activity definition itself.

Consequence: any attack that tries to certify activity by "short-window Padé denominator divides `X^n-1`" is dead. The needed window length is `≥ 2m = Theta(n)`, which we never have.

---

## 3. Exact reformulation that does advance the wall (BANKABLE)

Multiply the banked reciprocal-line condition `g_{S'} ≡ (1-θX)W (mod X^{σ+2})` by `Ũ = W^{-1} mod X^{σ+2}` (valid since `Ũ(0)=1`):

```text
theta active with witness S'
   <=>   g_{S'}(X) · Ũ(X)  ≡  1 - theta·X   (mod X^{sigma+2}).
```

Write `Phi_{S'} := g_{S'}·Ũ mod X^{σ+2} = sum_{i=0}^{sigma+1} phi_i(S') X^i`. Reading coefficients:

```text
phi_0 = 1                         (automatic)
phi_i(S') = 0     for i = 2,...,sigma+1     (sigma conditions, INDEPENDENT of theta)
theta = -phi_1(S') = e_1(S') - Ũ_1 = p_1(S') - Ũ_1   (theta is a LINEAR readout of S')
```

So `theta` enters in exactly one coordinate, linearly, and is **forced** by `S'`. Therefore, exactly:

> **Lemma (Ũ-flatness + linear readout).**
> ```text
> |Theta_U| = #{ distinct e_1(S') : S' ⊆ mu_n, |S'| = m,
>                phi_i(S') = [X^i](g_{S'}·Ũ) = 0  for i = 2,...,sigma+1 }.
> ```
> Equivalently, with `V := { S' : S' is "Ũ-flat to order sigma+1" }` (the σ θ-free vanishing conditions), `|Theta_U| = |e_1(V)|`, the size of the image of the linear statistic `e_1(S')=∑_{x∈S'}x` on `V`.

This is the precise reason min-distance/packing cannot work (Cycle 101's cut), now made structural: min-distance bounds `|V|`; the prize numerator is `|e_1(V)|`. A proof must show `e_1` has small image on the θ-free variety `V`, not that `V` is small.

It also pins the threshold consistency: `E|V| ≈ C(n,m)·p^{-σ} = main`, and `main ≤ 1` for `σ ≥ n/log_2 p`. So above corrected reserve the *expected* `|V|` is `≤ 1`; the wall is whether a special aperiodic `Ũ` forces an algebraic coincidence inflating `|e_1(V)|` to superpolynomial.

---

## 4. EXACT_NEW_WALL — the e_1-image / shifted-moment uncertainty bound

```text
L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY
```

> Let `Ũ ∈ F_p[X]`, `Ũ(0)=1`, aperiodic (not a polynomial in `X^d` for any `d|n, d<n`),
> `sigma ≥ C·n/log n`. Let
> ```text
> V = { S' ⊆ mu_n : |S'|=m,  [X^i](g_{S'}·Ũ)=0  for i=2,...,sigma+1 }.
> ```
> Prove `|e_1(V)| ≤ n^{O(1)}`, or construct a source-valid aperiodic `Ũ` with `|e_1(V)|` superpolynomial.

Exact uncertainty form of the same wall (finite-field support + Fourier-window hypothesis stated precisely): for a `0/1` indicator `c` on `mu_n` of weight `m`, the σ conditions are vanishing of the *twisted* high-frequency coefficients `[X^i](g_{S'}·Ũ)`, `i=2..σ+1` (convolution of the indicator's reciprocal-locator coefficients against the fixed window `Ũ`). The missing analytic input is:

> **Needed uncertainty lemma.** A weight-`m` `0/1` indicator on `mu_n` whose first `sigma ≈ n/log n` twisted moments `[X^i](g_{S'}·Ũ)` vanish (`i=2..σ+1`) can realize at most `n^{O(1)}` distinct mean values `e_1(S')`, unless `Ũ`/the indicator is quotient-periodic (already charged).

What converts this to PROOF or COUNTERPACKET:

- **PROOF** would follow from a quantitative bound that σ θ-free vanishing twisted-moment conditions confine the linear statistic `e_1` of a weight-`m` `0/1` vector to an `n^{O(1)}`-size set (an additive/uncertainty statement, **not** a dimension or min-distance statement). A regular-sequence/Bézout bound on `V` is **insufficient** — it bounds `|V|`, not `|e_1(V)|`, and `V` is a `0/1` solution set, not a positive-dimensional variety.
- **COUNTERPACKET** would be a source-valid aperiodic `Ũ` (above corrected reserve) where the σ flatness conditions are algebraically degenerate so that `e_1` sweeps superpolynomially many values on `V`. By §2 this can **no longer** be sought via the dead Padé lane.

Concrete next checker (decisive, small): for primes `p` with `n=(p-1)/r` and growing `σ`, enumerate `V` and measure `|V|`, `|e_1(V)|`, and `|e_1(V)|/|V|` for adversarial aperiodic `Ũ`. Counterpacket trigger: `|e_1(V)|` growing super-polynomially in `n` across a reproducible aperiodic family above reserve.

---

## Self-audit (the six required questions)

**1. What exact implication did I prove / not prove?**
Proved (by explicit `F_29` falsifier): "`theta` active ⟹ short-window Padé/BM denominator `Q_theta` divides / is compatible with a divisor of `X^n-1`" is **FALSE** — `Q_theta = T^2-24T+1` is irreducible over `F_29`, `∤ X^7-1`, while `theta=2` is genuinely active. Proved (corrected): the *full* locator `∏_{x∈S'}(X-x) | X^n-1`, but it is not window-accessible (need `≥2m` terms; have `σ+1≪2m`). Proved (exact reformulation): `|Theta_U| = |e_1(V)|` with `V` the θ-free Ũ-flat variety. **Not** proved: `|Theta_U| ≤ n^{O(1)}`; no superpolynomial counterpacket to `L2`.

**2. Official-prize-relevant, or only model/research?** Only a **research/model certificate**. The falsifier (`p=29, n=7`) kills a proof *lane*; it is not an MCA failure row, touches no `2^-128` target, and merges no field ledger. The `e_1`-reformulation is a research lemma toward the upper-side wall, not itself a prize theorem.

**3. First line where the theorem could fail (in the surviving route).** At the new wall `L-CYCLE103`: the step "σ θ-free flatness conditions ⟹ `|e_1(V)| ≤ n^{O(1)}`." This is exactly where an adversarial aperiodic `Ũ` could force algebraic coincidences. Nothing earlier is conjectural — §1–§3 are exact identities/finite computations.

**4. Are `q_gen, q_line, q_code, q_chal, 2^-128` used correctly?** They are **not invoked**; correctly so. This cycle works entirely inside the single field `F_p` (here `q_gen=p`), on the upper-side incidence numerator `|Theta_U|`. I did not merge ledgers and did not assert any `2^-128` threshold crossing — consistent with the constraint that this is upper-side structure, not a counterpacket row.

**5. Could quotient/periodic, contained incidences, same-slope collisions, or affine color normalization reduce the numerator?** In the falsifier, `n=7` is prime ⟹ no proper subgroup ⟹ no quotient-periodic reduction applies; the instance is genuinely aperiodic, so the Padé implication fails on the aperiodic core, not a chargeable branch. For the wall itself: yes — quotient-periodic `Ũ` is separated and charged (Cycle 99/101); the `e_1`-readout is the affine-normalized invariant (`theta` defined up to the additive constant `Ũ_1`), and `|Theta_U|` already counts **distinct** support, not the weighted `N`. The collapse of many `S'` to one `θ` (large fiber) is allowed and helps; the danger is the opposite (many distinct `e_1`).

**6. If PLAN, what converts it to PROOF/COUNTERPACKET?** The surviving content is part lemma (§1–3, definite) and part PLAN (§4). To convert §4: PROOF = the stated shifted-moment uncertainty bound `|e_1(V)| ≤ n^{O(1)}` (an additive-combinatorial statement, explicitly **not** min-distance and **not** Bézout on `|V|`); COUNTERPACKET = a source-valid aperiodic `Ũ` above reserve with `|e_1(V)|` superpolynomial, found by the enumeration checker described, **not** via the now-dead Padé route.