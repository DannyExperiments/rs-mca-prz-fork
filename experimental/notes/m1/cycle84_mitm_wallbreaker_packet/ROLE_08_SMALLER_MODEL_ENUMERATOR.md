# ROLE 08: SMALLER MODEL ENUMERATOR AND SANITY TEST

Your role is finite-model tester.

Build a smaller analog of the Cycle84 seven-slot product/color problem over
small fields or smaller roots of unity. The goal is not proof by analogy. The
goal is to discover whether `m_max<=12` is structurally plausible or whether
13-fold packets are common once parameters are scaled down.

Deliverables:

1. define a family of small surrogate models preserving:
   - seven slots;
   - color constraint;
   - product equality;
   - left/right MITM split;
   - tau-like symmetry if possible.
2. give executable pseudocode or code;
3. state observed or predicted `m_max`;
4. explain whether failures lift to the real model.

If you find a small 13-fold pattern, translate it into a candidate search
template for the real `F_{17^16}` model.

