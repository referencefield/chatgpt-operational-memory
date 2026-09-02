# Setup

This document is installation only. Runtime behavior lives in `START_HERE.md`; ongoing maintenance and recovery live in `OPERATIONS.md`; privacy/security guidance lives in `SECURITY.md`; protocol upgrades live in `MIGRATIONS.md`.

The intended user should not need a terminal or Git expertise.

## Setup at a glance

You will do five things:

1. create a **private** working repository from this template;
2. connect and authorize a **write-capable GitHub integration** for that repository;
3. prove read/create/update/delete and readback actually work;
4. add one small persistent ChatGPT instruction that points future sessions to `START_HERE.md`;
5. run one genuinely fresh-chat retrieval test using a value that exists only in GitHub.

After that, ordinary use should remain conversational.

## 1. Create and verify a private working copy

Use this public repository as a GitHub template to create your own working repository.

Make the working repository **private** and visibly confirm GitHub labels it Private before storing personal/project state.

The public template contains protocol structure, not user-specific memory.

## 2. Connect the correct GitHub capability

This workflow requires a GitHub integration that can actually write files, not merely search/read them.

On the ChatGPT surface available to you:

1. open the Plugins/Apps area shown by your account;
2. connect the GitHub capability that exposes write actions;
3. complete GitHub authorization;
4. authorize the account/organization that owns your private working repository;
5. grant access to that repository, preferably selected-repository access when available.

Do not assume capability from the word “GitHub” or from your ChatGPT plan name. Test the actions actually available in the current chat.

## 3. Confirm repository visibility and actions

Invoke GitHub explicitly when available and ask:

> `@GitHub Find my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Confirm that you can retrieve that exact repository. Then inspect the GitHub actions actually available in this chat and tell me whether you can read, create, update, and delete files there. Do not make changes yet and do not rely on my claim that you have access.`

If create/update capability cannot be established, stop. Resolve connection, authorization, repository selection, organization approval, workspace restrictions, or product-surface differences before continuing.

## 4. Run the write/readback and stale-write test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path and verify it exists in the intended repository;
3. identify the current blob/version identifier if GitHub exposes one;
4. update the file with a second phrase using the current observed blob/version as the update precondition when supported;
5. reread and verify the resulting content;
6. report repository owner/name, branch/ref, exact path, and resulting state when available;
7. show a shortened commit ID only when it is derived from a real GitHub commit SHA.

A tool saying it accepted a write is not enough. The test passes only when ChatGPT rereads the repository and observes the intended state.

If a stale update is rejected, that is a concurrency-safety success. ChatGPT should reread/reconcile rather than force or blindly retry.

Do **not** delete `SETUP-TEST.md` yet.

## 5. Put a repository-only nonce into GitHub outside ChatGPT

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

**Why it is intentionally small:** protocol rules evolve in the repository. A bootloader avoids maintaining two copies of routing/authority/failure rules and reduces configuration drift. Updating the repo updates the protocol without requiring the user to recopy a long Custom Instruction.

If you use a ChatGPT Project whose own instructions override global Custom Instructions, add the same small bootloader there when that Project should use this repository.

## 7. Test a genuinely fresh chat

Start a completely new ordinary ChatGPT conversation.

### First attempt: automatic selection

Without manually invoking GitHub, ask:

> `Enter my operational-memory repository through START_HERE.md. Then retrieve SETUP-TEST.md and tell me its exact contents, repository, and path.`

The automatic-selection test passes only when GitHub retrieval is actually evidenced and the returned content matches the repository-only nonce.

Correct content alone is not proof of retrieval.

### Explicit invocation fallback

If automatic GitHub selection does not occur, repeat with explicit `@GitHub`.

If explicit invocation retrieves the correct nonce from the correct repository/path, the core workflow passes. Use explicit GitHub invocation whenever certainty matters.

If explicit invocation cannot reliably retrieve the repository-only nonce, setup fails for this workflow.

## 8. Clean up the test

After the fresh-chat test passes, ask ChatGPT to delete `SETUP-TEST.md` and verify deletion by attempting to reread the exact repository/path.

## 9. Initialize normal use

Say:

> `@GitHub Enter my operational-memory repository through START_HERE.md. Verify PROTOCOL.yaml and the declared root structure, confirm there are no real projects yet unless PROJECTS.md says otherwise, and report the current scale/health status. Do not create project state just to initialize the repository.`

Then begin ordinary work.

## Optional `main` protection

Branch protection is optional hardening, not a requirement for operational memory. If desired, protect the default branch against deletion and force pushes while leaving ordinary direct commits allowed. See `SECURITY.md` for the exact rationale and configuration.

## Setup success criteria

Setup is complete when:

- the working repository is visibly private;
- the required write-capable GitHub capability is connected to the correct repository;
- explicit GitHub invocation can retrieve the intended repository;
- create/update/readback/delete succeeds on the current surface;
- current blob/version preconditions are used when available or their absence is explicitly reported;
- persistent instructions point fresh sessions to `START_HERE.md` without duplicating the full protocol;
- a fresh chat retrieves the repository-only nonce it has never seen;
- `SETUP-TEST.md` is deleted and deletion verified;
- failed or unverified operations are reported visibly instead of treated as success.

For normal use after setup, start with `START_HERE.md` and consult `OPERATIONS.md` only when you need project creation, closeout, health checks, recovery, or maintenance.