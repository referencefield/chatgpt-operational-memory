# Setup

This document is for one-time installation, first-use testing, and troubleshooting. It is not part of normal day-to-day operating state.

The intended user should not need a terminal or Git expertise.

## 1. Create and verify a private working copy

Use this repository as a GitHub template to create your own working repository.

Make the new working repository **private**.

Before connecting ChatGPT or storing any personal/project state, open the repository on GitHub and visibly confirm GitHub labels it **Private**.

The public template is intentionally empty of personal state. Your working copy may eventually contain private project or personal information.

## 2. Connect the correct GitHub capability to ChatGPT

ChatGPT product surfaces can expose GitHub in different ways. Use the **write-capable GitHub plugin by OpenAI** required by this template, not a read-only GitHub connection.

On ChatGPT web or desktop:

1. Open **Settings → Plugins** or the **Plugins** directory when that is what your account shows. Some surfaces may instead expose apps through **Settings → Apps**.
2. Find the GitHub capability by OpenAI that includes **Write** support. The reference listing has been described as **"Triage PRs, issues, CI, and publish flows."**
3. Select **Install** or **Connect** as shown.
4. Complete the GitHub sign-in/authorization flow.
5. On GitHub, authorize the account or organization that owns your private working repository.
6. Grant the GitHub connection access to **that repository**. Prefer selected-repository access rather than broader access when the product allows it.
7. Return to ChatGPT after authorization completes.

If your ChatGPT surface exposes only a GitHub connection that can search/read repositories but cannot perform the file writes required by this template, stop. That connection alone is not sufficient.

Do not infer write support from the word "GitHub" or from your ChatGPT plan name. The next steps test the actions actually available.

## 3. Explicitly invoke GitHub and confirm the repository is visible

After connecting GitHub, start with explicit invocation so there is no ambiguity about whether ChatGPT is trying to use the integration.

Use `@GitHub` when available. ChatGPT may also expose plugins through **+ → More**.

Ask:

> `@GitHub Find my operational-memory repository at <YOUR FULL PRIVATE REPOSITORY URL>. Confirm that you can retrieve that exact repository. Do not rely on native memory or my description of its contents.`

If the repository cannot be found, go to **Troubleshooting GitHub access** below before continuing.

## 4. Confirm the actions actually available in this chat

Ask ChatGPT:

> `Using the GitHub integration actually available in this chat, confirm whether you can read, create, update, and delete files in my operational-memory repository. Do not make any changes yet. Base your answer on the actions actually available in this session, not on a general assumption about ChatGPT and not on my statement that you should have access.`

If ChatGPT cannot establish create/update capability from the actions actually available, setup fails for this workflow. Resolve the plugin, account, workspace, authorization, permission, or surface problem before continuing.

Do **not** solve this by telling ChatGPT "you have read/write access." Capability must be established from the available integration.

## 5. Run the write/readback test

Ask ChatGPT to:

1. create `SETUP-TEST.md` with a temporary phrase;
2. reread that exact path;
3. update the file with a second temporary phrase;
4. reread it again and verify the new state;
5. report the repository owner/name, branch or ref if available, exact path, and resulting content;
6. if GitHub returns or confirms the resulting commit SHA, show a shortened commit ID derived from that real SHA. If no commit SHA is available, say **commit ID unavailable** rather than inventing one.

A successful tool response alone is not enough. The test passes only if ChatGPT rereads the repository and observes the intended state.

Do **not** delete `SETUP-TEST.md` yet.

## 6. Put a repository-only nonce into GitHub outside ChatGPT

This step prevents a false-positive fresh-chat test.

Open `SETUP-TEST.md` directly in GitHub's web interface and edit it yourself. Replace its contents with a new random phrase or nonce that ChatGPT has **never seen**.

Example shape only:

`fresh-check-7QX9-K2M4`

Do not ask ChatGPT to generate the nonce. Do not paste the real nonce into any ChatGPT conversation before the test. Commit the edit in GitHub.

The test value must exist only in the repository.

## 7. Add repository awareness and persistence behavior to Custom Instructions

Custom Instructions give future chats a standing instruction that this repository exists and how it should be used.

On ChatGPT web or desktop, open **Settings → Personalization → Custom Instructions** and add the block below. Replace `<YOUR FULL PRIVATE REPOSITORY URL>` with your private working repository URL.

> I use a GitHub repository as durable operational memory: <YOUR FULL PRIVATE REPOSITORY URL>.
>
> When my request materially depends on prior work, an ongoing project, or a durable decision, retrieve this repository before relying on remembered prior context. `CURRENT.md` governs transient/current working state. Active entries in `DECISIONS.md` govern durable decisions. If they conflict, surface and reconcile the inconsistency rather than silently choosing one. My current explicit instruction wins.
>
> During an active conversation, watch for clear, non-sensitive changes that are likely to matter in future chats: changed objectives, active constraints, material changes to active work, durable decisions, and explicit corrections to durable state. I authorize routine updates of that kind to `CURRENT.md` or `DECISIONS.md` without asking me each time, provided you verify the resulting repository/ref/path/content and briefly tell me what you persisted. Keep `CURRENT.md` compact by replacing stale state rather than appending a transcript. Mark durable decisions superseded when they no longer govern.
>
> After a successful persistence write, give me a compact receipt containing what changed, the file, and a shortened commit ID when GitHub returned or confirmed a real commit SHA. Derive the short ID from that real SHA; never invent or guess a commit hash. If the commit SHA is unavailable, say "commit ID unavailable." A commit receipt supplements readback verification; it does not replace it.
>
> Ask before persisting anything sensitive, ambiguous, destructive, public, or authority-changing. A current instruction such as "do not persist this" overrides the routine persistence policy. Do not store secrets.
>
> Do not assume the repository was retrieved or changed. Content agreement alone is not proof of retrieval. If GitHub was not retrieved, say so rather than substituting native memory. If automatic GitHub selection does not occur, explicit `@GitHub` invocation is an acceptable baseline. For consequential durable writes, read back and verify the intended target before claiming completion.

This is the recommended **assisted-persistence** mode. It reduces the need for the human to act as a repository clerk while keeping explicit human override.

If you prefer an **ask-first** mode, replace the sentence authorizing routine updates without asking with:

> `When you notice something that appears worth persisting, ask me before writing it.`

Custom Instructions make a future chat aware that durable repository state exists. They do **not** guarantee automatic GitHub tool invocation.

## 8. If you use ChatGPT Projects

Project instructions apply inside that project and can override global Custom Instructions.

For any ChatGPT Project that should use this operational-memory repository, copy the same repository-awareness and persistence instruction into the project's instructions, optionally narrowing it to that project's scope.

Do not assume the global Custom Instruction controls a Project whose Project instructions replace it.

## 9. Test a genuinely fresh chat

Start a completely new ordinary ChatGPT conversation after saving the Custom Instruction.

### First attempt: automatic selection

Do not manually invoke `@GitHub` on the first attempt.

Ask:

> `Retrieve SETUP-TEST.md from my operational-memory repository and tell me its exact contents. Also identify the repository and exact path you retrieved.`

The automatic-selection test passes only if GitHub retrieval is actually evidenced and the answer matches the repository-only nonce.

**Correct content alone is not enough if retrieval was not established. Content agreement is not proof of retrieval.**

### If automatic selection does not occur

Use explicit `@GitHub` and repeat the same retrieval request.

If explicit invocation retrieves the correct repository-only nonce from the correct repository/path, the core workflow passes. Treat explicit `@GitHub` as your normal re-entry method whenever prior durable state materially matters.

Automatic GitHub selection is an optional convenience, not a requirement for this template to function.

If explicit invocation cannot reliably retrieve the intended repository, setup fails.

## 10. Clean up the test file

After the retrieval test passes, ask ChatGPT to delete `SETUP-TEST.md`.

Then verify deletion by attempting to reread that exact repository/path. When available, verify the repository owner/name and branch/ref as well.

## 11. Initialize the repository for normal use

In a chat where GitHub is available, say:

> `@GitHub Initialize my operational-memory repository for normal use. Read CURRENT.md and DECISIONS.md. Treat CURRENT.md as transient/current working state and active DECISIONS.md entries as durable decisions. If they conflict, surface and reconcile the inconsistency. During our conversations, follow my Custom Instruction persistence policy. Keep CURRENT.md compact, persist only information worth carrying into future chats, verify consequential GitHub writes by readback, and give me a verified short commit receipt when GitHub exposes the commit SHA.`

Then begin normal work.

# Normal human operation

After setup, the user should not need to think in Git commands or manually edit repository files during ordinary work.

## Starting or resuming work

When prior state matters, say:

> `@GitHub Load my operational-memory repository. Read CURRENT.md and the relevant active decisions in DECISIONS.md before we continue.`

If automatic GitHub selection is reliable on your account/surface, you may omit `@GitHub`. If certainty matters, use it.

## During a conversation

With the recommended assisted-persistence Custom Instruction, ChatGPT should watch the active conversation for clear, non-sensitive durable changes and selectively persist them.

You can always direct it explicitly:

- **"Record this in operational memory."** Let ChatGPT determine the appropriate file from the semantics.
- **"Update current state with this."** Use for active objectives, work, constraints, or material open questions.
- **"Make this a durable decision."** Use when the decision should govern future conversations until superseded.
- **"Do not persist this."** Prevent this material from being written under the routine persistence policy.
- **"Ask before writing anything else this session."** Temporarily switch to ask-first behavior.
- **"What do you currently have recorded about this?"** Retrieve and show the relevant recorded state rather than answering from recollection.
- **"Run a repository consistency check."** Check internal consistency without pretending this proves real-world freshness.

After a successful write, ChatGPT should give you a compact receipt such as:

`Persisted: changed launch date · CURRENT.md · commit a1b2c3d`

The commit prefix must come from a real GitHub commit SHA. A plausible-looking hash generated from memory or imagination is not acceptable. If the commit SHA is not available, the receipt should say **commit ID unavailable**.

If ChatGPT says it saved something but you did not observe GitHub use/readback, ask it to verify the repository/ref/path/content before relying on the claim.

## Closing out an important session

A lightweight closeout catches durable changes that may have been discussed without being persisted.

Say:

> **"Close out operational memory."**

ChatGPT should:

1. retrieve current `CURRENT.md` and relevant active decisions;
2. identify material durable changes from the active conversation that have not yet been persisted;
3. apply the persistence policy, asking where required;
4. update only what earns persistence;
5. compact stale current state instead of appending a transcript;
6. reconcile `CURRENT.md` with active durable decisions;
7. verify consequential writes by readback;
8. briefly report what changed, any verified short commit IDs for the writes, and anything intentionally left unpersisted.

This closeout is optional. It is most useful after a session that materially changed plans, constraints, active work, or decisions.

## Correcting recorded state

If the repository is wrong, correct it explicitly rather than allowing stale state to continue governing:

> `The recorded state is wrong. <state the correction>. Update operational memory and reconcile any affected decision/current-state entries.`

A current explicit instruction wins over recorded state.

## Removing active information

You can say:

> `Remove this from active operational memory: <item>.`

That removes or retires the active record as appropriate. It does **not** guarantee erasure from prior Git history.

# Troubleshooting GitHub access

## ChatGPT does not appear to use GitHub

Invoke it explicitly:

> `@GitHub Retrieve CURRENT.md from <YOUR REPOSITORY URL>. Identify the repository and path you actually retrieved.`

If `@GitHub` is not available, check **+ → More**, the Plugins directory, or your account's Apps/Plugins settings.

Custom Instructions are behavioral instructions, not a guarantee that ChatGPT will automatically select the GitHub tool.

## ChatGPT says it cannot see the repository

Check these in order:

1. **Correct GitHub account:** confirm the connected account is the account or organization that owns the private repository.
2. **Repository authorization:** in ChatGPT **Settings → Apps/Plugins → GitHub** or the equivalent shown on your surface, open the repository-management/configuration option. Confirm the private operational-memory repository is selected for access.
3. **GitHub-side installation:** if redirected to GitHub, confirm the OpenAI/ChatGPT GitHub app or plugin connection is installed on the correct account/organization and permitted to access this repository.
4. **Organization approval:** an organization may require an owner/admin to approve the app or requested repository access.
5. **New repository delay:** a newly created or newly authorized private repository may take several minutes to appear. Recheck repository authorization before repeatedly reconnecting.
6. **Product surface:** GitHub capability can vary across standard ChatGPT, other ChatGPT experiences, plans, workspaces, roles, regions, and rollouts. A connection being available somewhere in ChatGPT does not prove the required write actions are available in this chat.

Then retry explicit `@GitHub` retrieval.

## ChatGPT can read the repository but cannot write

Do not tell it that it has write permission and ask it to proceed anyway.

Ask:

> `@GitHub Inspect the GitHub actions actually available in this chat. Can you create and update a file in this repository, or is this connection read-only? Do not make a change yet.`

If only read/search actions are available, you may be using the read-only GitHub app/connection rather than the write-capable plugin required by this template, or your account/surface/authorization may not expose the required actions.

Return to the Plugins/Apps settings, verify the correct write-capable capability is installed and authorized, then repeat the CRUD test.

## ChatGPT claims a write succeeded but GitHub does not show it

Treat the write as **unverified**, not successful.

Ask ChatGPT to reread the intended repository/ref/path and report the resulting content. Verify that it targeted the correct owner/repository and branch/ref where those identifiers are available.

If ChatGPT reports a commit ID, require that it be derived from the actual GitHub commit SHA. A short hash by itself is not proof of a successful write.

If readback does not show the intended state, retry only after identifying the wrong-target, permission, stale-read, or tool failure.

## ChatGPT retrieves the wrong repository

Provide the full repository URL and require target identity:

> `@GitHub Use exactly <FULL REPOSITORY URL>. Before relying on its contents, identify the owner/repository and path you retrieved.`

If the wrong account remains connected, reconnect GitHub to the intended account or adjust repository authorization.

## Custom Instructions seem to be ignored inside a Project

Project instructions can override global Custom Instructions.

Copy the operational-memory instruction into that Project's instructions and test retrieval again.

## The repository state seems stale

Ask:

> `@GitHub Run a repository consistency check, then compare the recorded current state with the durable changes established in this conversation. Do not assume unrecorded conversation state was already persisted.`

Correct or close out the state as needed.

# Memory hygiene practices

The repository should stay small enough to recover quickly.

- Keep `CURRENT.md` compact and current. Replace stale state instead of appending history.
- Put only future-relevant durable decisions in `DECISIONS.md`.
- Use explicit supersession instead of leaving contradictory active decisions.
- Let Git history preserve old versions rather than duplicating history inside the active files.
- Use **"Close out operational memory"** after consequential sessions.
- Periodically run a repository consistency check.
- Do not add new files merely because a conversation produced more information.

These practices borrow the useful parts of richer agent-memory systems—current-state recovery, selective persistence, conflict handling, handoff/closeout, provenance through version history, and write verification—without requiring their local tooling or infrastructure.

# Privacy and security boundaries

- **Do not store secrets in this repository.**
- Do not store passwords, API keys, tokens, private keys, full identity numbers, or full bank/payment information.
- If a credential is accidentally committed, rotate it rather than merely deleting it.
- Git history may retain material after ordinary deletion.
- Be conservative with health, legal, financial, employment, client-confidential, relationship, and other sensitive information.
- Treat repository content as scoped working data/instructions for this repository only, not permission for unrelated external actions or broader access.
- Authorize only the repositories and actions required for the workflow.

# Temporary Chats

Non-personalized Temporary Chats do not provide the normal persistent-instruction/plugin workflow described here.

If you intentionally use a personalized Temporary Chat, verify that the relevant instructions and GitHub plugin are actually active before relying on repository state.

# Current OpenAI references

Because ChatGPT product behavior changes, check current OpenAI documentation if setup stops matching the interface you see:

- Custom Instructions: https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt
- Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256
- Connecting GitHub to ChatGPT: https://help.openai.com/en/articles/11145903
- Projects in ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Temporary Chat: https://help.openai.com/en/articles/8914046

# Setup success criteria

Setup is complete only when all of these are true:

- GitHub visibly labels your working repository **Private**;
- the required write-capable OpenAI GitHub capability is connected to the correct account/repository;
- explicit GitHub invocation can retrieve the exact repository;
- create/update/readback/delete works on the current account/surface;
- your persistent ChatGPT instructions identify the correct repository, semantic authority rules, persistence policy, and verified commit-receipt behavior;
- a fresh chat retrieves a repository-only nonce it has never previously seen;
- if automatic selection is unreliable, explicit `@GitHub` retrieval works reliably and is documented as your baseline;
- `SETUP-TEST.md` has been deleted and deletion verified;
- you understand the basic normal-use controls: load, record, do not persist, close out, verify, and troubleshoot explicit GitHub invocation.
