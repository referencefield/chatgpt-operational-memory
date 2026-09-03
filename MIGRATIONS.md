# Protocol Migrations

`PROTOCOL.yaml` gives each working copy an explicit protocol release/status and identifies the public template source.

This repository is still **pre-release**. Pre-release development changes are folded into the eventual baseline release rather than preserved as fake release-to-release migrations.

## Public template source vs. working repository

The `template_source` entry in `PROTOCOL.yaml` identifies the public upstream used only for update discovery and migration guidance. Its GitHub repository ID is the durable upstream identity; the owner/name is human-readable metadata resolved at runtime and may change. It is **not** the required name or identity of a user's working repository.

A private working copy may have any GitHub owner/name. Its durable ChatGPT routing identity is the repository's own GitHub repository ID, resolved at runtime to the current owner/name.

Renaming a working repository does not change its internal protocol or durable state, does not require a protocol migration, and does not require changing the repository-ID bootloader. If a rename changes only owner/name, future sessions resolve the same repository ID to the new current location.

If repository ownership/organization changes and the GitHub plugin/app loses access, reauthorize the connection. Treat that as an access problem, not a state migration. If the configured repository ID cannot be resolved, fail closed rather than guessing a similarly named repository.

Do not rewrite `template_source.repository_id` or `template_source.repository` to the private working repository. Doing so would confuse the upstream update source with the user's runtime repository.

A rename or transfer of the public template source should not require edits to existing working copies when `template_source.repository_id` still resolves. Update discovery should resolve that ID to the upstream's current owner/name. If it cannot be resolved or accessed, report update status as `not checked` rather than guessing a replacement upstream by name.

## Current pre-release rule

While `PROTOCOL.yaml` reports:

`protocol_version: "unreleased"`

there is no ordered public protocol version to compare against another unreleased copy.

During this phase:

- do not infer chronology from commit count, repository age, or prior draft version labels;
- do not preserve temporary development version numbers in user-facing docs;
- compare the local and template manifests/content only when an explicit development comparison is needed;
- preserve private working state if a development copy is being refreshed;
- do not auto-migrate merely because the public template changed;
- if a pre-release working copy still carries a URL/name-based ChatGPT bootloader, replace it with the repository-ID bootloader before the final release baseline is frozen.

Acceptance candidates remain `protocol_version: "unreleased"`. The first real protocol identifier is assigned only after the acceptance gate passes, during the Gate 7 release transition.

## Update discovery

The template source is declared in `PROTOCOL.yaml`.

When checking for updates:

1. resolve the working repository by its configured repository ID;
2. retrieve the working copy's `PROTOCOL.yaml`;
3. resolve `template_source.repository_id` to the public template's current owner/name;
4. retrieve the resolved template source's declared manifest;
5. compare release/status and relevant structural fields;
6. if both are `unreleased`, report that ordered version comparison is unavailable and compare content only when explicitly needed;
7. after real releases exist, use their release identifiers plus this file to determine the applicable migration path;
8. never overwrite populated private state with blank template state;
9. never claim an upgrade merely because the public template changed.

If the template source repository ID cannot be resolved or the resolved source cannot be reached, report update status as **not checked**. Do not guess another source from owner/name similarity.

## Migration principles after release

When a future release changes protocol structure or semantics:

- preserve valid user state rather than replacing it with template examples;
- route/reconcile existing content before introducing a new required home;
- treat a migration affecting multiple files as a write-set with explicit postconditions;
- reread and verify the complete migrated structure before reporting completion;
- separate protocol migration from Git history rewriting;
- if migration partially succeeds, report **protocol migration is temporarily inconsistent** until the full postcondition holds.

A working-repository rename by itself is not a protocol migration.

## Pre-gate development state

The acceptance gate is **not automatically active** merely because the repository is close to release, has passed a validator run, has undergone adversarial review, or appears architecturally complete.

While `PROTOCOL.yaml` reports:

`protocol_status: development`

this repository is in active pre-release development. During that state:

- substantive design, documentation, protocol, validator, and implementation changes are allowed;
- validator runs, design reviews, smoke checks, and adversarial reviews are development evidence only and do not satisfy the acceptance gate unless a later gate step explicitly says otherwise;
- no candidate commit SHA or tree SHA is frozen;
- ordinary accepted changes do not “invalidate a candidate,” because no acceptance candidate exists yet;
- do not describe the repository as being in acceptance testing, in release-candidate freeze, or as release-ready;
- statements such as “getting close,” “almost ready,” or “we should test soon” do not activate the gate.

### Entering acceptance

Initial acceptance begins only after an explicit current instruction from the repository owner/maintainer authorizes starting the acceptance gate.

To enter acceptance from ordinary development:

1. finish the intended development changes that should precede testing;
2. change `protocol_status` from `development` to `acceptance_candidate` as the deliberate lifecycle transition;
3. merge that transition to canonical `main`;
4. record the resulting `main` commit SHA and tree SHA as the Gate 1 candidate;
5. from that recorded SHA forward, apply the freeze and restart rules below.

The commit that establishes `protocol_status: acceptance_candidate` is the first commit eligible to become the frozen acceptance candidate. Do not freeze an earlier development commit and then mutate the manifest afterward.

If testing exposes a defect or other accepted repository change, that candidate is invalid and the corrective change must restore `protocol_status: development`. If the owner's original authorization to run the acceptance gate remains in force and the work is corrective rather than a newly expanded design phase, fixes may re-enter `acceptance_candidate` and freeze a new SHA as part of the same authorized gate without another approval prompt. Require a new explicit entry decision only after the gate was stopped/revoked or the work returned to a new substantive development phase outside the already-authorized corrective loop.

## Objective pre-release acceptance gate

This section is dormant while `protocol_status: development` unless the repository is temporarily in corrective development inside an already-authorized acceptance run. Initial entry from ordinary development still requires the explicit procedure above.

Do not call the repository **done**, **release-ready**, or recommend stopping substantive review merely because an architecture/design sweep found no further improvements. Release readiness is established only by the evidence below against a frozen candidate.

### Gate 1 — Freeze candidate

Verify `PROTOCOL.yaml` reports `protocol_status: acceptance_candidate`, then record the resulting canonical `main` commit SHA and tree SHA. That exact commit is the frozen candidate.

From that point through Gates 2-6, do not make opportunistic improvements. Any accepted repository change before the prescribed Gate 7 release transition invalidates the candidate and returns the repository to development for corrective work. If the already-authorized acceptance run remains active, re-enter with a new `acceptance_candidate` transition and frozen SHA after those fixes; do not ask for redundant approval merely because the candidate changed.

### Gate 2 — Deterministic repository checks

Against the frozen candidate:

- run `tools/test_validate_protocol.py` and require all validator regression self-tests to pass;
- run `tools/validate_protocol.py` and require `RESULT: PASS` or consciously adjudicate every `Watch` signal;
- verify repository visibility/template status, default branch, branch set, and intended public-repository ruleset/settings;
- verify no setup/probe files or unintended artifacts remain;
- verify `START_HERE.md` and other declared soft budgets;
- verify the public template-source repository ID resolves correctly.

Record the exact candidate SHA used. A validator or self-test result from an earlier commit does not satisfy this gate.

### Gate 2B — Independent behavioral qualification

Before any zero-reading template-copy acceptance session, qualify the exact frozen candidate against the maintained behavioral/adversarial suite in `EVALS.md`.

- use fresh conversation/context for the evaluated model/surface and do not expose the corresponding `Expected` section before the model acts;
- exercise every scenario applicable to the public release claims; any scenario classified as not applicable must be explicitly recorded with the reason rather than silently omitted;
- judge observed behavior after the fact and do not count ambiguous outcomes as passes;
- distinguish protocol/model behavior failures from tool outage or capability unavailability;
- record the qualification in an acceptance evidence record **outside the frozen candidate tree**, including date, model/surface, candidate SHA, scenario coverage, pass/fail/blocked or not-applicable classifications, and material failure modes;
- do **not** update `EVAL_RESULTS.md` while Gates 1–6 freeze is active, because that would mutate and invalidate the candidate; publish the compact qualifying summary there during the prescribed Gate 7 release transition;
- same-session self-review after the expected answers have been seen may inform development but does **not** satisfy Gate 2B.

Gate 2B passes only when there is no unresolved behavioral failure that contradicts a public release claim or a required safety/authority/persistence invariant. If qualification exposes a repository change that should be made, invalidate the candidate and enter the Gate 6 corrective loop before proceeding to Gate 3.

### Gate 3 — Zero-reading template-copy acceptance test

Create a new **private** repository using GitHub **Use this template**, give it an arbitrary name, and approach it as a first-time non-expert user who has not read the repository files.

The minimum public ChatGPT support claim for this release is **ChatGPT Plus**. Free and ChatGPT Go are explicitly unsupported and are not eligible substitutes for this acceptance test. Run Gate 3 on a normal Plus account/surface, not a maintainer-only, administrator-only, internal, development, or unusually privileged environment.

Before activation, prove that the user-facing prerequisite path itself works: `@GitHub` can be installed/selected in ChatGPT, authenticated to GitHub, authorized for the exact private template copy, and exposes the repository create/update/delete actions required by activation. Plugin visibility alone is not enough. If any of those prerequisites is unavailable on the tested Plus surface, Gate 3 is **BLOCKED** and the release cannot claim Plus support until the capability path is established or the public support boundary is deliberately changed.

Using a fresh ChatGPT conversation and only the documented beginner **Create → Connect → Activate** path:

1. run activation from the private repository URL;
2. require the Plus-or-higher plan check, selected/authenticated/authorized `@GitHub`, correct repository ID, privacy check, reversible CRUD/readback, cleanup, and `Operational memory: READY` receipt;
3. install the repository-ID bootloader supplied by activation;
4. create a small piece of genuine durable project state through normal conversation;
5. for the exact `main` commit created by that durable-state write, verify the derived copy's **Operational-memory protocol validation** workflow starts from a `push` event on `main` and completes successfully with `RESULT: PASS`; a source-repository run or manual dispatch is not a substitute;
6. start another fresh conversation and recover that state from the repository;
7. rename the private repository;
8. start another fresh conversation and verify the same repository ID resolves to the renamed repository, the state is recovered, and a verified write succeeds without changing the bootloader.

For the Gate 3 acceptance evidence record, capture at minimum: date/time with timezone, frozen candidate SHA and tree SHA, ChatGPT model, plan, surface, GitHub integration/plugin path actually used, derived repository ID, activation READY/BLOCKED outcome, durable-state write commit SHA, and the derived-copy validator workflow run ID/result. Keep the record outside the frozen candidate tree during Gates 1–6 and focused on reproducibility; do not copy private memory content merely for instrumentation.

Failure or user confusion is release evidence. Fix the smallest root cause, return the public template to development, and, when the existing acceptance authorization remains in force, re-enter with a new candidate after corrective work.

### Gate 4 — Surface smoke tests

On the frozen candidate:

- **Codex:** verify root `AGENTS.md` enters through `PROTOCOL.yaml` / `START_HERE.md`, uses the existing memory topology, and can perform a verified repository-backed state change without creating a competing memory system.
- **ChatGPT Work:** when the required write-capable GitHub plugin/app is available on a supported plan/workspace, verify it uses the same repository ID/front door and preserves the same routing, privacy, write-set, and readback rules. If the required capability is unavailable on the tested Work surface, record that limitation and qualify public compatibility wording rather than inventing a pass.

### Gate 5 — Independent adversarial release audit

Run the maintained final pre-release audit against **every tracked file in the frozen candidate**, with the reviewer instructed to report only and not modify the repository. The reviewer must distinguish PASS/WARN/FAIL/BLOCKED and provide evidence for each finding.

Triage every finding into exactly one of:

- **Blocker:** must be fixed before release;
- **Should-fix:** cheap/material enough to fix before the first release;
- **Deferred:** consciously accepted for a later release with the reason recorded.

Do not accept or reject a finding merely because it agrees or disagrees with prior design intent. Reproduce or verify material claims against the actual candidate and current product capability.

### Gate 6 — Post-fix regression gate

If Gates 2–5, including Gate 2B, identify any repository change that should be made:

1. invalidate the current candidate and restore `protocol_status: development` as part of corrective work;
2. make and verify the accepted fixes in development;
3. if the existing acceptance authorization remains in force and the work stayed within the corrective loop, change `protocol_status` back to `acceptance_candidate` without a redundant approval prompt; otherwise obtain a new explicit entry decision;
4. freeze the resulting new canonical `main` SHA/tree;
5. rerun validator regression self-tests and deterministic validation against that exact candidate;
6. rerun the behavioral scenarios affected by the changes, plus any scenarios needed to establish that the new candidate still satisfies Gate 2B;
7. rerun the portions of the zero-reading/surface tests affected by the changes;
8. rerun the independent audit as a regression/delta audit, explicitly checking accepted fixes for newly introduced failures.

The candidate passes only when there are **zero unresolved blockers**, no unresolved applicable behavioral failure contradicts the release claims/invariants, every remaining warning is consciously classified, and no new material regression is found.

### Gate 7 — Release transition

Only after Gates 1–6 pass:

- assign the first real protocol release identifier and set `protocol_status: released`;
- replace the **pre-first-release bootstrap lifecycle** in `PROTOCOL.yaml`, `AGENTS.md`, and `tools/validate_protocol.py` with a post-release lifecycle that can represent the last/current released protocol and a future development/acceptance target without reverting a released protocol ambiguously to `unreleased`; define and validate that transition before tagging the first release;
- publish the compact Gate 2B qualifying behavioral summary from the external acceptance evidence record into `EVAL_RESULTS.md`, rerunning and updating any scenarios materially affected by the prescribed release/lifecycle transition;
- verify the pre-acceptance clean baseline remains intact; no additional history rewrite is part of Gate 7;
- restore and verify the intended public-repository protection/settings;
- rerun validator regression self-tests and deterministic validation against the final release tree;
- tag/publish the release;
- create one final private copy using **Use this template** and repeat the activation smoke test against what GitHub actually ships.

The prescribed release/version/lifecycle/evidence changes in Gate 7 are the release transition after the frozen candidate has passed; they are not an acceptance-candidate defect that sends the repository back through Gate 6. Any unrelated or opportunistic change discovered during Gate 7 still invalidates the release transition and must be handled through the normal corrective path.

That final private-copy activation is the release artifact check. A successful test against the source repository alone is not sufficient.

### Stopping rule

After the gate passes, new suggestions do not automatically reopen the release. Reopen only for a reproducible blocker, material regression, security/privacy defect, false product claim, or a change that clearly exceeds the agreed diminishing-returns threshold. Other improvements become post-release candidates.

## Pre-release clean baseline

The one-time public-history reset was completed before acceptance began. It established a clean parentless public baseline while preserving the intended repository tree, after which normal protected development may continue with ordinary commits.

Do not repeat history rewriting merely to return the repository to a one-commit count. Pull-request records, workflow metadata, and other ordinary public-development traces may remain. Gate 7 verifies repository protection/settings and the final release tree; it does not perform another history rewrite.

## Final-release checklist

When the first public release is actually cut:

1. freeze the release-candidate structure and behavior;
2. replace `protocol_version: "unreleased"` with the chosen first real release identifier in `PROTOCOL.yaml` and set `protocol_status: released`;
3. replace the pre-first-release lifecycle metadata/rules and validator assumptions with the post-release lifecycle described in Gate 7, and prove that future development can be represented without losing or ambiguously overwriting the last released protocol identity;
4. update the `PROTOCOL.yaml` `release_rule` from pre-release guidance to the released lifecycle rule;
5. remove or replace pre-release-only wording explicitly in **`README.md` (Development status), `MIGRATIONS.md` (Current pre-release rule), and `AGENTS.md` (the public-template unreleased-version instruction)**, then sweep for any other remaining `unreleased` wording that would confuse a working copy created from the release;
6. verify that setup/activation produces and uses the repository-ID bootloader and that a working-repository rename does not require bootloader changes;
7. verify that `template_source.repository_id` resolves the public upstream and update discovery does not depend on its current owner/name;
8. run validator regression self-tests, deterministic structural validation, and the semantic repository health check;
9. publish the Gate 2B behavioral summary into `EVAL_RESULTS.md` and confirm the evidence remains applicable to the release tree, rerunning any behavioral/adversarial scenarios affected by the prescribed Gate 7 lifecycle/release transition;
10. verify README/SETUP/START_HERE/OPERATIONS/SECURITY/MIGRATIONS all describe the same release behavior;
11. verify the pre-acceptance clean baseline history has not been rewritten again and intended protection/settings are active;
12. only then treat the public template as the migration source for user-created copies.

## Future release entries

For each post-release protocol change that requires working copies to update, add a migration entry containing:

- source release(s);
- target release;
- required structural additions/removals/renames;
- semantic authority/routing changes;
- state transformations required;
- validator/eval changes;
- rollback/recovery considerations;
- the postcondition that proves migration complete.

Do not create release numbers solely to record wording cleanup. Version changes should correspond to meaningful public protocol changes.
