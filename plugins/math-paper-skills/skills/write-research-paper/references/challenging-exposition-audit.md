# Challenging exposition audit

Use this audit emphasis when the owner asks for a challenging or adversarial
exposition audit, or when an authorized exposition review finds a concrete
quantifier or dependency ambiguity. It supplements the existing review route,
not its authority: direct review stays in one context, and independent review
still requires explicit delegation. It is not a fourth isolated-reader mode
and does not turn an exposition review into proof certification.

Prioritize hidden mathematical structure over vocabulary replacement. Apply
the rules in [author-style.md](author-style.md), especially quantification,
local dependencies, self-contained operators, and display roles:

- In each proof, locate the entry of any negated assumption and check that a
  contradiction argument announces that assumption explicitly. Do not classify
  proof methods by searching for the word `contradiction` alone.
- Identify where each symbol is bound and its domain, including indices,
  points, functions, measures, representatives, and function arguments.
- Track which parameters vary, which are fixed, and which a construction may
  depend on. Look for disappearing variables and changes of quantifier order
  or uniformity hidden by a combined sentence or display.
- Locate the actual identity or estimate that carries each inference, including
  kernel equalities, convergence, inequalities, and nondegeneracy. Distinguish
  an explicitly referenced formula from a vague assertion that one exists.
- Inspect integral variables/measures and sup/inf domains and admissibility
  conditions. For each display, also track dependent map codomains and the
  original versus ambient pushforward measures. Keep infimum and attained minimum distinct.
- Distinguish sequences, indexed representative choices, and equivalence
  classes; assess typefaces by the mathematical role of their objects.

For a candidate finding, identify the exact location, hidden binding or logical
step, concrete ambiguity or reader burden, and the smallest adequate repair.
State uncertainty rather than inventing the intended mathematics. A suspected
mathematical gap is routed under the host's proof-audit policy; an isolated
exposition reader reports the suspicion without investigating proofs or sources
outside its permitted inputs. Do not manufacture findings to meet a quota.

Recheck candidate findings against the current source after revisions; an old
audit is a locator, not evidence that the defect remains. Explicitly exclude
resolved findings and applicable author-accepted expressions from active defects,
unless current evidence identifies a new issue outside the accepted scope.

Preserve these nondefects:

- A direct application of an identified cited result needs no invented formula
  or reproduction of the source proof. If its applicability is not explicit,
  flag that particular missing hypothesis or interface instead of demanding a
  full new proof. This exception is not automatic source verification.
- Absence of a multiline formula is not a defect: seek the formula or clear
  citation carrying the inference, not a minimum formula count.
- One coherent estimate chain or derivation can remain a multiline display.
  Split only independently functioning assertions; do not split by line count.
- An applicable author-approved omission or brief proof remains accepted under
  [owner-proof-decisions.md](owner-proof-decisions.md). Reopening needs a concrete
  new issue outside that approval. Independent readers use only the permitted
  neutral contract, never the private decision registry.
- A symbol's visual appearance alone is not grounds for changing its font.
  Rendering checks belong to authorized typesetting work; an isolated reader
  does not compile a manuscript merely to inspect a glyph.

Keep the selected route's report and verdict format. These are candidate-finding
priorities and judgment criteria, not mechanical string replacements, a count
of required formulas, or an automatic request for more proof detail.
