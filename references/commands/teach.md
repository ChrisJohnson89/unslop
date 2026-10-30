# Unslop teach

Build a prose voice card from writing samples the user provides or explicitly
identifies. Read `references/voice.md` for the card structure and evidence rules.

If there are no samples, ask for representative writing. Do not search chat
history, accounts, or folders merely because the user wants a voice card. If
searching those sources is explicitly requested, use only the authorized scope.
Separate the user's writing from assistant text, quotations, and pasted examples.

Describe demonstrated habits with short evidence spans. Label inferred habits as
provisional when the sample is thin or from another genre. Keep stated preferences
separate from observed habits. Never invent the writer's beliefs or biography.

Return a reusable card and a short demonstration using facts from the supplied
material. Ask only for missing samples that would materially improve the requested
use. Save a card only when requested and only to a named or agreed destination;
returning one in chat is not persistent installation or training.
