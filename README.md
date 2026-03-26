# 拍立食

## 当前状态
- 当前仓库中的可运行界面资产是 H5 原型，位于 `frontend/prototype/`。
- 项目最终正式交付形态是微信小程序，不再以 React/Vite Web 应用作为最终落地目标。
- 给团队同步整体架构时，优先阅读 `docs/architecture/TECH_ARCHITECTURE.md`。

## 主要交付
- 当前对外转交的总交互 H5 是 `frontend/prototype/Chinese/完整App-总装.html`。
- 拆分页仍然保留在 `frontend/prototype/Chinese/`，用于查细节，不作为唯一交付物。

## 目录说明
- `frontend/`
  - `prototype/`：当前 H5 原型页面，作为视觉和交互锚点
  - `assets/`：前端页面直接引用的背景素材
  - `miniprogram/`：后续正式小程序前端代码目录
- `backend/`
  - `api/`：后端接口实现目录
  - `database/`：数据库脚本、表结构、迁移目录
- `docs/`
  - `architecture/`：技术架构、协作基线、交付清单
  - `planning/`：项目范围、任务板
  - `backend/`：后端接口与数据模型文档
  - `ui/`：UI 风格基线和 UI 协作提示词
  - `handoff/`：项目交接文档
  - `presentations/`：汇报/PPT 相关材料
  - `reference/`：课程和参考资料
- `tests/`
  - `visual/`：页面自检图、人工验收截图
- `tmp/`
  - `browser/`：当前开发过程产生的临时浏览器目录
- `archive/`
  - 历史归档资料，不作为正式开发目录

## 团队同步优先阅读
- `docs/architecture/TECH_ARCHITECTURE.md`
- `docs/README.md`
- `docs/architecture/TEAM_SYNC_PACKAGE.md`
- `docs/planning/PROJECT_SCOPE.md`
- `docs/ui/UI_STYLE_BASELINE.md`
- `frontend/prototype/Chinese/`
