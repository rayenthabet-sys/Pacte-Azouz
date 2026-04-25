"""
routes/articles.py — REST endpoints for articles.

GET /api/articles              → all articles
GET /api/articles?axis=informe → filtered by axis
GET /api/articles/{id}         → single article
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from backend.models import Article
from backend.data.articles import ALL_ARTICLES

router = APIRouter(tags=["Articles"])


@router.get("/articles", response_model=list[Article])
def get_articles(axis: Optional[str] = Query(None, description="Filter by axis: 'informe' or 'educate'")):
    """Return all articles, optionally filtered by axis."""
    if axis:
        return [a for a in ALL_ARTICLES if a.axis == axis]
    return ALL_ARTICLES


@router.get("/articles/{article_id}", response_model=Article)
def get_article(article_id: str):
    """Return a single article by its ID."""
    for article in ALL_ARTICLES:
        if article.id == article_id:
            return article
    raise HTTPException(status_code=404, detail=f"Article '{article_id}' not found.")
