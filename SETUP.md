# Setup

This document is installation only. Runtime behavior lives in `START_HERE.md`; ongoing operation in `OPERATIONS.md`; privacy/security in `SECURITY.md`; upgrades in `MIGRATIONS.md`.

## Beginner setup: Create → Connect → Activate

You only need to do this once.

You do **not** need to know Git, use a terminal, understand repository IDs, or edit memory files yourself.

**Supported release baseline:** **ChatGPT Plus (currently $20/month) or a higher ChatGPT plan** plus the installed/selected and authenticated `@GitHub` plugin with repository read/write actions. **Free and ChatGPT Go are not supported by this release.** A supported plan alone does not guarantee that the required plugin/actions are available on every account, region, workspace, or surface, so setup still verifies the actual capability.

### 1. Create your private memory repository

[**Create my private memory repository**](https://github.com/new?owner=%40me&template_owner=referencefield&template_name=operational-memory&visibility=private)

GitHub should open the new-repository form with this template selected and **Private** preselected. Choose any repository name you want, visibly confirm **Private**, then create it.

If you prefer, use GitHub's **Use this template** button manually and create a private repository. The working repository name does not matter.

Do not store passwords, API keys, recovery codes, full payment/bank information, or other secrets in this repository.

### 2. Connect GitHub to ChatGPT

In ChatGPT, install/select the **`@GitHub` plugin** in the message composer, authenticate it to GitHub, and authorize the private memory repository you just created. Prefer selected-repository access when available; you do not need to authorize unrelated repositories.

**Required capability:** the selected `@GitHub` plugin must be authenticated, authorized for the exact repository, and expose repository read/write actions. Merely seeing GitHub or the Plugin Directory is not enough. OpenAI also documents a separate GitHub app/connection used for repository search/analysis that may be read-only. That separate limitation does **not** prove that the selected `@GitHub` plugin cannot write.

### 3. Activate it

Copy the GitHub URL of your new private repository. In ChatGPT, send:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

That's it.

ChatGPT should handle the technical checks itself: supported plan, selected/authenticated `@GitHub`, exact repository, Private visibility, safe read/write, verified readback, cleanup of the temporary setup test, and protocol structure.

You should not have to perform those tests or name `START_HERE.md`, `PROTOCOL.yaml`, CRUD, repository IDs, blob versions, or an activation handshake.

## What success looks like

ChatGPT should return:

**Operational memory: READY**

It should show a compact human-facing result such as:

- supported ChatGPT plan ✓
- `@GitHub` authenticated ✓
- repository connected ✓
- Private ✓
- GitHub read/write verified ✓
- operational-memory structure healthy ✓

Then it should say **One final step** and tell you exactly where to install the completed Custom Instructions block.

**Web/Desktop**

1. Open **Settings → Personalization → Custom Instructions**.
2. Make sure customization is enabled.
3. Paste the block **at the very top, above any Custom Instructions you already have**.
4. Do **not** delete or replace your existing instructions.
5. Save the change.

**iOS/Android**

1. Open **Settings → Customize ChatGPT → Custom Instructions**.
2. Make sure customization is enabled.
3. Paste the block **at the very top, above any Custom Instructions you already have**.
4. Do **not** delete or replace your existing instructions.
5. Save the change.

ChatGPT supplies the completed block with your repository ID already filled in. Its compact form is:

> Operational Memory: I use GitHub repository ID `<ID>` for durable operational memory. When prior durable state could affect the task, or this conversation creates/changes clear future-governing state, use `@GitHub`, resolve this ID to its current repository, and follow `START_HERE.md`. Do not claim retrieval or persistence unless GitHub actions actually ran and writes were verified. If the ID cannot resolve or a write cannot be verified, say so; never guess another repository.

With a current 10-digit GitHub repository ID, this is about **487 characters**. You copy the completed block as-is; you do not need to understand, remember, or type the numeric ID yourself.

For dependable repository-backed retrieval or saving, start the message with **`@GitHub`**. The bootloader supplies the repository identity and routing, so you do not repeat the URL, ID, or protocol commands.

Examples:

- `@GitHub where were we on my project?`
- `@GitHub remember that I've decided to use option B.`
- `@GitHub update my current project status.`
- `@GitHub what do you currently have recorded about this?`

A generic explicit entry is also valid:

> `@GitHub Use my operational memory.`

Custom Instructions can tell ChatGPT when GitHub should be used, but they are not themselves proof that the plugin actually ran. ChatGPT should claim repository retrieval or persistence only after actual `@GitHub` actions provide the required evidence.

If you skip the Custom Instructions step, nothing breaks. For a later chat use:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

## If setup is blocked

ChatGPT should return:

**Operational memory: BLOCKED**

It should show **one problem and one next action**, not a technical diagnostic dump. After you fix the reported problem, say:

> `Retry setup.`

Examples:

**This release requires ChatGPT Plus or higher. Free and ChatGPT Go are unsupported.**  
**Fix:** Use ChatGPT Plus or a higher supported plan, then tell me `Retry setup.`

**The `@GitHub` plugin isn't installed, selected, or authenticated.**  
**Fix:** Install/select `@GitHub` in ChatGPT and authenticate it to GitHub. Then tell me `Retry setup.`

**I can't access your memory repository.**  
**Fix:** Give the authenticated `@GitHub` plugin access to that repository. Then tell me `Retry setup.`

**Your memory repository isn't private yet.**  
**Fix:** Change it to Private in GitHub. Then tell me `Retry setup.`

**I can read your memory repository but can't save changes.**  
**Fix:** Enable/authorize repository write actions for the `@GitHub` plugin. Then tell me `Retry setup.`

**I couldn't verify that saved changes are reaching GitHub.**  
**Fix:** Check the GitHub connection and try again. Then tell me `Retry setup.`

**The temporary setup test could not be cleaned up.**  
**Fix:** Restore GitHub write/delete access for this repository. Then tell me `Retry setup.`

Do not continue with real durable memory until setup reports **READY**.

## You're done

After READY and the one-time Custom Instructions copy, you should not normally need to visit GitHub or manage the memory files yourself.

The intended product experience is:

**Create → Connect → Activate → use `@GitHub` naturally when repository-backed continuity or persistence matters.**

Before READY, the user should make at most three meaningful setup decisions:

1. create the private repository;
2. install/select/authenticate `@GitHub` and allow it access to that repository;
3. give ChatGPT the repository URL.

Everything technical after that belongs to ChatGPT.

---

# Advanced / troubleshooting

The rest of this file is optional. Use it when setup is blocked, when you want stronger proof, or when you want to understand the implementation.

## Template-copy details

GitHub template copies do **not** inherit this public repository's branch-protection/ruleset configuration. Protection is optional hardening you may configure separately; see **Optional `main` protection** below.

The template includes an advisory GitHub Actions validator. In a derived working copy it does **not** run on every direct operational-memory write; it runs for pull requests or when manually dispatched. It is not a required status check.

Having many unrelated repositories connected does not make setup ambiguous. The activation URL selects one exact repository. ChatGPT captures that repository's numeric GitHub repository ID for future routing. If that exact repository later cannot be resolved or accessed, ChatGPT should stop rather than select another repository.

## Check `@GitHub` access without writing

If you want a separate access check, say:

> `@GitHub Check operational-memory access to <YOUR PRIVATE REPOSITORY URL>. Don't change anything.`

ChatGPT should retrieve that exact repository and determine whether the selected/authenticated `@GitHub` plugin exposes the repository actions needed for setup.

If ChatGPT says “GitHub is read-only,” verify that `@GitHub` was actually selected and authenticated. Do not stop solely because the model remembers documentation for the separate read-only GitHub app/connection. The selected plugin's actual actions and the reversible setup test determine readiness.

## Detailed write/readback test

Activation normally performs this automatically using temporary `SETUP-TEST.md`:

1. create the temporary file;
2. reread it from the exact repository/path;
3. update it using the current blob/version as a precondition when available;
4. reread and verify the change;
5. delete it;
6. verify deletion.

A tool acknowledgement alone is not proof. The test passes only when readback observes the intended state and cleanup is verified.

A deliberately stale update rejection is a concurrency-safety success; ChatGPT should reread/reconcile rather than force or blindly retry.

## Optional: prove it works from a completely fresh chat

This is **not required for normal setup**. Use it if you want stronger evidence that a new ChatGPT conversation is actually retrieving GitHub rather than relying on prior chat context.

1. After READY, create or temporarily retain `SETUP-TEST.md`.
2. In GitHub's web interface, replace its contents with a random phrase ChatGPT has never seen and commit it directly.
3. Do not paste that phrase into ChatGPT.
4. Start a completely new ChatGPT conversation.
5. If the bootloader is installed, say only:

> `@GitHub Read SETUP-TEST.md from my operational memory.`

If you skipped the bootloader, say:

> `@GitHub Read SETUP-TEST.md from <YOUR REPOSITORY URL>.`

The test passes only when GitHub retrieval is evidenced and the returned content matches the repository-only phrase. Then remove `SETUP-TEST.md` and verify deletion.

## Bootloader specification

The completed block generated after READY is the compact block shown above. The verified repository ID is already filled in.

The user pastes it at the top of Custom Instructions and preserves all existing instructions below it.

**Why the trigger has two directions:** operational memory may be needed because existing durable state affects the task, or because a conversation that began without repository context later creates a firm decision/status/constraint that should govern future work. The second case should still wake the repository before the session ends.

**Why explicit `@GitHub` remains the dependable path:** persistent instructions can tell ChatGPT when the plugin should be used, but product surfaces may differ in whether they automatically engage a plugin. Explicit `@GitHub` removes that ambiguity and does not require the user to restate repository identity.

**Why an ID is used internally:** GitHub owner/name can change; the repository's numeric ID remains stable across an ordinary rename. Renaming therefore requires no bootloader edit or memory migration.

If an ownership/organization change removes GitHub authorization, reconnect access. That is an authorization issue, not a state migration.

If a ChatGPT Project has instructions that override global Custom Instructions, add the same completed bootloader there only when that Project should use this repository.

## Repository rename behavior

Renaming the private working repository is supported. Future sessions resolve the configured repository ID to the current owner/name before retrieval.

If the configured ID stops resolving, fail closed and investigate access/deletion/authorization. Never silently switch to a similarly named repository.

## Codex

Codex is optional and not required for the lay-user workflow. Root `AGENTS.md` points Codex to `PROTOCOL.yaml` and `START_HERE.md` so it uses the same protocol rather than creating another memory system.

## ChatGPT Work

When equivalent write-capable `@GitHub` actions are available in Work on a supported plan/workspace, use the same repository, bootloader identity, and `START_HERE.md`. Do not create a Work-specific memory store.

## Optional `main` protection

Branch protection is optional hardening, not a requirement for operational memory. **Protection rules on the public template do not transfer through “Use this template.”**

If desired, configure lightweight protection against deleting or force-pushing the default `main` branch while leaving ordinary direct commits allowed. `SECURITY.md` contains the rationale and recommended configuration.

## Technical setup success criteria

Setup is technically complete when:

- ChatGPT Plus or a higher supported plan is in use; Free and Go are unsupported;
- `@GitHub` is installed/selected and authenticated to GitHub;
- the working repository is visibly private;
- the selected `@GitHub` plugin is authorized for that exact repository;
- required repository create/update/delete actions are available;
- create/update/readback/delete succeeds and cleanup is verified;
- stale-write protection is used when the integration exposes a current version/blob precondition;
- no temporary setup file remains unless intentionally retained for the optional fresh-chat proof;
- failures are reported as BLOCKED rather than represented as READY.

For normal use, return to conversation. Consult `OPERATIONS.md` only for project creation, health checks, recovery, update checks, or maintenance.
