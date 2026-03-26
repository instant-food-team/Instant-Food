Original prompt: Implement phase 5 global unified cleanup for the complete app shell and stages 1-4, keeping visuals unchanged and fixing bridge/title/size/stability issues.

## Progress
- 2026-03-22: Verified stage1 -> stage2 bridge and stage2 -> stage3 bridge in the shell. Stage3 generation chain still needs validation.
- 2026-03-22: Verified stage3 workbench -> confirmation -> loading -> result -> save -> stage4 flow in Playwright. Updated page titles to unified `拍立食`口径 for shell, loading, camera, and onboarding pages.
- 2026-03-22: Unified shell stageConfig to real filenames (`完整App-阶段1.html` - `完整App-阶段4.html`) and confirmed stage1 -> stage2 reload works again after the filename/title cleanup.
