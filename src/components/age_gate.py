"""
MÓDULO 01 (M01) — Compliance & Security Gateway (+18 Gate)
JD Group AXM · Control de Acceso y Cumplimiento Normativo
"""

import streamlit as st

def render_age_gate() -> bool:
    """
    Verifica y gestiona la pantalla restrictiva de mayoría de edad (+18).
    Retorna True si el usuario está validado, detiene el flujo si no lo está.
    """
    if "verified_age" not in st.session_state:
        st.session_state.verified_age = False

    if not st.session_state.verified_age:
        st.markdown("<div style='text-align: center; margin-top: 80px;'>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1543536448-d209d2d13a1c?q=80&w=300", width=150)
        st.markdown("<h1 style='font-size: 3em;'>JD GROUP AXM</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #F4F4F6;'>SENSORY LUXURY & DIGITAL INTIMACY</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.15em; color: #888;'>Armenia, Quindío · Plataforma Profesional para Adultos (+18)</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1.5, 2, 1.5])
        with col2:
            st.markdown(
                "<div style='text-align: center; padding: 24px; border: 1px solid #D4AF37; border-radius: 12px; background-color: #121216;'>"
                "<p style='font-size: 1.1em; color: #F4F4F6; margin-bottom: 20px;'>"
                "¿Eres mayor de 18 años y aceptas el ingreso a esta plataforma de entretenimiento y gestión digital exclusiva?"
                "</p>",
                unsafe_allow_html=True
            )
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button("SÍ, INGRESAR (+18)", key="btn_age_yes"):
                    st.session_state.verified_age = True
                    st.rerun()
            with c_btn2:
                if st.button("NO, SALIR", key="btn_age_no"):
                    st.error("Acceso restringido únicamente a mayores de edad.")
                    
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.stop()
        return False
        
    return True
