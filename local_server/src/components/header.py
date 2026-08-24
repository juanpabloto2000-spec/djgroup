"""
MÓDULO 01/02 — Header & Dual-Funnel Switcher (Actualizado con Modo Dirección)
JD Group AXM · Monograma de Marca y Selector de Perfiles
"""

import streamlit as st

def render_header() -> str:
    """
    Renderiza el encabezado principal con monograma 'JD GROUP AXM' y el selector trifronte.
    Retorna la ruta seleccionada.
    """
    col_logo, col_menu = st.columns([2.5, 2.5])
    
    with col_logo:
        st.markdown(
            "<h1 style='margin: 0; display: flex; align-items: center; gap: 10px;'>"
            "<span style='border: 2px solid #D4AF37; padding: 4px 14px; border-radius: 6px; font-family: Serif; color: #D4AF37;'>JD</span> "
            "<span style='font-size: 0.8em; letter-spacing: 4px; font-weight: 300; color: #F4F4F6;'>GROUP</span> "
            "<span style='font-size: 0.55em; background-color: #D946EF; color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold;'>AXM</span>"
            "</h1>",
            unsafe_allow_html=True
        )
        st.markdown("<p style='font-size: 0.85em; color: #888; margin: 2px 0 0 0;'>Sensory Luxury & Digital Intimacy · Armenia, Quindío</p>", unsafe_allow_html=True)
        
    with col_menu:
        ruta = st.radio(
            "Selecciona tu perfil de navegación:",
            options=["Ruta Talento (Postulantes)", "Ruta VIP (Institucional)", "Panel Dirección (Admin)"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
    st.markdown("---")
    return ruta
