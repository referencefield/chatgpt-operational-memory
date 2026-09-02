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

The first real protocol identifier should be assigned only when the release candidate is frozen.

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

## Objective pre-release acceptance gate

Do not call the repository **done**, **release-ready**, or recommend stopping substantive review merely because an architecture/design sweep found no further improvements. Release readiness is established only by the evidence below against a frozen candidate.

### Gate 1 — Freeze candidate

Record the candidate `main` commit SHA and tree SHA. From that point until the gate completes, do not make opportunistic improvements. Any accepted repository change invalidates the candidate and starts the gate again from a new frozen SHA.

### Gate 2 — Deterministic repository checks

Against the frozen candidate:

- run `tools/validate_protocol.py` and require `RESULT: PASS` or consciously adjudicate every `Watch` signal;
- verify repository visibility/template status, default branch, branch set, and intended public-repository ruleset/settings;
- verify no setup/probe files or unintended artifacts remain;
- verify `START_HERE.md` and other declared soft budgets;
- verify the public template-source repository ID resolves correctly.

Record the exact candidate SHA used. A validator result from an earlier commit does not satisfy this gate.

### Gate 3 — Zero-reading template-copy acceptance test

Create a new **private** repository using GitHub **Use this template**, give it an arbitrary name, and approach it as a first-time non-expert user who has not read the repository files.

Using a fresh ChatGPT conversation and the documented Fast start only:

1. run activation from the private repository URL;
2. require the correct repository ID, privacy check, reversible CRUD/readback, cleanup, and `Operational memory: READY` receipt;
3. install the repository-ID bootloader supplied by activation;
4. create a small piece of genuine durable project state through normal conversation;
5. start another fresh conversation and recover that state from the repository;
6. rename the private repository;
7. start another fresh conversation and verify the same repository ID resolves to the renamed repository, the state is recovered, and a verified write succeeds without changing the bootloader.

Failure or user confusion is release evidence. Fix the smallest root cause, freeze a new candidate, and restart the gate.

### Gate 4 — Surface smoke tests

On the frozen candidate:

- **Codex:** verify root `AGENTS.md` enters through `PROTOCOL.yaml` / `START_HERE.md`, uses the existing memory topology, and can perform a verified repository-backed state change without creating a competing memory system.
- **ChatGPT Work:** when the required write-capable GitHub plugin/app is available, verify it uses the same repository ID/front door and preserves the same routing, privacy, write-set, and readback rules. If the required capability is unavailable on the tested Work surface, record that limitation and qualify public compatibility wording rather than inventing a pass.

### Gate 5 — Independent adversarial release audit

Run the maintained final pre-release audit against **every tracked file in the frozen candidate**, with the reviewer instructed to report only and not modify the repository. The reviewer must distinguish PASS/WARN/FAIL/BLOCKED and provide evidence for each finding.

Triage every finding into exactly one of:

- **Blocker:** must be fixed before release;
- **Should-fix:** cheap/material enough to fix before the first release;
- **Deferred:** consciously accepted for a later release with the reason recorded.

Do not accept or reject a finding merely because it agrees or disagrees with prior design intent. Reproduce or verify material claims against the actual candidate and current product capability.

### Gate 6 — Post-fix regression gate

If Gates 2–5 caused any repository change:

1. freeze the new candidate SHA/tree;
2. rerun deterministic validation against that exact candidate;
3. rerun the portions of the zero-reading/surface tests affected by the changes;
4. rerun the independent audit as a regression/delta audit, explicitly checking accepted fixes for newly introduced failures.

The candidate passes only when there are **zero unresolved blockers**, every remaining warning is consciously classified, and no new material regression is found.

### Gate 7 — Release transition

Only after Gates 1–6 pass:

- assign the first real protocol release identifier/status;
- execute the controlled one-time history cleanup if still desired;
- restore and verify the intended public-repository protection/settings;
- rerun deterministic validation against the final release tree;
- tag/publish the release;
- create one final private copy using **Use this template** and repeat the activation smoke test against what GitHub actually ships.

That final private-copy activation is the release artifact check. A successful test against the source repository alone is not sufficient.

### Stopping rule

After the gate passes, new suggestions do not automatically reopen the release. Reopen only for a reproducible blocker, material regression, security/privacy defect, false product claim, or a change that clearly exceeds the agreed diminishing-returns threshold. Other improvements become post-release candidates.

## One-time pre-release history cleanup

The public repository currently uses lightweight `main` protection that blocks deletion and non-fast-forward updates. A final pre-release history reset/squash is therefore a deliberate maintenance exception, not a normal operational-memory action.

When the release candidate is ready for its one-time clean baseline:

1. freeze and validate the complete intended release tree, including the real release identifier/status;
2. record the pre-rewrite `main` commit SHA and tree SHA, and keep an independent local clone/archive if recovery from the development history would be costly;
3. verify that no non-`main` branch contains work that must survive into the release tree;
4. temporarily suspend only the protection necessary to permit the planned non-fast-forward rewrite; if the ruleset cannot be narrowed, disable it only for the controlled rewrite window;
5. create/repoint `main` to the clean release-baseline commit whose tree matches the frozen intended release tree;
6. immediately restore the normal `main` protection before any unrelated repository work;
7. verify the expected `main` commit/tree, protection rules, branch set, repository visibility/settings, and structural validator result;
8. create the public release/tag only after those postconditions hold.

Do not treat this as a requirement to erase every GitHub development artifact. Pull-request records, workflow metadata, and other ordinary public-development traces may remain. The release objective is a clean canonical release history and verified release tree, not a claim that development never happened.

## Final-release checklist

When the first public release is actually cut:

1. freeze the release-candidate structure and behavior;
2. replace `protocol_version: "unreleased"` with the chosen first real release identifier in `PROTOCOL.yaml` and set the appropriate released status there;
3. update the `PROTOCOL.yaml` `release_rule` from pre-release guidance to the released lifecycle rule;
4. remove or replace pre-release-only wording explicitly in **`README.md` (Development status), `MIGRATIONS.md` (Current pre-release rule), and `AGENTS.md` (the public-template unreleased-version instruction)**, then sweep for any other remaining `unreleased` wording that would confuse a working copy created from the release;
5. verify that setup/activation produces and uses the repository-ID bootloader and that a working-repository rename does not require bootloader changes;
6. verify that `template_source.repository_id` resolves the public upstream and update discovery does not depend on its current owner/name;
7. run deterministic structural validation and the semantic repository health check;
8. run the behavioral/adversarial eval set relevant to routing, persistence, update discovery, maintenance, and failure handling;
9. verify README/SETUP/START_HERE/OPERATIONS/SECURITY/MIGRATIONS all describe the same release behavior;
10. perform the controlled one-time history cleanup above if a clean release baseline is still desired;
11. only then treat the public template as the migration source for user-created copies.

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
