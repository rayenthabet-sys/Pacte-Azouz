"""
models.py — Pydantic schemas used by the API.

Every request body and response body is typed here so FastAPI can
auto-generate the OpenAPI docs at /docs.
"""

from typing import Optional
from pydantic import BaseModel


# ── Articles ─────────────────────────────────────────────────────────────────

class Article(BaseModel):
    id: str
    title: str
    title_ar: str
    excerpt: str
    content: str        # Markdown (French)
    content_ar: str     # Markdown (Arabic)
    category: str
    axis: str           # "informe" | "educate"
    image: Optional[str] = None


# ── Videos ───────────────────────────────────────────────────────────────────

class Video(BaseModel):
    id: str
    title: str
    title_ar: str
    url: str            # YouTube embed URL
    description: str
    description_ar: str
    category: str


# ── Chat ─────────────────────────────────────────────────────────────────────

class ChatMessage(BaseModel):
    role: str           # "user" | "model"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = []


class ChatResponse(BaseModel):
    reply: str
