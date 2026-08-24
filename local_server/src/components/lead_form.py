"""
MÓDULO 03 — Formulario de Postulación Cifrado & Habeas Data (Actualizado con Bóveda)
JD Group AXM · Captura Segura de Talento en el Eje Cafetero
"""

import streamlit as st
import time
from src.services.lead_service import save_lead

def render_lead_form():
    """Renderiza el formulario de postulación seguro conectado a la bóveda de datos."""
    st.markdown("### ✉️ Formulario de Postulación de Talento (Cifrado de Extremo a Extremo)")
    st.write(
        "Completa este formulario confidencial de precandidata. Un monitor/psicólogo de nuestro equipo en Armenia "
        "se pondrá en contacto contigo de manera discreta vía WhatsApp."
    )
    
    with st.form("form_postulacion_talento", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre o Nombre Artístico (Placeholder/Provisional):", placeholder="Ej: Isabella", key="lead_nombre")
            whatsapp = st.text_input("WhatsApp / Teléfono de Contacto:", placeholder="Ej: +57 300 123 4567", key="lead_whatsapp")
            edad = st.number_input("Edad Confirmada (Mínimo 18 años):", min_value=18, max_value=60, value=20, key="lead_edad")
        with col2:
            ciudad = st.selectbox(
                "Ciudad de Residencia:",
                options=["Armenia", "Calarcá", "Circasia", "Salento", "Montenegro", "La Tebaida", "Quimbaya", "Otra (Eje Cafetero)"],
                key="lead_ciudad"
            )
            modalidad = st.selectbox(
                "Modalidad de Interés:",
                options=["Sede Física (Armenia)", "Satélite (Casa)", "Por definir"],
                key="lead_modalidad"
            )
            horario = st.selectbox(
                "Horario preferido:",
                options=["Mañana (6 AM - 2 PM)", "Tarde (2 PM - 10 PM)", "Noche (10 PM - 6 AM)", "Flexible"],
                key="lead_horario"
            )
            
        comentarios = st.text_area("Cuéntanos sobre ti (Idiomas, metas o inquietudes):", placeholder="Escribe tus dudas o si cuentas con experiencia previa...", key="lead_comentarios")
        
        habeas_data = st.checkbox("Autorizo el tratamiento de mis datos personales de acuerdo con la política de Habeas Data de JD Group AXM y confirmo que soy mayor de 18 años.", key="lead_habeas")
        
        submit_btn = st.form_submit_button("ENVIAR POSTULACIÓN CONFIDENCIAL")
        
        if submit_btn:
            if not habeas_data:
                st.error("⚠️ Debes aceptar la autorización de Habeas Data y confirmar mayoría de edad para enviar tu postulación.")
            elif not nombre.strip() or not whatsapp.strip():
                st.error("⚠️ Por favor completa los campos obligatorios de Nombre y WhatsApp.")
            else:
                with st.spinner("Cifrando datos de postulación y registrando en bóveda segura..."):
                    time.sleep(1.2)
                    record = save_lead(
                        nombre=nombre,
                        whatsapp=whatsapp,
                        edad=edad,
                        ciudad=ciudad,
                        modalidad=modalidad,
                        horario=horario,
                        comentarios=comentarios,
                        habeas_data=habeas_data
                    )
                st.success(
                    f"✅ ¡Postulación enviada con éxito!\n\n"
                    f"**Código de Radicado Confidencial:** `{record['radicado_id']}`\n\n"
                    f"Tu proceso está blindado y es 100% confidencial. Nos comunicaremos contigo en las próximas 2 horas hábiles."
                )
