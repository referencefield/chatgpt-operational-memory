# Runtime Front Door

Status: active
Purpose: give a fresh ChatGPT session one small place to start, then route to only the durable state that can materially affect the current task.

This file is the **runtime protocol authority** for this repository. Persistent ChatGPT instructions should point here rather than duplicate this protocol.

Do not begin by loading the whole repository.

## Boot sequence

1. Retrieve `PROTOCOL.yaml` and confirm the protocol release/status, canonical branch, front door, declared structure, and template source.
2. Identify the user's current intent.
3. Decide whether durable repository state can materially change the answer or action. If not, use **no-repository-context** and continue normally.
4. If durable state matters, determine scope before retrieval:
   - **global / cross-project current state or decisions** -> load root `CURRENT.md` and/or `DECISIONS.md` as needed;
   - **global / cross-project durable facts or definitions** -> load root `KNOWLEDGE.md` when relevant;
   - **project-specific** -> load `PROJECTS.md`, identify the project, then load that project's `PROJECT.md` front door and only the files it says are needed;
   - **working-style / collaboration preference** -> load `WORKING_STYLE.md` only when those preferences can materially affect how the task should be handled.
5. Do not scan every project or every file. Route first, then retrieve the minimum authoritative state.
6. If a named project cannot be found, check `PROJECTS.md` before free-form repository search. A search miss is not proof that durable state does not exist.
7. Stop expanding context once the task can be handled correctly.

## Authority

When repository sources conflict, use this order unless a higher-level system/safety rule requires otherwise:

1. the user's current explicit instruction;
2. current verified project-local state and active project decisions;
3. current verified global state and active global decisions;
4. current verified durable knowledge when relevant and not superseded/stale;
5. explicit active entries in `WORKING_STYLE.md` when they apply to how work is performed;
6. historical/superseded repository state;
7. chat recollection or model inference.

Do not let working-style preference override a current project decision or explicit user instruction. Do not let stale knowledge override current verified state. Git history is historical evidence, not active authority by itself.

## Conservative persistence watch

During repository-backed work, do not require the user to remember a magic phrase every time durable state clearly changes.

Maintain a conservative persistence watch for **clear, non-sensitive changes that would make the loaded durable state materially wrong or incomplete if the session ended now**. Typical candidates include:

- an explicitly changed active objective, constraint, status, or next step;
- a clearly finalized decision;
- a direct correction to durable knowledge;
- an explicit durable working preference;
- a clearly established project boundary or other future-governing state.

When durable intent is explicit and the destination is unambiguous, route and persist under the normal write/verify rules unless the user has requested ask-first behavior.

If future relevance or durable intent is inferred rather than explicit, if the material is sensitive, or if routing is ambiguous, ask before persistence.

Do not persist brainstorming, possibilities, casual conversation, one-off preferences, or information merely because it might someday be useful. A user instruction such as **"do not persist this"** always blocks persistence of the specified material.

## Persistence routing gate

Before writing durable material, classify it. A request such as **"record this in operational memory"** authorizes correct routing, not arbitrary file creation.

Use this order:

1. **Existing source of record** -> update the existing canonical location. Prefer this over creating anything new.
2. **Global CURRENT** -> root `CURRENT.md` only for cross-project current focus, active portfolio-level work, cross-project constraints, or global open questions.
3. **Global DECISION** -> root `DECISIONS.md` only for durable decisions that govern more than one project or the repository as a whole.
4. **Global KNOWLEDGE** -> root `KNOWLEDGE.md` only for compact, stable cross-project facts, definitions, or corrections that materially matter later and have no better canonical source.
5. **WORKING STYLE** -> `WORKING_STYLE.md` only for stable, collaboration-relevant preferences about how the user and ChatGPT work together.
6. **PROJECT** -> route project-specific current state, decisions, or durable knowledge through `PROJECTS.md` to the appropriate project folder.
7. **UNROUTED / no legitimate home** -> do not invent a file. Tell the user the material does not fit the current structure and treat recurrence as a growth signal.

## Durable knowledge

Durable knowledge is not the same as current state or a decision.

Use root `KNOWLEDGE.md` for stable, supported facts/definitions/corrections that matter across projects. Use a project's `KNOWLEDGE.md` for project-local durable knowledge.

Prefer an existing canonical source when one already exists. Do not duplicate whole documents into knowledge files. For time-sensitive facts, use `Last verified`, `Review after`, and/or `Stale when` so future sessions do not treat old information as permanently current. Supersede corrections instead of keeping contradictory active facts.

Do not persist sensitive personal facts merely to personalize responses.

## Working-style learning

`WORKING_STYLE.md` may accumulate stable collaboration preferences over time, but it must not become a biography or personality dossier.

Good candidates include explicit or repeatedly confirmed preferences about communication, initiative, evidence standards, tool use, approval boundaries, recurring workflows, and corrections that should change future behavior.

Explicit durable preferences may be recorded directly. Ambiguous inferred preferences require confirmation before activation. Use `Review after` when a preference may deserve periodic reconfirmation.

Do not infer psychological traits, identity characteristics, sensitive personal facts, or broad preferences from a single interaction.

## When to create a project

Do not create a project for a one-off question.

A project becomes justified when any of these are true:

- the user explicitly identifies the work as an ongoing project or workstream;
- the work is expected to span multiple sessions and has its own objective, current state, constraints, decisions, or durable knowledge;
- project-specific durable material would otherwise begin accumulating in root global files;
- the same topic repeatedly produces legitimate durable state that needs its own retrieval boundary.

When project status is ambiguous, ask before creating a new project. When clearly authorized, create it from `projects/_TEMPLATE/`, register it in `PROJECTS.md`, and make its `PROJECT.md` the project-local front door.

No durable project folder should exist without a registry entry in `PROJECTS.md`.

## New-home promotion gate

A new durable file or category outside the declared structure is exceptional. Before creating one, establish all of the following:

- **distinct role:** the content cannot be represented correctly in an existing source of record;
- **recurrence:** the category is expected to matter again, not just once;
- **retrieval trigger:** a future session can know when to load it;
- **authority:** it is clear whether the new artifact is current authority, reference material, procedure, or history;
- **navigation:** the appropriate `PROJECT.md` or root router will point to it;
- **human visibility:** the user is told that the durable structure is expanding;
- **manifest impact:** if the artifact becomes protocol-required structure, update `PROTOCOL.yaml` and `MIGRATIONS.md` in the same write-set.

If those conditions are not met, do not create the new home.

## Write-set protocol for coupled changes

A persistence operation that affects more than one durable file is a **write-set**. Examples include changing a decision that also changes current state, creating a project, or changing protocol structure.

Before writing, establish internally:

- **Intent:** the durable outcome the user authorized;
- **Expected writes:** every file that must change;
- **Preconditions:** the current blob/version of each existing target when the integration exposes one;
- **Required postcondition/invariant:** what must be true across the complete affected set before success can be claimed.

Then execute:

`read current targets -> establish write-set -> write -> reread every affected target -> verify invariant -> report completion`

If atomic multi-file commit support is available and appropriate, prefer it. Otherwise, sequential writes are acceptable only if the complete postcondition is verified afterward.

If only part of a write-set succeeds, do not report overall completion. Report the temporary inconsistency, reread affected files, preserve valid intervening edits, and complete or deliberately reconcile the write-set before claiming success.

A series of successful API calls is not the success condition. The verified invariant is.

## Write verification and concurrency

Immediately before updating an existing file, retrieve the current target and use its current blob/version as the write precondition when the integration supports one.

If a stale/conflicting write is rejected, fail closed. Do not force or blindly retry. Reread, reconcile material intervening changes, and write only against the newly observed version.

For consequential persistence, read back the intended repository/ref/path/content before claiming completion. A commit receipt supplements readback; it does not replace it. Never invent a commit hash.

## Failure behavior

Default to **fail closed, fail loud, preserve the last known good state, and provide a recovery path**.

Examples:

- required retrieval missing -> report incomplete/partial retrieval;
- no legitimate persistence destination -> report `UNROUTED / no legitimate home`;
- ambiguous durable decision or inferred working preference -> ask before activating;
- stale write -> reread and reconcile, never force;
- unverified write -> report not verified;
- partial write-set -> report temporary inconsistency and reconcile;
- connector unavailable -> state that repository changes were not persisted.

Visible uncertainty is preferable to invented structure or plausible-looking success.

## Scale status

Repository health/maintenance should report:

### Healthy

Routing is clear; global files remain cross-project; project-specific state/knowledge live behind project front doors; working-style entries remain compact; minimum-scope retrieval is easy.

### Watch

Signals include project-specific material leaking into global files, unregistered durable workstreams, repeated UNROUTED material, duplicate/stale knowledge, contradictory or excessively narrow working-style entries, crossed soft budgets, frequent compaction merely to understand active state, or a project front door that no longer points cleanly to minimum authority.

A crossed soft budget is a reason to inspect structure, not an automatic deletion instruction.

### Outgrowing the template

Use this only when routing/project scoping is no longer sufficient, broad search routinely replaces front-door retrieval, active state remains too large after compaction, model-mediated routing/validation failures materially impair reliability, or the user genuinely needs typed schemas, indexed retrieval, deterministic semantic validation, atomic transactions, or a dedicated memory service.

At that point, preserve this repository as a human-readable control layer and recommend structured/indexed or tool-backed memory rather than uncontrolled Markdown growth.

## Where operational procedures live

- `PROTOCOL.yaml` -> machine-readable release/status/topology/budgets/template source
- `OPERATIONS.md` -> health checks, update checks, project creation, closeout, recovery, maintenance, write-set examples
- `SECURITY.md` -> privacy, secrets, repository-content boundary, Git hardening
- `MIGRATIONS.md` -> release-to-release upgrade guidance
- `EVALS.md` -> behavioral/adversarial scenarios used to test model-mediated parts of the protocol

Load those only when the task requires them. This front door should remain sufficient for ordinary routing.