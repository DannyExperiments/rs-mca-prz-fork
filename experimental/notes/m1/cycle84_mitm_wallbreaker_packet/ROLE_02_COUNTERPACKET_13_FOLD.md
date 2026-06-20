# ROLE 02: 13-FOLD COUNTERPACKET HUNTER

Your role is counterpacket hunter.

Try to find an explicit `v` with:

```text
m(v) >= 13.
```

This means producing 13 distinct compatible left/right representations:

```text
l_i in L_img,
r_i in R_img,
l_i * r_i = v,
colorL(l_i) + colorR(r_i) = 4 mod 16.
```

The packet must include enough raw symbolic or finite-field data for a later
checker to verify it. If you cannot enumerate actual field elements, give the
exact search constraints, pruning rules, and a minimal deterministic checker.

Focus on structured collision mechanisms:

- tau-paired packets;
- ratio cliques;
- common normalized product ratios;
- hidden subgroup/coset effects;
- near-equality among product slots;
- any defect not excluded by 4-slot injectivity.

If no packet is found, return the sharpest obstruction you discovered.

