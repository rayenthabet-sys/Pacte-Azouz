"""
config.py — Loads and validates environment variables.

Usage anywhere in the backend:
    from backend.config import settings
    key = settings.groq_api_key
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    groq_api_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
