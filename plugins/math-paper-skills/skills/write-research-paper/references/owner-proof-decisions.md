# Remembering author-approved proof detail

Use this policy when writing or reviewing a manuscript with an intentional
proof omission, a deliberately short argument, or an explicit owner decision
about proof detail. It applies to direct and independent exposition review.
It does not authorize a proof audit, a manuscript edit, or another reviewer.

## Durable record owned by the paper

The writer maintains the record in the paper workspace, not in global model
memory or the shared author profile. First inspect the paper's existing owner
choices, revision notes, and writing-state pointers. Reuse an existing durable
registry if it can preserve the fields below and is read at the start of work.
Otherwise create `AUTHOR-PROOF-DECISIONS.md` beside the manuscript, using the
[record template](../assets/author-proof-decisions.md), and link it from the
paper's existing README or writing state. Do not create an empty registry.
Do not delete this record when temporary writing state or reviews are retired.

A clear owner statement such as “この証明は意図的に省略”, “簡単な議論なので
この短い証明でよい”, or “ここはこれ以上詳しくしない” is enough to record the
identified decision without asking for the same approval again. If only record
editing is authorized, update the record and leave the manuscript untouched.
Silence, terse prose, an agent's judgment of easiness, a previous review pass,
and a suggestion by another agent are not owner approval. Recover existing
explicit decisions from authorized local records when available, preserving
the source and uncertainty; do not invent approvals for unmentioned passages.

## Recording authority and blocked persistence

A clear owner proof-detail decision authorizes its ordinary recording only
within the currently permitted record scope. Before recording, reconcile any
prior restriction with the current request: distinguish manuscript editing,
record-file editing, and Git staging/committing. A restriction on one is not
automatically a restriction on all three. A newer explicit request to record
this decision can supersede an earlier conflicting record restriction; a
request only to omit the proof does not by itself lift an explicit ban on
record editing. Do not ask again when the existing conversation already
clearly authorizes the specific record action.

The same-checkpoint rule below is a persistence default, not permission to
override owner restrictions or an automatic approval rejection. If blocked,
continue authorized manuscript work and apply the explicit owner decision in
the current conversation. Report the precise persistence state: recorded and
committed, recorded but uncommitted, or not recorded. Do not promise that future
sessions or independent reviews will remember an unrecorded decision.

If Git staging/committing alone is rejected, do not discard an otherwise
permitted record-file edit merely because it cannot be committed. Conversely,
if the record edit itself is prohibited, do not move the same record to another
file, project, or global memory to evade the restriction. Preserve unrelated
work when restoring any unauthorized edit. A denial does not erase the owner's
proof-detail decision or authorize re-expanding the proof.

When a real unresolved authority conflict requires clarification, ask one
specific question identifying the exact record file and whether permission is
needed to edit it, stage it, or commit it. Explain the earlier conflicting
restriction and, if applicable, the automatic review's rejected action and
stated reason. Do not vaguely ask the owner to approve the omission again.
Before a later audit, use an authorized durable decision record or supplied
neutral contract; if persistence is still blocked, report that limitation.

For each decision, keep:

- a stable ID, for example `OPD-001`, and state `active`, `recheck-needed`, or
  `superseded`;
- the manuscript identity, stable theorem/equation label or exact textual
  anchor, source path, and the version at which the decision was made;
- the precise step omitted or the argument deliberately kept short, including
  the relevant assumptions and dependency/interface being used;
- the approved extent: `omit proof`, `brief proof`, or `omit specified step`,
  with what must remain explicit and the intended audience/background;
- the actual owner wording and its date and checkable conversation/note
  locator when available; mark unavailable date/locator as unknown, not guessed;
- the stated reason, if supplied, and any limitations on the approval;
- the latest applicability check and its revision, with a concrete reason for
  any reopening or supersession.

Keep entries compact. Link private proof notes if useful rather than copying
full proofs. Owner approval of exposition does not assign `proved/owner-checked`
or supply a missing mathematical proof. Preserve mathematical evidence status
in the host's ordinary claim records.

## Applying the decision

Before proposing proof expansion or finalizing an exposition finding, locate
any matching decision and compare its scope with the current passage. An active
applicable decision is part of the detail budget and takes precedence over a
shared preference to display every estimate or expand every inference at that
location. Do not expand it, flag the same accepted omission as a new defect,
ask for approval again, or require a full proof just because a fresh reviewer
would prefer more detail. Report it as `accepted brevity` with the decision ID
when a report needs to account for that passage. Do not generate a list of
nonfindings for every entry.

Continue to check the retained statement, definitions, hypotheses, references,
and dependencies. A concrete new mismatch, undefined object, invalid inference,
missing hypothesis, or use of the omitted step beyond the approved interface
may be reported. Identify the new issue, the decision ID, and why that issue
falls outside the approved omission. “A proof is absent”, “I would add more
detail”, or “the reviewer is new” is not a reopening reason. A reader's own
unfamiliarity does not override the recorded intended background.

Preserve actual reading observations. An inference or pause within the accepted
detail budget may remain journal evidence without becoming a blocking expansion
request. If a contract-aware reader still encounters a concrete ambiguity not
covered by the decision, report that distinct ambiguity. Do not relabel a
previous review's literal FAIL as PASS; record the decision-based disposition
of its finding separately.

## Applicability and updates

Carry the decision forward after cosmetic edits, line-number drift, or a label
rename whose identity is established. Record the new locator when necessary;
do not reopen merely because a file hash changed. Changes to the statement,
assumptions, dependencies, role of the omitted step, intended audience, or use
elsewhere require a scoped applicability check. If the original approval still
clearly covers the same argument, record that and continue. Otherwise mark
`recheck-needed`, state the precise new reason, and ask one bounded question
only when the owner choice is needed for the requested work. Continue work
outside that dependency. Do not silently revoke approval or silently expand
the proof while waiting.

A newer explicit owner direction may supersede an entry. Preserve its ID and
source, record the replacement, and avoid parallel conflicting decisions.
Only the writer maintains this durable record; an independent reviewer reports
an applicability concern without editing it.

## Independent-review boundary

The full registry contains writer-only conversation and reasoning. Do not send
it, its raw quotations, previous review history, private proof notes, proposed
repairs, or diagnoses to an isolated reader. The supervisor verifies the
entries against the frozen manuscript and prepares only a neutral proof-detail
contract: decision ID, locator in the allowed manuscript, approved extent,
assumed background, and the interface that must remain explicit. Do not include
proof hints absent from the allowed manuscript or anticipated findings.
This contract is a narrow permitted exception to the ban on owner-decision
state; all other isolation requirements remain in force.

For continuous review, initialize with this general policy only. Freeze the
full contract on the supervisor side before launch, then reveal only entries
whose locators have become available in the issued cumulative segment. Send
them as a named contract sidecar with that segment, never as later-proof content
or as a reaction to the reader's findings. Do not reveal later labels, results,
or a map of future omissions. For editorial review, provide the frozen neutral
contract with the complete manuscript after readiness. For delta review,
provide only entries applicable to the supplied regions and dependencies.

The reviewer may read the explicitly issued contract sidecar, but not search
for the underlying registry. Report the contract identity and applicable IDs
with the reviewed revision. Missing contracts do not imply approval: the writer
must check the registry before launch, and the reviewer must not guess owner
intent. If isolation cannot be preserved, the writer can adjudicate an ordinary
unconditioned finding against the registry afterward; report that limitation
rather than pretending the reader used a contract it never received.

## Finish

In either mode, account for any finding at an approved omission by its decision
ID and current applicability. Close a repeated detail request under the
existing contract when no new issue is shown. Preserve a genuinely new issue
with its exact reason and evidence status. Record newly expressed owner choices
at the same checkpoint as the authorized work, within the recording authority
described above, so the next session can find them. If persistence is blocked,
report it explicitly rather than claiming this checkpoint requirement was met. Do not copy the private registry into manuscript prose or submission
artifacts merely to explain the process.
