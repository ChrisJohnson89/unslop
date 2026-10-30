# Agent instructions

This fork contains two native GPT/Codex skills. The current GPT session performs
drafting, editing, and voice work. Keep each installable as a standalone skill; do not reintroduce a
plugin manifest, external model runner, Claude setup, or automatic history harvest.

## Source and scope

- `SKILL.md` is the entrypoint. Keep it concise and route conditional detail into
  `references/`. `agents/openai.yaml` supplies picker metadata.
- The root skill, `unslop`, handles revisions and audits. `skills/unslop-write/`
  is the independent, automatically discoverable drafting skill. Keep routine
  drafting free of scanners, temporary files, and revision-reference loading.
  Configured style retrieval is scoped to the current request, not a history harvest.
- Local Python checks are optional supporting evidence and use only the standard
  library. They are not authorship detectors or complete semantic validators.
- An edit preserves facts, attribution, scope, uncertainty, quotes, code, and
  useful terminology. Scanner candidates need contextual confirmation.
- Voice cards use supplied or explicitly authorized samples. Never fabricate
  persistent memory, training, tool results, or a numerical voice score.

## Changes and tests

Add regression examples before changing scanner or preservation behavior. Scanner
patterns need a positive example and a contextual false-positive protection;
collocation-gated words also need a jargon-use example. Preserve the existing
assertions. Do not remove cases, weaken assertions, or add XFAILs to make a fix pass.

Run from the repository root:

```bash
python3 evals/check.py
python3 -m compileall -q scripts tools evals
python3 tools/package_skill.py
python3 tools/package_skill.py --skill unslop-write
```

The canonical check runs all contract examples under `evals/fixtures/contracts/`,
minimal pairs, pattern coverage, silhouette calibration, and the install test.
New `evals/check_*.py` tools use the shared `_check_support` import seam.

Skill behavior changes need a case in `evals/adversarial-evals.json`. Review actual
GPT responses against the cases when possible; do not present offline checks or
scenario-schema validation as live behavioral evidence. Record any unrun checks.
Use Skill Creator's `quick_validate.py` when available.

## Packaging

`tools/package_skill.py` includes only `SKILL.md`, `agents/`, `references/`,
`scripts/`, and `assets/` from the selected skill root. Each skill has its own
archive and must work without the other installed. Keep user drafts, voice cards,
tests, git metadata, and run outputs out of the archive. Verify the extracted skill from a directory
outside the checkout. Do not modify installed user copies while developing.
