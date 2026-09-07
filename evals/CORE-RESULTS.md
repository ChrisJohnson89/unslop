# Core Product Results

## Release status: BETA; COMPARATIVE CLAIM NOT YET REVALIDATED

Treat the current implementation as an experimental beta. Its bounded
deterministic suite is green, but the cross-family trials below do not
revalidate its general writing-quality claim.
Earlier paired Luna runs predate fixes to raw-span scoring and per-case
efficiency enforcement. The newest independently annotated corpus missed its
frozen composition floor before either arm ran. The latest valid public product result
therefore remains the v9 no-ship below.

The failed V7 corpus was a benchmark-construction failure, not a product
failure. Its holdout contained five issue spans across two dirty documents and
four clean documents; the frozen floor was six issues across three dirty and
three clean documents. V7 was spent before a product call, and neither arm ran.
It provides no evidence that the current pipeline is better, worse, or equal to
raw Luna.

## Cross-family development — 2026-09-07

Provider support now includes Codex, Claude CLI, Gemini, and explicit open models
through Cloudflare AI Gateway. This is development support, not a new release
claim. The shared writing contract remains below 650 words. Scored trials below
use public tune cases and an independent, blinded Sol judge; no holdout or
holdback was opened. Human judge calibration has not been performed.

The latest Gemini 3.5 Flash trial improves repair while preserving clean text:

| Outcome | Gemini + UNSLOP | Plain Gemini |
|---|---:|---:|
| Dirty-document detection | 9 TP, 3 FP, 11 FN | 3 TP, 5 FP, 17 FN |
| Annotated issues repaired | 11/20 | 6/20 |
| Dirty-document factual constraints preserved | 7/7 | 7/7 |
| Clean documents left exact | 7/7 | 3/7 |
| Clean-document factual constraints preserved | 39/39 | 37/39 |

The marketing case repaired 6/11 issues and the technical case 5/9. Neither
fell back to the source, but nine issues still need repair. These counts do not
support an "all AI tells removed" claim.

The latest Luna dirty trial failed because a finding added a comma absent from
the source quote; it is unscored. Its current clean trial left 4/7 documents
exact, versus 3/7 for raw Luna, and made three false findings. Both arms
preserved all 39 factual constraints. It over-edited a subscription heading,
a stated social benefit, and a conference recap transition.
The preceding Luna trial fell back on both
documents: 0/20 repairs versus 16/20 for its raw arm. A Gemini 3.8 Flash trial
also failed, because a finding crossed a sentence boundary. Those failures are
retained; they do not disappear behind the successful Gemini 3.5 result.

Error analysis led to four changes: the source audit now reads the shared
findings contract; Gemini reasoning is bounded; required findings survive a
one-word grammatical extension; and phrase deletion can consume its trailing
inline space. The old whitespace gate rejected otherwise authorized deletions.
Unique exact quotes now also repair read-only evidence offsets. Ambiguous or
inexact quotes still fail. These corrections do not establish a model ranking.

Current predictions, native responses, failures, and verified metrics are
retained locally under `evals/runs/families/current/`. Earlier trials remain in
`baseline/`, `retry/`, `revised/`, and `final/`; the last two include implementation
snapshots for their earlier hashes. These ignored artifacts are development
evidence, not replacements for frozen release inputs. The seven clean and two
dirty cases are too few for generalization. Repeated frozen trials and human
calibration remain required by the
[comparison protocol](CORE-BENCHMARK.md#evaluation-discipline).

Cloudflare's request shape, explicit gateway/model routing, cache bypass, and
native evidence verification passed offline contract checks. Live open-model
runs still need a gateway ID and authorized token configured locally. The
available Wrangler login could list Workers AI models but could not list
gateways. Claude CLI is installed but unauthenticated. Neither provider has
live writing-quality evidence from this work.

The legacy `check.py --behavioral tune` run completed 15/20 calls and failed on
five 180-second timeouts: both macro-rewrite arms, the with-skill relational
audit, and both dirty-memo arms. It did not reach judging and is not a passing
behavioral result. The full deterministic/integrity gate and lint passed;
the executable budget is 74 examples and 400 outcome predicates. No new test
files were added. The generic skill-creator validator rejects the preexisting
`user-invocable` and `argument-hint` frontmatter keys; those interface fields
were preserved.

## Latest valid public result: NO-SHIP (v9)

The first frozen public v9 holdout does not establish that UNSLOP safely
improves unfamiliar AI-generated or mixed prose. It does show that the UNSLOP
contract helps Luna find and repair substantially more annotated issues than a
neutral editing prompt. That gain is not enough: the treatment also produced
more false positives, caused one real damaging edit, and left every dirty
document short of safe whole-document improvement.

The sealed holdback was not opened after this public failure.

## Frozen public result

Both generation arms used `gpt-5.6-luna`. The blinded adjudicator was
`gpt-5.6-sol`. The holdout contained three dirty documents and one clean
document, with 31 annotated issues and nine protected spans.

| Metric | Luna + UNSLOP | Plain Luna | Required |
|---|---:|---:|---:|
| Detection precision | 81.25% | 83.33% | at least 90% |
| Detection recall | 83.87% | 32.26% | at least 90% |
| Repair success | 87.10% | 58.06% | at least 90% |
| Preservation | 100% | 100% | 100% |
| Damage rate | 11.11% | 0% | 0% |
| Dirty documents safely improved | 0 of 3 | 0 of 3 | at least 80% |
| Clean documents left byte-exact | 1 of 1 | 1 of 1 | 100% |

UNSLOP won the paired comparison on all three dirty documents and tied the
clean document, but no dirty document cleared the absolute safety bar. Paired
wins therefore do not override the no-ship decision.

## What failed

The treatment made 26 true-positive findings, six false-positive findings, and
missed five gold issues. It repaired 27 of 31 annotated issues and preserved
all seven required factual or relational constraints. Its single protected-span
failure weakened a literal energy description from "harnessed energy" to
"received light."

The independent adversarial review found three recurring product failures:

- It treated accurate reports of another source's mistake or claim as errors
  in the current authorial voice.
- It treated literal technical language as AI-style metaphor and edited it
  unnecessarily.
- It missed consequential semantic problems, including unsupported decisions,
  unsafe recommendations, and an unsupported stability conclusion.

Two unsafe decisions remained in the conservation case. An unsafe repeat
recommendation remained in the rover case, alongside the damaging literal
energy edit. The ceramics case retained an unsupported stability conclusion.

## Evidence integrity

Thresholds were frozen before the v9 model run and were not changed afterward.
The manifest, shipping contract, runner, scorer, and scanner hashes are pinned
in `core-thresholds.json`. After model outputs existed, scorer input
normalization was corrected and an initially proposed policy-text heuristic was
rejected by independent review. The final scorer permits deterministic
protected-span overrides only when the manifest explicitly declares
`enforcement: exact_span`; v9 used no such override. The resulting v17 score is
reproducible but is not represented as a pristine pre-frozen trial.

Raw local evidence contains prompt hashes, model events, parsed responses, and
the independent judgments under `evals/runs/core/holdout-v17/`. That directory
is intentionally ignored because the prediction artifact is large and may
contain provider event envelopes. The stable public inputs and frozen hashes
are committed instead.

## Engineering performance

On the measured development machine, `python3 evals/check.py --full` completed
in about three seconds with no expected or unexpected failures. The deterministic
surface is explicitly capped at 80 executable examples and 400 expanded outcome
predicates; the current counts are printed by
`python3 evals/check_complexity_budget.py`. The scanner contract separately
reports 36/36 structural patterns, 16/16 literal triggers, and 20/20 protected
categories.

## Next valid experiment

Do not tune directly against v9 and continue calling it a public holdout. Use
its failures as development evidence, improve the general attribution,
literal-language, and semantic-risk logic, and then evaluate once on a newly
authored, independently annotated public corpus. Open the sealed holdback only
after that new public corpus passes the frozen absolute gates.
