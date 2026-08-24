# IMPLEMENTATION PLAN: THE HOUSE — DIGITAL EXPERIENCE FILM
## Arquitectura Técnica de 8 Actos para Google Antigravity

---

### FASE 1: ARQUITECTURA & SISTEMA NERVIOSO VISUAL
* [x] **1.1** Crear la especificación formal `docs/EXPERIENCE_BIBLE.md` con los parámetros físicos globales ($f_b$, $m$, $\mu$, $T_c$, $Z$).
* [x] **1.2** Configurar el lienzo WebGL full-screen con Three.js y el Fragment Shader GLSL de Simplex Noise con modulación dinámica de uniforms (`uTime`, `uActBreathingFreq`, `uTensionLevel`, `uCursor`, `uColorBase`, `uColorAccent`).
* [x] **1.3** Sincronizar el motor de inercia Lenis 1.x y GSAP ScrollTrigger a través del GSAP Ticker con `lagSmoothing(0)` y `lerp: 0.07`.

---

### FASE 2: DESARROLLO DE LOS 8 ACTOS CINEMÁTICOS
* [x] **2.1 ACT I (Arrival — Presencia / Misterio):** Umbral ciego, latencia lumínica, respiración en $0.05\text{Hz}$, micro-parallax y ritual de activación espacial "ENTER THE HOUSE".
* [x] **2.2 ACT II (The House — Curiosidad):** Apertura de diafragma, barrido espacial en eje Z y siluetas arquitectónicas de las suites en Armenia.
* [x] **2.3 ACT III (The Art — Tensión):** Scroll pacing no lineal, claroscuro dinámico y foco selectivo en producción editorial.
* [x] **2.4 ACT IV (The Talent — Descubrimiento):** Temperatura cálida ($3200\text{K}$), galería en revista de moda con retratos interactivos de proximidad.
* [x] **2.5 ACT V (The Journey — Intimidad):** Historias de transformación con masking tipográfico y alta fricción de scroll.
* [x] **2.6 ACT VI (The Private — Deseo & Seguridad):** *Privacy as the Ultimate Luxury*, geobloqueo tangible nacional (IP/ASN) y sede anónima sin avisos exteriores.
* [x] **2.7 ACT VII (The Possibility — Anticipación):** Autonomía financiera en USD/COP con TRM oficial bancaria en vivo.
* [x] **2.8 ACT VIII (The Invitation — Claridad):** Silencio visual, formulario de entrevista privada en 3 pasos con Habeas Data (Ley 1581/2012), entrega de radicado `AXM-XXXXXX` y WhatsApp Private Concierge.

---

### FASE 3: SISTEMA DE MEMORIA VISUAL & ADAPTABILIDAD
* [x] **3.1 Session Visual Memory:** Registro reactivo del tiempo de atención en talento y propagación de variables implícitas hacia actos posteriores.
* [x] **3.2 Fotografía con Comportamiento:** Micro-expansión respiratoria, foco dinámico y distorsión sutil por velocidad de scroll.
* [x] **3.3 Protocolo Stealth:** Botón de Camuflaje Rápido de emergencia (`Tecla ESC`) con restauración instantánea.

---

### FASE 4: QA, RENDIMIENTO & ACCESIBILIDAD
* [x] **4.1** Tasa de cuadros objetivo: 60 FPS estables en GPU.
* [x] **4.2** Compatibilidad nativa con `@media (prefers-reduced-motion: reduce)`.
* [x] **4.3** Cero dependencias rotas y compilación Python/Streamlit 100% libre de errores.
