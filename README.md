# Agent onboarding framework

A plain-Markdown method for connecting an agent to an operator and a destination without mixing reusable instructions, private personal context, and local runtime facts. This repository is generic; do not fill in its templates here.

In plain terms: the framework describes *how* to onboard, the operator controls personal preferences, and the destination controls the actual agent setup and permissions. An agent cannot use a file just because it exists in this repository.

## Start here

1. Keep personal context with its existing private owner. If none exists, use `guides/CREATE-OPERATOR-PROFILE.md` and have the result reviewed. For a generic walkthrough, use a fictional private profile—not another person's candidate profile.
2. Read `ONBOARDING.md` and `guides/CREATE-DESTINATION-FILES.md` for the owner boundaries and binding procedure.
3. Inspect the destination's existing agent instructions, system/source owners, persona, and memory. Preserve sufficient local files before copying anything. `templates/AGENTS.template.md` is reference material, not a replacement; optional START_HERE, SOUL, and MEMORY examples are not an install checklist. Root `AGENTS.md` governs this repository only.
4. Bind the retained or approved local contract through the destination's *actual* runtime loader, then link it to the local manifest and source map. Follow `guides/USING-WORKFLOWS-AND-SKILLS.md` to choose a task-relevant method on demand; do not preload the library or put completed local bindings here.
5. Run the destination checks in `ACCEPTANCE.md` before consequential reliance. In a fresh session, separate observed runtime-injected context from later manual reads; prove source lookup, a refusal, and a bounded task. A separate human/harness path is required before claiming cross-harness portability. Keep results with the destination.

Neither this framework nor the profile grants tool access. The destination runtime and its actual permissions remain authoritative for what can be done. Missing access or a contradictory governing source is a stop condition, not permission to guess. You can use these documents with a human or any agent/harness that can read Markdown; adapt loading at the destination, not here.

## Optional static preflight and proof levels

Run `python3 scripts/check-onboarding.py --package .` to check literal framework-relative Markdown references. Once a destination has its own completed manifest, `python3 scripts/check-onboarding.py --manifest <completed-local-file>` checks for unfinished binding placeholders in that one file. These read-only checks cannot observe native loading or permissions. `ACCEPTANCE.md` separately tests one real destination and an independent human/harness path; until those are exercised, describe the package as available, not proven at a destination or across harnesses.
