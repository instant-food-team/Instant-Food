# Backend Workspace

本目录预留给正式后端实现。

当前协作口径：
- 小程序前端不直接调用第三方 AI 或数据库。
- 所有登录、上传、识别、生成、归档、社区读取、Shop 跳转配置都由后端 API 提供。
- 推荐采用单体 API 服务，不拆微服务。

子目录说明：
- `api/`：接口实现、服务层、路由层
- `database/`：表结构、迁移、初始化脚本、样例数据

正式实现前请先阅读：
- `../docs/architecture/TECH_ARCHITECTURE.md`
- `../docs/backend/HEALTH_API_CONTRACT.md`
- `../docs/backend/HEALTH_DATA_MODEL.md`

