# Create destination onboarding files

Use this guide when connecting a generic framework and an authorized private operator profile to one agent destination. Create these files in a single configuration location owned by that destination, not in the generic framework or the operator-profile repository. A destination may keep them in a repository only under its own explicit repository and access policy.

## Before writing

- Identify the destination's existing startup or agent-instruction entrypoint. A human or agent must be able to find the local `ONBOARDING-MANIFEST.md` from there without this conversation. If that entrypoint is governed elsewhere, ask its owner before changing it.
- Obtain authorized access to the framework and, if used, the private operator profile. If no personal profile exists, use `guides/CREATE-OPERATOR-PROFILE.md` and copy its blank template into a private location first. Do not put completed personal answers in the generic repository.
- Identify the destination's governing runtime instructions and real permission boundaries. Markdown files describe sources and limits; they do not override the runtime's instruction hierarchy or enforce filesystem, credential, and service access.
- Inspect existing owner documents before restating rules. If there is already a canonical personal, system, or project source, link it with its authority and scope; do not create a conflicting copy.

## Make the three required files

1. Copy `templates/SYSTEM.md` into the destination configuration location. Record only facts for this destination: harness/runtime, usable tools and limitations, actual permission route, how to access sources, and who can verify them. Confirm each fact through the destination owner or a read-only live check; mark unverified facts as such. Do not record secret values or transient service health here.
2. Copy `templates/SOURCES.md` into the same location. List downstream canonical operational and governing sources a new agent needs, each source's owner and authority scope, how it can be accessed, and what to do if unavailable or contradictory. A private profile's portable representation does not silently replace a reachable authoritative personal source. Do not repeat framework/profile package pins here; keep exact local routes to downstream sources here, not in the generic framework or broadly portable profile.
3. Copy `templates/ONBOARDING-MANIFEST.md` into the same location. Declare the exact framework and operator-profile source/revision, the required local files, optional files if present, authority notes, and the context loading sequence. Point to `SOURCES.md` for downstream routes rather than duplicating them. Use immutable commits/releases when available; otherwise record a stable, owner-verifiable version identifier. Give the startup entrypoint a pointer to this manifest through the destination's normal approved configuration process.

Create `ROLE.md` only if a distinct durable role needs conduct or routing beyond `SYSTEM.md`; point to its owner from the manifest. Keep task context with the project's/task's own source. If you temporarily use `CURRENT.md`, treat it as disposable, not a tracker or durable memory.

## Bootstrap and load

A fresh human starts with the generic `README.md`, locates or creates the destination's manifest using the destination's existing startup entrypoint, and obtains access to each declared source. An agent begins from that same entrypoint, reads only the manifest-declared onboarding files, verifies the declared revisions or stable identifiers, and reports what it actually loaded. A destination-owned adapter can translate Markdown into that harness's context mechanism; the framework does not require an adapter or prescribe a command, model, or provider.

The manifest is an index, not permission to execute. If a required source is missing, its version cannot be verified, the agent lacks access, or two authorities materially conflict, stop before consequential work and ask the owning human/source to resolve it. Do not invent a default profile, paths, permissions, or a role to keep going.

## Accept before consequential use

Using `ACCEPTANCE.md`, keep a compact record at the destination: exact loaded files/versions; unresolved placeholders (none); source/authority explanation; one successful canonical-source lookup; one refused out-of-authority request; one bounded authorized task; and disclosure/permission checks. A fresh human should be able to reproduce bootstrap without prior chat, and a meaningfully different agent/harness or human-led load path should follow the generic instructions without changes to generic files. Failure means fix the owning source and repeat the affected proof; a confident summary is not evidence of actual load or effective runtime permissions.
