# Operations

This document is for normal operation after setup: persistence watch, project creation, durable persistence, write-sets, health checks, update discovery, recovery, scale management, and repository maintenance.

`START_HERE.md` remains the runtime routing authority. Use this document when the task needs operational detail.

## Normal entry

When prior durable state matters and the repository-ID bootloader is configured, the user does not need to restate repository identity or routing mechanics. A minimal explicit invocation is enough:

> `@GitHub Use my operational memory.`

For a known project, the task itself can be the command, for example:

> `@GitHub where are we on Northstar?`

ChatGPT should use the configured repository ID, resolve the exact repository, enter through the current front door, and load only the durable state relevant to the request. The user should not have to mention repository-ID resolution, owner/name resolution, `START_HERE.md`, or file paths.

If no persistent bootloader is configured, supply only the identity ChatGPT genuinely cannot infer:

> `@GitHub Use operational memory from <repository URL>.`

For a known project, name it. ChatGPT should use `PROJECTS.md` to locate the project rather than asking you to remember a path.

Useful phrases during work:

- **“Record this in operational memory.”** Route to the correct existing home.
- **“Update current state with this.”** Use the correct global/project `CURRENT.md`.
- **“Make this a durable decision.”** Use the correct global/project `DECISIONS.md`.
- **“Record this as durable knowledge.”** Use the correct global/project `KNOWLEDGE.md` when appropriate.
- **“Remember this as a working preference.”** Use `WORKING_STYLE.md` when appropriate.
- **“This is an ongoing project.”** Create/register a project when the project boundary is clearly justified.
- **“Do not persist this.”** Block persistence of the specified material.
- **“Ask before writing anything else this session.”** Temporarily switch to ask-first behavior.
- **“What do you currently have recorded about this?”** Retrieve the durable source instead of answering from recollection.
- **`@GitHub Run a repository health check.`** Run structural + semantic health checks and report scale status.
- **`@GitHub Check for protocol updates.`** Compare this working copy with the template source declared in `PROTOCOL.yaml`.

These are controls, not required incantations. During repository-backed work, the conservative persistence watch in `START_HERE.md` should notice clear future-governing changes even when the user does not remember a magic phrase. When starting a fresh repository-backed control action such as health or update checking, explicit `@GitHub` is the dependable invocation path.

## Persistence watch

The purpose of the persistence watch is to keep loaded durable state from quietly becoming wrong while avoiding transcript-like over-persistence.

When the user explicitly establishes a clear, non-sensitive change that will materially govern future work, ChatGPT may route and persist it under the normal authorization, write, and verification rules without requiring a separate “remember this” phrase. Examples include a finalized decision, a changed active objective/constraint, a direct durable correction, or an explicit durable working preference.

Ask before writing when durable intent or future relevance is inferred rather than explicit, when the material is sensitive, when routing is ambiguous, when a new structural home would be required, or when the user has selected ask-first behavior.

Do not persist brainstorming, alternatives under consideration, casual facts, transient preferences, or conversational detail merely because they might be useful later. Working-style candidates must also pass the behavioral-authority boundary in `WORKING_STYLE.md` and `SECURITY.md`.

Persistence is maintained during repository-backed work rather than deferred to a special end-of-session command. When a qualifying change occurs, route and verify it at the point it becomes durable enough to govern future work.

## Project creation

A user should not have to design folders.

When a workstream earns a project boundary, ChatGPT should:

1. establish that a project boundary is justified under `START_HERE.md`;
2. ask only if project status is ambiguous;
3. establish a project-creation write-set;
4. create `projects/<slug>/PROJECT.md`, `CURRENT.md`, `DECISIONS.md`, and `KNOWLEDGE.md` from `projects/_TEMPLATE/`;
5. register the project in `PROJECTS.md`;
6. reread the registry and all required project files;
7. verify that the registry points to the correct project front door and the project front door points to the intended current authority;
8. report completion only after the complete project-routing invariant holds.

If only part succeeds, report **project routing is temporarily inconsistent** and reconcile the write-set before claiming completion.

## Write-set procedure

Use a write-set whenever one durable intent requires more than one file change.

Before writing, establish:

### Intent

One sentence stating the durable user-authorized outcome.

### Expected writes

Every file that must change for the intent to be complete.

### Preconditions

For each existing target, retrieve the current version/blob identifier immediately before writing when the integration exposes one.

### Required postcondition / invariant

State what must be simultaneously true after the write-set.

Example:

- Intent: change launch target from October to January.
- Expected writes: `DECISIONS.md`, `CURRENT.md`.
- Preconditions: current blob/version for both files.
- Postcondition: new launch decision active; prior launch decision superseded; current launch target = January.

Then execute:

`read current targets -> establish write-set -> write -> reread all affected targets -> verify invariant -> report success`

If atomic multi-file commit support is available and appropriate, prefer it. Otherwise sequential writes are acceptable only when the complete invariant is verified afterward.

Never treat “all API calls returned OK” as equivalent to the write-set being semantically complete.

## Persistence receipts

`START_HERE.md` defines **consequential write**. For those writes, verify the resulting repository/ref/path/content before claiming success.

When GitHub returns or confirms a real commit SHA, report a compact receipt:

`Persisted: <short description> · <file or write-set> · commit <short SHA>`

Never invent or guess a commit ID. If unavailable, say `commit ID unavailable`.

For a new durable decision, also show the exact stored one-sentence `Decision` field so the user can inspect the semantic result.

## Check for template/protocol updates

`PROTOCOL.yaml` declares the public template source and manifest path for this working copy. The template source's GitHub repository ID is the durable update-discovery key; its owner/name is human-readable metadata that may change.

When the user says **“Check for protocol updates”**, or when a repository health check can reach the template source without distracting from the user's task:

1. retrieve the local `PROTOCOL.yaml`;
2. resolve `template_source.repository_id` to the public template's current owner/name; do not substitute a similarly named repository if the ID cannot be resolved;
3. retrieve that resolved template source's declared manifest;
4. compare the local and source release/status plus any materially changed protocol structure relevant to migration;
5. report whether the working copy appears current, whether a newer released protocol is available, or whether comparison is indeterminate;
6. if the source is newer, read `MIGRATIONS.md` from the resolved source and describe the applicable migration before changing anything;
7. **do not auto-migrate** and do not overwrite private state merely because the public template changed.

During pre-release development, `protocol_version: "unreleased"` is intentionally not an ordered release identifier. If both source and working copy are unreleased, do not invent version ordering. Compare the manifest/content only when the user explicitly needs a development comparison.

After a real release identifier exists, use the release metadata plus `MIGRATIONS.md` to determine whether an upgrade is applicable.

If the template source repository ID cannot be resolved or the resolved source cannot be reached, report update status as **not checked** rather than guessing another source or assuming the working copy is current.

## Repository health check

A health check has two layers.

### Deterministic structural layer

Use the advisory validator declared in `PROTOCOL.yaml` when available. It checks machine-verifiable invariants such as required files, project registration/template structure, identifier uniqueness/reference integrity, supersession lifecycle consistency, manifest identity fields, and soft budget warnings.

The included GitHub Action is advisory and intentionally does **not** run on every direct operational-memory write. It runs for pull requests or when manually dispatched. It is **not** a required status check and does not block ordinary direct ChatGPT writes to `main`.

### Semantic layer

ChatGPT should additionally inspect what deterministic tooling cannot reliably determine:

- whether `CURRENT.md` semantically conflicts with an active decision;
- whether durable knowledge belongs globally or in a project;
- whether knowledge appears stale despite missing/weak lifecycle metadata;
- whether two project entries are really duplicate workstreams;
- whether a working-style entry is overbroad, contradictory, drifting into personal profiling, or would suppress honest evaluation/risk flagging;
- whether the minimum useful retrieval path is still obvious;
- whether persistence-watch behavior is missing obvious durable changes or producing noisy/overbroad writes.

A compact health result should include:

- protocol release/status / manifest readable;
- template update status when checked;
- front door present and readable;
- global current/decision consistency;
- global knowledge freshness/supersession;
- project registry integrity;
- registered active project front doors and required files present;
- non-template project folders registered;
- project-specific state/knowledge not leaking into global files;
- working-style hygiene;
- recent consequential writes relevant to the check observable;
- no leftover `SETUP-TEST.md` or other temporary setup/probe files;
- canonical branch/protection state when available;
- **`Scale status: Healthy | Watch | Outgrowing the template`**.

## Soft budgets and lifecycle pressure

Soft budgets live in `PROTOCOL.yaml`. They are warning indicators, not hard limits.

Crossing a soft budget means ask **why the supposedly compact active state is getting large**. Do not delete material merely to get under a number.

Typical corrections include moving project-specific material out of global files, creating/registering an earned project boundary, compacting stale current state, superseding inactive decisions, consolidating duplicate knowledge or working-style entries, moving project knowledge to the correct scope, or adding one justified routed source of record when the promotion gate is satisfied.

Knowledge and working-style entries may use `Review after:` to prompt future scrutiny without requiring background automation.

## Scale status

### Healthy

Routing is clear, front doors remain useful, and the minimum required context is small enough to retrieve/inspect easily.

### Watch

Structural pressure is appearing but the existing architecture can still correct it. Examples include soft-budget warnings, state leakage, repeated UNROUTED material, unregistered workstreams, duplicate/stale knowledge, or too many narrow working-style rules.

Apply the smallest structural correction first.

### Outgrowing the template

Use only when project scoping, compaction, supersession, and routed durable homes are no longer sufficient, or when reliability requires typed schemas, indexed/scoped retrieval beyond the current router, deterministic semantic validation, atomic transactions, or a dedicated memory service.

At that point, preserve this repo as a human-readable control layer and migrate storage/retrieval incrementally rather than dumping more unindexed Markdown into it.

## Failure and recovery

Default to fail closed, fail loud, preserve the last known good state, and offer a recovery path.

- Missing required retrieval -> report incomplete/partial retrieval.
- No legitimate persistence destination -> report `UNROUTED / no legitimate home`.
- Unsupported/ambiguous durable fact -> ask rather than activate it.
- Stale write -> reload and reconcile, never force/blind retry.
- Unverified write -> report `not verified`.
- Partial write-set -> report temporary inconsistency and reconcile.
- Inferred working preference -> ask before activation.
- Required GitHub write actions unavailable -> state that changes were not persisted.

If GitHub write actions are temporarily unavailable, a human may make the appropriate edit directly in the GitHub web interface. When access returns, enter through `START_HERE.md`, reread affected state, and reconcile the manual change before proceeding.

## Repository maintenance

The desired normal Git branch model is one canonical `main` branch.

Routine operational-memory writes go directly to `main`. Temporary implementation branches are acceptable when needed, but they should be removed after their work is safely incorporated or deliberately abandoned.

### Branch-cleanup safety rule

A branch is **not** safe to delete merely because an ahead/behind or commit-ancestry comparison looks a certain way.

In particular, squash merges and rebases can leave a source branch reporting commits “ahead of `main`” even when the branch's intended content has already been incorporated into `main` under different commit identities. Conversely, a branch may contain unique work that a superficial comparison misses.

Before deleting any non-`main` branch:

1. identify why the branch exists and whether it belongs to a pull request;
2. explicitly exclude the canonical/default branch from the deletion target set;
3. if the branch belongs to a pull request, verify that the PR is merged and identify the resulting merge/squash/rebase commit on `main`;
4. verify that the intended resulting content is present on `main` using the merged PR record, changed-file/content comparison, tree/content verification, or another method appropriate to the merge strategy;
5. do **not** use `ahead_by == 0`, `behind_by`, commit ancestry, or branch-name similarity alone as proof that work is incorporated;
6. if there is no associated merged PR, inspect the branch's unique commits and content/diff against `main`; preserve anything not clearly incorporated or deliberately abandoned;
7. if incorporation remains uncertain, stop and keep the branch;
8. execute validation and deletion as one fail-closed operation: a failed validation must prevent the deletion phase from running or being represented as safe;
9. after deletion, verify the canonical `main` head is the expected commit, `main` remains protected when protection is configured, and only the intended branches were removed.

For interactive terminal cleanup, do not rely on a prior `throw`, failed command, or warning to prevent a later separately pasted deletion block. The deletion commands themselves must be conditional on a successful validation result.

### Protection is a backstop, not deletion proof

Recommended `main` protection blocks deletion and non-fast-forward/force-push changes to the canonical branch. It does not protect ordinary temporary branches unless separate rules target them, and it does not establish that those branches are safe to delete.

Do not use force pushes, hard resets, or history rewrites as routine cleanup.

See `SECURITY.md` for optional `main` protection against deletion and force pushes.

## Behavioral evals

`EVALS.md` contains adversarial scenarios for model-mediated behavior. Use them when changing routing, persistence, failure, authority, update discovery, release lifecycle, or repository-maintenance rules, or when evaluating a new model/integration. They complement structural validation rather than replacing it.
