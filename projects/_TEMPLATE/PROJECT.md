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
2. `CURRENT.md`;
3. `DECISIONS.md` when durable decisions can materially affect the task.

Load additional project artifacts only when this front door or the current task identifies them as necessary.

## Current authority

- **Current state:** `CURRENT.md`
- **Durable project decisions:** `DECISIONS.md`
- **Other canonical sources:** none yet

When another project artifact becomes a source of record, register its exact path and role here. Do not create unindexed durable files.

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

If recurring project material does not belong in `CURRENT.md` or `DECISIONS.md`, first check whether an existing canonical source already holds it. A new project artifact is justified only when it has a distinct role, expected recurrence, a retrieval trigger, clear authority, and is registered under **Current authority** above.

Possible roles, when genuinely needed, include compact reference facts, a recurring procedure, or a project-specific evidence/source register. These are examples, not files that should automatically be created.

## Persistence routing

Before persisting project material:

1. prefer an existing registered source of record;
2. current objective/state/constraints/open questions -> `CURRENT.md`;
3. durable governing decision -> `DECISIONS.md`;
4. stable global collaboration preference -> root `WORKING_STYLE.md`, not this project;
5. material with no legitimate project home -> do not invent a file; surface it as a routing/growth signal.

## Maintenance

Update this front door when:

- project purpose or status materially changes;
- the current authority moves;
- a new canonical artifact is added;
- routing triggers become misleading;
- the project closes or reopens.

Keep this file small enough that it remains useful as a front door rather than becoming the project itself.
