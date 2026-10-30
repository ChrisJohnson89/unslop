# Unslop cleanup

Audit or propose edits. Read the core contract; leave the source unchanged.

For “audit only,” “flag only,” “don't change anything,” or `--report`, identify
concrete defects and explain why each needs attention. Quote the smallest useful
span, distinguish definite issues from judgment calls, and include relevant
protections when a requested span is already sound. Do not infer AI authorship.

When the user wants suggestions, pair each confirmed defect with a proposed
replacement and a short reason. Make proposals in this conversation; do not
silently write them into the document. Keep unchanged context out of the proposal
unless it is needed to understand the edit.

If Python is available, phrase, structure, and silhouette scans can help find
candidates. Interpret them in context. A quiet scanner is not proof of clear
writing, and a scanner hit is not proof of a defect. When execution is unavailable,
review manually using the same contract.
