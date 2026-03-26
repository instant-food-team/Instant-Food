# HANDOFF

## 当前项目状态
项目当前处于“原型收口 + 微信小程序实现前对齐 + 仓库结构整理”阶段。

当前统一口径：
- 主链路优先。
- 社区只做 UI 前端展示。
- Shop 只做第三方平台导购跳转壳。
- 最终正式交付形态是微信小程序。
- 任何执行以 `docs/` 目录下治理文档为准。

---

## 本次交接

### 日期
- 2026-03-19

### 本次完成内容
- 完成第一轮仓库整理，根目录已拆成 `frontend / backend / docs / tests / tmp`。
- 将原始 H5 原型移动到 `frontend/prototype/`。
- 将背景素材移动到 `frontend/assets/backgrounds/`。
- 将测试截图和自检图片归档到 `tests/visual/`。
- 将临时浏览器目录移动到 `tmp/browser/`。
- 将开发文档按 `architecture / planning / backend / ui / handoff / presentations / reference` 拆分。
- 修正项目技术口径，明确最终正式交付形态是微信小程序。
- 新增整体技术架构文档与团队同步清单文档。
- 新增 `docs/README.md` 作为文档总入口。
- 新增 `docs/handoff/TEAM_SYNC_MESSAGE_TEMPLATE.md` 作为对队友的直接同步模板。
- 将社区页面的物理文件名从 `商城.html` 改为 `社区.html`。

### 本次修改文件
- `frontend/prototype/Chinese/`
- `frontend/assets/backgrounds/`
- `frontend/miniprogram/`
- `backend/`
- `docs/architecture/`
- `docs/planning/`
- `docs/backend/`
- `docs/ui/`
- `docs/handoff/HANDOFF.md`
- `docs/handoff/TEAM_SYNC_MESSAGE_TEMPLATE.md`
- `docs/README.md`
- `tests/visual/`
- `tmp/browser/`

### 未完成内容
- 正式微信小程序代码还没有开始写，`frontend/miniprogram/` 目前只有目录约定。
- 后端 API 与数据库仍未实现，`backend/` 目前是占位结构。
- Shop 在小程序里的正式跳转方案还需要后续确认。

### 风险与注意事项
- 以后不要再把底部第二栏改回 `商城`。
- 以后不要再恢复文字输入、语音输入或工具输入弹层。
- 以后不要再把最终前端技术栈写成 React/Vite。
- H5 原型仅作为视觉和交互锚点，不要误当成正式运行时架构。
- 小程序中不能直接照搬 H5 的任意外跳逻辑。

### 下一位 Codex 接手前必读
- 先读 `docs/architecture/TECH_ARCHITECTURE.md`
- 再读 `docs/architecture/ARCHITECTURE_RULES.md`
- 再读 `docs/planning/PROJECT_SCOPE.md`
- 再读 `docs/planning/TASK_BOARD.md`
- 再读 `docs/ui/UI_STYLE_BASELINE.md`
- 再读 `docs/ui/UI_NEW_WINDOW_PROMPT.md`
- 再看 `frontend/prototype/Chinese/Nexus.html`
- 再看 `frontend/prototype/Chinese/拍摄.html`
- 再看 `frontend/prototype/Chinese/加载过渡.html`

---

## 交接模板

### 日期
- YYYY-MM-DD

### 本次完成内容
-

### 本次修改文件
-

### 未完成内容
-

### 风险与注意事项
-

### 下一位 Codex 接手前必读
-
