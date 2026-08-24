"""
MÓDULO 02/03 — Panel de Gestión y Control para Directores
JD Group AXM · Armenia, Quindío
"""

import streamlit as st
import pandas as pd
from src.services.lead_service import get_all_leads

def render_admin_panel():
    """Panel de auditoría y gestión de postulaciones para la dirección de JD Group AXM."""
    st.markdown("## 🔐 Panel de Dirección y Gestión de Talento")
    st.markdown("<p style='color: #888;'>Acceso reservado para directores y monitores de sede en Armenia, Quindío.</p>", unsafe_allow_html=True)
    
    leads = get_all_leads()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"<div class='vip-card' style='text-align: center;'>"
            f"<h5 style='color: #aaa; margin: 0;'>Total Postulaciones</h5>"
            f"<h2 style='color: #D4AF37; margin: 8px 0;'>{len(leads)}</h2>"
            f"</div>",
            unsafe_allow_html=True
        )
    with col2:
        sede_count = sum(1 for l in leads if "Sede" in l.get("modalidad", ""))
        st.markdown(
            f"<div class='vip-card' style='text-align: center;'>"
            f"<h5 style='color: #aaa; margin: 0;'>Interés Sede Presencial</h5>"
            f"<h2 style='color: #D946EF; margin: 8px 0;'>{sede_count}</h2>"
            f"</div>",
            unsafe_allow_html=True
        )
    with col3:
        sat_count = sum(1 for l in leads if "Satélite" in l.get("modalidad", ""))
        st.markdown(
            f"<div class='vip-card' style='text-align: center;'>"
            f"<h5 style='color: #aaa; margin: 0;'>Interés Satélite / Remoto</h5>"
            f"<h2 style='color: #8B5CF6; margin: 8px 0;'>{sat_count}</h2>"
            f"</div>",
            unsafe_allow_html=True
        )
        
    st.markdown("### 📋 Registro Inmutable de Bóveda de Talento (Habeas Data)")
    
    if not leads:
        st.info("No hay postulaciones registradas en la bóveda por el momento.")
    else:
        df = pd.DataFrame(leads)
        display_df = df[["radicado_id", "timestamp", "nombre", "whatsapp", "edad", "ciudad", "modalidad", "horario", "estado_gestion"]]
        st.dataframe(display_df, use_container_width=True)
        
        st.download_button(
            label="📥 Exportar Bóveda de Leads (CSV Cifrado)",
            data=display_df.to_csv(index=False).encode('utf-8'),
            file_name="jdgroup_leads_vault_axm.csv",
            mime="text/csv"
        )
