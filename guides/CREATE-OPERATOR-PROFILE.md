# Create your operator profile

Use this guide when you do not already have a reliable personal profile for your agents. It is a how-to, not a profile to fill in inside the framework repository. Keep your answers in a private location that you control. You may use one short document rather than a directory of files.

## Start from what you already own

1. List current authoritative sources for your preferences, approval boundaries, terminology, and any stable environment overview. If a rule already has an owner, reference it instead of copying it into a second competing file. Check that the intended agent can actually access that source; if it cannot, create a reviewed, portable representation, mark it as such, and define how you will refresh it. Do not mistake a copy for the live source of truth.
2. Decide who may read the personal profile. A private Git repository is optional; a local private document is sufficient. If you use Git, assume every commit persists and that a later deletion does not erase copies already fetched or published. Keep personal material out of the generic framework's files and history from the first draft onward.
3. Write only stable, task-relevant information. Put exact host paths, available tools, credential mechanisms, local permissions, and live source routes in the destination-owned overlay. Put project rules with their project owners. Do not include passwords, tokens, account identifiers, sensitive locations, logs, sessions, task queues, or raw memory exports in either shared package.

## Questions to answer in your private profile

Answer only what changes the agent's work. Mark unknowns as unknown; do not invent answers or force a questionnaire on the operator.

- Identity and scope: How should the agent address you? Which roles or projects does this profile cover? Is there an existing source it must defer to?
- Communication: How concise or detailed should replies be? What counts as a useful result, a citation, or proof? When should the agent ask rather than assume?
- Authority: Which actions are read-only by default? What requires your explicit approval (for example publication, purchases, messages, destructive actions, service changes)? Can a narrower destination policy make the boundary stricter? What should the agent do if instructions conflict?
- Working agreement: What stable collaboration habits matter across destinations, such as how to report uncertainty, stop at missing authority, or distinguish a question from permission? Avoid claiming that prose overrides the runtime's actual permissions or higher-priority instructions.
- Vocabulary: What terms or abbreviations would another human or agent misunderstand? Include only stable concepts, not live addresses or account names.
- Environment overview (optional): Which broad systems or capability classes help route work? Which owner holds exact operational facts? Do not recreate a machine inventory here.

A minimal profile can have just `Purpose`, `Communication`, `Approval boundaries`, `Terms`, and `Source owners`. Omit empty headings and split files only when different owners, access controls, or lifecycles require it.

## Connect it to a destination

Keep the personal document private and separate from generic materials. The destination manifest should point to the authorized profile source and its exact reviewed revision or stable version, identify any destination-owned authority and overlay files, and say how to obtain them without relying on a previous conversation. A destination-specific loader may translate these Markdown documents for its runtime; that adapter belongs at the destination, not in the generic guide. If an agent cannot access a required profile or verify its intended revision, it must stop before consequential work and ask for the correct source.

A later-loaded file does not automatically outrank an earlier one. The operator owns personal preferences and approvals; the destination owns runtime permissions, paths, and role assignment; projects own their project facts. Explicitly name the owner and stop on an unresolved contradiction. A task request cannot turn an unavailable permission into an available one.

## Check before use

- Have a human review the wording of the personal profile for accuracy and unintended disclosure.
- Check that no private facts entered the generic repository or its Git history. If sensitive content reached others or a remote, stop distribution and assess exposure; rewriting history alone cannot recall their copies.
- From the destination's manifest, ask a fresh human or agent to locate the declared sources, state which owns each rule, identify the revision loaded, refuse one out-of-authority request, and complete one bounded authorized task. Save a compact acceptance record in the destination's own evidence location, not in the generic repository.
- Refresh deliberately when an owner source changes. Do not silently float to a new version or maintain an unreviewed second rulebook.
