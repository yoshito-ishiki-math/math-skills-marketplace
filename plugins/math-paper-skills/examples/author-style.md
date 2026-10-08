# Example author-style profile

This is an **optional example**, adapted from a working author's concrete style
preferences with identifying details, project-specific references, and private
source evidence removed. It is not a universal standard for mathematical
English and is not activated by installing the skills. Rules such as avoiding
`give`, restricting `suppose`, or preferring particular punctuation are choices
of this profile, not claims that other styles are incorrect.

## Adopt and customize

Copy the portions you want into one private shared author profile, and explicitly
designate it through your host project's style configuration. Adjust internal
links if you copy this file outside the repository. Keep manuscript-specific
exceptions in that manuscript's local style file. Do not edit the shared public
example merely to configure a private project.

Read the adopted profile in full when directed to it by the writing workflow.
For independent review, include only the permitted frozen style contract, not
private source material or writer records. Mathematical correctness and exact
scope come first. Current explicit author instructions override preferences;
mandatory venue requirements take precedence where necessary. Selecting this
example never authorizes editing, delegation, or publication by itself.

The formulas and TeX snippets below are generic illustrations, not quotations
from research manuscripts. Commands such as `\Z` in examples assume an
appropriate local macro or package; these snippets are not a complete preamble.
No names, affiliations, contact details, local source paths, paper identifiers,
corpus excerpts, or individual proof-decision records are included. Public
hosting still associates the example with its publisher's account.

## Concrete preferences in this example

### Prose and proof language

- Do not use `:` or `;` in running prose. This restriction does not apply to
  TeX syntax, labels, metadata, displayed formulas, or structural proof labels
  whose punctuation has a technical function.
- Do not coin a new hyphenated word unless that word occurs in the cited
  references or relevant prior literature.
- Do not use the word `give` in manuscript prose.
- Use `suppose` only to introduce an assumption made for a proof by
  contradiction.
- Signal a proof by contradiction explicitly with wording such as `For the
  sake of contradiction, suppose that ...`. Audit the actual entry of the
  negated assumption, not merely the occurrence of the word `contradiction`.
- In every theorem-like statement, make the boundary between the hypotheses
  and the conclusion grammatically explicit. Prefer a construction such as
  `If ..., then ...` when the statement introduces its hypotheses directly.
- When the hypotheses occupy a preceding sentence, introduce the conclusion
  with `Then` or another unmistakable transition. Do not separate hypotheses
  from the conclusion only by a comma or leave the boundary implicit.
- When proving an equality of sets $A=B$ by double inclusion, normally argue
  elementwise in both directions. For $A\subseteq B$, take $x\in A$ and prove
  $x\in B$. For $B\subseteq A$, take $x\in B$ and prove $x\in A$. Name the two
  sets explicitly by their actual mathematical symbols rather than referring
  only to `the first set`, `the other set`, or similar phrases.
- Apply this template only when the proof uses the elementwise double-inclusion
  method. Do not force it onto a proof that establishes the set equality by a
  different appropriate argument.

- For a single map-defining formula, prefer `Define the map ... by ...`.
  `As follows` is acceptable for cases or multiple defining formulas; apply
  explicit paper-local permissions before treating this preference as a defect.

### Authorial voice and explicit exposition

Preserve the author's vocabulary and style. Consult the adopted profile and any reference material explicitly designated
for the current task. Retain author-originated
wording whenever its mathematical meaning, grammar, and clarity are sound.
Before changing it, identify the concrete reason, such as an ambiguous
referent, an omitted inference, or unsuitable terminology.

1. State a mathematical claim in the corresponding notation whenever it
   supports the argument. When an image, kernel, eigenspace, density statement,
   dimension, or convergence assertion is load-bearing, write the equality,
   inclusion, quantifiers, limit, or estimate actually needed. For example,
   express density by the relevant closure equality and identify an image by
   an equality of subspaces. Use prose to explain why the formula is stated and
   how it leads to the next inference. In proofs of convergence, continuity,
   boundedness, compactness, separation, or approximation, display the decisive
   identity or estimate when the argument depends on one. Treat prose-only
   transitions such as `by continuity` or `by compactness` as review targets
   when that formula is absent. This is a check for a missing inference, not a
   requirement to insert decorative formulas into a qualitative proof.
   Show a load-bearing kernel identity, inequality, convergence statement, or
   nondegeneracy condition in a display or by an exact formula reference.
   A proof consisting solely of direct application of a cited result need not
   acquire an artificial calculation; identify the result and make its
   applicability explicit. This exception does not cover an unstated reduction
   or an additional argument beyond the cited result.
   When equality of operators needs justification, take an element of the
   relevant subspace and display both operator values rather than only saying
   that they agree on each summand. For a direct-sum argument, distinguish
   equality on each component, equality on finite sums by linearity, and
   extension to the full space by boundedness and density. Verify the needed
   hypotheses rather than treating those steps as interchangeable.

2. Identify referents locally. Attach the relevant notation to phrases such as
   `the bases`, `their ranges`, `this kernel`, and `the normalizing matrices`.
   When discussing a basis, specify as needed the space, index range, and inner
   product with respect to which it is orthonormal. Do not leave a summary such
   as `the rank assertion` in place of the corresponding dimension equality or
   precise proposition. More generally, write forms such as `the space $X$`,
   `the map $f$`, and `the family $\mathcal{F}$` whenever reasonably possible.
   In spectral arguments, name the spectra with their operators, the eigenvalue
   selection conditions, intersections with the contour, and projection images.
   Do not leave these as `either spectrum`, `the selected eigenvalues`, or
   `this range`. Explain how the listed conditions support the subsequent
   contour integral or direct-sum decomposition.

3. In a difficult proof, state the goal of each stage before its calculation.
   Identify the object to be constructed or the property to be proved, then
   supply the calculation and justification, and finally connect the result to
   the next stage. Consider extracting a coherent part as a lemma when it has
   its own hypotheses and conclusion and is used later.
   In particular, inspect explanatory text following definitions for an
   independently reusable fact. Consider extracting it as a numbered lemma
   with its own hypotheses and conclusion. Cite the source for a borrowed
   result without expanding its proof unnecessarily.
   Inspect displays immediately followed by `\end{proof}`. When the conclusion
   needs to be connected to the display, add a short, specific closing sentence,
   such as `This proves the uniform cardinality bound.` Do not insert
   `This finishes the proof.` mechanically or expand an already explicit ending.

4. In arguments involving integration, convergence, or continuity, identify
   the variables and spaces explicitly. Distinguish the integration variable,
   fixed variables, domain of integration, and measure. When an operator acts
   on a function, include a pointwise formula when useful. Justify exchanges of
   integrals and operators and limiting operations, and show the intermediate
   formula that makes the justification visible. Specify the norm or topology
   of convergence, the set on which uniformity is asserted, and the parameters
   varying simultaneously. When using `joint continuity`, display the map on
   the relevant product space. Make displays involving integration, suprema,
   or infima self-contained: include the integration variable and measure,
   function arguments, and the space and admissibility conditions over which
   the supremum or infimum is taken. Bind parameters before the display as well;
   an operator subscript is not a substitute for introducing its ambient space.
   Track a measure on its original space separately from its pushforward into
   an ambient space. At every integral, check the domain, measure, and integration
   variable together; write the pushforward relationship when changing spaces.

5. Place prerequisites where the argument uses them. In a long paper,
   distinguish preliminaries shared by the whole paper from preliminaries local
   to a part or section. Before applying a known theorem, state the hypotheses
   and conclusion needed here and give the source. Choose the level of detail
   by whether the intended reader can follow the proof.
   Distinguish unpacking a theorem's terminology from deriving a consequence.
   Use `Namely, ...` for a restatement according to the definitions; use
   `By Theorem ..., ...` for an additional inference and show that inference.
   Do not leave a concrete assertion following a theorem ambiguous between
   these roles. When changing a connective, revise the preceding and following
   sentences as one explanation. For example, adopting `Namely, if ...` calls
   for checking whether `the following extension property` has become redundant;
   replacing just the requested phrase is not enough.

6. Check notation for role and visual distinguishability, not only literal
   duplication. Avoid visually similar symbols for different objects in the
   same argument. Use consistent typefaces for related objects and visibly
   distinct notation for different roles. Name macros after mathematical
   meaning or role, and preserve notation approved by the owner. Use calligraphic
   notation for sets, families, classes, or structures; use ordinary Greek
   letters for scalar errors, distances, and displacements. Do not change
   `\delta` to calligraphic notation merely for appearance. If a calligraphic
   Greek form such as `\mathcal{\delta}` is deliberately considered, check the
   rendered glyph with the actual typesetting setup rather than assuming the
   command produces an appropriate alphabet. This is a rule about semantic
   roles, not about any particular lemma's symbol.

7. Consider a diagram where it materially clarifies a construction, the
   relation among maps, or the role of several factors. Do not add a diagram
   without a concrete explanatory benefit. Keep its notation consistent with
   the text and make every arrow's source, target, and meaning clear. Place the
   diagram immediately after or near the corresponding explanation. If the
   owner fixes its position, preserve its order relative to the text.

### Quantification, dependencies, and mathematical objects

1. Bind every symbol before its first mathematical use. In particular,
   bind indices, points, functions, measures, representatives, correspondences,
   group elements, sequences, time parameters, and ranks before displaying a
   formula that uses them. State the domain or
   index range and make the order of dependent quantifiers explicit. Do not
   leave the binding to a trailing `for every` after the display or leave a
   domain or index range to be supplied by a later formula.
   Do not combine formulas with different variable dependencies under a single
   blanket quantifier sentence. Immediately before each formula or coherent
   group, quantify only its actual varying parameters; distinguish them from
   already fixed objects. Preserve quantifier order and uniformity when
   separating statements, including parameters on which a chosen object must
   not depend.
   Do not silently extend a sentence-local quantifier into the next sentence
   or display. Rebind the genuinely varying variables immediately before the
   display, distinguishing them from objects explicitly fixed for the argument.
   For maps with dependent domains or codomains, such as
   $f_X:A_X\to B_X$, quantify a map for each admissible $X$
   and state its source and target. Calling this merely a family indexed by
   all $X$ does not specify the dependent mapping types.

2. When a theorem constructs several interdependent objects, state their
   existence simultaneously and make their dependencies visible. For example,
   specify the space, maps, error function, and homotopy as one package when
   their required properties link them. Avoid introducing part of that package
   later with `There also exists` or `We can choose`. The proof may construct
   the objects in stages while preserving the stated dependencies.

3. Distinguish an equivalence class from a chosen representative. Do not write
   a class-valued output as if it were a concrete metric space. Choose and name
   a representative before using pointwise formulas, and state when the choice
   depends on a sequence or an isometry. State the sequence first, then define
   its indexed representative family or selection map, specifying which class
   each representative belongs to and the index set. “Choose representatives”
   alone does not define that family.

4. When `representative` refers both to a representative of an isometry class
   and to a representative of a coordinate class, use different names for the
   two choices and identify the class represented by each.

5. Do not compress logically independent equalities or inequalities into one
   unlabeled display when they play different roles in the proof. Split them
   into separately labeled formulas or visibly separated aligned lines. Give
   each formula used in a later inference an exact reference as required below.
   Keep a single estimate chain or coherent derivation in one display. The
   number of lines is not a splitting criterion; distinct logical roles are.

6. Do not silently introduce a stronger hypothesis halfway through a theorem
   or lemma. State the new hypothesis with an explicit `If ...` clause that
   identifies which conclusion requires it, or split the result into separate
   statements. Preserve the scope of conclusions proved under weaker hypotheses.

7. When a vector, function, measure, or map is derived from another object,
   define the two objects separately and state their relationship explicitly.
   For example, distinguish a minimizing coefficient vector from the best
   approximation function constructed from it.

8. When the ambient space, metric, or correspondence has changed, replace
   `the same formula`, `the same relation`, or `the same properties` by the
   explicit formula or the name of the induced object with its defining
   relationship. Make clear how the construction applies in the new setting.
   More generally, if `the corresponding identity`, `the same assertion`, or
   `the condition on the right` hides a load-bearing statement, repeat the
   formula, cite it exactly, or name its full mathematical content. A relative
   phrase is insufficient even when the ambient space has not changed.

9. Preserve the meaning of a defined invariant. If it is defined by an
   infimum, do not later call it a `minimum` or a `least value` unless attainment
   has been proved under the hypotheses in force.

### Acknowledgements and use of AI

- Unless the venue supplies an equivalent structure, define the following
  environments in the paper preamble:

```tex
\newenvironment{acknowledgements}{%
  \medskip\noindent\textit{Acknowledgements.}\ }{\par}
\newenvironment{useofai}{%
  \medskip\noindent\textbf{Use of AI.}\ }{\par}
```

- Place the `useofai` environment before the `acknowledgements` environment at
  the end of the introduction, after any Organization and Conventions and
  notation blocks, unless the venue requires another location.
- In `useofai`, identify the actual system by name and state its concrete uses,
  such as language editing, `\LaTeX{}` typesetting assistance, literature
  searches, or exploration of proof constructions. If the system contributed
  a mathematical construction or proof route, state that contribution
  explicitly rather than hiding it under general editing language.
- The intended closing statement records that the author verified the arguments,
  understands the proofs and constructions, and takes responsibility for the
  mathematical content and final manuscript. Include these factual assertions
  only when the author has actually confirmed them; otherwise leave the
  disclosure pending author confirmation. Mention a prior AI-assisted report
  only when it exists and its relationship to the manuscript is established.
  Do not invent a publication venue or version history.
- Use `acknowledgements` for concise funding, institutional, and personal
  acknowledgements. Record grant names and numbers exactly and do not infer
  support that the owner has not supplied.

### Bibliography and citations

- Unless the venue requires another bibliography system, use `biblatex` with
  Biber and the following baseline configuration:

```tex
\usepackage[
  backend=biber,
  style=numeric,
  doi=true,
  sorting=nyt,
  eprint=true,
  giveninits=true,
  maxnames=99
]{biblatex}
\addbibresource{bib/references.bib}
```

- Typeset journal article titles in italics and omit `In:` before journal names
  with:

```tex
\DeclareFieldFormat[article]{title}{\mkbibemph{#1}}
\renewbibmacro*{in:}{%
  \ifentrytype{article}
    {}
    {\printtext{\bibstring{in}\intitlepunct}}}
```

- Put bibliography data in `bib/references.bib`, cite entries with `\cite`, and
  place `\printbibliography` after the mathematical body and before
  `\end{document}`. Do not mix `biblatex` with `\bibliographystyle` or
  `\bibliography`.
- Configure `latexmk` to invoke Biber with `$bibtex = 'biber %O %B';` when the
  project uses a `.latexmkrc`.
- For journal articles, record `author`, `title`, `journaltitle`, `volume`, the
  applicable `number`, `pages`, or `eid`, `year`, and `doi` when available. For
  arXiv records, use `eprint`, `eprinttype = {arXiv}`, and `eprintclass`. For
  reports, record the actual `institution`, `type`, `version`, `date`, `doi`,
  `url`, and `urldate` when applicable. Preserve capitalization needed in
  titles with BibLaTeX braces.
- Do not invent missing bibliographic fields. Verify load-bearing citations
  and their exact locators under the host project's literature policy rather
  than treating a valid `.bib` entry as source verification.

### Hyperlinks and cross-references

- Unless a venue requires different settings, keep linked text black and use
  colored rectangular borders: red for
  internal references, green for citations, and cyan for URLs. Then load
  `cleveref` immediately after `hyperref`. Use the following explicit baseline,
  chosen for this example:

```tex
\usepackage[
  colorlinks=false,
  linkbordercolor={1 0 0},
  citebordercolor={0 1 0},
  urlbordercolor={0 1 1}
]{hyperref}
\usepackage[nameinlink,noabbrev]{cleveref}
```

- Preserve this loading order. The `nameinlink` option makes the reference name
  part of the hyperlink, and `noabbrev` keeps reference names unabbreviated.
- For every custom theorem-like environment used with `\Cref` or `\cref`,
  define both its singular and plural lowercase and uppercase names with
  `\crefname` and `\Crefname`. For example:

```tex
\crefname{theorem}{theorem}{theorems}
\Crefname{theorem}{Theorem}{Theorems}
```

- Do not refer to a formula only as `the preceding estimate`, `the above
  equality`, `the previous display`, or a similar relative phrase. If a
  formula is used in a later inference, give it an equation number and a
  descriptive label, and cite that exact formula with `\eqref{...}`. For
  example, write `By the estimate \eqref{eq:uniform-bound}, ...`. When using
  individual terms, identify their expressions or mathematical roles together
  with the exact equation reference; `the first term` or `the second term`
  alone is insufficient for a load-bearing inference.
- Do not add PDF metadata or further `\hypersetup` entries merely by habit.
  Add them only when the venue, host project, or owner calls for them.

### Notation and enumerated conditions

- Write the empty set as `\emptyset`. Do not use `\varnothing` or another
  alternative empty-set glyph.
- Write sequences primarily in the form `\{a_n\}_{n\in\Z_{\ge 0}}`.
- Use `\to` for map arrows.
- Do not chain equivalence symbols in one formula. In particular, never write
  `A\iff B\iff C` or another expression with two or more successive
  equivalence links. State the equivalences separately and give each needed
  justification separately.
- In set-builder notation, separate the object from its condition with a
  vertical bar typeset as `\mid`, not with a colon. For example, write
  `\{x\in X \mid P(x)\}`.
- When the braces in set-builder notation are enlarged, enlarge the middle
  vertical bar as well. For example, write
  `\left\{x\in X \,\middle|\, P(x)\right\}` rather than using an
  unscaled `\mid` between `\left\{` and `\right\}`.
- Avoid `'` and `\prime` whenever a clear notation without primes is
  available.
- Implement `enumerate` lists with `enumitem`. Specify both `label=...` and
  `ref=...`, and typeset both representations upright with `\textup`, including
  inside theorem environments. For example, use
  `[label=\textup{(A\arabic*)},ref=\textup{(A\arabic*)}]`.
- Use a content-specific alphabetic prefix of exactly one letter so that items
  have forms such as `(A1)` and `(A2)`. Do not use a multi-letter prefix. Use a
  different prefix for every `enumerate` environment in the manuscript,
  including lists in different sections.
- Add a `\label` to every item that is cited. Refer to it with `\ref` or
  `\Cref` instead of writing the item number manually.

### TeX source layout

- When restructuring a tagged paragraph into a separate lemma, retain its old
  paragraph ID on one resulting part and assign new IDs to the new parts.
  Update uses of the extracted result to its precise lemma label and check for
  obsolete broad section references. Manage IDs and mathematical references
  together; do not introduce paragraph IDs into an otherwise untagged manuscript
  solely because of this rule.

- In manuscript TeX source, write inline mathematics as `$...$` and displayed
  mathematics as `\[...\]`. Do not use `\(...\)` or `$$...$$` as alternative
  delimiters.
- In manuscript source, insert a line break after every period or comma outside
  a mathematical expression.
- Put each mathematical expression on its own source line without changing the
  rendered output.
- Keep punctuation immediately following a mathematical expression on the
  same line as that expression, then insert the line break after the
  punctuation.
- When a mathematical expression begins a hyphenated word, keep the expression
  and the complete hyphenated word on the same source line.
- Do not insert blank lines solely to implement these source-layout rules.
- Before breaking a long sum at `+`, check whether it fits on one line. If it
  does not, organize definitions or estimates according to the roles of the
  error terms; do not invent notation solely to solve a typesetting problem.
  Preserve coherent estimate chains and the paper's local display conventions.
- As an exception, keep the entire abstract body on one source line.
- Do not pursue aesthetically polished pagination or adjust the manuscript
  merely to improve page breaks. Let the document class and TeX determine the
  natural pagination.
- Do not add or move commands such as `\newpage`, `\pagebreak`, `\clearpage`,
  `\enlargethispage`, `\looseness`, or local spacing adjustments solely to
  avoid an awkward page ending, balance pages, or reposition a theorem. Use a
  manual page break only when the document structure or a venue rule requires
  it.

## Introduction and paragraph rhythm

The following are additional preferences in this example. No source papers,
corpus statistics, or claims about their frequency are distributed here.

- In the introduction, move directly from the relevant earlier results to a
  statement of the present paper's contribution. Wording such as `In the
  present paper` is appropriate when it makes that transition precise.
- Before a principal theorem, include one short orientation paragraph that
  explains why the formulation is useful.
- Introduce notation immediately before its first serious use.
- Write proofs in compact mathematical paragraphs. Use enumerated conditions
  only when the items will later be cited or compared.
- Prefer the direct authorial voice `we` and restrained transitions such as `We
  next prove` and `It remains to show`.

## Scope and local conventions

Keep notation tied to one paper or subject in that paper's local style file.
Do not transfer subject-specific macros or conventions into unrelated papers.
If private corpus evidence is used, treat observed usage as advisory rather
than a mandatory phrase list. Do not attach the corpus or quotations to this
public example.

## Paper-specific proof-detail decisions

Before requiring a fuller proof or another displayed estimate, apply the
paper's explicit author decisions under
[the proof-detail decision policy](../skills/write-research-paper/references/owner-proof-decisions.md). An applicable
approved omission or brief argument is part of the local detail budget and
must not be repeatedly treated as a defect. This exception is scoped to the
identified passage and does not certify mathematical correctness. Independent
readers receive only the permitted neutral contract, not the private registry.
