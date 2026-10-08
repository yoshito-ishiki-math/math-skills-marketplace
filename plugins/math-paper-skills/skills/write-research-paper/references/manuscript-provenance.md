# Manuscript provenance and protected revisions

Read the relevant sections when a manuscript uses research claim catalogs,
several source projects, a citation register, protected passages, or review
records. This guide supports authorized writing; it does not start a proof
audit, independent review, migration, or submission. Small edits need no new
ledger. Reuse the host's existing records and schema.

## Claim scope and imported manuscripts

Identify the current manuscript, the claim range it covers, and the date or
revision of the research records consulted. Compare with current definitions,
claims, and proof notes rather than relying on an old overview. Read enough of
the actual statements to check hypotheses, conventions, and dependencies.

Where the host uses a claim map, connect every load-bearing theorem label to
its primary claim. Keep introduction statements connected to their proofs in
the body and distinguish any new specialization from its source. A numbered
appendix covering many claims may require several evidence statuses; do not
apply one summary label to the whole range. A reconstructed short proof and a
summary of a longer proof establish different reading and checking scopes.

During an authorized manuscript merge, preserve originals and record where
each original result, section, and proof went. Retain stable manuscript and
claim identities. In a numbered host, use its permanent numbers without
renumbering or reusing withdrawn numbers. Keep source numbering in historical
records, with an explicit translation to current identities.

Mechanical correspondence is only one check. Inspect mathematical meaning
when one theorem has several source claims, one claim has several theorem
labels, or the manuscript proves a stronger result. An adapter must not turn
a derived result into a direct source match or an agent proof into an owner
check. Distinguish a genuine unsupported inference from correct but compressed
exposition; apply the paper's approved detail budget before expanding it.
Check relevant empty, degenerate, and boundary cases when a revision changes
the statement or the proof's case division.

## Source identity and attribution

For a load-bearing imported result, state the hypotheses and conclusion used
and keep an exact source locator. Distinguish the source theorem from the
consequence proved here and preserve a narrower application scope.

When citations or versions need reconciliation, maintain the existing source
register or a compact equivalent. Connect bibliography keys, current printed
reference numbers when useful, saved source files, exact versions, and checked
locators. Printed numbers may change after bibliography updates; citation keys
are the more durable identity. Distinguish printed page numbers from PDF page
indices and locators in a published version from those in an author preprint.

Record separately a source not obtained, a published version not obtained,
and a preprint used as a substitute. Say which statement or pages were actually
read; metadata checks are not content verification. Do not infer equivalence
between versions. Attribute a question, an answer, and a later paper to their
actual authors and roles instead of transferring authorship through a citation.

## Protected content and revision identity

Before a restricted edit, identify its actual locks: protected files, theorem
scope, key formulas, paragraph boundaries, author metadata, or a prescribed
display. Do not invent locks absent from the request. Compare protected files
byte for byte or by hashes before and after. For a protected formula whose
source whitespace may change, compare an explicit whitespace-normalized form
and inspect the content diff; normalization must not erase mathematical tokens.
Byte checks and formula checks answer different questions.

Retain deleted results and retired paragraph identities through existing
history or authorized archives. Mark a proof-detail decision superseded when
its passage is retired; do not apply it to another result because its number
looks similar. A numbered owner instruction must be matched to the exact
candidate list that the owner answered. A conditional omission applies only
after its condition, such as finding the matching cited result, is actually
verified. Keep the raw decision and its private provenance in the paper's own
registry under [the decision policy](owner-proof-decisions.md).

Distinguish the current working draft from past submission snapshots and ZIPs.
A body edit does not update an old package. Preparing a new package needs the
authorized release workflow, including its own output inspection.

## Review records in a research harness

Use the host's format when it has input-bound review records. Keep proof,
writing, owner checking, formal alignment, and build health separate.
Record the actual date, reviewer, mode, scope, and report against the checked
revision. A shared review lists every claim it actually covered. Include
external figures, style overlays, certificates, and other consumed inputs in
that input set; the source tree alone may not capture them.

An inherited review is historical evidence until its reviewed input and scope
match the current use. Do not backfill a current pass, refresh only a stale
pass's hashes, or infer owner checking from an editing request. Preserve the
owner's explicit confirmation and exact locator where required. A hash match
establishes input identity, not review performance or proof correctness.

For a formally verified claim, inspect the fixed formal statement and its
informal alignment when needed for the manuscript; a Lean build alone does not
establish that correspondence. Report finite computations within their actual
scope and do not describe an included open or unverified dependency as proved.

Run host checks required for the authorized work. In a Kicho project, run
`check` and `build` at the manuscript root and inspect relevant artifacts.
For an available standalone native editor, use its supported compiler and
preserve the source when compilation is unavailable. Inspect transformed or
submission outputs before relying on them; when an operation fails, inspect
its help and concrete diagnostics before choosing a supported alternative.

If a repository-wide strict check fails on another manuscript's migration
debt, report that separately from the current paper's result. Do not fabricate
missing reviews or change evidence statuses to clear the diagnostics. Describe
writer checks of new passages as such; they do not replace an earlier failed
independent verdict or establish a whole-paper independent pass.
