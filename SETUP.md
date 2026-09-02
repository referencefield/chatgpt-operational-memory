# Setup

This document is installation only. Runtime behavior lives in `START_HERE.md`; ongoing maintenance and recovery live in `OPERATIONS.md`; privacy/security guidance lives in `SECURITY.md`; protocol upgrades live in `MIGRATIONS.md`.

The intended user should not need a terminal or Git expertise for normal use.

## Fast path if GitHub is already authenticated in ChatGPT

If you already have the GitHub plugin installed/authenticated and you created a **private** working copy from this template, you do not need to read the rest of this file before starting.

In ChatGPT, say:

> `@GitHub Activate my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Use START_HERE.md and run the activation handshake.`

ChatGPT should then verify the exact repository, confirm it is private, retrieve the protocol/front door, check the declared structure, run a reversible create/read/update/read/delete diagnostic through the GitHub plugin, remove the diagnostic file, and return a compact **Operational memory: READY** or **Operational memory: BLOCKED** receipt.

Activation does not create a project or record personal state merely to mark the repository initialized.

One thing cannot be installed by repository writeback: the optional persistent ChatGPT bootloader that helps future chats enter the repository automatically when durable context matters. After activation, ChatGPT should give you that small block if you have not already installed it. If you skip that step, nothing in the repository breaks; begin relevant future chats with:

> `@GitHub Use my operational memory at <YOUR FULL PRIVATE REPOSITORY URL>`

The detailed procedure below exists for users who want to inspect or independently test each setup step.

## Setup at a glance

You will do five things:

1. create a **private** working repository from this template;
2. install and authenticate the **GitHub plugin** in ChatGPT and authorize it for that repository;
3. prove read/create/update/delete and readback actually work through `@GitHub`;
4. add one small persistent ChatGPT instruction that points future sessions to `START_HERE.md`;
5. optionally run a stronger genuinely fresh-chat retrieval test using a value that exists only in GitHub.

After that, ordinary use should remain conversational.

## 1. Create and verify a private working copy

Use this public repository as a GitHub template to create your own working repository.

Make the working repository **private** and visibly confirm GitHub labels it Private before storing personal/project state.

The public template contains protocol structure, not user-specific memory.

## 2. Install and authenticate the GitHub plugin

The normal ChatGPT path for this template is the **GitHub plugin with repository read/write actions**, invoked with `@GitHub` when repository access is needed.

1. open ChatGPT's **Plugins** area;
2. install/select the GitHub plugin;
3. connect/authenticate the underlying GitHub account when prompted;
4. authorize the account or organization that owns your private working repository;
5. grant the plugin access to that repository, preferably selected-repository access when available.

If you also encounter a different GitHub connection that only exposes repository search/read, that is **not** the setup path documented by this template. Use the GitHub plugin described above.

The action test below confirms that authentication, repository selection, and permissions are working correctly for your private copy. It is not an optional substitute for installing the plugin.

## 3. Confirm repository access and write actions

In ChatGPT, explicitly invoke the plugin:

> `@GitHub Find my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Confirm that you can retrieve that exact repository and that the authenticated GitHub plugin can read, create, update, and delete files there. Do not make changes yet.`

If this fails, correct the plugin connection, GitHub authorization, selected repository, or organization approval before continuing.

## 4. Run the write/readback and stale-write test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path and verify it exists in the intended repository;
3. identify the current blob/version identifier when GitHub exposes one;
4. update the file with a second phrase using the current observed blob/version as the update precondition when supported;
5. reread and verify the resulting content;
6. report repository owner/name, branch/ref, exact path, and resulting state when available;
7. show a shortened commit ID only when it is derived from a real GitHub commit SHA.

A write acknowledgement is not enough. The test passes only when ChatGPT rereads the repository and observes the intended state.

If a deliberately stale update is rejected, that is a concurrency-safety success. ChatGPT should reread/reconcile rather than force or blindly retry.

Do **not** delete `SETUP-TEST.md` yet if you intend to run the stronger fresh-chat nonce test below. Otherwise, delete it and verify deletion after the CRUD diagnostic passes.

## 5. Optional stronger repository-only nonce test

This step is not required for the fast activation path. It independently tests fresh-chat retrieval using information ChatGPT has never seen.

Open `SETUP-TEST.md` yourself in GitHub's web interface. Replace its contents with a random phrase/nonce ChatGPT has never seen and commit it directly in GitHub.

Example shape only:

`fresh-check-7QX9-K2M4`

Do not ask ChatGPT to generate the actual nonce and do not paste the real nonce into a chat before the fresh-session test.

## 6. Add the persistent ChatGPT bootloader

The persistent instruction should identify **where the current protocol lives**, not duplicate the protocol itself.

Add this block to ChatGPT Custom Instructions, or the equivalent persistent instruction surface available to you. Replace `<YOUR FULL PRIVATE REPOSITORY URL>` with your private working repository URL.

> I use this GitHub repository as durable operational memory: <YOUR FULL PRIVATE REPOSITORY URL>.
>
> When my request can materially depend on prior durable work, retrieve `START_HERE.md` from that repository before relying on remembered context. `START_HERE.md` defines the repository's current routing and persistence protocol; follow it rather than relying on an older copy of the protocol in chat or memory. Do not load the whole repository by default.
>
> If the repository cannot be retrieved, routing cannot be established, or a persistence write cannot be verified, say so rather than claiming operational memory was loaded or persisted.

That is the complete recommended persistent instruction.

**Why it is intentionally small:** protocol rules evolve in the repository. A bootloader avoids maintaining two copies of routing/authority/failure rules and reduces configuration drift.

If you use a ChatGPT Project whose own instructions override global Custom Instructions, add the same small bootloader there when that Project should use this repository.

## 7. Test a genuinely fresh chat

If you performed the repository-only nonce test, start a completely new ordinary ChatGPT conversation.

First try:

> `Enter my operational-memory repository through START_HERE.md. Then retrieve SETUP-TEST.md and tell me its exact contents, repository, and path.`

If ChatGPT does not invoke GitHub automatically, repeat with explicit plugin invocation:

> `@GitHub Enter my operational-memory repository through START_HERE.md. Then retrieve SETUP-TEST.md and tell me its exact contents, repository, and path.`

The test passes only when repository retrieval is actually evidenced and the returned content matches the repository-only nonce. Correct content alone is not proof of retrieval.

For consequential repository work, explicit `@GitHub` invocation is always acceptable and removes ambiguity about which plugin should be used.

## 8. Clean up the test

After the fresh-chat test passes, ask ChatGPT to delete `SETUP-TEST.md` and verify deletion by attempting to reread the exact repository/path.

## 9. Initialize normal use

The fast path's activation handshake already performs this initialization check. Otherwise say:

> `@GitHub Activate my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Use START_HERE.md and run the activation handshake.`

Then begin ordinary work.

## Codex

Codex is optional and is not required for the lay-user workflow.

The repository includes a root `AGENTS.md` bootloader. When Codex opens the repository, that file points it to `PROTOCOL.yaml` and `START_HERE.md` so Codex uses the same routing, authority, persistence, and verification model rather than inventing a second protocol.

Do not copy the whole runtime protocol into `AGENTS.md`.

## ChatGPT Work

ChatGPT Work can use the same authenticated GitHub plugin and the same repository front door. There is no separate Work-specific memory store in this template.

When using Work for a longer multi-step task, enter through `START_HERE.md` when durable repository context matters and keep the same persistence, write-set, and readback rules. If the Work surface provides a persistent instruction area, point it to `START_HERE.md` rather than duplicating the protocol.

## Optional `main` protection

Branch protection is optional hardening, not a requirement for operational memory. If desired, protect the default branch against deletion and force pushes while leaving ordinary direct commits allowed. See `SECURITY.md` for the exact rationale and configuration.

## Setup success criteria

Setup is complete when:

- the working repository is visibly private;
- the GitHub plugin is installed/authenticated and authorized for the intended repository;
- explicit `@GitHub` invocation retrieves the intended repository;
- create/update/readback/delete succeeds through the plugin;
- current blob/version preconditions are used when available or their absence is explicitly reported;
- `SETUP-TEST.md` is removed after diagnostics unless intentionally retained for the optional nonce test;
- failed or unverified operations are reported visibly instead of treated as success.

For automatic future routing, also install the small persistent bootloader. Without it, explicit `@GitHub Use my operational memory at <repository URL>` remains the supported manual entry path.

For normal use after setup, start with `START_HERE.md` and consult `OPERATIONS.md` only when you need project creation, closeout, health checks, recovery, update checks, or maintenance.