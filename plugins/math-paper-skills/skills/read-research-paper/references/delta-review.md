# Delta regression review

Use delta mode only after a bounded accepted repair. Receive, in document
order:

- base and changed revision identifiers;
- the complete list of repair-cluster identifiers the packet claims to cover;
- each changed region with enough preceding and following context;
- the cold-reader success criterion for each repair cluster; and
- explicit non-scope, without the diagnosis, preferred wording, or expected
  answer.

For each cluster report what the passage now communicates; whether the
criterion passes, fails, or is untestable; what reconstruction remains; and
whether the edit introduced ambiguity, process leakage, over-definition,
displaced motivation, boilerplate, conflict, or out-of-scope change. Do not
rewrite the passage. A brief repair direction is allowed only to explain a
failure and must remain separate from the evidence.

End with the exact set of cluster identifiers actually checked and the literal
line `Delta verdict: PASS`, `Delta verdict: FAIL`, or `Delta verdict:
UNTESTABLE`. `PASS` means only that every listed cluster passed its supplied
criterion in the material read. It says nothing about omitted findings,
unchanged text, or a prior whole-paper verdict.

If the packet changes the paper promise, structural front matter, section
order, or reading path, report that delta mode is insufficient and a new
continuous read is required.

Apply the shared [proof-detail policy](../../write-research-paper/references/owner-proof-decisions.md)
to any neutral contract issued for the supplied regions. The private owner
registry remains withheld. An approved omission is not itself a failed repair;
report concrete new issues beyond its scope separately.
