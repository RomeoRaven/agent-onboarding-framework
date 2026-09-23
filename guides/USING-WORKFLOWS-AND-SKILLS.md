# Using workflows and skills at a destination

The framework supplies portable methods, not an installed skill library. A destination must name its own workflow, skill, runbook, checker, and task-owner routes in `SOURCES.md` or an adequate existing source map. Bind the actual runtime loader and permissions separately. This guide answers how to choose a method; it does not replace the complete methods in `workflows/`.

## What to load for a new request

1. Follow the native instructions and manifest first. Let the current request select the task and its live owner. Do not make an old handoff today's agenda.
2. Search the destination's declared catalog or known owner for the exact kind of work. An index is discovery; open the owning artifact and check its trigger, status, scope, compatibility, and approval conditions. Draft/pilot/source-only artifacts may be useful candidates but are not automatically installed defaults. Do not bulk-load a library just because it exists.
3. If the runtime offers skills, use its actual loading mechanism. A skill may only route to a complete workflow or provide task-specific capability; distinguish installed from source-only and verify loader behavior rather than infer it from a `SKILL.md` filename. If no skill loader exists, read an authorized workflow directly. Neither path grants new tool permissions.
4. Use the narrowest applicable owner. If two documents seem to own the same behavior, check their source and lifecycle; resolve material conflict with the destination owner before consequential action. An archived copy is provenance, not a competing current procedure.

## Portable methods in this package

- `workflows/task-execution.md` — ordinary request framing, authority, action, proportionate proof, and follow-up. Do not invoke it ceremonially for a small question.
- `workflows/session-continuity.md` — selective startup/recovery and handoff when restart context actually matters.
- `workflows/memory-routing.md` — deciding whether a durable fact belongs in compact pointers, selected procedures, or dated evidence; open work remains with the task owner.
- `workflows/continuous-improvement.md` — right-sized future-path improvement without hijacking the current task.
- `workflows/workflow-and-skill-maintenance.md` — conditional method when creating, changing, adopting, or retiring a repeatable artifact.

These filenames identify generic source material. At a destination, reuse a sufficient local owner instead of copying these methods into five new files by default. Record the approved source revision and the actual local route in the manifest/source map. The installed agent contract should point to selection, not preload all methods.

## Conditional capability questions

- Material operator choice? Reduce facts to the real decision, recommendation, trade-off, exact approval boundary, and what remains if not approved. A concise answer can suffice; use a destination decision-packet workflow only when reread/approval evidence warrants it.
- Verification? Select inspection, smoke, realistic scenario, or costly-boundary test to match the claim. A code-specific TDD, review, browser, deployment, or security skill belongs to the destination/project when that task calls for it.
- Cross-agent work? Distinguish local payload from receiver-visible delivery and acknowledgment; bind the destination's communication owner and prove the receiver can access the material. A local file alone is not delivery.
- New skill? First test whether a workflow or existing skill owns the trigger. Audit external provenance/license and destination compatibility before installing. Keep runtime trigger metadata thin and the durable procedure with one owner.
- Unreliable session? Stop relying on its inferred objective; use the destination's containment/recovery contract. Do not infer that a generic Markdown workflow can quarantine a runtime.

## Installer check

For a fresh realistic task, show the actual path from installed contract to source map to the selected workflow/skill, confirm whether it was injected or opened later, exercise one applicable stop condition, and prove the task result at its owner. Keep this receipt at the destination under `ACCEPTANCE.md`, never in the generic repository.
