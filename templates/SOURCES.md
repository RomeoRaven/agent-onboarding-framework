# Sources — destination-local template

<!-- Copy to the destination's configuration location and replace bindings. List only sources needed here. Exact routes belong in this local copy, not either shared package. -->

## Canonical sources

For each needed downstream source, record one entry in this shape (repeat only as needed):

- Source and owner: `<name; owner>`
  Authority scope: `<what it governs and what it does not>`
  Authorized route and verification: `<exact local route; revision or check method>`
  If unavailable: `<owner to consult and safe stop>`

Include runtime governing sources, a reachable authoritative personal source if distinct from the portable profile, current project/task owners, and any actual workflow, skill, runbook, and checker discovery routes needed for the agent's work. For each, distinguish installed/runtime-loaded from candidate or source-only; record a way to check current status and compatibility. If no native skill library exists, say so and use the authorized workflow route instead. The manifest owns framework/profile package pins and local file declarations; do not repeat them or copy full rules here.

## Conflicts and missing access

Resolve apparent conflicts by named owner and scope, not load order. Apply stricter applicable boundaries; on a material unresolved conflict, missing required source, or unverified revision, stop consequential work and consult `<local resolution owner>`. This index grants no permission.

## Maintenance

Route maintainer: `<local owner>`; read-only route check: `<smallest permitted check>`.
Refresh when a canonical owner moves; do not track open work or live service status here.
