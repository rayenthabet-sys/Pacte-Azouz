import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import { fetchArticle } from "@/api";
import type { Article } from "@/api";
import { ArrowLeft, Globe } from "lucide-react";

export default function ArticlePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [article, setArticle] = useState<Article | null>(null);
  const [lang, setLang] = useState<"fr" | "ar">("fr");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!id) return;
    fetchArticle(id)
      .then(setArticle)
      .catch(() => setError("Article introuvable."))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading)
    return (
      <div className="max-w-3xl mx-auto">
        <div className="skeleton h-5 w-28 mb-6" />
        <div className="bg-white rounded-2xl border border-slate-200/80 p-8">
          <div className="skeleton h-6 w-3/4 mb-4" />
          <div className="skeleton h-4 w-full mb-3" />
          <div className="skeleton h-4 w-5/6 mb-3" />
          <div className="skeleton h-4 w-4/6" />
        </div>
      </div>
    );

  if (error || !article)
    return (
      <div className="text-center py-20">
        <p className="text-lg font-semibold text-red-500 mb-4">{error || "Article introuvable."}</p>
        <button onClick={() => navigate(-1)} className="text-sm font-bold text-blue-600 hover:underline">
          ← Retour
        </button>
      </div>
    );

  const isAr = lang === "ar";

  return (
    <div className="max-w-3xl mx-auto anim-in">
      {/* Top bar */}
      <div className="flex items-center justify-between mb-6">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center gap-2 text-sm font-bold text-blue-600 hover:underline"
        >
          <ArrowLeft size={16} /> Retour
        </button>
        <div className="flex items-center gap-2">
          <Globe size={16} className="text-slate-400" />
          {(["fr", "ar"] as const).map((l) => (
            <button
              key={l}
              onClick={() => setLang(l)}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-colors ${
                lang === l
                  ? "bg-blue-600 text-white"
                  : "bg-white border border-slate-200 text-slate-500 hover:bg-blue-50"
              }`}
            >
              {l === "fr" ? "FR" : "عربي"}
            </button>
          ))}
        </div>
      </div>

      {/* Article */}
      <div className="bg-white rounded-2xl border border-slate-200/80 overflow-hidden">
        <div className="px-8 py-6 border-b border-slate-100">
          <span className="inline-block px-3 py-1 rounded-full bg-blue-50 text-blue-600 text-xs font-bold uppercase tracking-wider mb-3">
            {article.category}
          </span>
          <h1 className="text-2xl font-extrabold text-slate-800 leading-snug" dir={isAr ? "rtl" : "ltr"}>
            {isAr ? article.title_ar : article.title}
          </h1>
        </div>
        <div className="px-8 py-8 prose" dir={isAr ? "rtl" : "ltr"}>
          <ReactMarkdown>{isAr ? article.content_ar : article.content}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
