# Contributing

This fork focuses on native GPT editing and evidence-based voice cards. Keep
changes scoped to that workflow. See [AGENTS.md](AGENTS.md) for the checks.

For a scanner change, add a failing example and a literal or domain-valid
protection to `evals/fixtures/contracts/scanner-examples.json` first. For a
preservation change, add a before/after case to the preservation table. Update
`exact_total` without changing existing assertions. Useful contextual pairs live
in `evals/fixtures/pairs/`.

For instruction changes, add a realistic behavioral scenario to
`evals/adversarial-evals.json`, including the expected preservation and routing
behavior. Include examples that should stay unchanged. Check the result in a GPT
conversation when possible and distinguish observed results from expectations.

Run `python3 evals/check.py` and `python3 tools/package_skill.py`. A clean scanner
result is not proof of good prose. Do not claim an independent writing-quality
benchmark unless you actually ran and recorded one.

Use invented examples or material you are authorized to share. Keep private drafts,
writing samples, credentials, and taught voice cards out of commits and archives.
