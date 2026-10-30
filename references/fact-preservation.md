# Preserve claims and relationships

Keep facts intact while changing their presentation. Use this reference when a
source contains quantities, dates, obligations, scientific uncertainty, or several
actors. The local validator catches only some errors; compare the text yourself.

## Keep exact

Preserve names, identifiers, dates, quantities, units, ranges, version numbers,
URLs, citations, quotations, and code. Do not round a number, silently convert a
unit, expand an acronym with a guessed definition, or rename a component.

Keep each value attached to its original referent. The same numbers appearing
somewhere in the output is insufficient: swapping a 30-second timeout and a
10-second retry interval still changes the facts.

## Keep meaning

- **Direction:** reduced from 500 to 250 is not increased to 500.
- **Basis:** a forecast, target, trial result, and production measurement differ.
- **Uncertainty:** may, might, estimated, preliminary, and untested carry information.
- **Causality:** happened after does not mean caused by.
- **Scope:** some, most, all, only, approximately, and exceptions affect the claim.
- **Conditions:** if, unless, until, and except must retain their logical role.
- **Obligations:** must, must not, may, and should are not interchangeable.
- **Attribution:** an assertion by a customer stays their assertion; an unknown
  actor stays unknown. Never assign a completed action to someone without evidence.
- **Relationships:** preserve who acts, who receives the action, and which object
  it affects. Do not resolve ambiguous pronouns by guessing.

## Before returning a rewrite

Compare every affected sentence with the source and its neighbors. Check numbers
with units and referents, not as a bag of tokens. Read negations and conditions
aloud in meaning: would the reader now take a different action or believe a
stronger claim? Keep unchanged sentences in place.

For an internal contradiction, preserve the evidence and distinguish it from the
conclusion. If the text cannot support a safe resolution, flag the conflict.
Do not perform unsolicited external fact-checking during a prose edit.

A preservation-script exit 0 means its implemented checks found no loss. It is
not a certificate that all facts or relationships survived. For sensitive
requirements, use `validate_preservation.py --strict` when execution is available
and review semantic warnings. Do not report strict validation as passed when it
could not run.
