<<<<<<< HEAD
"""
拍立食 - 拍立食后端配置
"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List, Optional


BASE_DIR = Path(__file__).resolve().parent
=======
"""Application settings for the Instant Food backend."""

from __future__ import annotations

from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _split_csv(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]
>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49


class Settings(BaseSettings):
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str

    gemini_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
<<<<<<< HEAD
    gemini_api_key: Optional[str] = None
    
    # AI 模型配置
=======

>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49
    ai_model: str = "gemini-2.5-flash"
    vision_model: str = "gemini-2.5-flash"
    image_model: str = "gemini-2.5-flash-image"
    max_tokens: int = 4096
    temperature: float = 0.7

    app_env: str = "development"
    log_level: str = "INFO"
    debug: bool = False

    api_prefix: str = "/api/v1"
    cors_origins_raw: str = Field(
        default="http://localhost:3000",
        alias="CORS_ORIGINS",
    )

    max_image_size_mb: int = 10
    allowed_image_types_raw: str = Field(
        default="image/jpeg,image/png,image/webp",
        alias="ALLOWED_IMAGE_TYPES",
    )

    use_supabase_storage: bool = True
    storage_bucket: str = "recipe-images"
<<<<<<< HEAD
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        enable_decoding=False,
    )

    @field_validator("debug", mode="before")
    @classmethod
    def normalize_debug(cls, value):
        """兼容非标准布尔环境值，避免外部环境变量污染导致启动失败。"""
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"release", "prod", "production"}:
                return False
            if normalized in {"debug", "dev", "development"}:
                return True
        return value

    @field_validator("cors_origins", "allowed_image_types", mode="before")
    @classmethod
    def split_comma_separated_list(cls, value):
        """兼容 .env 中的逗号分隔列表配置。"""
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value
    
=======

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

    @property
    def cors_origins(self) -> List[str]:
        return _split_csv(self.cors_origins_raw)

    @property
    def allowed_image_types(self) -> List[str]:
        return _split_csv(self.allowed_image_types_raw)

>>>>>>> 51a614dd83ddd58cde631993ed292f06df3aac49
    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"

    def has_openai(self) -> bool:
        return bool(self.openai_api_key)

    def has_anthropic(self) -> bool:
        return bool(self.anthropic_api_key)
    
    def has_gemini(self) -> bool:
        return bool(self.gemini_api_key)

    def has_gemini(self) -> bool:
        return bool(self.gemini_api_key)

    @property
    def ai_provider(self) -> str:
        if self.has_gemini():
            return "gemini"
        if self.has_openai():
            return "openai"
        if self.has_anthropic():
            return "anthropic"
        return "none"


settings = Settings()
