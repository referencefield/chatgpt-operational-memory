# Durable Decisions

Record only decisions likely to matter in later conversations.

Do not record every suggestion, preference, or conversational choice.

## Decision format

### D-001 — Example only

- **Status:** active | superseded
- **Date:** YYYY-MM-DD
- **Decision:** State the durable decision in one sentence.
- **Why / evidence:** Give only the brief basis future recovery needs.
- **Supersedes:** none, or prior decision ID(s).
- **Superseded by:** none, or later decision ID.

Delete this example when the first real decision is recorded.

## Active decisions

_No durable decisions have been recorded yet._

## Superseded decisions

_None yet._

## Authority and supersession rules

- The user's current explicit instruction wins.
- Active entries in this file govern durable decisions.
- `CURRENT.md` governs transient/current working state.
- If `CURRENT.md` conflicts with an active durable decision, do **not** silently choose one. Surface the inconsistency and reconcile the affected state.
- Git history is historical evidence, not active authority by itself.
- Do not promote an ambiguous conversational inference into an active durable decision. If the user did not clearly authorize the decision or its durable status, ask before activating it.
- If the user explicitly says **"make this a durable decision"**, **"record this decision"**, or otherwise clearly states a final decision in a context that authorizes persistence, no additional confirmation is required.
- When a new durable decision is recorded, report the exact one-sentence `Decision` field to the user so semantic intent can be checked, along with the verified write/commit receipt when available.

When a later durable decision replaces an earlier one:

1. record the new decision as `active`;
2. identify the prior decision in `Supersedes`;
3. mark the prior decision `superseded` and identify the new decision in `Superseded by`;
4. move or retain the older entry under `Superseded decisions` so its inactive status is visually unambiguous;
5. update `CURRENT.md` if the decision changes current working state;
6. verify both files are consistent before reporting completion.

Do not let an older decision continue governing merely because it remains in Git history.
