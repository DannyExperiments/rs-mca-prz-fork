# ROLE 07: EXTERNAL CENSUS CERTIFICATE

Your role is certificate engineer.

Assume we can run on a stronger external machine. Specify the exact reproducible
certificate pipeline for:

```text
max_v m(v) <= 12
```

or for finding a 13-fold packet.

Requirements:

1. exact finite field model for `F_{17^16}`;
2. deterministic generation of all 48 states per slot;
3. deterministic generation of `L_img` and `R_img`;
4. threshold counter up to 13;
5. certificate format for PASS:
   - shard summaries;
   - max count;
   - hashes;
   - independent replay recipe.
6. certificate format for FAIL:
   - explicit 13 representations;
   - full raw slot choices;
   - field products;
   - color sums.

Prefer designs that can run with 64-128GB RAM or under 1TB scratch. Be ruthless
about false negatives: none are allowed.

