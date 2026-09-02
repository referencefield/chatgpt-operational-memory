# Runtime Front Door

Status: active
Purpose: give a fresh ChatGPT session one small place to start, then route to only the durable state that can materially affect the current task.

This file is the **front door** for operational memory. Do not begin by loading the whole repository.

## Fresh-session route

1. Identify the user's current intent.
2. Decide whether durable repository state can materially change the answer or action. If not, use no-repository-context and continue normally.
3. If durable state matters, determine the scope before retrieval:
   - **global / cross-project current state or decisions** -> load root `CURRENT.md` and `DECISIONS.md` as needed;
   - **global / cross-project durable facts or definitions** -> load root `KNOWLEDGE.md` when those facts can materially affect the task;
   - **project-specific** -> load `PROJECTS.md`, identify the project, then load that project's `PROJECT.md` front door and only the files it says to load first;
   - **working-style / collaboration preference** -> load `WORKING_STYLE.md` when those preferences can materially affect how the task should be handled.
4. Do not scan every project or every file. Route first, then retrieve the minimum authoritative state.
5. If a named project cannot be found, check `PROJECTS.md` before free-form repository search. A search miss is not proof that durable state does not exist.
6. Stop expanding context once the current task can be handled correctly.

## Authority

When sources conflict, use this order unless a higher-level system/safety rule requires otherwise:

1. the user's current explicit instruction;
2. current verified project-local state and active project decisions;
3. current verified global state and active global decisions;
4. current verified durable knowledge when it is relevant and not superseded/stale;
5. explicit active entries in `WORKING_STYLE.md` when they apply to how the work is performed;
6. historical/superseded repository state;
7. chat recollection or model inference.

Do not let a working-style preference override a current project decision or an explicit user instruction. Do not let stale knowledge override current verified state.

## Persistence routing gate

Before writing durable material, classify it. Every candidate must go through this gate:

1. **Existing source of record** -> update the existing canonical location. Prefer this over creating anything new.
2. **Global CURRENT** -> root `CURRENT.md` only for cross-project current focus, active portfolio-level work, cross-project constraints, or global open questions.
3. **Global DECISION** -> root `DECISIONS.md` only for durable decisions that govern more than one project or the repository as a whole.
4. **Global KNOWLEDGE** -> root `KNOWLEDGE.md` only for compact, stable cross-project facts, definitions, or corrections that materially matter later and have no better canonical source.
5. **WORKING STYLE** -> `WORKING_STYLE.md` only for stable, collaboration-relevant preferences about how the user and ChatGPT work together.
6. **PROJECT** -> route project-specific current state, decisions, or durable knowledge through `PROJECTS.md` to the appropriate project folder.
7. **NOT-V1 / no legitimate home** -> do not invent a file. Tell the user the material does not fit the current structure and treat recurrence as a growth signal.

A request such as **"record this in operational memory"** authorizes routing, not arbitrary file creation.

## Knowledge rules

Durable knowledge is not the same as current state or a decision.

Use `KNOWLEDGE.md` for stable, supported facts/definitions/corrections that matter across projects. Use a project's `KNOWLEDGE.md` for project-local durable knowledge.

Prefer an existing canonical source when one already exists. Do not duplicate whole documents into knowledge files.

For time-sensitive facts, record a last-verified date or stale condition. Supersede corrections instead of keeping contradictory active facts.

Do not persist sensitive personal facts merely to personalize responses.

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

A new durable file or category outside the provided structure is exceptional. Before creating one, establish all of the following:

- **distinct role:** the content cannot be represented correctly in an existing source of record;
- **recurrence:** the category is expected to matter again, not just once;
- **retrieval trigger:** a future session can know when to load it;
- **authority:** it is clear whether the new artifact is current authority, reference material, procedure, or history;
- **navigation:** the appropriate `PROJECT.md` or root router will point to it;
- **human visibility:** the user is told that the durable structure is expanding.

If those conditions are not met, do not create the new home.

## Working-style learning

`WORKING_STYLE.md` may accumulate stable collaboration preferences over time, but it must not become a personality dossier.

Good candidates include explicit or repeatedly confirmed preferences about communication, initiative, evidence standards, tool use, approval boundaries, recurring workflows, and corrections that should change future behavior.

Do not infer psychological traits, identity characteristics, sensitive personal facts, or broad preferences from a single interaction. Ambiguous inferred preferences require confirmation before durable activation.

## V1 scale status

A repository health or maintenance check should report one of these statuses:

### Healthy

Routing is clear; global files remain cross-project; project-specific state and knowledge live behind project front doors; working-style entries are compact; complete required retrieval remains easy.

### Watch

One or more signals are appearing:

- project-specific material is leaking into global files;
- multiple durable workstreams exist but are not registered as projects;
- similar material repeatedly routes to NOT-V1;
- global/project knowledge files are becoming cross-domain scrapbooks or contain duplicate/stale facts;
- `WORKING_STYLE.md` contains duplicates, contradictions, or increasingly vague inferred preferences;
- compaction/supersession is needed unusually often just to keep normal retrieval understandable;
- a project front door no longer points cleanly to the minimum current authority.

When status is Watch, recommend the smallest structural correction first: register/split a project, compact state, supersede stale entries, move knowledge into the correct scope, or add one justified routed source of record.

### Outgrowing the template

Use this only when the routing skeleton itself is no longer sufficient, for example:

- correct work routinely requires broad repository search instead of following front doors/indexes;
- many independent knowledge domains need selective retrieval beyond project boundaries;
- active durable state/knowledge is too large to load or inspect reliably even after project scoping and compaction;
- repeated model-mediated routing or validation failures materially impair reliability;
- the user needs typed schemas, indexed retrieval, deterministic validation, atomic transactions, or a dedicated memory service.

At that point, preserve this repository as the human-readable control layer and recommend a structured/indexed or tool-backed memory system rather than adding uncontrolled Markdown.

## Failure rule

Visible uncertainty is preferable to invented structure.

If the correct durable home cannot be established, say so. Do not create a plausible-looking file merely to complete a persistence request.
