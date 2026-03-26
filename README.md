# 拍立食（Instant Food）

拍立食是一个围绕“拍照识别食物 + 健康反馈 + 轻社交表达”的课程项目仓库。当前以 H5 原型为主，后续会逐步接入 API 与小程序端。

## 当前状态
- 正式入口已切到新壳页（并已通过标准验收）
- H5 仍是当前主要交付形态
- 大文件资源通过 Git LFS 管理

## 入口与关键路径
- 正式入口：`frontend/index.html`
- 线上入口重定向：`frontend/vercel.json`
- 当前壳页：`frontend/prototype/Chinese/完整App-总装_真实阶段直连版.html`
- 验收标准：`docs/h5_acceptance_standard.md`
- 验收归档：`archive/validation/`

## 目录结构（简版）
```text
frontend/     H5 页面、素材、小程序前端目录
backend/      后端预留结构
docs/         架构、计划、UI、交接与验收标准
tests/        验证脚本与测试
archive/      历史归档与验收证据
scripts/      辅助脚本
tmp/          本地临时文件（不入库）
```

## 本地预览
建议使用本地静态服务，不要直接双击 HTML：
```powershell
cd frontend
python -m http.server 8000
```
然后访问：
- `http://localhost:8000/index.html`

## 首次拉取大文件
```powershell
git lfs install
git lfs pull
```

## 协作要求
- 任何 H5 改动都必须遵循：`docs/h5_acceptance_standard.md`
- 未通过必过项前，不能切正式入口
- 验收证据统一放在：`archive/validation/<date>-<topic>`
