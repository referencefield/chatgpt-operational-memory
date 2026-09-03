# Global Durable Decisions

Record only durable decisions likely to matter across projects or govern the repository/user's broader operating system.

Project-specific durable decisions belong in the relevant `projects/<slug>/DECISIONS.md` once the workstream has its own project boundary.

Do not record every suggestion, preference, or conversational choice. Stable collaboration preferences belong in `WORKING_STYLE.md`, not here.

## Decision format

### D-001 — Example only

- **Status:** active | superseded
- **Date:** YYYY-MM-DD
- **Decision:** State the durable global decision in one sentence.
- **Why / evidence:** Give only the brief basis future recovery needs.
- **Supersedes:** none, or prior decision ID(s).
- **Superseded by:** none, or later decision ID.

Delete this example when the first real decision is recorded.

## Active decisions

_No global durable decisions have been recorded yet._

## Superseded decisions

_None yet._

## Authority and routing rules

- The user's current explicit instruction wins.
- Active entries in this file govern cross-project/global durable decisions.
- Root `CURRENT.md` governs cross-project/global transient state.
- Project-local `CURRENT.md` and `DECISIONS.md` govern their projects, subject to applicable global decisions.
- `WORKING_STYLE.md` governs active collaboration preferences about how work is performed, not what a project has decided.
- If global current state conflicts with an active global durable decision, do **not** silently choose one. Surface and reconcile the inconsistency.
- Git history is historical evidence, not active authority by itself.
- Do not promote an ambiguous conversational inference into an active durable decision. If the user did not clearly authorize the decision or its durable status, ask before activating it.
- If the user explicitly says **"make this a durable decision"**, **"record this decision"**, or otherwise clearly states a final durable decision in a context that authorizes persistence, no additional confirmation is required.
- Before recording here, confirm the decision is genuinely global/cross-project. If it governs only one registered project, route it to that project's `DECISIONS.md` instead.
- When a new durable decision is recorded, report the exact one-sentence `Decision` field so semantic intent can be checked, along with the verified write/commit receipt when available.

When a later global durable decision replaces an earlier one:

1. record the new decision as `active`;
2. identify the prior decision in `Supersedes`;
3. mark the prior decision `superseded` and identify the new decision in `Superseded by`;
4. move or retain the older entry under `Superseded decisions` so its inactive status is visually unambiguous;
5. update root `CURRENT.md` and any materially affected project front doors/current-state files;
6. verify the coupled state is consistent before reporting completion.

Do not let an older decision continue governing merely because it remains in Git history.
