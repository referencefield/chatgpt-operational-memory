# ChatGPT Operational Memory

A low-infrastructure GitHub template for giving ChatGPT durable, user-owned working state across conversations: current state, decisions, durable knowledge, working preferences, and routed projects.

The goal is not to make ChatGPT remember everything. It is to keep the smaller set of information that genuinely needs to survive a conversation somewhere you can inspect, correct, version, and own.

> **A portable continuity layer for serious ongoing ChatGPT work.**

> **Required ChatGPT capability:** use the **`@GitHub` plugin** and connect/authorize it to the private working repository. This template requires that selected plugin to expose repository **create/update/delete** actions. OpenAI also documents a separate GitHub app/connection used for repository search and analysis that may be read-only; that limitation is **not** evidence that the `@GitHub` plugin itself cannot write. Setup proves the selected path with reversible CRUD/readback before returning READY.
>
> **Plan/surface note:** OpenAI currently makes the Plugin Directory visible across ChatGPT plans, but individual plugin/action availability varies by plan, workspace, role, region, and product surface. Compatibility here is therefore **capability-based, not plan-name-based**. If your account/surface cannot invoke `@GitHub` with repository write actions, this template can support retrieval there but cannot provide write-backed operational memory.

## Fast start

Already have the **`@GitHub` plugin with repository read/write actions** authenticated in ChatGPT?

1. Use this public repository as a template to create your own **private** GitHub repository. Give your working copy any name you want.
2. In ChatGPT, say:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

That is the complete normal setup command. ChatGPT should inspect the repository, discover its runtime front door, and run the activation procedure without requiring the user to name `START_HERE.md`, `PROTOCOL.yaml`, or an “activation handshake.”

Having other repositories connected to GitHub does not change this. The URL selects one exact working repository; activation records that repository's numeric GitHub repository ID, and future automatic routing uses only that ID. If the selected repository cannot be resolved or accessed, ChatGPT should stop rather than choose another connected repository.

ChatGPT should verify the exact repository, confirm that it is private, obtain its GitHub repository ID, check the protocol structure, prove reversible read/write access, remove its diagnostic file, and return either:

**Operational memory: READY**

or

**Operational memory: BLOCKED**

If ChatGPT says “GitHub is read-only,” do not treat that sentence alone as a setup result. Explicitly invoke `@GitHub` and use the access check in `SETUP.md`. The selected plugin's actual repository actions and CRUD/readback result determine readiness.

You do not need to read the repository first. Activation should not create a fake project or personal profile merely to initialize the system.

After READY, just start working.

For automatic routing in future chats, ChatGPT will offer a tiny Custom Instructions bootloader keyed to the working repository's numeric **GitHub repository ID**. That ID is used instead of the repository name, so an ordinary repository rename does **not** require changing the bootloader or migrating your memory.

See [`SETUP.md`](SETUP.md) only if you want the detailed tests or installation explanation.

## Development status

This template is currently **unreleased**. Pre-release changes are being folded into the eventual baseline release rather than published as fake version history. The first real release identifier will be assigned only when the release candidate is frozen.

## What the user experiences

The intended interface is the conversation, not the files.

A user can activate the private repository once, then work normally. When durable repository context matters, ChatGPT enters through `START_HERE.md`, determines the relevant scope, and retrieves only the minimum state needed for the task.

If the user clearly changes something that should govern future work, such as a finalized decision or active project target, a conservative persistence watch can route and persist that change under normal verification rules without requiring a magic “remember this” phrase. Ambiguous, inferred, sensitive, or structurally novel persistence still requires confirmation.

Later, a fresh conversation can ask “Where were we?” and reconstruct the situation from explicit current state and active decisions rather than relying only on conversational recollection.

See [`EXAMPLE.md`](EXAMPLE.md) for a short fictional before/after demonstration.

## How this fits with native ChatGPT memory

This repository complements native ChatGPT memory and conversation history; it does not replace them.

Native memory can continue providing useful conversational continuity. Operational Memory adds an **explicit authority layer** for the smaller subset of information where it matters to know what is current, what superseded what, where the governing state lives, and whether a consequential change actually persisted.

A useful mental model is:

- **conversation** — the normal working surface;
- **tools, files, and web sources** — evidence and execution surfaces when needed;
- **native ChatGPT memory** — useful continuity and personalization;
- **operational memory** — the relatively small set of explicit state, decisions, durable knowledge, and working preferences important enough to govern future work.

The repository should therefore stay selective. It is not a transcript archive and should not turn every useful conversation into a persistence ceremony. If durable state cannot materially change the task, using no repository context is a valid route.

When sources conflict, the user's current instruction still wins. Current verified operational state and active decisions can then serve as explicit authority for ongoing work rather than allowing older native memory or conversational recollection to quietly overrule them.

## What changes in practice

| Situation | ChatGPT without this repo | With this repo |
| --- | --- | --- |
| Fresh chat later | Prior context may be useful but its basis may be unclear. | ChatGPT can retrieve explicit durable state through a scoped front door. |
| “Where were we?” | Reconstruct from available chat/native context. | Retrieve current project/global state and active decisions. |
| Important decision changes | Old and new positions may coexist. | New decision can explicitly supersede the old one. |
| Durable fact becomes stale | Freshness may be unclear. | Knowledge can carry verification/review metadata. |
| Repeated working preference | May need to be re-taught. | Explicit/confirmed collaboration preferences can be stored compactly. |
| Several ongoing projects | Context can blur across conversations. | `PROJECTS.md` routes to the correct project front door. |
| Write claims success | No Git-style receipt is inherent to ordinary chat memory. | Consequential writes are reread and verified; real commit IDs are reported when available. |
| Concurrent/manual edit | Silent overwrite is possible in an unversioned store. | Current blob/version preconditions can reject stale writes. |
| Repository renamed | A name-based pointer may become stale. | The bootloader resolves the same GitHub repository ID to the current owner/name. |
| One-off casual question | Just chat. | Also just chat. No-repository-context is a valid route. |

The practical difference is not **“ChatGPT remembers more.”** It is:

**For the information important enough to govern ongoing work, the user can inspect what is current, what was superseded, where it belongs, and whether changes actually persisted.**

## Architecture

```text
START_HERE.md
    |
    +-- global state
    |      CURRENT.md
    |      DECISIONS.md
    |      KNOWLEDGE.md
    |      WORKING_STYLE.md
    |
    +-- project router
           PROJECTS.md
              |
              +-- projects/<slug>/PROJECT.md
                       |
                       +-- CURRENT.md
                       +-- DECISIONS.md
                       +-- KNOWLEDGE.md
```

`PROTOCOL.yaml` is the machine-readable manifest. `START_HERE.md` is the runtime front door. Detailed procedures are pushed down to `OPERATIONS.md` so normal sessions do not need to load the whole protocol library.

Git history preserves evolution, but **Git history is not current authority**.

## The bootloader principle

Persistent ChatGPT instructions should be tiny. They identify the working repository by GitHub repository ID and point ChatGPT to `START_HERE.md` rather than duplicating the protocol.

At runtime ChatGPT resolves that repository ID to the repository's current owner/name and then retrieves the front door. This means:

- the user may give the private working repository any name;
- an ordinary rename does not require editing Custom Instructions;
- the public template/update source is also identified in `PROTOCOL.yaml` by its immutable GitHub repository ID, so update discovery does not depend on the upstream's current owner/name;
- `referencefield/chatgpt-operational-memory` remains the current human-readable location of that public source, not a required working-repository name;
- if a configured working or template-source repository ID cannot be resolved, ChatGPT should fail visibly rather than guess a similarly named repository.

For users who skip Custom Instructions, the simple manual fallback is:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

The repository URL supplies the only identity ChatGPT cannot infer. Repository-ID resolution, owner/name resolution, and entry through the protocol front door are internal steps, not user commands.

## Controlled persistence

Before writing durable material, the protocol routes it to an existing source of record, global current state, a durable decision, durable knowledge, working style, the correct registered project, or `UNROUTED / no legitimate home`.

The system should not automatically persist brainstorming, discarded alternatives, casual conversation, one-off preferences, or sensitive material merely because it could be useful later.

Working style is for collaboration preferences, not biography or psychological profiling, and it may not be used to suppress honest evaluation, correction, or material risk flagging.

## Verification and failure posture

For consequential writes, the basic closed loop is:

`read -> authorized/routed write -> reread -> verify intended state`

Multi-file changes use a write-set with an explicit postcondition. Tool acknowledgement alone is not proof that the intended durable state exists.

The preferred failure behavior is **closed, loud, and recoverable**:

- missing required retrieval -> report incomplete retrieval;
- configured repository ID cannot be resolved -> stop rather than guess;
- stale write -> reread and reconcile, never force blindly;
- unverified write -> report `not verified`;
- partial multi-file change -> report temporary inconsistency and reconcile;
- required GitHub write actions unavailable -> say that the change was not persisted.

The repository also includes an advisory deterministic validator for structural invariants. It does not pretend to validate semantic truth, correct routing, prompt-injection safety, or model behavior.

## Supported OpenAI surfaces

### ChatGPT Chat

The primary lay-user path is ordinary ChatGPT with the authenticated **`@GitHub` plugin** and its underlying authorized GitHub connection exposing repository read/write actions for the private working repository.

OpenAI separately documents a GitHub app/connection used for repository search and analysis as read-only. That surface is useful for retrieval but cannot satisfy this persistence protocol. Do not generalize that read-only limitation to the `@GitHub` plugin. `SETUP.md` uses the selected plugin's actual actions plus a reversible CRUD test to prove write readiness.

### Codex

The repository includes a tiny root `AGENTS.md` bootloader. Codex enters through the same `PROTOCOL.yaml` and `START_HERE.md`; it should not create a competing Codex-specific memory structure.

### ChatGPT Work

When the same write-capable GitHub plugin/app is available in Work, the same repository and front door apply. Longer multi-step execution does not weaken persistence authorization, routing, privacy, write-set, or readback rules.

### Other models

The Markdown protocol is intentionally portable. Other models may be able to use it when their normal user interface provides equivalent persistent bootstrapping plus scoped GitHub read/write capability. This release does not add speculative provider-specific machinery.

## Privacy and recovery boundaries

Use a **private** working repository. Do not store passwords, tokens, private keys, recovery codes, full payment/bank information, or similar secrets.

A private GitHub repository is private on GitHub, but content retrieved into ChatGPT enters the ChatGPT processing path under the applicable product settings and terms.

Git history is useful recovery evidence but is not an independent backup of the GitHub account/repository itself. If losing the operational-memory repository would be materially costly, keep an independent clone/archive using a backup practice you trust.

See [`SECURITY.md`](SECURITY.md) for details.

## Structural validation and behavioral evals

Two different test surfaces are included:

- `tools/validate_protocol.py` checks machine-verifiable structural invariants and soft warning budgets.
- `EVALS.md` defines adversarial scenarios for model-mediated behavior, including routing, authority, false retrieval/write claims, over-persistence, stale writes, activation, GitHub surface selection, working/upstream repository rename identity, working-style safety boundaries, Codex/Work compatibility, and maintenance failures.

The included GitHub Actions workflow is advisory and intentionally does not run on every direct operational-memory write. It runs for pull requests or when manually dispatched.

`EVAL_RESULTS.md` is the results ledger. It deliberately distinguishes a structural validator PASS from behavioral evidence. No qualifying independent behavioral run is claimed until one is actually performed.

## Feedback and contributions

- **GitHub Discussions**: questions, usage experiences, early ideas, experiments, and show-and-tell.
- **GitHub Issues**: reproducible bugs, setup failures, confusing behavior, and actionable improvements.
- **Pull Requests**: concrete proposed changes. Contributors may fork the public repository and submit a PR directly.
- **Private contact**: `contact@referencefield.com`.

Do not post credentials, private repository contents, or sensitive personal information in public feedback channels.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository map

- `README.md` — product overview and fast start
- `SETUP.md` — detailed installation and fresh-chat tests
- `START_HERE.md` — compact runtime authority/front door
- `PROTOCOL.yaml` — machine-readable protocol and compatibility manifest
- `AGENTS.md` — Codex bootloader
- `OPERATIONS.md` — project creation, write-sets, health, closeout, recovery, maintenance
- `SECURITY.md` — privacy, secrets, recovery boundaries, optional Git hardening
- `MIGRATIONS.md` — release/update rules and controlled release cleanup
- `EXAMPLE.md` — fictional worked example
- `EVALS.md` — adversarial behavioral scenarios
- `EVAL_RESULTS.md` — behavioral-results ledger
- `CONTRIBUTING.md` — contribution routes and design guardrails
- `CURRENT.md`, `DECISIONS.md`, `KNOWLEDGE.md`, `WORKING_STYLE.md` — global durable state
- `PROJECTS.md` — project registry/router
- `projects/_TEMPLATE/` — project skeleton
- `tools/` — advisory structural validator
- `.github/` — contribution forms and advisory validation workflow

## Prior art and positioning

This project grew out of long-running ChatGPT + GitHub operational work at **Reference Field, Inc.** It does **not** claim novelty for Git-backed memory, Markdown state, durable decision logs, supersession, repository-local AI instructions, retrieval-before-work, or validation.

Repository-local AI instruction files are established prior art, including OpenAI Codex `AGENTS.md`, Anthropic Claude Code `CLAUDE.md`, and Cursor project rules. Neighboring or more infrastructure-heavy systems include Context Spine, Letta/MemFS, Agent Zero, ProjectMemory, context-repository, Supersede, and filesystem-based memory research.

This template's narrower proposition is a low-infrastructure, human-readable operational-memory layer for ordinary ChatGPT users who want conversational GitHub writeback, scoped routing, explicit supersession, and post-write verification without first adopting an agent framework or database.

## Validation status and limits

The repository has undergone design review, adversarial review, prior-art comparison, deterministic structural validation, and live GitHub write/readback iteration.

**Longitudinal multi-user reliability has not yet been established.** Many semantically important safeguards remain instructions executed by ChatGPT rather than independently enforced controls.

This is not an infallible memory system, objective source of truth, deterministic control plane, background synchronization service, security boundary, or universal replacement for native ChatGPT memory/Projects.

It cannot know about changes that were never recorded or guarantee future product behavior.

Licensed under the MIT License. See [`LICENSE`](LICENSE).

Created by **Reference Field, Inc.** · https://referencefield.com · contact@referencefield.com
