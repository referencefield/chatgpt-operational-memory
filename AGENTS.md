# Codex Bootloader

This file exists only to make the repository safe and legible when opened with OpenAI Codex. It is **not** a second operational-memory protocol.

For any task involving this repository's operational-memory behavior or state:

1. read `PROTOCOL.yaml`;
2. read `START_HERE.md`;
3. follow `START_HERE.md` as the runtime routing and persistence authority;
4. retrieve only the minimum relevant scope rather than broad-loading the repository;
5. preserve populated user state when modifying a working copy;
6. use the repository's write-set, readback, concurrency, and fail-loud rules for consequential changes.

For changes to the public template itself:

- do not add user-specific memory;
- keep `protocol_version: "unreleased"` while `protocol_status` is `development` or `acceptance_candidate`; assign the first real protocol identifier only after the acceptance gate passes during the release transition;
- do not enter `acceptance_candidate` from ordinary development without the explicit authorization required by `MIGRATIONS.md`;
- update `PROTOCOL.yaml` if required topology changes;
- update `EVALS.md` when model-mediated behavior changes;
- update `tools/validate_protocol.py` when a new deterministic structural invariant is justified;
- run `python tools/validate_protocol.py` before claiming structural completion.

If this file conflicts with a current explicit user instruction, higher-level system/safety instruction, or the current protocol declared by `PROTOCOL.yaml` and `START_HERE.md`, the higher/current authority wins.
