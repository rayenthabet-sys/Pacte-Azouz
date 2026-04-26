export default function CategoryBadge({ category, isAr }: { category: string, isAr?: boolean }) {
  // Use distinct, darker colors for strong contrast in both light and dark modes.
  const colorMap: Record<string, string> = {
    "Comprendre": "bg-blue-100 text-blue-900",
    "Sensoriel": "bg-yellow-100 text-yellow-900",
    "Dépistage": "bg-red-100 text-red-900",
    "Diagnostic": "bg-red-100 text-red-900",
    "Communication": "bg-green-100 text-green-900",
    "Famille": "bg-purple-100 text-purple-900",
    "Pédagogie": "bg-indigo-100 text-indigo-900",
    "Sensibilisation": "bg-pink-100 text-pink-900",
    "Inclusion": "bg-teal-100 text-teal-900",
    "Droits": "bg-orange-100 text-orange-900",
    "Histoire": "bg-amber-100 text-amber-900",
    "Talents": "bg-lime-100 text-lime-900",
    "Environnement": "bg-emerald-100 text-emerald-900",
    "Autonomie": "bg-cyan-100 text-cyan-900",
    "Apprentissage": "bg-sky-100 text-sky-900",
    "Émotions": "bg-rose-100 text-rose-900",
    "Partenariat": "bg-fuchsia-100 text-fuchsia-900",
    "Observation": "bg-violet-100 text-violet-900",
    "Projet éducatif": "bg-indigo-100 text-indigo-900",
    "Scénarios sociaux": "bg-blue-100 text-blue-900",
    "Relaxation": "bg-teal-100 text-teal-900",
  };

  const arMap: Record<string, string> = {
    "Comprendre": "الفهم",
    "Sensoriel": "حسي",
    "Dépistage": "التشخيص",
    "Diagnostic": "التشخيص",
    "Communication": "التواصل",
    "Famille": "الأسرة",
    "Pédagogie": "بيداغوجيا",
    "Sensibilisation": "توعية",
    "Inclusion": "إدماج",
    "Droits": "حقوق",
    "Histoire": "تاريخ",
    "Talents": "مواهب",
    "Environnement": "بيئة",
    "Autonomie": "استقلالية",
    "Apprentissage": "تعلم",
    "Émotions": "مشاعر",
    "Partenariat": "شراكة",
    "Observation": "ملاحظة",
    "Projet éducatif": "مشروع تربوي",
    "Scénarios sociaux": "سيناريوهات اجتماعية",
    "Relaxation": "استرخاء",
  };
  
  const classes = colorMap[category] || "bg-slate-200 text-slate-900";
  const displayCat = isAr && arMap[category] ? arMap[category] : category;
  
  return (
    <span
      className={`inline-block px-3 py-1 rounded-full text-[10px] sm:text-xs font-black uppercase tracking-wider ${classes}`}
      style={{ fontWeight: 800 }}
    >
      {displayCat}
    </span>
  );
}
