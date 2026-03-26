# Validation Archive Guide

本目录用于保存每次 H5 验收证据，命名统一为：
- `YYYY-MM-DD-topic`

## 当前正式入口切换验收（基线）
- `2026-03-26-formal-entry-switch-acceptance/validation-summary.md`
- `2026-03-26-formal-entry-switch-acceptance/validation-result.json`
- `2026-03-26-formal-entry-switch-acceptance/overlay-states.json`

## 归档策略
- `validation-summary.md` / `validation-result.json` / `overlay-states.json`：建议入库
- 截图（`.png`）和中间调试产物（`.html` / `.mjs` / `.txt`）：默认本地归档，不强制入库

## 发布门槛
- `P0 fail: 0`
- `P1 fail: 0`
- 才允许切换正式入口
