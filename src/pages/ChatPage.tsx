import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import { sendChatMessage } from "@/api";
import type { ChatMessage } from "@/api";
import { Send, Bot, User } from "lucide-react";

export default function ChatPage() {
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [history, loading]);

  async function handleSend() {
    const msg = input.trim();
    if (!msg || loading) return;
    const userMsg: ChatMessage = { role: "user", content: msg };
    setHistory((h) => [...h, userMsg]);
    setInput("");
    setLoading(true);
    setError("");
    try {
      const reply = await sendChatMessage(msg, history);
      setHistory((h) => [...h, { role: "model", content: reply }]);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Une erreur est survenue.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col" style={{ height: "calc(100vh - 8rem)" }}>
      {/* Header */}
      <div className="bg-white rounded-2xl border border-slate-200/80 p-5 flex items-center gap-4 mb-4 anim-in">
        <div className="w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center text-blue-500">
          <Bot size={24} />
        </div>
        <div>
          <h1 className="font-extrabold text-lg text-slate-800">Assistant Aura</h1>
          <p className="text-sm text-slate-400">Posez vos questions en français ou en arabe</p>
        </div>
        {loading && (
          <span className="ml-auto px-3 py-1 rounded-full bg-blue-50 text-blue-500 text-xs font-semibold animate-pulse">
            Réflexion…
          </span>
        )}
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto space-y-4 pb-4">
        {history.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full gap-5 text-center px-4">
            <div className="w-20 h-20 rounded-2xl bg-blue-50 flex items-center justify-center">
              <Bot size={40} className="text-blue-400" />
            </div>
            <div>
              <p className="font-bold text-lg text-slate-800 mb-1">Comment puis-je vous aider ?</p>
              <p className="text-sm text-slate-400 max-w-md">
                Je suis spécialisé dans l'autisme chez l'enfant. Posez-moi vos questions
                sur le diagnostic, l'accompagnement ou l'éducation.
              </p>
            </div>
            <div className="flex flex-wrap gap-2 justify-center mt-2">
              {[
                "Qu'est-ce que l'autisme ?",
                "Signes précoces chez l'enfant",
                "Comment adapter ma classe ?",
              ].map((q) => (
                <button
                  key={q}
                  onClick={() => setInput(q)}
                  className="px-4 py-2.5 rounded-xl text-sm font-medium bg-white border border-slate-200 text-slate-500 hover:border-blue-300 hover:text-blue-600 transition-colors"
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {history.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"} anim-in`}>
            {msg.role === "model" && (
              <div className="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center mr-3 mt-1 shrink-0">
                <Bot size={16} className="text-blue-500" />
              </div>
            )}
            <div
              className={`max-w-[75%] rounded-2xl px-5 py-3.5 text-sm leading-relaxed ${
                msg.role === "user"
                  ? "bg-blue-600 text-white rounded-br-md"
                  : "bg-white border border-slate-200/80 text-slate-600 rounded-bl-md bubble"
              }`}
            >
              {msg.role === "user" ? msg.content : <ReactMarkdown>{msg.content}</ReactMarkdown>}
            </div>
            {msg.role === "user" && (
              <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center ml-3 mt-1 shrink-0">
                <User size={16} className="text-white" />
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="flex items-end gap-3">
            <div className="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0">
              <Bot size={16} className="text-blue-500" />
            </div>
            <div className="bg-white border border-slate-200/80 rounded-2xl rounded-bl-md px-5 py-3.5 flex gap-1.5">
              {[0, 1, 2].map((j) => (
                <div
                  key={j}
                  className="w-2 h-2 rounded-full bg-blue-400"
                  style={{ animation: `bouncy 1.4s ${j * 0.16}s infinite ease-in-out` }}
                />
              ))}
            </div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-100 rounded-xl px-4 py-3 text-sm text-red-600">
            ⚠️ {error}
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="flex gap-3 pt-3">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Votre question sur l'autisme…"
          className="flex-1 px-5 py-3.5 rounded-xl bg-white border border-slate-200 text-sm font-medium text-slate-800 placeholder-slate-400 outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-100 transition-all"
        />
        <button
          onClick={handleSend}
          disabled={loading || !input.trim()}
          className="px-5 py-3.5 rounded-xl bg-blue-600 text-white font-bold text-sm transition-all hover:bg-blue-700 active:scale-[0.97] disabled:opacity-40 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Send size={16} />
          Envoyer
        </button>
      </div>
    </div>
  );
}
