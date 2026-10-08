# Public distribution

## Origin and scope

Based on the public `haruhisa-enomoto/math-paper-skills` default branch at
`614efd5039ea3794581fa610ae02ca84d78279f0`. Original MIT licensing and attribution are preserved.
Local enhancements were transferred as file changes onto that public history;
private development commits and branches were not imported.

## Included enhancements

- Explicitly delegated independent review, delta review, scoped proof-detail decisions.
- Writer-side revision tracking and challenging exposition audits.
- Conditional guides for manuscript provenance, mathematical figures, and
  resolving manuscript-local conventions.
- Kicho paragraph-ID usage conventions and private corpus retrieval/indexing scripts.
- A neutral author-profile entry point in place of personal style instructions.

## Excluded material

Identifying author-profile details, manuscript corpora and quotations, derived vocabulary
data, real research records, machine-specific paths, credentials, private logs,
and local development history are excluded. Research examples are upstream fictional
fixtures or newly written synthetic tests. `examples/author-style.md` is a
separately authorized, sanitized extract of concrete style preferences, with
generic notation and no manuscript quotations. It is optional, not a default. Public account identity remains
visible through GitHub hosting and noreply commit metadata.

The manuscript-local conventions guide retains general reconciliation rules;
private manuscript numbers, per-paper notation inventories, and individual
proof-detail decisions are excluded. The provenance and mathematical-figures
guides contain portable workflow guidance. No private corpus material was
added with these references.

## Customization

Store personal configuration, source material, and generated evidence outside
this public checkout or in explicitly ignored private locations. Ignoring a file
does not remove it from existing history. Review additions before future pushes.
A vocabulary tool's output contains private source excerpts even when its code
is safe to distribute.

## Validation limits

Repository tests check software behavior and record consistency, not mathematical
correctness. Corpus tests use synthetic text. Paragraph-ID implementation and its tests now live in Kicho; this repository
keeps only usage conventions and routing. Kicho, Lean, and external literature
services require their own project-specific setup and validation.

## Release checks

3 synthetic corpus/link tests passed after paragraph-ID runtime tests moved to Kicho.
All three skill packages passed the skill validator.
The release file scan found no configured personal identifiers, local home paths,
private-key blocks, or recognized access-token patterns. This scan is bounded
by its patterns; it is not a guarantee about arbitrary future additions.

## Optional style example

The example was added after the initial portable release. Private profile paths,
project-specific references, source evidence, and individual decisions remain
excluded. Adopting its rules requires an explicit profile choice; the shared
skill entry point remains neutral.
