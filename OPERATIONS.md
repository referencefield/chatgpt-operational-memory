# Operations

This document is for normal operation after setup: project creation, durable persistence, write-sets, closeout, health checks, recovery, scale management, and repository maintenance.

`START_HERE.md` remains the runtime routing authority. Use this document when the task needs operational detail.

## Normal entry

When prior durable state matters:

> `@GitHub Enter my operational-memory repository through START_HERE.md and load only the durable state relevant to this task.`

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
- **“Run a repository health check.”** Run structural + semantic health checks and report scale status.

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

For consequential writes, verify the resulting repository/ref/path/content before claiming success.

When GitHub returns or confirms a real commit SHA, report a compact receipt:

`Persisted: <short description> · <file or write-set> · commit <short SHA>`

Never invent or guess a commit ID. If unavailable, say `commit ID unavailable`.

For a new durable decision, also show the exact stored one-sentence `Decision` field so the user can inspect the semantic result.

## Closing out an important session

Say:

> **“Close out operational memory.”**

ChatGPT should:

1. enter through `START_HERE.md`;
2. identify the global/project scopes actually touched;
3. identify material durable changes not yet persisted;
4. apply the persistence-routing gate;
5. establish any required write-set before writing;
6. update only what earns persistence;
7. compact stale current state instead of appending a transcript;
8. reconcile active decisions, durable knowledge, and working-style changes;
9. reread and verify consequential writes/write-sets;
10. report persistence receipts and anything intentionally left unpersisted;
11. surface a `Watch` condition if the session exposed routing/sprawl problems.

This is a conversational closeout, not a transcript archive.

## Repository health check

A health check has two layers.

### Deterministic structural layer

Use the advisory validator declared in `PROTOCOL.yaml` when available. It checks machine-verifiable invariants such as required files, project registration/template structure, identifier uniqueness/reference integrity, and soft budget warnings.

The GitHub Action is advisory. It is **not** a required status check and does not block ordinary direct ChatGPT writes to `main`.

### Semantic layer

ChatGPT should additionally inspect what deterministic tooling cannot reliably determine:

- whether `CURRENT.md` semantically conflicts with an active decision;
- whether durable knowledge belongs globally or in a project;
- whether knowledge appears stale despite missing/weak lifecycle metadata;
- whether two project entries are really duplicate workstreams;
- whether a working-style entry is overbroad, contradictory, or drifting into personal profiling;
- whether the minimum useful retrieval path is still obvious.

A compact health result should include:

- protocol version / manifest readable;
- front door present and readable;
- global current/decision consistency;
- global knowledge freshness/supersession;
- project registry integrity;
- registered active project front doors and required files present;
- non-template project folders registered;
- project-specific state/knowledge not leaking into global files;
- working-style hygiene;
- recent consequential writes relevant to the check observable;
- no leftover `SETUP-TEST.md`;
- canonical branch/protection state when available;
- **`V1 scale status: Healthy | Watch | Outgrowing the template`**.

## Soft budgets and lifecycle pressure

Soft budgets live in `PROTOCOL.yaml`. They are warning indicators, not hard limits.

Crossing a soft budget means ask **why the supposedly compact active state is getting large**. Do not delete material merely to get under a number.

Typical corrections include:

- move project-specific material out of global files;
- create/register a project boundary that has clearly been earned;
- compact stale current state;
- supersede inactive decisions;
- consolidate duplicate knowledge or working-style entries;
- move stable project knowledge to the correct project scope;
- add one justified routed source of record when the promotion gate is satisfied.

Knowledge and working-style entries may use `Review after:` to prompt future scrutiny without requiring background automation.

## Scale status

### Healthy

Routing is clear, front doors remain useful, and the minimum required context is small enough to retrieve/inspect easily.

### Watch

Structural pressure is appearing but the existing architecture can still correct it. Examples include soft-budget warnings, state leakage, repeated NOT-V1 material, unregistered workstreams, duplicate/stale knowledge, or too many narrow working-style rules.

Apply the smallest structural correction first.

### Outgrowing the template

Use only when project scoping, compaction, supersession, and routed durable homes are no longer sufficient, or when reliability requires typed schemas, indexed/scoped retrieval beyond the current router, deterministic semantic validation, atomic transactions, or a dedicated memory service.

At that point, preserve this repo as a human-readable control layer and migrate storage/retrieval incrementally rather than dumping more unindexed Markdown into it.

## Failure and recovery

Default to fail closed, fail loud, preserve the last known good state, and offer a recovery path.

- Missing required retrieval -> report incomplete/partial retrieval.
- No legitimate persistence destination -> report `NOT-V1 / no legitimate home`.
- Unsupported/ambiguous durable fact -> ask rather than activate it.
- Stale write -> reload and reconcile, never force/blind retry.
- Unverified write -> report `not verified`.
- Partial write-set -> report temporary inconsistency and reconcile.
- Inferred working preference -> ask before activation.
- Connector unavailable -> state that changes were not persisted.

If GitHub is temporarily unavailable, a human may make the appropriate edit directly in the GitHub web interface. When access returns, enter through `START_HERE.md`, reread affected state, and reconcile the manual change before proceeding.

## Repository maintenance

The desired normal Git branch model is one canonical `main` branch.

Routine operational-memory writes go directly to `main`.

If another branch exists:

1. compare it with `main`;
2. preserve unique work;
3. verify the resulting canonical state;
4. delete the branch only after its unique work is incorporated or deliberately abandoned.

Do not use force pushes, hard resets, or history rewrites as routine cleanup.

See `SECURITY.md` for optional `main` protection against deletion and force pushes.

## Behavioral evals

`EVALS.md` contains adversarial scenarios for model-mediated behavior. Use them when changing routing, persistence, failure, or authority rules, or when evaluating a new model/integration. They complement structural validation rather than replacing it.