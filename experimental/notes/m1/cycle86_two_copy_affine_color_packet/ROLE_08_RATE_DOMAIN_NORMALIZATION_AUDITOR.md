# ROLE 08: Rate And Domain Normalization Auditor

You are a fresh normalization auditor.

Cycle85 produced conflicting normalization proposals. Resolve them.

One-copy proposals:

```text
add 18 fixed points -> (n,k)=(274,137)
remove 18 unused points -> (n,k)=(238,119)
marker constraints -> (n,k)=(256,128)
```

Two-copy proposals:

```text
(n,k,sigma,j)=(560,280,6,274)
(n,k,sigma,j)=(476,238,12,226)
(n,k,sigma,j)=(512,256,12,244)
```

Your job:

1. Check each proposal against `j=n-k-sigma`.
2. Check support sizes and whether fixed padding/removal preserves all
   witnesses.
3. Check whether the resulting code is RS/GRS over one domain.
4. Check official rate.
5. Identify the simplest valid package for the two-copy theorem.
6. If none are valid, give a concrete counterexample to the normalization.

Return a table and then a verdict. This role should be arithmetic- and
definition-heavy, not speculative.
