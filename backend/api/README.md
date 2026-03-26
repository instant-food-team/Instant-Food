# Backend API

建议放置：
- 路由定义
- 服务逻辑
- DTO / schema
- 第三方服务适配层

建议首批接口：
- `POST /api/auth/wechat/login`
- `POST /api/media/upload`
- `POST /api/ingredients/recognize`
- `POST /api/recipes/generate`
- `GET /api/archives`
- `POST /api/archives`
- `GET /api/community/feed`
- `GET /api/community/{id}`
- `GET /api/shop/{entry_id}`
- `GET /api/user/settings`
- `PUT /api/user/settings`

