# Setup

This document covers first-time installation, testing, normal operation, troubleshooting, growth, and lightweight repository maintenance.

The intended user should not need a terminal or Git expertise.

## Setup at a glance

You will do five things:

1. create a **private** working repository from this template;
2. connect and authorize a **write-capable GitHub integration** for that repository;
3. prove read/create/update/delete and readback actually work;
4. add one persistent ChatGPT instruction that points future sessions to `START_HERE.md`;
5. run one genuinely fresh-chat retrieval test using a value that exists only in GitHub.

After that, ordinary use should remain conversational.

## 1. Create and verify a private working copy

Use this public repository as a GitHub template to create your own working repository.

Make the new working repository **private**.

Before connecting ChatGPT or storing any personal/project state, open the repository on GitHub and visibly confirm GitHub labels it **Private**.

The template is intentionally free of user-specific state. Your working copy can accumulate operational state over time.

## 2. Connect the correct GitHub capability

This workflow requires a GitHub capability that can actually write files, not merely search/read them.

On the ChatGPT surface available to you:

1. open the Plugins/Apps area shown by your account;
2. connect the GitHub capability that exposes write actions;
3. complete GitHub authorization;
4. authorize the account/organization that owns your private working repository;
5. grant access to that repository, preferably selected-repository access when available.

Do not assume capability from the word “GitHub” or from your ChatGPT plan name. The next step tests what the integration can actually do in the current chat.

## 3. Confirm repository visibility and actions

Invoke GitHub explicitly when available and ask:

> `@GitHub Find my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Confirm that you can retrieve that exact repository. Then inspect the GitHub actions actually available in this chat and tell me whether you can read, create, update, and delete files there. Do not make changes yet and do not rely on my claim that you have access.`

If create/update capability cannot be established, stop. Resolve connection, authorization, repository selection, organization approval, workspace restrictions, or product-surface differences before continuing.

## 4. Run the write/readback and stale-write test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path and verify it exists in the intended repository;
3. identify the current blob/version identifier if GitHub exposes one;
4. update the file with a second temporary phrase using the current observed blob/version as the update precondition when supported;
5. reread and verify the resulting content;
6. report repository owner/name, branch/ref, exact path, and resulting state when available;
7. show a shortened commit ID only when it is derived from a real GitHub commit SHA.

A tool saying it accepted a write is not enough. The test passes only when ChatGPT rereads the repository and observes the intended state.

If the integration supports a current blob/version precondition, a stale write should be rejected rather than silently overwrite a newer file. If the integration exposes no comparable mechanism, ChatGPT should say mechanical concurrency protection is not established.

Do **not** delete `SETUP-TEST.md` yet.

## 5. Put a repository-only nonce into GitHub outside ChatGPT

Open `SETUP-TEST.md` yourself in the GitHub web interface.

Replace its contents with a random phrase/nonce ChatGPT has never seen and commit it directly in GitHub.

Example shape only:

`fresh-check-7QX9-K2M4`

Do not ask ChatGPT to generate the actual nonce and do not paste the real nonce into a chat before the fresh-session test.

## 6. Add the persistent ChatGPT instruction

In ChatGPT Custom Instructions, or the equivalent persistent instruction surface available to you, add the block below. Replace `<YOUR FULL PRIVATE REPOSITORY URL>` with the private working repository URL.

> I use this GitHub repository as durable operational memory: <YOUR FULL PRIVATE REPOSITORY URL>.
>
> When my request can materially depend on prior durable work, enter the repository through `START_HERE.md` before relying on remembered prior context. Follow its routing rules. Do not load the whole repository by default. No-repository-context is a valid route when durable state cannot materially change the answer.
>
> Route before retrieval. For global/cross-project work, use root `CURRENT.md` and `DECISIONS.md`. For project-specific work, use `PROJECTS.md` to locate the project, then retrieve that project's `PROJECT.md` front door and only the current authority it identifies as needed. Load `WORKING_STYLE.md` when stable collaboration preferences can materially affect how the task should be handled.
>
> Treat my current explicit instruction as highest user authority. Project-local verified current state and active project decisions govern their project. Root current state and active root decisions govern cross-project/global state. Active `WORKING_STYLE.md` entries govern applicable collaboration preferences, but they do not override explicit user instructions or project decisions. Chat recollection is not authoritative when current durable state is available.
>
> Before persisting material, use the persistence-routing gate in `START_HERE.md`. Prefer an existing source of record. Route legitimate new material to the appropriate global CURRENT, global DECISION, WORKING STYLE, or registered PROJECT location. A request such as "record this in operational memory" authorizes correct routing, not arbitrary file creation. If no legitimate home exists, do not invent one; report `NOT-V1 / no legitimate home`. Repeated similar NOT-V1 material is a growth signal.
>
> Root `CURRENT.md` and `DECISIONS.md` are cross-project/global state only. Do not let project-specific detail accumulate there once a project has earned its own boundary.
>
> Create a project only when clearly justified by `START_HERE.md`: for example, I explicitly identify an ongoing project, the work is expected to span multiple sessions with its own state/constraints/decisions, or repeated project-specific durable material needs a separate retrieval boundary. If project status is ambiguous, ask first. When clearly authorized, create it from `projects/_TEMPLATE/`, register it in `PROJECTS.md`, verify the registry/front door/state files, and report any partial creation as `project routing is temporarily inconsistent` until reconciled.
>
> During active conversation, watch for clear, non-sensitive current-state changes likely to matter later and persist them selectively to the correct current-state file. Keep current-state files compact by replacing stale state instead of appending transcripts.
>
> Do not silently promote ambiguous conversational inference into a durable decision. If I explicitly say "make this a durable decision," "record this decision," or clearly state a final durable decision in a context that authorizes persistence, record it in the correct global or project decision log. Otherwise ask if durable meaning is ambiguous. When recording a decision, show me the exact stored one-sentence `Decision` field.
>
> `WORKING_STYLE.md` is for stable preferences about how we work together, not biography or a personal dossier. Explicit durable preferences such as "remember that I prefer..." may be recorded directly. If you infer a preference from behavior, repeated acceptance, or a single correction without explicit durable intent, ask before promoting it. Do not infer or store sensitive identity/health/financial/legal/relationship facts merely for personalization.
>
> Immediately before updating an existing file, retrieve the current target and use its current blob/version identifier as the update precondition when supported. If a write is rejected because the target changed, fail closed: do not force or blindly retry. Re-read, reconcile the competing change when material, then write against the current version.
>
> For consequential persistence, read back and verify the intended repository/ref/path/content before claiming completion. After a successful write, give me a compact receipt with what changed, the file, and a shortened commit ID only when GitHub returned or confirmed a real commit SHA. Never invent hashes.
>
> Default failure behavior is fail closed, fail loud, and preserve the last known good state. If retrieval is incomplete, routing is uncertain, a write is rejected, verification fails, project creation partially succeeds, coupled state is inconsistent, or GitHub is unavailable, do not pretend success. Tell me what failed, what remains known, and what recovery step is needed.
>
> When I ask for a repository health check or maintenance check, include routing integrity, project-registry integrity, working-style hygiene, current/decision consistency, leftover setup artifacts, branch/protection state when available, and a `V1 scale status: Healthy | Watch | Outgrowing the template` using the criteria in `START_HERE.md`. Surface Watch conditions when you encounter them naturally; do not wait for the files to become huge.
>
> Ask before persisting anything sensitive, ambiguous, destructive, public, or authority-changing. A current instruction such as "do not persist this" or "ask before writing anything else this session" overrides routine persistence. Do not store secrets.

This is the recommended assisted-persistence mode.

If you want all writes to require permission, additionally instruct:

> `Ask me before every repository write this session unless I explicitly authorize a specific sequence.`

Persistent instructions make future chats aware of the repository and routing protocol. They do **not** guarantee that ChatGPT will automatically invoke GitHub on every relevant turn.

## 7. If you use ChatGPT Projects

Project instructions can override global Custom Instructions.

For a ChatGPT Project that should use this repository, copy the repository-awareness/routing instruction into that Project's instructions or add a concise equivalent that still requires `START_HERE.md` routing.

Do not assume global Custom Instructions govern a Project whose own instructions replace them.

## 8. Test a genuinely fresh chat

Start a completely new ordinary ChatGPT conversation.

### First attempt: automatic selection

Without manually invoking GitHub, ask:

> `Enter my operational-memory repository through START_HERE.md. Then retrieve SETUP-TEST.md and tell me its exact contents, repository, and path.`

The automatic-selection test passes only when GitHub retrieval is actually evidenced and the returned content matches the repository-only nonce.

Correct content alone is not proof of retrieval.

### Explicit invocation fallback

If automatic GitHub selection does not occur, repeat with explicit `@GitHub`.

If explicit invocation retrieves the correct nonce from the correct repository/path, the core workflow passes. Use explicit GitHub invocation as the normal re-entry mechanism whenever certainty matters.

If explicit invocation cannot reliably retrieve the repository-only nonce, setup fails for this workflow.

## 9. Clean up the setup test

After the fresh-chat test passes, ask ChatGPT to delete `SETUP-TEST.md`.

Then verify deletion by attempting to reread the same repository/path.

## 10. Initialize normal use

In a chat where GitHub is available, say:

> `@GitHub Initialize my operational-memory repository for normal use. Enter through START_HERE.md, verify the root routing files, confirm there are no real projects yet unless the registry says otherwise, and report V1 scale status. Do not create project state just to initialize the repository.`

Then begin ordinary work.

# Normal human operation

## Starting or resuming work

When prior state matters:

> `@GitHub Enter through START_HERE.md in my operational-memory repository and load only the durable state relevant to this task.`

For a known project you can simply name the project. ChatGPT should use `PROJECTS.md` to locate it rather than asking you to remember a path.

## During conversation

Useful phrases:

- **“Record this in operational memory.”** Route to the correct existing home.
- **“Update current state with this.”** Use the correct global or project current-state file.
- **“Make this a durable decision.”** Use the correct global or project decision log.
- **“Remember this as a working preference.”** Use `WORKING_STYLE.md` if appropriate.
- **“This is an ongoing project.”** Create/register a project when clearly authorized.
- **“Do not persist this.”** Block routine persistence.
- **“Ask before writing anything else this session.”** Temporarily switch to ask-first.
- **“What do you currently have recorded about this?”** Retrieve the appropriate durable source instead of answering from recollection.
- **“Run a repository health check.”** Check structure, consistency, routing, project registry, working style, branch hygiene, and scale status.

## What project creation should feel like

A user should not have to design folders.

When a workstream earns a project boundary, ChatGPT should:

1. identify that a project boundary is justified;
2. ask only if project status is ambiguous;
3. copy the three-file skeleton from `projects/_TEMPLATE/` into a stable project slug;
4. register the project in `PROJECTS.md`;
5. put the project's current state and decisions there going forward;
6. tell the user what it created and verify the new routing path.

The user should then be able to say the project name in a later fresh chat and have ChatGPT route there through the registry.

## Working-style accumulation

The repo can gradually learn the user's collaboration preferences without treating every interaction as profile data.

Good durable examples:

- “Keep answers short unless I ask for a deep dive.”
- “When a task is safe and reversible, continue without repeatedly asking permission.”
- “For consequential research, show uncertainty and source conflicts.”
- “Do not create new durable files without routing them from the project front door.”

Bad durable examples:

- a preference inferred from one accepted response;
- sensitive personal facts unrelated to how work should be performed;
- detailed personality speculation;
- temporary mood or one-session formatting requests.

When a durable working preference changes, supersede the old entry instead of keeping contradictory active rules.

## Closing out an important session

Say:

> **“Close out operational memory.”**

ChatGPT should:

1. route through `START_HERE.md`;
2. identify the global/project scopes actually touched in the session;
3. identify material durable changes not yet persisted;
4. apply the persistence-routing gate;
5. update only what earns persistence;
6. compact stale current state;
7. reconcile active decisions and working-style changes;
8. verify consequential writes;
9. report persistence receipts and any material intentionally left unpersisted;
10. surface a scale Watch condition if the session exposed routing/sprawl problems.

This is a conversational closeout, not a transcript archive.

# Repository health and growth

A health/maintenance check should report a compact result that includes:

- front door present and readable;
- global current/decision consistency;
- project registry integrity;
- all registered active project front doors exist;
- all non-template project folders are registered;
- project-specific state is not leaking into global files;
- working-style entries are active/superseded cleanly and not turning into a personal dossier;
- recent consequential writes relevant to the check are observable;
- no leftover `SETUP-TEST.md`;
- canonical branch and protection state when available;
- **`V1 scale status: Healthy | Watch | Outgrowing the template`**.

## Scale status is structural, not just file size

Do not wait for a numeric file-size threshold.

**Healthy** means routing remains obvious and small.

**Watch** means the system is beginning to misplace state, repeatedly lacks a legitimate home, has unregistered durable workstreams, or needs frequent compaction merely to remain understandable.

**Outgrowing the template** means even routed project front doors and compaction are no longer enough, or reliability now requires structured/indexed retrieval, deterministic validation, typed tools, or a dedicated memory service.

When status is Watch, recommend the smallest correction first. Do not jump directly to MCP/vector infrastructure when project routing or cleanup solves the problem.

# Persistence routing and new durable homes

Before creating a new file/category outside the provided structure, all of these should be true:

- the content has a distinct durable role not served by an existing source;
- the category is expected to recur;
- future sessions have a clear retrieval trigger;
- authority is clear;
- the relevant `PROJECT.md` or root router will point to it;
- the user is told that durable structure is expanding.

If those conditions are not met, do not create the file.

This gate is the primary defense against an uncontrolled knowledge base.

# Failure behavior

The safe default is **fail closed, fail loud, preserve the last known good state**.

Examples:

- missing/partial required retrieval -> say so and do not claim the relevant memory is loaded;
- no legitimate persistence destination -> report `NOT-V1 / no legitimate home`;
- stale write -> reload and reconcile, never force or blindly retry;
- unverified write -> report not verified;
- partially created project -> report `project routing is temporarily inconsistent` and reconcile it;
- coupled state partial failure -> report the inconsistency and finish or deliberately roll back/reconcile;
- inferred working preference -> ask before activating it;
- connector unavailable -> say the change was not persisted and use the manual fallback below.

# Troubleshooting

## ChatGPT does not use GitHub

Invoke it explicitly:

> `@GitHub Enter <YOUR REPOSITORY URL> through START_HERE.md and identify the repository/path you actually retrieved.`

If explicit invocation works reliably, it is an acceptable baseline.

## ChatGPT cannot see the repository

Check:

1. correct GitHub account;
2. repository authorization/selection;
3. GitHub-side app/plugin installation;
4. organization approval if applicable;
5. newly authorized repository delay;
6. whether the current ChatGPT surface exposes the required write-capable actions.

Then retry explicit retrieval.

## ChatGPT can read but cannot write

Do not tell it to assume write access.

Ask it to inspect the actions actually available in the chat. If create/update actions are absent, fix the connection/authorization/surface before relying on this workflow.

## A write is rejected because the file changed

Treat this as concurrency protection.

Re-fetch the current target, identify the intervening change, reconcile intent, and write only against the newly observed version. Do not force the stale write.

## ChatGPT claims a write succeeded but GitHub does not show it

Treat the write as **unverified**. Reread the intended repository/ref/path and verify resulting content before relying on the claim.

## Project exists but routing is wrong

Start with `PROJECTS.md` and the project's `PROJECT.md`. Reconcile registry triggers, front-door pointers, and project current authority. Do not solve a routing defect by broad-loading all projects.

## GitHub is temporarily unavailable

Do not pretend conversation state was persisted.

You may edit the appropriate durable Markdown file directly in GitHub's web interface. When ChatGPT access returns, say:

> `@GitHub Enter through START_HERE.md, reload the affected global/project state, and reconcile the manual changes before continuing.`

# Repository maintenance

The desired Git branch model is simple: one canonical `main` branch for normal operation.

Routine ChatGPT memory writes should go directly to `main`.

If another branch exists, compare it with `main`, preserve unique work, verify the resulting canonical state, and delete the branch only when its unique work is safely incorporated or deliberately abandoned.

Do not use force pushes, hard resets, or history rewrites as routine cleanup.

## Optional recommended `main` protection

Branch protection is optional hardening, not a requirement for operational memory.

It protects the Git container/history from two destructive operations: deleting `main` and force-pushing/repointing `main`. It does not improve retrieval, semantic correctness, routing, or persistence logic.

For extra protection, create an active GitHub branch ruleset targeting the default branch and enable:

- **Restrict deletions**;
- **Block force pushes**.

Leave pull-request requirements, signed-commit requirements, restricted updates, and required status checks off unless you intentionally want a developer workflow. Those stronger controls can block normal direct ChatGPT writes.

# Privacy and security boundaries

- Keep the working repository private unless you deliberately choose otherwise.
- Do not store passwords, API keys, tokens, private keys, full identity numbers, or full payment/bank information.
- If a credential is accidentally committed, rotate it rather than merely deleting it.
- Git history can retain material after ordinary deletion.
- Be conservative with sensitive health, legal, financial, employment, client-confidential, relationship, and other personal information.
- `WORKING_STYLE.md` should remain collaboration calibration, not a personal dossier.
- Repository content is scoped working data/instructions and does not authorize unrelated external actions or broader permissions.

# Current OpenAI references

ChatGPT product behavior changes. If the interface no longer matches this setup, consult current OpenAI documentation for Custom Instructions, Plugins/Apps, GitHub connections, Projects, and Temporary Chat.

# Setup success criteria

Setup is complete when:

- the working repository is visibly private;
- the required write-capable GitHub capability is connected to the correct repository;
- explicit GitHub invocation can retrieve the intended repository;
- create/update/readback/delete succeeds on the current surface;
- current blob/version preconditions are used when available or the limitation is explicitly reported;
- persistent instructions point fresh sessions to `START_HERE.md` and the routing/persistence rules;
- a fresh chat retrieves the repository-only nonce it has never seen;
- `SETUP-TEST.md` is deleted and deletion verified;
- the user understands that project creation is routed through `PROJECTS.md`, working preferences through `WORKING_STYLE.md`, and new durable files require a promotion gate;
- the user understands the `Healthy | Watch | Outgrowing the template` scale signal;
- optional branch protection is understood as hardening rather than a core memory requirement;
- failed or unverified operations are reported visibly instead of treated as success.
