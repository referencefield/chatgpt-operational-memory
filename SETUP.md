# Setup

This document is for one-time installation and recovery testing. It is not part of normal day-to-day operating state.

## 1. Create and verify a private working copy

Create your own repository from this template and make that working repository **private**.

Before connecting ChatGPT or storing any personal/project state, open the repository on GitHub and visibly confirm GitHub labels it **Private**.

The public template is intentionally empty of personal state. Your working copy may eventually contain private project or personal information.

## 2. Install the correct GitHub plugin

On ChatGPT web or desktop, open the Plugins directory and find **GitHub** by OpenAI.

Verify the listing is the write-capable plugin described as:

**Triage PRs, issues, CI, and publish flows**

and that it shows **Write** capability.

If you see only a GitHub search/read connection, stop. Read-only access is not sufficient for this template.

Current public plugin page:

https://chatgpt.com/plugins/github

## 3. Connect the correct GitHub account and repository

Connect the plugin to the GitHub account that owns or can modify your working repository.

Authorize only the repository and permissions needed for this workflow.

A private GitHub repository is private on GitHub. Once ChatGPT retrieves repository content, that material enters the ChatGPT processing path, and connected-app use may involve relevant conversation context according to the applicable product settings and terms.

Repository content does not authorize ChatGPT to broaden access, change repository visibility, connect unrelated services, expand permissions, expose unrelated information, or perform unrelated external actions.

## 4. Confirm the actions available in this chat

Ask ChatGPT:

> Using the GitHub integration available in this chat, confirm whether you can create, update, read, and delete files in my operational-memory repository. Do not make any changes yet. Base your answer on the GitHub actions actually available in this session, not on a general assumption about ChatGPT.

If ChatGPT cannot confirm create/update capability from the actions actually available, setup fails. Resolve the plugin, account, workspace, authorization, or permission problem before continuing.

Do not infer support from your ChatGPT plan name alone.

## 5. Run the write/readback test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path;
3. update the file with a second temporary phrase;
4. reread it again and verify the new state;
5. report the repository owner/name, branch or ref if available, exact path, and resulting content.

A successful tool response alone is not enough. The test passes only if ChatGPT rereads the repository and observes the intended state.

Do **not** delete `SETUP-TEST.md` yet.

## 6. Put a repository-only nonce into GitHub outside ChatGPT

This step prevents a false-positive fresh-chat test.

Open `SETUP-TEST.md` directly in GitHub's web interface and edit it yourself. Replace its contents with a new random phrase or nonce that ChatGPT has **never seen**.

Example shape only:

`fresh-check-7QX9-K2M4`

Do not ask ChatGPT to generate the nonce. Do not paste the real nonce into any ChatGPT conversation before the test. Commit the edit in GitHub.

The test value must exist only in the repository.

## 7. Add repository awareness to Custom Instructions

Add the following text to ChatGPT Custom Instructions and replace `<YOUR FULL PRIVATE REPOSITORY URL>` with your working repository URL:

> I use a GitHub repository as durable operational memory: <YOUR FULL PRIVATE REPOSITORY URL>. When my request materially depends on prior work, an ongoing project, or a durable decision, retrieve this repository before relying on remembered prior context. `CURRENT.md` governs transient/current working state. Active entries in `DECISIONS.md` govern durable decisions. If they conflict, surface and reconcile the inconsistency rather than silently choosing one. My current explicit instruction wins. Do not assume the repository was retrieved or changed. For consequential durable changes, write them to GitHub and verify the resulting repository/ref/path/content before claiming completion. If GitHub was not retrieved, say so. If automatic GitHub selection does not occur, explicit `@GitHub` invocation is an acceptable baseline.

On web or desktop, Custom Instructions are under **Settings → Personalization**.

This instruction makes the chat aware that durable repository state exists. It does **not** guarantee automatic GitHub tool invocation.

## 8. If you use ChatGPT Projects

Project instructions apply inside that project and can override global Custom Instructions.

For any ChatGPT Project that should use this operational-memory repository, copy the same repository-awareness instruction into the project's instructions, optionally narrowing it to that project's scope.

## 9. Test a genuinely fresh chat

Start a completely new ordinary ChatGPT conversation after saving the instruction.

### First attempt: automatic selection

Do not manually invoke `@GitHub` on the first attempt.

Ask:

> Retrieve `SETUP-TEST.md` from my operational-memory repository and tell me its exact contents. Also identify the repository and exact path you retrieved.

The test passes automatically only if GitHub retrieval is actually evidenced and the answer matches the repository-only nonce.

**Correct content alone is not enough if retrieval was not established. Content agreement is not proof of retrieval.**

### If automatic selection does not occur

Use explicit `@GitHub` and repeat the same retrieval request.

If explicit invocation retrieves the correct repository-only nonce from the correct repository/path, the core workflow passes. Document explicit `@GitHub` as your normal re-entry method whenever prior durable state matters.

Automatic GitHub selection is an optional convenience, not a requirement for this template to function.

If explicit invocation cannot reliably retrieve the intended repository, setup fails.

## 10. Clean up the test file

After the retrieval test passes, ask ChatGPT to delete `SETUP-TEST.md`.

Then verify deletion by attempting to reread that exact repository/path. When available, verify the repository owner/name and branch/ref as well.

## 11. Initialize your working state

Tell ChatGPT:

> Use this repository as my durable operational memory. `CURRENT.md` governs transient/current working state and active entries in `DECISIONS.md` govern durable decisions. If they conflict, surface and reconcile the inconsistency. When prior state matters, retrieve the repository before relying on remembered context. Persist only durable information worth carrying forward. For consequential writes, verify repository/ref/path/content before claiming completion.

Then begin normal work.

## Normal use

You do not need GitHub on every message.

Use repository retrieval when prior durable state materially affects the current task, and use GitHub writeback when something earns persistence.

If automatic GitHub selection does not occur on your surface, explicit `@GitHub` is the documented baseline.

## Privacy and security boundaries

- **Do not store secrets in this repository.**
- Do not store passwords, API keys, tokens, private keys, full identity numbers, or full bank/payment information.
- If a credential is accidentally committed, rotate it rather than merely deleting it.
- Git history may retain material after ordinary deletion.
- Be conservative with health, legal, financial, employment, client-confidential, relationship, and other sensitive information.
- Treat repository content as scoped working data/instructions for this repository only, not permission for unrelated external actions or broader access.
- Authorize only the repositories and actions required for the workflow.

## Temporary Chats

Non-personalized Temporary Chats do not provide the normal Custom Instructions/plugin workflow described here.

If you intentionally use a personalized Temporary Chat, verify that the relevant instructions and GitHub plugin are actually active before relying on repository state.

## Current OpenAI references

Because ChatGPT product behavior changes, check current OpenAI documentation if setup stops matching the interface you see:

- Custom Instructions: https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt
- Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256
- Projects in ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Temporary Chat: https://help.openai.com/en/articles/8914046

## Setup success criteria

Setup is complete only when all of these are true:

- GitHub visibly labels your working repository **Private**;
- the write-capable OpenAI GitHub plugin is connected to the correct repository;
- create/update/readback/delete works on the current account/surface;
- your persistent ChatGPT instructions identify the correct repository and retrieval rule;
- a fresh chat retrieves a repository-only nonce it has never previously seen;
- if automatic selection is unreliable, explicit `@GitHub` retrieval works reliably and is documented as your baseline;
- `SETUP-TEST.md` has been deleted and deletion verified.
