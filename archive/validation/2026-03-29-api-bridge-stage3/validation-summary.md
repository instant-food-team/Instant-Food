# 2026-03-29 API Bridge Stage3 Validation Summary

## Scope

本次验收覆盖以下前端联调改动：

- `frontend/prototype/Chinese/拍摄.html`
- `frontend/prototype/Chinese/加载过渡.html`
- `frontend/prototype/Chinese/艺术的诞生.html`
- `frontend/prototype/Chinese/instant-food-api-bridge.js`
- `frontend/prototype/Chinese/完整App-总装_真实阶段直连版.html`
- `docs/handoff/FRONTEND_BACKEND_INTEGRATION_BRIDGE.md`

目标是确认前端已经补齐：

- 图片与食材确认到真实 API 的入口
- 统一结果对象 `generatedRecipeResult`
- 结果页真实消费
- 保存档案动作
- Stage3 与总装壳对更新后拆分页的接线

## Validation Setup

- 前端静态服务：`http://127.0.0.1:4173`
- mock API：`http://127.0.0.1:8001`
- 真实后端联调地址：`http://127.0.0.1:8000`
- 浏览器验证：Playwright，视口以 `414 x 896` / `430 x 932` 为主

## Passed Checks

### 1. 拍摄页写入图片缓存

- 拍摄页点击确认后，`sessionStorage.capturedImageDataUrl` 成功写入。
- 本次回归记录到的长度为 `76163`。
- 结果见：
  - `playwright-results.json`
  - `01-camera-upload-ready.png`

### 2. Stage3 独立页主链路可跑通

- `完整App-阶段3.html` 中，工作台 -> 加载 -> 结果 -> 保存链路在 mock API 下通过。
- 结果标题正确渲染为：`香煎鸡胸佐番茄蒜香汁`
- 保存成功后按钮文案更新为：`已保存到档案馆`
- 结果见：
  - `02b-stage3-standalone-result-frame.png`
  - `03b-stage3-standalone-saved-frame.png`
  - `playwright-results.json`

### 3. 总装入口的 Stage3 主链路可跑通

- `完整App-总装_真实阶段直连版.html#stage3` 已切到更新后的 `加载过渡.html` 与 `艺术的诞生.html`。
- 在 mock API 下，总装内 Stage3 的结果页正确渲染为：`香煎鸡胸佐番茄蒜香汁`
- 保存成功后按钮文案更新为：`已保存到档案馆`
- 结果见：
  - `04c-total-shell-stage3-saved-inner-frame.png`
  - `playwright-results.json`

### 4. 真实后端失败态已有设计化兜底

- 当浏览器无法完成对真实后端的请求时，加载页会进入设计化错误态，而不是原始异常堆栈。
- 当前错误态标题：`连接未完成`
- 当前错误态文案：`Failed to fetch`
- 结果见：
  - `05-loading-real-backend-error.png`
  - `playwright-results.json`

## Residual Risks

### 1. 真实后端浏览器联调仍未打通

- 当前浏览器侧对 `http://127.0.0.1:8000` 的联调仍表现为 `Failed to fetch`。
- 这说明前端入口已经预留，但真实后端仍有浏览器不可达问题。
- 高概率需要后端同学继续确认：
  - 实际可访问的 API Base URL
  - CORS
  - 本地服务是否对浏览器开放
  - 反向代理或 HTTPS 要求

### 2. 真实后端保存档案仍返回密钥错误

- 对 `POST /api/v1/archives` 的直接请求仍返回：
  - `{"detail":"Invalid API key"}`
- 结果见：
  - `real-backend-archive-error.txt`

### 3. 真实后端生成接口仍返回 500

- 对 `POST /api/v1/generate/recipe` 的直接请求当前仍是 `Internal Server Error`。
- 结果见：
  - `real-backend-generate-error.txt`

### 4. 拆分页 `分子重构台.html` 当前分支仍存在既有文字编码问题

- 拍摄页确认后会落到该拆分页。
- 该页面在当前分支里有既有乱码问题，不是这次 API bridge 改动引入，但如果有人直接用拆分页联调，会影响观感和判断。
- 本次主联调建议以后都以 Stage3 页或总装页为准。

## Conclusion

结论分两层：

- 前端侧“该补的联调入口”已经补上，mock API 下主链路可跑通。
- 真实后端侧仍有独立阻塞，当前不属于前端入口缺失，而属于后端可访问性 / 密钥 / 服务可用性问题。
