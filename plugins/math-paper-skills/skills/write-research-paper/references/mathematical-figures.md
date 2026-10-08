# Mathematical figures and artifact checks

Use this guide for an authorized figure or diagram edit and for concrete
visual questions caused by that edit. A figure explains the construction; it
does not supply an unstated hypothesis or establish a theorem.

## State what the drawing represents

Identify the corresponding passage, objects, and mathematical role before
drawing. Prefer editable vector source, such as TikZ or SVG, when appropriate
for a mathematical schematic. Keep the source with the manuscript under its
existing convention and retain a passage-to-figure mapping when several
figures or imported constructions need tracking. A separate source table is
useful for that case, not mandatory for every diagram.

Label every relevant map with its source, target, and meaning. Check that
commutativity, factorization, or an asserted inclusion agrees with the text.
If an illustration is schematic, explain the specific convention needed to
avoid a false inference. A rectangle used to arrange factors must not imply
that a zero-dimensional factor is an interval or that the product carries
extra Euclidean geometry.

Distinguish a cover by closures from actual containment, a finite sample from
an infinite family or sum, and completeness of a function space from a property
of its metric image. Show choices, dependencies, and logical order as stated
in the proof. A plausible drawing cannot repair a missing mathematical step.

## Respect the requested edit boundary

When only illustrations are authorized, preserve theorem statements, proofs,
and evidence statuses. Compare protected source hashes and content diffs rather
than inferring preservation from an unchanged-looking PDF. Follow
[protected-revision checks](manuscript-provenance.md) for the actual locks.

If a theorem environment changes type during an authorized structural edit,
retain its stable labels and paragraph identity, preserve numbering where
required, and check generated reference names in both TeX and the PDF.
Do not confuse an environment rename with a new theorem identity.

## Inspect the affected artifact

Compile with the project's supported workflow. Inspect the affected pages for
readable labels, clipping, arrow endpoints, collisions, and placement relative
to the explanation. If a float moves across a section boundary, check the new
context as well. Preserve an owner-fixed figure location.

Use PDF text comparison, replacement-character checks, or page-bound checks
when they help diagnose the change. A text comparison does not inspect arrow
geometry or figure layout. Render only relevant pages when a visual check is
needed; do not turn every prose edit into a full image audit.

For a tagged manuscript whose ID display changes, check that the body area and
the affected figure layout remain as intended. Preserve the publication
convention for removing display tags without changing the body or paragraph
boundaries. Do not add page breaks or spacing merely to polish pagination;
repair a concrete readability, clipping, or misplaced-figure problem within
the existing typesetting conventions.
