# TEAM_SYNC_MESSAGE_TEMPLATE

## 这份文件的用途
这是一份可以直接发给队友的同步模板。你后续只需要把路径和责任人替换掉，就可以直接发群或发私聊。

## 最小同步版本
大家统一一下当前项目口径：

1. 最终正式交付不是 Web App，而是微信小程序。
2. 当前 `frontend/prototype/Chinese/` 是 H5 原型，只用于确认页面、交互和主链路。
3. 正式实现会拆成三块：小程序前端、后端 API、数据库/对象存储。
4. 小程序前端不直连数据库，也不直接对接第三方 AI，统一走后端 API。
5. 社区当前只按展示页推进，Shop 当前只按导购入口推进，不做交易闭环。

请先看这些文件：
- `docs/architecture/TECH_ARCHITECTURE.md`
- `docs/planning/PROJECT_SCOPE.md`
- `docs/ui/UI_STYLE_BASELINE.md`
- `frontend/prototype/Chinese/`

## 发给后端 / API / 数据库同学的版本
这边已经把项目口径整理成微信小程序方案了。请你们先按以下基线评估后端与数据层：

- 最终前端是微信小程序，不是 React/Vite Web。
- 前端当前给你们的是 H5 原型，用于看页面和交互，不是运行时技术栈。
- 建议后端统一为 `FastAPI + Python`。
- 正式关系库只保留一个方案，建议 `MySQL 8`，也可选 `PostgreSQL`，但不要并行两套。
- 图片、生成图、社区封面图走对象存储。

请优先确认这些问题：
1. 微信登录接口怎么定义。
2. 图片上传接口怎么定义。
3. 食材识别和生成结果是拆两个接口还是一个链路。
4. 档案馆、社区、设置页需要哪些核心字段。
5. Shop 在小程序中的跳转配置如何由后端返回。

请先看：
- `docs/architecture/TECH_ARCHITECTURE.md`
- `docs/backend/HEALTH_API_CONTRACT.md`
- `docs/backend/HEALTH_DATA_MODEL.md`
- `docs/backend/health-data-templates/`

## 发给上架 / 提审同学的版本
这边需要提前确认小程序上线相关约束，避免后面返工：

- 最终形态是微信小程序。
- 当前原型里有外跳逻辑，但小程序里不能按 H5 任意外跳处理。
- 需要尽早确认登录、域名白名单、上传下载域名、web-view 或合作方小程序跳转方案。

请先看：
- `docs/architecture/TECH_ARCHITECTURE.md`
- `docs/planning/PROJECT_SCOPE.md`
- `frontend/prototype/Chinese/`

## 你自己交付给团队时最少带上的文件
- `docs/architecture/TECH_ARCHITECTURE.md`
- `docs/planning/PROJECT_SCOPE.md`
- `docs/ui/UI_STYLE_BASELINE.md`
- `docs/architecture/TEAM_SYNC_PACKAGE.md`
- `frontend/prototype/Chinese/`
