# TECH_ARCHITECTURE

## 1. 文档目的
本文件用于统一《拍立食》的正式技术方向，避免团队继续把当前 H5 原型误认为最终交付形态。

统一结论：
- 当前仓库里的页面是 H5 原型。
- 最终正式产品是微信小程序。
- 你负责 UI 和前端交互。
- 其他同学负责后端、数据库、API 接入、小程序发布与提审。

## 2. 一句话架构
`微信小程序前端 -> 单体后端 API -> 关系型数据库 + 对象存储 -> 识别/生成能力`

## 3. 最终交付形态与当前资产

### 当前资产
- `frontend/prototype/Chinese/`
  - 中文 H5 原型，是视觉和交互锚点
- `frontend/prototype/English/`
  - 英文版原型/参考页
- `frontend/assets/backgrounds/`
  - 当前原型使用的背景和平台素材

### 最终交付
- 微信小程序前端
- 独立后端 API 服务
- 单一关系型数据库
- 对象存储

当前 H5 原型的职责是：
- 统一页面结构
- 固定主链路
- 固定文案和交互规则
- 给小程序前端和后端联调提供可视化基线

## 4. 推荐技术栈

### 小程序前端
- 原生微信小程序
- `WXML`
- `WXSS`
- `JavaScript`
- 工程化阶段建议启用 `TypeScript`
- 微信开发者工具

说明：
- 正式前端不再以 React/Vite/Tailwind 作为最终落地栈。
- 当前也不默认引入 Taro、uni-app、React 风格跨端框架。
- 如果团队后续决定改用跨端框架，必须全组确认后再改文档，不允许口头变更。

### 后端
- 推荐：`FastAPI + Python`
- 统一提供 REST 风格 API
- 统一处理微信登录、图片上传、识别、生成、归档、社区读取、Shop 配置

### 数据层
- 单一关系型数据库
- 推荐：`MySQL 8`
- 也可选 `PostgreSQL`
- 但团队只能选一个正式方案，不允许并行维护两套

### 文件/图片存储
- 对象存储
- 用于保存：
  - 用户拍摄图片
  - 生成结果封面
  - 社区封面图
  - 档案馆媒体资源

### 第三方能力
- 微信登录
- 图片上传
- 识别/生成模型或外部 AI API
- 第三方买菜平台跳转配置

## 5. 整体架构分层

### 客户端层
微信小程序负责：
- 页面展示
- 本地交互状态
- 表单确认
- 图片选择/拍摄
- 调用后端 API
- 展示生成结果和档案

### 服务层
后端 API 负责：
- 用微信 `code` 换取用户身份
- 接收图片和确认后的食材信息
- 调用识别/生成服务
- 存储归档记录
- 返回社区内容列表
- 返回 Shop 平台配置和跳转信息

### 数据层
数据库负责：
- 用户信息
- 档案馆记录
- 社区共享内容
- Shop 条目配置
- 设置项
- 健康参考规则与营养数据

### 存储层
对象存储负责：
- 原始拍摄图片
- 生成图
- 卡片图

## 6. 团队分工边界

### 你负责的部分
- UI 视觉基线
- 前端交互逻辑
- 页面状态流转
- H5 原型维护
- 小程序前端页面实现
- mock 数据与前端适配层

### 后端/API/数据库同学负责的部分
- API 设计与实现
- 数据库建模与迁移
- 微信登录接入
- 图片上传链路
- 识别/生成能力接入
- 归档与社区读取接口
- 对象存储

### 上架/提审同学负责的部分
- AppID
- 小程序后台配置
- 服务器域名白名单
- upload/download 合法域名
- web-view 业务域名
- 提审材料和发布流程

## 7. 页面映射

| 当前原型页面 | 小程序建议页面 | 说明 |
| --- | --- | --- |
| `frontend/prototype/Chinese/身份验证.html` | `pages/auth/index` | 微信登录/进入产品 |
| `frontend/prototype/Chinese/Nexus.html` | `pages/nexus/index` | 首页中枢 |
| `frontend/prototype/Chinese/拍摄.html` | `pages/capture/index` | 拍摄/选图入口 |
| `frontend/prototype/Chinese/分子重构台.html` | `pages/reconstruct/index` | 食材确认与偏好选择 |
| `frontend/prototype/Chinese/加载过渡.html` | `pages/generate/index` | 确认菜单态 + 生成中 |
| `frontend/prototype/Chinese/艺术的诞生.html` | `pages/result/index` | 结果页 |
| `frontend/prototype/Chinese/风味档案馆.html` | `pages/archive/index` | 档案馆 |
| `frontend/prototype/Chinese/社区.html` | `pages/community/index` | 社区展示页 |
| `frontend/prototype/Chinese/策展人设置.html` | `pages/settings/index` | 设置页 |
| `frontend/prototype/Chinese/引导页1~3.html` | `pages/onboarding/*` | 引导页 |

## 8. 建议接口清单

### 认证
- `POST /api/auth/wechat/login`
  - 输入：`wx.login` 返回的 `code`
  - 输出：用户标识、会话信息、是否首次进入

### 媒体
- `POST /api/media/upload`
  - 上传拍摄图片
  - 返回媒体 ID、访问 URL、存储键

### 识别
- `POST /api/ingredients/recognize`
  - 输入：图片或媒体 ID
  - 输出：识别出的食材列表

### 生成
- `POST /api/recipes/generate`
  - 输入：确认后的食材、技法、厨具、味觉偏好
  - 输出：生成结果、封面、步骤、可选健康参考

### 档案馆
- `GET /api/archives`
- `POST /api/archives`
- `GET /api/archives/{id}`

### 社区
- `GET /api/community/feed`
- `GET /api/community/{id}`

### Shop
- `GET /api/shop/{entry_id}`

### 用户设置
- `GET /api/user/settings`
- `PUT /api/user/settings`

## 9. 小程序特有约束

### 登录方式
- 必须走微信登录
- 前端通过 `wx.login` 获取 `code`
- 后端换取用户身份

### 本地存储
- 不再使用 `window.localStorage` 或 `sessionStorage`
- 小程序端如需临时存储，使用微信本地存储能力

### 网络调用
- 不再使用浏览器 `fetch/window.location`
- 小程序端统一使用微信网络与上传能力

### Shop 外跳限制
- 小程序不能像 H5 一样随意跳任意外链
- Shop 模块必须在以下方案里选一种正式落地：
  - 跳转到已配置业务域名的 `web-view`
  - 跳转到合作方小程序
  - 展示平台信息并给出复制/打开指引

这件事必须在上线前明确，否则当前 H5 的“任意外跳”行为无法原样落地。

### 审核与合规
- 健康参考只能做参考信息，不可写成医疗诊断
- 图片、文案、跳转方式要符合小程序审核要求

## 10. P0 实现建议
- 先把主链路跑通：登录 -> Nexus -> 拍摄 -> 确认 -> 生成 -> 结果 -> 保存归档 -> 档案馆
- 社区只做读，不做真实互动
- Shop 只做导购入口，不做交易闭环
- 前端先用 mock，后端接口稳定后再替换

## 11. 当前最重要的协作结论
- 最终技术栈已经改口径为“微信小程序前端 + 单体后端 API”。
- 当前 H5 原型仍然有用，但只是原型，不是最终代码栈。
- 给队友同步时，不要再说“最终前端是 React/Vite”。
- 给后端同学的第一优先信息不是页面长什么样，而是：
  - 页面主链路是什么
  - 接口边界是什么
  - 小程序端有哪些平台限制


