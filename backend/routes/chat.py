"""
routes/chat.py — REST endpoint for the Gemini-powered chatbot.

POST /api/chat
  Body: { "message": "...", "history": [...] }
  Response: { "reply": "..." }
"""

from fastapi import APIRouter, HTTPException

from backend.models import ChatRequest, ChatResponse
from backend.chatbot import ask_chatbot

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to the Auti-Aura assistant and get a reply.
    Pass the full conversation history to maintain context.
    """
    try:
        reply = await ask_chatbot(request.message, request.history)
        return ChatResponse(reply=reply)
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chatbot error: {str(e)}")
