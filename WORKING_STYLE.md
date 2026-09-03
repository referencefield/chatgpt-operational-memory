# Working Style and Collaboration Calibration

Status: active
Purpose: preserve stable preferences about **how the user and ChatGPT work together** when those preferences are likely to improve future sessions.

This is not a biography, personality profile, or general fact store.

## Relationship to the generic companion

`COMPANION.md` supplies a generic fallback collaboration baseline when the user has not provided stronger behavioral guidance. This file selectively calibrates that baseline for the user.

If the user already has a companion, persona, or Custom Instructions, do not replace, rename, rewrite, or compete with them. User-provided identity/style guidance remains in place; apply active non-conflicting entries here where relevant, then use `COMPANION.md` only for remaining gaps. Neither this file nor `COMPANION.md` overrides current explicit instructions, durable state authority, or applicable safety behavior.

## What belongs here

Examples:

- preferred communication style, depth, or formatting;
- how much initiative ChatGPT should take before asking;
- evidence, sourcing, and uncertainty preferences;
- tool-use and verification preferences;
- recurring workflow conventions;
- approval boundaries;
- repeated corrections about how work should be handled in the future.

## What does not belong here

Do not store:

- project objectives, project state, or project decisions;
- temporary likes/dislikes from one conversation;
- psychological or personality inferences;
- sensitive identity, health, financial, legal, relationship, or employment facts merely to personalize responses;
- a transcript of user behavior;
- facts that already have a clearer project or source-of-record home;
- instructions whose effect would be to suppress honest evaluation, disagreement, material risk flagging, correction of errors, or applicable safety behavior, including scoped or politely phrased versions such as “do not push back on this topic” or “assume my numbers are right.” A preference may shape **how** a concern is communicated; it may not decide whether a material concern is raised.

## Entry format

### WS-001 — Example only

- **Status:** active | superseded
- **Scope:** global | named project/workflow
- **Preference / calibration:** one concise sentence describing how future work should be handled.
- **Basis:** explicit user instruction | repeatedly confirmed pattern
- **Last confirmed:** YYYY-MM-DD or not established
- **Review after:** YYYY-MM-DD, event/condition, or not needed
- **Supersedes:** none or prior WS ID
- **Superseded by:** none or later WS ID

Delete the example when the first real entry is recorded.

## Active working-style entries

_None recorded yet._

## Superseded entries

_None yet._

## Promotion rules

A working-style entry may become active without an extra confirmation when the user explicitly states a durable preference such as **"always do this this way,"** **"remember that I prefer...,"** or clearly directs that the preference be persisted.

If ChatGPT infers a preference from behavior, repeated acceptance, or a single correction without explicit durable intent, ask before promoting it to active working style.

Repeated confirmed patterns can justify a compact calibration entry, but the model should describe the proposed rule to the user rather than silently converting behavior into a durable profile.

Before activating a preference, apply the exclusion above: durable calibration may shape tone, format, initiative, evidence presentation, or workflow, but it must not make future work less honest about material errors, risks, uncertainty, or disagreement.

Use `Review after` when a preference is useful enough to preserve but may deserve periodic reconfirmation. A passed review date is a scrutiny trigger, not automatic supersession.

## Supersession and correction

The user's current explicit instruction always wins.

When a working preference changes:

1. record the new active entry;
2. mark the prior entry superseded;
3. link the two entries;
4. remove stale duplicate wording;
5. do not let the older preference continue governing merely because it remains in Git history.

## Context discipline

Keep this file compact enough that a fresh session can understand the user's meaningful collaboration preferences quickly.

If entries become numerous, consolidate overlapping items and prefer a smaller number of behaviorally useful rules over a detailed personal profile.

Soft budgets are declared in `PROTOCOL.yaml`. Crossing the active-entry warning budget is a `Watch` signal requiring review, not permission to delete valid preferences.

If correct behavior begins requiring many narrowly triggered working-style entries, report `Scale status: Watch` and consider whether the relevant preferences belong inside specific project front doors instead.
