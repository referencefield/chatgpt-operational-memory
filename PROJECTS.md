# Project Registry

Status: active
Purpose: route a fresh session to the correct durable workstream without scanning unrelated repository state.

This file is an **index**, not a project notebook. Keep each entry compact.

## Active projects

_None registered yet._

Recommended entry format:

#### Example entry: project-slug — Project name

- **Status:** active | paused
- **Purpose:** one sentence describing the durable workstream.
- **Activate when:** concise phrases/topics that should route here.
- **Do not load for:** obvious exclusions if ambiguity is likely.
- **Front door:** `projects/project-slug/PROJECT.md`
- **Current authority:** usually `projects/project-slug/CURRENT.md` plus active project decisions.

Real registered project entries use a level-three heading in this form:

`### project-slug — Project name`

## Closed / archived projects

_None yet._

Closed projects remain discoverable but should not be loaded as active state unless the user reopens them or historical context is specifically needed.

## Project creation rule

Create a project only when the work has earned its own retrieval boundary.

A project is justified when:

- the user explicitly identifies an ongoing project/workstream; or
- the work is expected to span multiple sessions and has its own objective/current state/constraints/decisions; or
- project-specific durable information would otherwise clutter root `CURRENT.md`, `DECISIONS.md`, or `KNOWLEDGE.md`; or
- repeated durable material on the same topic needs to be retrieved together later.

Do not create a project for a one-off question, temporary brainstorm, or single fact.

When project status is ambiguous, ask first.

## Project creation procedure

When a new project is clearly authorized:

1. establish a project-creation write-set;
2. choose a short stable slug;
3. create `projects/<slug>/PROJECT.md`, `CURRENT.md`, `DECISIONS.md`, and `KNOWLEDGE.md` using `projects/_TEMPLATE/` as the starting structure;
4. register the project here in the same write-set;
5. make `projects/<slug>/PROJECT.md` the project-local front door;
6. put project-specific state/decisions/knowledge in that project, not in root global files;
7. reread the registry and all required project files;
8. verify the complete routing invariant before reporting success.

If only part of project creation succeeds, report **project routing is temporarily inconsistent**, reread the registry and project paths, and finish or deliberately reconcile the structure before claiming completion.

## Routing rules

- Route before search.
- A named/known project should be located here before free-form repository search.
- Load only the selected project's front door first.
- Do not preload other projects merely because they are related.
- Root `CURRENT.md`, `DECISIONS.md`, and `KNOWLEDGE.md` are cross-project/global state, not duplicates of every project's state.
- A project's own verified current state outranks this registry summary if they differ; update the stale registry entry afterward.

## Maintenance

During repository health/maintenance checks:

- verify every active/paused registered entry points to an existing `PROJECT.md`;
- verify every non-template project folder has a registry entry;
- verify required project files match `PROTOCOL.yaml`;
- flag project-specific state/knowledge leaking into root global files;
- flag duplicate projects or ambiguous routing triggers;
- move closed projects to the closed section rather than deleting their durable history.
