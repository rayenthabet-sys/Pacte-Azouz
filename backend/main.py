"""
main.py — Auti-Aura FastAPI application entry point.

Starts the server, registers all routes, and configures CORS so the
React frontend (running on port 3000) can talk to this API (port 8000).

Run with:
    uvicorn backend.main:app --reload --port 8000
"""

import os
from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.routes import articles, videos, chat

app = FastAPI(
    title="Auti-Aura API",
    description="Backend for the Auti-Aura autism awareness platform.",
    version="1.0.0",
)

# ── CORS ─────────────────────────────────────────────────────────────────────
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


@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "Auti-Aura API"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Favicon endpoint to prevent 404 errors."""
    return Response(status_code=204)


# ── Serve React frontend (production build) ───────────────────────────────────
DIST_DIR = Path(__file__).parent.parent / "dist"

if DIST_DIR.exists():
    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(full_path: str):
        # Try to serve the exact file requested
        file_path = DIST_DIR / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        # Fallback to index.html for client-side routing
        return FileResponse(DIST_DIR / "index.html")
else:
    @app.get("/")
    def root():
        return {"status": "ok", "note": "Frontend not built yet. Run: npm run build"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port)
