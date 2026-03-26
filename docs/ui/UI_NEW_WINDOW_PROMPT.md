# UI_NEW_WINDOW_PROMPT

## 1. 用途
这份文档给你一个固定话术。每次你开一个新的 Codex 窗口准备做 UI 时，先把下面的话直接发过去，避免新窗口忘记项目风格、字体、颜色和交互边界。

## 2. 推荐直接复制版
```md
先不要自由发挥。你现在做的是《拍立食》的 UI 工作。

开始前先读这 6 个文件，并以它们为第一优先级：
- C:\Users\Yang\Desktop\拍立食\docs\architecture\TECH_ARCHITECTURE.md
- C:\Users\Yang\Desktop\拍立食\docs\architecture\ARCHITECTURE_RULES.md
- C:\Users\Yang\Desktop\拍立食\docs\planning\PROJECT_SCOPE.md
- C:\Users\Yang\Desktop\拍立食\docs\planning\TASK_BOARD.md
- C:\Users\Yang\Desktop\拍立食\docs\ui\UI_STYLE_BASELINE.md
- C:\Users\Yang\Desktop\拍立食\docs\handoff\HANDOFF.md

UI 风格必须严格沿用现有中文页面，不允许重新发明一套设计语言。视觉锚点先看：
- C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\Nexus.html
- C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\拍摄.html
- C:\Users\Yang\Desktop\拍立食\frontend\prototype\Chinese\加载过渡.html

固定要求：
- 主品牌色只能用 #235347
- 辅助强调色只能用 #8EB69B
- 标题用 SF Pro Display，正文用 SF Pro Text，中文回退用 PingFang SC / Microsoft YaHei
- 视觉语言必须是苹果系、深色、液态玻璃、黑曜石玻璃、移动端优先
- 卡片圆角以 28px 为主，设备壳圆角 40px，胶囊按钮 999px
- 间距按 8 / 12 / 16 / 20 / 24 / 32 体系
- 动效轻量，hover/press 只做轻微漂浮、缩放和透明度变化

当前已经锁定的交互规则：
- 底部第二栏固定是社区，不是商城
- 首页中间 + 直接进入拍摄页面
- 不允许做文字输入、语音输入或工具弹层
- 拍摄页主 CTA 固定是“确认拍摄”，点击后先进入分子重构确认页
- 分子重构确认页里的按钮不能是死的，食材和技法选择都要能点
- 分子重构确认页底部 CTA 先进入加载过渡页的确认菜单，再从确认菜单进入生成
- 首页当前不保留“最近档案”和“身份摘要”
- 食材确认、加载过渡、结果页兜底里的数量优先用“块 / 片 / 颗 / 瓣”这类口语单位

禁止项：
- 不准改成浅色主界面
- 不准换品牌色
- 不准用随机字体
- 不准做成通用电商、通用社区、通用 SaaS 风格
- 不准为了好看去重构无关页面

如果你的方案和现有页面风格或交互规则不一致，请不要直接实现，先指出冲突点，再等我确认。
```

## 3. 超短版
如果你只是想快速防跑偏，可以直接发这段：

```md
先读 docs 里的 architecture/TECH_ARCHITECTURE、architecture/ARCHITECTURE_RULES、planning/PROJECT_SCOPE、planning/TASK_BOARD、ui/UI_STYLE_BASELINE、handoff/HANDOFF，再看 frontend/prototype/Chinese/Nexus.html、拍摄.html、加载过渡.html。
严格沿用《拍立食》现有苹果系深色液态玻璃风格：主色 #235347，辅色 #8EB69B，标题 SF Pro Display，正文 SF Pro Text。
底部第二栏固定社区，+ 直达拍摄，不做文字/语音输入弹层，拍摄页主 CTA 固定“确认拍摄”并先进入分子重构确认页；确认页按钮要能点，点击“开始生成”后先进入加载过渡页的确认菜单，再进入生成。
首页不保留最近档案和身份摘要；确认页与相关兜底文案里的数量优先用块/片/颗/瓣。
如果你的方案和现有风格或交互不一致，先指出冲突，不要直接实现。
```

