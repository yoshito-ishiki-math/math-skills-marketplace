# Math Skills Marketplace

English | [日本語](README.ja.md)

A GitHub-backed Codex plugin marketplace maintained by Yoshito Ishiki.
The marketplace identifier is `yoshito-ishiki-math`.

## Install

With a Codex CLI that supports `codex plugin`, run:

```sh
codex plugin marketplace add yoshito-ishiki-math/math-skills-marketplace
codex plugin add math-paper-skills@yoshito-ishiki-math
```

Start a new chat after installation. In the desktop app, refresh or restart if
the newly added marketplace has not appeared, then select **Yoshito Ishiki Math**
in the plugin directory and install **Math Paper Skills**.

Check the installation with:

```sh
codex plugin marketplace list
codex plugin list --marketplace yoshito-ishiki-math --json
```

## Included plugin

`math-paper-skills` version **0.1.0** installs these three skills together:

| Skill | Purpose |
| --- | --- |
| `write-research-paper` | Owner-directed mathematics manuscript writing and revision |
| `read-research-paper` | Explicitly delegated independent exposition review of a frozen manuscript |
| `latex-paragraph-ids` | Stable paragraph identifiers and associated LaTeX helpers |

The reader uses sibling-relative links to the writer's shared guidance.
The package preserves that layout. Exposition review does not certify proof
validity. Optional corpus tools need owner-designated input; the package does
not contain private manuscripts or a private corpus. Python 3.10 or later is
recommended for the bundled helpers. Paragraph-ID typesetting needs a LaTeX
installation with the packages described in the bundled usage guide.

## Update

```sh
codex plugin marketplace upgrade yoshito-ishiki-math
codex plugin add math-paper-skills@yoshito-ishiki-math
```

Published marketplace releases are snapshots: they do not automatically follow
changes in the source skills repository. Check the version and provenance before
updating a reproducible manuscript workflow.

## Source and license

The bundled files come from
[yoshito-ishiki-math/math-paper-skills](https://github.com/yoshito-ishiki-math/math-paper-skills)
at commit `f2faa773fa073869d29b4e2a369d10170d2a4feb`.
That repository is a public derivative of
[Haruhisa Enomoto's math-paper-skills](https://github.com/haruhisa-enomoto/math-paper-skills).
Its original MIT license, attribution, and public-release notes are retained.

[UPSTREAM.json](UPSTREAM.json) records the source revision, original Git blob
identities, and SHA-256 hashes. All 35 imported files are preserved byte for byte.
The plugin manifest and icon are additions. Marketplace packaging is licensed
under the root [MIT license](LICENSE); imported files retain their
[source license](plugins/math-paper-skills/LICENSE).

This is a repository marketplace. It has not been submitted to OpenAI's public
plugin directory. See the official
[packaging guide](https://developers.openai.com/plugins/build/plugins) and
[public submission guide](https://developers.openai.com/plugins/deploy/submission).

## Validate a checkout

```sh
python3 tools/validate.py
python3 -m unittest discover -s plugins/math-paper-skills/tests -v
```

Validation covers package metadata, paths, skill references, imported file
integrity, and the source repository's synthetic helper tests. It does not
verify mathematics or certify all LaTeX classes and layouts.
