"""
chatbot.py — Wraps Google Gemini and Groq to power the Auti-Aura assistant.

The chatbot is specialised in autism awareness for parents and educators.
It always replies in the same language the user writes in (French or Arabic).
"""

import os
import google.generativeai as genai
from groq import Groq

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

def build_history_groq(history: list[ChatMessage]) -> list[dict]:
    """Convert our internal ChatMessage list to the format Groq expects."""
    return [
        {"role": msg.role, "content": msg.content}
        for msg in history
    ]

def build_history_gemini(history: list[ChatMessage]) -> list[dict]:
    """Convert our internal ChatMessage list to the format Gemini expects."""
    return [
        {"role": "user" if msg.role == "user" else "model", "parts": [msg.content]}
        for msg in history
    ]

async def ask_chatbot(message: str, history: list[ChatMessage]) -> str:
    """
    Send a user message to Gemini (primary) or Groq (fallback).
    Raises ValueError if neither API key is configured.
    """
    gemini_key = os.environ.get("GEMINI_API_KEY")
    groq_key = os.environ.get("GROQ_API_KEY")

    if gemini_key:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel(
            'gemini-2.0-flash',
            system_instruction=SYSTEM_PROMPT
        )
        chat_history = build_history_gemini(history)
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(message)
        return response.text
        
    elif groq_key:
        client = Groq(api_key=groq_key)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(build_history_groq(history))
        messages.append({"role": "user", "content": message})

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
        
    else:
        raise ValueError("Neither GEMINI_API_KEY nor GROQ_API_KEY is found in the environment. Please add them via Railway variables or .env file.")
