import os
from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ===== 基础环境 =====
    ENV: str = Field(default="dev", description="dev / test / prod")
    DEBUG: bool = False

    # ===== 服务信息 =====
    PROJECT_NAME: str = "FastAPI Standard Template"
    DESCRIPTION: str = "一个符合最佳实践的 FastAPI 应用模板"
    VERSION: str = "0.1.0"

    # ===== 数据库 =====
    DATABASE_URL: str

    # ===== 安全 =====
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE", ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    @field_validator("ENV")
    @classmethod
    def validate_env(cls, v: str):
        if v not in {"dev", "test", "prod"}:
            raise ValueError("ENV 必须为 dev / test / prod 其中之一")
        return v

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, v: str, info):
        if info.data.get("ENV") == "prod" and v == "change-me":
            raise ValueError("SECRET_KEY 在生产环境中必须更改")
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
