"""
main.py — Auti-Aura FastAPI application entry point.

Starts the server, registers all routes, and configures CORS so the
React frontend (running on port 3000) can talk to this API (port 8000).

Run with:
    uvicorn backend.main:app --reload --port 8000
"""

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import articles, videos, chat

app = FastAPI(
    title="Auti-Aura API",
    description="Backend for the Auti-Aura autism awareness platform.",
    version="1.0.0",
)

# ── CORS ─────────────────────────────────────────────────────────────────────
# Allow the Vite dev server and any localhost port.
# Replace your current CORS middleware with this:
import os

ALLOWED_ORIGINS = os.environ.get(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routes ───────────────────────────────────────────────────────────────────
app.include_router(articles.router, prefix="/api")
app.include_router(videos.router,   prefix="/api")
app.include_router(chat.router,     prefix="/api")


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Auti-Aura API"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Favicon endpoint to prevent 404 errors."""
    return Response(status_code=204)


import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port)
