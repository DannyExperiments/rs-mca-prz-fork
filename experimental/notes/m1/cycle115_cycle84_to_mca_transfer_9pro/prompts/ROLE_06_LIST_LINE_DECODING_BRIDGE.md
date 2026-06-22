# Role 06: List / Line-Decoding Bridge

Use the common prompt. No Internet.

Your role is to decide whether Cycle84's finite certificate transfers more cleanly through line-decoding or list-decoding than through raw MCA.

Use `context/notes_m2/m2_line_decoding_mca_bridge.md`, `snarks_v4.tex`, `proximity_blueprint_v3.tex`, and the source definitions. Your task is to produce a clean theorem or route cut of the form:

```text
Cycle84 finite slope/product occupancy
  -> support-wise line-decoding numerator a_LD
  -> MCA numerator or protocol-facing line-decoding failure
```

Questions to answer:

- What exact line-decoding definition is being used?
- Is the Cycle84 support-wise bad-slope set identical to a line-decoding obstruction set?
- Does line-decoding avoid any support-wise MCA bookkeeping, or does it require the same noncontainment data?
- What are the exact `(delta, a_LD, b)` parameters?
- Does the denominator use `q_line`, `q_code`, or `q_chal`?
- Can line-decoding make the Cycle88/89 two-copy row paper-facing even if the MCA phrasing is awkward?
- Is there a list-decoding implication, or would using list-decoding here be a category error?

If you prove a bridge, state the theorem in a form usable in a paper. If not, state the exact missing conversion theorem.
