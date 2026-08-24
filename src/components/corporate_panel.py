"""
MÓDULO 02 — Plataforma Corporativa & Producción Audiovisual (Ruta VIP)
JD Group AXM · Portal Institucional
"""

import streamlit as st

def render_corporate_panel():
    """Renderiza el portal institucional para inversionistas y aliados estratégicos."""
    st.markdown("<h2 style='font-size: 2.2em;'>Plataforma Corporativa & Producción Audiovisual</h2>", unsafe_allow_html=True)
    st.write(
        "JD Group AXM no es solo un estudio de transmisión; es una productora de experiencias multimedia "
        "e intimidad digital de alto rendimiento orientada a mercados internacionales de alta gama."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<div class='vip-card'>"
            "<h4>⚙️ Tecnología de Transmisión de Vanguardia</h4>"
            "<ul>"
            "<li>Cámaras réflex profesionales con transmisión nativa 4K.</li>"
            "<li>Aislamiento acústico de alto rendimiento en cada set temático.</li>"
            "<li>Redes de fibra óptica simétrica dedicada con balanceo de carga LAN/WAN.</li>"
            "<li>Maquillaje y estilismo profesional de Portrait Editorial en sede.</li>"
            "</ul>"
            "</div>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            "<div class='vip-card'>"
            "<h4>🤝 Cumplimiento Normativo y Respaldo Legal</h4>"
            "<ul>"
            "<li>Estructura jurídica legalmente constituida en Armenia, Quindío.</li>"
            "<li>Certificaciones de retención y asesoría tributaria integral.</li>"
            "<li>Apoyo psicológico gratuito integrado (Convenios de Bienestar).</li>"
            "<li>Monitores bilingües y soporte técnico presencial y remoto 24/7.</li>"
            "</ul>"
            "</div>",
            unsafe_allow_html=True
        )
        
    st.markdown("### 🏆 Nuestro Estándar Operativo")
    st.write(
        "Nos alineamos con las mejores prácticas internacionales de formalización y dignificación del rol de "
        "Creadora de Contenido. No competimos con esquemas informales; establecemos el estándar de lujo en el Quindío."
    )
    
    st.info("💡 Para consultas de alianzas corporativas o formalización de nuevos estudios, contáctanos en: vinculacion@jdgroupaxm.com")
