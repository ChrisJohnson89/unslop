# Unslop rewrite

Read the core contract. Diagnose the source, then repair only confirmed defects.

Use the current GPT session for both passes. With execution available, run the
source through `extract_constraints.py`, `banned_phrase_scan.py`,
`structure_scan.py`, and `silhouette_scan.py` to catch candidates you missed.
Use `--genre docs` or `--genre social` only when the source fits. Quoted material
is protected by default; audit it only when requested.

For each candidate, decide whether context confirms a defect or protects the
wording. A matched phrase alone does not justify an edit. Preserve meaningful
courtesy and domain terms. Return a clean source exactly.

Make the smallest repair to affected sentences. Check facts and relations before
polishing rhythm. Use the validation workflow in the core contract. One focused
correction pass is usually enough; if a conflict cannot be resolved from the
source, flag it rather than guessing or repeatedly rewriting the whole draft.

Return the cleaned text only unless the user requested analysis.
