# ChatGPT Operational Memory

A low-infrastructure GitHub template for giving ChatGPT durable, user-owned working state across conversations: current state, decisions, durable knowledge, working preferences, and routed projects.

The goal is not to make ChatGPT remember everything. It is to keep the smaller set of information that genuinely needs to survive a conversation somewhere you can inspect, correct, version, and own.

> **A portable continuity layer for serious ongoing ChatGPT work.**

## Get started: Create → Connect → Activate

You only need to do this once. You do **not** need Git expertise, a terminal, or knowledge of the repository's internal protocol.

### 1. Create

[**Create my private memory repository**](https://github.com/new?owner=%40me&template_owner=referencefield&template_name=chatgpt-operational-memory&visibility=private)

GitHub should open a new-repository form using this template with **Private** preselected. Choose any repository name, visibly confirm **Private**, and create it.

### 2. Connect

In ChatGPT, install/select the **`@GitHub` plugin**, sign in to GitHub, and authorize the private memory repository you just created. Prefer access to only that repository when available; unrelated repositories are not needed.

**Requires:** `@GitHub` with repository write actions. Setup checks this automatically. OpenAI also documents a separate GitHub app/connection used for repository search and analysis that may be read-only; that separate limitation is not proof that the `@GitHub` plugin cannot write.

Availability varies by account and ChatGPT surface, so compatibility is based on the actions actually available rather than a hard-coded plan name.

### 3. Activate

Copy the URL of your new private repository and send:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

That's it.

ChatGPT should verify the exact repository, Private visibility, safe read/write, verified readback, cleanup of its temporary setup test, and protocol structure without making you perform those technical checks.

Success begins:

**Operational memory: READY**

Then ChatGPT should give you **one completed Custom Instructions block** to copy into ChatGPT so future conversations can find the same repository. The repository's numeric ID is already embedded; you do not need to understand or type it yourself.

After that, talk normally. For example:

- `Where were we on my project?`
- `Remember that I've decided to use option B.`
- `Update my current project status.`
- `What do you currently have recorded about this?`

You can explicitly invoke it anytime with:

> `@GitHub Use my operational memory.`

If setup cannot safely complete, ChatGPT should return **Operational memory: BLOCKED**, show one plain-language problem and one **Fix**, then ask you to say **`Retry setup.`** after fixing it. It should not dump repository IDs, blob details, or protocol jargon unless you ask.

See [`SETUP.md`](SETUP.md) for advanced verification and troubleshooting.

## Development status

This template is currently **unreleased**. Pre-release changes are being folded into the eventual baseline release rather than published as fake version history. The first real release identifier will be assigned only when the release candidate is frozen.

## What the user experiences

The intended interface is the conversation, not the files.

A user activates the private repository once, copies the completed bootloader once, then works normally. When durable repository context matters, ChatGPT enters through `START_HERE.md`, determines the relevant scope, and retrieves only the minimum state needed.

If the user clearly changes something that should govern future work, such as a finalized decision or active project target, a conservative persistence watch can route and persist that change under normal verification rules without requiring a magic “remember this” phrase. Ambiguous, inferred, sensitive, or structurally novel persistence still requires confirmation.

Later, a fresh conversation can ask “Where were we?” and reconstruct the situation from explicit current state and active decisions rather than relying only on conversational recollection.

See [`EXAMPLE.md`](EXAMPLE.md) for a fictional before/after demonstration.

## How this fits with native ChatGPT memory

This repository complements native ChatGPT memory and conversation history; it does not replace them.

Native memory can continue providing useful conversational continuity. Operational Memory adds an **explicit authority layer** for the smaller subset of information where it matters to know what is current, what superseded what, where governing state lives, and whether a consequential change actually persisted.

A useful mental model is:

- **conversation** — normal working surface;
- **tools, files, and web sources** — evidence and execution when needed;
- **native ChatGPT memory** — continuity and personalization;
- **operational memory** — explicit state, decisions, durable knowledge, and working preferences important enough to govern future work.

The repository should stay selective. It is not a transcript archive. If durable state cannot materially change the task, using no repository context is a valid route.

When sources conflict, the user's current instruction wins. Current verified operational state and active decisions can then serve as explicit authority rather than allowing older memory or recollection to quietly overrule them.

## What changes in practice

| Situation | ChatGPT without this repo | With this repo |
| --- | --- | --- |
| Fresh chat later | Prior context may be useful but its basis may be unclear. | ChatGPT can retrieve explicit durable state through a scoped front door. |
| “Where were we?” | Reconstruct from available chat/native context. | Retrieve current project/global state and active decisions. |
| Important decision changes | Old and new positions may coexist. | New decision can explicitly supersede the old one. |
| Durable fact becomes stale | Freshness may be unclear. | Knowledge can carry verification/review metadata. |
| Repeated working preference | May need to be re-taught. | Explicit collaboration preferences can be stored compactly. |
| Several ongoing projects | Context can blur. | `PROJECTS.md` routes to the correct project front door. |
| Write claims success | No Git-style receipt is inherent to chat memory. | Consequential writes are reread and verified. |
| Concurrent/manual edit | Silent overwrite is possible in an unversioned store. | Current version/blob preconditions can reject stale writes. |
| Repository renamed | A name-based pointer may become stale. | The bootloader resolves the same GitHub repository ID to its new owner/name. |
| One-off casual question | Just chat. | Also just chat. No-repository-context is valid. |

The practical difference is not **“ChatGPT remembers more.”** It is:

**For information important enough to govern ongoing work, the user can inspect what is current, what was superseded, where it belongs, and whether changes actually persisted.**

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

`PROTOCOL.yaml` is the machine-readable manifest. `START_HERE.md` is the runtime front door. Detailed procedures live in `OPERATIONS.md` so normal sessions do not need to load the whole protocol library.

Git history preserves evolution, but **Git history is not current authority**.

## The bootloader principle

Persistent ChatGPT instructions should be tiny. Activation obtains the working repository's stable numeric GitHub repository ID and fills it into a completed Custom Instructions block for the user to copy.

The user does not need to understand or manually manage the ID. ChatGPT uses it internally so an ordinary repository rename does **not** require editing the bootloader or migrating durable state.

At runtime ChatGPT resolves that ID to the repository's current owner/name and retrieves `START_HERE.md`. If the ID cannot be resolved, ChatGPT should fail visibly rather than guess a similarly named repository.

For users who skip Custom Instructions, the simple manual fallback is:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

Repository resolution and front-door entry are internal steps, not user commands.

## Controlled persistence

Before writing durable material, the protocol routes it to an existing source of record, global current state, a durable decision, durable knowledge, working style, the correct registered project, or `UNROUTED / no legitimate home`.

The system should not automatically persist brainstorming, discarded alternatives, casual conversation, one-off preferences, or sensitive material merely because it could be useful later.

Working style is for collaboration preferences, not biography or psychological profiling, and it may not suppress honest evaluation, correction, or material risk flagging.

## Verification and failure posture

For consequential writes, the basic closed loop is:

`read -> authorized/routed write -> reread -> verify intended state`

Multi-file changes use a write-set with an explicit postcondition. Tool acknowledgement alone is not proof that the intended durable state exists.

The preferred failure behavior is **closed, loud, and recoverable**. During setup that is deliberately translated into a lay-user response: **BLOCKED → one problem → one Fix → Retry setup.** Technical diagnostics remain available when requested.

The repository also includes an advisory deterministic validator for structural invariants. It does not pretend to validate semantic truth, correct routing, prompt-injection safety, or model behavior.

## Supported OpenAI surfaces

### ChatGPT Chat

The primary lay-user path is ordinary ChatGPT with the authenticated **`@GitHub` plugin** exposing repository read/write actions for the private working repository.

OpenAI separately documents a GitHub app/connection used for repository search and analysis as read-only. That surface can support retrieval but cannot satisfy this persistence protocol. Do not generalize its read-only limitation to the selected `@GitHub` plugin; `SETUP.md` uses actual exposed actions plus reversible CRUD/readback to determine readiness.

### Codex

The repository includes a tiny root `AGENTS.md` bootloader. Codex enters through the same `PROTOCOL.yaml` and `START_HERE.md`; it should not create a competing Codex-specific memory structure.

### ChatGPT Work

When equivalent write-capable GitHub actions are available in Work, the same repository and front door apply. Longer multi-step execution does not weaken persistence authorization, routing, privacy, write-set, or readback rules.

### Other models

The Markdown protocol is intentionally portable. Other models may be able to use it when their normal interface provides equivalent persistent bootstrapping plus scoped GitHub read/write capability. This release does not add speculative provider-specific machinery.

## Privacy and recovery boundaries

Use a **private** working repository. Do not store passwords, tokens, private keys, recovery codes, full payment/bank information, or similar secrets.

A private GitHub repository is private on GitHub, but content retrieved into ChatGPT enters the ChatGPT processing path under the applicable product settings and terms.

Git history is useful recovery evidence but is not an independent backup of the GitHub account/repository itself. If losing the operational-memory repository would be materially costly, keep an independent clone/archive using a backup practice you trust.

See [`SECURITY.md`](SECURITY.md) for details.

## Structural validation and behavioral evals

Two different test surfaces are included:

- `tools/validate_protocol.py` checks machine-verifiable structural invariants and soft warning budgets.
- `EVALS.md` defines adversarial scenarios for model-mediated behavior, including routing, authority, false retrieval/write claims, over-persistence, activation, GitHub surface selection, onboarding failure recovery, repository identity/rename behavior, working-style safety, compatibility, and maintenance failures.

The included GitHub Actions workflow is advisory and intentionally does not run on every direct operational-memory write. It runs for pull requests or when manually dispatched.

`EVAL_RESULTS.md` is the results ledger. It deliberately distinguishes a structural validator PASS from behavioral evidence. No qualifying independent behavioral run is claimed until one is actually performed.

## Feedback and contributions

- **GitHub Discussions**: questions, usage experiences, early ideas, experiments, and show-and-tell.
- **GitHub Issues**: reproducible bugs, setup failures, confusing behavior, and actionable improvements.
- **Pull Requests**: concrete proposed changes.
- **Private contact**: `contact@referencefield.com`.

Do not post credentials, private repository contents, or sensitive personal information in public feedback channels.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository map

- `README.md` — product overview and beginner start
- `SETUP.md` — beginner setup plus advanced verification/troubleshooting
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
