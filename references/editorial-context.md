# Edit for the reader

Use this reference for support replies, documentation, reports, and business
drafts. These are applications of the core contract, not new scanner patterns.
Infer audience and purpose from the request; ask only when the answer would
change the edit materially. Preserve register when the user has not requested
a different one. Read only the relevant examples below.

## Context checks

- **Useful information:** A reader should be able to identify the stated result,
  decision, or next action. Delete empty introductions when they obscure that
  information. Do not invent missing owners, deadlines, results, or evidence.
- **Terminology:** Keep one name for one concept. Repeated component names can
  prevent ambiguity; synonyms added for variety can introduce it. Preserve
  defined terms, API names, UI labels, and domain-valid jargon. Flag an unfamiliar
  term for explanation only when the audience needs it; do not invent a definition.
- **Agency:** Prefer an explicit actor when the source supplies one and the
  sentence is unclear. Passive voice can be right when the actor is unknown,
  irrelevant, or less important than the result. Never invent an actor to avoid it.
- **Tone:** Useful courtesy, warmth, and direct requests belong in a customer
  reply. Removing every “please” or contraction can make it less natural.
  Do not add fake experience, anecdotes, slang, typos, or opinions to “humanize” it.
- **Evidence:** Preserve the difference between observed, inferred, planned,
  completed, and validated. “Restarted” does not mean “fixed”; a target is not a
  result; “may” does not mean “will.” Keep attribution with the claim it qualifies.
- **Shape:** Headings, bullets, and short sentences are useful when the content
  calls for them. Neither a fixed sentence length nor varying every sentence is
  a goal. Treat readability and cadence metrics as diagnostic clues.
- **Authorship:** Review writing quality, not who wrote it. Never assign an AI
  probability, promise to evade detectors, or treat non-native English, a dialect,
  or consistent punctuation as proof of machine authorship.

## Original before/after examples

### Support reply: keep the validation limit

Before: “It is important to note that we restarted the worker at 09:15 UTC. This
may resolve the timeout; checkout is still untested. Please retry the upload.”

After: “We restarted the worker at 09:15 UTC. This may resolve the timeout;
checkout is still untested. Please retry the upload.”

Only the importance framing is empty. Do not turn the restart into a root cause
or successful checkout test, and do not remove the retry request.

### Product update: keep the direction of the change

Before: “We're excited to announce a game-changing update. Version 3.2 reduces
the export limit from 500 rows to 250 rows.”

After: “Version 3.2 reduces the export limit from 500 rows to 250 rows.”

The smaller limit is not an improvement merely because the introduction says so.
Retain both quantities and the direction; do not invent a performance benefit.

### Technical documentation: leave precise repetition alone

“The lease holder renews the lease every 30 seconds. If the lease expires, the
lease holder must stop writing.”

Keep it unchanged. “Owner,” “leader,” and “client” are not interchangeable with
the defined role just because a repeated noun looks monotonous.

### Incident report: an unknown actor stays unknown

“The signing key was revoked at 14:20 UTC. The operator has not been identified.”

Keep it unchanged. “The security team revoked the key” invents attribution.

### Business proposal: retain an estimate

Before: “Our cutting-edge approach represents a paradigm shift. The pilot may
reduce review time by 10%, based on six internal trials.”

After: “The pilot may reduce review time by 10%, based on six internal trials.”

Keep the estimate, sample size, and basis. Do not upgrade this to a measured
production result or imply independent verification.

## Sources and limits

Reviewed 2026-10-30. The examples above are original. The following sources
inform editorial judgment; they do not validate Unslop's performance.

- [GOV.UK: Use clear language](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/)
  supports accessible language for general and specialist readers.
- [Google: Voice and tone](https://developers.google.com/style/tone) supports
  clear, respectful, conversational documentation without forced informality.
- [Google: Words](https://developers.google.com/tech-writing/one/words) supports
  consistent terminology and clear references.
- [Google: Active voice](https://developers.google.com/style/voice) explains both
  the preference for visible actors and legitimate passive constructions.
- [Liang et al., 2023](https://arxiv.org/abs/2304.02819) found bias against
  non-native English writing in the detectors they studied. This is not an
  assessment of every current detector or an evaluation of Unslop. It supports
  keeping stylistic review separate from authorship accusations.
