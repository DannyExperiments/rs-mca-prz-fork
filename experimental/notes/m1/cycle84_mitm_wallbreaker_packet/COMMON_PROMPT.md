# COMMON PROMPT FOR CYCLE 84

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

You are working on the RS-MCA / proximity-prize finite obstruction route. You
are not brainstorming from scratch. You are adjudicating and attacking the
specific finite wall left by Cycles 64-83.

Read the attached context first, especially:

```text
CYCLE84_CURRENT_STATE.md
m1_cycle83_mitm_mmax_threshold_audit.md
m1_cycle82_four_slot_or_mitm_mmax_audit.md
m1_cycle81_compiled_three_slot_certificate_audit.md
m1_cycle80_mindist_symmetric_energy_audit.md
m1_cycle79_common_ratio_bound_audit.md
m1_cycle78_exact_mmax_census_audit.md
m1_cycle77_ab_product_maxfiber_audit.md
m1_cycle76_right_half_mmax_audit.md
m1_cycle75_direct_mmax_fiber_audit.md
m1_cycle68_collision_multiplicity_audit.md
m1_cycle67_cross_color_injectivity_audit.md
m1_cycle66_sevenfold_product_occupancy_audit.md
```

## Current Target

The active target is:

```text
prove m_max(beta) <= 12
or find an explicit 13-fold colored packet.
```

In the MITM formulation:

```text
L_img = products on slots {1,2,3}, |L_img| = 48^3 = 110592.
R_img = products on slots {4,5,6,7}, |R_img| = 48^4 = 5308416.
```

For each field element `v`,

```text
m(v) = #{
  l in L_img :
  v*l^{-1} in R_img
  and colorL(l) + colorR(v*l^{-1}) = 4 mod 16
}.
```

The goal is:

```text
max_v m(v) <= 12.
```

or an explicit `v` with at least 13 compatible left/right representations.

## Known Banked Facts

Do not re-prove these unless your role asks you to audit them:

1. The Role 05 thickened-color route reduces to an explicit sevenfold product
   occupancy model over `F_{17^16}`.
2. The pure color shortcut is false.
3. The valid key is product-only unless color is proved forced by product.
4. Product injectivity has been locally certified for every 1-slot, 2-slot,
   3-slot, and 4-slot subset.
5. Therefore product-fiber minimum distance is at least 5.
6. Minimum distance 5 alone does not prove `m_max <= 12`.
7. The exact remaining target is color-filtered left/right MITM multiplicity.

## Output Rules

Start your answer with one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. executive verdict and confidence;
2. exact theorem/counterpacket/checker statement;
3. proof or construction;
4. verification requirements;
5. next exact lemma or construction.

Do not return broad strategy without an exact target. Do not claim prize-level
resolution. This is a finite-wall attack.

If you write code, it must be self-contained, deterministic, and accompanied by
the exact certificate it should emit. If you cannot run code, mark it `UNRUN`.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

