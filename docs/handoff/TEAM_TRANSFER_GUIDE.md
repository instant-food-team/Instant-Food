# 拍立食转交清单

这份清单用于你把资料上传到 Google Drive 后，组员按目录直接取用。

## 先给哪一份
- 如果只能给一份交互 H5，优先给 `frontend/prototype/Chinese/完整App-总装.html`。
- 拆分页保留在 `frontend/prototype/Chinese/`，用于查细节，不是必须逐个转交。

## 建议的 Drive 目录
1. `01_Governance`
2. `02_Main_H5`
3. `03_Reference_Pages`
4. `04_Assets`
5. `05_Backend_and_Data`
6. `06_Presentation`
7. `07_Archive_Optional`

## 三位同学各自拿什么

### 同学 1: Xcode / iOS 海外版
目标:
- 基于当前 UI/UX 复刻一版 iOS App
- 做成海外版，替换不适合海外的操作风格、买菜跳转和文案
- 以现有原型为蓝本，重新适配成 App 交互

需要拿的文件:
- `02_Main_H5/完整App-总装.html`
- `01_Governance/PROJECT_SCOPE.md`
- `01_Governance/ARCHITECTURE_RULES.md`
- `01_Governance/UI_STYLE_BASELINE.md`
- `03_Reference_Pages/` 里的关键页面
- `04_Assets/` 里的背景图和结果页素材

重点看什么:
- 页面顺序和主链路
- 底部导航结构
- 液态玻璃视觉基线
- 社区卡片到第三方平台的跳转逻辑
- 拍摄、确认、加载、结果页的状态切换

本地完整路径:
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\完整App-总装.html`
- `C:\Users\Yang\Desktop\拍立食\docs\planning\PROJECT_SCOPE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\ARCHITECTURE_RULES.md`
- `C:\Users\Yang\Desktop\拍立食\docs\ui\UI_STYLE_BASELINE.md`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\Nexus.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\拍摄.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\加载过渡.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\艺术的诞生.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\assets\backgrounds\`

### 同学 2: API 接入 / 识图 / 文本生成 / 小程序适配
目标:
- 接入 Nano Banana 识图 API
- 识别拍照食材，生成确认菜单
- 生成符合要求的结果图
- 接入 DeepSeek 或同类文本 API，给菜起名、生成说明
- 加规则限制，不符合要求的菜要拦截
- 把当前交互接到微信小程序代码里

需要拿的文件:
- `01_Governance/PROJECT_SCOPE.md`
- `01_Governance/ARCHITECTURE_RULES.md`
- `01_Governance/TASK_BOARD.md`
- `02_Main_H5/完整App-总装.html`
- `03_Reference_Pages/拍摄.html`
- `03_Reference_Pages/分子重构台.html`
- `03_Reference_Pages/加载过渡.html`
- `03_Reference_Pages/艺术的诞生.html`
- `05_Backend_and_Data/HEALTH_API_CONTRACT.md`
- `05_Backend_and_Data/HEALTH_DATA_MODEL.md`
- `05_Backend_and_Data/health-data-templates/`

重点看什么:
- 拍摄 -> 确认食材 -> 确认菜单 -> 加载过渡 -> 结果页 的顺序
- 哪些字段需要 AI 生成，哪些字段需要前端传入
- 哪些图片和文案要由 API 决定
- 哪些食材或菜品需要被禁止
- 微信小程序和 H5 的写法差异

本地完整路径:
- `C:\Users\Yang\Desktop\拍立食\docs\planning\PROJECT_SCOPE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\ARCHITECTURE_RULES.md`
- `C:\Users\Yang\Desktop\拍立食\docs\planning\TASK_BOARD.md`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\完整App-总装.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\拍摄.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\分子重构台.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\加载过渡.html`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\艺术的诞生.html`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_API_CONTRACT.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_DATA_MODEL.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\health-data-templates\`

### 同学 3: 后端 / Supabase / 数据库
目标:
- 建后端数据结构
- 用 Supabase 存储用户、菜品、社区、归档、健康规则
- 为前端和小程序提供统一 API
- 让 AI 生成结果能被保存和查询

需要拿的文件:
- `01_Governance/PROJECT_SCOPE.md`
- `01_Governance/ARCHITECTURE_RULES.md`
- `01_Governance/TASK_BOARD.md`
- `01_Governance/TECH_ARCHITECTURE.md`
- `05_Backend_and_Data/HEALTH_API_CONTRACT.md`
- `05_Backend_and_Data/HEALTH_DATA_MODEL.md`
- `05_Backend_and_Data/health-data-templates/`
- `06_Presentation/HEALTH_MODULE_PPT_BRIEF.md`，如果需要顺手理解健康模块汇报口径

重点看什么:
- 数据表怎么分
- 哪些字段是核心表，哪些是扩展表
- Supabase RLS 怎么做
- 图片存储放哪里
- 前端和小程序怎样通过 API 读写数据

本地完整路径:
- `C:\Users\Yang\Desktop\拍立食\docs\planning\PROJECT_SCOPE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\ARCHITECTURE_RULES.md`
- `C:\Users\Yang\Desktop\拍立食\docs\planning\TASK_BOARD.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\TECH_ARCHITECTURE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_API_CONTRACT.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_DATA_MODEL.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\health-data-templates\`
- `C:\Users\Yang\Desktop\拍立食\docs\presentations\HEALTH_MODULE_PPT_BRIEF.md`

### 同学 4: PPT / 演示视频 / 汇报表达
目标:
- 根据项目流程做 PPT
- 做 3 到 4 分钟演示视频
- 讲清楚项目目标、流程、算法、健康模块和最终交付价值
- 把 UI、AI、数据库、微信小程序、海外 App 这些内容统一成一条可讲清的故事线

需要拿的文件:
- `01_Governance/PROJECT_SCOPE.md`
- `01_Governance/TASK_BOARD.md`
- `01_Governance/ARCHITECTURE_RULES.md`
- `01_Governance/TECH_ARCHITECTURE.md`
- `05_Backend_and_Data/HEALTH_DATA_MODEL.md`
- `05_Backend_and_Data/HEALTH_API_CONTRACT.md`
- `05_Backend_and_Data/health-data-templates/`
- `06_Presentation/HEALTH_MODULE_PPT_BRIEF.md`
- `06_Presentation/HEALTH_MODULE_PPT_BRIEF.docx`
- `02_Main_H5/完整App-总装.html`

重点看什么:
- 这个小程序到底解决什么问题
- 主流程为什么这样设计
- 识图、生成、确认菜单、健康参考、归档分别在讲什么
- 课程要求里提到的算法如何落到项目里
- UI 设计为什么统一成液态玻璃苹果风
- 社区、Shop、健康模块和结果页怎样串成完整故事

可直接参考的讲述材料:
- `06_Presentation/HEALTH_MODULE_PPT_BRIEF.md`
- `06_Presentation/HEALTH_MODULE_PPT_BRIEF.docx`
- `01_Governance/PROJECT_SCOPE.md`
- `01_Governance/TASK_BOARD.md`
- `01_Governance/TECH_ARCHITECTURE.md`
- `05_Backend_and_Data/HEALTH_API_CONTRACT.md`

本地完整路径:
- `C:\Users\Yang\Desktop\拍立食\docs\planning\PROJECT_SCOPE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\planning\TASK_BOARD.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\ARCHITECTURE_RULES.md`
- `C:\Users\Yang\Desktop\拍立食\docs\architecture\TECH_ARCHITECTURE.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_DATA_MODEL.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\HEALTH_API_CONTRACT.md`
- `C:\Users\Yang\Desktop\拍立食\docs\backend\health-data-templates\`
- `C:\Users\Yang\Desktop\拍立食\docs\presentations\HEALTH_MODULE_PPT_BRIEF.md`
- `C:\Users\Yang\Desktop\拍立食\docs\presentations\HEALTH_MODULE_PPT_BRIEF.docx`
- `C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\完整App-总装.html`

## 转交表
| Drive 目录 | 需要上传的文件 | 仓库位置 | 给谁用 | 作用 |
| --- | --- | --- | --- | --- |
| `01_Governance` | `TECH_ARCHITECTURE.md`, `PROJECT_SCOPE.md`, `ARCHITECTURE_RULES.md`, `TASK_BOARD.md`, `UI_STYLE_BASELINE.md`, `UI_NEW_WINDOW_PROMPT.md`, `HANDOFF.md`, `TEAM_TRANSFER_GUIDE.md` | `docs/planning/`, `docs/architecture/`, `docs/ui/`, `docs/handoff/` | 全组 | 统一项目边界、风格和交接口径 |
| `02_Main_H5` | `完整App-总装.html` | `frontend/prototype/Chinese/` | 前端、iOS、API、后端 | 当前唯一最重要的总交互 H5 |
| `03_Reference_Pages` | `Nexus.html`, `拍摄.html`, `分子重构台.html`, `加载过渡.html`, `艺术的诞生.html`, `社区.html`, `风味档案馆.html`, `策展人设置.html`, `身份验证.html`, `引导页1.html`, `引导页2.html`, `引导页3.html`, `onboarding-shared.css`, `onboarding-shared.js`, `wechat-unified.css` | `frontend/prototype/Chinese/` | 需要查细节的人 | 备用参考页，用来核对局部交互 |
| `04_Assets` | `backgrounds/` 里的底图、`art-step-*.svg` | `frontend/assets/backgrounds/`, `frontend/prototype/Chinese/` | 前端、设计 | 页面底图和结果页素材 |
| `05_Backend_and_Data` | `HEALTH_DATA_MODEL.md`, `HEALTH_API_CONTRACT.md`, `HEALTH_MODULE_PPT_BRIEF.md`, `health-data-templates/` | `docs/backend/`, `docs/presentations/` | API、Supabase、AI 同学 | 数据结构、接口契约、健康模块材料 |
| `06_Presentation` | `HEALTH_MODULE_PPT_BRIEF.docx`, `HEALTH_MODULE_PPT_BRIEF.md` | `docs/presentations/` | 汇报同学 | 直接做 PPT 和视频脚本的底稿 |
| `07_Archive_Optional` | 只在需要回溯历史时上传 | `archive/` | 仅备查 | 临时 profile、旧自检图、历史脚本，不是正式交付 |

## 组员查找规则
- 先看 `01_Governance`，再看 `02_Main_H5`。
- iOS 同学先看 `02_Main_H5`，需要细节时再查 `03_Reference_Pages`。
- API 和小程序同学先看 `05_Backend_and_Data`，再对照 `03_Reference_Pages`。
- 后端和 Supabase 同学先看 `05_Backend_and_Data`，再看 `01_Governance`。
- 做 PPT / 视频的人直接看 `06_Presentation`，再回到 `01_Governance` 补流程边界。

## 不建议转交
- `tmp/`
- `tests/visual/`
- `archive/` 里的历史调试文件，除非对方明确要查旧版本

## 当前项目命名
- 对外统一名称：`拍立食`
- 当前仓库内部路径仍保留旧目录名，不影响交付和开发
