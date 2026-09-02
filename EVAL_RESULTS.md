# Behavioral Evaluation Results

Status: **No qualifying behavioral run has been published yet.**

This file is the results location for the adversarial scenarios in `EVALS.md`. It exists to prevent a structural-validator PASS from being mistaken for evidence that model-mediated behavior also passed.

The repository's deterministic validator and GitHub Action test structural invariants only. They do not prove correct routing, retrieval claims, persistence classification, write verification, authority handling, or over-persistence behavior.

## What counts as a publishable run

A behavioral run should be recorded here only when the evaluation is meaningfully independent of the expected answers. At minimum:

- use a fresh conversation/context for the evaluated model/surface;
- provide the scenario/task and necessary repository access, but do not expose the corresponding `Expected` section from `EVALS.md` before the model acts;
- judge the observed behavior against the written expectation afterward;
- record the date, model/surface, scenario IDs, pass/fail counts, and material failure modes;
- preserve enough notes to distinguish an actual behavior failure from a tool outage or unavailable capability;
- do not convert ambiguous outcomes into passes merely to improve the score.

A same-session self-review in which the model has already read the expected answers is useful for development but is **not** a publishable independent behavioral result.

## Published runs

_None yet._

When a qualifying run exists, add a compact summary table such as:

| Date | Model / surface | Scenarios | Pass | Fail | Material notes |
| --- | --- | ---: | ---: | ---: | --- |
| YYYY-MM-DD | Example | E-01–E-37 | 0 | 0 | Replace with actual observed results |

Then record only the failures, ambiguities, or especially informative passes that deserve detail below the table. Do not turn this file into a transcript archive.

## Release interpretation

Until at least one qualifying run is recorded, public claims should remain limited to design review, adversarial scenario coverage, live GitHub write/readback experience, and deterministic structural validation. Do not claim longitudinal or independently demonstrated behavioral reliability.
