"""
拍立食 - AI 服务客户端
<<<<<<< HEAD
仅从 ai_training_data 数据库提取食谱信息
"""
from collections import Counter
import logging
import time
from typing import Optional, Dict, Any, List

from database.supabase_client import get_supabase_admin
=======

当前分支优先支持 Gemini：
- 文本食谱生成
- 图片识别
- 成品图生成
"""
from __future__ import annotations

import base64
import json
import logging
from typing import Any, Dict, List, Optional, Tuple

import httpx

from config import settings
>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49

logger = logging.getLogger(__name__)


class AIServiceError(Exception):
    """AI 服务错误。"""


<<<<<<< HEAD
=======
class ImageRecognitionResult:
    """图片识别结果。"""

    def __init__(
        self,
        ingredients: List[Dict[str, Any]],
        cooking_method: str,
        nutrition_notes: str,
        allergen_warning: List[str],
    ) -> None:
        self.ingredients = ingredients
        self.cooking_method = cooking_method
        self.nutrition_notes = nutrition_notes
        self.allergen_warning = allergen_warning

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ingredients": self.ingredients,
            "cooking_method": self.cooking_method,
            "nutrition_notes": self.nutrition_notes,
            "allergen_warning": self.allergen_warning,
        }


>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49
class RecipeGenerationResult:
    """食谱生成结果。"""

    def __init__(
        self,
        title: str,
        title_zh: str,
        description: str,
        ingredients: List[Dict[str, Any]],
        steps: List[Dict[str, Any]],
        tips: str,
        nutrition: Dict[str, Any],
        image_prompt: str = "",
    ) -> None:
        self.title = title
        self.title_zh = title_zh
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.tips = tips
        self.nutrition = nutrition
        self.image_prompt = image_prompt

    def to_dict(self) -> Dict[str, Any]:
        payload = {
            "title": self.title,
            "title_zh": self.title_zh,
            "description": self.description,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "tips": self.tips,
            "nutrition": self.nutrition,
        }
        if self.image_prompt:
            payload["image_prompt"] = self.image_prompt
        return payload



class AIClient:
<<<<<<< HEAD
    """统一 AI 服务客户端 - 仅从 ai_training_data 数据库提取食谱"""
    
    def __init__(self):
        self._training_rows_cache: List[Dict[str, Any]] = []

    def _load_training_rows(self) -> List[Dict[str, Any]]:
        """带重试地读取 ai_training_data，并缓存最近一次成功结果。"""
        last_error: Optional[Exception] = None
        for attempt in range(3):
            try:
                supabase = get_supabase_admin()
                response = (
                    supabase.table("ai_training_data")
                    .select("input_description,expected_output,quality_score")
                    .order("quality_score", desc=True)
                    .limit(120)
                    .execute()
                )
                rows = response.data or []
                if rows:
                    self._training_rows_cache = rows
                return rows
            except Exception as exc:
                last_error = exc
                time.sleep(0.25 * (attempt + 1))

        if self._training_rows_cache:
            logger.warning(
                "Failed to load AI training examples from Supabase, using cached rows instead: %s",
                last_error,
            )
            return self._training_rows_cache

        logger.warning(f"Failed to load AI training examples: {last_error}")
        return []

    def _fetch_training_examples(self, ingredients: List[str], limit: int = 1) -> List[Dict[str, Any]]:
        """从 ai_training_data 中挑选与当前输入最相关的样本。"""
        rows = self._load_training_rows()
        if not rows:
            return []

        lowered_ingredients = [item.lower() for item in ingredients if item]
        scored = []
        for row in rows:
            input_description = (row.get("input_description") or "").lower()
            expected_output = (row.get("expected_output") or "").lower()
            score = sum(
                1 for ingredient in lowered_ingredients
                if ingredient in input_description or ingredient in expected_output
            )
            score += float(row.get("quality_score") or 0)
            scored.append((score, row))

        scored.sort(key=lambda item: item[0], reverse=True)
        matched_rows = [row for score, row in scored if score > 0][:limit]
        if matched_rows:
            return matched_rows

        return rows[:1]
=======
    """Gemini 优先的 AI 客户端。"""

    GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

    IMAGE_RECOGNITION_PROMPT = """
请分析这张食物图片，并严格输出 JSON。

输出格式：
{
  "ingredients": [
    {"name": "食材名称", "estimated_quantity": "估计用量", "confidence": 0.0}
  ],
  "cooking_method": "烹饪方式",
  "nutrition_notes": "营养特点",
  "allergen_warning": ["可能过敏原"]
}

要求：
1. 只输出 JSON，不要额外说明。
2. ingredients 至少返回 1 个项目。
3. confidence 使用 0 到 1 的数值。
""".strip()

    RECIPE_GENERATION_PROMPT_TEMPLATE = """
你是一位专业主厨，请根据给定食材生成一份适合 H5 展示的食谱，并严格输出 JSON。

输入信息：
- 食材：{ingredients_list}
- 烹饪技法：{cooking_technique}
- 风味方向：{flavor_profile}
- 辣度：{spice_level}/5
- 最大时长：{max_time} 分钟
- 可用厨具：{equipment}

输出格式：
{{
  "title": "英文或创意标题",
  "title_zh": "中文菜名",
  "description": "一句简介",
  "ingredients": [
    {{"name": "食材名称", "quantity": "数量", "unit": "单位", "notes": "备注"}}
  ],
  "steps": [
    {{
      "title": "步骤标题",
      "instruction": "步骤描述",
      "duration_minutes": 5,
      "tips": "小贴士"
    }}
  ],
  "tips": "整道菜的提示",
  "nutrition": {{
    "calories_per_serving": 520,
    "protein_g": 28,
    "fat_g": 18,
    "carbs_g": 35
  }},
  "image_prompt": "用于生成成品图的简洁描述"
}}

要求：
1. 只输出 JSON。
2. title_zh、description、ingredients、steps 必须存在。
3. 风格适合移动端结果页展示，避免过长。
""".strip()

    def __init__(self) -> None:
        self._http = httpx.Client(timeout=90.0)

        if settings.has_gemini():
            logger.info("Gemini client initialized with model: %s", settings.ai_model)
        elif settings.has_openai() or settings.has_anthropic():
            logger.warning("Only Gemini is supported on this branch. Ignoring non-Gemini provider config.")

    @property
    def is_available(self) -> bool:
        return settings.has_gemini()

    def recognize_image(self, image_data: bytes, image_type: str = "image/jpeg") -> ImageRecognitionResult:
        if not self.is_available:
            raise AIServiceError("Gemini API key not configured")

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": self.IMAGE_RECOGNITION_PROMPT},
                        {
                            "inline_data": {
                                "mime_type": image_type,
                                "data": base64.b64encode(image_data).decode("utf-8"),
                            }
                        },
                    ],
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": settings.max_tokens,
                "responseMimeType": "application/json",
            },
        }
        response_json = self._gemini_request(settings.vision_model, payload)
        text = self._extract_text(response_json)
        return self._parse_image_result(text)

    def recognize_image_from_url(self, image_url: str) -> ImageRecognitionResult:
        if not self.is_available:
            raise AIServiceError("Gemini API key not configured")

        try:
            response = self._http.get(image_url)
            response.raise_for_status()
        except httpx.HTTPError as error:
            raise AIServiceError(f"Failed to download source image: {error}") from error

        content_type = response.headers.get("content-type", "image/jpeg").split(";")[0].strip() or "image/jpeg"
        return self.recognize_image(response.content, content_type)
>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49

    def generate_recipe(
        self,
        ingredients: List[str],
        cooking_technique: str = "煎炒",
        flavor_profile: str = "家常",
        spice_level: int = 3,
        max_time: int = 30,
        equipment: Optional[List[str]] = None,
    ) -> RecipeGenerationResult:
<<<<<<< HEAD
        """
        根据食材从数据库生成食谱
        
        Args:
            ingredients: 食材列表
            cooking_technique: 烹饪技法（参考用，主要从数据库提取）
            flavor_profile: 风味档案（参考用，主要从数据库提取）
            spice_level: 辣度 1-5（参考用，主要从数据库提取）
            max_time: 最大时间（参考用，主要从数据库提取）
            equipment: 可用厨具（参考用，主要从数据库提取）
        
        Returns:
            RecipeGenerationResult: 生成的食谱
        """
        return self._build_recipe_from_training_data(
            ingredients=ingredients,
=======
        if not self.is_available:
            raise AIServiceError("Gemini API key not configured")

        equipment = equipment or ["炒锅", "砧板", "刀"]
        prompt = self.RECIPE_GENERATION_PROMPT_TEMPLATE.format(
            ingredients_list=", ".join(ingredients),
>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49
            cooking_technique=cooking_technique,
            flavor_profile=flavor_profile,
            spice_level=spice_level,
            max_time=max_time,
<<<<<<< HEAD
        )

    def _build_recipe_from_training_data(
        self,
        ingredients: List[str],
        cooking_technique: str,
        flavor_profile: str,
        spice_level: int,
        max_time: int,
    ) -> RecipeGenerationResult:
        """仅根据 ai_training_data.input_description 组织文字结果。"""
        training_examples = self._fetch_training_examples(ingredients)
        counts = Counter([item.strip() for item in ingredients if item.strip()])
        ingredient_items = []

        quantity_map = {
            "鸡蛋": "个",
            "番茄": "个",
            "西红柿": "个",
            "葱": "根",
        }

        for name, count in counts.items():
            unit = quantity_map.get(name, "份")
            ingredient_items.append(
                {
                    "name": name,
                    "quantity": str(count),
                    "unit": unit,
                    "notes": infer_training_note(name),
                }
            )

        top_example = training_examples[0] if training_examples else None
        input_description = top_example.get("input_description") if top_example else ""

        title_zh = build_fallback_title(
            list(counts.keys()),
            cooking_technique,
            top_example=top_example,
        )
        description = extract_description_from_training(input_description) or (
            f"基于训练库检索结果整理出的{flavor_profile}风味做法，主要食材为 {'、'.join(counts.keys())}。"
        )
        steps = build_fallback_steps(
            list(counts.keys()),
            cooking_technique,
            spice_level,
            input_description=input_description,
        )
        nutrition = estimate_fallback_nutrition(counts)
        tips = build_training_tips(input_description, ingredients, max_time)

        return RecipeGenerationResult(
            title=title_zh,
            title_zh=title_zh,
            description=description,
            ingredients=ingredient_items,
            steps=steps,
            tips=tips,
            nutrition=nutrition,
=======
            equipment=", ".join(equipment),
        )
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ],
            "generationConfig": {
                "temperature": settings.temperature,
                "maxOutputTokens": settings.max_tokens,
                "responseMimeType": "application/json",
            },
        }
        response_json = self._gemini_request(settings.ai_model, payload)
        text = self._extract_text(response_json)
        return self._parse_recipe_result(text)

    def generate_recipe_image(
        self,
        recipe: RecipeGenerationResult,
        cooking_technique: str = "",
        flavor_profile: str = "",
    ) -> Tuple[bytes, str, str]:
        if not self.is_available:
            raise AIServiceError("Gemini API key not configured")

        prompt = recipe.image_prompt or self._build_image_prompt(recipe, cooking_technique, flavor_profile)
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ],
            "generationConfig": {
                "temperature": 0.8,
                "responseModalities": ["TEXT", "IMAGE"],
            },
        }
        response_json = self._gemini_request(settings.image_model, payload)
        image_bytes, mime_type = self._extract_inline_image(response_json)
        return image_bytes, mime_type, prompt

    def _gemini_request(self, model: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.GEMINI_API_BASE}/{model}:generateContent"
        headers = {
            "x-goog-api-key": settings.gemini_api_key or "",
            "Content-Type": "application/json",
        }

        try:
            response = self._http.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as error:
            body = error.response.text
            logger.error("Gemini request failed: %s", body)
            raise AIServiceError(f"Gemini request failed: {body}") from error
        except httpx.HTTPError as error:
            logger.error("Gemini network error: %s", error)
            raise AIServiceError(f"Gemini network error: {error}") from error

    @staticmethod
    def _extract_text(response_json: Dict[str, Any]) -> str:
        candidates = response_json.get("candidates") or []
        if not candidates:
            raise AIServiceError("Gemini returned no candidates")

        parts = candidates[0].get("content", {}).get("parts") or []
        text_chunks = [part.get("text", "") for part in parts if part.get("text")]
        text = "\n".join(text_chunks).strip()
        if not text:
            raise AIServiceError("Gemini returned no text content")
        return text

    @staticmethod
    def _extract_inline_image(response_json: Dict[str, Any]) -> Tuple[bytes, str]:
        candidates = response_json.get("candidates") or []
        if not candidates:
            raise AIServiceError("Gemini returned no candidates")

        parts = candidates[0].get("content", {}).get("parts") or []
        for part in parts:
            blob = part.get("inlineData") or part.get("inline_data")
            if not blob:
                continue

            data = blob.get("data")
            mime_type = blob.get("mimeType") or blob.get("mime_type") or "image/png"
            if data:
                return base64.b64decode(data), mime_type

        raise AIServiceError("Gemini returned no image data")

    @staticmethod
    def _strip_json_fence(content: str) -> str:
        text = content.strip()
        if text.startswith("```json"):
            return text.split("```json", 1)[1].rsplit("```", 1)[0].strip()
        if text.startswith("```"):
            return text.split("```", 1)[1].rsplit("```", 1)[0].strip()
        return text

    def _parse_image_result(self, content: str) -> ImageRecognitionResult:
        try:
            data = json.loads(self._strip_json_fence(content))
        except json.JSONDecodeError as error:
            raise AIServiceError(f"Invalid image recognition JSON: {content}") from error

        return ImageRecognitionResult(
            ingredients=data.get("ingredients", []),
            cooking_method=data.get("cooking_method", "未知"),
            nutrition_notes=data.get("nutrition_notes", ""),
            allergen_warning=data.get("allergen_warning", []),
        )

    def _parse_recipe_result(self, content: str) -> RecipeGenerationResult:
        try:
            data = json.loads(self._strip_json_fence(content))
        except json.JSONDecodeError as error:
            raise AIServiceError(f"Invalid recipe JSON: {content}") from error

        return RecipeGenerationResult(
            title=data.get("title", ""),
            title_zh=data.get("title_zh", data.get("title", "")),
            description=data.get("description", ""),
            ingredients=data.get("ingredients", []),
            steps=data.get("steps", []),
            tips=data.get("tips", ""),
            nutrition=data.get("nutrition", {}),
            image_prompt=data.get("image_prompt", ""),
        )

    @staticmethod
    def _build_image_prompt(
        recipe: RecipeGenerationResult,
        cooking_technique: str,
        flavor_profile: str,
    ) -> str:
        title = recipe.title_zh or recipe.title or "拍立食菜品"
        ingredient_names = ", ".join(
            item.get("name", "")
            for item in recipe.ingredients
            if isinstance(item, dict) and item.get("name")
        )
        flavor_hint = flavor_profile or "电影感、食欲感、真实拍摄"
        technique_hint = cooking_technique or "精致摆盘"

        return (
            f"生成一张高质感成品菜图片：菜名是“{title}”。"
            f"主要食材包含：{ingredient_names or '用户选择食材'}。"
            f"画面要求真实可食、近景摆盘、适合 H5 首页展示，"
            f"风格为{flavor_hint}，突出{technique_hint}，避免插画感和文字。"
>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49
        )


ai_client = AIClient()


def get_ai_client() -> AIClient:
    return ai_client


def build_fallback_title(
    ingredients: List[str],
    cooking_technique: str,
    top_example: Optional[Dict[str, Any]] = None,
) -> str:
    if top_example and top_example.get("expected_output"):
        return top_example["expected_output"]
    lead = "".join(ingredients[:2]) if ingredients else "家常料理"
    return f"{lead}{cooking_technique}"


def infer_training_note(name: str) -> str:
    """从训练数据推断食材处理建议"""
    if name in {"鸡蛋", "鸭蛋", "鹌鹑蛋"}:
        return "建议打散或单独处理后再合入主菜。"
    if name in {"番茄", "西红柿"}:
        return "适合先切块，烹饪时可利用其自然出汁。"
    if name in {"葱", "姜", "蒜"}:
        return "通常用于提香，建议切小备用。"
    return "根据训练库相近做法，建议先洗净并按菜式切配。"


def extract_description_from_training(input_description: str) -> str:
    text = input_description or ""
    marker = "简介："
    if marker in text:
        tail = text.split(marker, 1)[1]
        for stop in ["步骤：", "关键词："]:
            if stop in tail:
                tail = tail.split(stop, 1)[0]
        return tail.strip(" ，。")
    return ""


def extract_steps_text_from_description(input_description: str) -> str:
    text = input_description or ""
    marker = "步骤："
    if marker in text:
        tail = text.split(marker, 1)[1]
        if "关键词：" in tail:
            tail = tail.split("关键词：", 1)[0]
        return tail.strip(" ，。")
    return ""


def build_fallback_steps(
    ingredients: List[str],
    cooking_technique: str,
    spice_level: int,
    input_description: str = "",
) -> List[Dict[str, Any]]:
    """从训练数据获取烹饪步骤"""
    generated_from_training = build_steps_from_training_description(input_description)
    if generated_from_training:
        return generated_from_training
    return [
        {
            "instruction": build_generic_flow_text(ingredients, cooking_technique, spice_level),
            "duration_minutes": 0,
            "tips": "当前流程说明基于输入食材自动整理，建议结合现场状态微调火候。"
        }
    ]


def build_steps_from_training_description(input_description: str) -> List[Dict[str, Any]]:
    """从训练数据描述中提取步骤"""
    text = (input_description or "").strip()
    if not text:
        return []

    flow_text = extract_steps_text_from_description(text)
    if not flow_text:
        return []

    return [
        {
            "instruction": flow_text,
            "duration_minutes": 0,
            "tips": "以下流程说明直接根据 ai_training_data 的 input_description 整理。"
        }
    ]


def estimate_fallback_nutrition(counts: Counter) -> Dict[str, Any]:
    """估算营养信息"""
    eggs = counts.get("鸡蛋", 0)
    tomatoes = counts.get("番茄", 0) + counts.get("西红柿", 0)
    return {
        "calories_per_serving": 120 * eggs + 25 * tomatoes,
        "protein_g": 6 * eggs,
        "fat_g": 5 * eggs,
        "carbs_g": 5 * tomatoes,
    }


def build_training_tips(input_description: str, ingredients: List[str], max_time: int) -> str:
    extracted = extract_steps_text_from_description(input_description)
    if extracted:
        return f"已根据训练库中的相关做法整理流程，建议在约 {max_time} 分钟内按顺序完成。"
    return f"当前结果主要依据输入食材 {'、'.join(ingredients)} 和训练库相关文本整理而成。"


def build_generic_flow_text(ingredients: List[str], cooking_technique: str, spice_level: int) -> str:
    joined = "、".join(ingredients) if ingredients else "当前食材"
    spice_text = "清淡" if spice_level <= 2 else "偏重口" if spice_level >= 4 else "中等"
    return (
        f"先将{joined}按菜式需要完成清洗和切配，再根据{cooking_technique}方式依次下锅处理。"
        f"烹饪过程中保持{spice_text}风味方向，按食材成熟度补充基础调味，确认口感后出锅即可。"
    )
