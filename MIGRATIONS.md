# Protocol Migrations

`PROTOCOL.yaml` gives each working copy an explicit protocol release/status and identifies the public template source.

This repository is still **pre-release**. Pre-release development changes are folded into the eventual baseline release rather than preserved as fake release-to-release migrations.

## Public template source vs. working repository

The `template_source` entry in `PROTOCOL.yaml` identifies the public upstream used only for update discovery and migration guidance. It is **not** the required name of a user's working repository.

A private working copy may have any GitHub owner/name. Renaming a working repository does not change its internal protocol or durable state and does not require a protocol migration. If an external reference such as a ChatGPT Custom Instructions URL stops resolving after a rename, refresh that reference to the working repository's current URL and continue using the existing state.

Do not rewrite `template_source.repository` to the private working repository. Doing so would confuse the upstream update source with the user's runtime repository.

## Current pre-release rule

While `PROTOCOL.yaml` reports:

`protocol_version: "unreleased"`

there is no ordered public protocol version to compare against another unreleased copy.

During this phase:

- do not infer chronology from commit count, repository age, or prior draft version labels;
- do not preserve temporary development version numbers in user-facing docs;
- compare the local and template manifests/content only when an explicit development comparison is needed;
- preserve private working state if a development copy is being refreshed;
- do not auto-migrate merely because the public template changed.

The first real protocol identifier should be assigned only when the release candidate is frozen.

## Update discovery

The template source is declared in `PROTOCOL.yaml`.

When checking for updates:

1. retrieve the working copy's `PROTOCOL.yaml`;
2. retrieve the template source's declared manifest;
3. compare release/status and relevant structural fields;
4. if both are `unreleased`, report that ordered version comparison is unavailable and compare content only when explicitly needed;
5. after real releases exist, use their release identifiers plus this file to determine the applicable migration path;
6. never overwrite populated private state with blank template state;
7. never claim an upgrade merely because the public template changed.

If the template source cannot be reached, report update status as **not checked**.

## Migration principles after release

When a future release changes protocol structure or semantics:

- preserve valid user state rather than replacing it with template examples;
- route/reconcile existing content before introducing a new required home;
- treat a migration affecting multiple files as a write-set with explicit postconditions;
- reread and verify the complete migrated structure before reporting completion;
- separate protocol migration from Git history rewriting;
- if migration partially succeeds, report **protocol migration is temporarily inconsistent** until the full postcondition holds.

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
2. replace `protocol_version: "unreleased"` with the chosen first real release identifier;
3. set an appropriate released status in `PROTOCOL.yaml`;
4. remove any remaining pre-release-only wording that would confuse a working copy created from the release;
5. run deterministic structural validation and the semantic repository health check;
6. run the behavioral/adversarial eval set relevant to routing, persistence, update discovery, maintenance, and failure handling;
7. verify README/SETUP/START_HERE/OPERATIONS/SECURITY/MIGRATIONS all describe the same release behavior;
8. perform the controlled one-time history cleanup above if a clean release baseline is still desired;
9. only then treat the public template as the migration source for user-created copies.

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