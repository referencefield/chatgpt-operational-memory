# Runtime Front Door

Status: active  
Purpose: give a fresh ChatGPT session one small place to start, then route only to durable state that can materially affect the task.

This file is the **runtime protocol authority**. Do not load the whole repository. Details live in `OPERATIONS.md`; privacy/security in `SECURITY.md`; upgrades in `MIGRATIONS.md`.

## Activation

Treat **set up**, **activate**, **initialize**, **wake up**, or **start using** operational memory plus an identified repository as activation intent. After a BLOCKED attempt in the same conversation, **“Retry setup.”** means rerun against that same repository; if its identity is no longer available, ask only for its URL.

The user need not mention protocol files, repository IDs, CRUD, or a handshake.

1. confirm the exact working repository, default branch, visibility, and GitHub repository ID; owner/name may be arbitrary;
2. require the working copy to be **private** before storing personal/project state;
3. retrieve `PROTOCOL.yaml`, this file, declared root memory files, and `PROJECTS.md`; verify structure without broad-loading unrelated content;
4. using the selected `@GitHub` plugin's actual actions, verify reversible `SETUP-TEST.md` create/read/update/read/delete plus deletion readback, using the current version when available. A separate read-only GitHub app does not prove `@GitHub` is read-only; missing required write actions means BLOCKED;
5. create no durable state merely to mark activation;
6. return READY or BLOCKED below.

The setup URL selects the exact repository even when GitHub can access many others. Never substitute another repository. Future bootloader routing uses its numeric ID.

### READY

Begin **`Operational memory: READY`**. Show only useful status such as repository, Private, GitHub read/write verified, structure healthy, and ready to use. Do not make the numeric repository ID something the user must understand or copy separately.

Then say **One final step:** and provide the completed Custom Instructions bootloader from `SETUP.md` with the verified ID already filled in. The user copies it as-is.

### BLOCKED

Begin **`Operational memory: BLOCKED`**. Report only the first actionable blocker in this order: exact repository access, Private visibility, required write actions, write/readback verification, diagnostic cleanup, protocol structure.

Use plain language, give exactly one **Fix:**, and end **Then tell me `Retry setup.`** Hide IDs, blob/version details, branch diagnostics, and protocol jargon unless requested.

Activation is idempotent. Cloning/naming alone is not activation.

For future routing, prefer repository ID over owner/name. Resolve it before retrieval. A normal rename requires no migration or bootloader edit. If the ID does not resolve, fail closed rather than guessing by name.

Without a persistent bootloader, offer:

`@GitHub Use operational memory from <repository URL>.`

Repository resolution and front-door routing are internal, not user syntax.

## Normal route

1. Resolve the configured repository ID to its current owner/name when available, then retrieve `PROTOCOL.yaml`.
2. Identify the user's intent.
3. If durable repository state cannot materially change the task, use **no-repository-context**.
4. Scope before retrieval:
   - global current/decisions -> root `CURRENT.md` and/or `DECISIONS.md`;
   - global durable facts/definitions -> root `KNOWLEDGE.md` when relevant;
   - project-specific -> `PROJECTS.md`, then the matching `PROJECT.md` and only files it routes to;
   - working style -> `WORKING_STYLE.md` only when materially relevant.
5. Do not scan every project/file. If a named project is not found, check `PROJECTS.md` before free-form search. A search miss is not proof of absence.
6. Stop expanding context once the task can be handled correctly.

## Authority

When repository sources conflict, use this order unless a higher-level rule requires otherwise:

1. current explicit user instruction;
2. current verified project-local state and active project decisions;
3. current verified global state and active global decisions;
4. relevant verified durable knowledge not stale/superseded;
5. applicable active `WORKING_STYLE.md` entries;
6. historical/superseded repository state;
7. native ChatGPT memory, chat recollection, or model inference.

Working style cannot override current instructions/decisions or suppress honest evaluation, material disagreement, correction, material risk flagging, uncertainty disclosure, or applicable safety behavior. Stale knowledge does not override current verified state. Git history is evidence, not active authority. Native memory may help but does not override verified durable state.

## Conservative persistence watch

During repository-backed work, notice clear non-sensitive changes that would leave durable state materially wrong/incomplete if the session ended now.

Good candidates: explicitly changed objective/constraint/status/next step, finalized decision, direct durable correction, or explicit durable working preference.

When durable intent is explicit and routing unambiguous, persist under normal write/verify rules unless ask-first is active. Ask when intent/future relevance is inferred, material is sensitive, routing is ambiguous, or structure must expand.

Do not persist brainstorming, possibilities, casual conversation, one-off preferences, anything the user says not to persist, or a working-style preference that would make future work less honest about errors, risks, uncertainty, or disagreement.

## Persistence routing gate

Route durable material in this order:

1. existing source of record;
2. global `CURRENT.md`;
3. global `DECISIONS.md`;
4. global `KNOWLEDGE.md`;
5. `WORKING_STYLE.md`;
6. correct registered project through `PROJECTS.md`;
7. **`UNROUTED / no legitimate home`** -> do not invent a file.

Global files are cross-project. Project-specific material belongs behind a project front door. Durable knowledge should be supported, scoped, and freshness-aware. Working style is collaboration preference, not biography/profiling.

“Record this in operational memory” authorizes correct routing, not arbitrary file creation.

## Project and structure triggers

Do not create a project for a one-off question. A project is justified when the user clearly identifies ongoing work, it spans sessions with its own state/decisions/knowledge, project material would otherwise leak globally, or the topic repeatedly needs its own retrieval boundary. Ask when ambiguous.

For creation procedure, use `OPERATIONS.md`. No durable project folder may exist without a `PROJECTS.md` registry entry.

A new durable file/category is exceptional. Require a distinct role, recurrence, retrieval trigger, defined authority, navigation from an existing front door/index, human visibility, and any required manifest/migration update. Otherwise use an existing home or report `UNROUTED`.

## Write safety

A **consequential write** changes declared durable memory, routing, authority, project structure, or protocol configuration. Temporary reversible diagnostics such as `SETUP-TEST.md` are excluded, though activation still requires their readback and cleanup verification.

For consequential writes:

`read current target(s) -> authorize/route -> write -> reread -> verify intended state`

Use the current blob/version as update precondition when available. On stale/conflicting writes, reread and reconcile; never force or blindly retry.

If one intent changes multiple durable files, use a **write-set** and verify the cross-file postcondition before success. Detailed procedure lives in `OPERATIONS.md`.

Tool acknowledgement is not persistence proof. Readback is required. Never invent a commit ID.

## Failure and growth signals

Default to **fail closed, fail loud, preserve the last known good state, and provide a recovery path**.

Examples:
- required retrieval missing -> report incomplete/partial retrieval;
- configured repository ID unresolved -> stop rather than guess;
- no legitimate home -> `UNROUTED / no legitimate home`;
- ambiguous durable decision/preference -> ask;
- stale write -> reread/reconcile;
- unverified write -> `not verified`;
- partial write-set/project creation -> report temporary inconsistency and reconcile;
- required GitHub write actions unavailable -> state changes were not persisted.

For health/scale checks, use `OPERATIONS.md` and report **`Healthy | Watch | Outgrowing the template`**. Soft budgets are warnings, not deletion targets.

## Load details only when needed

- `OPERATIONS.md` -> project creation, persistence detail, write-sets, closeout, health/update checks, recovery, maintenance, scale
- `SECURITY.md` -> privacy, secrets, repository-content boundary, Git hardening
- `MIGRATIONS.md` -> release-to-release upgrades
- `EVALS.md` -> behavioral/adversarial scenarios

This front door should remain sufficient for ordinary routing.
