export default function CategoryBadge({ category }: { category: string }) {
  // Use distinct, darker colors for better contrast in light mode.
  const colorMap: Record<string, string> = {
    "Comprendre": "bg-blue-100 text-blue-800",
    "Sensoriel": "bg-yellow-100 text-yellow-800",
    "Dépistage": "bg-red-100 text-red-800",
    "Communication": "bg-green-100 text-green-800",
    "Famille": "bg-purple-100 text-purple-800",
    "Pédagogie": "bg-indigo-100 text-indigo-800",
    "Sensibilisation": "bg-pink-100 text-pink-800",
    "Inclusion": "bg-teal-100 text-teal-800",
    "Droits": "bg-orange-100 text-orange-800",
  };
  
  const classes = colorMap[category] || "bg-slate-200 text-slate-800";
  
  return (
    <span className={`inline-block px-3 py-1 rounded-full text-[10px] sm:text-xs font-bold uppercase tracking-wider ${classes}`}>
      {category}
    </span>
  );
}
