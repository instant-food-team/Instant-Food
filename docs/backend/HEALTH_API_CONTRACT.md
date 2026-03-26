# HEALTH_API_CONTRACT

## 1. 目标
本文件定义结果页 `health_reference` 的前后端 contract。

当前原则：
- 健康模块只是结果页增强字段。
- 不新增独立微服务。
- 不改变主链路顺序。
- 最优先方案是把健康信息直接挂进现有生成结果响应。

## 2. 推荐接入位置
推荐直接扩展现有结果生成响应。

推荐方式：
- `POST /api/generate` 或等价生成接口完成后，返回原有结果数据。
- 在返回体中新增 `health_reference`。

不推荐首版就做：
- 独立 `health-service`
- 独立数据库服务
- 复杂异步队列

## 3. 输入依赖
`health_reference` 的计算依赖于以下输入：

```json
{
  "confirmed_ingredients": [
    {
      "canonical_name": "shrimp",
      "display_name_zh": "虾",
      "estimated_grams": 120,
      "state": "raw"
    }
  ],
  "cooking_methods": ["stir_fry"],
  "sauces_or_seasonings": ["soy_sauce"],
  "user_flags": {
    "allergy_tags": ["shellfish"],
    "dietary_blacklist": [],
    "special_population": ["pregnant"]
  }
}
```

## 4. 输出 contract
结果页推荐统一读取以下结构：

```json
{
  "health_reference": {
    "source_version": "2026-03-14-p0",
    "estimated_kcal_range": {
      "min": 420,
      "max": 560,
      "unit": "kcal",
      "confidence": "medium"
    },
    "nutrition_labels": [
      {
        "code": "HIGH_PROTEIN_MEAL",
        "label": "高蛋白",
        "severity": "info",
        "basis": "protein_g_per_recipe",
        "value": 38,
        "unit": "g"
      },
      {
        "code": "HIGH_SODIUM_PER_SERVING",
        "label": "高盐",
        "severity": "warning",
        "basis": "percent_daily_value",
        "value": 24,
        "unit": "percent"
      }
    ],
    "allergen_alerts": [
      {
        "allergen_code": "shellfish",
        "label": "含有甲壳类",
        "severity": "warning",
        "evidence_ingredients": ["虾"]
      }
    ],
    "food_safety_alerts": [
      {
        "risk_code": "SEAFOOD_COOK_THOROUGHLY",
        "label": "海鲜建议充分加热",
        "severity": "caution",
        "reason": "海鲜建议充分加热后食用。"
      }
    ],
    "population_alerts": [
      {
        "population_code": "pregnant",
        "label": "孕期谨慎食用",
        "severity": "warning",
        "reason": "孕妇不建议食用未充分加热海鲜。"
      }
    ],
    "risk_level": "caution",
    "disclaimer": "该结果为营养与食安参考，不构成医疗建议。"
  }
}
```

## 5. 字段说明
### `estimated_kcal_range`
- 输出热量区间，不输出伪精确单值。
- `min/max` 来自默认分量和烹饪方式修正。
- `confidence` 建议使用 `high / medium / low`。

### `nutrition_labels`
- 只放用户看得懂的标签。
- 推荐首版标签：
  - `高蛋白`
  - `高盐`
  - `高脂`
  - `偏高热量`
  - `轻负担`

### `allergen_alerts`
- 用 `ingredient -> allergen` 映射表生成。
- 结果页必须能展示命中的具体食材。

### `food_safety_alerts`
- 来自 `food_safety_rules`。
- 优先处理海鲜、鸡蛋、禽类、绞肉、生面糊、生奶、剩菜回热。

### `population_alerts`
- 来自 `population_risk_rules`。
- 首版只建议支持 `pregnant` 和 `immunocompromised`。

### `risk_level`
- 推荐三档：
  - `info`
  - `caution`
  - `warning`

## 6. 前端展示建议
结果页中建议拆成 4 个区域：
- `热量摘要区`
  - 展示热量区间和健康等级
- `营养标签区`
  - 展示高蛋白、高盐、高脂等标签
- `过敏原提醒区`
  - 展示命中过敏原和证据食材
- `食安提示区`
  - 展示半生熟、特定人群和高风险原料提示

前端不应显示：
- 疾病诊断语句
- “中毒组合”
- “相克指数”

## 7. 后端实现建议
后端当前不需要新服务，只需要在生成链路里增加一个内部构建步骤：

```text
confirmed_ingredients
  -> portion estimation
  -> nutrition lookup
  -> threshold evaluation
  -> allergen lookup
  -> food safety evaluation
  -> population evaluation
  -> build health_reference
```

推荐内部模块命名：
- `health_reference_builder`
- `nutrition_lookup`
- `risk_rule_evaluator`

不推荐首版拆出新服务。

## 8. 调试接口
如果后续需要单独调试，可以加一个非必须的调试接口：

`POST /api/health/evaluate`

用途：
- 仅用于开发和联调。
- 输入确认后的食材和用户标记。
- 返回 `health_reference`。

但正式产品首版仍建议把它并入生成结果接口。

## 9. 错误处理
### 可接受降级
- 找不到某个食材营养数据时，不中断整道菜生成。
- 降级输出：
  - 缺失的食材不计入精确热量
  - 返回 `confidence: low`
  - 附加 `部分食材未命中营养库，结果为估算值`

### 不可接受行为
- 没有依据却输出精确卡路里
- 没有命中具体食材却输出过敏原结论
- 没有规则来源却输出食安警告

## 10. 结论
当前最稳的 contract 方案是：
- 把 `health_reference` 作为结果页附加结构返回
- 用小而清晰的标签和提醒表达
- 保持“参考信息”定位
- 不把功能做成单独医疗系统
