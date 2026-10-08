---
name: latex-paragraph-ids
description: Use Kicho-managed stable paragraph IDs for LaTeX editing and release preparation. Apply when IDs are requested or already present; do not add tags during unrelated manuscript work.
---

# Kicho-managed paragraph IDs

Kicho owns `paragraphids.sty`, its distribution, ID tooling, and submission
cleanup. This skill only records author conventions and routes to Kicho; do
not bundle the package or maintain an independent implementation in skills.
Check `kicho help paraids` for the installed interface. If an older Kicho lacks
the command, report the needed update while continuing independent work.
The [migration note](references/usage.md) replaces the former bundled-skill manual.

## Use the Kicho commands

```sh
kicho paraids install --root <paper>
kicho paraids new --root <paper> --count 3
kicho paraids find p-a7f3c921e40b --root <paper>
kicho paraids check --root <paper>
```

Installation preserves a local package copy and refuses to overwrite a
different version. Inspect customizations before an explicitly requested
upgrade. These commands do not insert tags or rewrite manuscript text.
`new` reserves commented IDs; `find` and `check` accept `--include-comments`.
Scope checks to the active manuscript, since alternative versions can share IDs.

Place each literal `\paraid{p-xxxxxxxxxxxx}` on its own line immediately before
its paragraph, after any theorem/proof/item command, without an intervening
blank line. Move IDs with their paragraphs. Retain IDs through wording edits;
give new and copied paragraphs new IDs. When splitting, retain one old ID and
issue new ones for the other parts; when merging, retain one ID and retire the
others. Update mathematical references during structural edits as well.
Never regenerate all IDs or reuse retired IDs. Preserve retired IDs in existing
source comments or editorial records when they must remain reserved.

The package keeps `[show]`/`[hide]`, `\ParagraphIDsOn`/`\ParagraphIDsOff`, and
physical-left placement independent of showkeys. Authorized red notes use
`\paranote[vertical offset]{number}{comment}` on separate source lines. Inspect
collisions and adjust the annotation, preserving body layout. Japanese notes
use the manuscript's Japanese-capable engine and fonts.

## Submission and publication

For `submit`, `submit --arxiv`, or publication preparation, use the existing
Kicho project's submission workflow. Its release copy comments out package
loading, IDs, complete multiline notes, display/font/width settings, and
showkeys loading, and omits `paragraphids.sty`. Hiding alone is insufficient.
Kicho preserves working review sources and rebuilds marked standard-submission
PDFs from the cleaned copy; arXiv export remains source-only.

Check the actual exported files, compile without the custom package available,
and inspect both the absence of editorial marks and preservation of body text,
paragraph boundaries, and layout. Custom TeX wrappers may exceed the literal
scanner's scope. Batch these checks with the existing release checks; they do
not authorize uploading or publication. For detailed syntax, consult Kicho's
`docs/paragraphids.md`, rather than a second manual maintained in this skill.
