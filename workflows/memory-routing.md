# Memory routing — portable method

Use when deciding whether a fact or lesson should persist across sessions. The destination owns actual storage, loader behavior, access, and task tracking; this method does not create a shared memory database or grant authority.

## Choose the owner, then the tier

1. Identify the current authoritative source and intended future reader. If a preference, runtime fact, project rule, task, or procedure already has an owner, point to it rather than copy it into another memory store. Do not admit unverified, sensitive, or transient claims as standing guidance.
2. Tier 1 — tiny every-session identity/safety/routing pointers the runtime actually loads. Include only durable facts necessary before task selection and links to owners; verify native load and refresh semantics. Do not include workflow bodies, task state, raw logs, or long histories.
3. Tier 2 — selected-on-demand governing documents, indexed skills, workflows, runbooks, and checks. A skill can trigger loading; the named owner document supplies the method. Select for the current request, verify provenance/status/compatibility, then use the smallest needed portion. Do not export a source system's whole index as generic policy.
4. Tier 3 — dated session notes, references, reports, receipts, and handoffs. Store only useful continuity/evidence, with date, provenance, owner links, what was observed, limitations, and sensitivity. Read when recovery or proof calls for it; check old claims against live owners. A latest pointer may aid discovery but cannot choose the next task.

A dated file is Tier 3 by function here even if an older system called it something else. Classify by purpose, not filename. Open commitments live in the destination's actual task owner, not in a memory note.

## Admission and refresh

Before writing, ask: Will a future session need this? Is it stable, sourced, safe to retain, and placed with the right owner? If not, leave it in the current conversation or a dated evidence record. Promote a repeated, verified procedure to its workflow owner only through that owner's review; replace any stale pointer rather than retaining parallel rules. Refresh Tier 1 sparingly and deliberately, respecting the native runtime's snapshot/restart behavior.

## Failure and proof

If the owner, sensitivity, revision, or access route is unclear, do not promote the claim. Mark uncertainty at the narrowest permissible evidence surface and ask its owner. Verify a saved pointer can locate the intended current source without exposing private material; do not infer successful runtime injection from a file write.
