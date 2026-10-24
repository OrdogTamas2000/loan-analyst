from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App configuration, read from environment variables (or a local .env file)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    sec_user_agent: str

    llm_provider: str = "gemini"
    # Model names live only in .env / .env.example; the LLM layer rejects an empty value.
    llm_model: str = ""
    llm_fallback_provider: str | None = None
    llm_fallback_model: str | None = None
    gemini_api_key: SecretStr | None = None
    groq_api_key: SecretStr | None = None

    api_keys: list[str] = []

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str | None = None

    web_origin: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
