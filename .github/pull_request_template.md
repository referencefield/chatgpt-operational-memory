## What problem does this solve?

Describe the user failure mode, friction, or missing capability.

## What changed?

Summarize the smallest change that addresses it.

## Why does it belong in this template?

Explain why this fits a lay-user, low-infrastructure operational-memory protocol rather than requiring an advanced agent/memory framework.

## Protocol impact

Check all that apply:

- [ ] Routing / retrieval behavior changed
- [ ] Persistence / authority behavior changed
- [ ] Privacy or security guidance changed
- [ ] Required repository topology changed
- [ ] `PROTOCOL.yaml` was updated if required
- [ ] `EVALS.md` was updated if model-mediated behavior changed
- [ ] `tools/validate_protocol.py` was updated if a deterministic structural invariant changed
- [ ] Release/migration guidance was updated if a released working copy would need migration

## Verification

- [ ] I did not include secrets, private memory, credentials, or sensitive personal information
- [ ] I preserved the existing route-first / source-of-record discipline
- [ ] I ran `python tools/validate_protocol.py` when protocol structure was affected
- [ ] I verified that any new durable file/category has a clear role, recurrence, retrieval trigger, authority, navigation path, and user-visible reason to exist

## Additional notes

Anything reviewers should know.
