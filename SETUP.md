# Setup

This document is installation only. Runtime behavior lives in `START_HERE.md`; ongoing maintenance and recovery live in `OPERATIONS.md`; privacy/security guidance lives in `SECURITY.md`; protocol upgrades live in `MIGRATIONS.md`.

The intended user should not need a terminal or Git expertise for normal use.

> **Required ChatGPT capability:** this setup uses the **`@GitHub` plugin** with repository **read/write actions**. OpenAI also documents a separate GitHub app/connection used for repository search/analysis that may be read-only. Do not treat that separate app's limitation as proof that `@GitHub` cannot write. The selected `@GitHub` plugin's exposed actions plus the reversible CRUD/readback test below determine readiness.
>
> **Plan/surface note:** plugin availability is not safely inferred from a plan name alone. OpenAI currently says plugin availability can vary by plan, workspace, role, region, surface, and included app capabilities. If `@GitHub` with repository create/update/delete actions is unavailable on the current account/surface, this write-backed setup cannot reach READY there.

## Fast path if write-capable GitHub access is already authenticated in ChatGPT

If you already have the **`@GitHub` plugin with repository read/write actions** installed/authenticated and you created a **private** working copy from this template, you do not need to read the rest of this file before starting.

In ChatGPT, say:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

That is the complete normal setup command. ChatGPT should inspect the repository, discover the runtime front door, and run the activation procedure without requiring you to name `START_HERE.md`, `PROTOCOL.yaml`, or an “activation handshake.”

Having several other repositories connected or authorized does not make setup ambiguous. The URL identifies one exact working repository. Activation captures that repository's numeric GitHub repository ID, and the optional bootloader uses only that ID in future chats. If that exact repository cannot be resolved or accessed, ChatGPT should stop rather than choose another repository.

ChatGPT should verify the exact repository, confirm it is private, retrieve the protocol/front door, obtain the repository's GitHub repository ID, check the declared structure, run a reversible create/read/update/read/delete diagnostic through the selected write-capable `@GitHub` plugin, remove the diagnostic file, and return a compact **Operational memory: READY** or **Operational memory: BLOCKED** receipt.

A successful receipt should include the repository's numeric GitHub repository ID. That ID is the preferred long-lived identifier for future ChatGPT routing because the repository owner/name may later change without changing the repository itself.

Activation does not create a project or record personal state merely to mark the repository initialized.

One thing cannot be installed by repository writeback: the optional persistent ChatGPT bootloader that helps future chats enter the repository automatically when durable context matters. After activation, ChatGPT should give you the small repository-ID bootloader below, filled with the verified ID from the activation receipt.

If you skip that step, nothing in the repository breaks. For a relevant future chat, paste the current private repository URL and say:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

ChatGPT should handle repository resolution and entry through the protocol internally. You do not need to remember a repository ID, file path, or routing command.

The detailed procedure below exists for users who want to inspect or independently test each setup step.

## Setup at a glance

You will do five things:

1. create a **private** working repository from this template; the working repository may have any name you want;
2. install/authenticate the **`@GitHub` plugin**, connect/authorize its GitHub account access for the intended repository, and confirm repository **write actions** are available;
3. prove read/create/update/delete and readback actually work through `@GitHub`;
4. add one small persistent ChatGPT instruction containing the working repository's GitHub repository ID;
5. optionally run a stronger genuinely fresh-chat retrieval test using a value that exists only in GitHub.

After that, ordinary use should remain conversational.

## 1. Create and verify a private working copy

Use this public repository as a GitHub template to create your own working repository.

Give the private working repository any owner/name you want. The name is not part of the operational-memory protocol and does not need to match this public template.

Make the working repository **private** and visibly confirm GitHub labels it Private before storing personal/project state.

The public template contains protocol structure, not user-specific memory.

GitHub template copies do **not** inherit this public repository's branch-protection/ruleset configuration. Protection is optional hardening that you configure separately on your own working repository if you want it; see **Optional `main` protection** below.

The template also includes an advisory GitHub Actions validator. In a derived working copy it does **not** run on every direct operational-memory write; it runs for pull requests or when manually dispatched. It is not a required status check.

## 2. Install and authenticate the write-capable `@GitHub` plugin

OpenAI currently uses both **plugin** and **app** terminology. For this template, the distinction matters:

- the normal write-backed path is the **GitHub plugin invoked as `@GitHub`**, when that plugin exposes repository read/write actions;
- OpenAI also documents a separate GitHub app/connection for repository search and analysis that may be **read-only**;
- the existence of that read-only app must **not** be generalized into “ChatGPT cannot write to GitHub.”

The public GitHub plugin listing identifies GitHub as having **Write** capability. Actual availability still depends on the current account/surface and its authorization/action controls, so the test below remains authoritative.

1. open ChatGPT's **Plugins** area, or the equivalent plugin/app surface available to your account;
2. install/select the **GitHub plugin**;
3. connect/authenticate the GitHub account/app access it requests;
4. authorize the account or organization that owns your private working repository;
5. grant access to that repository, preferably selected-repository access when available;
6. invoke it as **`@GitHub`** in ChatGPT;
7. confirm that the selected plugin exposes repository create/update/delete actions, not only search/read.

If ChatGPT responds that “GitHub is read-only,” first verify that the request actually selected `@GitHub` and inspect/test the actions available to that plugin. Do not stop setup solely because the model recalls documentation for the separate read-only GitHub app.

The action test below is the authoritative check. If create/update/delete actions are unavailable on the selected `@GitHub` plugin, activation must not claim persistence readiness.

### Plan and surface availability

Do not rely on a hard-coded plan list in this repository. OpenAI currently states that the Plugin Directory is visible across ChatGPT plans, while installation/use of an individual plugin depends on plan, workspace, role, region, supported surface, and the capabilities of its included apps.

For this template, the practical requirement is simple: the current ChatGPT account/surface must let the user invoke **`@GitHub` with repository create/update/delete actions**. If those actions are unavailable, the repository can still be read where supported, but write-backed operational memory is unavailable on that surface.

## 3. Confirm repository access, identity, and write actions

For the detailed no-write access check, say:

> `@GitHub Check operational-memory access to <YOUR PRIVATE REPOSITORY URL>. Don't change anything.`

ChatGPT should retrieve that exact repository, report its GitHub repository ID, and determine whether the selected `@GitHub` plugin exposes the repository read/create/update/delete actions needed by the later diagnostic. Those implementation checks are ChatGPT's job; the user should not have to spell them out in the command.

The repository ID is the stable identifier the bootloader will use. The current owner/name remains useful for human-readable receipts but is not the durable routing key.

If this fails, correct the plugin/app connection, GitHub authorization, selected repository, organization approval, or available action permissions before continuing.

## 4. Run the write/readback and stale-write test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path and verify it exists in the intended repository;
3. identify the current blob/version identifier when GitHub exposes one;
4. update the file with a second phrase using the current observed blob/version as the update precondition when supported;
5. reread and verify the resulting content;
6. report repository ID, current owner/name, branch/ref, exact path, and resulting state when available;
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

The persistent instruction should identify the **working repository by GitHub repository ID**, then point to the current protocol. It should not duplicate the protocol itself.

Use the repository ID reported by the activation handshake or Step 3 above. Add this block to ChatGPT Custom Instructions, or the equivalent persistent instruction surface available to you. Replace `<YOUR REPOSITORY ID>` with that numeric ID.

> I use GitHub repository ID <YOUR REPOSITORY ID> as durable operational memory.
>
> When my request can materially depend on prior durable work, use `@GitHub` to resolve that repository ID to its current owner/name, then retrieve `START_HERE.md` from that repository before relying on remembered context. `START_HERE.md` defines the repository's current routing and persistence protocol; follow it rather than relying on an older copy of the protocol in chat or memory. Do not load the whole repository by default.
>
> If the repository ID cannot be resolved, routing cannot be established, or a persistence write cannot be verified, say so rather than guessing a replacement repository or claiming operational memory was loaded or persisted.

That is the complete recommended persistent instruction.

**Why it uses repository ID instead of URL:** GitHub owner/name is human-facing and can change. The repository ID identifies the repository independently of an ordinary rename, so renaming the working repository does not require editing this bootloader.

If ownership/organization changes cause the GitHub plugin/app to lose permission to the repository, reconnect or reauthorize access as needed. That is an access problem, not a memory migration; the repository ID and bootloader do not change merely because the repository was renamed.

**Why the instruction is intentionally small:** protocol rules evolve in the repository. A bootloader avoids maintaining two copies of routing/authority/failure rules and reduces configuration drift.

If you use a ChatGPT Project whose own instructions override global Custom Instructions, add the same small repository-ID bootloader there when that Project should use this repository.

## 7. Test a genuinely fresh chat

If you performed the repository-only nonce test and installed the bootloader, start a completely new ordinary ChatGPT conversation and say only:

> `@GitHub Read SETUP-TEST.md from my operational memory.`

That short request is deliberate. The test is meant to prove that the installed bootloader supplies the repository identity and that ChatGPT performs repository resolution and protocol entry without the user restating those mechanics.

If you intentionally skipped the bootloader, use the repository URL instead:

> `@GitHub Read SETUP-TEST.md from <YOUR REPOSITORY URL>.`

The test passes only when repository retrieval is actually evidenced and the returned content matches the repository-only nonce. Correct content alone is not proof of retrieval.

For consequential repository work, explicit `@GitHub` invocation is always acceptable and removes ambiguity about which plugin/app should be used.

## 8. Clean up the test

After the fresh-chat test passes, ask ChatGPT to delete `SETUP-TEST.md` and verify deletion by attempting to reread the exact repository/path.

## 9. Initialize normal use

The fast path's activation handshake already performs this initialization check. Otherwise say:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

ChatGPT should discover the repository's front door and activation procedure itself. Then begin ordinary work.

## Repository rename behavior

Renaming the private working repository is supported.

The repository's internal protocol and durable state do not depend on its owner/name. Future sessions should resolve the configured repository ID to the current owner/name before retrieval. A normal rename therefore requires **no** memory migration and **no** Custom Instructions/bootloader edit.

If the configured repository ID stops resolving, fail closed and investigate access/deletion/authorization. Do not silently switch to another repository merely because its name looks similar.

## Codex

Codex is optional and is not required for the lay-user workflow.

The repository includes a root `AGENTS.md` bootloader. When Codex opens the repository, that file points it to `PROTOCOL.yaml` and `START_HERE.md` so Codex uses the same routing, authority, persistence, and verification model rather than inventing a second protocol.

Do not copy the whole runtime protocol into `AGENTS.md`.

## ChatGPT Work

When the same write-capable GitHub plugin/app is available in Work, the same repository and front door apply. There is no separate Work-specific memory store in this template.

When using Work for a longer multi-step task, resolve the same working repository ID and enter through `START_HERE.md` when durable repository context matters. Keep the same persistence, write-set, and readback rules. If the Work surface provides a persistent instruction area, use the same repository-ID bootloader rather than duplicating the protocol.

## Optional `main` protection

Branch protection is optional hardening, not a requirement for operational memory. **Protection rules on the public template do not transfer to a repository created with “Use this template.”** If desired, configure protection on your own working repository against deletion and force pushes while leaving ordinary direct commits allowed. See `SECURITY.md` for the exact rationale and configuration.

## Setup success criteria

Setup is complete when:

- the working repository is visibly private;
- the **`@GitHub` plugin** is authenticated and authorized for the intended repository;
- explicit `@GitHub` invocation retrieves the intended repository and reports its repository ID;
- create/update/readback/delete succeeds through the selected write-capable GitHub actions;
- current blob/version preconditions are used when available or their absence is explicitly reported;
- `SETUP-TEST.md` is removed after diagnostics unless intentionally retained for the optional nonce test;
- failed or unverified operations are reported visibly instead of treated as success.

For automatic future routing, also install the small repository-ID bootloader. Without it, the supported manual entry path is simply:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

For normal use after setup, start with `START_HERE.md` and consult `OPERATIONS.md` only when you need project creation, closeout, health checks, recovery, update checks, or maintenance.
