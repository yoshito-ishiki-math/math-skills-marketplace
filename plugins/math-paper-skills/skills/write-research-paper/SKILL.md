---
name: write-research-paper
description: Draft or revise an owner-directed mathematics manuscript, including direct exposition review and repair. Use for manuscript writing or revision, not standalone proof audits or literature research. Independent review requires explicit delegation.
---

# Write a research paper

Complete the authorized manuscript work while preserving the owner's mathematical
scope, authorial voice, and explicit decisions. Ordinary work stays with one
writer. Review evidence, edit authority, mathematical correctness, and build
health remain separate.

## Establish scope and load the relevant guidance

Identify the manuscript, current revision, requested deliverable, edit authority,
and existing work to preserve from the conversation and local records. A review
request alone does not authorize manuscript edits. Resolve routine choices from
context; ask only when a missing owner decision materially affects the work.
Continue independent in-scope work while that decision is pending.

- Read the host instructions and the paper's current records and local overlay.
- Before substantive manuscript drafting, revision, or exposition review, read
  the complete [author profile](references/author-style.md) and
  [paper-writing guide](references/paper-writing.md). Reuse them within the
  session unless they change. An exact mechanical correction needs the local
  context and applicable rules, not an unrelated whole-paper review.
- Use [workflow](references/workflow.md) for scope, revision, adjudication, and
  finish decisions. Read the sections for the current route; independent-review
  sections apply only to explicit delegation.
- For optional source-based wording evidence, use [corpus retrieval](references/corpus-method.md)
  only with an owner-designated private corpus. No corpus or personal wording
  choices are bundled. Historical usage does not override current directions.
- Before changing or reviewing proof detail, locate the paper's durable owner
  decisions and apply [the proof-detail policy](references/owner-proof-decisions.md).
  Preserve approved omissions and short arguments within their recorded scope.
  These records belong in private working files, never manuscript prose or
  submission artifacts, and do not certify mathematical correctness.

For a requested challenging exposition audit, or a concrete quantifier or
logical-dependency ambiguity in an authorized review, use
[challenging audit](references/challenging-exposition-audit.md). It prioritizes
mathematical interfaces over word substitutions and preserves approved brevity.

Use the existing writing state. For a complex task lacking one,
[writing-state.md](assets/writing-state.md) is an optional starting point;
do not create duplicate or empty records for a small edit.

For paragraph-ID setup or edits addressed by an existing paragraph ID, use
Kicho's `paraids` command and the conventions in
[latex-paragraph-ids](../latex-paragraph-ids/SKILL.md). Kicho owns the package
and helper; do not install them from skill assets or maintain a second copy of
the implementation here. Preserve existing IDs during revisions and do not
introduce tags into unrelated manuscript work. For submission or publication,
use Kicho's release preparation to comment out the package, IDs, red notes,
and settings in the release copy. Inspect the package-free compiled release,
its body layout, and the absence of editorial marks.

## Choose the route

**Lightweight, default.** Read enough manuscript context for the requested scope,
draft or revise, review the affected exposition, repair accepted issues, and
finish with proportional validation. A whole-paper request covers the whole
paper; a named-section request does not authorize sibling changes. Report the
review as writer-side or single-context.

**Heavyweight, explicitly delegated.** Use the independent-review section of
[workflow](references/workflow.md) and the selected protocol in
[read-research-paper](../read-research-paper/SKILL.md). Choose continuous,
editorial, or delta review to answer the owner's question. One authorization
covers one run unless comparison or iteration was explicitly requested.
Difficulty, failure, or submission proximity does not authorize another agent.
The mode-specific direction and launcher templates define frozen inputs,
isolation, and the permitted neutral proof-detail contract. The writer reads
the complete returned report and uses [revision-batch.md](assets/revision-batch.md)
to account for its findings without changing its literal verdict.

## Finish the requested work

Carry the authorized work through necessary repairs and the host's applicable
checks, rather than stopping at the first draft. Match validation to what
changed; batch independent checks and rerun only affected checks after a
failure or further edit. Compile and inspect manuscript artifacts when the
change or host workflow requires it. Do not launch unrelated tests or another
review simply because the previous checks passed.

Report the delivered scope, actual validation and its limits, any remaining
owner dependency, and the relevant working-tree state. Preserve evidence
statuses and current owner locks. Create only checkpoints required by the host
or requested by the owner. Submission packaging and publication require their
own authorization.
