# Project Registry

Status: active
Purpose: route a fresh session to the correct durable workstream without scanning unrelated repository state.

This file is an **index**, not a project notebook. Keep each entry compact.

## Active projects

_None registered yet._

Recommended entry format:

### project-slug — Project name

- **Status:** active | paused
- **Purpose:** one sentence describing the durable workstream.
- **Activate when:** concise phrases/topics that should route here.
- **Do not load for:** obvious exclusions if ambiguity is likely.
- **Front door:** `projects/project-slug/PROJECT.md`
- **Current authority:** usually `projects/project-slug/CURRENT.md` plus active project decisions; load project knowledge only when relevant.

## Closed / archived projects

_None yet._

Closed projects remain discoverable but should not be loaded as active state unless the user reopens them or historical context is specifically needed.

## Project creation rule

Create a project only when the work has earned its own retrieval boundary.

A project is justified when:

- the user explicitly identifies an ongoing project/workstream; or
- the work is expected to span multiple sessions and has its own objective/current state/constraints/decisions/durable knowledge; or
- project-specific durable information would otherwise clutter root global files; or
- repeated durable material on the same topic needs to be retrieved together later.

Do not create a project for a one-off question, temporary brainstorm, or single fact.

When project status is ambiguous, ask first.

## Project creation procedure

When a new project is clearly authorized:

1. choose a short stable slug;
2. create `projects/<slug>/PROJECT.md`, `CURRENT.md`, `DECISIONS.md`, and `KNOWLEDGE.md` using `projects/_TEMPLATE/` as the starting structure;
3. register the project here in the same change sequence;
4. make `projects/<slug>/PROJECT.md` the project-local front door;
5. put project-specific current state, decisions, and knowledge in that project rather than the root global files;
6. verify the new front door, registry entry, and state files before reporting completion.

If only part of project creation succeeds, report **project routing is temporarily inconsistent**, reread the registry and project paths, and finish or deliberately reconcile the structure before claiming completion.

## Routing rules

- Route before search.
- A named/known project should be located here before free-form repository search.
- Load only the selected project's front door first.
- Do not preload other projects merely because they are related.
- Root `CURRENT.md`, `DECISIONS.md`, and `KNOWLEDGE.md` are cross-project/global state, not duplicates of every project's state.
- A project's own verified current state/decisions/knowledge outrank this registry summary if they differ; update the stale registry entry afterward.

## Maintenance

During repository health/maintenance checks:

- verify every active registry entry points to an existing `PROJECT.md`;
- verify every non-template project folder has a registry entry;
- verify expected project skeleton files exist unless a project's front door explicitly documents a deliberate exception;
- flag project-specific state or knowledge leaking into root global files;
- flag duplicate projects or ambiguous routing triggers;
- move closed projects to the closed section rather than deleting their durable history.
