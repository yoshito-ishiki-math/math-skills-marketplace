# Mathematics-paper workflow

This is the operational contract for the writer/supervisor. The portable
[paper-writing guide](paper-writing.md) is the exposition standard, while the
reader skill owns the independent review protocols. Host-project instructions
may add local state, tooling, artifact, and publication requirements.

## Owner intent, state, and authority

Use the paper's existing compact writing state for sustained work. Create one
only when the task needs durable coordination. It records current positive
decisions, the base revision, valid gates, and the next authorized action, not
the history of every correction. An exact small edit needs no new state file.

Infer a compact task contract from ordinary owner language:

- exact target and revision;
- requested outcome;
- whole-paper, named-section, or bounded edit scope;
- content boundary and structural locks;
- owner-decision boundary; and
- finish state.

Resolve routine details from the conversation and relevant project records.
Ask only about a material owner choice that cannot be inferred. Wait on the
dependent action while continuing independent authorized work. Do not require
the owner to configure the harness or reduce a broad task to one local repair.

`Edit authority` is exact:

- `none`: discuss, diagnose, review, or propose; do not edit the manuscript;
- a named file, section, or batch: edit only that scope; and
- a broad drafting request: draft within the current owner locks, without
  expanding the mathematical or publication target.

Skill activation never creates authority. Pause when a needed choice would
materially change the owner's audience, story, theorem hierarchy, scope, or
voice.

Treat owner wording as approved copy only when it is offered as copy. If the
owner marks a phrase as approximate, says an earlier version existed, or is
uncertain about the wording, recover the referenced text when available. If it
cannot be recovered, preserve the substantive direction but label new wording
as a proposal; do not silently literalize the paraphrase or invent a label.

## Durable proof-detail choices

Use [author proof-detail decisions](owner-proof-decisions.md) to record and
reuse the owner's intentional omissions and deliberately concise proofs.
Keep the registry durable and separate from temporary writing state. Check it
before expanding a proof, preparing a reviewer packet, or adjudicating a
finding about missing detail. A valid matching approval can close that repeated
request without asking again; a genuinely new concern needs a precise reason.

## Select one mode

### Lightweight writing and review — default

Use lightweight mode unless the owner explicitly requests heavyweight mode or
subagent delegation. Use the owner request, not the easiest defect found, to
select a direct route:

```text
whole paper: inspect/recover contract -> direct revise -> writer regression -> validate/finish
named section: read cumulative context -> scoped revise -> writer regression -> validate/finish
exact local edit: revise -> focused writer regression -> validate/finish
new paper: shape -> draft/integrate -> writer regression -> validate/finish
new section: shape if needed -> draft/integrate -> writer regression -> validate/finish
```

These routes are deliberately single-agent. Do not spawn an independent reader
for routine revision, ordinary drafting, or every exposition edit. An
unqualified request to revise a paper means the direct whole-paper route. For a
named-section task, read enough cumulative context to understand its role while
keeping edit authority confined to the section. A needed change outside that
scope requires one short expansion request.

A precise local correction may enter at `revise`. Adding a section authorizes
only the new section and the minimal introduction, transition,
cross-reference, and later-summary changes needed to integrate it. Reopen shape
before a new paper or any addition that materially changes audience, promise,
result package, architecture, or budget.

Never escalate automatically. Spawn an isolated reviewer only when the owner
explicitly asks to use a subagent, another agent, or an isolated reviewer for
the current task. A request to review, revise, check submission readiness, or
read cold is not delegation authorization by itself. Neither a nearly final
paper, a changed promise or architecture, nor an unresolved exposition risk
creates authorization.

Without explicit delegation, complete the direct route and label any review as
writer-side or single-context. You may recommend independent review as a later
option without blocking completion.

### Heavyweight writing and independent review — explicit only

Enter heavyweight mode only after the owner explicitly names heavyweight
review, subagent delegation, another agent, or an isolated reviewer. Its route
is:

```text
shape/inspect -> draft or revise -> freeze -> one selected independent review -> adjudicate/repair -> authorized regression -> validate/finish
```

Select the one review mode that answers the live question. Continuous mode
tests first encounter; editorial mode tests necessity and referential
precision; delta mode tests bounded repair closure. One authorization permits
one reviewer run unless the owner explicitly requests comparison or an
iterative cycle. Do not replace an invalid or failed reviewer automatically.

## Shared writing method

### Shape calibration

For a new paper or a material change to its audience, promise, or architecture,
resolve the following choices together, reusing existing owner decisions:

- audience and assumed background;
- one-sentence paper promise;
- three to five results in narrative order;
- section jobs and alternate reading paths;
- main-text/appendix and length/detail boundary; and
- provisional title, abstract/introduction sketch, and one representative body
  passage.

Record approved choices positively with locators or exemplars. Reopen shape
only after a material change to audience, promise, result package,
architecture, or budget. Title wording may remain provisional.

Do not schedule approval rounds merely to follow a template. Present a
calibration or adjudication question only when an unresolved owner choice
blocks the authorized work; existing decisions remain effective.

### Draft and integrate

Draft section-sized units within the locks. Before writing a section, know what
the reader may use, what capability the section adds, why it appears there,
and what later result consumes it.

Integrate in document order. Check first encounters, terminology, theorem
hierarchy, reading paths, duplicated explanation, orphaned remarks, and unused
machinery. Record the exact revision and audit scope. This contaminated
writer-side pass is not independent reading evidence. Never label it forward
reading, forward-blind reading, or a cold review.

Make a separate boundary pass from top to bottom. First check the structural
invariant: every numbered section and subsection, including appendices, begins
with ordinary prose before any formal environment, display, list, or nested
heading. Then retain the job of the preceding passage and read the heading
together with the opening prose and first formal statement. Check whether the
manuscript supplies the local handoff between those jobs, rather than merely
making the sequence recoverable from the table of contents or Organization
block. Distinguish a concise natural opening from an abrupt switch, an
interruptive detour, delayed motivation, or displaced explanation. The prose
must do real connective work; a formulaic transition does not pass the
continuity test merely because it passes the structural one.

Apply two tests to every transition, remark, qualification, repeated
explanation, informal alias, and apparent result name. First, retain it only
when deletion would cause an identifiable loss for the intended reader, such
as a plausible false inference, an unexplained hypothesis, a hidden dependency,
or missing context used later. Second, if retained, require an exact
mathematical subject, predicate, status, and referent. A true limitation or
understandable purpose does not by itself earn space, and a reader's ability to
guess which theorem or assertion was intended does not make the wording
precise.

## Heavyweight mode: independent review

The remainder of this section does not apply to lightweight mode.

### Freeze and review

Apply this section only after the owner explicitly authorizes subagent
delegation for the current review.
Freeze one revision. The host must give `read-research-paper` a fresh,
read-only context without drafting history, expected findings, or later
manuscript text. One stable reader must handle a continuous review; use
one reader for the selected gate. Do not default to a swarm.

The neutral proof-detail contract allowed by
[the decision policy](owner-proof-decisions.md) is part of the audience and
detail boundary, not drafting history. Freeze it before launch. Withhold the
full registry; disclose only entries for issued text, as specified in that
policy. Never add contracts in reaction to review findings.

Use a two-step launch: first give the fresh reader only the governing guides
and task direction and wait for its readiness confirmation; then reveal the
first cumulative segment. Never combine initialization and manuscript exposure
in one message.

If isolation, frozen input, or reader continuity cannot be established, record
the review as invalid rather than weakening the label.

### Run the skeptical editorial pass

Use this pass only when the owner explicitly delegates an editorial reviewer,
not automatically after a continuous report, whole-manuscript revision, or
nearly final integrated candidate. Run one fresh agent in `editorial` mode
under the reader skill's
[skeptical-editor protocol](../../read-research-paper/references/skeptical-editor-review.md).
It is especially appropriate when the owner requests a necessity, compression,
or referential-precision audit.

The editor receives the complete reading-order manuscript with a reproducible
content hash, audience, promise, detail budget, and protected content, but no
drafting history, diagnoses, continuous report, vocabulary report, expected
findings, or proposed cuts. It verifies the hash before reading, reads the
whole paper, then runs separate necessity and referential-precision audits. It
inventories remarks, defensive qualifications, informal aliases, apparent
result names, loose result pointers, and descriptive substitutes for exact
mathematical predicates. A necessity finding must identify marginal reader value rather
than merely say that a passage is clear or mathematically true. A precision
finding must identify the intended exact referent or predicate and the
inference or ambiguity imposed by the current wording; a necessary passage may
require `rename` or `replace` rather than deletion or compression.

If both continuous and editorial review were separately justified or explicitly
requested, adjudicate their owner-judgment findings together. Accepted clean
deletions, compressions, renamings, and local precision replacements ordinarily
need writer-side regression, not another editorial pass. Commission another
fresh editorial review only after explicit authorization for that additional
run.

### Adjudicate and revise

When an independent review was run, read the complete review before editing.
Convert observations into clusters by
common cause. Each cluster records an exact stumble, success test, minimal
repair, explicit non-scope, risk class, decision, changed locators, and
regression result.

Before changing the manuscript, build the finding-coverage table in
`assets/revision-batch.md`. Give every ranked finding a stable source
identifier. Also give an identifier to every distinct objective defect stated
in the report's synthesis but not already represented by a ranked finding, and
to every editorial inventory item whose verdict calls for change. Map each
source identifier to exactly one cluster. Several findings may share a cause
and cluster, but none may be omitted or silently absorbed. Journal entries are
evidence for these source findings; they need not each become a separate
cluster.

Copy each review's literal verdict and exact reviewed revision into the batch
and writing state. The writer cannot upgrade `FAIL` to `PASS` by adjudication,
self-review, compilation, or repair. Record closure of the failed review's
findings separately through the fresh regression required below. If the edit
invalidates the continuous or editorial gate, only a new review in that mode
can establish the replacement verdict.

First decide whether the evidence establishes a defect at all. Abstention is a
valid temporary decision. Record it as `defer`; it remains open and prevents a
finished checkpoint. Missing surrounding context warrants a conditional
diagnosis, not a manufactured repair.

Separate the reader's observation from its diagnosis and proposed repair. A
report that the reader had to infer, reread, search backward, or translate
ordinary language into an exact mathematical predicate is evidence about the
current prose. `Reject` or `defer` may apply to the proposed cause or remedy;
it must not erase that observed burden merely because the intended meaning is
nearby, familiar to the audience, or recoverable to an expert. If the signal
identifies ordinary language standing in for the predicate or referent used by
the argument, treat it as a local/objective exposition defect and make the
smallest adequate repair. Treat the signal as a nondefect only when the exact
content was already available at that point or the reported burden conflicts
with the explicitly assumed reader background; record that concrete textual
or contract evidence rather than an expertise judgment.

`local/objective` means the intended result is fixed by accepted manuscript
content or an accepted project convention—for example, a broken reference, undefined
symbol, literal numerical error, omitted already-accepted hypothesis, or clear
drafting-process leakage with a direct deletion or replacement. It also
includes a first-reader signal that ordinary language conceals the exact
mathematical predicate or referent used in the argument.

`owner-judgment` includes paper promise, story or architecture, title/abstract
voice, theorem hierarchy, literature position, length/detail boundary,
retention of substantial material, new terminology, and disputed diagnoses.
Batch these with one recommendation, reason, tradeoff, and minimal alternative.

Use the four decisions literally.

- `implement`: accept the diagnosis and proposed repair class;
- `modify`: accept the observed burden but use a different repair;
- `reject`: close the finding only with exact earlier text or an explicit
  audience/owner contract showing that the reported burden is not a defect;
- `defer`: leave the finding open for owner judgment or missing evidence.

An applicable explicit proof-detail decision is an owner contract for the
`reject` disposition of a repeated expansion request. Cite its ID, approved
scope, and applicability check. Preserve the reading observation without
making the accepted omission an unresolved defect. Reopening requires the
concrete new reason specified in the decision policy, not a preference for
more detail.

Disagreement with proposed wording is not rejection of the observed burden.
An objective finding cannot remain deferred in a completed writing task. An
owner-judgment finding may remain open only if the task is reported unfinished
and the owner decision is named as the dependency, or if the owner explicitly
excludes it from the requested finish state.

A reader's prescription is not an accepted repair. Use the smallest repair
that passes the cold-reader success test:

1. delete unneeded material;
2. reorder existing material;
3. replace the defective sentence or paragraph;
4. add one local clause; then
5. add a definition, proof block, or theory only if the interface requires it.

Apply accepted clusters in one bounded pass. Check the aggregate diff against
success tests and non-scopes, and justify substantial net prose growth. For an
editorial necessity finding, record the passage's intended role, the exact
reader-visible loss under deletion, and any concrete beneficiary before
deciding to retain it. For an editorial precision finding, record the intended
exact referent or predicate, what the current wording licenses, and the
reconstruction imposed on the reader before deciding to keep, rename, or
replace it.

## Validate and finish either mode

### Adjudicate host-project diagnostics

After applying the accepted revision and before freezing it for independent
regression, run any writer-side diagnostics required by the host project. A
diagnostic locates passages for judgment; its warnings are not defects and
clearing its warning count is not a success criterion.

For a lexical or terminology warning, inspect the complete sentence and its
mathematical role before changing the flagged form. Decide first whether the
passage uses an undefined or unnecessary label, an ordinary-language
paraphrase that hides the exact mathematical predicate, an apparent theorem
name without an established referent, a citation in place of the result being
used, or private-process language. Repair that semantic or expository defect
under the paper-writing guide. Consider spelling, hyphenation, or another
surface normalization only after the phrase itself is precise, necessary, and
properly introduced.

Never change a token merely to make a warning disappear. A justified technical
term may remain flagged. The diagnostic gate is satisfied when the required
scope has been checked against the exact revision and every warning has been
inspected and adjudicated, not when the report is empty. Rerun the diagnostic
after any accepted wording change so that the recorded report matches the
revision being frozen. Keep writer-side diagnostic reports from isolated
readers.

### Regress, validate, and finish

For an ordinary direct route, check changed regions and their affected
context, references, terminology, notation, and promised scope. Run compilation
and host checks applicable to the change. Batch independent checks; repeat
affected checks only after a further edit, failure, or unresolved concern.
This proportional writer regression is the default completion invariant.

Use a fresh delta reader only when the owner explicitly delegates that
additional independent run. It checks changed regions, surrounding context,
and recorded success tests without seeing diagnoses or preferred repairs.

The regression packet names the exact implemented or modified cluster
identifiers it covers. Compare that set with the revision batch before launch
and after the report returns. A delta verdict applies only to those identifiers
and their supplied dependencies. It cannot close a rejected or deferred
finding, an omitted cluster, or unchanged prose outside the packet, and it does
not relabel an earlier failed whole-paper verdict.

Independent regression is not required for every exposition edit and is never
spawned automatically. Run it only after the owner explicitly authorizes that
reviewer run. Otherwise complete the manuscript revision under direct
validation and do not mislabel writer-side checking as independent evidence.

- Any further edit to a checked region or its dependency invalidates its delta
  result.
- A changed promise, structural front matter, section order, or reading path
  invalidates the continuous review. A new full run still requires explicit
  delegation authority.
- Unchanged local prose outside those dependencies does not require a full run.
- If the abstract or introduction grows in consecutive rounds, the repairs are
  the wrong kind and the review will not terminate; correct that before
  asking the owner whether to commission another reader.

A completed writing task is tied to one exact revision. For a direct route,
require current owner locks, completed requested edits, proportional writer
regression, compilation, artifact inspection, and host-project gates. When an
independent review was run, additionally require complete adjudication of its
in-scope findings and preserve its literal verdict. A source `FAIL` never
becomes a source `PASS` through writer-side repair.

If an independent regression fails, repair directly and commission one more
review only after explicit owner authorization. Otherwise report the unresolved
gate instead of entering an automatic reviewer loop. If no repair is
accepted, do not manufacture an edit or empty checkpoint. Keep reader and
editor reports in the host project's temporary review area unless their
preservation was authorized.

Do not prepare submission packages, declare a release, or perform external
publication actions unless the owner separately requests them. Compilation,
search results, automated checks, and writer self-review do not certify the
whole manuscript.
