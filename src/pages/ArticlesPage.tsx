import { useEffect, useState } from "react";
import { fetchArticles } from "@/api";
import type { Article } from "@/api";
import ArticleCard from "@/components/ArticleCard";

interface Props {
  axis: "informe" | "educate";
  title: string;
  subtitle: string;
  icon: string;
  tint: string;
  tintBg: string;
}

export default function ArticlesPage({ axis, title, subtitle }: Props) {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchArticles(axis).then(setArticles).finally(() => setLoading(false));
  }, [axis]);

  return (
    <div>
      {/* Header */}
      <div className="mb-8 anim-in">
        <p className="text-xs font-bold uppercase tracking-widest text-blue-500 mb-2">{subtitle}</p>
        <h1 className="text-3xl font-extrabold text-slate-800">{title}</h1>
      </div>

      {loading ? (
        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="bg-white rounded-2xl border border-slate-200/80 p-7">
              <div className="skeleton h-9 w-9 rounded-xl mb-5" />
              <div className="skeleton h-5 w-3/4 mb-3" />
              <div className="skeleton h-4 w-full mb-2" />
              <div className="skeleton h-4 w-5/6" />
            </div>
          ))}
        </div>
      ) : (
        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {articles.map((a, i) => (
            <ArticleCard key={a.id} article={a} index={i} />
          ))}
        </div>
      )}
    </div>
  );
}
