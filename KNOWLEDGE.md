# Shared Durable Knowledge

Status: active
Purpose: preserve compact, stable, cross-project facts or definitions that materially improve future work and do not belong in current state, decisions, or working-style calibration.

This is not a transcript, scrapbook, or general-purpose personal database.

## What belongs here

Examples:

- stable cross-project facts the user repeatedly relies on;
- standing definitions or terminology;
- durable context that affects several workstreams;
- compact factual corrections that should stop stale assumptions from resurfacing.

Project-specific knowledge belongs in that project's `KNOWLEDGE.md` once the project exists.

## What does not belong here

Do not store:

- transient/current state;
- governing decisions;
- collaboration preferences;
- project-local facts when a project boundary exists;
- speculative or weakly supported model inference;
- secrets;
- sensitive personal facts merely because they might personalize a response.

## Entry format

### K-001 — Example only

- **Status:** active | superseded | stale
- **Scope:** global / cross-project
- **Knowledge:** one concise durable fact, definition, or correction.
- **Basis / source:** user explicit | repository source | external source | other stated basis
- **Last verified:** YYYY-MM-DD or not established
- **Review after:** YYYY-MM-DD, event/condition, or not needed
- **Stale when:** event/date/condition, or none known
- **Supersedes:** none or prior K ID
- **Superseded by:** none or later K ID

Delete the example when the first real entry is recorded.

## Active knowledge

_None recorded yet._

## Superseded / stale knowledge

_None yet._

## Promotion rules

Prefer an existing canonical source of record when one already exists. This file should not duplicate a better source merely for convenience.

A fact may be recorded here when it is clearly supported, likely to matter again across projects, and does not fit more authoritative current/decision/project/working-style state.

If the fact is time-sensitive, record a `Stale when` condition or last-verified date. Use `Review after` when a future health check should reconsider the entry even if no deterministic stale event is known.

A passed `Review after` date does **not** automatically make the entry false. It is a scrutiny trigger: reverify when the entry materially affects current work, then refresh lifecycle metadata, supersede it, or mark it stale as evidence warrants.

If support is ambiguous or the proposed durable fact is model-inferred rather than user/source established, ask before activating it.

## Maintenance

- supersede corrections instead of keeping contradictory active facts;
- mark time-sensitive knowledge stale when its condition is reached or uncertainty becomes material;
- review entries whose `Review after` trigger has arrived when they become relevant;
- move project-local knowledge into the relevant project when a project boundary is created;
- consolidate duplicates;
- keep this file small enough that global shared knowledge remains inspectable.

Soft budgets are declared in `PROTOCOL.yaml`. Crossing one is a `Watch` signal requiring structural review, not a command to delete valid knowledge.

If this file starts becoming a large cross-domain encyclopedia, report `Scale status: Watch` and route knowledge into project scopes or a justified indexed/structured layer instead of continuing flat growth.