# Workflow and skill maintenance — portable method

Use when creating, changing, adopting, or retiring repeatable agent instructions. This is an on-demand maintainer workflow, not a requirement to install a skill system. The destination owns its runtime skill loader, artifact locations, lifecycle policy, approvals, and authoritative catalogs. Do not replace existing local procedures with this document.

## Decide whether an artifact is needed

1. Name the recurring task and the future agent's actual trigger. Inspect the current owner files, workflow/skill indexes, project instructions, and related artifacts before designing another owner. Check whether the work belongs in a task, a source reference, a procedure, a checker, or history instead.
2. Freeze the simplest complete design: operator action, input, usable result, owner, allowed action boundary, proof, later maintenance, and non-goals. Compare at least the alternatives of improving an existing owner, adding a link, or creating nothing. Do not add a lifecycle queue or review gate without a failure it prevents.
3. Choose the form by job: workflow for judgment and branches; runbook for concrete operations and rollback; checklist for bounded verification; reference for stable facts; script for deterministic action/check; skill for a runtime-specific trigger or bundled capability. A thin skill can point to a workflow owner; it should not duplicate that owner's body. The framework's generic Markdown is not proof a destination runtime loaded any skill.

## Reconcile and change

- Inspect existing local instructions before editing. Identify their owner, scope, source authority, loader behavior, status, and rollback route. Prefer keep, link, or a narrow owner-approved edit over a competing file. Never overwrite `AGENTS.md` or a skill solely because a generic template has the same purpose.
- Check a candidate's provenance and license before installation, especially when obtained externally. Treat a mirrored, generated, archived, draft, or pilot copy as a candidate within its limits, not the active authority. Do not import an entire library to obtain one method.
- Write a complete procedure when one is warranted: when to use it; inputs/owners; ordered steps and alternatives; approval/stop conditions; result/proof; where follow-up and maintenance live. For a trigger skill, state the trigger, supported runtime, and exact procedure owner. Place source detail with its owner rather than copying it into every loader.
- If a change crosses protected, shared, public, service, retention, or another destination-owned boundary, seek the required owner approval before applying it. A suggestion or successful local draft does not authorize rollout or install.

## Verify and maintain

Test discovery and use, not just file existence: from a fresh relevant task, can an agent find the artifact, distinguish active/default from candidate, load it in the actual runtime when applicable, follow its stop rule, and produce the intended result? Check that existing local instructions still work. Update the destination's real index/loader link and lifecycle record only under its owner policy; keep generated copies downstream of their source. Record material use or a concrete gap with the owning artifact or task, not a receipt for every routine load. Merge or retire duplicates through their owner rather than leaving two apparently current procedures.

Do not promote an untested draft to a universal default, claim skill installation grants tool permissions, or infer compatibility from a matching filename. The exit state is one current owner with a usable discovery path and proportionate proof—or a clear no-change/blocked decision.
