# HANDOFF — JD GROUP AXM
## Protocolo de Transferencia y Continuidad Operativa

---

### 1. Resumen del Proyecto
* **Nombre:** JD Group AXM (DJGROUP)
* **Ubicación:** Armenia, Quindío, Colombia
* **Concepto Rector:** *Sensory Luxury & Digital Intimacy*
* **Entorno de Trabajo:** `C:\Users\prada\Documents\CENTRO DE PAGINAS\DJGROUP`
* **Estado Actual:** `VERIFIED_AND_TESTED / PRODUCTION-READY`

---

### 2. Mapa de Archivos y Componentes

```text
DJGROUP/
├── app.py                      # Orquestador principal de la plataforma
├── requirements.txt            # Librerías de Python requeridas
├── run_app.bat                 # Lanzador rápido de un clic para Windows
├── README.md                   # Documentación general y guía de uso
├── PROJECT_BRIEF.md            # Resumen estratégico y de branding
├── PROJECT_STATE.md            # Estado actual y matriz de decisiones
├── DECISION_LOG.md             # Registro histórico de decisiones técnicas
├── SOURCE_REGISTRY.md          # Registro y validación de fuentes de información
├── AUDIT_REPORT.md             # Reporte de auditoría multicriterio (G1-G10)
├── HANDOFF.md                  # Este documento de transferencia
├── data/
│   └── leads_vault.json        # Bóveda de postulaciones de talento (Habeas Data)
├── src/
│   ├── __init__.py
│   ├── theme.py                # M00: Sistema de diseño, tokens y CSS
│   ├── services/
│   │   ├── __init__.py
│   │   ├── data_service.py     # M04: Servicio de TRM y fórmulas financieras
│   │   └── lead_service.py     # M03: Bóveda y persistencia de postulaciones
│   └── components/
│       ├── __init__.py
│       ├── age_gate.py         # M01: Puerta restrictiva de mayoría de edad (+18)
│       ├── header.py           # M01/M02: Header con monograma y switcher
│       ├── calculator.py       # M02: Simulador interactivo de ingresos
│       ├── sets_tour.py        # M02: Tour virtual de sets de Armenia
│       ├── corporate_panel.py  # M02: Portal corporativo e infraestructura 4K
│       ├── lead_form.py        # M03: Formulario cifrado de postulación
│       └── admin_panel.py      # M02/M03: Panel de control de postulaciones
└── tests/
    └── test_platform.py        # Suite de pruebas unitarias automatizadas
```

---

### 3. Procedimiento para Iniciar el Servidor

```bash
# Opción 1: Ejecutar directamente el archivo por lotes en Windows
run_app.bat

# Opción 2: Ejecutar manualmente desde la terminal
streamlit run app.py
```

---

### 4. Próximos Pasos para Fase Productiva
1. **Fotografía Editorial:** Reemplazar las URLs provisionales de Unsplash en `src/components/sets_tour.py` por los renders/fotografías finales de las sedes en Armenia.
2. **Conector de Mensajería:** Configurar la API oficial de WhatsApp Business o Webhook en `src/services/lead_service.py` para alertas automáticas a los monitores en turno.
3. **Despliegue en la Nube:** Si se requiere acceso web público, empaquetar en contenedor Docker o desplegar en Streamlit Community Cloud / Google Cloud Run.
