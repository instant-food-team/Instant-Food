# HEALTH_DATA_MODEL

## 1. 目标定位
本文件用于定义《拍立食》结果页“健康参考卡”的数据结构与权威数据来源。

这个模块当前的产品定位固定为：
- `健康参考`
- `营养估算`
- `过敏原提醒`
- `食安提示`
- `高风险原料/处理方式提醒`

明确不做：
- 医疗诊断
- 疾病治疗建议
- 民间“食物相克”判断
- 真实临床营养处方

原因：
- 官方权威资料能稳定支持的是营养、过敏原、食安与特定人群风险。
- “食物 A + 食物 B 同吃会中毒”的通用权威表没有可靠统一来源，不适合作为当前项目规则基础。

## 2. 最终建议的数据表
当前建议使用 `6 张核心表 + 1 张可选扩展表`：

### 核心表
1. `ingredient_nutrition_master`
2. `ingredient_portion_reference`
3. `nutrient_threshold_rules`
4. `allergen_rules`
5. `food_safety_rules`
6. `population_risk_rules`

### 可选扩展表
7. `natural_toxin_rules`

## 3. 数据来源总览
### 可直接作为官方主数据源
- USDA FoodData Central API / Downloads
  - 用途：食材营养成分、portion weight、可食部描述、FDC ID
  - 来源：
    - [API Guide](https://fdc.nal.usda.gov/api-guide)
    - [Data Documentation](https://fdc.nal.usda.gov/data-documentation/)
    - [Foundation Foods Documentation](https://fdc.nal.usda.gov/Foundation_Foods_Documentation/)
    - [Download Datasets](https://fdc.nal.usda.gov/download-datasets)

### 可直接作为官方规则来源
- FDA 过敏原：
  - [Food Allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies)
- WHO 健康饮食与糖/脂建议：
  - [Healthy diet](https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet)
- WHO 钠摄入建议：
  - [Sodium reduction](https://www.who.int/news-room/fact-sheets/detail/sodium-reduction)
- FDA Daily Value：
  - [Daily Value on the Nutrition and Supplement Facts Labels](https://www.fda.gov/food/new-nutrition-facts-label/daily-value-new-nutrition-and-supplement-facts-labels)
- FoodSafety.gov 安全烹饪温度：
  - [Cook to a Safe Minimum Internal Temperature](https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures)
- CDC 高风险人群食安：
  - [People at Increased Risk for Food Poisoning](https://www.cdc.gov/food-safety/risk-factors/index.html)
  - [Safer Food Choices for Pregnant Women](https://www.cdc.gov/food-safety/foods/pregnant-women.html)
- FDA 生面粉/生面糊风险：
  - [Handling Flour Safely: What You Need to Know](https://www.fda.gov/food/buy-store-serve-safe-food/handling-flour-safely-what-you-need-know)
- FDA / WHO 天然毒素：
  - [FDA Natural Toxins in Food](https://www.fda.gov/food/chemical-contaminants-pesticides/natural-toxins-food)
  - [WHO Natural toxins in food](https://www.who.int/news-room/fact-sheets/detail/natural-toxins-in-food)

## 4. 表结构设计
## 4.1 `ingredient_nutrition_master`
用途：
- 作为所有结果页营养估算的主表。
- 以每 `100g edible portion` 为统一口径。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 内部主键 |
| `fdc_id` | integer | 是 | USDA 直接导入 | FoodData Central 主键 |
| `canonical_name` | string | 是 | USDA + 人工归一 | 标准食材名 |
| `display_name_zh` | string | 是 | 人工整理 | 中文显示名 |
| `display_name_en` | string | 否 | USDA 直接导入 | 英文显示名 |
| `category_l1` | string | 是 | USDA + 人工归类 | 例如 `protein / vegetable / grain / dairy / sauce` |
| `category_l2` | string | 否 | 人工归类 | 例如 `shellfish / leafy_green / processed_meat` |
| `state` | string | 否 | USDA 直接导入 | 例如 `raw / cooked / dried` |
| `edible_portion_basis` | string | 是 | USDA 直接导入 | 统一记录为 edible portion |
| `kcal_per_100g` | number | 是 | USDA 直接导入 | 热量 |
| `protein_g_per_100g` | number | 否 | USDA 直接导入 | 蛋白质 |
| `fat_g_per_100g` | number | 否 | USDA 直接导入 | 总脂肪 |
| `saturated_fat_g_per_100g` | number | 否 | USDA 直接导入 | 饱和脂肪 |
| `carb_g_per_100g` | number | 否 | USDA 直接导入 | 总碳水 |
| `fiber_g_per_100g` | number | 否 | USDA 直接导入 | 膳食纤维 |
| `sugar_g_per_100g` | number | 否 | USDA 直接导入 | 总糖 |
| `sodium_mg_per_100g` | number | 否 | USDA 直接导入 | 钠 |
| `cholesterol_mg_per_100g` | number | 否 | USDA 直接导入 | 胆固醇，可选 |
| `source_dataset` | string | 是 | USDA 直接导入 | `foundation_foods / fndds / sr_legacy` |
| `source_url` | string | 否 | 项目生成 | 回溯来源 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |
| `updated_at` | datetime | 是 | 项目生成 | 更新时间 |

直接导入字段：
- `fdc_id`
- `display_name_en`
- `state`
- 大部分营养字段
- `source_dataset`

必须人工补充字段：
- `canonical_name`
- `display_name_zh`
- `category_l1`
- `category_l2`

原因：
- 你项目做结果页推理时，需要统一食材别名，例如 `鸡胸肉 / chicken breast / boneless skinless chicken breast`。

## 4.2 `ingredient_portion_reference`
用途：
- 把“识别到的食材”从抽象食材变成可估算的默认分量。
- 支撑“热量区间”而不是死板单值。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 内部主键 |
| `ingredient_id` | string | 是 | 关联 | 对应 `ingredient_nutrition_master.id` |
| `portion_label` | string | 是 | USDA 直接导入 | 例如 `1 cup / 1 fruit / 1 leg / 1 tbsp` |
| `portion_grams` | number | 是 | USDA 直接导入 | 对应克重 |
| `portion_type` | string | 是 | 人工标准化 | `cup / piece / tablespoon / teaspoon / serving / bowl` |
| `is_default` | boolean | 是 | 人工设定 | 当前项目默认估算分量 |
| `scene_hint` | string | 否 | 人工设定 | 例如 `single_plate / garnish / sauce / protein_main` |
| `confidence_level` | string | 否 | 项目生成 | `high / medium / low` |
| `source_dataset` | string | 是 | USDA 直接导入 | `foundation_foods / fndds` |
| `updated_at` | datetime | 是 | 项目生成 | 更新时间 |

直接导入字段：
- `portion_label`
- `portion_grams`
- `source_dataset`

必须人工补充字段：
- `portion_type`
- `is_default`
- `scene_hint`

原因：
- 官方数据给的是 portion 和 weight，但不会替你决定“结果页默认这道菜按多少份估算”。

## 4.3 `nutrient_threshold_rules`
用途：
- 将营养值转成用户能理解的标签与提醒。
- 用于高糖、高盐、高脂、轻负担、高蛋白等文案输出。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 主键 |
| `rule_code` | string | 是 | 项目生成 | 例如 `HIGH_SODIUM_PER_SERVING` |
| `rule_name` | string | 是 | 项目生成 | 中文规则名 |
| `nutrient_key` | string | 是 | 项目生成 | `sodium / sugar / saturated_fat / kcal` |
| `evaluation_basis` | string | 是 | 项目设定 | `per_serving / per_100g / per_recipe / percent_daily_value` |
| `operator` | string | 是 | 项目设定 | `>= / <= / between` |
| `threshold_value` | number | 是 | 官方依据 + 项目落地 | 阈值 |
| `threshold_upper_value` | number | 否 | 项目设定 | 范围上限 |
| `unit` | string | 是 | 官方依据 | `g / mg / kcal / percent` |
| `severity_level` | string | 是 | 项目设定 | `info / caution / warning` |
| `output_label` | string | 是 | 项目设定 | 例如 `高盐` |
| `output_copy` | string | 是 | 项目设定 | 给结果页展示文案 |
| `source_authority` | string | 是 | 官方依据 | `WHO / FDA` |
| `source_url` | string | 是 | 官方依据 | 来源链接 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |

建议落地规则：
- `HIGH_SODIUM_PER_SERVING`
- `HIGH_SATURATED_FAT_PER_SERVING`
- `HIGH_ADDED_SUGAR_OR_HIGH_SUGAR_ESTIMATE`
- `LIGHT_MEAL_KCAL`
- `MODERATE_MEAL_KCAL`
- `HEAVY_MEAL_KCAL`
- `HIGH_PROTEIN_MEAL`

说明：
- `added sugar` 很难从天然食材组合里精确得出，MVP 可优先使用 `total sugar` 或“如果包含高糖酱料则提升风险等级”的混合规则。
- `5% DV` 低、`20% DV` 高可以直接用 FDA 的 Daily Value 口径。

## 4.4 `allergen_rules`
用途：
- 识别食材是否命中主要过敏原。
- 给结果页输出“含有/可能含有”提示。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 主键 |
| `ingredient_id` | string | 是 | 关联 | 对应食材 |
| `allergen_code` | string | 是 | FDA 直接定义 | 例如 `milk / egg / fish / shellfish / tree_nut / peanut / wheat / soy / sesame` |
| `allergen_name_zh` | string | 是 | 人工整理 | 中文显示名 |
| `match_type` | string | 是 | 项目设定 | `direct / derived / possible` |
| `evidence_note` | string | 否 | 人工整理 | 例如“该原料属于甲壳类” |
| `severity_level` | string | 是 | 项目设定 | 通常 `warning` |
| `source_authority` | string | 是 | FDA | 官方来源 |
| `source_url` | string | 是 | FDA | 官方链接 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |

说明：
- FDA 直接给的是 `9 大主要过敏原`，不是具体到所有食材映射。
- 所以 `ingredient -> allergen` 这一步必须人工整理一层映射。

## 4.5 `food_safety_rules`
用途：
- 给出半生熟、未巴氏灭菌、生食、加热不足、室温放置等风险提示。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 主键 |
| `food_group` | string | 是 | 人工设定 | 例如 `poultry / ground_meat / egg / seafood / flour / leftovers` |
| `ingredient_id` | string | 否 | 可选关联 | 若规则细到单一食材可关联 |
| `risk_code` | string | 是 | 项目设定 | 例如 `RAW_EGG_RISK` |
| `risk_name` | string | 是 | 项目设定 | 中文风险名 |
| `trigger_condition` | string | 是 | 项目设定 | 触发条件，建议结构化表达 |
| `safe_min_temp_c` | number | 否 | FoodSafety.gov 直接采用 | 安全中心温度 |
| `safe_min_temp_f` | number | 否 | FoodSafety.gov 直接采用 | 安全中心温度 |
| `requires_pasteurized` | boolean | 否 | CDC/FDA 规则 | 是否要求巴氏灭菌 |
| `allow_raw` | boolean | 否 | 项目设定 | 是否允许生食 |
| `severity_level` | string | 是 | 项目设定 | `info / caution / warning` |
| `output_copy` | string | 是 | 项目设定 | 结果页文案 |
| `source_authority` | string | 是 | 官方依据 | `FoodSafety.gov / CDC / FDA` |
| `source_url` | string | 是 | 官方依据 | 来源链接 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |

首批高价值规则：
- 禽类必须熟透
- 绞肉必须熟透
- 鸡蛋不建议生食
- 贝类/海鲜需充分加热
- 生面粉/生面糊不可直接食用
- 剩菜回热需足够温度
- 冷藏和室温暴露时间提醒

## 4.6 `population_risk_rules`
用途：
- 给特定人群显示更严格的风险提醒。
- 和策展人设置里的“忌口/偏好/私密模式”一样，属于可个性化的风险层。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 主键 |
| `population_code` | string | 是 | CDC 直接口径 | `pregnant / age_65_plus / under_5 / immunocompromised` |
| `food_group` | string | 否 | 人工设定 | 例如 `raw_seafood / deli_meat / unpasteurized_dairy` |
| `ingredient_id` | string | 否 | 可选关联 | 如果需要细到原料 |
| `risk_code` | string | 是 | 项目设定 | 例如 `PREGNANCY_RAW_SEAFOOD` |
| `risk_name` | string | 是 | 项目设定 | 中文规则名 |
| `riskier_choice` | string | 是 | CDC 直接整理 | 风险项 |
| `safer_choice` | string | 否 | CDC 直接整理 | 更安全替代 |
| `severity_level` | string | 是 | 项目设定 | `caution / warning` |
| `output_copy` | string | 是 | 项目设定 | 结果页提示文案 |
| `source_authority` | string | 是 | CDC/FoodSafety.gov | 官方来源 |
| `source_url` | string | 是 | 官方链接 | 来源链接 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |

首批建议只做：
- `pregnant`
- `immunocompromised`

原因：
- 这两类人群的风险提示最明确，也最容易从官方资料稳定抽取。

## 4.7 `natural_toxin_rules`
用途：
- 替代“食材搭配冲突中毒”这类不稳概念。
- 用“原料自身天然毒素/处理不当风险”表达更科学。

字段建议：

| 字段 | 类型 | 必填 | 来源方式 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | 项目生成 | 主键 |
| `ingredient_or_group` | string | 是 | FDA/WHO + 人工整理 | 食材或食材组 |
| `toxin_name` | string | 是 | FDA/WHO 直接整理 | 毒素名 |
| `risk_code` | string | 是 | 项目设定 | 例如 `RAW_KIDNEY_BEAN_PHA` |
| `trigger_condition` | string | 是 | 人工整理 | 生食、未煮透、来源不明等 |
| `symptom_summary` | string | 否 | FDA/WHO 整理 | 简短症状说明 |
| `safe_handling` | string | 是 | FDA/WHO 整理 | 正确处理方式 |
| `severity_level` | string | 是 | 项目设定 | `warning` |
| `source_authority` | string | 是 | `FDA / WHO` | 官方来源 |
| `source_url` | string | 是 | 官方链接 | 来源链接 |
| `is_active` | boolean | 是 | 项目生成 | 是否启用 |

MVP 首批值得做的条目：
- `raw_or_undercooked_kidney_beans`
- `wild_mushrooms_unknown`
- `unpasteurized_dairy`
- `certain_shellfish_toxin_risk`
- `stone_fruit_pits_or_seeds_large_intake`

## 5. 哪些字段能直接用，哪些必须人工归纳
### 可以直接从官方数据抽取
- `fdc_id`
- 英文食材名
- 每 100g 营养值
- portion label
- portion grams
- FoodData Central 数据集类型
- 主要过敏原名单本身
- 安全中心温度
- 高风险人群名单

### 必须人工建立的项目层映射
- 中文食材名
- 食材别名归一
- 项目内食材分类
- 默认分量
- 结果页文案模板
- `ingredient -> allergen` 映射
- `ingredient/group -> safety rule` 映射
- `ingredient/group -> toxin rule` 映射

### 不能依赖官方直接给出，必须项目自己定义
- `健康等级`
- `轻负担 / 中等 / 偏高热量`
- `建议少量食用`
- `适合夜宵 / 不建议夜宵`
- 任何审美化文案

## 6. MVP 最小落地范围
当前最推荐的 MVP 不是 7 张表全做满，而是按下面顺序：

### P0
- `ingredient_nutrition_master`
- `ingredient_portion_reference`
- `nutrient_threshold_rules`
- `allergen_rules`

### P1
- `food_safety_rules`
- `population_risk_rules`

### P1.5
- `natural_toxin_rules`

原因：
- P0 就足够支撑结果页上的 `卡路里估算 + 过敏原提醒 + 高糖高盐高脂提示`。
- 这已经能让功能成立，而且课程答辩更容易讲。
- 后面再叠加半生熟风险和特定人群风险即可。

## 7. 结果页如何消费这些表
建议前端/后端输出结构统一为：

```json
{
  "health_reference": {
    "estimated_kcal_range": {"min": 420, "max": 560},
    "nutrition_tags": ["高蛋白", "中等热量", "钠偏高"],
    "allergen_alerts": ["含有甲壳类", "含有芝麻"],
    "food_safety_alerts": ["海鲜建议充分加热后食用"],
    "population_alerts": ["孕妇不建议食用未充分加热海鲜"],
    "risk_level": "caution",
    "disclaimer": "该结果为营养与食安参考，不构成医疗建议。"
  }
}
```

## 8. 当前实现建议
### 先不要做
- “食物相克得分”
- “中毒组合检测器”
- 疾病诊断结论
- 个性化减脂/增肌计划

### 先做
- 热量区间
- 高糖/高盐/高脂标签
- 9 大过敏原提醒
- 半生熟/未巴氏灭菌风险
- 孕妇/免疫低下人群警示

## 9. 和课程算法的挂钩方式
这套数据表能直接服务你课程里的算法解释：
- `回归`：用营养表 + 默认分量估算热量区间。
- `分类`：用阈值规则或分类模型输出 `低/中/高热量`、`低/中/高风险`。
- `KNN`：用相似食材组合找到近似营养参考菜谱。
- `聚类`：把档案馆作品聚类成 `轻负担 / 高蛋白 / 放纵型`。

当前最稳的答辩路线：
- 一个 `卡路里估算` 模块
- 一个 `健康/食安规则引擎`

不要在首版里塞太多模型。

## 10. 结论
对当前项目来说，最稳的数据结构不是“3 张表”，而是：
- `2 张官方营养基础表`
- `4 张项目规则表`
- `1 张天然毒素扩展表`

其中：
- 官方数据负责“事实”
- 项目规则负责“解释”
- 结果页负责“可读性”

这才是可实现、可答辩、可持续扩展的结构。

