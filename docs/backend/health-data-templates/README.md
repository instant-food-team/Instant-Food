# HEALTH DATA TEMPLATES

本目录用于存放结果页“健康参考卡”P0 阶段的 4 张核心表模板。

当前包含：
- `ingredient_nutrition_master.template.json`
- `ingredient_nutrition_master.template.csv`
- `ingredient_portion_reference.template.json`
- `ingredient_portion_reference.template.csv`
- `nutrient_threshold_rules.template.json`
- `nutrient_threshold_rules.template.csv`
- `allergen_rules.template.json`
- `allergen_rules.template.csv`

使用规则：
- `JSON` 模板用于定义结构和嵌套字段。
- `CSV` 模板用于后续快速填表和导入。
- 模板中的示例值仅用于演示字段含义，不应直接视为最终生产数据。
- 正式导入时，优先用 USDA / FDA / WHO / CDC / FoodSafety.gov 的权威数据覆盖示例值。

当前 P0 只先做这 4 张表：
- `ingredient_nutrition_master`
- `ingredient_portion_reference`
- `nutrient_threshold_rules`
- `allergen_rules`

P1 再补：
- `food_safety_rules`
- `population_risk_rules`

P1.5 再补：
- `natural_toxin_rules`
