import { Routes, Route, useLocation } from "react-router-dom";
import Navbar from "@/components/Navbar";
import HomePage from "@/pages/HomePage";
import ArticlesPage from "@/pages/ArticlesPage";
import ArticlePage from "@/pages/ArticlePage";
import VideosPage from "@/pages/VideosPage";
import ChatPage from "@/pages/ChatPage";

export default function App() {
  const { pathname } = useLocation();
  const isHome = pathname === "/";

  return (
    <div className="min-h-screen" style={{ background: "#eff6ff" }}>
      <Navbar />

      <Routes>
        {/* Home: full-width layout (hero has its own internal max-width) */}
        <Route path="/" element={<HomePage />} />

        {/* All other pages: constrained container */}
        <Route
          path="/*"
          element={
            <main className="max-w-6xl mx-auto px-6 py-10">
              <Routes>
                <Route path="/informe" element={
                  <ArticlesPage axis="informe" title="Je m'informe" subtitle="Sensibilisation" icon="" tint="" tintBg="" />
                } />
                <Route path="/educate" element={
                  <ArticlesPage axis="educate" title="Ressources éducateurs" subtitle="Pédagogie & inclusion" icon="" tint="" tintBg="" />
                } />
                <Route path="/articles/:id" element={<ArticlePage />} />
                <Route path="/videos" element={<VideosPage />} />
                <Route path="/chat" element={<ChatPage />} />
              </Routes>
            </main>
          }
        />
      </Routes>
    </div>
  );
}
