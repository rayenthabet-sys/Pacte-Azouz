# Replace your existing chatbot.py with this

import os
import httpx
from backend.config import settings
from backend.models import ChatMessage

SYSTEM_PROMPT = """
Tu es l'assistant virtuel d'Auti-Aura, une plateforme dédiée à la sensibilisation
à l'autisme chez les enfants en Tunisie.

Ton rôle est d'aider les parents et les éducateurs avec des informations claires,
bienveillantes et fondées sur les données scientifiques actuelles concernant le
Trouble du Spectre de l'Autisme (TSA).

Règles importantes :
- Réponds TOUJOURS dans la langue du message reçu (français ou arabe).
- Ne pose jamais de diagnostic ; oriente vers un professionnel de santé si nécessaire.
- Reste positif, empathique et non-stigmatisant.
- Si tu ne sais pas, dis-le clairement.
- Limite tes réponses à 300 mots maximum.
"""

async def ask_chatbot(message: str, history: list[ChatMessage]) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in history:
        messages.append({"role": msg.role, "content": msg.content})
    messages.append({"role": "user", "content": message})

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.openrouter_api_key}",
                "HTTP-Referer": "https://auti-aura.up.railway.app",  # your Railway URL
                "X-Title": "Auti-Aura",
            },
            json={
                "model": "meta-llama/llama-3.3-70b-instruct:free",
                "messages": messages,
                "max_tokens": 500,
            },
        )
        data = response.json()
        return data["choices"][0]["message"]["content"]