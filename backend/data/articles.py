"""
data/articles.py — All article content for Auti-Aura.

Two axes:
  • "informe"  — awareness articles ("Le saviez-vous ?") for the general public
  • "educate"  — educator-focused articles with practical tips

Each article is bilingual (French + Arabic).
"""

from backend.models import Article

# ── Awareness articles (axis: informe) ──────────────────────────────────────

INFORME_ARTICLES: list[Article] = [
    Article(
        id="i1",
        axis="informe",
        category="Comprendre",
        title="Le saviez-vous ? L'autisme, une différence de traitement de l'information",
        title_ar="هل كنت تعلم؟ التوحد، اختلاف في معالجة المعلومات",
        excerpt="L'autisme n'est pas une maladie mentale mais un fonctionnement neurologique différent.",
        content="""L'autisme n'est pas une maladie mentale mais un fonctionnement neurologique différent.
Présentation des « lunettes » à travers lesquelles l'enfant voit le monde (détails vs globalité).

### Vrai / Faux
**L'autisme est une maladie mentale ?**
**Faux.** C'est un trouble neurodéveloppemental.""",
        content_ar="""التوحد ليس مرضاً نفسياً، بل هو اختلاف في طريقة معالجة المعلومات في الدماغ.
يرى المصاب بالتوحد العالم من خلال عدسة تركز على التفاصيل الدقيقة أكثر من المعنى الإجمالي.

### صحيح أم خطأ؟
**التوحد هو مرض نفسي؟**
**خطأ.** التوحد هو اضطراب نمائي عصبي يختلف فيه عمل الدماغ.""",
    ),
    Article(
        id="i2",
        axis="informe",
        category="Histoire",
        title="Le saviez-vous ? Histoire et Évolution du concept",
        title_ar="هل كنت تعلم؟ تطور مفهوم التوحد",
        excerpt="Passer du terme maladie au Trouble du Spectre de l'Autisme (TSA).",
        content="""Passer du terme « maladie » au « Trouble du Spectre de l'Autisme » (TSA).
La notion de « spectre » : il n'y a pas un autisme, mais des autismes, chaque personne étant unique.

### Vrai / Faux
**Il n'y a qu'un seul type d'autisme ?**
**Faux.** L'autisme est un spectre, ce qui signifie qu'il y a une grande diversité de profils.""",
        content_ar="""تطور مفهوم التوحد من "مرض" إلى "طيف اضطراب التوحد".
كلمة "طيف" تعني أنه لا يوجد نوع واحد من التوحد، بل حالات متنوعة تختلف من شخص لآخر.

### صحيح أم خطأ؟
**يوجد نوع واحد فقط من التوحد؟**
**خطأ.** التوحد عبارة عن طيف، مما يعني وجود تنوع كبير في الحالات والقدرات.""",
    ),
    Article(
        id="i3",
        axis="informe",
        category="Talents",
        title="Le saviez-vous ? Les forces et talents souvent ignorés",
        title_ar="هل كنت تعلم؟ نقاط القوة والمواهب",
        excerpt="Mettre en avant la mémoire exceptionnelle, la capacité de concentration...",
        content="""Mettre en avant la mémoire exceptionnelle, la capacité de concentration sur des sujets
précis et l'honnêteté sociale qui caractérisent souvent les personnes autistes.

### Vrai / Faux
**Les personnes autistes n'ont pas de capacités particulières ?**
**Faux.** Beaucoup ont des intérêts spécifiques qui développent des talents remarquables.""",
        content_ar="""غالباً ما يتمتع الأشخاص ذوو التوحد بنقاط قوة مذهلة، مثل الذاكرة القوية،
والقدرة العالية على التركيز في مواضيع محددة، والصدق في التعامل الاجتماعي.

### صحيح أم خطأ؟
**الأشخاص ذوو التوحد ليس لديهم قدرات خاصة؟**
**خطأ.** كثير منهم يمتلكون مواهب استثنائية كقوة الذاكرة أو الدقة المتناهية.""",
    ),
    Article(
        id="i4",
        axis="informe",
        category="Dépistage",
        title="Les signes qui doivent alerter (Dépistage précoce)",
        title_ar="علامات الإنذار للتشخيص المبكر",
        excerpt="Le diagnostic est clinique. Les signes précoces à observer.",
        content="""Le diagnostic est clinique. Les signes incluent le retard de l'utilisation du pointage
du doigt (vers 18 mois), l'absence de réponse au prénom, ou le retard de langage (écholalie).

### Vrai / Faux
**Chaque enfant autiste présente les mêmes signes dès la naissance ?**
**Faux.** Les signes deviennent généralement plus visibles autour de 18 mois à 2 ans et varient considérablement.""",
        content_ar="""يتم التشخيص سريرياً. من العلامات المبكرة تأخر اكتساب الإشارة بالأصبع (حوالي 18 شهراً)،
عدم الاستجابة عند المناداة بالاسم، أو تأخر النطق.

### صحيح أم خطأ؟
**كل الأطفال ذوي التوحد تظهر عليهم نفس العلامات منذ الولادة؟**
**خطأ.** تبدأ العلامات بالظهور بين 18 شهراً وسنتين وتختلف من طفل لآخر.""",
    ),
    Article(
        id="i5",
        axis="informe",
        category="Sensoriel",
        title="L'hypersensibilité sensorielle expliquée",
        title_ar="فرط الحساسية الحسية",
        excerpt="De nombreuses personnes autistes ont des réactions intenses aux stimuli.",
        content="""De nombreuses personnes autistes ont des réactions intenses aux stimuli : peur des bruits
d'appareils ménagers, fascination pour la lumière, ou gêne face à certaines textures de vêtements.

### Vrai / Faux
**Un enfant qui se bouche les oreilles fait un caprice ?**
**Faux.** C'est souvent une réaction à une surcharge sensorielle — un bruit normal peut être douloureux pour lui.""",
        content_ar="""يبدي العديد من الأشخاص ذوي التوحد ردود فعل مبالغ فيها تجاه المحفزات الحسية.

### صحيح أم خطأ؟
**عندما يغطي الطفل أذنيه، فهو يتدلل؟**
**خطأ.** هذا غالباً رد فعل على عبء حسي زائد.""",
    ),
    Article(
        id="i6",
        axis="informe",
        category="Droits",
        title="Le droit à l'éducation : Un cadre mondial",
        title_ar="الحق في التعليم: إطار عالمي",
        excerpt="L'éducation est un droit garanti par la Déclaration universelle.",
        content="""L'éducation est un droit garanti par la Déclaration universelle des droits de l'homme
(Art. 26) et la Convention de l'UNESCO. Chaque enfant, quel que soit son handicap, doit avoir accès
à une école inclusive.

### Vrai / Faux
**Un enfant autiste ne peut pas aller dans une école classique ?**
**Faux.** Avec un accompagnement adapté, l'inclusion est tout à fait possible et très bénéfique.""",
        content_ar="""التعليم حق تضمنه الإعلان العالمي لحقوق الإنسان (المادة 26).
يجب أن يتمتع كل طفل بالحق في تعليم دامج.

### صحيح أم خطأ؟
**لا يمكن للطفل التوحدي الذهاب إلى مدرسة عادية؟**
**خطأ.** مع الدعم المناسب، الإدماج في المدارس العادية ممكن جداً ومفيد.""",
    ),
]

# ── Educator articles (axis: educate) ────────────────────────────────────────

EDUCATE_ARTICLES: list[Article] = [
    Article(
        id="5",
        axis="educate",
        category="Droits",
        title="Le droit à l'éducation en Tunisie",
        title_ar="الحق في التعليم في تونس",
        excerpt="Cadre légal tunisien et international pour l'éducation inclusive.",
        content="""Le droit à l'éducation est garanti par la Constitution tunisienne (Art. 44, 2022)
et la mégislation internationale. L'enseignement est obligatoire jusqu'à 16 ans.

### Conseils pratiques
- **Connaître les droits :** Familiarisez-vous avec les textes de loi pour mieux orienter les familles.
- **Adapter la classe :** Demandez les aménagements nécessaires à l'administration.""",
        content_ar="""تضمن الدولة الحق في التعليم العمومي المجاني بكامل مراحله، والتعليم إلزامي إلى سن السادسة عشرة (الفصل 44 من دستور 2022).

### نصائح عملية
- **معرفة حقوق الطفل:** تأكد من إلمامك بالتشريعات المدرسية.
- **تكييف القسم:** اطلب التجهيزات اللازمة من الإدارة.""",
    ),
    Article(
        id="6",
        axis="educate",
        category="Comprendre",
        title="Comprendre le TSA : Les 3 grandes théories",
        title_ar="فهم طيف التوحد: النظريات الثلاث الكبرى",
        excerpt="Intelligence émotionnelle, cohérence centrale et fonctions exécutives.",
        content="""Pour comprendre l'enfant, on s'appuie sur trois théories :
la théorie de l'intelligence émotionnelle, la cohérence centrale et les fonctions exécutives du cerveau.

### Conseils pratiques
- **Évitez les jugements hâtifs :** Les comportements ne sont pas de l'entêtement.
- **Utilisez des supports visuels :** Tableaux visuels pour organiser les tâches quotidiennes.""",
        content_ar="""لفهم الطفل، نعتمد على ثلاث نظريات: نظرية الذكاء الوجداني، نظرية التناسق المركزي للتفكير، والوظائف التنفيذية للمخ.

### نصائح عملية
- **تجنب الحكم المتسرع:** تذكر أن التصرفات ليست عناداً.
- **استخدام وسائل بصرية:** الجداول البصرية لتنظيم المهام اليومية.""",
    ),
    Article(
        id="7",
        axis="educate",
        category="Dépistage",
        title="Les premiers signes et le processus de diagnostic",
        title_ar="العلامات الأولى وعملية التشخيص",
        excerpt="Le retard du pointage, l'absence de réponse au prénom, et l'écholalie.",
        content="""Le retard du pointage (après 18 mois) est un signe clé. Le diagnostic est établi
par une équipe spécialisée via observation clinique.

### Conseils pratiques
- **Observation fine :** Documentez objectivement le comportement de l'enfant.
- **Orientation douce :** Guidez les parents vers un pédiatre sans poser vous-même un diagnostic.""",
        content_ar="""يمثل تأخر اكتساب الإشارة بالإصبع عن عمر السنة أحد الأعراض الفارقة.

### نصائح عملية
- **الملاحظة الدقيقة:** راقب تفاعل الطفل وسجل ملاحظاتك.
- **التوجيه اللطيف:** وجه الأولياء بلطف للتحدث مع طبيب الأطفال.""",
    ),
    Article(
        id="8",
        axis="educate",
        category="Environnement",
        title="Structurer l'espace et le temps",
        title_ar="هيكلة الفضاء والوقت",
        excerpt="Un environnement structuré réduit l'anxiété et favorise l'apprentissage.",
        content="""Structurer l'espace en zones d'activités claires et instaurer un planning visuel
quotidien réduit considérablement l'anxiété de l'enfant.

### Conseils pratiques
- **Délimiter les espaces :** Chaque coin = une activité (lecture, jeu, détente).
- **Planning visuel :** Afficher le programme du jour avec des images.""",
        content_ar="""هيكلة محيط الطفل يضمن له الاستقرار النفسي. يجب وضع روتين يومي مرئي لتقليص القلق.

### نصائح عملية
- **تحديد المساحات:** اجعل كل ركن في القسم مقترناً بنشاط واحد.
- **الروتين البصري:** ضع جدولاً يومياً مرئياً.""",
    ),
    Article(
        id="9",
        axis="educate",
        category="Autonomie",
        title="Développer l'autonomie : La technique du chaînage arrière",
        title_ar="تنمية الاستقلالية: تقنية التسلسل الخلفي",
        excerpt="Aider l'enfant pas à pas pour qu'il réussisse la dernière étape seul.",
        content="""La technique du « chaînage arrière » consiste à aider l'enfant pour toutes les étapes
sauf la dernière, afin qu'il vive le succès. On ajoute progressivement des étapes.

### Conseils pratiques
- **Découper les tâches :** Une tâche complexe = plusieurs petites étapes simples.
- **Renforcement positif :** Célébrez chaque petite réussite immédiatement.""",
        content_ar="""يمكن استخدام تقنية "التسلسل الخلفي": ساعد الطفل في كل خطوة باستثناء الأخيرة.

### نصائح عملية
- **تجزئة المهام:** قسم المهمة الصعبة إلى خطوات صغيرة.
- **التعزيز الإيجابي المباشر:** شجع الطفل واحتفل بنجاحه في الخطوة الأخيرة.""",
    ),
    Article(
        id="10",
        axis="educate",
        category="Communication",
        title="Favoriser la communication non-verbale",
        title_ar="تشجيع التواصل غير اللفظي",
        excerpt="La communication ne se réduit pas à la parole.",
        content="""Si l'enfant ne parle pas encore, commencez par des jeux de bouche, accompagnez
chaque mot d'un geste. Le jeu est le moteur principal.

### Conseils pratiques
- **Exploiter les intérêts :** Utilisez les jouets préférés comme pont vers la communication.
- **L'attente active :** Donnez 5 à 10 secondes à l'enfant pour traiter l'information.""",
        content_ar="""التواصل لا يقتصر على النطق. إذا كان الطفل لم ينطق بعد، ارفق كل كلمة بالإيماءات أو الصور.

### نصائح عملية
- **استغلال الاهتمامات:** استخدم ألعاب الطفل المفضلة كجسر.
- **الانتظار النشط:** أعط الطفل 5 إلى 10 ثوان للرد قبل تكرار السؤال.""",
    ),
    Article(
        id="11",
        axis="educate",
        category="Apprentissage",
        title="Apprentissage de la lecture, écriture et calcul",
        title_ar="تعلم القراءة والكتابة والحساب",
        excerpt="Des méthodes concrètes et sensorielles adaptées au profil TSA.",
        content="""L'apprentissage de la lecture commence par l'amour des livres.
Pour l'écriture, préférez les supports effaçables. Pour le calcul, partez toujours du concret.

### Conseils pratiques
- **Enseignement concret :** Boutons, pâte à modeler pour illustrer les mathématiques.
- **Réduire les distracteurs :** Proposez des feuilles de travail épurées.""",
        content_ar="""تعلم القراءة يبدأ بحب الكتاب. في الحساب، يجب الاعتماد على المحسوس قبل الانتقال للرموز المجردة.

### نصائح عملية
- **التعليم الملموس:** استخدم أدوات حسية حقيقية لتبسيط المفاهيم.
- **تقليل المشتتات:** قدم للطفل ورقة عمل خالية من الزينة المفرطة.""",
    ),
    Article(
        id="12",
        axis="educate",
        category="Émotions",
        title="Gérer les émotions et les crises",
        title_ar="إدارة المشاعر والنوبات",
        excerpt="Nommer les émotions et utiliser le baromètre des émotions.",
        content="""Utilisez le « baromètre des émotions » (visages allant de calme à très en colère)
pour aider l'enfant à identifier l'intensité de son ressenti.

### Conseils pratiques
- **Voix calme :** Maintenez un ton très calme pour éviter d'escalader la crise.
- **Coin calme :** Un espace sans stimuli (petite tente, coussin) pour se ressourcer.""",
        content_ar="""يجد الأطفال صعوبة في التعرف على مشاعرهم. استخدم "مقياس المشاعر" بالوجوه الضاحكة والباكية.

### نصائح عملية
- **الهدوء التام:** حافظ على نبرة صوت هادئة.
- **ركن الهدوء:** وفر زاوية مريحة خالية من المثيرات.""",
    ),
    Article(
        id="13",
        axis="educate",
        category="Partenariat",
        title="Collaborer avec la famille et les spécialistes",
        title_ar="التعاون مع الأسرة والمختصين",
        excerpt="L'éducateur au carrefour des partenariats pour une inclusion réussie.",
        content="""L'éducateur doit travailler en réseau avec la famille, l'orthophoniste,
l'ergothérapeute et l'assistant social pour garantir une inclusion réussie.

### Conseils pratiques
- **Cahier de communication :** Un cahier hebdomadaire positif avec les familles.
- **Coordination :** Appliquez les mêmes stratégies que le spécialiste en classe.""",
        content_ar="""يجب التعاون مع العائلة والشبكات الخارجية لضمان دمج مدرسي ناجح.

### نصائح عملية
- **كراس التواصل:** استخدم كراساً أسبوعياً للتواصل مع الأولياء.
- **تنسيق الجهود:** طبق نفس استراتيجيات المختص داخل القسم.""",
    ),
    Article(
        id="14",
        axis="educate",
        category="Observation",
        title="Observer et documenter le développement de l'enfant",
        title_ar="مراقبة تطور الطفل وتوثيقه",
        excerpt="L'observation objective est la base d'un accompagnement de qualité.",
        content="""L'éducateur observe et documente l'évolution de l'enfant, soutient ses intérêts
et renforce ses relations avec les autres enfants.

### Conseils pratiques
- **Observer sans juger :** Notez les intérêts spécifiques et utilisez-les comme levier.
- **Soyez un modèle :** Montrez comment interagir positivement avec l'enfant.""",
        content_ar="""المربي مسؤول عن الإشراف الاجتماعي والعاطفي للطفل داخل المؤسسة.

### نصائح عملية
- **الملاحظة الواعية:** دوّن اهتمامات الطفل الخاصة.
- **كن النموذج:** كن مقداماً ومشجعاً طوال الوقت.""",
    ),
    Article(
        id="15",
        axis="educate",
        category="Projet éducatif",
        title="Construire un Projet Éducatif Individuel (PEI)",
        title_ar="بناء المشروع التربوي الفردي",
        excerpt="L'évaluation initiale pose les bases du PEI adapté au rythme de l'enfant.",
        content="""L'évaluation initiale permet de dresser un portrait précis des capacités de l'enfant
dans tous les domaines. Le PEI en découle avec des objectifs mesurables.

### Conseils pratiques
- **Objectifs réalistes :** Court terme, mesurables et atteignables.
- **Évaluation continue :** Révisez les objectifs régulièrement selon l'évolution.""",
        content_ar="""التقييم الأولي هو حجر الزاوية في التكفل بالطفل. يسمح برسم صورة دقيقة لقدراته.

### نصائح عملية
- **أهداف واقعية:** حدد أهداف قصيرة المدى قابلة للقياس.
- **التقييم المستمر:** راجع الأهداف بانتظام.""",
    ),
    Article(
        id="16",
        axis="educate",
        category="Sensoriel",
        title="Gérer la sensibilité auditive en classe",
        title_ar="التعامل مع الحساسية السمعية في القسم",
        excerpt="Aménagements simples pour réduire la surcharge sensorielle.",
        content="""Si l'enfant est très sensible aux bruits, expliquez l'origine des sons.
Un « coin calme » est indispensable.

### Conseils pratiques
- **Aménagements simples :** Balles de tennis sous les chaises pour réduire le bruit.
- **Casque antibruit :** Autorisez-le lors de surcharges sensorielles importantes.""",
        content_ar="""إذا كان الطفل شديد الحساسية السمعية، قم بتفسير ماهية الأصوات المختلفة.

### نصائح عملية
- **التعديلات البيئية:** ضع كرات تنس أسفل كراسي القسم.
- **الإعفاء عند اللزوم:** اسمح باستخدام سماعات عند الشعور بإرهاق حسي.""",
    ),
    Article(
        id="17",
        axis="educate",
        category="Scénarios sociaux",
        title="Utiliser les scénarios sociaux",
        title_ar="استخدام السيناريوهات الاجتماعية",
        excerpt="Une courte histoire avec l'enfant comme héros pour préparer les situations nouvelles.",
        content="""Un scénario social est une courte histoire (l'enfant en est le héros) qui décrit
comment se comporter dans une situation précise (première journée à l'école, visite chez le médecin).

### Conseils pratiques
- **Écrire ensemble :** Impliquez l'enfant et utilisez de vraies photos de l'école.
- **Lecture anticipatoire :** Lisez le scénario avant que la situation ne se produise.""",
        content_ar="""استخدم السيناريو الاجتماعي (قصة قصيرة الطفل بطلها) لمساعدته على فهم كيفية التصرف.

### نصائح عملية
- **كتابة السيناريو سوياً:** اجعل الطفل بطل القصة.
- **قراءة استباقية:** اقرأ القصة مع الطفل قبل حدوث الموقف.""",
    ),
    Article(
        id="18",
        axis="educate",
        category="Pédagogie",
        title="Adapter ses consignes et son langage",
        title_ar="تكييف التعليمات واللغة",
        excerpt="Des consignes courtes, simples et accompagnées de supports visuels.",
        content="""N'évaluez pas l'enfant sur les mêmes bases que ses camarades.
Utilisez un langage simple, des phrases courtes et découpez les tâches.

### Conseils pratiques
- **Une consigne à la fois :** "Ouvre le livre." Pause. "Prends ton crayon."
- **Support visuel permanent :** Accompagnez chaque consigne orale d'un geste ou d'une image.""",
        content_ar="""لا تقيم الطفل على نفس القواعس التي تفرضها على زملائه.
استعمل كلمات بسيطة وابتعد عن الجمل الطويلة.

### نصائح عملية
- **تعليمات مبسطة:** قدم تعليماً واحداً قصيراً في كل مرة.
- **الدعم البصري الدائم:** رافق كلماتك بإشارة من يدك.""",
    ),
    Article(
        id="19",
        axis="educate",
        category="Relaxation",
        title="Introduire des techniques de relaxation",
        title_ar="تقديم تقنيات الاسترخاء",
        excerpt="Exercices de respiration et activités apaisantes pour réduire le stress.",
        content="""Apprenez à l'enfant des techniques de relaxation : exercices de respiration,
allongement tranquille, ou musique douce. Commencez par des activités courtes.

### Conseils pratiques
- **Jeux de respiration :** Souffler des bulles de savon pour apprendre la respiration profonde.
- **Routine de relaxation :** 5 minutes de détente dans le programme quotidien.""",
        content_ar="""يمكن للمربي تعليم الطفل تقنيات الاسترخاء لتقليل التوتر.

### نصائح عملية
- **تمارين التنفس:** استخدم نفخ فقاعات الصابون للتدريب.
- **روتين الاسترخاء:** اجعل 5 دقائق من الاسترخاء جزءاً ثابتاً من اليوم.""",
    ),
    Article(
        id="20",
        axis="educate",
        category="Inclusion",
        title="Favoriser l'inclusion par le jeu collectif",
        title_ar="تعزيز الاندماج عبر اللعب الجماعي",
        excerpt="Des activités partagées pour développer les habiletés sociales.",
        content="""Encouragez l'enfant à réaliser des tâches avec un camarade (projet artistique, jeu de balle).
Expliquez clairement ce que l'interaction sociale implique.

### Conseils pratiques
- **Le camarade aidant :** Choisissez un enfant calme et coopératif comme "binôme" dans certaines activités.
- **Jeu guidé :** Établissez des règles très claires et intervenez positivement si nécessaire.""",
        content_ar="""شجع الطفل على القيام بمهام مشتركة مع زميل.

### نصائح عملية
- **الرفيق الداعم:** اختر طفلاً هادئاً ليكون "زميل مساعدة".
- **اللعب الموجه:** حدد قواعد لعب واضحة جداً.""",
    ),
]

# ── Combined list ─────────────────────────────────────────────────────────────

ALL_ARTICLES: list[Article] = INFORME_ARTICLES + EDUCATE_ARTICLES
