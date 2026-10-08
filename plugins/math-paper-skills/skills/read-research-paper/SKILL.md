---
name: read-research-paper
description: Independently review a frozen mathematics manuscript in an explicitly delegated reviewer context. Use for continuous first-reader, editorial, or bounded delta review, not proof verification, manuscript editing, or ordinary writer-side review.
---

# Independent exposition review

Review the frozen manuscript in the assigned mode and report reading evidence.
The writer owns adjudication and edits. Selecting this skill does not authorize
creating a reviewer; the owner must explicitly delegate the run. The reviewer
does not spawn additional agents.

## Validate the context

Require an explicit `continuous`, `editorial`, or `delta` mode, a fresh context,
a frozen manuscript revision, allowed inputs, assumed background, report
destination, and read-only access to the manuscript. Editorial review also
requires a reproducible reading-copy hash. If an isolation requirement fails,
report the run invalid; do not simulate freshness.

Before reading, load the complete shared
[paper-writing guide](../write-research-paper/references/paper-writing.md) and
[author profile](../write-research-paper/references/author-style.md), then the
selected mode's protocol below. These define review criteria, not writer state.

Withhold writer workflow and conversation, private owner-decision records,
research notes and ledgers, earlier reviews, drafting/version-control history,
expected findings, and overlays containing writer-only state. Under the shared
[proof-detail policy](../write-research-paper/references/owner-proof-decisions.md),
a neutral contract explicitly issued with allowed text is a narrow exception:
respect approved omissions and brief arguments without reading their private
registry. Preserve actual reading observations, but require a concrete new
issue beyond the approval before repeating an expansion request.

## Read only the selected protocol

| Mode | Input and purpose | Protocol |
|---|---|---|
| `continuous` | Cumulative segments, one stable reader, no later text; first-encounter exposition | [Continuous first reader](references/first-reader-review.md) |
| `editorial` | Complete frozen paper; necessity and referential precision | [Skeptical editor](references/skeptical-editor-review.md) |
| `delta` | Named repair clusters, changed regions and sufficient context; bounded regression | [Delta regression](references/delta-review.md) |

Continuous and editorial review initialize with guides and direction only.
Confirm readiness before receiving a manuscript path or text in a second
message. Editorial readers verify the supplied reading-copy hash before
reading. Continuous readers receive only issued cumulative text and neutral
contract entries for already visible locators; later text, later contracts,
compiled output, and the supervisor's segment map remain unavailable.

For a requested challenging audit or a concrete quantifier/dependency ambiguity,
apply the shared [audit emphasis](../write-research-paper/references/challenging-exposition-audit.md)
within the assigned mode and allowed inputs. It does not authorize proof
verification, later-text access, or another reviewer.

## Report the evidence and its limits

Use the selected protocol's report and literal verdict format. Identify the
mode, exact revision, material actually read, isolation conditions, completion
state, and any applicable proof-detail contract IDs. Give precise locations and
a concrete reader burden, ambiguity, or marginal reader value for findings;
word categories and flag counts do not establish defects. Distinguish an
observation from its diagnosis and proposed repair.

Do not edit or adjudicate the manuscript, verify proofs or novelty, open cited
sources, or certify mathematics. A delta verdict covers only supplied clusters;
an editorial verdict does not certify first-encounter readability. Preserve
these boundaries when reporting a possible gap or a successful review.
