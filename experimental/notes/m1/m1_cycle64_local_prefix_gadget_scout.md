# Cycle 64 Local Prefix-Gadget Scout Note

## Status

`AUDIT / PLAN / LOCAL_REDUCTION`.

This is Codex's bounded local follow-up while the Cycle 64 Fable run is
active. It is not a proof. It records the immediate structural reading of the
Cycle 63 Role 05 counterpacket.

## Point

The Role 05 characteristic-17 packet is not a random residual. It is already a
clean product-color coefficient of a finite prefix-collision class.

Role 05 constructs 48 local states `A_{i,a}` in `mu_16` with

```text
E_A(w) == 1 mod w^3
```

and product-color exponents lying in

```text
S = {1,4,7,9,12,15} mod 16,
```

with multiplicity `8` per color.

After quadratic lifting into a 32-element block `K`, each lifted local state
has

```text
E_{\tilde A}(z) == 1 mod z^6
```

and the same product color. Thus the 48 states form one local
`sigma=6` prefix-collision gadget class with group-ring enumerator

```text
W(Y) = 8 * (Y^1 + Y^4 + Y^7 + Y^9 + Y^12 + Y^15)
       in Z[Z/16Z].
```

The seven oriented `K`-cosets used in Role 05 contribute the coefficient

```text
[Y^4] W(Y)^7
= 8^7 * c_7(4)
= 52,747,567,104.
```

The marker `{1}` supplies the fixed linear jet

```text
E_{\{1\}}(z) == 1 - z mod z^6,
```

so the total target becomes

```text
(prod T, e_1(T),...,e_5(T)) = (1,1,0,0,0,0).
```

## Consequence

Role 05 kills only the *small residual after full-block trades* theorem. It
does not by itself kill a prefix-gadget charge theorem, because the packet is
exactly chargeable by the local enumerator above.

The next question is quantitative and frontier-facing:

```text
Does the sum of all canonical prefix-gadget charges remain below the finite
target at the first safe reserve, after banked lower packets and quotient
packets are registered?
```

This is why Cycle 64 should not merely ask for a qualitative partition. It
must ask for:

1. exact canonical assignment to local prefix classes;
2. exact product-color group-ring charge;
3. bounded overlap across subgroup scales;
4. a finite-checker interface for total charge.

## Local Candidate Definition

For subgroup `J <= H`, a coset `C=cJ`, and subsets `A,B subset C`, define

```text
A ~_{sigma,J,C} B
iff |A|=|B| and
prod_{x in A}(1-xz) == prod_{x in B}(1-xz) mod z^sigma.
```

The class charge is not just the class size. It is the group-ring polynomial

```text
W_C = sum_{A in class} Y^{log(prod A)}
```

in the quotient product-color group naturally visible after normalizing by a
base representative. Full `K`-blocks are the degenerate class whose prefix is
`1 mod z^sigma` and whose product color is `c^M`.

## Immediate Risk

The prefix-gadget formalism may absorb Role 05 but still be too large for the
prize frontier. Therefore the next serious deliverable after Cycle 64 should
be an `RS-PRIZE-FRONTIER-V1` registry run with:

- banked lower/failure terms;
- quotient/projective equality/Lattes terms;
- scalar apolar block charges;
- prefix-gadget residual charges, at least in the model `Delta=[0]+sigma infinity`.

If the checker says the model charge already exceeds the target at the first
candidate reserve, the route must switch from broad upper theorem to finite
frontier obstruction accounting.

## Next Prompt If Cycle 64 Returns Only An Exact Wall

Target:

```text
L-MODEL-GJ-PREFIX-GADGET-FRONTIER-CHARGE-CHECKER
```

Ask for an implementation-ready finite registry term:

```text
Charge(H,sigma,j,b)
= sum over canonical prefix-gadget decompositions of
  coefficient of target product color in product of W_C.
```

with all multiplicities and subgroup-scale overlaps explicit.
