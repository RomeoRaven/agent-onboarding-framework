# Better prompt — portable method

Use when an operator asks to improve a prompt, turn a rough idea into an instruction for an agent to run later, or explicitly invokes a locally defined prompt-refinement shortcut. Do not infer a shortcut's meaning without checking the destination's own convention. This method prepares an execution request; it does not execute that request.

## Outcome and boundary

Produce a paste-ready prompt that tells its recipient what result to achieve, where to find authoritative context, what is in and out of scope, what constraints apply, and how to know when to stop. The current operator request and destination permissions control all later actions. The improved prompt cannot grant authority that the recipient lacks, and writing it is not approval to run it. If the operator explicitly requests both improvement and execution, treat those as separate stages and execute only the separately authorized scope.

Use a specialized destination method instead when the operator specifically asks for a native goal, planning, review, or handoff format. Do not force every request into a long-running agent run or create a tracker simply to hold a prompt.

## Method

1. Read the rough text as intent, not as a final command. Identify the desired result, intended recipient, relevant context, and any already-stated boundaries. If the input is code, prose, or a design to edit rather than a request to improve instructions, use the corresponding editing method instead.
2. Select the smallest fitting target: a direct task for bounded execution, a planning/decision request for unresolved choices, a research/evaluation request for evidence and recommendation, a handoff for another actor, or a sustained-work request only when depth and recovery actually matter. Follow a destination-native format only if it exists and is requested or genuinely needed.
3. Supply the useful missing pillars without inventing facts: objective and usable outcome; source/owner lookup; scope and exclusions; constraints and approval gates; verification or definition of done; expected output; and stop conditions. For a substantial sustained-work request, preserve the requested depth with a finish line and an appropriate time, batch, surface, or blocker boundary rather than allowing the first small step to count as completion.
4. Ask a targeted question only when the answer materially changes outcome, owner, authority, safety, execution surface, or validation. Otherwise make a conservative, visible assumption. If a required source or owner cannot be identified, instruct the recipient to locate it and stop before consequential action if it remains unavailable; do not invent a path or permission.
5. Return the paste-ready prompt and a short note on assumptions (only if needed), the material improvement, and the recommended target surface. Keep the prompt proportional. For a broad, multi-section, research-heavy, or otherwise complex sustained-work prompt, use a file-backed packet by default rather than dumping the full packet into chat: when file creation is authorized within this request, save it at the destination's durable owner and return a verified, concise launcher (normally one or two lines, at most 500 characters). If that owner or write authority is unavailable, do not invent a file or claim it was saved; provide a compact version or ask for the missing route. For smaller prompts, return the complete prompt in the answer.

## Output shape

Use only sections the recipient needs. A substantive task may look like:

```text
Objective: <observable result and why it matters>
Context and owner lookup: <known source, or how to identify the current owner>
Scope: <what to do and what not to change>
Constraints and approvals: <applicable boundaries; no inferred permission>
Definition of done: <evidence of the usable result>
Stop conditions: <missing authority, material ambiguity, or out-of-scope work>
Response: <requested human-facing output>
```

After the prompt, briefly state any assumption and whether it is ready to run or requires one answer. This note is not part of the executable prompt unless it changes the recipient's instructions.

## Validation and stop

A good result is paste-ready, preserves the operator's intent and depth, gives the next actor a workable owner-lookup path and proportionate proof, and does not smuggle in new authority. Test it mentally against a narrow task, a broad sustained request, and an ambiguous owner: none should silently turn into an unauthorized implementation. Stop after producing the prompt unless a distinct current instruction explicitly authorizes execution. When essential facts cannot be safely assumed, stop with the highest-value question rather than fabricating a complete-looking prompt.
