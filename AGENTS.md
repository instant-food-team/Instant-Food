# AGENTS.md

## Project Rule
When working in this repository, any H5 or frontend page change must load and follow:
- `C:\Users\Yang\Desktop\拍立食\docs\h5_acceptance_standard.md`

## Mandatory Workflow
For any change involving page structure, image, copy, interaction, route, shell logic, API integration, or deployment path:
1. Read `C:\Users\Yang\Desktop\拍立食\docs\h5_acceptance_standard.md`
2. Treat the acceptance standard as required, not optional
3. Do not mark the task complete until the impacted checks are run
4. Save validation evidence under `C:\Users\Yang\Desktop\拍立食\archive\validation\<date>-<topic>`

## Entry Safety
- Do not switch the formal entry to the experimental shell unless all required acceptance items pass
- Keep the stable entry as default until the experimental version fully passes regression

## Current Formal Entry
- `C:\Users\Yang\Desktop\拍立食\frontend\index.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\vercel.json`

## Current Experimental Entry
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\完整App-总装_真实阶段直连版.html`

## Quality Bar
Do not rely on the user to manually discover regressions one by one.
You must proactively check:
- navigation
- back and close buttons
- overlays and dark bands
- image integrity and image fill
- typography consistency
- route transitions
- core interactions
