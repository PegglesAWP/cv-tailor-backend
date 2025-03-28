import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Base settings
    APP_NAME: str = "CV Tailor"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-for-jwt")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # AI Provider settings
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "anthropic")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Storage settings
    STORAGE_TYPE: str = os.getenv("STORAGE_TYPE", "local")

    # Payment settings
    STRIPE_API_KEY: str = os.getenv("STRIPE_API_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    PRICE_ID_MONTHLY: str = os.getenv("PRICE_ID_MONTHLY", "")
    PRICE_ID_YEARLY: str = os.getenv("PRICE_ID_YEARLY", "")
    PRICE_ID_ONE_TIME: str = os.getenv("PRICE_ID_ONE_TIME", "")

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
