import { Routes, Route } from "react-router-dom";
import Navbar from "@/components/Navbar";
import HomePage from "@/pages/HomePage";
import ArticlesPage from "@/pages/ArticlesPage";
import ArticlePage from "@/pages/ArticlePage";
import VideosPage from "@/pages/VideosPage";
import ChatPage from "@/pages/ChatPage";

function PageWrapper({ children }: { children: React.ReactNode }) {
  return <main className="max-w-6xl mx-auto px-6 py-10">{children}</main>;
}

export default function App() {
  return (
    <div className="min-h-screen" style={{ background: "#eff6ff" }}>
      <Navbar />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route
          path="/informe"
          element={
            <PageWrapper>
              <ArticlesPage axis="informe" title="Je m'informe" subtitle="Sensibilisation" icon="" tint="" tintBg="" />
            </PageWrapper>
          }
        />
        <Route
          path="/educate"
          element={
            <PageWrapper>
              <ArticlesPage axis="educate" title="Ressources éducateurs" subtitle="Pédagogie & inclusion" icon="" tint="" tintBg="" />
            </PageWrapper>
          }
        />
        <Route path="/articles/:id" element={<PageWrapper><ArticlePage /></PageWrapper>} />
        <Route path="/videos" element={<PageWrapper><VideosPage /></PageWrapper>} />
        <Route path="/chat" element={<PageWrapper><ChatPage /></PageWrapper>} />
      </Routes>
    </div>
  );
}
