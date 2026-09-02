# Setup

This document is installation only. Runtime behavior lives in `START_HERE.md`; ongoing operation in `OPERATIONS.md`; privacy/security in `SECURITY.md`; upgrades in `MIGRATIONS.md`.

## Beginner setup: Create → Connect → Activate

You only need to do this once.

You do **not** need to know Git, use a terminal, understand repository IDs, or edit memory files yourself.

### 1. Create your private memory repository

[**Create my private memory repository**](https://github.com/new?owner=%40me&template_owner=referencefield&template_name=chatgpt-operational-memory&visibility=private)

GitHub should open the new-repository form with this template selected and **Private** preselected. Choose any repository name you want, visibly confirm **Private**, then create it.

If you prefer, use GitHub's **Use this template** button manually and create a private repository. The working repository name does not matter.

Do not store passwords, API keys, recovery codes, full payment/bank information, or other secrets in this repository.

### 2. Connect GitHub to ChatGPT

In ChatGPT, install/select the **`@GitHub` plugin**, sign in to GitHub when asked, and authorize the private memory repository you just created. Prefer selected-repository access when available; you do not need to authorize unrelated repositories.

**Required capability:** the selected `@GitHub` plugin must expose repository read/write actions. OpenAI also documents a separate GitHub app/connection used for repository search/analysis that may be read-only. That separate limitation does **not** prove that the `@GitHub` plugin cannot write.

Plugin availability varies by account, workspace, role, region, and ChatGPT surface. Setup determines compatibility from the actual `@GitHub` actions available, not from the plan name alone.

### 3. Activate it

Copy the GitHub URL of your new private repository. In ChatGPT, send:

> `@GitHub Set up operational memory from <YOUR PRIVATE REPOSITORY URL>.`

That's it.

ChatGPT should handle the technical checks itself: exact repository, Private visibility, safe read/write, verified readback, cleanup of the temporary setup test, and protocol structure.

You should not have to perform those tests or name `START_HERE.md`, `PROTOCOL.yaml`, CRUD, repository IDs, blob versions, or an activation handshake.

## What success looks like

ChatGPT should return:

**Operational memory: READY**

It should show a compact human-facing result such as:

- repository connected ✓
- Private ✓
- GitHub read/write verified ✓
- operational-memory structure healthy ✓

Then it should say **One final step:** and give you a completed Custom Instructions block to copy into ChatGPT. The repository's numeric GitHub ID is already embedded in that instruction; you do not need to understand, remember, or type it yourself.

After that, start chatting normally. For example:

- `Where were we on my project?`
- `Remember that I've decided to use option B.`
- `Update my current project status.`
- `What do you currently have recorded about this?`

You can explicitly invoke the repository anytime with:

> `@GitHub Use my operational memory.`

If you skip the Custom Instructions step, nothing breaks. For a later chat use:

> `@GitHub Use operational memory from <YOUR REPOSITORY URL>.`

## If setup is blocked

ChatGPT should return:

**Operational memory: BLOCKED**

It should show **one problem and one next action**, not a technical diagnostic dump. After you fix the reported problem, say:

> `Retry setup.`

Examples:

**I can't access your memory repository.**  
**Fix:** Give the `@GitHub` plugin access to that repository. Then tell me `Retry setup.`

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

**Create → Connect → Activate → talk normally.**

Before READY, the user should make at most three meaningful setup decisions:

1. create the private repository;
2. allow `@GitHub` access to that repository;
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

ChatGPT should retrieve that exact repository and determine whether the selected `@GitHub` plugin exposes the repository actions needed for setup.

If ChatGPT says “GitHub is read-only,” verify that `@GitHub` was actually selected. Do not stop solely because the model remembers documentation for the separate read-only GitHub app/connection. The selected plugin's actual actions and the reversible setup test determine readiness.

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

For technical inspection, the completed Custom Instructions block generated after READY has this shape, with the verified numeric repository ID filled in automatically:

> I use GitHub repository ID `<VERIFIED ID>` as durable operational memory.
>
> When my request can materially depend on prior durable work, use `@GitHub` to resolve that repository ID to its current owner/name, then retrieve `START_HERE.md` from that repository before relying on remembered context. `START_HERE.md` defines the repository's current routing and persistence protocol; follow it rather than relying on an older copy of the protocol in chat or memory. Do not load the whole repository by default.
>
> If the repository ID cannot be resolved, routing cannot be established, or a persistence write cannot be verified, say so rather than guessing a replacement repository or claiming operational memory was loaded or persisted.

The user should copy the completed block, not manually find or substitute the numeric ID.

**Why an ID is used internally:** GitHub owner/name can change; the repository's numeric ID remains stable across an ordinary rename. Renaming therefore requires no bootloader edit or memory migration.

If an ownership/organization change removes GitHub authorization, reconnect access. That is an authorization issue, not a state migration.

If a ChatGPT Project has instructions that override global Custom Instructions, add the same completed bootloader there only when that Project should use this repository.

## Repository rename behavior

Renaming the private working repository is supported. Future sessions resolve the configured repository ID to the current owner/name before retrieval.

If the configured ID stops resolving, fail closed and investigate access/deletion/authorization. Never silently switch to a similarly named repository.

## Codex

Codex is optional and not required for the lay-user workflow. Root `AGENTS.md` points Codex to `PROTOCOL.yaml` and `START_HERE.md` so it uses the same protocol rather than creating another memory system.

## ChatGPT Work

When equivalent write-capable `@GitHub` actions are available in Work, use the same repository, bootloader identity, and `START_HERE.md`. Do not create a Work-specific memory store.

## Optional `main` protection

Branch protection is optional hardening, not a requirement for operational memory. **Protection rules on the public template do not transfer through “Use this template.”**

If desired, configure lightweight protection against deleting or force-pushing the default `main` branch while leaving ordinary direct commits allowed. `SECURITY.md` contains the rationale and recommended configuration.

## Technical setup success criteria

Setup is technically complete when:

- the working repository is visibly private;
- the selected `@GitHub` plugin is authenticated and authorized for that exact repository;
- required repository create/update/delete actions are available;
- create/update/readback/delete succeeds and cleanup is verified;
- stale-write protection is used when the integration exposes a current version/blob precondition;
- no temporary setup file remains unless intentionally retained for the optional fresh-chat proof;
- failures are reported as BLOCKED rather than represented as READY.

For normal use, return to conversation. Consult `OPERATIONS.md` only for project creation, closeout, health checks, recovery, update checks, or maintenance.
