# THE HOUSE — EXPERIENCE BIBLE & SPECIFICATIONS
## Arquitectura de Experiencia Digital Inmersiva y Parámetros Técnico-Narrativos
### JD Group AXM · Armenia, Quindío

---

## 1. CORE PHILOSOPHY & ARCO EMOCIONAL
El proyecto NO es un sitio web tradicional ni un portal de empleo. Es un **Digital Experience Film** que opera como una residencia privada de alta costura y hospitalidad de ultra-lujo.

El arco emocional gobernante se articula en ocho actos inquebrantables:
$$\text{PRESENCIA} \longrightarrow \text{CURIOSIDAD} \longrightarrow \text{TENSIÓN} \longrightarrow \text{DESCUBRIMIENTO} \longrightarrow \text{INTIMIDAD} \longrightarrow \text{DESEO} \longrightarrow \text{ANTICIPACIÓN} \longrightarrow \text{INVITACIÓN}$$

---

## 2. MATRIZ DE LOS 8 ACTOS NARRATIVOS

| Acto Narrativo | Dominio Emocional | Estado Lumínico | Comportamiento de Scroll / Cámara | Pistas Visuales y Contenido |
| :--- | :--- | :--- | :--- | :--- |
| **ACT I: Arrival** | Presencia / Misterio | Oscuridad profunda (`#080807`), destello orgánico | Bloqueo inicial; micro-parallax al cursor ($2\text{px} - 8\text{px}$) | Fotografía en penumbra, respiración del fondo ($0.05\text{Hz}$), ritual "ENTER". |
| **ACT II: The House** | Curiosidad | Apertura focal, luz cenital tenue | Transición de entrada profunda (eje Z) | Siluetas arquitectónicas, fragmentos del manifiesto. |
| **ACT III: The Art** | Tensión | Contraste elevado, claroscuro dinámico | Scroll Pacing no lineal (aceleración/desaceleración) | Fotografía editorial con foco selectivo y grano analógico. |
| **ACT IV: The Talent** | Descubrimiento | Temperatura cálida ($3200\text{K}$) | Desplazamiento lateral controlado y revelación progresiva | Retratos interactivos de autor con proximidad al cursor. |
| **ACT V: The Journey** | Intimidad | Claridad difusa, gradientes suaves | Desplazamiento lento con alta fricción ($\mu = 0.85$) | Relatos de transformación que emergen mediante masking. |
| **ACT VI: The Private** | Deseo & Seguridad | Oscuridad íntima, iluminación puntual | Micro-scroll estático con fijación (*pinning*) de escena | Geobloqueo tangible nacional (IP/ASN), sede anónima en Armenia. |
| **ACT VII: The Possibility**| Anticipación | Expansión luminosa, tonos neutros suaves | Flujo continuo con inercia prolongada | Simulador de autonomía en USD/COP con TRM en tiempo real. |
| **ACT VIII: The Invitation**| Invitación / Claridad| Luz limpia, alto contraste tipográfico | Scroll guiado hacia punto focal central | Formulario de entrevista privada con radicado `AXM-XXXXXX`. |

---

## 3. EL SISTEMA NERVIOSO VISUAL (PARÁMETROS FÍSICOS & SHADERS)

* **Frecuencia de Respiración ($f_b$):** Modulación sinusoidal continua entre $0.05\text{Hz}$ (reposo) y $0.25\text{Hz}$ (pico).
* **Inercia de Masa ($m$):** Elementos estructurales ($m = 10.0$, lentos y nobles); elementos tipográficos y micro-detalles ($m = 1.0$, reactivos).
* **Coeficiente de Fricción ($\mu$):** Control de amortiguamiento de cámara desde $\mu = 0.35$ (descubrimiento fluido) hasta $\mu = 0.85$ (intimidad y pausa).
* **Temperatura de Color ($T_c$):** Interpolación en espacio de color Oklab desde $2200\text{K}$ (boudoir cálido) hasta $5500\text{K}$ (luz natural de estudio).
* **Profundidad Óptica ($Z$):** 4 planos de profundidad desfasados: Fondo WebGL ($Z_0$), Haze atmosférico ($Z_1$), Fotografía ($Z_2$) y Tipografía ($Z_3$).

---

## 4. MOTOR DE SCROLL CINEMÁTICO (LENIS 1.X + GSAP SCROLLTRIGGER)
* **Integración Unificada:** Bucle RAF sincronizado a través de `gsap.ticker` con `lagSmoothing(0)` y `lerp: 0.07` para inercia aristocrática.
* **Scroll Pacing:** Transiciones elásticas donde la velocidad del usuario modula la apertura de máscaras de imagen y la tensión del shader.

---

## 5. REGLAS DE COMPONENTES & RESTRICCIONES ABSOLUTAS
1. **Fotografía:** Se prohíben etiquetas `<img>` estáticas planas. Todas las imágenes principales deben poseer máscaras de recorte, micro-parallax y foco dinámico.
2. **Cero Ruido Comercial:** Quedan estrictamente prohibidos gradientes de oro chillones, luces de neón baratas, pop-ups de falsa urgencia ("últimos cupos") o estética de catálogo de venta.
3. **Privacidad en la Vida Real:** Inclusión obligatoria del **Botón de Camuflaje Rápido (`Tecla ESC`)** para ocultar la pantalla instantáneamente.
4. **Accesibilidad Kinésica:** Soporte total de `@media (prefers-reduced-motion: reduce)` con desactivación de shaders y transiciones estáticas.
