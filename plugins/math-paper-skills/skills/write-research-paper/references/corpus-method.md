# Optional private corpus tools

No author corpus, manifest, quotations, vocabulary preferences, or generated
index is distributed. Ordinary writing does not require this workflow.

For authorized corpus work, keep source files read-only and keep the manifest,
choices, and generated outputs in a private directory outside this checkout.
The tools use Python 3.10 or newer and only the standard library.

A manifest is a JSON object with a `records` array. Each record has `id`, `work` (a stable work identifier), `role`
(`primary`, `historical`, or `evaluation`), `path` relative to the corpus root,
and `sha256` of the exact source bytes. Use primary records for distinct works,
historical records for older versions, and evaluation records for held-out work.
Choices are a JSON array of four-element arrays: search terms, attested target,
role, and condition. An empty array builds only the word inventory.

```sh
python3 scripts/style_corpus.py --manifest /private/corpus/manifest.json --root /private/sources
python3 scripts/build_lexicon.py --manifest /private/corpus/manifest.json --choices /private/corpus/choices.json --root /private/sources --output /private/corpus/output
python3 scripts/lookup_lexicon.py --references /private/corpus/output --word obtain
```

Run from this skill directory or use an absolute script path. Source hashes are
checked before reading; paths must stay within the designated source root.
Output must be outside that root. Extraction is heuristic: TeX macros are not
expanded, surface forms are not lemmatized, and source snippets can include
adjacent text. Generated output contains source excerpts and paths and must be
reviewed separately before any publication. Missing words are not prohibited
words; proposed alternatives are not evidence of actual author revisions.
