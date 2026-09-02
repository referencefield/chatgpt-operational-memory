# Worked Example

This is a **fictional demonstration**, not active operational memory. A repository created from this template should not load or treat this file as user state.

The purpose is to show what the system does underneath an ordinary conversation without requiring a new user to understand the file architecture first.

## The conversation

Imagine a user is working over several weeks on a project called **Northstar Launch**.

During one conversation the user says:

> We are definitely not launching in October anymore. January 15 is the target. Atlas is the vendor we selected. The market-pricing research we collected in March is useful, but recheck it after December 1. Also, for research like this, remember that I want primary sources before commentary.

The user did not say “save every sentence.” The protocol routes only the parts that are clearly future-governing.

## What would become durable

### Project current state

`projects/northstar-launch/CURRENT.md` would compact the active situation rather than append the transcript:

- Launch target: **January 15**
- Selected vendor: **Atlas**
- Next relevant research action: recheck market pricing after December 1

### Project decision

`projects/northstar-launch/DECISIONS.md` would preserve the change in governing choice:

- Prior launch decision: October — **superseded**
- Active launch decision: January 15

The important point is not merely that both dates are remembered. The repository makes it explicit which one currently governs.

### Project knowledge

`projects/northstar-launch/KNOWLEDGE.md` could retain the March market-pricing research only if it is genuinely useful durable reference material, with lifecycle metadata such as:

- Knowledge: March market-pricing baseline
- Last verified: March
- Review after: December 1
- Status: active until reverified or superseded

Passing the review date would trigger scrutiny, not automatically make the knowledge false.

### Working style

Because the user explicitly said this should be remembered as a way of working, root `WORKING_STYLE.md` could contain a compact preference such as:

- For research tasks, prefer primary sources before commentary.

It would not infer broader personality traits or turn the user's conversation into a profile.

## What would *not* become durable

The system would not automatically preserve:

- the wording of the conversation;
- discarded alternatives discussed before the final decision;
- incidental personal details;
- speculative ideas that were never finalized;
- a new file just because a sentence did not fit neatly somewhere.

Selective persistence is the point.

## A later fresh chat

Two weeks later the user opens a fresh ChatGPT conversation. The one-time repository-ID bootloader was installed during setup, so the user does **not** need to restate the repository ID, repository name, routing instructions, or `START_HERE.md`.

They can simply say:

> `@GitHub where are we on Northstar?`

The `@GitHub` invocation selects the GitHub capability. The installed bootloader supplies the durable repository identity and tells ChatGPT to enter through the repository's current front door whenever prior durable work can materially matter.

ChatGPT should resolve the configured repository ID even if the user renamed the private repository since activation, enter through `START_HERE.md`, use `PROJECTS.md` to locate Northstar, and retrieve only the minimum current project authority.

A useful response would look approximately like:

> Northstar is targeting **January 15**. The earlier October launch decision is superseded. **Atlas** is the selected vendor. The March market-pricing baseline remains useful, but it is scheduled for recheck after **December 1**. The next obvious action is that pricing refresh.

If the user then asks for new research, the stored working preference can also shape how the research is performed without overriding the user's current instruction.

If the user did **not** install the optional bootloader, ChatGPT must not pretend it knows which repository to use. In that case the explicit repository-ID fallback in `SETUP.md` remains available.

## If the plan changes again

Suppose the user later says:

> January 15 is off. We are moving the launch to February 10.

That is a clear future-governing change. During repository-backed work, the conservative persistence watch can route it without requiring a magic “remember this” phrase.

A multi-file write-set would make the new February decision active, supersede January 15, update current state, reread the affected files, and verify that the complete postcondition holds before claiming success.

The result is maintained state rather than accumulated recollection.

## What the user experiences

The user does not need to know which Markdown file received each item.

The intended interaction remains conversational:

1. activate the private repository once;
2. install the tiny repository-ID bootloader if automatic future routing is desired;
3. talk normally, using `@GitHub` when explicit repository invocation is useful;
4. let ChatGPT route clear durable changes conservatively;
5. return later and ask where things stand;
6. inspect or correct the GitHub state whenever desired.

The files are the control layer. The conversation is the user interface.
