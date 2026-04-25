import { Link } from "react-router-dom";
import { BookOpen, Info, Users, ArrowRight, Sparkles } from "lucide-react";

const AXIS_CARDS = [
  {
    color: "bg-blue-500",
    iconBg: "bg-blue-100",
    icon: <Info size={28} className="text-blue-600" />,
    label: "Je m'informe",
    to: "/informe",
  },
  {
    color: "bg-green-500",
    iconBg: "bg-green-100",
    icon: <Users size={28} className="text-green-600" />,
    label: "Je suis Éducateur",
    to: "/educate",
  },
  {
    color: "bg-yellow-400",
    iconBg: "bg-yellow-100",
    icon: <BookOpen size={28} className="text-yellow-600" />,
    label: "Vidéos",
    to: "/videos",
  },
];

export default function HomePage() {
  return (
    <div>
      {/* ── Hero — full width with gradient ─────────────────── */}
      <section className="hero-section text-center px-6 py-24">
        {/* Badge pill */}
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/80 border border-slate-200 text-slate-600 text-sm font-semibold mb-8 shadow-sm">
          <Sparkles size={14} className="text-yellow-500" />
          Sensibilisation &amp; Éducation
        </div>

        {/* Main heading */}
        <h1 className="text-5xl sm:text-6xl font-black text-slate-900 leading-[1.1] mb-6 max-w-3xl mx-auto">
          Comprendre l'autisme
          <br />
          pour{" "}
          <span className="text-orange-500">mieux</span>{" "}
          <span className="text-green-500">accompagner</span>
          <br />
          nos enfants
        </h1>

        {/* Subtitle */}
        <p className="text-lg text-slate-500 max-w-xl mx-auto mb-10 leading-relaxed">
          Une ressource complète pour les parents, les enseignants et toute
          personne souhaitant créer un monde plus inclusif et bienveillant pour
          les enfants autistes.
        </p>

        {/* CTA */}
        <Link
          to="/informe"
          className="inline-flex items-center gap-3 bg-slate-900 text-white font-bold text-base px-8 py-4 rounded-full transition-all hover:bg-slate-700 active:scale-[0.97] shadow-lg shadow-slate-900/20"
        >
          Choisir mon profil <ArrowRight size={18} />
        </Link>
      </section>

      {/* ── Content below hero — constrained ────────────────── */}
      <div className="max-w-6xl mx-auto px-6 pb-16 space-y-10">
        {/* Axis cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
          {AXIS_CARDS.map((c, i) => (
            <Link
              key={i}
              to={c.to}
              className="group rounded-2xl overflow-hidden shadow-sm hover:shadow-md hover:-translate-y-1 transition-all"
            >
              <div className={`${c.color} flex items-center justify-center h-28 group-hover:h-32 transition-all`}>
                <div className={`w-14 h-14 rounded-2xl ${c.iconBg} flex items-center justify-center`}>
                  {c.icon}
                </div>
              </div>
              <div className="bg-white px-5 py-4 border border-t-0 border-slate-200 rounded-b-2xl">
                <p className="font-extrabold text-slate-800 text-lg">{c.label}</p>
              </div>
            </Link>
          ))}
        </div>

        {/* Info cards */}
        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-blue-50 flex items-center justify-center">
                <Info size={20} className="text-blue-500" />
              </div>
              <h2 className="font-extrabold text-xl text-slate-800">Présentation Auti-Aura</h2>
            </div>
            <p className="text-slate-500 leading-relaxed">
              Auti'Aura est une initiative solidaire menée par l'équipe n°21 de
              SUP'COM visant à soutenir le Club des Bleus. Ce club, fondé par des
              parents membres de l'UNFT Bardo, accueille 12 enfants atteints
              d'autisme.
            </p>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-green-50 flex items-center justify-center">
                <Users size={20} className="text-green-500" />
              </div>
              <h2 className="font-extrabold text-xl text-slate-800">Le Projet PACTE</h2>
            </div>
            <p className="text-slate-500 leading-relaxed">
              Le <strong>Projet PACTE à SUP'COM</strong> est un exercice de
              pédagogie active formant les élèves ingénieurs à la gestion de
              projet et au travail d'équipe. En groupes, les étudiants mènent
              une action concrète sur le terrain en partenariat avec un
              organisme extérieur.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
