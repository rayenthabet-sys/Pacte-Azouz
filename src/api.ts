/**
 * api.ts — Types, mock data, and API client in one place.
 * Falls back to mock data (and direct Gemini) when backend is offline.
 */

/* ── Types ─────────────────────────────────────────────────────── */

export interface Article {
  id: string;
  title: string;
  title_ar: string;
  excerpt: string;
  content: string;
  content_ar: string;
  category: string;
  axis: "informe" | "educate";
}

export interface Video {
  id: string;
  title: string;
  title_ar: string;
  url: string;
  description: string;
  description_ar: string;
  category: string;
}

export interface ChatMessage {
  role: "user" | "model";
  content: string;
}

/* ── Mock articles ─────────────────────────────────────────────── */

const MOCK_ARTICLES: Article[] = [
  {
    id: "1",
    axis: "informe",
    category: "Sensibilisation",
    title: "Qu'est-ce que l'autisme ?",
    title_ar: "ما هو التوحد؟",
    excerpt: "Le trouble du spectre autistique (TSA) est un trouble neuro-développemental qui affecte la communication et le comportement.",
    content: `## Comprendre l'autisme

Le **trouble du spectre autistique** (TSA) est un trouble du développement neurologique caractérisé par des défis dans la communication sociale et des comportements ou intérêts restreints et répétitifs.

### Caractéristiques principales

- **Communication sociale** — difficultés à comprendre les indices sociaux, maintenir le contact visuel ou engager une conversation
- **Comportements répétitifs** — mouvements stéréotypés, routines rigides ou intérêts intenses
- **Sensibilités sensorielles** — hyper ou hyposensibilité aux sons, lumières, textures ou odeurs

### Quelques chiffres

Le TSA touche environ **1 enfant sur 100** dans le monde selon l'OMS. Il est diagnostiqué 4 fois plus souvent chez les garçons, bien que les filles soient probablement sous-diagnostiquées.

### Un spectre, pas une catégorie

Chaque personne autiste est unique. Certaines ont besoin d'un soutien quotidien important, d'autres vivent de façon autonome avec peu d'aménagements.`,
    content_ar: `## فهم التوحد

**اضطراب طيف التوحد** هو اضطراب في النمو العصبي يتميز بتحديات في التواصل الاجتماعي وأنماط سلوكية مقيدة ومتكررة.

### الخصائص الرئيسية

- **التواصل الاجتماعي** — صعوبات في فهم الإشارات الاجتماعية
- **السلوكيات المتكررة** — حركات نمطية وروتين صارم
- **الحساسيات الحسية** — فرط أو نقص الحساسية للمحفزات`,
  },
  {
    id: "2",
    axis: "informe",
    category: "Diagnostic",
    title: "Signes précoces : quand consulter ?",
    title_ar: "العلامات المبكرة: متى تستشير؟",
    excerpt: "Reconnaître les premiers signes de l'autisme permet une prise en charge précoce et plus efficace.",
    content: `## Repérer les signes précoces

Un diagnostic précoce est un levier majeur pour l'accompagnement. Voici les signaux d'alerte par tranche d'âge.

### Avant 12 mois

- Peu ou pas de babillage
- Absence de gestes communicatifs (pointer, faire coucou)
- Pas de réponse au prénom

### Entre 12 et 24 mois

- Pas de mots isolés à 16 mois
- Régression du langage ou des compétences sociales
- Peu d'imitation

### Après 2 ans

- Jeu solitaire et répétitif
- Difficulté avec les changements de routine
- Réactions inhabituelles aux sons ou textures

> **Important :** un seul signe ne suffit pas à poser un diagnostic. C'est l'accumulation et la persistance des signaux qui doivent alerter.`,
    content_ar: `## اكتشاف العلامات المبكرة

التشخيص المبكر هو رافعة رئيسية للمرافقة.

### قبل 12 شهراً
- قليل أو لا يوجد مناغاة
- غياب الإيماءات التواصلية
- عدم الاستجابة للاسم`,
  },
  {
    id: "3",
    axis: "informe",
    category: "Famille",
    title: "Accompagner son enfant au quotidien",
    title_ar: "مرافقة طفلك يومياً",
    excerpt: "Des stratégies pratiques pour créer un environnement bienveillant et structuré à la maison.",
    content: `## Accompagner au quotidien

### Structurer l'environnement

- Établir des routines visuelles (planning illustré)
- Annoncer les transitions à l'avance
- Aménager un espace calme de retrait

### Communiquer efficacement

- Utiliser des phrases courtes et concrètes
- Accompagner les mots de supports visuels
- Respecter le temps de traitement de l'enfant

### Favoriser l'autonomie

- Décomposer les tâches en petites étapes
- Valoriser chaque progrès, même minime
- Impliquer l'enfant dans les choix du quotidien`,
    content_ar: `## المرافقة اليومية

### هيكلة البيئة
- إنشاء روتين بصري
- الإعلان عن التحولات مسبقاً
- تهيئة مساحة هادئة للانسحاب`,
  },
  {
    id: "4",
    axis: "educate",
    category: "Pédagogie",
    title: "Adapter sa classe pour un élève autiste",
    title_ar: "تكييف الفصل لطالب مصاب بالتوحد",
    excerpt: "Stratégies concrètes pour les enseignants : aménagement de l'espace, supports visuels et gestion des transitions.",
    content: `## Pédagogie adaptée

### Aménager l'espace

- Place fixe, éloignée des sources de bruit
- Affichage épuré et structuré
- Zone de retrait accessible

### Adapter les apprentissages

- Consignes décomposées et illustrées
- Supports visuels systématiques
- Temps supplémentaire pour les évaluations

### Gérer les transitions

- Emploi du temps visuel affiché
- Signal sonore ou visuel avant chaque changement
- Objet transitionnel si nécessaire`,
    content_ar: `## التربية المكيفة

### تهيئة المساحة
- مقعد ثابت بعيد عن مصادر الضوضاء
- عرض منظم ومبسط
- منطقة انسحاب متاحة`,
  },
  {
    id: "5",
    axis: "educate",
    category: "Communication",
    title: "La Communication Alternative et Augmentative",
    title_ar: "التواصل البديل والمعزز",
    excerpt: "La CAA aide les personnes non verbales ou peu verbales à s'exprimer grâce à des outils adaptés.",
    content: `## Communication Alternative et Augmentative

La CAA regroupe tous les moyens qui complètent ou remplacent la parole.

### Outils sans technologie

- **PECS** — échange d'images pour communiquer
- **Makaton** — système de signes + pictogrammes
- **Tableaux de communication** — grilles d'images organisées par thème

### Outils numériques

- Applications sur tablette (Proloquo2Go, GoTalk)
- Synthèse vocale personnalisée
- Logiciels de pictogrammes (Araword, Pictoselector)

### Mise en place

1. Évaluation par un orthophoniste
2. Formation de l'entourage (famille + école)
3. Utilisation dans tous les contextes de vie`,
    content_ar: `## التواصل البديل والمعزز

يشمل جميع الوسائل التي تكمل أو تحل محل الكلام.

### أدوات بدون تكنولوجيا
- **PECS** — تبادل الصور للتواصل
- **ماكاتون** — نظام إشارات + رسوم توضيحية`,
  },
  {
    id: "6",
    axis: "educate",
    category: "Inclusion",
    title: "Travailler avec les familles",
    title_ar: "العمل مع العائلات",
    excerpt: "Le partenariat école-famille est la clé d'un accompagnement cohérent et efficace.",
    content: `## Partenariat école-famille

### Communication régulière

- Carnet de liaison (papier ou numérique)
- Réunions de suivi régulières
- Partage des objectifs du PPS

### Valoriser l'expertise parentale

Les parents sont les premiers experts de leur enfant. Leur vécu et leurs observations sont précieux pour adapter l'accompagnement.

### Cohérence des approches

- Utiliser les mêmes supports visuels à l'école et à la maison
- Harmoniser les stratégies comportementales
- Célébrer ensemble les progrès de l'enfant`,
    content_ar: `## الشراكة بين المدرسة والأسرة

### التواصل المنتظم
- دفتر الاتصال
- اجتماعات المتابعة المنتظمة`,
  },
];

/* ── Mock videos ───────────────────────────────────────────────── */

const MOCK_VIDEOS: Video[] = [
  {
    id: "v1",
    category: "Sensibilisation",
    title: "Mon petit frère de la lune",
    title_ar: "أخي الصغير من القمر",
    url: "https://www.youtube.com/embed/Clhk7ot1xSA",
    description: "Court-métrage d'animation primé racontant l'autisme à travers le regard d'une grande sœur.",
    description_ar: "فيلم رسوم متحركة قصير حائز على جوائز يروي التوحد من خلال عيون أخت كبرى.",
  },
  {
    id: "v2",
    category: "Éducation",
    title: "L'autisme expliqué aux enfants",
    title_ar: "شرح التوحد للأطفال",
    url: "https://www.youtube.com/embed/GmPnG_ydCnk",
    description: "Vidéo pédagogique qui explique l'autisme de façon simple et accessible pour les enfants.",
    description_ar: "فيديو تعليمي يشرح التوحد بطريقة بسيطة ومتاحة للأطفال.",
  },
  {
    id: "v3",
    category: "Témoignage",
    title: "Vivre avec l'autisme — Témoignages",
    title_ar: "العيش مع التوحد — شهادات",
    url: "https://www.youtube.com/embed/j0sWkkPOCnk",
    description: "Des familles partagent leur vécu et leurs conseils pour accompagner un enfant autiste.",
    description_ar: "عائلات تشارك تجاربها ونصائحها لمرافقة طفل مصاب بالتوحد.",
  },
  {
    id: "v4",
    category: "Formation",
    title: "Stratégies éducatives pour l'autisme",
    title_ar: "استراتيجيات تعليمية للتوحد",
    url: "https://www.youtube.com/embed/TlnEb9EnWTE",
    description: "Formation pour les enseignants sur les meilleures pratiques d'inclusion scolaire.",
    description_ar: "تدريب للمعلمين على أفضل ممارسات الإدماج المدرسي.",
  },
];

/* ── Config ────────────────────────────────────────────────────── */

const BASE_URL = import.meta.env.VITE_API_URL
  ? `${import.meta.env.VITE_API_URL}/api`
  : "/api";
const GEMINI_KEY = import.meta.env.VITE_GEMINI_API_KEY || "";
const GEMINI_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_KEY}`;

const SYSTEM_PROMPT = `Tu es "Aura", un assistant bienveillant spécialisé dans l'autisme chez les enfants.
Ton rôle :
- Répondre aux questions des parents et éducateurs sur le trouble du spectre autistique (TSA)
- Donner des conseils pratiques, validés et empathiques
- Répondre dans la langue de l'utilisateur (français ou arabe)
- Utiliser un ton chaleureux, rassurant et accessible
- Structurer tes réponses avec des titres et listes quand c'est utile
Tu ne dois JAMAIS poser de diagnostic. Oriente toujours vers un professionnel de santé pour les questions médicales.`;

/* ── API functions ─────────────────────────────────────────────── */

export async function fetchArticles(axis?: string): Promise<Article[]> {
  try {
    const url = axis ? `${BASE}/articles?axis=${axis}` : `${BASE}/articles`;
    const res = await fetch(url);
    if (!res.ok) throw new Error();
    return await res.json();
  } catch {
    return MOCK_ARTICLES.filter((a) => !axis || a.axis === axis);
  }
}

export async function fetchArticle(id: string): Promise<Article> {
  try {
    const res = await fetch(`${BASE}/articles/${id}`);
    if (!res.ok) throw new Error();
    return await res.json();
  } catch {
    const found = MOCK_ARTICLES.find((a) => a.id === id);
    if (found) return found;
    throw new Error("Article introuvable.");
  }
}

export async function fetchVideos(): Promise<Video[]> {
  try {
    const res = await fetch(`${BASE}/videos`);
    if (!res.ok) throw new Error();
    return await res.json();
  } catch {
    return MOCK_VIDEOS;
  }
}

export async function sendChatMessage(
  message: string,
  history: ChatMessage[],
): Promise<string> {
  // Try backend first
  try {
    const res = await fetch(`${BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, history }),
    });
    if (res.ok) {
      const data = await res.json();
      return data.reply as string;
    }
  } catch {
    // fall through to direct Gemini call
  }

  // Direct Gemini API
  const contents = [
    { role: "user",  parts: [{ text: SYSTEM_PROMPT }] },
    { role: "model", parts: [{ text: "Compris ! Je suis Aura, votre assistant spécialisé en autisme. Comment puis-je vous aider ?" }] },
    ...history.map((m) => ({ role: m.role === "user" ? "user" : "model", parts: [{ text: m.content }] })),
    { role: "user",  parts: [{ text: message }] },
  ];

  const res = await fetch(GEMINI_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ contents }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(
      (err as { error?: { message?: string } }).error?.message ?? "Erreur de l'assistant IA",
    );
  }

  const data = await res.json();
  return data?.candidates?.[0]?.content?.parts?.[0]?.text ?? "Je n'ai pas pu formuler une réponse. Veuillez réessayer.";
}
