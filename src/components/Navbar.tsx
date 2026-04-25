import { NavLink, Link, useLocation } from "react-router-dom";
import { useState } from "react";
import { BookOpen, Users, Play, Gamepad2, Menu, X } from "lucide-react";

const NAV_LINKS = [
  { to: "/informe", label: "Je m'informe", icon: BookOpen },
  { to: "/educate", label: "Je suis Éducateur", icon: Users },
  { to: "/videos", label: "Vidéos", icon: Play },
  { to: "/chat", label: "Assistant IA", icon: Gamepad2 },
];

export default function Navbar() {
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-blue-100">
      <div className="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
        {/* Logo — multi-color like the reference */}
        <Link to="/" className="flex items-center gap-1 font-black text-xl tracking-tight">
          <span className="text-red-500">A</span>
          <span className="text-red-500">U</span>
          <span className="text-green-500">T</span>
          <span className="text-blue-500">I</span>
          <span className="text-yellow-500">'</span>
          <span className="text-red-500">A</span>
          <span className="text-green-500">U</span>
          <span className="text-blue-500">R</span>
          <span className="text-yellow-500">A</span>
        </Link>

        {/* Desktop */}
        <ul className="hidden md:flex items-center gap-1">
          {NAV_LINKS.map((l) => {
            const active = pathname.startsWith(l.to);
            const Icon = l.icon;
            return (
              <li key={l.to}>
                <NavLink
                  to={l.to}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-semibold transition-colors ${
                    active
                      ? "text-blue-600 bg-blue-50"
                      : "text-slate-500 hover:text-blue-600 hover:bg-blue-50/50"
                  }`}
                >
                  <Icon size={16} />
                  {l.label}
                </NavLink>
              </li>
            );
          })}
        </ul>

        {/* Mobile toggle */}
        <button
          className="md:hidden w-10 h-10 flex items-center justify-center rounded-lg text-slate-500 hover:bg-blue-50"
          onClick={() => setOpen(!open)}
          aria-label="Menu"
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      {/* Mobile menu */}
      {open && (
        <div className="md:hidden px-6 pb-4 flex flex-col gap-1 bg-white border-b border-blue-100">
          {NAV_LINKS.map((l) => {
            const active = pathname.startsWith(l.to);
            const Icon = l.icon;
            return (
              <NavLink
                key={l.to}
                to={l.to}
                onClick={() => setOpen(false)}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-semibold ${
                  active ? "text-blue-600 bg-blue-50" : "text-slate-500"
                }`}
              >
                <Icon size={18} />
                {l.label}
              </NavLink>
            );
          })}
        </div>
      )}
    </nav>
  );
}
