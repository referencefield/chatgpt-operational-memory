# Runtime Front Door

Status: active  
Purpose: small entry point for routing to durable state that can materially affect the task.

This file is the **runtime protocol authority**. Do not load the whole repository. Details: `OPERATIONS.md`; security: `SECURITY.md`; upgrades: `MIGRATIONS.md`.

## Activation

Treat **set up**, **activate**, **initialize**, **wake up**, or **start using** operational memory plus an identified repository as activation intent. After BLOCKED in the same conversation, **“Retry setup.”** reruns against that repository; if identity is unavailable, ask only for its URL.

The user need not mention protocol files, IDs, CRUD, or a handshake.

Supported release: **paid ChatGPT plan** plus write-capable `@GitHub`; Free is unsupported. Paid status alone does not prove the required plugin/actions exist.

1. confirm exact repository, default branch, visibility, and GitHub repository ID;
2. require the working copy to be **private** before storing personal/project state;
3. retrieve `PROTOCOL.yaml`, this file, declared root memory files, and `PROJECTS.md`; verify structure without broad-loading unrelated content;
4. using selected `@GitHub` actions, verify reversible `SETUP-TEST.md` create/read/update/read/delete plus deletion readback, using current version when available. A separate read-only GitHub app does not prove `@GitHub` is read-only; missing required write actions means BLOCKED;
5. create no durable state merely to mark activation;
6. return READY or BLOCKED below.

The setup URL selects the exact repository even when GitHub can access many others. Never substitute another repository. Future bootloader routing uses its numeric ID.

### READY

Begin **`Operational memory: READY`**. Show only useful status such as repository, Private, GitHub read/write verified, structure healthy, and ready to use. Keep the numeric ID out of the user's mental model.

Then say **One final step:** and provide the completed `PROTOCOL.yaml` bootloader with the verified ID filled in. Tell the user:
- Web/Desktop: **Settings → Personalization → Custom Instructions**.
- Mobile: **Settings → Customize ChatGPT → Custom Instructions**.
- enable customization; paste **at the top above existing instructions**; keep existing instructions; save.

The user copies it as-is. Do not ask them to edit, understand, or separately record the ID.

### BLOCKED

Begin **`Operational memory: BLOCKED`**. Report only the first actionable blocker: supported setup when known, repository access, Private visibility, write actions, write/readback, cleanup, then protocol structure.

Use plain language, give exactly one **Fix:**, and end **Then tell me `Retry setup.`** Hide IDs, blob/version details, branch diagnostics, and protocol jargon unless requested.

Activation is idempotent. Cloning/naming alone is not activation.

For future routing, prefer repository ID over owner/name. Resolve it before retrieval. Rename requires no migration or bootloader edit. If the ID does not resolve, fail closed rather than guessing by name.

Without a persistent bootloader, offer:

`@GitHub Use operational memory from <repository URL>.`

Repository resolution/front-door routing are internal, not user syntax.

Operational memory has **two runtime triggers**: prior durable state may materially affect the task, or the conversation creates/changes clear future-governing state that should persist. The second does not require prior repository relevance. The bootloader tells ChatGPT when to use `@GitHub`; it is not proof the plugin ran. Claim retrieval/persistence only after actual GitHub evidence.

## Normal route

1. Resolve configured repository ID to current owner/name when available, then retrieve `PROTOCOL.yaml`.
2. Identify user intent.
3. If neither prior durable state nor a clear new durable change can materially affect future work, use **no-repository-context**. A conversation may enter operational memory later when a persistence trigger emerges.
4. Scope before retrieval:
   - global current/decisions -> root `CURRENT.md` and/or `DECISIONS.md`;
   - global durable facts/definitions -> root `KNOWLEDGE.md` when relevant;
   - project-specific -> `PROJECTS.md`, then matching `PROJECT.md` and only files it routes to;
   - working style -> `WORKING_STYLE.md` only when materially relevant.
5. Do not scan every project/file. If a named project is not found, check `PROJECTS.md` before free-form search. Search miss is not proof of absence.
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

When entered for retrieval **or because a later persistence trigger emerged**, notice clear non-sensitive changes that would leave durable state materially wrong/incomplete if the session ended now.

Good candidates: changed objective/constraint/status/next step, finalized decision, direct durable correction, or explicit durable working preference.

When durable intent is explicit and routing unambiguous, persist under normal write/verify rules unless ask-first is active. Ask when intent/future relevance is inferred, material is sensitive, routing is ambiguous, or structure must expand. If entry happened only after a new durable change emerged, retrieve minimum current target/routing state before writing.

Do not persist brainstorming, possibilities, casual conversation, one-off preferences, anything the user says not to persist, or working style that would make future work less honest about errors, risks, uncertainty, or disagreement.

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

Do not create a project for a one-off question. A project is justified when the user identifies ongoing work, it spans sessions with its own state/decisions/knowledge, project material would otherwise leak globally, or the topic repeatedly needs its own retrieval boundary. Ask when ambiguous.

For creation procedure, use `OPERATIONS.md`. No durable project folder may exist without a `PROJECTS.md` registry entry.

A new durable file/category is exceptional. Require a distinct role, recurrence, retrieval trigger, authority, navigation from an existing front door/index, human visibility, and any required manifest/migration update. Otherwise use an existing home or report `UNROUTED`.

## Write safety

A **consequential write** changes declared durable memory, routing, authority, project structure, or protocol configuration. Temporary reversible diagnostics such as `SETUP-TEST.md` are excluded, though activation still requires readback and cleanup verification.

For consequential writes:

`read current target(s) -> authorize/route -> write -> reread -> verify intended state`

Use current blob/version as update precondition when available. On stale/conflicting writes, reread and reconcile; never force or blindly retry.

If one intent changes multiple durable files, use a **write-set** and verify the cross-file postcondition before success. Details live in `OPERATIONS.md`.

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
