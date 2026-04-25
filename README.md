# Auti-Aura

> Une plateforme de sensibilisation à l'autisme chez les enfants.
> Articles éducatifs bilingues (FR/AR), vidéos et assistant IA (Gemini).

---

## Project structure

```
auti-aura/
├── backend/                  ← FastAPI Python backend
│   ├── main.py               ← App entry point (CORS, route registration)
│   ├── chatbot.py            ← Gemini AI assistant logic
│   ├── config.py             ← Environment settings (API key)
│   ├── models.py             ← Pydantic schemas (Article, Video, Chat)
│   ├── routes/
│   │   ├── articles.py       ← GET /api/articles, GET /api/articles/{id}
│   │   ├── videos.py         ← GET /api/videos
│   │   └── chat.py           ← POST /api/chat
│   └── data/
│       ├── articles.py       ← All article content (replaces update_*.ts)
│       └── videos.py         ← All video content
│
├── frontend/                 ← React + TypeScript + Vite frontend
│   ├── index.html
│   ├── vite.config.ts        ← Proxies /api → localhost:8000 in dev
│   ├── package.json
│   └── src/
│       ├── main.tsx          ← React entry point
│       ├── App.tsx           ← Router setup
│       ├── api.ts            ← All fetch() calls to the backend
│       ├── types.ts          ← TypeScript interfaces
│       ├── index.css
│       ├── components/
│       │   ├── Navbar.tsx
│       │   └── ArticleCard.tsx
│       └── pages/
│           ├── HomePage.tsx
│           ├── InformePage.tsx   ← Awareness articles
│           ├── EducatePage.tsx   ← Educator articles
│           ├── ArticlePage.tsx   ← Single article (FR/AR toggle)
│           ├── VideosPage.tsx
│           └── ChatPage.tsx      ← AI chatbot
│
├── scripts/
│   └── seed_articles.py      ← Export content to JSON (replaces update_*.ts)
│
├── requirements.txt          ← Python dependencies
├── .env.example              ← Copy to .env and fill in your API key
└── README.md
```

---

## Quick start

### 1 — Prerequisites

- Python 3.11+
- Node.js 20+

### 2 — Environment

```bash
cp .env.example .env
# Edit .env and set your GEMINI_API_KEY
```

### 3 — Backend (FastAPI)

```bash
# Install Python deps
pip install -r requirements.txt

# Start the API server (port 8000)
uvicorn backend.main:app --reload --port 8000
```

The interactive API docs are available at **http://localhost:8000/docs**.

### 4 — Frontend (React)

```bash
cd frontend
npm install
npm run dev        # starts on http://localhost:3000
```

Vite automatically proxies `/api/*` to the FastAPI backend, so no CORS issues
in development.

---

## API endpoints

| Method | Path                       | Description                       |
|--------|----------------------------|-----------------------------------|
| GET    | `/api/articles`            | All articles                      |
| GET    | `/api/articles?axis=informe` | Filtered by axis                |
| GET    | `/api/articles/{id}`       | Single article                    |
| GET    | `/api/videos`              | All videos                        |
| GET    | `/api/videos/{id}`         | Single video                      |
| POST   | `/api/chat`                | Send a message to the AI assistant |

---

## Adding content

All content lives in plain Python files — no database required:

- **Articles** → edit `backend/data/articles.py`
- **Videos** → edit `backend/data/videos.py`

To export content as JSON (e.g. for a static build):

```bash
python scripts/seed_articles.py --out public_data.json
```
