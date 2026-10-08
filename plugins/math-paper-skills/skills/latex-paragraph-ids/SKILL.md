---
name: latex-paragraph-ids
description: Install and maintain stable random paragraph IDs in LaTeX projects, toggle margin display independently, and locate paragraphs for ID-based editing requests. Use when paragraph identifiers are requested or already present, including submit, submit --arxiv, and publication preparation for tagged manuscripts; do not add tags during unrelated manuscript work.
---

# Stable LaTeX paragraph IDs

Keep the package and helper in this skill as the shared source. Each manuscript
uses a local copy of the package so it remains portable and version-stable.
Read [usage](references/usage.md) for placement, display controls, and limitations.

## Introduce IDs into an authorized project

Identify the intended manuscript and its main TeX directory. Install with
`python3 <skill>/scripts/install.py <main-tex-directory>`. This copies only
`assets/paragraphids.sty`, is idempotent, and refuses to replace a different
existing file. For a requested update, inspect the difference, preserve local
customizations, then replace deliberately; do not silently upgrade projects.

Add `\usepackage{paragraphids}` to show IDs; `[hide]` hides them during
ordinary drafting. IDs always use the physical left page margin, including
even pages and two-column pages; check collisions for aligned column starts. There is no showkeys dependency or auto option in v0.4.
Place each literal `\paraid{p-xxxxxxxxxxxx}` on its own line immediately before
the paragraph text, with no blank line between marker and text. Put theorem,
proof, and item commands on separate preceding lines. Generate IDs with
`python3 <skill>/scripts/paraids.py new --root <paper> --count <n>`.
The helper never edits manuscript sources; do not attempt blanket regex-based
paragraph insertion. The shared helper need not be copied into every project.

## Edit or review by ID

Find the source with `python3 <skill>/scripts/paraids.py find <id> --root <paper>`.
Use `find --include-comments` to locate commented IDs too. New-ID generation
reserves commented IDs within the search scope automatically. Keep retired IDs
in existing project records or source comments if future generation must avoid
them; deleted history outside the search scope is not scanned.
Move the ID line together with its paragraph, never independently. When copying,
copy the pair then issue a new ID for the copy. Do not insert a heading or another
paragraph between a marker and its intended text.
Confirm the paragraph's current context before editing. Preserve IDs during
wording changes and moves. Give new/copied paragraphs new IDs. On splitting,
retain the old ID on one part; on merging, retain one ID and retire the others.
When extracting a lemma or otherwise restructuring paragraphs, update the
mathematical references together with the IDs. Retain the original ID on one
part, issue IDs for new parts, update the lemma's uses to its precise label,
and check for obsolete broad section references.
Never regenerate all IDs, derive IDs from content hashes, or reuse retired IDs.
Where a project already records editorial decisions outside the manuscript,
use IDs as locators in those records; an ID itself stores no proof decision.

## Validate proportionally

Batch source checks with `python3 <skill>/scripts/paraids.py check --root <paper>`.
The scanner handles literal UTF-8 tags and common comments/verbatim constructs,
not full TeX expansion. Scope it to the active manuscript; alternative versions
may repeat IDs. TeX also rejects duplicates and invalid IDs, including hidden
ones. First integration or layout changes warrant two-pass shown/hidden builds
and PDF inspection, checking line/page breaks and margin collisions. Ordinary
text edits need only the project's relevant checks. Do not imply universal
layout invariance from the article sample; two-sided/two-column and custom
margin layouts require local verification.

Bundling this skill does not authorize bulk changes to existing manuscripts.

## Submission and publication convention

When the author requests `submit`, `submit --arxiv`, or preparation for publication,
comment out the paragraphids package loading command AND every paraid marker
in the release source. Preserve the literal IDs in comments. Comment out package
configuration and display commands too (ParagraphIDsOn/Off, paragraphidfont,
paragraphidwidth); leave no active dependency on this package. Separate mixed
package-loading lines before commenting so other packages remain loaded.
Comment out showkeys loading as well if present; it is independent of paragraphids.
Do not merely set `[hide]`: the submitted source must compile without
paragraphids.sty, which should be omitted from the submission archive.

Each marker occupies its own line. If an old marker shares a line with body text,
separate it first; never comment out the paragraph itself. Preserve blank lines
that separate paragraphs, and do not insert new blank lines around markers.
Handle included preambles and TeX files within the actual release scope.
Make release preparation idempotent: leave already-commented lines unchanged,
never accumulate percent prefixes, and never change body text or paragraph
boundaries on repeated runs.
Use the release/staging copy when available, preserving working review sources.
Compile the extracted release files without the custom package available; inspect
the PDF for hidden IDs/keys and compare body line/page breaks. Treat these as
two separate checks: absence of editorial marks and preservation of body text
and layout. A successful compile alone establishes neither. Comment removal
is expected to preserve paragraph layout but must be checked for the actual
manuscript. Keep validation lightweight and batch it with existing release checks.
This convention does not authorize uploading or publishing by itself.

## Red editorial notes

Use `\paranote[vertical offset]{number}{comment}` on its own source line at the
relevant paragraph. The optional offset defaults to 8pt, below the paragraph ID.
The number is supplied explicitly to preserve the author's issue numbering.
Notes wrap in the physical left margin in red, share the package show/hide
switch, and do not automatically avoid collisions. Inspect annotated pages and
adjust offsets or shorten notes where needed; do not change body layout merely
to fit notes. Width and font are configurable with paragraphnotewidth and
paragraphnotefont. Japanese notes require the manuscript's Japanese-capable
engine/font setup. Notes may be written in the original manuscript when
annotating is authorized, rather than requiring a separate PDF-only workflow.

For every submission or publication version, comment out ALL paranote calls
and their continuation lines, plus their package-specific settings, along with
the package and paraid lines. Keep body text outside comment lines. Check all
included source files and inspect the final PDF to ensure no red editorial note
or issue number survives. Hiding alone does not satisfy the release convention.
The working source can retain notes in comments; never leave active note calls
when the package loading is commented out.
