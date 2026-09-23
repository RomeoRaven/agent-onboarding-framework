# Create destination onboarding files

Use this guide when connecting a generic framework and an authorized private operator profile or authoritative personal source to one agent destination. Keep the manifest, system facts, and source map together where practical in a destination-owned location; put the installed contract, persona, or memory at their verified native loader locations if required. None belongs in the generic framework or another operator's profile repository. A destination may commit local files only under its own explicit repository and access policy.

## Before writing

- Identify the destination's existing startup or agent-instruction entrypoint. A human or agent must be able to find the local `ONBOARDING-MANIFEST.md` from there without this conversation. If that entrypoint is governed elsewhere, ask its owner before changing it.
- Obtain authorized access to the framework and, if used, the private operator profile. If no personal profile exists, use `guides/CREATE-OPERATOR-PROFILE.md` and copy its blank template into a private location first. Do not put completed personal answers in the generic repository.
- Identify the destination's governing runtime instructions and real permission boundaries. Markdown files describe sources and limits; they do not override the runtime's instruction hierarchy or enforce filesystem, credential, and service access.
- Inspect existing owner documents before restating rules. If there is already a canonical personal, system, or project source, link it with its authority and scope; do not create a conflicting copy.

## Make and bind the required files

1. Copy `templates/AGENTS.template.md` as an installed `AGENTS.md`, or adapt its complete contract to the harness's native instruction file. Record its actual location and native loader/config mechanism. The framework's root `AGENTS.md` is for maintaining this repository, not the destination. In the installed contract, fill the destination identity/owner and the exact next link to `ONBOARDING-MANIFEST.md` directly or through `START_HERE.md`.
2. Copy `templates/SYSTEM.md` into the destination configuration location. Record only verified durable runtime, tools, permission boundaries, native loader evidence route, and local owner. Do not record secret values or transient health.
3. Copy `templates/SOURCES.md` into the same location. List downstream canonical governing and operational sources with owner, scope, access route, and failure behavior. A private portable profile does not silently replace a reachable authoritative personal source. Package pins belong in the manifest, not here.
4. Copy `templates/ONBOARDING-MANIFEST.md` into the same location. Declare exact framework/personal source revisions, required local files, conditional files if installed, and the actual loader -> installed contract -> manifest hops. Use immutable commits/releases when available; otherwise record owner-verifiable identifiers. Point to `SOURCES.md` for downstream sources. Bind the native entrypoint through its approved owner/configuration process, not by relying on a filename.

Copy `templates/START_HERE.md` only when the contract needs a separate startup pointer. Copy `templates/SOUL.md` only for a distinct durable role and a verified persona loader; copy `templates/MEMORY.md` only for a real compact pointer need and a verified native Tier 1 store. Adapt filenames to the harness. Do not install optional files just to complete a template list. Keep task context with its project/task owner; use `workflows/memory-routing.md` and `workflows/session-continuity.md` for dated records and handoffs.

## Bootstrap and load

A fresh human starts with generic `README.md`, determines the destination's actual loader and owner, installs only authorized local files, and follows every explicit link from the native entrypoint through the contract to the manifest. An agent in a fresh session distinguishes files injected by the runtime (including unlisted native overrides) from files fetched later. Record observable loader/config evidence and verified revisions. If injection cannot be observed, mark it unverified; manual access alone is not proof of auto-loading. A destination-owned adapter may translate Markdown into its harness's context mechanism; no generic adapter, command, model, or provider is required.

The manifest is an index, not permission to execute. If a required source is missing, its version cannot be verified, the agent lacks access, or two authorities materially conflict, stop before consequential work and ask the owning human/source to resolve it. Do not invent a default profile, paths, permissions, or a role to keep going.

## Accept before consequential use

Using `ACCEPTANCE.md`, keep a compact record at the destination: observed injection versus later reads; exact sources/versions; unresolved placeholders (none); authority explanation; one source lookup; one refusal; one bounded task with readback; and disclosure/permission checks. For generic fresh-human proof, use a fictional/private profile created from the operator guide, not another person's unapproved candidate. A different human/harness path should follow the method without changing generic files. Failure means fix the owning source and repeat affected proof; a confident summary is not evidence of actual load or runtime permissions.
