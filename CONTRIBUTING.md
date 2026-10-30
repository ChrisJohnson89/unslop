# Contributing

This fork contains Unslop for revisions and audits, and Unslop Write for lightweight
drafting in the user's style. Keep their runtime resources independent and do not
add scanner or voice-card setup to everyday drafting. See [AGENTS.md](AGENTS.md)
for the checks.

For a scanner change, add a failing example and a literal or domain-valid
protection to `evals/fixtures/contracts/scanner-examples.json` first. For a
preservation change, add a before/after case to the preservation table. Update
`exact_total` without changing existing assertions. Useful contextual pairs live
in `evals/fixtures/pairs/`.

For instruction changes, add a realistic behavioral scenario to
`evals/adversarial-evals.json`, including the expected preservation and routing
behavior. Include examples that should stay unchanged. Check the result in a GPT
conversation when possible and distinguish observed results from expectations.
Set `skill_name` to `unslop-write` for drafting cases; cases without that field
target the original Unslop skill.

Run the checks in AGENTS.md and build both packages, using
`python3 tools/package_skill.py` and `python3 tools/package_skill.py --skill unslop-write`.
A clean scanner
result is not proof of good prose. Do not claim an independent writing-quality
benchmark unless you actually ran and recorded one.

Use invented examples or material you are authorized to share. Keep private drafts,
writing samples, credentials, and taught voice cards out of commits and archives.
