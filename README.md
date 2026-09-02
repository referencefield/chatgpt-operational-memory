# ChatGPT Operational Memory

A low-infrastructure GitHub template for ChatGPT users who want explicit, user-owned working state with conversational GitHub writeback, scoped retrieval, and post-write verification.

The goal is not to make ChatGPT “remember everything.” It is to keep the smaller set of state, decisions, knowledge, and collaboration preferences that actually need to survive a conversation somewhere you can inspect, correct, version, route, and own.

> **A portable continuity layer for serious ongoing ChatGPT work.**

## What this is architecturally

This is a **small operational-memory protocol**, not a server-side enforcement engine.

GitHub supplies durable files, history, and some mechanical protections such as current-version/blob write preconditions when the integration exposes them. ChatGPT performs routing, interpretation, selective persistence, reconciliation, and semantic checks by following the current protocol in this repository.

Many safeguards therefore remain model-mediated. The repository adds an advisory deterministic validator for structural invariants, but it does not pretend that prose plus Markdown creates a deterministic memory service.

If you need typed APIs, indexed retrieval, atomic transactions, deterministic semantic validation, automatic transcript ingestion, or a dedicated memory server, this template is probably a control layer or stepping stone rather than your final storage architecture.

## Who this is for

This template is intended for people who:

- primarily work in ordinary ChatGPT chats or Projects;
- have ongoing work that spans conversations;
- expect to accumulate more than a handful of isolated facts;
- want important state to remain inspectable and user-owned;
- are comfortable creating a private GitHub repository and connecting ChatGPT to it;
- do not want to install an agent framework, database, MCP server, or command-line tooling merely to get useful continuity.

It is deliberately capable of growing from simple cross-chat continuity into multiple routed projects without turning the repository into an unstructured notes dump.

## What this is good for

Typical uses include:

- **Long-running project continuity:** resume objectives, constraints, current work, open questions, decisions, and durable project knowledge without reconstructing everything from old chats.
- **Durable decisions:** preserve choices that should continue governing future work until explicitly superseded.
- **Stable knowledge and corrections:** retain supported facts/definitions/corrections while giving time-sensitive information freshness metadata.
- **Working-style calibration:** preserve explicit or repeatedly confirmed preferences about how ChatGPT should work with you without constructing a personal dossier.
- **Multiple workstreams:** route future chats to the correct project front door instead of broad-loading unrelated state.
- **Recovery and auditability:** see what changed over time and verify that claimed persistence actually reached GitHub.

## What changes in practice

| Situation | ChatGPT out of the box | With this repo connected |
| --- | --- | --- |
| **Starting a fresh chat later** | ChatGPT may have useful prior context, but you may not know exactly what it is relying on. | ChatGPT can enter through `START_HERE.md`, determine scope, and retrieve the minimum durable state that actually governs the task. |
| **You ask “Where were we?”** | ChatGPT reconstructs from whatever context is available. | The relevant global/project current state and decisions are explicit and inspectable. |
| **You make an important decision** | It exists in the conversation and may influence later work. | You can make it a durable decision with explicit active/superseded status. |
| **You change your mind later** | Old and new positions can coexist across prior conversations or memory. | The newer decision explicitly supersedes the old one so only the active decision governs. |
| **You establish a durable fact** | It may remain in chat/native memory without clear freshness or scope. | Supported durable knowledge can live globally or inside the correct project with provenance/freshness fields. |
| **You repeatedly teach ChatGPT how you work** | Some preferences may be learned natively, but the user may not have a compact inspectable operational profile. | Explicit or confirmed collaboration preferences can accumulate in `WORKING_STYLE.md` with supersession and review metadata. |
| **You accumulate several ongoing projects** | Context may be distributed across many chats/Projects. | `PROJECTS.md` routes to a project-specific `PROJECT.md` front door, then only the minimum project authority is loaded. |
| **You wonder whether something was actually saved** | There is usually no Git-style transaction receipt for an ordinary conversational fact. | Consequential writes use readback verification and real commit receipts when GitHub exposes a commit SHA. |
| **Two sessions/manual edits collide** | Native conversational memory does not expose this as a versioned write problem. | Existing-file updates can use current blob/version preconditions so stale writes are rejected and reconciled. |
| **One intent changes several files** | There is no separate state transaction to inspect. | The protocol establishes a write-set and verifies the complete postcondition, not merely individual API successes. |
| **Something does not fit the existing memory structure** | A user/model may create another note/file ad hoc. | The routing gate reports `NOT-V1 / no legitimate home` unless a new durable home passes an explicit promotion test. |
| **The repository starts getting too complicated** | There is no built-in architectural growth signal. | Health checks report `Healthy`, `Watch`, or `Outgrowing the template`, informed by routing quality and soft budgets. |
| **One-off casual conversation** | Just chat. | Also just chat. No-repository-context is a valid route. |

The practical difference is not **“ChatGPT remembers more.”** It is:

**Out of the box:** “ChatGPT may have useful context available.”

**With this repository:** “For the parts important enough to govern ongoing work, I can inspect what was loaded, where it belongs, what is current, what was superseded, and whether changes actually persisted.”

## Architecture

The repository separates memory by role and scope:

```text
START_HERE.md
    |
    +-- global current/decisions/knowledge
    |      CURRENT.md
    |      DECISIONS.md
    |      KNOWLEDGE.md
    |
    +-- working style
    |      WORKING_STYLE.md
    |
    +-- projects
           PROJECTS.md
              |
              +-- projects/<slug>/PROJECT.md
                       |
                       +-- CURRENT.md
                       +-- DECISIONS.md
                       +-- KNOWLEDGE.md
```

Git history preserves evolution, but **Git history is not current authority**.

`PROTOCOL.yaml` provides the machine-readable protocol version, canonical topology, required project files, validator paths, and soft warning budgets.

## The front-door principle

A fresh session should not preload the repository.

The small persistent ChatGPT instruction installed by `SETUP.md` tells ChatGPT where the operating protocol lives. When durable context matters, ChatGPT retrieves `START_HERE.md`, which routes to the minimum relevant scope.

That means protocol improvements can be made in the repository without asking every user to maintain a long duplicate Custom Instruction.

**Persistent instructions point to the operating system; they do not contain the operating system.**

## Controlled growth instead of a junk drawer

Before durable material is written, it is routed to:

- an existing source of record;
- global current state;
- global durable decision;
- global durable knowledge;
- working-style calibration;
- a registered project;
- or `NOT-V1 / no legitimate home`.

Project-specific material should not keep accumulating in global files after a project boundary has been earned.

A new durable file/category outside the declared structure is exceptional. It must have a distinct role, expected recurrence, retrieval trigger, clear authority, navigation path, and human visibility. If it becomes required protocol structure, the manifest and migration record change with it.

## Verification and write-sets

For consequential writes, the core closed loop is:

`read -> authorized write -> reread -> verify intended state`

Existing-file updates should use the current GitHub blob/version as a precondition when available. Stale/conflicting writes should be reread and reconciled rather than forced.

When one intent affects multiple files, the protocol uses a **write-set**:

`intent + expected writes + current preconditions + required postcondition`

Success means the complete postcondition is verified after rereading all affected targets. A series of successful API calls is not itself the success condition.

## Structural validation and behavioral evals

The repository includes two complementary test surfaces:

- `tools/validate_protocol.py` checks deterministic structural invariants and soft budget warnings.
- `EVALS.md` defines behavioral/adversarial scenarios for model-mediated routing, authority, persistence, failure, privacy boundaries, and lifecycle behavior.

The GitHub workflow is intentionally **advisory at protocol 1.0**. It is not a required status check and does not block ordinary direct ChatGPT writes to `main`.

Structural validation cannot determine whether a fact belongs in the right project or whether a current-state sentence semantically contradicts a decision. Those remain part of the semantic health check in `OPERATIONS.md`.

## Repository map

- **`README.md`** — what the system is, who it is for, and why it differs from ordinary ChatGPT context.
- **`SETUP.md`** — one-time installation and fresh-chat test only.
- **`START_HERE.md`** — runtime routing/persistence authority.
- **`PROTOCOL.yaml`** — machine-readable version/topology/budgets.
- **`OPERATIONS.md`** — project creation, write-sets, closeout, health, recovery, maintenance.
- **`SECURITY.md`** — privacy, secrets, repository-content boundary, optional branch hardening.
- **`MIGRATIONS.md`** — upgrading older private working copies.
- **`EVALS.md`** — adversarial behavioral test cases.
- **`CURRENT.md`** — cross-project current state.
- **`DECISIONS.md`** — cross-project durable decisions.
- **`KNOWLEDGE.md`** — cross-project durable knowledge.
- **`WORKING_STYLE.md`** — durable collaboration preferences/calibration.
- **`PROJECTS.md`** — project registry/router.
- **`projects/_TEMPLATE/`** — four-file skeleton for durable workstreams.

## Setup

Start with [`SETUP.md`](SETUP.md).

Normal use after setup is intentionally simple. When prior state matters, a user can say:

> `@GitHub Enter my operational-memory repository through START_HERE.md and load only the durable state relevant to this task.`

A user should not need to think in Git commands or design repository structure during ordinary work.

## Failure posture

The preferred failure behavior is **closed, loud, recoverable**:

- do not promote uncertain/stale/partially retrieved state into authority;
- do not claim persistence when readback cannot verify it;
- do not force stale writes;
- do not claim a coupled operation complete when only part succeeded;
- preserve the last known good state;
- provide a clear recovery path.

A visible stop is preferable to a plausible but silently wrong success.

## Scale and graduation

The valuable metric is not how much has been remembered. It is **how little needs to be retrieved to reconstruct the situation correctly**.

`PROTOCOL.yaml` contains soft warning budgets. They are not hard limits. Crossing one means inspect the architecture, not delete valid information merely to get under a number.

A normal growth path is:

```text
simple global continuity
        -> accumulated durable knowledge / working style
        -> several routed projects
        -> justified project-specific sources of record
        -> structured/indexed/tool-backed memory only when needed
```

The repository should report `Watch` before it becomes an uncontrolled knowledge base. `Outgrowing the template` is reserved for cases where routing, project scoping, compaction, and supersession are no longer sufficient or deterministic tooling/indexed retrieval has become materially necessary.

## Privacy

Use a private working copy. Do not store secrets. Be conservative with sensitive personal information. Git history can preserve previously committed content.

See [`SECURITY.md`](SECURITY.md) for the full boundary and optional `main` protection guidance.

## Prior art, lineage, and advanced alternatives

This template did **not** begin as a reimplementation of another memory repository. It grew out of long-running ChatGPT + GitHub operational work at **Reference Field, Inc.**, where explicit current state, durable decisions with supersession, retrieve-before-relying, write/readback verification, reconciliation, routing, and conversational closeout became useful through repeated collaboration.

Later adversarial review and prior-art research found substantial overlap with public work. This project therefore does **not** claim novelty for Git-backed memory, Markdown state, durable decision logs, supersession, repository-local AI instructions, retrieval-before-work, or validation.

Repository-local AI instruction files are established read-side prior art, including OpenAI Codex `AGENTS.md`, Anthropic Claude Code `CLAUDE.md`, and Cursor Project Rules / `AGENTS.md`. This template overlaps with that pattern but emphasizes ordinary ChatGPT use, mutable operational state, conversational writeback, scoped project routing, durable knowledge/working-style layers, explicit supersession, observable retrieval, and post-write verification.

Users who need more infrastructure should also examine neighboring systems such as:

- **Context Spine v2** — https://github.com/BerniceHole/context-spine
- **Letta / MemFS** — https://github.com/letta-ai/letta-code
- **Agent Zero** — https://github.com/agent0ai/agent-zero
- **ProjectMemory** — https://github.com/micsh/ProjectMemory
- **context-repository** — https://github.com/evanfollis/context-repository
- **Supersede** — https://github.com/Vrin-cloud/supersede
- **Filesystem-Based Memory for LLM Agents** — https://arxiv.org/abs/2607.26637

These are neighboring work and stronger alternatives for users whose needs exceed this template's deliberately low-infrastructure scope.

## Validation status

The repository has undergone design review, adversarial review, prior-art comparison, and live GitHub write/readback iteration.

**Longitudinal multi-user reliability has not yet been established.** The project should not claim that it eliminates silent failures or that ordinary users will maintain correct state over months until demonstrated empirically.

Protocol 1.0 adds deterministic structural validation and explicit behavioral evals, but many semantically important safeguards remain instructions executed by ChatGPT rather than independently enforced controls.

## What this does not promise

This is not an infallible memory system, objective source of truth, deterministic control plane, compliance system, background synchronization service, or universal replacement for native ChatGPT memory/Projects.

It cannot know about changes that were never recorded, guarantee automatic GitHub invocation in every conversation, or guarantee future ChatGPT/plugin behavior.

The Markdown state is portable. Automated writeback depends on a supported GitHub integration that passes the setup tests.

## Disclaimer

This is an experimental reference template. Verify consequential state and actions. **Do not store secrets here.** Do not use this repository as the sole system of record for regulated information or mission-critical records.

Licensed under the MIT License. See [`LICENSE`](LICENSE).

Created by **Reference Field, Inc.** · https://referencefield.com