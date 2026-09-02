# Protocol Migrations

`PROTOCOL.yaml` gives each working copy an explicit operational-memory protocol version.

This file records changes that require a user-created private repository to update structure or operating behavior. Ordinary wording/documentation improvements that do not change required structure or semantics do not require a migration entry.

## How to check your version

Retrieve `PROTOCOL.yaml` from your working repository and read `protocol_version`.

Do not infer version from repository age, README wording, or the current public template.

## Migration principles

- Migrations must preserve valid user state rather than overwrite it with blank template content.
- Route/reconcile existing content before introducing a new required home.
- Treat a migration affecting multiple files as a write-set with explicit postconditions.
- Reread and verify the complete migrated structure before reporting completion.
- Never claim a private working copy has upgraded merely because the public template changed.
- Protocol migration is separate from Git history rewriting.

## 1.0 — First versioned protocol release

This is the first release with an explicit machine-readable version.

Required global protocol structure:

- `PROTOCOL.yaml`
- `START_HERE.md`
- `CURRENT.md`
- `DECISIONS.md`
- `KNOWLEDGE.md`
- `WORKING_STYLE.md`
- `PROJECTS.md`
- `projects/_TEMPLATE/PROJECT.md`
- `projects/_TEMPLATE/CURRENT.md`
- `projects/_TEMPLATE/DECISIONS.md`
- `projects/_TEMPLATE/KNOWLEDGE.md`

Human documentation is separated by role:

- `SETUP.md` — installation only;
- `START_HERE.md` — runtime routing/persistence protocol;
- `OPERATIONS.md` — maintenance, health, recovery, project creation, write-sets;
- `SECURITY.md` — privacy and hardening;
- `MIGRATIONS.md` — protocol upgrades;
- `EVALS.md` — behavioral/adversarial test scenarios.

The recommended persistent ChatGPT instruction is now a **bootloader** that points to `START_HERE.md` rather than duplicating the full runtime protocol.

Coupled multi-file changes now use an explicit write-set model: intent, expected writes, current preconditions, required postcondition, full readback verification.

Knowledge and working-style entries may include `Review after:` lifecycle metadata. Soft budgets are declared in `PROTOCOL.yaml` as warning indicators.

An advisory structural validator is available at `tools/validate_protocol.py` and can run through `.github/workflows/protocol-validation.yml`. It is not a required status check in this protocol.

### Migrating an older unversioned working copy

If your repository was created before `PROTOCOL.yaml` existed:

1. retrieve the current public template's migration documentation and your private repository's existing front door/state files;
2. preserve all valid private state;
3. add the missing protocol/documentation/validator files without replacing populated state files with blank examples;
4. update the persistent ChatGPT instruction to the small bootloader shown in current `SETUP.md`;
5. reconcile any project-specific information that still lives in global files;
6. add `Review after:` only where useful; do not invent dates merely to populate the field;
7. run the structural validator and a semantic repository health check;
8. verify `PROTOCOL.yaml` reports `protocol_version: "1.0"` only after the complete required structure and routing behavior are present.

If migration partially succeeds, report **protocol migration is temporarily inconsistent** and reconcile before claiming the version upgrade complete.

## Future releases

For each future protocol version, record:

- prior version(s) supported for migration;
- required structural additions/removals/renames;
- semantic authority/routing changes;
- state transformations required;
- validator/eval changes;
- rollback/recovery considerations;
- the postcondition that proves migration complete.

Do not create migrations solely to keep version numbers moving. Version changes should correspond to meaningful protocol changes.