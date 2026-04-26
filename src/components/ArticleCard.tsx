import { Link } from "react-router-dom";
import { BookOpen, ArrowRight } from "lucide-react";
import type { Article } from "@/api";
import CategoryBadge from "@/components/CategoryBadge";

export default function ArticleCard({
  article,
  index = 0,
  isAr = false,
}: {
  article: Article;
  index?: number;
  isAr?: boolean;
}) {
  return (
    <Link
      to={`/articles/${article.id}`}
      className="group block bg-white rounded-2xl border border-slate-200/80 p-7 transition-all hover:shadow-lg hover:shadow-blue-100/50 hover:-translate-y-1 anim-in"
      style={{ animationDelay: `${index * 60}ms` }}
    >
      {/* Category */}
      <div className="flex items-center gap-2.5 mb-5">
        <div className="w-9 h-9 rounded-xl bg-blue-50 flex items-center justify-center text-blue-500">
          <BookOpen size={18} />
        </div>
        <CategoryBadge category={article.category} isAr={isAr} />
      </div>

      {/* Title */}
      <h2 className="font-extrabold text-lg text-slate-800 leading-snug mb-3 group-hover:text-blue-600 transition-colors">
        {isAr && article.title_ar ? article.title_ar : article.title}
      </h2>

      {/* Excerpt */}
      <p className="text-sm text-slate-500 leading-relaxed line-clamp-3 mb-6">
        {article.excerpt}
      </p>

      {/* Link */}
      <div className="flex items-center gap-2 text-sm font-bold text-blue-600">
        {isAr ? "اقرأ المقال" : "Lire l'article"}
        <ArrowRight size={16} className="transition-transform group-hover:translate-x-1" />
      </div>
    </Link>
  );
}
