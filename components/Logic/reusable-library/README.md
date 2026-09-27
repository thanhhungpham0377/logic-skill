# Reusable Logic Library

This library stores generalized, evidence-backed behavior patterns that can transfer between projects. It is not a dump of project requirements.

## Promotion rules

A candidate may be promoted only after review confirms that it:

- has been generalized beyond one project's names, architecture, and assumptions;
- describes a recurring behavior/invariant rather than a one-off implementation;
- includes a verification idea and known limits;
- includes provenance links and a review date;
- contains no secrets, personal data, or private project information.

Run `python scripts/scan_logic.py --project <path> --write-report` to produce candidates. The scanner is a heuristic locator; it does not validate semantics or promote rules automatically.

## Evidence discipline

Label each pattern as `candidate`, `observed`, or `validated`. A pattern becomes `validated` only after it has been applied and checked in more than one distinct project context. Record counterexamples and retire patterns that prove misleading.
