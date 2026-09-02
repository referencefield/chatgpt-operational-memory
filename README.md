# ChatGPT Operational Memory

A low-infrastructure GitHub template for ordinary ChatGPT users who want important working state to survive across conversations in a form they can inspect, correct, version, and own.

The template starts simple, but it is designed to **grow without turning into an uncontrolled knowledge base**.

It gives ChatGPT:

- one runtime front door;
- explicit global working state and durable decisions;
- a bounded durable knowledge layer for stable facts and corrections;
- a durable place for collaboration preferences and accumulated working-style calibration;
- a project registry and project-local front doors for multiple ongoing workstreams;
- routing rules that prefer existing sources of record before creating new files;
- visible retrieval, persistence, conflict, and scaling signals.

You do not need a terminal, local agent framework, vector database, MCP server, or Git expertise for normal use.

## The core idea

ChatGPT already has native memory, chat history, Projects, and conversation context. Those features are useful and this template does not replace them.

This repository is for the smaller class of state and knowledge that is important enough to **govern or materially improve future work** and valuable enough that you want to know where it lives.

The practical difference is not “ChatGPT remembers more.” It is:

**Out of the box:** “ChatGPT may have useful context available.”

**With this repository:** “For the parts important enough to matter later, I can see how ChatGPT routed the task, what durable state/knowledge it loaded, what is current, what decisions remain active, what working preferences apply, and whether changes were actually persisted.”

## Architecture at a glance

A fresh session should not load the whole repository.

`START_HERE.md` is the runtime front door:

```text
user request
    |
    v
START_HERE.md
    |
    +-- no durable state needed -> ordinary ChatGPT conversation
    |
    +-- global / cross-project work
    |      +-- CURRENT.md
    |      +-- DECISIONS.md
    |      +-- KNOWLEDGE.md when stable shared facts matter
    |
    +-- collaboration / working preference
    |      +-- WORKING_STYLE.md
    |
    +-- project-specific work
           +-- PROJECTS.md
                  |
                  v
             projects/<slug>/PROJECT.md
                  +-- CURRENT.md
                  +-- DECISIONS.md
                  +-- KNOWLEDGE.md
                  +-- only other registered sources actually needed
```

The goal is **route first, retrieve second**. A project-specific question should not cause ChatGPT to load every other project.

## What changes in practice

| Situation | ChatGPT out of the box | With this repo connected |
| --- | --- | --- |
| **Starting a fresh chat later** | ChatGPT may have useful prior context, but you may not know exactly what it is relying on. | ChatGPT can enter through `START_HERE.md`, route to the relevant durable state/knowledge, and show what was actually retrieved. |
| **You ask “Where were we?”** | ChatGPT reconstructs from the context available to that conversation. | The appropriate global or project current-state file provides an explicit recorded answer. |
| **You have several ongoing projects** | Context can be distributed across chats, Projects, files, and memory. | `PROJECTS.md` routes each workstream to its own project front door so unrelated projects do not share one giant state file. |
| **A stable fact/correction should carry forward** | It may live in prior chat context or native memory. | Supported stable facts can live in the correct global or project `KNOWLEDGE.md`, with basis/source, last-verified, stale, and supersession fields. |
| **You make an important decision** | The decision exists in the conversation and may influence later work. | A durable decision is recorded in the correct global or project `DECISIONS.md` with explicit supersession. |
| **You change your mind later** | Old and new positions can coexist across prior context. | The new decision/knowledge can explicitly supersede the old one so stale history does not remain active authority. |
| **You repeatedly teach ChatGPT how you like to work** | Native personalization may help, but the durable collaboration rule may not be visible as a project artifact. | Stable, collaboration-relevant preferences can be recorded in `WORKING_STYLE.md`, corrected, superseded, and inspected. |
| **You say “record this”** | There is no Git-backed routing transaction. | ChatGPT must classify the material, prefer an existing source of record, and route it to current state, decision, knowledge, working style, a project, or `NOT-V1`. The instruction does not authorize arbitrary file creation. |
| **Something does not fit anywhere** | The conversation can continue without a formal structural signal. | ChatGPT should say the material has no legitimate current home rather than inventing a file. Repeated `NOT-V1` candidates become a growth signal. |
| **You wonder whether something was actually saved** | There is normally no Git-style receipt for an ordinary conversational fact. | Consequential writes should be read back and, when GitHub exposes it, accompanied by a real commit receipt. |
| **Only part of required state was retrieved** | ChatGPT may still try to answer from partial context. | The workflow reports incomplete/partial retrieval and should not claim the relevant operational state is fully loaded. |
| **Two sessions edit the same file** | Native conversational memory does not expose a versioned write conflict. | Existing-file updates can use the current GitHub blob/version as a precondition so stale writes are rejected and reconciled. |
| **The repository starts getting messy** | There is no repository-specific growth signal. | Health/maintenance checks report `Healthy`, `Watch`, or `Outgrowing the template` and recommend the smallest structural correction. |
| **You want portability** | Native ChatGPT context is a ChatGPT product capability. | The durable operational layer is ordinary Markdown in a GitHub repository you control. |
| **You just want casual personalization or a one-off chat** | Native ChatGPT is usually the simpler fit. | The repository should stay out of the way. No durable state is a valid route. |

## What each durable layer is for

### `START_HERE.md` - runtime front door

This is the first repository file a fresh session should use when durable state may matter.

It decides whether repository context is needed at all, then routes to global state/knowledge, working-style calibration, or the correct project. It also contains the persistence-routing gate and the growth/scale signals.

### `KNOWLEDGE.md` - stable shared knowledge

This holds compact, supported cross-project facts, definitions, and corrections that materially improve future work but are not current state, decisions, or working-style preferences.

Entries include a basis/source, last-verified field, stale condition when relevant, and supersession links. Time-sensitive facts should not silently become permanent truth.

It is not a transcript, scrapbook, or general personal database. Project-specific knowledge belongs behind that project's front door.

### `WORKING_STYLE.md` - accumulated collaboration calibration

This holds stable preferences about **how the user and ChatGPT work together**, for example:

- preferred communication depth or formatting;
- how much initiative ChatGPT should take;
- evidence and uncertainty standards;
- tool-use and verification preferences;
- approval boundaries;
- recurring workflow conventions;
- corrections that should change future behavior.

It is deliberately **not** a biography or personality dossier. Project state/knowledge does not belong there, and ambiguous model-inferred preferences require confirmation before becoming durable.

### `PROJECTS.md` - project registry and router

Most people who use operational memory for long enough will have more than one ongoing workstream. That should not force all project material into root files.

`PROJECTS.md` is the compact index. Each durable project gets a stable path such as:

`projects/home-renovation/PROJECT.md`

That project front door tells a future session what the project is, when to route there, what the current authority is, and what to load first.

### Root `CURRENT.md` and `DECISIONS.md` - global state only

Root `CURRENT.md` is for cross-project current focus, coordination, constraints, and global open questions.

Root `DECISIONS.md` is for durable decisions that govern multiple projects or the repository as a whole.

Root `KNOWLEDGE.md` is for stable cross-project knowledge.

Once a workstream has its own project boundary, its detailed current state, decisions, and knowledge belong inside that project instead of being duplicated globally.

### `projects/_TEMPLATE/` - latent growth skeleton

The project template includes:

- `PROJECT.md` - project-local front door;
- `CURRENT.md` - transient/current project state;
- `DECISIONS.md` - durable governing project decisions;
- `KNOWLEDGE.md` - stable project facts, definitions, corrections, and compact reference context.

Do **not** instantiate it for every topic. A project earns a durable boundary when it is explicitly ongoing, expected to span sessions, has its own state/constraints/decisions/knowledge, or repeatedly produces durable material that should be retrieved together later.

## The persistence-routing gate

“Record this in operational memory” means **route this correctly**, not “create a file.”

Before a write, ChatGPT should classify the material:

1. **Existing source of record** - update it rather than duplicating state.
2. **Global CURRENT** - cross-project transient/current state.
3. **Global DECISION** - cross-project durable governing decision.
4. **Global KNOWLEDGE** - compact stable cross-project facts/definitions/corrections with no better canonical source.
5. **WORKING STYLE** - stable collaboration preference about how work should be performed.
6. **PROJECT** - project-specific current state, decisions, or knowledge routed through `PROJECTS.md`.
7. **NOT-V1 / no legitimate home** - do not invent structure; surface the mismatch and treat recurrence as a growth signal.

A new durable file outside the provided structure should be exceptional. Before one is created, it needs a distinct role, expected recurrence, a future retrieval trigger, clear authority, navigation from the relevant front door, and human visibility that the structure is expanding.

## Growing without becoming a knowledge junk drawer

This repository is designed to grow by **adding routing boundaries**, not by accumulating miscellaneous files.

A typical progression is:

```text
simple use
  global CURRENT + DECISIONS + KNOWLEDGE
        |
        v
stable collaboration preferences emerge
  WORKING_STYLE
        |
        v
multiple ongoing workstreams emerge
  PROJECTS + project front doors
        |
        v
individual projects need additional canonical artifacts
  register only justified sources in that project's PROJECT.md
        |
        v
routing/indexing itself becomes insufficient
  graduate to structured/indexed/tool-backed memory
```

The project/knowledge skeleton should make the scaling boundary arrive much later than a flat two-file design. A normal user should be able to maintain multiple durable projects and accumulate meaningful shared knowledge without turning the root into an uncontrolled knowledge base.

## Built-in scale signal

A repository health or maintenance check should report:

### `V1 scale status: Healthy`

Routing is clear, global files remain global, project-specific material is behind project front doors, knowledge files remain scoped/compact, working-style entries are compact, and required retrieval is straightforward.

### `V1 scale status: Watch`

Examples:

- project-specific state/knowledge is leaking into global files;
- multiple ongoing durable workstreams are not registered as projects;
- similar material repeatedly has no legitimate home;
- knowledge files are becoming cross-domain scrapbooks or contain duplicated/stale facts;
- working-style entries are duplicative or contradictory;
- compaction is needed unusually often just to understand current state;
- a project front door no longer points cleanly to its current authority.

The first response should be a small structural correction such as registering a project, moving state/knowledge into the project, superseding stale material, or creating one specifically justified source of record.

### `V1 scale status: Outgrowing the template`

Use this only when the routing skeleton itself is no longer sufficient, for example when correct work routinely requires broad repository search, many independent knowledge domains require indexed retrieval, active state/knowledge remains too large after project scoping and compaction, or the user needs deterministic schemas/validation/transactions or a dedicated memory service.

At that point, preserve this repository as a human-readable control layer and add or migrate to structured/indexed/tool-backed memory rather than continuing to bolt on Markdown.

## 60-second operating model

After completing [`SETUP.md`](SETUP.md), normal use should still feel like normal ChatGPT.

When prior durable state matters, say:

> `@GitHub Enter through START_HERE.md in my operational-memory repository and load only the durable state relevant to this task.`

Useful controls include:

- **“Record this in operational memory.”** Route it to the correct existing home.
- **“Update current state with this.”** Use the appropriate global or project current-state file.
- **“Make this a durable decision.”** Record it in the appropriate global or project decision log.
- **“Record this as durable knowledge.”** Use the appropriate global/project `KNOWLEDGE.md` when the fact is supported and future-relevant.
- **“Remember this as a working preference.”** Record it in `WORKING_STYLE.md` when appropriate.
- **“This is an ongoing project.”** Create/register a project boundary when clearly authorized.
- **“Do not persist this.”** Override routine persistence.
- **“What do you currently have recorded about this?”** Retrieve the relevant durable state/knowledge rather than answer from recollection.
- **“Run a repository health check.”** Check routing, consistency, project registry integrity, knowledge/working-style hygiene, branches/root hygiene, and scale status.
- **“Close out operational memory.”** Catch material durable changes that were discussed but not yet persisted.

## Architectural honesty

This is a **lightweight operating protocol**, not a server-side enforcement engine.

GitHub provides durable files, version history, and some mechanical protections such as current-version/blob preconditions when the available integration exposes them. ChatGPT performs retrieval, interpretation, routing, selective persistence, reconciliation, and much failure reporting by following these instructions.

Many safeguards therefore remain behavioral rather than independently enforced.

If you require typed APIs, deterministic schema validation, atomic multi-file transactions, CI-enforced invariants, automated secret scanning, semantic/vector retrieval, or a memory service that can reject invalid state outside the model's discretion, this template is not the final endpoint.

## Failure behavior

The preferred failure model is **closed, loud, and recoverable**.

- incomplete required retrieval -> say so and do not claim the relevant memory is loaded;
- no legitimate persistence destination -> do not invent one;
- stale/concurrent write -> reread and reconcile rather than overwrite;
- unverified write -> do not claim persistence;
- partially completed coupled update -> report the temporary inconsistency and reconcile it before success;
- ambiguous durable decision, knowledge claim, or inferred working preference -> ask before activating it;
- connector unavailable -> say the change was not persisted and use the documented manual fallback.

A visible stop is preferable to a plausible but silently wrong success.

## Setup

Follow [`SETUP.md`](SETUP.md).

Setup verifies that:

1. the user's working copy is private;
2. a write-capable GitHub integration can access the intended repository;
3. create/update/readback/delete operations actually work;
4. existing-file updates can use current version/blob preconditions when supported;
5. persistent ChatGPT instructions point future sessions to `START_HERE.md`;
6. a fresh chat can retrieve a repository-only value it has never previously seen;
7. the user understands the routing/persistence model and optional branch hardening.

## Repository maintenance

The normal steady state uses one canonical branch, `main`. Routine ChatGPT memory writes go directly to `main`; users do not need a feature-branch workflow.

Temporary branches should be compared with `main`, unique work preserved, and removed only when safely incorporated or deliberately abandoned.

Optional light `main` protection can block branch deletion and force pushes without blocking ordinary direct commits. See `SETUP.md`.

A repository health/maintenance check should also verify:

- `START_HERE.md`, `KNOWLEDGE.md`, `WORKING_STYLE.md`, `PROJECTS.md`, root state files, README, SETUP, and LICENSE exist;
- every registered active project has a valid front door;
- every non-template project directory is registered;
- project-specific state/knowledge is not accumulating in global files;
- active/superseded decisions and knowledge are internally consistent;
- working-style entries are compact and non-contradictory;
- no leftover setup test file exists;
- branch/protection state is reported when available;
- `V1 scale status` is reported.

## Privacy and connected-app boundary

Create the user's working copy as a **private GitHub repository** and visibly confirm that GitHub labels it Private before storing personal/project state.

Treat anything committed to Git as durable history. Ordinary deletion does not necessarily erase material from earlier commits.

**Do not store secrets.** Do not persist passwords, API keys, access tokens, private keys, full identity numbers, or full payment/bank information.

Be deliberately conservative with health, legal, financial, employment, client-confidential, relationship, and other sensitive information. `WORKING_STYLE.md` should describe collaboration behavior, not become a personal dossier. `KNOWLEDGE.md` should not become a personal data dump.

Repository content is scoped working data/instructions. It does not authorize exposing unrelated information, changing repository visibility, expanding permissions, connecting other services, or performing unrelated external actions.

## Prior art, lineage, and advanced alternatives

This template did not begin as a reimplementation of another memory repository. It grew from long-running ChatGPT + GitHub operational work at Reference Field, Inc., where repeated collaboration exposed the need for durable state, accumulated knowledge, calibration, corrections, supersession, routing, verification, and recovery.

Later adversarial review and prior-art research found substantial overlap with public work. This project therefore does **not** claim novelty for Git-backed memory, Markdown state, durable decision logs, repository instruction files, project routing, supersession, retrieval-before-work, handoff/closeout, or memory validation.

### Neighboring read-side prior art

Repository-versioned AI instructions are already established:

- **OpenAI Codex `AGENTS.md`** - repository-local instructions for coding agents.
- **Anthropic Claude Code `CLAUDE.md`** - persistent project instructions loaded from files.
- **Cursor Project Rules / `AGENTS.md`** - version-controlled project rules; `.cursorrules` is the older legacy format.

Those systems demonstrate the read-side pattern. This template's narrower emphasis is ordinary ChatGPT use plus mutable operational state/knowledge, conversational writeback, project routing, working-style calibration, explicit supersession, observable retrieval, and post-write verification.

### If you need stronger memory infrastructure

Relevant neighboring systems include:

- **Context Spine v2** - more formal state, authority, handoff, and execution-evidence protocols.
- **Letta / MemFS** - Git-backed memory in a stateful agent harness.
- **Agent Zero** - richer persistent/vector memory in a full agent framework.
- **ProjectMemory** - structured project memory exposed through MCP.
- **context-repository** - formal context/provenance contracts and governance patterns.

These are useful graduation targets when this template's human-readable routing skeleton stops being sufficient.

## Validation status

This repository has undergone design review, adversarial review, prior-art comparison, and live write/readback iteration during development.

The current multi-project/front-door/knowledge/working-style architecture is newer than the original two-file design and has **not yet established longitudinal multi-user reliability**.

Broader reliability claims should wait for repeated testing of:

- fresh-chat front-door routing;
- correct project selection without human coaching;
- wrong-target and partial-retrieval detection;
- knowledge promotion/freshness/supersession without scrapbook growth;
- working-style promotion/supersession without profile creep;
- new-project creation and registry reconciliation;
- concurrent/stale-write handling;
- durable-decision supersession and semantic correctness;
- scale-status detection before uncontrolled knowledge growth;
- longitudinal use by people who did not design the workflow.

## What this does not promise

This is not an infallible memory system, objective source of truth, deterministic control plane, security boundary, compliance system, or background synchronization service.

It cannot know about changes that were never recorded, guarantee automatic GitHub invocation in every conversation, guarantee perfect routing by a nondeterministic model, or guarantee that future ChatGPT/plugin behavior will remain unchanged.

The durable Markdown and routing structure are portable. Automated conversational writeback depends on a supported integration that passes setup testing.

## Disclaimer

This is an experimental reference template. ChatGPT, plugin capabilities, and product behavior can change. Verify consequential state and actions. **Do not store secrets here.** Do not use this repository as the sole system of record for regulated information or mission-critical records.

Licensed under the MIT License. See [`LICENSE`](LICENSE).

Created by **Reference Field, Inc.** · https://referencefield.com
