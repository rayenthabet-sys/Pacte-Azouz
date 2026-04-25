"""
data/videos.py — All video content for Auti-Aura.

Each video is bilingual (French + Arabic title and description).
URLs are YouTube embed links.
"""

from backend.models import Video

ALL_VIDEOS: list[Video] = [
    Video(
        id="v1",
        title="Comprendre l'autisme en 3 minutes",
        title_ar="فهم التوحد في 3 دقائق",
        url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        description="Une présentation simple et claire du Trouble du Spectre de l'Autisme pour les parents.",
        description_ar="عرض بسيط وواضح لطيف اضطراب التوحد للآباء.",
        category="Sensibilisation",
    ),
    Video(
        id="v2",
        title="La communication alternative et améliorée (CAA)",
        title_ar="التواصل البديل والمعزز",
        url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        description="Comment utiliser les pictogrammes, les tablettes et les gestes pour aider l'enfant à communiquer.",
        description_ar="كيفية استخدام الصور والأجهزة اللوحية لمساعدة الطفل على التواصل.",
        category="Communication",
    ),
    Video(
        id="v3",
        title="Témoignage : Parcours d'un enfant autiste à l'école inclusive",
        title_ar="شهادة: مسار طفل توحدي في المدرسة الدامجة",
        url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        description="Une famille tunisienne partage son expérience avec l'intégration scolaire.",
        description_ar="عائلة تونسية تشارك تجربتها مع الإدماج المدرسي.",
        category="Témoignages",
    ),
    Video(
        id="v4",
        title="Les thérapies comportementales : ABA et TEACCH",
        title_ar="العلاجات السلوكية: ABA و TEACCH",
        url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        description="Présentation des deux approches thérapeutiques les plus utilisées avec les enfants TSA.",
        description_ar="عرض للمقاربتين العلاجيتين الأكثر استخداماً مع أطفال طيف التوحد.",
        category="Thérapies",
    ),
    Video(
        id="v5",
        title="Gérer une crise sensorielle : Guide pour les éducateurs",
        title_ar="التعامل مع الأزمة الحسية: دليل للمربين",
        url="https://www.youtube.com/embed/dQw4w9WgXcQ",
        description="Techniques pratiques pour aider un enfant en surcharge sensorielle en classe.",
        description_ar="تقنيات عملية لمساعدة طفل يعاني من عبء حسي زائد في الفصل.",
        category="Gestion des crises",
    ),
]
