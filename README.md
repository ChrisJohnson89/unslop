# Unslop

A native GPT skill for clearer writing that keeps your facts and voice.

Ask Unslop to edit a draft, audit awkward passages, or work from samples of your
writing. GPT reads and edits in the current conversation. Optional local Python
checks catch familiar patterns and some preservation errors.

```text
Use $unslop to clean up this email. Keep the uncertainty and technical details.
Use $unslop to audit this draft. Flag problems without rewriting it.
Use $unslop to build a voice card from these three samples.
Use $unslop to rewrite this announcement using my voice card.
```

In ChatGPT's desktop skill picker, select Unslop with `@`. In Codex, use `$unslop`.
An audit leaves the text unchanged. A rewrite repairs confirmed defects; clean
writing stays unchanged. The skill does not determine whether someone used AI.

## Install

Ask Skill Installer in Codex:

```text
$skill-installer install the skill at https://github.com/ChrisJohnson89/unslop
```

For a manual local install, clone the repo and copy its runtime files into your
personal skills directory:

```bash
git clone https://github.com/ChrisJohnson89/unslop.git
cd unslop
python3 tools/package_skill.py
```

This creates `dist/unslop.skill`, a ZIP containing the `unslop/` skill folder.
Extract that folder into your local skills directory (the current documented
personal location is `~/.agents/skills/`; existing Codex setups may use
`~/.codex/skills/`). Keep only one installed copy. Start a new chat; restart the
app if Unslop has not appeared. This is a local skill install, not publication to
ChatGPT's web plugin directory. See [OpenAI's skills guide](https://learn.chatgpt.com/docs/build-skills).

No API key, MCP server, plugin manifest, or third-party Python package is needed.
The skill can edit without Python. When checks cannot run, a requested validation
report explicitly says the review was manual.

## What changed in this fork

- Native GPT task routing and UI metadata; no Claude slash-command setup.
- Evidence-based voice cards built from supplied samples, without model training
  or automatic harvesting of private history.
- Contextual editing guidance for support replies, documentation, reports, and
  business drafts. Keep defined terms, useful courtesy, uncertainty, and unknown actors.
- A manual review path that cannot claim fabricated tool results.
- A runtime-only archive, tested after extraction outside the repository.
- Preservation checks now catch written-out durations, changed whole quantities,
  and numbers paired with the wrong units.

The port removes the old multi-provider benchmark infrastructure, model-tier
routing, statistical voice profiling/refinement, contribution automation,
Wikipedia sync, legacy presets, and implementation plans. The retained scanner,
structure, and preservation tests still run offline.

## Research behind the editing guidance

The [editorial reference](references/editorial-context.md) links the sources and
shows original before/after examples. It draws on [GOV.UK clear-language guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/),
Google's guidance on [consistent terminology](https://developers.google.com/tech-writing/one/words),
[voice and tone](https://developers.google.com/style/tone), and
[appropriate passive voice](https://developers.google.com/style/voice).
[Liang et al.](https://arxiv.org/abs/2304.02819) motivates caution about confusing
writing style with AI authorship; that study evaluates particular detectors,
not Unslop or every current detector.

These sources inform the skill. They do not establish that this port improves
writing on every task. The upstream project's last documented core benchmark
reported a [no-ship result](https://github.com/theclaymethod/unslop/blob/17ed39c9d0b522f44190ff0c6233867eadee192a/evals/CORE-RESULTS.md).
This fork does not inherit a passing quality claim from its offline tests.

## Local checks

Requires Python 3.8+ for the standard-library scripts:

```bash
python3 evals/check.py
python3 tools/package_skill.py
```

The check runs the retained contract examples, minimal-pair checks, scanner
coverage, silhouette reference checks, and isolated installation tests. Behavioral
scenarios in [`evals/adversarial-evals.json`](evals/adversarial-evals.json) require
actual GPT outputs and contextual review; validating their shape does not grade them.

To inspect a draft directly:

```bash
python3 scripts/banned_phrase_scan.py draft.md
python3 scripts/structure_scan.py draft.md
python3 scripts/silhouette_scan.py draft.md
python3 scripts/validate_preservation.py original.md edited.md
```

Findings are candidates for review. A clean scan cannot prove fact preservation,
clarity, authorship, or the absence of subtle problems.

## Layout

```text
SKILL.md                 Native skill instructions and routing
agents/openai.yaml       GPT/Codex picker metadata
references/              Editing contract, voice guidance, contextual examples
scripts/                 Optional offline checks
assets/                  Runtime reference data
evals/                   Developer regression fixtures and behavioral scenarios
tools/package_skill.py   Runtime-only archive builder
```

Derived from [theclaymethod/unslop](https://github.com/theclaymethod/unslop),
originally authored by Clayton Kim. This fork preserves the upstream skill's MIT
license declaration and attribution. Git history retains the original implementation.
