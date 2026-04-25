import { useEffect, useState } from "react";
import { fetchVideos } from "@/api";
import type { Video } from "@/api";
import { Play } from "lucide-react";

export default function VideosPage() {
  const [videos, setVideos] = useState<Video[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchVideos().then(setVideos).finally(() => setLoading(false));
  }, []);

  return (
    <div>
      <div className="mb-8 anim-in">
        <p className="text-xs font-bold uppercase tracking-widest text-blue-500 mb-2">Médiathèque</p>
        <h1 className="text-3xl font-extrabold text-slate-800">Vidéos éducatives</h1>
      </div>

      {loading ? (
        <div className="grid gap-6 md:grid-cols-2">
          {[1, 2].map((i) => (
            <div key={i} className="bg-white rounded-2xl border border-slate-200/80 overflow-hidden">
              <div className="skeleton aspect-video" />
              <div className="p-6">
                <div className="skeleton h-5 w-3/4 mb-3" />
                <div className="skeleton h-4 w-full" />
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="grid gap-6 md:grid-cols-2">
          {videos.map((v, i) => (
            <div
              key={v.id}
              className="bg-white rounded-2xl border border-slate-200/80 overflow-hidden transition-all hover:shadow-lg hover:-translate-y-1 anim-in"
              style={{ animationDelay: `${i * 70}ms` }}
            >
              <div className="aspect-video bg-slate-100 relative">
                <iframe
                  src={v.url}
                  title={v.title}
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                  className="w-full h-full"
                />
              </div>
              <div className="p-6">
                <div className="flex items-center gap-2.5 mb-3">
                  <div className="w-8 h-8 rounded-lg bg-blue-50 flex items-center justify-center text-blue-500">
                    <Play size={16} />
                  </div>
                  <span className="text-xs font-bold uppercase tracking-widest text-slate-400">
                    {v.category}
                  </span>
                </div>
                <h2 className="font-bold text-lg text-slate-800 mb-2">{v.title}</h2>
                <p className="text-sm text-slate-500 leading-relaxed">{v.description}</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
