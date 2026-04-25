"""
chatbot.py — Wraps Google Gemini to power the Auti-Aura assistant.

The chatbot is specialised in autism awareness for parents and educators.
It always replies in the same language the user writes in (French or Arabic).
"""

import os
from groq import Groq

from backend.config import settings
from backend.models import ChatMessage

# ── System prompt ─────────────────────────────────────────────────────────────
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

أنت المساعد الافتراضي لمنصة أوتي-أورا، المخصصة للتوعية بالتوحد عند الأطفال في تونس.
دورك هو مساعدة الآباء والمربين بمعلومات واضحة وعلمية حول طيف اضطراب التوحد.
"""

def build_history(history: list[ChatMessage]) -> list[dict]:
    """Convert our internal ChatMessage list to the format Groq expects."""
    return [
        {"role": msg.role, "content": msg.content}
        for msg in history
    ]


async def ask_chatbot(message: str, history: list[ChatMessage]) -> str:
    """
    Send a user message (with conversation history) to Groq and return the reply.
    Raises ValueError if the API key is not configured.
    """
    if not settings.groq_api_key:
        raise ValueError("GROQ_API_KEY is not set. Please add it to your .env file.")

    client = Groq(api_key=settings.groq_api_key)
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(build_history(history))
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )
    
    return chat_completion.choices[0].message.content
