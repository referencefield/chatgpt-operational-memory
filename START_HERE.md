# Runtime Front Door

Status: active  
Purpose: give a fresh ChatGPT session one small place to start, then route to only the durable state that can materially affect the current task.

This file is the **runtime protocol authority**. Do not begin by loading the whole repository. Detailed procedures live in `OPERATIONS.md`; privacy/security in `SECURITY.md`; release upgrades in `MIGRATIONS.md`.

## Activation handshake

Treat **set up**, **activate**, **initialize**, **wake up**, or **start using** operational memory plus an identified repository as activation intent. If a prior attempt in the current conversation was BLOCKED, **“Retry setup.”** means rerun against that same exact repository after the user fixes the reported problem. If the repository cannot be established from the current conversation, ask only for its URL.

The user does not need to mention `START_HERE.md`, `PROTOCOL.yaml`, repository IDs, CRUD, or an activation handshake. Those are implementation details.

1. confirm the exact working repository, default branch, visibility, and GitHub repository ID; owner/name may be arbitrary;
2. require the personal working copy to be **private** before storing personal/project state;
3. retrieve `PROTOCOL.yaml`, this file, the declared root memory files, and `PROJECTS.md`; verify structure without broad-loading unrelated content;
4. using the selected `@GitHub` plugin's actual actions, verify read/write with reversible `SETUP-TEST.md`: create -> reread -> update using the current version when available -> reread -> delete -> verify deletion. Do not infer that `@GitHub` is read-only from a separate GitHub app; if required write actions are absent, BLOCKED;
5. create **no** project, decision, knowledge, working-style, or current-state entry merely to mark activation;
6. return **READY** or **BLOCKED** using the user-facing rules below.

The setup URL selects the exact working repository even when GitHub can access many others. Never substitute another repository. After activation, bootloader routing uses that repository's numeric ID.

### READY response

Begin **`Operational memory: READY`** and show only useful human-facing status such as repository, Private, GitHub read/write verified, structure healthy, and ready to use. Do **not** make the numeric repository ID something the user must understand or copy separately.

Then say **One final step:** and provide the completed Custom Instructions bootloader from `SETUP.md` with the verified repository ID already filled in. The ID may appear inside that copyable instruction because it is the routing key, but do not require the user to interpret or manually edit it.

### BLOCKED response

Begin **`Operational memory: BLOCKED`**. Report only the first actionable blocker in this order: exact repository access, private visibility, required write actions, write/readback verification, diagnostic cleanup, protocol structure.

Use plain language and give exactly one next action under **Fix:**. End with **Then tell me `Retry setup.`** Do not dump repository IDs, blob/version details, branch diagnostics, or protocol jargon unless the user asks for technical detail.

Activation is idempotent. Cloning/naming the repository alone is not activation.

For future routing, prefer the GitHub repository ID over owner/name. Resolve it to the current owner/name before retrieval. A normal repository rename therefore requires no protocol migration or bootloader edit.

If a configured repository ID does not resolve, fail closed. Do not guess from a similar repository name.

If no persistent bootloader is configured, offer the simple fallback from `SETUP.md`:

`@GitHub Use operational memory from <repository URL>.`

Repository resolution and front-door routing are internal, not user syntax.

## Normal route

1. Resolve the configured GitHub repository ID to the working repository's current owner/name when an ID is available, then retrieve `PROTOCOL.yaml`.
2. Identify the user's current intent.
3. Decide whether durable repository state can materially change the answer/action. If not, use **no-repository-context** and continue normally.
4. Scope before retrieval:
   - global/cross-project current state or decisions -> root `CURRENT.md` and/or `DECISIONS.md`;
   - global/cross-project durable facts/definitions -> root `KNOWLEDGE.md` when relevant;
   - project-specific -> `PROJECTS.md`, then the matching project's `PROJECT.md` and only the minimum files it routes to;
   - working-style/calibration -> `WORKING_STYLE.md` only when it can materially affect how work should be handled.
5. Do not scan every project/file. If a named project is not found, check `PROJECTS.md` before free-form search. A search miss is not proof of absence.
6. Stop expanding context once the task can be handled correctly.

## Authority

When repository sources conflict, use this order unless a higher-level rule requires otherwise:

1. current explicit user instruction;
2. current verified project-local state and active project decisions;
3. current verified global state and active global decisions;
4. relevant verified durable knowledge that is not stale/superseded;
5. applicable active `WORKING_STYLE.md` entries;
6. historical/superseded repository state;
7. native ChatGPT memory, chat recollection, or model inference.

Working style does not override current instructions/decisions. It also cannot suppress honest evaluation, material disagreement, correction of errors, material risk flagging, uncertainty disclosure, or applicable safety behavior. Stale knowledge does not override current verified state. Git history is evidence, not active authority by itself. Native ChatGPT memory may be useful context, but it does not override current verified durable repository state.

## Conservative persistence watch

During repository-backed work, notice clear non-sensitive changes that would leave durable state materially wrong/incomplete if the session ended now.

Good candidates include an explicitly changed objective/constraint/status/next step, a finalized decision, a direct durable correction, or an explicit durable working preference.

When durable intent is explicit and routing is unambiguous, persist under the normal write/verify rules unless the user selected ask-first behavior. Ask first when intent/future relevance is inferred, material is sensitive, routing is ambiguous, or structure must expand.

Do not persist brainstorming, possibilities, casual conversation, one-off preferences, or anything the user says not to persist. Do not persist a working-style preference whose effect would be to make future work less honest about material errors, risks, uncertainty, or disagreement.

## Persistence routing gate

Route durable material in this order:

1. existing source of record;
2. global `CURRENT.md`;
3. global `DECISIONS.md`;
4. global `KNOWLEDGE.md`;
5. `WORKING_STYLE.md`;
6. the correct registered project through `PROJECTS.md`;
7. **`UNROUTED / no legitimate home`** -> do not invent a file.

Global files are for cross-project material. Project-specific material belongs behind a project front door. Durable knowledge should be supported, scoped, and freshness-aware. Working style is for collaboration preferences, not biography or profiling.

A request such as **“record this in operational memory”** authorizes correct routing, not arbitrary file creation.

## Project and structure triggers

Do not create a project for a one-off question. A project is justified when the user clearly identifies ongoing work, the work spans sessions with its own state/decisions/knowledge, project-specific material would otherwise leak into global files, or the same topic repeatedly needs its own retrieval boundary. Ask when project status is ambiguous.

For project creation procedure, use `OPERATIONS.md`. No durable project folder may exist without a `PROJECTS.md` registry entry.

A new durable file/category outside declared structure is exceptional. Before creating one, require: a distinct role, expected recurrence, a future retrieval trigger, defined authority, navigation from an existing front door/index, human visibility, and any required manifest/migration update. Otherwise keep the material routed to an existing home or report `UNROUTED`.

## Write safety

A **consequential write** is any write that changes declared durable memory, routing, authority, project structure, or protocol configuration. Temporary reversible diagnostics such as `SETUP-TEST.md` are excluded from this term, though their activation procedure still requires readback and cleanup verification.

For consequential writes:

`read current target(s) -> authorize/route -> write -> reread -> verify intended state`

Use the current blob/version as the update precondition when available. On stale/conflicting writes, reread and reconcile; never force or blindly retry.

If one intent changes multiple durable files, use a **write-set** and verify the complete cross-file postcondition before claiming success. Detailed write-set procedure lives in `OPERATIONS.md`.

A tool acknowledgement is not persistence proof. Readback is required for consequential state. Never invent a commit ID.

## Failure and growth signals

Default to **fail closed, fail loud, preserve the last known good state, and provide a recovery path**.

Examples:
- required retrieval missing -> report incomplete/partial retrieval;
- configured repository ID cannot be resolved -> stop rather than guess a replacement repository;
- no legitimate home -> `UNROUTED / no legitimate home`;
- ambiguous durable decision/preference -> ask;
- stale write -> reread/reconcile;
- unverified write -> report `not verified`;
- partial write-set/project creation -> report temporary inconsistency and reconcile;
- required GitHub write actions unavailable -> state that changes were not persisted.

For health/scale checks, use `OPERATIONS.md` and report **`Healthy | Watch | Outgrowing the template`**. Soft budgets are warning indicators, not deletion targets.

## Load detailed procedures only when needed

- `OPERATIONS.md` -> project creation, persistence detail, write-sets, closeout, health/update checks, recovery, maintenance, scale
- `SECURITY.md` -> privacy, secrets, repository-content boundary, Git hardening
- `MIGRATIONS.md` -> release-to-release upgrade guidance
- `EVALS.md` -> behavioral/adversarial scenarios

This front door should remain sufficient for ordinary routing. Load detailed documents only when the task requires them.
