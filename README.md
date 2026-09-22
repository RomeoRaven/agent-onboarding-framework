# Agent onboarding framework

A plain-Markdown method for connecting an agent to an operator and a destination without mixing reusable instructions, private personal context, and local runtime facts. This repository is generic; do not fill in its templates here.

## Start here

1. If you already have an authoritative personal profile, keep it with its existing owner. Otherwise read `guides/CREATE-OPERATOR-PROFILE.md`, copy `templates/OPERATOR-PROFILE.md` to a private location, and complete only the useful sections there.
2. Read `guides/CREATE-DESTINATION-FILES.md`. With the destination owner, copy and complete `templates/SYSTEM.md`, `templates/SOURCES.md`, and `templates/ONBOARDING-MANIFEST.md` in one destination-owned configuration location. Do not publish completed local copies here.
3. Put a pointer to the local manifest in that destination's existing startup entrypoint through its normal approved owner process. A new human or agent must be able to find the manifest without prior conversation. Consult `ONBOARDING.md` for authority and failure handling.
4. Run the manual checks in `ACCEPTANCE.md` before relying on the onboarding for consequential work. Keep the results at the destination.

Neither this framework nor the profile grants tool access. The destination runtime and its actual permissions remain authoritative for what can be done. Missing access or a contradictory governing source is a stop condition, not permission to guess. You can use these documents with a human or any agent/harness that can read Markdown; adapt loading at the destination, not here.
