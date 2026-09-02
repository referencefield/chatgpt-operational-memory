# Project Front Door

Project: <name>
Slug: <slug>
Status: active | paused | closed
Last reconciled: not yet established

## Purpose

One sentence describing what this durable workstream is trying to accomplish.

## Route here when

- <trigger/topic>

## Do not load for

- <obvious exclusion if needed>

## Load first

A fresh session handling this project should normally retrieve:

1. this `PROJECT.md`;
2. `CURRENT.md` when current project state can matter;
3. `DECISIONS.md` when durable project decisions can matter;
4. `KNOWLEDGE.md` when stable project facts/definitions/corrections can matter.

Load additional project artifacts or linked repositories only when this front door or the current task identifies them as necessary.

## Current authority

- **Current state:** `CURRENT.md`
- **Durable project decisions:** `DECISIONS.md`
- **Durable project knowledge:** `KNOWLEDGE.md`
- **Other canonical sources:** none yet

When another project artifact becomes a source of record, register its exact path and role here. Do not create unindexed durable files.

## Linked repositories

_None yet._

A project may link zero or more external GitHub repositories when ongoing work genuinely spans repositories. Do not pre-register unrelated repositories merely because GitHub can access them.

Register each linked repository using:

- **Repository ID:** <numeric GitHub repository ID>
- **Role:** <why this repository belongs to the project>
- **Authority:** <what canonical content/state this repository owns>
- **Human label:** <current owner/name, informational only>

Rules:

- capture the ID from the exact repository the user identifies; owner/name may later change;
- Operational Memory owns cross-session purpose, current context, durable decisions, and cross-repository relationships unless a better source is explicitly registered;
- a linked repository owns the canonical content assigned to its **Authority** field, such as source code, implementation documentation, issues, or releases; do not duplicate that canonical content here merely for convenience;
- registration records relationship and routing, **not permission**. Before reading or writing a linked repository, verify that the selected `@GitHub` surface actually has the required access for the current task;
- resolve the repository ID at runtime only when its content can materially affect the task. If it cannot be resolved or accessed, report that and fail closed; never substitute a similarly named or unrelated repository;
- when the user introduces an external repository during clearly ongoing project work, link it conversationally if the relationship, role, and authority are clear. Ask only when those are ambiguous.

## Current phase

_Not yet established._

## Fixed / settled

_None yet._

## Unresolved

_None yet._

## Next useful action

_Not yet established._

## Optional durable homes

Do not create additional files merely because information exists.

If recurring project material does not belong in `CURRENT.md`, `DECISIONS.md`, or `KNOWLEDGE.md`, first check whether an existing canonical source already holds it. A new project artifact is justified only when it has a distinct role, expected recurrence, a retrieval trigger, clear authority, and is registered under **Current authority** above.

Possible roles, when genuinely needed, include a recurring procedure or a project-specific evidence/source register. These are examples, not files that should automatically be created.

## Persistence routing

Before persisting project material:

1. prefer an existing registered source of record, including a linked repository when its declared authority owns the material;
2. current objective/state/constraints/open questions -> `CURRENT.md`;
3. durable governing decision -> `DECISIONS.md`;
4. stable supported project fact/definition/correction -> `KNOWLEDGE.md`;
5. stable global collaboration preference -> root `WORKING_STYLE.md`, not this project;
6. cross-project fact/definition/correction -> root `KNOWLEDGE.md` when no better source exists;
7. material with no legitimate project home -> do not invent a file; surface it as a routing/growth signal.

## Maintenance

Update this front door when:

- project purpose or status materially changes;
- the current authority moves;
- a new canonical artifact or linked repository is added;
- a linked repository's role/authority changes or access becomes unavailable;
- routing triggers become misleading;
- the project closes or reopens.

Keep this file small enough that it remains useful as a front door rather than becoming the project itself.
