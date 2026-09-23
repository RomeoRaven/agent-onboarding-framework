# Agent onboarding framework

A plain-Markdown method for connecting an agent to an operator and a destination without mixing reusable instructions, private personal context, and local runtime facts. This repository is generic; do not fill in its templates here.

## Start here

1. If you already have an authoritative personal source, keep it with its owner. Otherwise read `guides/CREATE-OPERATOR-PROFILE.md`, copy `templates/OPERATOR-PROFILE.md` privately, and have its wording reviewed. For a generic walkthrough, make a fictional private profile; do not use someone else's candidate profile.
2. Read `guides/CREATE-DESTINATION-FILES.md`. With the destination owner, copy/adapt `templates/AGENTS.template.md` as a destination `AGENTS.md` or native contract, plus `templates/SYSTEM.md`, `templates/SOURCES.md`, and `templates/ONBOARDING-MANIFEST.md`. Use `templates/START_HERE.md` only when an intermediate pointer is useful. `templates/SOUL.md` and `templates/MEMORY.md` are optional examples, not an installation checklist. Fill only the genuinely local bindings in the complete templates; never fill them here.
3. Bind the installed contract through the destination's real native loader. Record and exercise each hop to the local manifest in a fresh session. Consult `ONBOARDING.md` for authority, the portable `workflows/memory-routing.md` and `workflows/session-continuity.md` when relevant, and the guides for adaptation questions. Root `AGENTS.md` governs work in this framework repository only.
4. Run `ACCEPTANCE.md` before relying on consequential onboarding. Prove injected context separately from files opened afterward, source lookup, a refusal, a bounded task, and an independent human/harness path; keep results at the destination.

Neither this framework nor the profile grants tool access. The destination runtime and its actual permissions remain authoritative for what can be done. Missing access or a contradictory governing source is a stop condition, not permission to guess. You can use these documents with a human or any agent/harness that can read Markdown; adapt loading at the destination, not here.
