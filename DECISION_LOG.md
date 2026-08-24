# DECISION LOG — JD GROUP AXM
## Registro Formal de Decisiones Arquitectónicas y de Negocio

---

### DEC-001: Arquitectura Desacoplada Modular (LEGO Pattern)
* **Fecha:** 2026-08-19
* **Estado:** `ACTIVE`
* **Nivel de Certeza:** `C5 (Verificado)`
* **Decisión:** Segmentar la aplicación en módulos independientes dentro de `/src` (`theme`, `services`, `components`) orquestados por `app.py`.
* **Motivo:** Evitar código monolítico y permitir que cada componente pueda ser mantenido, probado o reemplazado sin efectos colaterales.
* **Módulos Afectados:** M00, M01, M02, M03, M04, M05.

---

### DEC-002: Dirección de Arte "Super Dark Mode & Sensory Luxury"
* **Fecha:** 2026-08-19
* **Estado:** `ACTIVE`
* **Nivel de Certeza:** `C4 (Confirmado por Especificación)`
* **Decisión:** Implementar paleta de color estricta: Negro Carbón (`#0A0A0C`), Oro Champán (`#C5A059` / `#D4AF37`), Neón Magenta (`#D946EF`), Blanco Humo (`#F4F4F6`) y Púrpura Eléctrico (`#8B5CF6`).
* **Motivo:** Transmitir exclusividad tipo *Boutique VIP*, desestigmatizar la industria en Armenia (Quindío) y optimizar para visualización nocturna.
* **Módulos Afectados:** M00, M01, M02.

---

### DEC-003: Arquitectura Multiembuto (Triple Funnel)
* **Fecha:** 2026-08-19
* **Estado:** `ACTIVE`
* **Nivel de Certeza:** `C5 (Verificado)`
* **Decisión:** Proveer tres rutas de navegación:
  1. *Ruta Talento:* Reclutamiento de streamers, geobloqueo, calculadora financiera y postulación.
  2. *Ruta VIP:* Portal corporativo, especificaciones técnicas 4K y cumplimiento normativo.
  3. *Panel Dirección:* Monitoreo confidencial de aspirantes y métricas para directores en sede.
* **Motivo:** Separar las audiencias comerciales, institucionales y operativas en una sola plataforma integrada.
* **Módulos Afectados:** M01, M02, M03.

---

### DEC-004: Bóveda Local de Datos con Trazabilidad Habeas Data
* **Fecha:** 2026-08-19
* **Estado:** `ACTIVE`
* **Nivel de Certeza:** `C5 (Verificado)`
* **Decisión:** Almacenar postulaciones en formato estructurado local (`data/leads_vault.json`) con generación de códigos de radicado confidenciales (`AXM-XXXXXX`) y registro explícito de aceptación de la Ley 1581 de 2012 (Habeas Data).
* **Motivo:** Garantizar privacidad, confidencialidad y cumplimiento legal desde la fase interactiva.
* **Módulos Afectados:** M03.
