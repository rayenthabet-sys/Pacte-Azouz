"""
chatbot.py — Wraps Groq to power the Auti-Aura assistant.

The chatbot is specialised in autism awareness for parents and educators.
It always replies in the same language the user writes in (French or Arabic).
"""

import os
from dotenv import load_dotenv
load_dotenv()
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
- Limite tes réponses à 100 mots maximum.
- Pose des questions si nécéssaire à la fin de la réponse.

أنت المساعد الافتراضي لمنصة أوتي-أورا، المخصصة للتوعية بالتوحد عند الأطفال في تونس.
دورك هو مساعدة الآباء والمربين بمعلومات واضحة وعلمية حول طيف اضطراب التوحد.

قواعد مهمّة:
أجب دائمًا باللغة التي كُتب بها السؤال (الفرنسية أو العربية).
لا تقدّم أي تشخيص أبدًا؛ وجّه المستخدم إلى مختصّ صحي عند الحاجة.
حافظ على نبرة إيجابية، متعاطفة، وغير مُوصِمة.
إذا لم تكن تعرف الإجابة، فصرّح بذلك بوضوح.
اجعل إجاباتك لا تتجاوز 100 كلمة كحد أقصى.
اطرح أسئلة إذا لزم الأمر في نهاية الإجابة.
"""

def build_history_groq(history: list[ChatMessage]) -> list[dict]:
    """Convert our internal ChatMessage list to the format Groq expects."""
    return [
        {"role": "assistant" if msg.role == "model" else msg.role, "content": msg.content}
        for msg in history
    ]

async def ask_chatbot(message: str, history: list[ChatMessage]) -> str:
    """
    Send a user message to Groq LLM and return the reply.
    Raises ValueError if GROQ_API_KEY is not configured.
    """
    groq_key = os.environ.get("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("GROQ_API_KEY is not found in the environment. Please add it via Railway variables or .env file.")

    client = Groq(api_key=groq_key)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(build_history_groq(history))
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content
